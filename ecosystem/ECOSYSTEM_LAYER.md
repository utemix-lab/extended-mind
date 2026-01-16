# Экосистемный слой (надстройка)

> **extended-mind** выполняет роль мета-координатора экосистемы, объединяя проекты через единый Universe Graph.

## Что это

Экосистемный слой — гипотезы связей между проектами.  
Он не меняет канон проектов и не влияет на их внутренние правила.

## Правила

- **Vova & Petrova — read‑only канон.**  
  Никаких изменений slug/таксономии/RAG/CI/UI.
- Экосистема — только гипотезы (nodes/edges).
- Дельты — только предложения, без автопринятия.

## Три слоя рёбер

| Слой | Описание | Автопринятие |
|------|----------|--------------|
| **SYMBOLIC** | Жёсткие связи (теги, ссылки, ручные) | Да |
| **VECTOR** | Мягкие (semantic_near, similarity) | Нет |
| **UNIVERSE** | Межпроектные (экосистемные) | Нет |

## Инструменты: extended-mind-console

**extended-mind-console** — платформа с вкладками для работы с экосистемой.

| Вкладка | Назначение | Статус |
|---------|------------|--------|
| **Console** | RAG-среда для разработки движка extended-mind | Эксперимент |
| **Core Taxonomy Editor** | Редактор таксономии vovaipetrova-core | Активен |
| *(будущие)* | Редакторы для других проектов | Планируется |

### Core Taxonomy Editor

Среда для работы с таксономией vovaipetrova-core:
- Визуализация графа страниц, терминов, сторис, тегов
- Три слоя рёбер: SYMBOLIC, VECTOR, UNIVERSE
- Delta Inbox для предложения связей

- **Расположение**: `spaces/extended-mind-console/core-taxonomy/`
- **Документация**: [docs/ecosystem/think-tank-editor.md](../docs/ecosystem/think-tank-editor.md)

## Где живут данные

| Путь | Содержимое |
|------|------------|
| `ecosystem/graph/` | Узлы/рёбра экосистемного слоя |
| `ecosystem/graph/inbox/` | Inbox гипотез (candidate edges) |
| `ecosystem/logs/` | Лог самопроверки |

## Как принимать Graph Delta вручную

1. Открыть `ecosystem/graph/inbox/from-ecosystem.codex.jsonl`.
2. Проверить `rationale` и `confidence`.
3. Если согласовано — перенести в канонический граф.
4. Иначе — оставить/удалить запись с комментарием.

## Дорожная карта

| Фаза | Описание | Статус |
|------|----------|--------|
| 1 | Core Taxonomy Editor для vovaipetrova-core | ✅ |
| 2 | Universe overlay (межпроектные связи) | ✅ |
| 3 | Редакторы для других проектов экосистемы | ⏳ |
| 4 | Step-by-step review дельт | планируется |
| 5 | RAG-graph интеграция | планируется |

## Связанные документы

- [Экосистемный слой (docs)](../docs/ecosystem/index.md)
- [Core Taxonomy Editor](../docs/ecosystem/think-tank-editor.md)
