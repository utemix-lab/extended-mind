import json
import os
from typing import Any, Dict, List

import faiss  # type: ignore
import gradio as gr  # type: ignore
import numpy as np
from huggingface_hub import hf_hub_download
from sentence_transformers import SentenceTransformer  # type: ignore


DATASET_REPO = os.getenv("KB_DATASET_REPO", "utemix/extended-mind-kb")
EMBED_MODEL = os.getenv("KB_EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")


def _download_artifact(filename: str) -> str:
    return hf_hub_download(
        repo_id=DATASET_REPO,
        repo_type="dataset",
        filename=filename,
    )


def _load_chunks(path: str) -> List[Dict[str, Any]]:
    chunks: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            chunks.append(json.loads(line))
    return chunks


def _safe_join_title(title_path: Any) -> str:
    if isinstance(title_path, list):
        return " > ".join([str(x) for x in title_path if x is not None])
    return str(title_path) if title_path is not None else ""


class KBSearch:
    def __init__(self) -> None:
        chunks_path = _download_artifact("chunks.jsonl")
        index_path = _download_artifact("faiss.index")

        try:
            _download_artifact("build_info.json")
        except Exception:
            pass

        self.chunks = _load_chunks(chunks_path)
        self.index = faiss.read_index(index_path)
        self.model = SentenceTransformer(EMBED_MODEL)

    def search(self, query: str, top_k: int) -> List[Dict[str, Any]]:
        q = (query or "").strip()
        if not q:
            return []

        k = max(1, min(int(top_k), len(self.chunks)))

        emb = self.model.encode([q], normalize_embeddings=True)
        qv = np.asarray(emb, dtype="float32")

        scores, idxs = self.index.search(qv, k)
        scores = scores[0].tolist()
        idxs = idxs[0].tolist()

        results: List[Dict[str, Any]] = []
        for score, i in zip(scores, idxs):
            if i < 0 or i >= len(self.chunks):
                continue
            c = self.chunks[i]
            results.append(
                {
                    "score": float(score),
                    "rel_path": c.get("rel_path", ""),
                    "title_path": _safe_join_title(c.get("title_path", [])),
                    "text": c.get("text", ""),
                }
            )
        return results


KB = KBSearch()


def ui_search(query: str, top_k: int) -> str:
    res = KB.search(query, int(top_k))
    if not res:
        return "No results found. Try a different query."

    lines = []
    for n, r in enumerate(res, 1):
        lines.append(f"### {n}) score={r['score']:.4f}")
        lines.append(f"- path: `{r['rel_path']}`")
        if r["title_path"]:
            lines.append(f"- title: {r['title_path']}")
        lines.append("")
        lines.append(r["text"])
        lines.append("\n---\n")
    return "\n".join(lines)


with gr.Blocks(title="extended-mind console") as demo:
    gr.Markdown(
        "# extended-mind Search Console\n"
        "Local retrieval-only search over the extended-mind knowledge base. "
        "No LLM, just vector search."
    )

    with gr.Row():
        query = gr.Textbox(
            label="Query",
            placeholder="Ask a question, e.g. What is extended-mind?",
            lines=2,
        )
    with gr.Row():
        top_k = gr.Slider(1, 20, value=8, step=1, label="Top K")

    btn = gr.Button("Search")
    out = gr.Markdown()

    btn.click(fn=ui_search, inputs=[query, top_k], outputs=[out])

    gr.Markdown(
        f"**Dataset:** `{DATASET_REPO}`  \n"
        f"**Embedding model:** `{EMBED_MODEL}`"
    )

if __name__ == "__main__":
    demo.launch()
