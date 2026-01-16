# Core Taxonomy Editor

Конструктор графа таксономии **vovaipetrova-core** — отдельный режим визуального редактирования структуры проекта.

## Назначение

Core Taxonomy Editor позволяет:
- Визуализировать связи между страницами, терминами KB и Stories
- Редактировать узлы и рёбра графа
- Создавать новые связи между сущностями
- Сохранять сессии локально или через PR

## Доменная модель

### Типы узлов (NODE_TYPES)

| Тип | Источник | Описание |
|-----|----------|----------|
| `page` | `canon_map.v1.json` | Страницы проекта (docs, think-tank, kb) |
| `term` | `kb_terms.v1.jsonl` | Термины базы знаний с stable_id |
| `story` | `stories.v1.jsonl` | Эпизоды и серии Stories |
| `tag` | теги из term.tags | Фасеты и машинотеги |

### Типы рёбер (EDGE_KINDS)

| Тип | Описание |
|-----|----------|
| `links_to` | Явная ссылка в тексте |
| `mentions` | Упоминание термина |
| `has_tag` | Страница/термин → тег |
| `alias_of` | Синоним (alias → page) |
| `related_to` | Семантическая связь |
| `child_of` | Иерархия (страница → родитель) |
| `series_of` | Серия Stories |

## Изоляция от extended-mind

Core Taxonomy Editor использует **собственную доменную модель**, не пересекающуюся с extended-mind:

- **extended-mind types**: project, layer, artifact, actor, system
- **core-taxonomy types**: page, term, story, tag

Переиспользуется только инфраструктура:
- Cytoscape.js для визуализации
- Layout algorithms (cose)
- UI паттерны (фильтры, панели редактирования)

## Режимы работы

### View mode (`?mode=view`)
- Только просмотр графа
- Узлы нельзя перемещать
- Панели редактирования скрыты

### Edit mode (`?mode=edit`)
- Перемещение узлов drag & drop
- Создание/удаление узлов и рёбер
- Редактирование свойств
- Добавление custom props

## Источники данных

```
vovaipetrova-core/
├── data/exports/
│   ├── canon_map.v1.json      → page nodes + alias edges
│   ├── kb_terms.v1.jsonl      → term nodes + tag edges + links_to edges
│   └── stories.v1.jsonl       → story nodes
```

## Сохранение

### Локально (localStorage)
- Кнопка "Сохранить локально"
- Данные сохраняются в `localStorage['core-taxonomy-draft']`
- Загружаются автоматически при следующем открытии

### Экспорт JSON
- Кнопка "Экспорт JSON"
- Скачивает `core-taxonomy-export.json`
- Формат: `{ version, generated_at, source, nodes, edges }`

### Создание PR (TODO)
- Интеграция с GitHub API для создания PR с обновлённым графом

## Использование

### В Gradio Space
1. Открыть extended-mind-console
2. Перейти на вкладку "Core Taxonomy"
3. Использовать iframe с редактором

### Standalone
1. Открыть `core-taxonomy/index.html` в браузере
2. Данные загружаются из `vovaipetrova-core/data/exports/`
3. Или загрузить файл через "Загрузить из файла"

## Развитие

### Планируемые функции
- [ ] Интеграция с GitHub API для PR
- [ ] Валидация по universe.schema.json
- [ ] Экспорт в graph.jsonl формат
- [ ] Подгрузка дополнительных источников (routes.json, slices)
- [ ] Undo/Redo
