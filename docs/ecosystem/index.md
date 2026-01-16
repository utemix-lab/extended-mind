# Экосистемный слой extended-mind

> **extended-mind** — это мета-проект, объединяющий экосистему проектов через единый граф связей.

## Миссия

Создание **Universe Graph** — единого графа, который:
- Читает локальные подграфы проектов
- Добавляет межпроектные связи и гипотезы
- Не ломает канон отдельных проектов
- Готов к будущему слиянию через ручное принятие Graph Delta

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

## Проекты экосистемы

| Проект | Роль | Статус |
|--------|------|--------|
| [vovaipetrova-core](../projects/vova-and-petrova/) | Канонический контент-проект | read-only |
| [extended-mind](../projects/extended-mind-overview.md) | Мета-координация, RAG, Universe Graph | активен |
| [dream-graph](../../graph/dream-graph-contract.md) | 3D визуализация графов | активен |
| evoquant | Финансовая аналитика | наблюдение |
| minds-lorgnette | Семантические пайплайны | наблюдение |

## Компоненты экосистемного слоя

### 1. Universe Graph Specification
- **Спецификация**: [UNIVERSE_SPEC.md](https://github.com/utemix-lab/vovaipetrova-core/blob/main/docs/graph/UNIVERSE_SPEC.md)
- **Схема**: `universe.schema.json`
- **Формат**: `graph.jsonl` (NDJSON)

### 2. Think Tank Editor
- **Документация**: [think-tank-editor.md](./think-tank-editor.md)
- **Расположение**: `spaces/extended-mind-console/core-taxonomy/`
- **Назначение**: Визуализация и редактирование таксономии vovaipetrova-core

### 3. Graph Delta Inbox
- **Назначение**: Входящие гипотезы связей
- **Формат**: `candidate_edge` в JSONL
- **Правило**: Никакого авто-слияния; только ручной review

### 4. Cosmos Map
- **Документация**: [docs/cosmos/](../cosmos/)
- **Схема**: `schema.v0.2.json`
- **Назначение**: Универсальный формат графа для визуализации

## Принципы

### 1. Read-only канон
```
Проект-источник → READ-ONLY
        ↓
   Ecosystem Layer
        ↓
extended-mind → Saved sessions + proposed deltas
```

### 2. Три слоя рёбер

| Слой | Описание | Автопринятие |
|------|----------|--------------|
| **SYMBOLIC** | Жёсткие связи (теги, ссылки, ручные) | Да |
| **VECTOR** | Мягкие (semantic_near, similarity) | Нет |
| **UNIVERSE** | Межпроектные (экосистемные) | Нет |

### 3. Гипотезы vs Канон
- **Канон** — данные проекта, прошедшие governance
- **Гипотеза** — предложенная связь, ожидающая review
- **Граф** — договор между ними

## Дальнейшее развитие

| Фаза | Описание | Статус |
|------|----------|--------|
| 1 | Think Tank как основной граф-вид | ✅ |
| 2 | Universe overlay (read-only экосистема) | ✅ |
| 3 | Интеракции (конфликты, step-by-step review) | ⏳ |
| 4 | RAG-graph интеграция | планируется |

## Связанные документы

- [Think Tank Editor](./think-tank-editor.md) — редактор таксономии
- [Cosmos Map Contract](../cosmos/contract-v0.1.md) — формат графа
- [ECOSYSTEM_LAYER.md](../../ecosystem/ECOSYSTEM_LAYER.md) — правила экосистемного слоя
