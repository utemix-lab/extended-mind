# Экосистемный слой (надстройка)

## Что это

Экосистемный слой — гипотезы связей между проектами.  
Он не меняет канон проектов и не влияет на их внутренние правила.

**extended-mind** выполняет роль мета-координатора экосистемы, объединяя проекты через единый Universe Graph.

## Правила

- **Vova & Petrova — read‑only канон.**  
  Никаких изменений slug/таксономии/RAG/CI/UI.
- Экосистема — только гипотезы (nodes/edges).
- Дельты — только предложения, без автопринятия.

## Архитектура

```
┌─────────────────────────────────────────────────────────────────┐
│                      UNIVERSE GRAPH                              │
│  (Project nodes, Pattern nodes, inter-project edges)            │
└─────────────────────────────────────────────────────────────────┘
         ↑                    ↑                    ↑
         │ read-only          │ read-only          │ read-only
    ┌────┴────┐         ┌─────┴─────┐        ┌─────┴─────┐
    │  V&P    │         │  dream-   │        │  evoquant │
    │  core   │         │  graph    │        │           │
    └─────────┘         └───────────┘        └───────────┘
      LOCAL               LOCAL                 LOCAL
      SUBGRAPH            SUBGRAPH              SUBGRAPH
```

## Три слоя рёбер

| Слой | Описание | Визуал | Автопринятие |
|------|----------|--------|--------------|
| **SYMBOLIC** | Жёсткие связи (теги, ссылки, ручные) | Сплошная линия | Да |
| **VECTOR** | Мягкие (semantic_near, similarity) | Пунктир | Нет |
| **UNIVERSE** | Межпроектные (экосистемные) | Точечная | Нет |

## Инструменты

### Think Tank Editor

Визуализатор и редактор таксономии vovaipetrova-core.

- **Расположение**: `spaces/extended-mind-console/core-taxonomy/`
- **Документация**: [docs/ecosystem/think-tank-editor.md](../docs/ecosystem/think-tank-editor.md)
- **Возможности**:
  - Три слоя визуализации (SYMBOLIC, VECTOR, UNIVERSE)
  - Режимы: Project Focus / Ecosystem Overlay
  - Focus + Context (N-хопов соседей)
  - Provenance on hover
  - Delta Inbox (предложить связь)

### Cosmos Map

Универсальный формат графа для визуализации.

- **Расположение**: `cosmos/`
- **Схема**: `schema.v0.2.json`
- **Документация**: [docs/cosmos/](../docs/cosmos/)

## Где живут данные

| Путь | Содержимое |
|------|------------|
| `ecosystem/graph/` | Узлы/рёбра экосистемного слоя |
| `ecosystem/graph/inbox/` | Inbox гипотез (candidate edges) |
| `ecosystem/logs/` | Лог самопроверки |
| `cosmos/` | Cosmos Map графы |

## Как принимать Graph Delta вручную

1. Открыть `ecosystem/graph/inbox/from-ecosystem.codex.jsonl`.
2. Проверить `rationale` и `confidence`.
3. Если согласовано — перенести в канонический граф.
4. Иначе — оставить/удалить запись с комментарием.

## Принцип изоляции

```
vovaipetrova-core    →    READ-ONLY source
                    ↓
             Think Tank Editor
                    ↓
extended-mind        →    Saved sessions + proposed deltas
```

## Дорожная карта

| Фаза | Описание | Статус |
|------|----------|--------|
| 1 | Think Tank как основной граф-вид | ✅ |
| 2 | Universe overlay (read-only экосистема) | ✅ |
| 3 | Интеракции (конфликты, step-by-step review) | ⏳ |
| 4 | RAG-graph интеграция | планируется |

## Связанные документы

- [Экосистемный слой (docs)](../docs/ecosystem/index.md)
- [Think Tank Editor](../docs/ecosystem/think-tank-editor.md)
- [Cosmos Map](../docs/cosmos/index.md)
- [UNIVERSE_SPEC.md](https://github.com/utemix-lab/vovaipetrova-core/blob/main/docs/graph/UNIVERSE_SPEC.md)
