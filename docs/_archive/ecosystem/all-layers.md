# Ecosystem Layers — Индекс всех слоёв

> Каждый репозиторий экосистемы имеет собственный `ecosystem/ECOSYSTEM_LAYER.md`, описывающий его роль и связи.

## Зачем это нужно

Ecosystem Layer — это единый контракт, который:
- Объясняет роль репо в экосистеме
- Описывает входящие и исходящие связи
- Содержит граф-данные для Universe Graph
- Позволяет LLM быстро понять контекст

## Структура ecosystem/ папки

```
<repo>/
└── ecosystem/
    ├── ECOSYSTEM_LAYER.md           # Описание роли
    ├── graph/
    │   ├── ecosystem_nodes.jsonl    # Узлы этого репо
    │   ├── ecosystem_edges.symbolic.jsonl  # Явные связи
    │   ├── ecosystem_edges.vector.jsonl    # Семантические связи
    │   └── inbox/
    │       └── from-ecosystem.codex.jsonl  # Входящие дельты
    └── logs/
        └── ecosystem_graph_validation.md   # Отчёт валидации
```

## Индекс слоёв

| Репо | Ecosystem Layer | Роль |
|------|-----------------|------|
| **extended-mind** | [ecosystem/ECOSYSTEM_LAYER.md](../../ecosystem/ECOSYSTEM_LAYER.md) | Мета-координатор |
| **vovaipetrova-core** | [ecosystem/ECOSYSTEM_LAYER.md](https://github.com/utemix-lab/vovaipetrova-core/blob/main/ecosystem/ECOSYSTEM_LAYER.md) | Канон контента |
| **dream-graph** | [ecosystem/ECOSYSTEM_LAYER.md](https://github.com/utemix-lab/dream-graph/blob/main/ecosystem/ECOSYSTEM_LAYER.md) | 3D рендер |
| **minds-lorgnette** | [ecosystem/ECOSYSTEM_LAYER.md](https://github.com/utemix-lab/minds-lorgnette/blob/main/ecosystem/ECOSYSTEM_LAYER.md) | Универсальное приложение |
| **evoquant** | [evoquant/ecosystem/ECOSYSTEM_LAYER.md](https://github.com/utemix-lab/evoquant/blob/main/evoquant/ecosystem/ECOSYSTEM_LAYER.md) | Исследования |

## Репо без ecosystem/ слоя

Некоторые репозитории (contracts, godot-sandbox, vovaipetrova-site) пока не имеют ecosystem/ слоя, так как являются:
- Инфраструктурными (contracts)
- Sandbox/WIP (godot-sandbox)
- Чисто UI (vovaipetrova-site)

При необходимости слой может быть добавлен.

## Граф-данные

Все `ecosystem_nodes.jsonl` и `ecosystem_edges.*.jsonl` экспортируются в единый Universe Graph через:

```bash
# В extended-mind
npm run graph:aggregate
```

Это создаёт консолидированный граф в `extended-mind/data/graph/universe.jsonl`.

## Валидация

Каждый ecosystem/ слой валидируется по схеме:
- `extended-mind/docs/graph/universe.schema.json`

Отчёты валидации сохраняются в `ecosystem/logs/ecosystem_graph_validation.md`.

## Как добавить ecosystem/ слой в новый репо

1. Создать структуру папок:
```bash
mkdir -p ecosystem/graph/inbox ecosystem/logs
```

2. Создать `ECOSYSTEM_LAYER.md`:
```markdown
# Ecosystem Layer — <repo-name>

## Роль в экосистеме
<описание>

## Входящие связи
- От кого получает данные/методы

## Исходящие связи
- Кому передаёт данные/методы

## Граф-данные
- ecosystem_nodes.jsonl — узлы этого репо
- ecosystem_edges.symbolic.jsonl — явные связи
```

3. Добавить начальные узлы в `ecosystem_nodes.jsonl`:
```jsonl
{"id":"<repo>","type":"Repo","label":"<Repo Name>","project":"utemix-lab"}
```

4. Добавить ссылку в этот индекс (extended-mind/docs/ecosystem/all-layers.md)

## Связанные документы

- [Экосистема utemix-lab](./index.md)
- [META_GRAPH_SPEC.md](../graph/META_GRAPH_SPEC.md) — типы узлов и связей
- [MANIFEST.md](../graph/MANIFEST.md) — 7 инвариантов

---

*Последнее обновление: 2026-01-20*
