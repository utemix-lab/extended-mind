"""
extended-mind console — Route Graph Editor v0.1

Авторский конструктор маршрутов и карт экосистемы.
"""

import html as html_module
import os
from pathlib import Path
from typing import Any, Dict, List

import gradio as gr
from huggingface_hub import InferenceClient

# === Config ===
UI_VERSION = "route-graph-editor-v0.1"

DEFAULT_LLM_MODEL = os.getenv(
    "HF_INFERENCE_MODEL", "meta-llama/Meta-Llama-3.1-8B-Instruct"
)


# === LLM Chat API (для будущего использования) ===
def route_graph_chat(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Chat with LLM about Route Graph."""
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
def validate_route_graph(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Validate Route Graph payload against limits and structure."""
    errors: List[str] = []
    warnings: List[str] = []

    nodes = payload.get("nodes", [])
    edges = payload.get("edges", [])
    limits = payload.get("limits", {"max_nodes": 50, "max_edges": 100, "max_depth": 10})
    start_node_id = payload.get("start_node_id")

    # Check limits
    if len(nodes) > limits.get("max_nodes", 50):
        errors.append(f"Превышен лимит шагов: {len(nodes)} > {limits['max_nodes']}")
    if len(edges) > limits.get("max_edges", 100):
        errors.append(f"Превышен лимит связей: {len(edges)} > {limits['max_edges']}")

    # Check start node exists
    node_ids = {n.get("id") for n in nodes}
    if start_node_id and start_node_id not in node_ids:
        errors.append(f"Начальный узел не найден: {start_node_id}")

    # Check edge references
    for e in edges:
        if e.get("source") not in node_ids:
            errors.append(f"Связь ссылается на несуществующий узел: {e.get('source')}")
        if e.get("target") not in node_ids:
            errors.append(f"Связь ссылается на несуществующий узел: {e.get('target')}")

    # Check for empty Story/System/Service (warnings only)
    for n in nodes:
        if not n.get("story", {}).get("text"):
            warnings.append(f"Пустой Story: {n.get('label', n.get('id'))}")
        if not n.get("system", {}).get("text"):
            warnings.append(f"Пустой System: {n.get('label', n.get('id'))}")

    # Calculate depth
    depth = 0
    if start_node_id:
        visited = set()
        def dfs(node_id: str, d: int) -> int:
            if node_id in visited:
                return d
            visited.add(node_id)
            max_d = d
            for e in edges:
                if e.get("source") == node_id and e.get("type") == "NEXT":
                    max_d = max(max_d, dfs(e.get("target"), d + 1))
            return max_d
        depth = dfs(start_node_id, 1)
    
    if depth > limits.get("max_depth", 10):
        errors.append(f"Превышена глубина: {depth} > {limits['max_depth']}")

    return {
        "ok": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "stats": {
            "nodes": len(nodes),
            "edges": len(edges),
            "depth": depth,
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
# 🛤️ extended-mind — Route Graph Editor

**Авторский конструктор маршрутов и карт экосистемы.**

Версия: `{UI_VERSION}`
"""
    )

    with gr.Tabs():
        with gr.TabItem("Route Graph Editor"):
            gr.Markdown(
                """
## Редактор маршрутов

**Route Graph** — конечный граф маршрута (Steps + NEXT/BRANCH/RELATED).

**Ключевые принципы:**
- **Route Graph первичен** — редактируется в центре
- **Universe Graph = read-only канон** — источник refs
- **3S = линзы** — Story / System / Service — редактируют содержимое шага
- **Конечность** — лимиты на nodes, edges, depth

**Спецификации:**
- [MANIFEST.md](https://github.com/utemix-lab/extended-mind/blob/main/docs/graph/MANIFEST.md)
- [ROUTE_GRAPH_SPEC.md](https://github.com/utemix-lab/extended-mind/blob/main/docs/graph/ROUTE_GRAPH_SPEC.md)
"""
            )

            # Load Route Graph editor from HTML
            route_graph_html_path = (
                Path(__file__).parent / "route-graph" / "index.html"
            )

            if route_graph_html_path.exists():
                route_graph_html = route_graph_html_path.read_text(encoding="utf-8")
                route_graph_srcdoc = html_module.escape(route_graph_html, quote=True)

                gr.HTML(
                    f'<iframe srcdoc="{route_graph_srcdoc}" '
                    'style="width:100%;height:850px;border:0;"></iframe>'
                )

                gr.Markdown(
                    """
---

**Типы узлов:**
- `RouteNode` (Step) — шаг маршрута с тремя проекциями

**Типы связей:**
- **NEXT** — основной путь (сплошная линия)
- **BRANCH** — альтернатива (пунктир)
- **RELATED** — мягкая связь (тонкая линия)

**Три проекции (3S):**
- 📖 **Story** — что происходит (нарратив)
- ⚙️ **System** — как устроено (архитектура)
- 🎯 **Service** — что делать (действия)

---

*LLM интеграция будет добавлена позже.*
"""
                )

                # Hidden API components for validation
                rg_validate_payload = gr.JSON(visible=False)
                rg_validate_result = gr.JSON(visible=False)
                rg_validate_btn = gr.Button(visible=False)

                rg_validate_btn.click(
                    fn=validate_route_graph,
                    inputs=[rg_validate_payload],
                    outputs=[rg_validate_result],
                    api_name="validate_route_graph",
                )

                # LLM API (для будущего)
                rg_chat_payload = gr.JSON(visible=False)
                rg_chat_result = gr.JSON(visible=False)
                rg_chat_btn = gr.Button(visible=False)

                rg_chat_btn.click(
                    fn=route_graph_chat,
                    inputs=[rg_chat_payload],
                    outputs=[rg_chat_result],
                    api_name="route_graph_chat",
                )
            else:
                gr.Markdown("⚠️ Route Graph editor not found.")

# Enable queue for API access
demo.queue()

if __name__ == "__main__":
    demo.launch()
