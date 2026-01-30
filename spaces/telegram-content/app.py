"""
Telegram Content Generator for extended-mind ecosystem.
Reads story-nodes and generates formatted posts for Telegram.
"""

import gradio as gr
import requests
import re
from datetime import datetime

# Configuration
PAGES_URL = "https://utemix-lab.github.io/dream-graph/visitor.html"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/utemix-lab/extended-mind/main/docs/narrative/story-nodes"
GITHUB_API_BASE = "https://api.github.com/repos/utemix-lab/extended-mind/contents/docs/narrative/story-nodes"
DEFAULT_MAX_POSTS = 3

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
    perspective = story_node.get('Что это закладывает', '')
    
    post = f"""🔮 {title}

{what_happened}

💡 Почему это важно:
{why_needed}"""
    
    if perspective:
        post += f"\n\n🚀 Перспектива:\n{perspective}"
    
    post += f"\n\n❓ Открытый вопрос:\n{open_question}"
    
    if include_link:
        post += f"\n\n→ Смотреть систему: {PAGES_URL}"
    
    return post

def get_story_nodes() -> list:
    """Get list of all story-nodes from GitHub."""
    try:
        response = requests.get(GITHUB_API_BASE, timeout=10)
        if response.status_code == 200:
            files = response.json()
            nodes = [f['name'] for f in files if f['name'].startswith('story-node-') and f['name'].endswith('.md')]
            return sorted(nodes)
    except Exception as e:
        print(f"Error fetching story-nodes list: {e}")
    return []

def load_story_node(node_name: str) -> str:
    """Load story-node content from GitHub."""
    if not node_name:
        return ""
    try:
        url = f"{GITHUB_RAW_BASE}/{node_name}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error loading story-node: {e}")
    return ""

def load_and_generate(node_name: str) -> tuple:
    """Load story-node and generate TG post."""
    if not node_name:
        return "Выберите story-node из списка", "", 0
    
    content = load_story_node(node_name)
    if not content:
        return "Не удалось загрузить файл", "", 0
    
    parsed = parse_story_node(content)
    post = generate_tg_post(parsed)
    char_count = len(post)
    
    return content, post, char_count

def extract_checkpoint_refs(raw_content: str) -> list:
    matches = re.findall(r'checkpoint:\s*`?([0-9]{4}-[0-9]{2}-[0-9]{2})`?', raw_content)
    return matches

def get_checkpoint_dates() -> list:
    """Get list of checkpoint dates referenced in story-nodes."""
    nodes = get_story_nodes()
    dates = set()

    for node_name in nodes:
        content = load_story_node(node_name)
        if not content:
            continue
        for date in extract_checkpoint_refs(content):
            dates.add(date)

    return sorted(dates, reverse=True)

def get_story_nodes_without_checkpoint() -> list:
    """List story-nodes that do not reference a checkpoint."""
    nodes = get_story_nodes()
    missing = []

    for node_name in nodes:
        content = load_story_node(node_name)
        if not content:
            continue
        if not extract_checkpoint_refs(content):
            missing.append(node_name)

    return missing

def load_and_generate_batch(checkpoint_date: str, max_posts: int) -> tuple:
    if not checkpoint_date:
        return "Введите дату checkpoint (YYYY-MM-DD).", "", 0

    nodes = get_story_nodes()
    matched = []

    for node_name in nodes:
        content = load_story_node(node_name)
        if not content:
            continue
        parsed = parse_story_node(content)
        checkpoints = extract_checkpoint_refs(content)
        if checkpoint_date in checkpoints:
            matched.append((node_name, parsed))

    if not matched:
        return "Не найдены story-nodes для этого checkpoint.", "", 0

    max_posts = max_posts or DEFAULT_MAX_POSTS
    selected = matched[:max_posts]
    posts = [generate_tg_post(parsed) for _, parsed in selected]
    combined = "\n\n---\n\n".join(posts)
    node_list = ", ".join([name for name, _ in selected])
    return combined, node_list, len(combined)

def run_validator() -> tuple:
    missing = get_story_nodes_without_checkpoint()
    if not missing:
        return "Все story-nodes имеют checkpoint.", 0
    return "\n".join(missing), len(missing)

def refresh_lists():
    """Refresh the list of story-nodes and checkpoints."""
    nodes = get_story_nodes()
    checkpoints = get_checkpoint_dates()
    return (
        gr.update(choices=nodes, value=nodes[0] if nodes else None),
        gr.update(choices=checkpoints, value=checkpoints[0] if checkpoints else None)
    )

# UI
with gr.Blocks(title="Telegram Content Generator") as app:
    gr.Markdown("""
    # 📝 Telegram Content Generator
    
    Генератор постов для Telegram из story-nodes системы **extended-mind**.
    
    ---
    
    **Критерии зрелости story-node:**
    1. ✅ Реальное изменение в системе
    2. ✅ Снятое напряжение/тупик
    3. ✅ Одно решение (без ветвлений)
    4. ✅ Явное следствие
    5. ✅ Открытый вопрос
    6. ✅ Что это закладывает (перспектива)
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            node_dropdown = gr.Dropdown(
                choices=get_story_nodes(),
                label="Story-node",
                value=None
            )
            refresh_btn = gr.Button("🔄 Обновить список из GitHub")
            
            gr.Markdown("---")
            gr.Markdown(f"""
**Ссылка на систему:**

[{PAGES_URL}]({PAGES_URL})

---

**Источник:** [GitHub](https://github.com/utemix-lab/extended-mind/tree/main/docs/narrative/story-nodes)
            """)
        
        with gr.Column(scale=2):
            with gr.Tab("📱 Telegram пост"):
                tg_output = gr.Textbox(
                    label="Готовый пост (скопируйте)",
                    lines=15
                )
                char_count = gr.Number(label="Символов", precision=0)
                gr.Markdown("*Рекомендуемый размер: 1200-1500 символов*")

            with gr.Tab("📦 System Fix batch"):
                checkpoint_date = gr.Dropdown(
                    label="Checkpoint date (YYYY-MM-DD)",
                    choices=get_checkpoint_dates(),
                    value=None,
                    allow_custom_value=True
                )
                max_posts = gr.Number(
                    label="Max posts",
                    value=DEFAULT_MAX_POSTS,
                    precision=0
                )
                batch_btn = gr.Button("⚡ Сгенерировать")
                batch_output = gr.Textbox(
                    label="Пакет постов (разделены ---)",
                    lines=18
                )
                batch_nodes = gr.Textbox(
                    label="Story-nodes",
                    lines=2
                )
                batch_count = gr.Number(label="Символов", precision=0)
                gr.Markdown("---")
                validator_btn = gr.Button("🧭 Валидатор story-nodes")
                validator_output = gr.Textbox(
                    label="Story-nodes без checkpoint",
                    lines=6
                )
                validator_count = gr.Number(label="Найдено", precision=0)
            
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

    batch_btn.click(
        fn=load_and_generate_batch,
        inputs=[checkpoint_date, max_posts],
        outputs=[batch_output, batch_nodes, batch_count]
    )

    validator_btn.click(
        fn=run_validator,
        outputs=[validator_output, validator_count]
    )
    
    refresh_btn.click(
        fn=refresh_lists,
        outputs=[node_dropdown, checkpoint_date]
    )

if __name__ == "__main__":
    app.launch()
