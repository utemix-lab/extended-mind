"""
extended-mind console — Route Graph Editor v0.1

Авторский конструктор маршрутов и карт экосистемы.
"""

import html as html_module
import os
from pathlib import Path
from typing import Any, Dict

import gradio as gr
from huggingface_hub import InferenceClient

# === Config ===
UI_VERSION = "route-graph-editor-v0.1"

DEFAULT_LLM_MODEL = os.getenv(
    "HF_INFERENCE_MODEL", "meta-llama/Meta-Llama-3.1-8B-Instruct"
)
MODEL_PRESETS = [
    DEFAULT_LLM_MODEL,
    "mistralai/Mistral-7B-Instruct-v0.3",
    "Qwen/Qwen2.5-7B-Instruct",
]


# === LLM Chat API ===
def universe_graph_chat(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Chat with LLM about Universe Graph."""
    token = os.getenv("HF_TOKEN")
    if not token:
        return {"ok": False, "error": "HF_TOKEN not configured"}

    messages = payload.get("messages", [])
    model = payload.get("model", DEFAULT_LLM_MODEL)
    max_tokens = payload.get("max_tokens", 512)
    temperature = payload.get("temperature", 0.7)

    if not messages:
        return {"ok": False, "error": "No messages provided"}

    try:
        client = InferenceClient(token=token)
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=int(max_tokens),
            temperature=float(temperature),
        )
        content = response.choices[0].message.content or ""
        return {"ok": True, "content": content}
    except Exception as exc:
        return {"ok": False, "error": str(exc)}


# === Validation ===
def validate_universe_graph(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Validate Universe Graph payload."""
    errors = []
    warnings = []

    nodes = payload.get("nodes", [])
    edges = payload.get("edges", [])

    # Check for orphan nodes
    node_ids = {n.get("id") for n in nodes}
    connected = set()
    for e in edges:
        connected.add(e.get("source"))
        connected.add(e.get("target"))
    orphans = node_ids - connected
    for o in orphans:
        warnings.append(f"Orphan node: {o}")

    # Check layer balance
    layers = {"story": 0, "system": 0, "service": 0}
    for n in nodes:
        layer = n.get("layer")
        if layer in layers:
            layers[layer] += 1
    for layer, count in layers.items():
        if count == 0:
            warnings.append(f"Empty layer: {layer}")

    return {
        "ok": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "stats": {
            "nodes": len(nodes),
            "edges": len(edges),
            "rag_ready": len([n for n in nodes if n.get("rag_include")]),
        },
    }


# === UI ===
with gr.Blocks(
    title="extended-mind — Route Graph Editor",
    theme=gr.themes.Base(
        primary_hue="purple",
        secondary_hue="gray",
        neutral_hue="gray",
    ),
) as demo:
    gr.Markdown(
        f"""
# extended-mind — Route Graph Editor

**Авторский конструктор маршрутов и карт экосистемы.**

Версия: `{UI_VERSION}`
"""
    )

    with gr.Tabs():
        with gr.TabItem("Universe Graph v0.1"):
            gr.Markdown(
                """
## Universe Graph Editor

Редактор мета-графа экосистемы **utemix-lab**.

**Ключевые принципы:**
- **Канон мал** — только Projects, Repos, Concepts, Principles, Decisions, Roles
- **3S = линзы** — Story / System / Service — режимы просмотра, не сущности
- **Маршрут ≠ канон** — Route Graph ссылается на канон через refs

**Спецификации:**
- [MANIFEST.md](https://github.com/utemix-lab/extended-mind/blob/main/docs/graph/MANIFEST.md)
- [ROUTE_GRAPH_SPEC.md](https://github.com/utemix-lab/extended-mind/blob/main/docs/graph/ROUTE_GRAPH_SPEC.md)
"""
            )

            # Load Universe Graph editor from HTML
            universe_graph_html_path = (
                Path(__file__).parent / "universe-graph" / "index.html"
            )

            if universe_graph_html_path.exists():
                universe_graph_html = universe_graph_html_path.read_text(
                    encoding="utf-8"
                )
                universe_graph_srcdoc = html_module.escape(
                    universe_graph_html, quote=True
                )

                gr.HTML(
                    f'<iframe srcdoc="{universe_graph_srcdoc}" '
                    'style="width:100%;height:800px;border:0;"></iframe>'
                )

                gr.Markdown(
                    """
---

**Типы узлов (Canon):**
- `Project`, `Repository` — Universe
- `Decision`, `Principle`, `Pattern` — Architecture
- `Concept`, `Definition` — Ontology
- `Role` — Actors

**Типы связей:**
- **SYMBOLIC:** governs, implements, defines, contains, uses, derives_from
- **VECTOR:** semantic_near, similar_to (для будущего RAG)

---

*LLM интеграция временно отключена. Используйте "Экспорт ТЗ" для работы в Cursor.*
"""
                )

                # Hidden API components
                ug_validate_payload = gr.JSON(visible=False)
                ug_validate_result = gr.JSON(visible=False)
                ug_validate_btn = gr.Button(visible=False)

                ug_validate_btn.click(
                    fn=validate_universe_graph,
                    inputs=[ug_validate_payload],
                    outputs=[ug_validate_result],
                    api_name="validate_universe_graph",
                )

                ug_chat_payload = gr.JSON(visible=False)
                ug_chat_result = gr.JSON(visible=False)
                ug_chat_btn = gr.Button(visible=False)

                ug_chat_btn.click(
                    fn=universe_graph_chat,
                    inputs=[ug_chat_payload],
                    outputs=[ug_chat_result],
                    api_name="universe_chat",
                )
            else:
                gr.Markdown("⚠️ Universe Graph editor not found.")

# Enable queue for API access
demo.queue()

if __name__ == "__main__":
    demo.launch()
