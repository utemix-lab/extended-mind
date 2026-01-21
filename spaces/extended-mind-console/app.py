"""
extended-mind — Universe Graph Editor

Канонический граф системы. Место истины.
Редактируется вручную, потом будет осмысляться через RAG.

При локальном запуске: Save сохраняет в contracts для Godot.
"""

import html as html_module
import json
import os
from pathlib import Path

import gradio as gr

UI_VERSION = "universe-graph-v0.2"

# Путь для сохранения графа (относительно workspace)
# При локальном запуске — сохраняем в contracts
CONTRACTS_PATH = Path(__file__).parent.parent.parent.parent / "contracts" / "contracts" / "public" / "graph"
GRAPH_FILE = CONTRACTS_PATH / "universe.json"


def save_graph(graph_json: str) -> dict:
    """Сохранить граф в contracts/public/graph/universe.json"""
    try:
        # Проверить, что это валидный JSON
        data = json.loads(graph_json)
        
        # Создать директорию если нет
        CONTRACTS_PATH.mkdir(parents=True, exist_ok=True)
        
        # Сохранить
        with open(GRAPH_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return {
            "ok": True,
            "message": f"Saved to {GRAPH_FILE}",
            "nodes": len(data.get("nodes", [])),
            "edges": len(data.get("edges", []))
        }
    except json.JSONDecodeError as e:
        return {"ok": False, "error": f"Invalid JSON: {e}"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def load_graph() -> dict:
    """Загрузить граф из contracts/public/graph/universe.json"""
    try:
        if GRAPH_FILE.exists():
            with open(GRAPH_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            return {"ok": True, "data": data}
        else:
            # Вернуть пустой граф с начальным узлом
            return {
                "ok": True,
                "data": {
                    "id": "universe-graph",
                    "nodes": [{"id": "universe", "label": "Universe", "position": {"x": 400, "y": 300}}],
                    "edges": []
                }
            }
    except Exception as e:
        return {"ok": False, "error": str(e)}


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

- **Save** — сохраняет в `contracts/public/graph/universe.json`
- Godot читает этот файл как шаблон
- RAG-осмысление будет позже
"""
    )

    # Load Universe Graph editor from HTML
    graph_html_path = Path(__file__).parent / "route-graph" / "index.html"

    if graph_html_path.exists():
        graph_html = graph_html_path.read_text(encoding="utf-8")
        graph_srcdoc = html_module.escape(graph_html, quote=True)

        gr.HTML(
            f'<iframe id="graph-frame" srcdoc="{graph_srcdoc}" '
            'style="width:100%;height:650px;border:0;"></iframe>'
        )
        
        # API для сохранения/загрузки
        with gr.Row():
            save_btn = gr.Button("💾 Save to Contracts", variant="primary")
            load_btn = gr.Button("📂 Load from Contracts")
            status_text = gr.Textbox(label="Status", interactive=False, max_lines=1)
        
        # Скрытые компоненты для данных
        graph_data_input = gr.Textbox(visible=False, elem_id="graph-data-input")
        graph_data_output = gr.JSON(visible=False, elem_id="graph-data-output")
        
        save_btn.click(
            fn=save_graph,
            inputs=[graph_data_input],
            outputs=[graph_data_output],
            api_name="save_graph"
        ).then(
            fn=lambda x: x.get("message", x.get("error", "Unknown")),
            inputs=[graph_data_output],
            outputs=[status_text]
        )
        
        load_btn.click(
            fn=load_graph,
            inputs=[],
            outputs=[graph_data_output],
            api_name="load_graph"
        ).then(
            fn=lambda x: f"Loaded: {len(x.get('data', {}).get('nodes', []))} nodes" if x.get("ok") else x.get("error"),
            inputs=[graph_data_output],
            outputs=[status_text]
        )
        
        # JavaScript для связи iframe с Gradio
        gr.HTML("""
        <script>
        (function() {
            // Получить данные из iframe и отправить в Gradio
            window.getGraphData = function() {
                const iframe = document.getElementById('graph-frame');
                if (iframe && iframe.contentWindow) {
                    try {
                        const data = iframe.contentWindow.graphData;
                        if (data) {
                            // Обновить позиции
                            const cy = iframe.contentWindow.cy;
                            if (cy) {
                                data.nodes.forEach(node => {
                                    const cyNode = cy.$('#' + node.id);
                                    if (cyNode.length) {
                                        node.position = cyNode.position();
                                    }
                                });
                            }
                            return JSON.stringify(data);
                        }
                    } catch(e) {
                        console.error('Error getting graph data:', e);
                    }
                }
                return '{}';
            };
            
            // Загрузить данные в iframe
            window.loadGraphData = function(data) {
                const iframe = document.getElementById('graph-frame');
                if (iframe && iframe.contentWindow && data) {
                    try {
                        iframe.contentWindow.graphData = data;
                        iframe.contentWindow.renderGraph();
                        iframe.contentWindow.updateStats();
                    } catch(e) {
                        console.error('Error loading graph data:', e);
                    }
                }
            };
            
            // Перехватить кнопку Save
            setTimeout(() => {
                const saveBtn = document.querySelector('button[variant="primary"]');
                if (saveBtn) {
                    saveBtn.addEventListener('click', function() {
                        const input = document.querySelector('#graph-data-input textarea');
                        if (input) {
                            input.value = getGraphData();
                            input.dispatchEvent(new Event('input', { bubbles: true }));
                        }
                    }, true);
                }
            }, 1000);
        })();
        </script>
        """)
        
    else:
        gr.Markdown("⚠️ Universe Graph editor not found.")

demo.queue()

if __name__ == "__main__":
    demo.launch()
