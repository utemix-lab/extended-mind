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

## Инструменты экосистемы

### extended-mind-console (редактирование)

**Платформа с вкладками** для редактирования таксономий.

| Вкладка | Назначение | Статус |
|---------|------------|--------|
| **Console** | RAG-среда для разработки движка | Эксперимент |
| **Core Taxonomy Editor** | Редактор таксономии vovaipetrova-core | Активен |
| *(будущие)* | Редакторы для других проектов | Планируется |

- **Расположение**: `spaces/extended-mind-console/`
- **Документация**: [docs/ecosystem/think-tank-editor.md](../docs/ecosystem/think-tank-editor.md)

### dream-graph (визуализация)

**Рендер со вкладками разных сцен и стеков**.

Среда для поиска визуальных выразительных средств и элементов UI.

| Сцена | Описание |
|-------|----------|
| **Planetary** | Орбитальная модель |
| **Universe Map** | Экосистемный вид |
| **Core Taxonomy** | Граф vovaipetrova-core |

- **Репозиторий**: `dream-graph`
- **Документация**: [docs/ecosystem/dream-graph-overview.md](../docs/ecosystem/dream-graph-overview.md)
- **Демо**: https://utemix-lab.github.io/dream-graph/

### Связь инструментов

```
extended-mind-console (редактирование)
        ↓ экспорт Cosmos Map
dream-graph (визуализация)
```

dream-graph **экспортирует данные** для построения графов из разных сред extended-mind.

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
- [dream-graph](../docs/ecosystem/dream-graph-overview.md)
