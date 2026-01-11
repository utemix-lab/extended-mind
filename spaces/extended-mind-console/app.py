import base64
import json
import os
import time
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Tuple

import faiss  # type: ignore
import gradio as gr  # type: ignore
import numpy as np
from huggingface_hub import InferenceClient, hf_hub_download
from jsonschema import Draft202012Validator  # type: ignore
from sentence_transformers import SentenceTransformer  # type: ignore

from console_utils import build_context_cocktail, serialize_bundle_json, should_call_llm

DATASET_REPO = os.getenv("KB_DATASET_REPO", "utemix/extended-mind-kb")
EMBED_MODEL = os.getenv("KB_EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
UI_VERSION = "nodes-v0-console-0.4"
COSMOS_SCHEMA_PATH = Path("cosmos/schema.v0.2.json")
COSMOS_SAVE_RATE_LIMIT_SEC = int(os.getenv("COSMOS_SAVE_RATE_LIMIT_SEC", "300"))
COSMOS_GITHUB_REPO = os.getenv("COSMOS_GITHUB_REPO", "utemix-lab/extended-mind")
_LAST_COSMOS_SAVE_TS = 0.0

DEFAULT_LLM_MODEL = os.getenv(
    "HF_INFERENCE_MODEL", "meta-llama/Meta-Llama-3.1-8B-Instruct"
)
MODEL_PRESETS = [
    DEFAULT_LLM_MODEL,
    "mistralai/Mistral-7B-Instruct-v0.3",
    "Qwen/Qwen2.5-7B-Instruct",
    "HuggingFaceH4/zephyr-7b-beta",
]
MODEL_PRESETS = [m for i, m in enumerate(MODEL_PRESETS) if m and m not in MODEL_PRESETS[:i]]

NODE_PRESETS = {
    "Custom": [],
    "Core": ["manifest", "adr", "principle", "pattern"],
    "ADR-only": ["adr"],
    "Principles-only": ["principle"],
    "Manifest-only": ["manifest"],
    "Story-layer": ["storylayer"],
}


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


def _unique_values(chunks: List[Dict[str, Any]], key: str) -> List[str]:
    vals = {str(c.get(key)).strip() for c in chunks if c.get(key)}
    return sorted(vals)


def _present_count(chunks: List[Dict[str, Any]], key: str) -> int:
    return sum(1 for c in chunks if c.get(key))


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
        self.source_dir_values = _unique_values(self.chunks, "source_dir")
        self.doc_kind_values = _unique_values(self.chunks, "doc_kind")
        self.project_values = _unique_values(self.chunks, "project")

        self.source_dir_present_count = _present_count(self.chunks, "source_dir")
        self.doc_kind_present_count = _present_count(self.chunks, "doc_kind")
        self.project_present_count = _present_count(self.chunks, "project")

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
                    "source_dir": c.get("source_dir"),
                    "doc_kind": c.get("doc_kind"),
                    "project": c.get("project"),
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
    return q.startswith("what is") or q.startswith("\u0447\u0442\u043e \u0442\u0430\u043a\u043e\u0435")


def _apply_filters(
    results: List[Dict[str, Any]],
    min_score: float,
    dedup: bool,
    prefer_manifest_adr: bool,
    selected_source_dirs: List[str] | None,
    selected_doc_kinds: List[str] | None,
    selected_project: str,
    query: str,
) -> Tuple[List[Dict[str, Any]], int, int]:
    filtered = results
    if selected_source_dirs:
        allowed = {s for s in selected_source_dirs if s}
        if allowed:
            filtered = [r for r in filtered if r.get("source_dir") in allowed]

    if selected_doc_kinds:
        allowed = {s for s in selected_doc_kinds if s}
        if allowed:
            filtered = [r for r in filtered if r.get("doc_kind") in allowed]

    if selected_project and selected_project != "all":
        filtered = [r for r in filtered if r.get("project") == selected_project]

    if min_score > 0:
        filtered = [r for r in filtered if r["score"] >= min_score]

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
    selected_source_dirs: List[str],
    selected_doc_kinds: List[str],
    selected_project: str,
    full_text: bool,
    llm_mode: str,
    llm_model: str,
    max_tokens: int,
    temperature: float,
    answer_style: str,
    preset: str,
    strict_mode: bool,
    strict_min_sources: int,
):
    raw_k = max(int(top_k), int(top_k) * 5)
    res = KB.search(query, raw_k)
    res, matched_count, dedup_removed = _apply_filters(
        res,
        float(min_score),
        dedup_by_path,
        prefer_manifest_adr,
        selected_source_dirs,
        selected_doc_kinds,
        selected_project,
        query,
    )
    res = res[: int(top_k)]
    if not res:
        debug = _format_debug(
            len(KB.chunks),
            matched_count,
            dedup_removed,
            raw_k,
            len(res),
            min_score,
            selected_source_dirs,
            selected_doc_kinds,
            selected_project,
            view_mode,
            preset,
            strict_mode,
            strict_min_sources,
        )
        return (
            "No results found. Try a different query.",
            "",
            "",
            "No sources.",
            "",
            {},
            debug,
        )

    if view_mode == "Table":
        context_out = _format_table(res)
    else:
        context_out = _format_cards(res, full_text)

    bundle_md, bundle_json, citations = build_context_cocktail(query, res, len(res))
    sources_out = _format_sources(citations)

    answer_out = ""
    if strict_mode and len(res) < int(strict_min_sources):
        answer_out = f"Strict mode: not enough sources (need {int(strict_min_sources)})."
    elif llm_mode == "ON":
        provider = os.getenv("HF_INFERENCE_PROVIDER")
        answer_out, err = _call_llm(
            query,
            bundle_md,
            llm_model,
            max_tokens,
            temperature,
            answer_style,
            provider,
        )
        if err:
            answer_out = "LLM unavailable"

    why_out = _format_why(
        matched_count,
        dedup_removed,
        len(res),
        min_score,
        selected_source_dirs,
        selected_doc_kinds,
        selected_project,
        strict_mode,
        int(strict_min_sources),
        llm_mode,
    )

    debug = _format_debug(
        len(KB.chunks),
        matched_count,
        dedup_removed,
        raw_k,
        len(res),
        min_score,
        selected_source_dirs,
        selected_doc_kinds,
        selected_project,
        view_mode,
        preset,
        strict_mode,
        strict_min_sources,
    )
    return context_out, answer_out, why_out, sources_out, bundle_md, bundle_json, debug


def _format_sources(citations: List[Dict[str, Any]]) -> str:
    if not citations:
        return "No sources."
    lines = []
    for i, c in enumerate(citations, 1):
        parts = [f"**{i})** score={c['score']:.4f}"]
        if c.get("doc_kind"):
            parts.append(f"doc_kind={c['doc_kind']}")
        lines.append(" - ".join(parts))
        lines.append(f"- path: `{c['path']}`")
        if c.get("title"):
            lines.append(f"- title: {c['title']}")
        lines.append("- matched by semantic similarity")
        lines.append("")
    return "\n".join(lines).strip()


def _load_cosmos_schema() -> Dict[str, Any]:
    if not COSMOS_SCHEMA_PATH.exists():
        return {}
    return json.loads(COSMOS_SCHEMA_PATH.read_text(encoding="utf-8"))


def validate_cosmos_payload(payload: Dict[str, Any]) -> List[str]:
    schema = _load_cosmos_schema()
    if not schema:
        return ["schema not found"]
    validator = Draft202012Validator(schema)
    errors = []
    for err in validator.iter_errors(payload):
        errors.append(f"{err.message} (at {list(err.path)})")
    return errors


def _github_request(method: str, url: str, token: str, body: Dict[str, Any] | None) -> Dict[str, Any]:
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def save_cosmos_payload(payload: Dict[str, Any], override: bool) -> Dict[str, Any]:
    global _LAST_COSMOS_SAVE_TS

    errors = validate_cosmos_payload(payload)
    if errors:
        return {"ok": False, "errors": errors}

    now = time.time()
    if not override and _LAST_COSMOS_SAVE_TS and now - _LAST_COSMOS_SAVE_TS < COSMOS_SAVE_RATE_LIMIT_SEC:
        return {"ok": False, "error": "recent save, please wait"}

    token = os.getenv("GH_TOKEN")
    if not token:
        return {"ok": False, "error": "missing GH_TOKEN"}

    owner_repo = COSMOS_GITHUB_REPO
    api = "https://api.github.com"
    ref = _github_request(
        "GET", f"{api}/repos/{owner_repo}/git/ref/heads/main", token, None
    )
    base_sha = ref["object"]["sha"]

    branch = time.strftime("cosmos/%Y%m%d-%H%M%S")
    _github_request(
        "POST",
        f"{api}/repos/{owner_repo}/git/refs",
        token,
        {"ref": f"refs/heads/{branch}", "sha": base_sha},
    )

    content = base64.b64encode(json.dumps(payload, ensure_ascii=True, indent=2).encode("utf-8")).decode(
        "utf-8"
    )
    _github_request(
        "PUT",
        f"{api}/repos/{owner_repo}/contents/cosmos/cosmos-map.v0.2.json",
        token,
        {
            "message": "cosmos: update map (session)",
            "content": content,
            "branch": branch,
        },
    )

    nodes_count = len(payload.get("nodes", []))
    edges_count = len(payload.get("edges", []))
    pr = _github_request(
        "POST",
        f"{api}/repos/{owner_repo}/pulls",
        token,
        {
            "title": "cosmos: update map (session)",
            "head": branch,
            "base": "main",
            "body": f"session save\\n\\n- nodes: {nodes_count}\\n- edges: {edges_count}\\n- ts: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        },
    )

    _LAST_COSMOS_SAVE_TS = now
    return {"ok": True, "pr_url": pr.get("html_url", "")}


def validate_cosmos_api(payload: Dict[str, Any]) -> Dict[str, Any]:
    errors = validate_cosmos_payload(payload)
    return {"ok": not errors, "errors": errors}


def _format_why(
    matched_count: int,
    dedup_removed: int,
    final_count: int,
    min_score: float,
    selected_source_dirs: List[str],
    selected_doc_kinds: List[str],
    selected_project: str,
    strict_mode: bool,
    strict_min_sources: int,
    llm_mode: str,
) -> str:
    lines = []
    lines.append("- Routing: filter by doc kind/source/project, then semantic rerank.")
    lines.append(
        f"- Filters: doc_kind={selected_doc_kinds or []}, "
        f"source_dir={selected_source_dirs or []}, "
        f"project={selected_project or 'all'}, "
        f"min_score={float(min_score):.2f}"
    )
    lines.append(
        f"- Matched after filters: {matched_count}, "
        f"removed by dedup: {dedup_removed}, final: {final_count}."
    )
    if strict_mode:
        status = "ok" if final_count >= strict_min_sources else "not enough sources"
        lines.append(f"- Strict mode: ON (min_sources={strict_min_sources}, {status}).")
    else:
        lines.append("- Strict mode: OFF.")
    lines.append(f"- LLM mode: {llm_mode}.")
    return "\n".join(lines)


def _call_llm(
    query: str,
    bundle_md: str,
    model: str,
    max_tokens: int,
    temperature: float,
    answer_style: str,
    provider: str | None,
) -> Tuple[str, str]:
    token = os.getenv("HF_TOKEN")
    if not should_call_llm(True, token, model):
        return "", "LLM unavailable"

    system = (
        "You are a neutral engineer. Use only the provided context. "
        "Cite sources by path when possible. If missing, say you do not know."
    )
    if answer_style == "strict":
        system += " Be concise and strict."
    elif answer_style == "explainer":
        system += " Explain clearly and briefly."

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": f"Question: {query}\n\n{bundle_md}"},
    ]

    client = InferenceClient(token=token)
    kwargs = {
        "model": model,
        "messages": messages,
        "max_tokens": int(max_tokens),
        "temperature": float(temperature),
    }
    if provider:
        kwargs["provider"] = provider

    try:
        response = client.chat.completions.create(**kwargs)
    except TypeError:
        kwargs.pop("provider", None)
        response = client.chat.completions.create(**kwargs)
    except Exception as exc:
        print(f"LLM error: {exc}")
        return "", "LLM unavailable"

    content = response.choices[0].message.content or ""
    return content, ""


def _format_debug(
    total_chunks: int,
    matched_count: int,
    dedup_removed: int,
    top_k_raw: int,
    top_k_final: int,
    min_score: float,
    selected_source_dirs: List[str],
    selected_doc_kinds: List[str],
    selected_project: str,
    view_mode: str,
    preset: str,
    strict_mode: bool,
    strict_min_sources: int,
) -> str:
    filters_selected = {
        "view_mode": view_mode,
        "min_score": float(min_score),
        "source_dir": selected_source_dirs or [],
        "doc_kind": selected_doc_kinds or [],
        "project": selected_project or "all",
        "preset": preset or "Custom",
        "strict_mode": bool(strict_mode),
        "strict_min_sources": int(strict_min_sources),
    }
    return (
        f"- ui_version: **{UI_VERSION}**\n"
        f"- top_k_raw: **{top_k_raw}**\n"
        f"- top_k_final: **{top_k_final}**\n"
        f"- total chunks: **{total_chunks}**\n"
        f"- matched (after filters): **{matched_count}**\n"
        f"- removed by dedup: **{dedup_removed}**\n"
        f"- filters_selected: `{json.dumps(filters_selected, ensure_ascii=False)}`\n"
        f"- doc_kind_present_count: **{KB.doc_kind_present_count}**\n"
        f"- source_dir_present_count: **{KB.source_dir_present_count}**\n"
        f"- project_present_count: **{KB.project_present_count}**"
    )


def _load_graph_map() -> str:
    path = Path("docs/maps/graph.mmd")
    if not path.exists():
        return "Map not built yet. Run the auto-map workflow."
    text = path.read_text(encoding="utf-8", errors="replace")
    return "```mermaid\n" + text.strip() + "\n```"


with gr.Blocks(title="extended-mind console") as demo:
    gr.Markdown(
        "# extended-mind Search Console\n"
        "Retrieval over the extended-mind knowledge base with an optional LLM layer."
    )

    with gr.Tabs():
        with gr.TabItem("Console"):
            with gr.Row():
                query = gr.Textbox(
                    label="Query",
                    placeholder="Ask a question, e.g. What is extended-mind?",
                    lines=2,
                )
            with gr.Row():
                top_k = gr.Slider(1, 20, value=8, step=1, label="Top K")

            gr.Markdown("### Node Presets")
            with gr.Row():
                preset = gr.Dropdown(
                    choices=list(NODE_PRESETS.keys()),
                    value="Custom",
                    label="Preset",
                )
                gr.Markdown("Routing: doc kind filter -> semantic rerank.")

            gr.Markdown("### Filters")
            with gr.Row():
                source_dirs = gr.CheckboxGroup(
                    choices=KB.source_dir_values,
                    label="Source dir",
                )
                doc_kinds = gr.CheckboxGroup(
                    choices=KB.doc_kind_values,
                    label="Doc kind",
                )
                projects = gr.Dropdown(
                    choices=["all"] + KB.project_values,
                    value="all",
                    label="Project",
                )
                view_mode = gr.Radio(
                    choices=["Cards", "Table"],
                    value="Cards",
                    label="Mode",
                )

            with gr.Row():
                min_score = gr.Slider(0.0, 1.0, value=0.0, step=0.01, label="Min score")
                dedup_by_path = gr.Checkbox(value=True, label="Deduplicate by rel_path")
                prefer_manifest_adr = gr.Checkbox(
                    value=True, label='Prefer manifest/adr for "what is"'
                )
                full_text = gr.Checkbox(value=False, label="Show full text (cards)")

            reset_filters = gr.Button("Reset filters")

            if (
                KB.doc_kind_present_count == 0
                or KB.source_dir_present_count == 0
                or KB.project_present_count == 0
            ):
                gr.Markdown("Metadata fields missing in chunks - run KB rebuild")

            gr.Markdown("### LLM Mode")
            with gr.Row():
                llm_mode = gr.Radio(
                    choices=["OFF", "ON"],
                    value="OFF",
                    label="LLM",
                )
                llm_model = gr.Dropdown(
                    choices=MODEL_PRESETS,
                    value=DEFAULT_LLM_MODEL,
                    label="Model",
                )
                max_tokens = gr.Slider(32, 1024, value=256, step=32, label="max_tokens")
                temperature = gr.Slider(0.0, 1.2, value=0.2, step=0.05, label="temperature")
                answer_style = gr.Dropdown(
                    choices=["neutral", "strict", "explainer"],
                    value="neutral",
                    label="Answer style",
                )

            gr.Markdown("### Answer Policy")
            with gr.Row():
                strict_mode = gr.Checkbox(value=False, label="Strict mode")
                strict_min_sources = gr.Slider(1, 10, value=3, step=1, label="Min sources")

            btn = gr.Button("Search")
            gr.Markdown("## Context Cocktail")
            context_out = gr.Markdown()
            gr.Markdown("## Answer (LLM)")
            answer_out = gr.Markdown()
            gr.Markdown("## Why this answer")
            why_out = gr.Markdown()
            gr.Markdown("## Sources")
            sources_out = gr.Markdown()
            bundle_md_state = gr.State("")
            bundle_json_state = gr.State({})

            with gr.Accordion("Debug panel", open=False):
                debug_out = gr.Markdown(
                    _format_debug(
                        len(KB.chunks),
                        0,
                        0,
                        0,
                        0,
                        0.0,
                        [],
                        [],
                        "all",
                        "Cards",
                        "Custom",
                        False,
                        3,
                    )
                )

            btn.click(
                fn=ui_search,
                inputs=[
                    query,
                    top_k,
                    view_mode,
                    min_score,
                    dedup_by_path,
                    prefer_manifest_adr,
                    source_dirs,
                    doc_kinds,
                    projects,
                    full_text,
                    llm_mode,
                    llm_model,
                    max_tokens,
                    temperature,
                    answer_style,
                    preset,
                    strict_mode,
                    strict_min_sources,
                ],
                outputs=[
                    context_out,
                    answer_out,
                    why_out,
                    sources_out,
                    bundle_md_state,
                    bundle_json_state,
                    debug_out,
                ],
            )

            def _reset_filters():
                return "Custom", [], [], "all", "Cards", 0.0, True, True, False, False, 3

            reset_filters.click(
                fn=_reset_filters,
                inputs=[],
                outputs=[
                    preset,
                    source_dirs,
                    doc_kinds,
                    projects,
                    view_mode,
                    min_score,
                    dedup_by_path,
                    prefer_manifest_adr,
                    full_text,
                    strict_mode,
                    strict_min_sources,
                ],
            )

            def _apply_preset(preset_name: str):
                return NODE_PRESETS.get(preset_name, [])

            preset.change(fn=_apply_preset, inputs=[preset], outputs=[doc_kinds])

            gr.Markdown("### Export")
            with gr.Row():
                copy_bundle_btn = gr.Button("Copy bundle (MD)")
                download_json_btn = gr.Button("Download bundle.json")
                copy_prompt_btn = gr.Button("Copy prompt scaffold")

            bundle_md_out = gr.Textbox(label="Bundle (MD)", lines=10)
            prompt_out = gr.Textbox(label="Prompt scaffold", lines=8)
            bundle_file = gr.File(label="bundle.json")

            def _bundle_md_out(bundle_md: str) -> str:
                return bundle_md or ""

            def _prompt_scaffold(bundle_md: str) -> str:
                if not bundle_md:
                    return ""
                return "Use this prompt with your LLM:\n\n" + bundle_md

            def _bundle_json_file(bundle: Dict[str, Any]) -> str | None:
                if not bundle:
                    return None
                import tempfile

                fd, path = tempfile.mkstemp(suffix=".json")
                with os.fdopen(fd, "w", encoding="utf-8") as f:
                    f.write(serialize_bundle_json(bundle))
                return path

            copy_bundle_btn.click(fn=_bundle_md_out, inputs=[bundle_md_state], outputs=[bundle_md_out])
            copy_prompt_btn.click(fn=_prompt_scaffold, inputs=[bundle_md_state], outputs=[prompt_out])
            download_json_btn.click(fn=_bundle_json_file, inputs=[bundle_json_state], outputs=[bundle_file])

            schema_version = KB.build_info.get("chunk_schema_version")
            schema_line = f"**Chunk schema:** `{schema_version}`" if schema_version else ""
            header = f"**Dataset:** `{DATASET_REPO}`  \n**Embedding model:** `{EMBED_MODEL}`"
            if schema_line:
                header = f"{header}  \n{schema_line}"
            gr.Markdown(header)

            with gr.Accordion("Help / About", open=False):
                gr.Markdown(
                    "Search vs thinking:\n"
                    "- Search = retrieval from KB.\n"
                    "- Thinking = optional LLM over the context cocktail.\n\n"
                    "Inputs:\n"
                    "- Query: your question.\n"
                    "- Top K: how many chunks to keep.\n\n"
                    "Node presets & routing:\n"
                    "- Preset sets doc_kind filters (Core/ADR/Principles/Manifest/Story-layer).\n"
                    "- Routing order: doc kind filter -> semantic rerank.\n\n"
                    "Filters:\n"
                    "- Source dir / Doc kind / Project: metadata filters.\n"
                    "- Min score: drop low-similarity results.\n"
                    "- Deduplicate by rel_path: keep one chunk per file.\n"
                    "- Prefer manifest/adr for \"what is\": bias for definitions.\n"
                    "- Show full text (cards): full chunk vs preview.\n\n"
                    "LLM mode:\n"
                    "- OFF = only context cocktail and sources.\n"
                    "- ON = calls HF Inference chat completion.\n\n"
                    "Answer policy:\n"
                    "- Strict mode: answer only if >= N sources.\n\n"
                    "Outputs:\n"
                    "- Context Cocktail: top fragments + metadata.\n"
                    "- Answer (LLM): optional response.\n"
                    "- Why this answer: brief rationale and constraints.\n"
                    "- Sources: score, path, doc kind, and reason.\n\n"
                    "Export:\n"
                    "- Copy bundle (MD), Download bundle.json, Copy prompt scaffold.\n\n"
                    "Debug panel:\n"
                    "- Diagnostic counters and selected filters.\n\n"
                    "Map tab:\n"
                    "- Mermaid graph of docs (raw render).\n\n"
                    "Secrets (Space env vars):\n"
                    "- HF_TOKEN (required for LLM calls)\n"
                    "- HF_INFERENCE_MODEL (model name for chat completion)\n"
                    "- HF_INFERENCE_PROVIDER (optional)\n\n"
                    "Safety:\n"
                    "- Answer uses sources; if none, it should say it does not know."
                )
        with gr.TabItem("Map"):
            gr.Markdown("## Map")
            gr.Markdown(_load_graph_map())

        with gr.TabItem("Cosmos"):
            gr.Markdown("## Cosmos Map")
            cosmos_html_path = Path(__file__).parent / "cosmos-map" / "index.html"
            if cosmos_html_path.exists():
                import html

                cosmos_html = cosmos_html_path.read_text(encoding="utf-8")
                cosmos_srcdoc = html.escape(cosmos_html, quote=True)
                gr.HTML(
                    f'<iframe srcdoc="{cosmos_srcdoc}" '
                    'style="width:100%;height:720px;border:0;"></iframe>'
                )
                gr.Markdown("Direct links: /?mode=view or /?mode=edit")

                cosmos_payload = gr.JSON(visible=False)
                cosmos_override = gr.Checkbox(visible=False)
                cosmos_result = gr.JSON(visible=False)
                cosmos_save_btn = gr.Button(visible=False)
                cosmos_validate_btn = gr.Button(visible=False)

                cosmos_save_btn.click(
                    fn=save_cosmos_payload,
                    inputs=[cosmos_payload, cosmos_override],
                    outputs=[cosmos_result],
                    api_name="save_cosmos",
                )

                cosmos_validate_btn.click(
                    fn=validate_cosmos_api,
                    inputs=[cosmos_payload],
                    outputs=[cosmos_result],
                    api_name="validate_cosmos",
                )
            else:
                gr.Markdown("Cosmos map UI not found.")

if __name__ == "__main__":
    demo.launch()
