import json
import os
from typing import Any, Dict, List, Tuple

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

        build_info: Dict[str, Any] = {}
        try:
            build_info_path = _download_artifact("build_info.json")
            with open(build_info_path, "r", encoding="utf-8") as f:
                build_info = json.load(f)
        except Exception:
            pass

        self.chunks = _load_chunks(chunks_path)
        self.index = faiss.read_index(index_path)
        self.model = SentenceTransformer(EMBED_MODEL)
        self.build_info = build_info

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
CARD_PREVIEW_CHARS = 400


def _preview_text(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "..."


def _format_cards(results: List[Dict[str, Any]], full_text: bool) -> str:
    lines = []
    for n, r in enumerate(results, 1):
        lines.append(f"### {n}) score={r['score']:.4f}")
        lines.append(f"- path: `{r['rel_path']}`")
        if r["title_path"]:
            lines.append(f"- title: {r['title_path']}")
        lines.append("")
        text = r["text"] if full_text else _preview_text(r["text"], CARD_PREVIEW_CHARS)
        lines.append(text)
        lines.append("\n---\n")
    return "\n".join(lines)


def _format_table(results: List[Dict[str, Any]]) -> str:
    lines = [
        "| score | rel_path | title_path | preview |",
        "| --- | --- | --- | --- |",
    ]
    for r in results:
        preview = " ".join(str(r["text"]).split())
        if len(preview) > 200:
            preview = preview[:200].rstrip() + "..."
        lines.append(
            f"| {r['score']:.4f} | `{r['rel_path']}` | {r['title_path']} | {preview} |"
        )
    return "\n".join(lines)


def _is_what_is_query(query: str) -> bool:
    q = (query or "").strip().lower()
    return q.startswith("what is") or q.startswith("что такое")


def _apply_filters(
    results: List[Dict[str, Any]],
    min_score: float,
    dedup: bool,
    prefer_manifest_adr: bool,
    query: str,
) -> Tuple[List[Dict[str, Any]], int, int]:
    filtered = [r for r in results if r["score"] >= min_score]
    matched_count = len(filtered)

    if prefer_manifest_adr and _is_what_is_query(query):
        def prefer_key(r: Dict[str, Any]) -> int:
            rp = r.get("rel_path", "")
            return 0 if rp.startswith("manifest/") or rp.startswith("adr/") else 1

        filtered.sort(key=lambda r: (-r["score"], prefer_key(r)))
    else:
        filtered.sort(key=lambda r: -r["score"])

    dedup_removed = 0
    if dedup:
        seen = set()
        deduped = []
        for r in filtered:
            rp = r.get("rel_path")
            if rp in seen:
                continue
            seen.add(rp)
            deduped.append(r)
        dedup_removed = len(filtered) - len(deduped)
        filtered = deduped

    return filtered, matched_count, dedup_removed


def ui_search(
    query: str,
    top_k: int,
    view_mode: str,
    min_score: float,
    dedup_by_path: bool,
    prefer_manifest_adr: bool,
    full_text: bool,
):
    res = KB.search(query, int(top_k))
    res, matched_count, dedup_removed = _apply_filters(
        res, float(min_score), dedup_by_path, prefer_manifest_adr, query
    )
    if not res:
        debug = _format_debug(len(KB.chunks), matched_count, dedup_removed)
        return "No results found. Try a different query.", [], query, debug

    if view_mode == "Table":
        out = _format_table(res)
    else:
        out = _format_cards(res, full_text)
    debug = _format_debug(len(KB.chunks), matched_count, dedup_removed)
    return out, res, query, debug


def ui_export_json(results: List[Dict[str, Any]]):
    if not results:
        return "```json\n[]\n```"
    return "```json\n" + json.dumps(results, ensure_ascii=False, indent=2) + "\n```"


def ui_bundle(query: str, results: List[Dict[str, Any]]):
    if not results:
        return "No results to bundle."
    lines = [f"Query: {query}", ""]
    for n, r in enumerate(results, 1):
        header = f"[{n}] {r['rel_path']}"
        if r["title_path"]:
            header += f" | {r['title_path']}"
        lines.append(header)
        lines.append(r["text"])
        lines.append("")
    return "\n".join(lines).strip()


def _format_debug(total_chunks: int, matched_count: int, dedup_removed: int) -> str:
    return (
        f"- total chunks: **{total_chunks}**\n"
        f"- matched (after filters): **{matched_count}**\n"
        f"- removed by dedup: **{dedup_removed}**"
    )


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

    with gr.Row():
        view_mode = gr.Radio(
            choices=["Cards", "Table"],
            value="Cards",
            label="View mode",
        )

    with gr.Row():
        min_score = gr.Slider(0.0, 1.0, value=0.0, step=0.01, label="Min score")
        dedup_by_path = gr.Checkbox(value=True, label="Deduplicate by rel_path")
        prefer_manifest_adr = gr.Checkbox(
            value=True, label='Prefer manifest/adr for "what is"'
        )

    with gr.Row():
        full_text = gr.Checkbox(value=False, label="Show full text (cards)")

    btn = gr.Button("Search")
    out = gr.Markdown()
    results_state = gr.State([])
    query_state = gr.State("")

    with gr.Accordion("Debug panel", open=False):
        debug_out = gr.Markdown(_format_debug(len(KB.chunks), 0, 0))

    btn.click(
        fn=ui_search,
        inputs=[
            query,
            top_k,
            view_mode,
            min_score,
            dedup_by_path,
            prefer_manifest_adr,
            full_text,
        ],
        outputs=[out, results_state, query_state, debug_out],
    )

    with gr.Row():
        export_btn = gr.Button("Export JSON")
        bundle_btn = gr.Button("Copy bundle")

    export_out = gr.Markdown(label="Export JSON")
    bundle_out = gr.Textbox(label="Bundle", lines=12, show_copy_button=True)

    export_btn.click(fn=ui_export_json, inputs=[results_state], outputs=[export_out])
    bundle_btn.click(fn=ui_bundle, inputs=[query_state, results_state], outputs=[bundle_out])

    schema_version = KB.build_info.get("chunk_schema_version")
    schema_line = f"**Chunk schema:** `{schema_version}`" if schema_version else ""
    header = f"**Dataset:** `{DATASET_REPO}`  \n**Embedding model:** `{EMBED_MODEL}`"
    if schema_line:
        header = f"{header}  \n{schema_line}"
    gr.Markdown(header)

if __name__ == "__main__":
    demo.launch()
