# Экосистемный слой extended-mind

> **extended-mind** — мета-проект, объединяющий экосистему проектов utemix-lab через единый граф связей и инструменты согласования.

## Миссия

Создание **Universe Graph** — единого графа, который:
- Читает локальные подграфы проектов
- Добавляет межпроектные связи и гипотезы
- Не ломает канон отдельных проектов
- Готов к будущему слиянию через ручное принятие Graph Delta

## Инструменты: extended-mind-console

**extended-mind-console** — это платформа с вкладками для работы с разными аспектами экосистемы.

### Вкладки

| Вкладка | Назначение | Статус |
|---------|------------|--------|
| **Console** | Среда для разработки движка extended-mind с RAG | Эксперимент, гипотеза |
| **Core Taxonomy Editor** | Редактор таксономии vovaipetrova-core | Активен |
| *(будущие)* | Редакторы для других проектов экосистемы | Планируется |

### Console (RAG-среда)

Экспериментальная среда для разработки самого движка extended-mind:
- Подгруженный RAG для поиска по базе знаний
- Интерфейс для тестирования запросов
- **Статус**: гипотеза, проба, эксперимент

### Core Taxonomy Editor

Среда для работы с таксономией **vovaipetrova-core**:
- Визуализация графа страниц, терминов, сторис, тегов
- Три слоя рёбер: SYMBOLIC, VECTOR, UNIVERSE
- Focus + Context, Provenance, Delta Inbox
- **Принцип**: vovaipetrova-core остаётся read-only

Документация: [think-tank-editor.md](./think-tank-editor.md)

## Компоненты экосистемного слоя

### Universe Graph
- **Спецификация**: [UNIVERSE_SPEC.md](https://github.com/utemix-lab/vovaipetrova-core/blob/main/docs/graph/UNIVERSE_SPEC.md)
- **Формат**: `graph.jsonl` (NDJSON)

### Cosmos Map
- **Схема**: `schema.v0.2.json`
- **Назначение**: Универсальный формат графа для визуализации

### Graph Delta Inbox
- **Назначение**: Входящие гипотезы связей
- **Правило**: Никакого авто-слияния; только ручной review

## Принципы

### Read-only канон
```
Проект-источник → READ-ONLY
        ↓
   extended-mind (редактор)
        ↓
Saved sessions + proposed deltas
```

### Три слоя рёбер

| Слой | Описание | Автопринятие |
|------|----------|--------------|
| **SYMBOLIC** | Жёсткие связи (теги, ссылки, ручные) | Да |
| **VECTOR** | Мягкие (semantic_near, similarity) | Нет |
| **UNIVERSE** | Межпроектные (экосистемные) | Нет |

## Дорожная карта

| Фаза | Описание | Статус |
|------|----------|--------|
| 1 | Core Taxonomy Editor для vovaipetrova-core | ✅ |
| 2 | Universe overlay (межпроектные связи) | ✅ |
| 3 | Редакторы для других проектов | ⏳ |
| 4 | RAG-graph интеграция | планируется |

## Связанные документы

- [Core Taxonomy Editor](./think-tank-editor.md) — редактор таксономии V&P
- [ECOSYSTEM_LAYER.md](../../ecosystem/ECOSYSTEM_LAYER.md) — правила экосистемного слоя
