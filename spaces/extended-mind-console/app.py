"""
extended-mind — Universe Graph Editor

Канонический граф системы. Место истины.
Редактируется вручную, потом будет осмысляться через RAG.
"""

import html as html_module
from pathlib import Path

import gradio as gr

UI_VERSION = "universe-graph-v0.1"

with gr.Blocks(
    title="extended-mind — Universe Graph",
    theme=gr.themes.Base(
        primary_hue="gray",
        secondary_hue="gray",
        neutral_hue="gray",
    ),
) as demo:
    gr.Markdown(
        f"""
# Universe Graph Editor

**Канонический граф системы — место истины.**

Версия: `{UI_VERSION}`

---

- Добавляй узлы и рёбра вручную
- Экспортируй в JSON
- Граф транслируется в Godot для режиссуры
- RAG-осмысление будет позже
"""
    )

    # Load Universe Graph editor from HTML
    graph_html_path = Path(__file__).parent / "route-graph" / "index.html"

    if graph_html_path.exists():
        graph_html = graph_html_path.read_text(encoding="utf-8")
        graph_srcdoc = html_module.escape(graph_html, quote=True)

        gr.HTML(
            f'<iframe srcdoc="{graph_srcdoc}" '
            'style="width:100%;height:700px;border:0;"></iframe>'
        )
    else:
        gr.Markdown("⚠️ Universe Graph editor not found.")

demo.queue()

if __name__ == "__main__":
    demo.launch()
