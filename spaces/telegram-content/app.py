"""
Telegram Content Generator for extended-mind ecosystem.
Reads story-nodes and generates formatted posts for Telegram.
"""

import gradio as gr
import os
import re
from pathlib import Path
from datetime import datetime

# Configuration
PAGES_URL = "https://utemix-lab.github.io/dream-graph/visitor.html"
STORY_NODES_PATH = Path(__file__).parent.parent.parent / "docs" / "narrative" / "story-nodes"

def parse_story_node(content: str) -> dict:
    """Parse story-node markdown into structured data."""
    sections = {}
    current_section = None
    current_content = []
    
    for line in content.split('\n'):
        if line.startswith('## '):
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = line[3:].strip()
            current_content = []
        elif current_section and not line.startswith('#'):
            if not line.startswith('<!--') and not line.endswith('-->'):
                current_content.append(line)
    
    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections

def generate_tg_post(story_node: dict, include_link: bool = True) -> str:
    """Generate Telegram post from story-node data."""
    title = story_node.get('Название', 'Без названия')
    what_happened = story_node.get('Что произошло', '')
    why_needed = story_node.get('Почему это было необходимо', '')
    open_question = story_node.get('Открытый вопрос', '')
    
    post = f"""🔮 {title}

{what_happened}

💡 Почему это важно:
{why_needed}

❓ Открытый вопрос:
{open_question}"""
    
    if include_link:
        post += f"\n\n→ Смотреть систему: {PAGES_URL}"
    
    return post

def get_story_nodes() -> list:
    """Get list of all story-nodes."""
    if not STORY_NODES_PATH.exists():
        return []
    
    nodes = []
    for file in sorted(STORY_NODES_PATH.glob("story-node-*.md")):
        nodes.append(file.name)
    return nodes

def load_and_generate(node_name: str) -> tuple:
    """Load story-node and generate TG post."""
    if not node_name:
        return "", "", 0
    
    file_path = STORY_NODES_PATH / node_name
    if not file_path.exists():
        return "Файл не найден", "", 0
    
    content = file_path.read_text(encoding='utf-8')
    parsed = parse_story_node(content)
    post = generate_tg_post(parsed)
    char_count = len(post)
    
    return content, post, char_count

def refresh_nodes():
    """Refresh the list of story-nodes."""
    nodes = get_story_nodes()
    return gr.update(choices=nodes, value=nodes[0] if nodes else None)

# UI
with gr.Blocks(title="Telegram Content Generator") as app:
    gr.Markdown("""
    # 📝 Telegram Content Generator
    
    Генератор постов для Telegram из story-nodes системы.
    
    **Критерии зрелости story-node:**
    1. Реальное изменение в системе
    2. Снятое напряжение/тупик
    3. Одно решение (без ветвлений)
    4. Явное следствие
    5. Открытый вопрос
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            node_dropdown = gr.Dropdown(
                choices=get_story_nodes(),
                label="Story-node",
                value=get_story_nodes()[0] if get_story_nodes() else None
            )
            refresh_btn = gr.Button("🔄 Обновить список")
            
            gr.Markdown("---")
            gr.Markdown(f"**Ссылка на систему:**\n\n[{PAGES_URL}]({PAGES_URL})")
        
        with gr.Column(scale=2):
            with gr.Tab("📱 Telegram пост"):
                tg_output = gr.Textbox(
                    label="Готовый пост (скопируйте вручную)",
                    lines=15
                )
                char_count = gr.Number(label="Символов", precision=0)
                gr.Markdown("*Рекомендуемый размер: 1200-1500 символов*")
            
            with gr.Tab("📄 Исходный story-node"):
                source_output = gr.Textbox(
                    label="Markdown",
                    lines=20
                )
    
    # Events
    node_dropdown.change(
        fn=load_and_generate,
        inputs=[node_dropdown],
        outputs=[source_output, tg_output, char_count]
    )
    
    refresh_btn.click(
        fn=refresh_nodes,
        outputs=[node_dropdown]
    )
    
    # Initial load
    app.load(
        fn=load_and_generate,
        inputs=[node_dropdown],
        outputs=[source_output, tg_output, char_count]
    )

if __name__ == "__main__":
    app.launch()
