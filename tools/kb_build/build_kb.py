#!/usr/bin/env python3
"""
Build & publish an "extended-mind" knowledge base:
- Reads Markdown from selected folders
- Chunks by headings + length limits
- Embeds chunks (SentenceTransformers)
- Builds FAISS index
- Publishes artifacts to Hugging Face Dataset repo

Designed for: small/medium repos (tens to a few hundreds of md files).
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Dict, Tuple, Optional

import numpy as np
from tqdm import tqdm

# Heavy deps (import lazily-ish, but keep simple)
import faiss  # type: ignore
from sentence_transformers import SentenceTransformer  # type: ignore
from huggingface_hub import HfApi


MD_EXT = {".md", ".markdown"}


@dataclass
class Chunk:
    chunk_id: str
    source_path: str
    rel_path: str
    title_path: List[str]
    text: str
    sha1: str


def utc_now_iso() -> str:
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def sha1_text(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def strip_frontmatter(md: str) -> str:
    """
    Remove YAML frontmatter if present at the top of file:
    ---
    ...
    ---
    """
    if md.startswith("---"):
        # Match first frontmatter block only
        m = re.match(r"^---\s*\n.*?\n---\s*\n", md, flags=re.DOTALL)
        if m:
            return md[m.end() :]
    return md


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", flags=re.MULTILINE)


def iter_sections(md: str) -> List[Tuple[List[str], str]]:
    """
    Split markdown into sections by headings.
    Returns list of (title_path, section_text) where section_text includes content under that heading.
    """
    md = strip_frontmatter(md).strip()
    if not md:
        return []

    matches = list(HEADING_RE.finditer(md))
    if not matches:
        return [([], md)]

    sections: List[Tuple[List[str], str]] = []

    # Track heading stack
    stack: List[Tuple[int, str]] = []

    def current_title_path() -> List[str]:
        return [t for (_lvl, t) in stack]

    for i, m in enumerate(matches):
        lvl = len(m.group(1))
        title = m.group(2).strip()

        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md)
        body = md[start:end].strip()

        # Update stack to this heading level
        while stack and stack[-1][0] >= lvl:
            stack.pop()
        stack.append((lvl, title))

        sections.append((current_title_path(), body))

    return sections


def chunk_text(
    title_path: List[str],
    section_text: str,
    max_chars: int,
    overlap_chars: int,
) -> List[Tuple[List[str], str]]:
    """
    Further chunk a section by max_chars with overlap, without trying to be too clever.
    Keeps title_path same for all derived chunks.
    """
    t = section_text.strip()
    if len(t) <= max_chars:
        return [(title_path, t)]

    chunks: List[Tuple[List[str], str]] = []
    i = 0
    while i < len(t):
        j = min(i + max_chars, len(t))
        piece = t[i:j].strip()
        if piece:
            chunks.append((title_path, piece))
        if j >= len(t):
            break
        i = max(0, j - overlap_chars)

    return chunks


def collect_md_files(root: Path, include_dirs: List[str]) -> List[Path]:
    files: List[Path] = []
    for d in include_dirs:
        p = (root / d).resolve()
        if not p.exists():
            continue
        for fp in p.rglob("*"):
            if fp.is_file() and fp.suffix.lower() in MD_EXT:
                files.append(fp)
    # Stable sort for determinism
    files.sort(key=lambda x: str(x).lower())
    return files


def build_chunks(
    repo_root: Path,
    include_dirs: List[str],
    max_chars: int,
    overlap_chars: int,
) -> List[Chunk]:
    md_files = collect_md_files(repo_root, include_dirs)
    chunks: List[Chunk] = []

    for fp in tqdm(md_files, desc="Reading & chunking"):
        rel_path = fp.relative_to(repo_root).as_posix()
        raw = read_text(fp)
        sections = iter_sections(raw)

        if not sections:
            continue

        derived: List[Tuple[List[str], str]] = []
        for title_path, section_text in sections:
            derived.extend(chunk_text(title_path, section_text, max_chars, overlap_chars))

        for idx, (title_path, text) in enumerate(derived):
            sha = sha1_text(f"{rel_path}::{idx}::{text}")
            chunk_id = sha  # stable id
            chunks.append(
                Chunk(
                    chunk_id=chunk_id,
                    source_path=str(fp),
                    rel_path=rel_path,
                    title_path=title_path,
                    text=text,
                    sha1=sha,
                )
            )

    return chunks


def embed_chunks(
    chunks: List[Chunk],
    model_name: str,
    batch_size: int,
) -> np.ndarray:
    model = SentenceTransformer(model_name)
    texts = [c.text for c in chunks]
    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,  # cosine-friendly
    )
    emb = np.asarray(embeddings, dtype="float32")
    return emb


def build_faiss_index(emb: np.ndarray) -> faiss.Index:
    """
    Since embeddings are normalized, inner product ~= cosine similarity.
    Use IndexFlatIP for simplicity.
    """
    dim = emb.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(emb)
    return index


def write_artifacts(out_dir: Path, chunks: List[Chunk], emb: np.ndarray, index: faiss.Index, build_info: dict) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    chunks_path = out_dir / "chunks.jsonl"
    with chunks_path.open("w", encoding="utf-8") as f:
        for c in chunks:
            row = {
                "chunk_id": c.chunk_id,
                "rel_path": c.rel_path,
                "title_path": c.title_path,
                "text": c.text,
                "sha1": c.sha1,
            }
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    np.save(out_dir / "embeddings.npy", emb)

    faiss.write_index(index, str(out_dir / "faiss.index"))

    with (out_dir / "build_info.json").open("w", encoding="utf-8") as f:
        json.dump(build_info, f, ensure_ascii=False, indent=2)


def publish_to_hf(dataset_repo: str, out_dir: Path, token: str, commit_message: str) -> None:
    api = HfApi(token=token)
    api.upload_folder(
        repo_id=dataset_repo,
        repo_type="dataset",
        folder_path=str(out_dir),
        path_in_repo=".",
        commit_message=commit_message,
    )


def get_git_sha() -> Optional[str]:
    # Avoid importing subprocess if not needed
    import subprocess

    try:
        sha = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
        return sha
    except Exception:
        return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".", help="Path to extended-mind repo root")
    parser.add_argument("--include-dirs", default="manifest,patterns,adr,docs", help="Comma-separated dirs to index")
    parser.add_argument("--out-dir", default="dist/kb", help="Output directory for artifacts")
    parser.add_argument("--dataset-repo", required=True, help="HF dataset repo, e.g. utemix/extended-mind-kb")
    parser.add_argument("--hf-token-env", default="HF_TOKEN", help="Env var name that holds HF token")
    parser.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2", help="Embedding model name")
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--max-chars", type=int, default=1800)
    parser.add_argument("--overlap-chars", type=int, default=200)
    args = parser.parse_args()

    token = os.environ.get(args.hf_token_env)
    if not token:
        print(f"ERROR: missing HF token in env var: {args.hf_token_env}", file=sys.stderr)
        return 2

    repo_root = Path(args.repo_root).resolve()
    include_dirs = [x.strip() for x in args.include_dirs.split(",") if x.strip()]
    out_dir = Path(args.out_dir).resolve()

    git_sha = get_git_sha()
    build_info = {
        "created_at": utc_now_iso(),
        "git_sha": git_sha,
        "include_dirs": include_dirs,
        "chunking": {"max_chars": args.max_chars, "overlap_chars": args.overlap_chars},
        "embedding_model": args.model,
    }

    chunks = build_chunks(repo_root, include_dirs, args.max_chars, args.overlap_chars)
    if not chunks:
        print("ERROR: no chunks produced. Check include dirs / markdown files.", file=sys.stderr)
        return 3

    emb = embed_chunks(chunks, model_name=args.model, batch_size=args.batch_size)
    index = build_faiss_index(emb)

    write_artifacts(out_dir, chunks, emb, index, build_info)

    commit_msg = f"KB update: {build_info['created_at']}" + (f" ({git_sha[:7]})" if git_sha else "")
    publish_to_hf(args.dataset_repo, out_dir, token=token, commit_message=commit_msg)

    print(f"OK: published {len(chunks)} chunks to dataset {args.dataset_repo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
