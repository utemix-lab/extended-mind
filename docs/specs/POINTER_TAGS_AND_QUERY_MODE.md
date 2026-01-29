# POINTER TAGS AND QUERY MODE

## Purpose
Pointer-tags are the lightweight query layer for large external catalogs.
They are not canon nodes and should not expand the graph.

## Canon vs Catalogs
- Canon (`universe.json`) stays minimal: domains, practices, characters, anchors.
- Large datasets live in `contracts/public/exports/*` (JSONL).
- Renderers are read-only consumers.

## Pointer-tags
- Tag = anchor for query, not a navigation route.
- Tags appear as text pills; no icons or widgets.
- Capabilities are tags, not practices.
- Projection prefixes are labels for context, not nodes or ontology.

### Tag format
Prefixes (minimal v0):
`cap:`, `provider:`, `domain:`, `country:`

Reserved prefix: `tag:` (not used yet)

Rules:
- Projection prefixes are reserved; do not create nodes for them.
- Entity prefixes are also reserved: `service:`, `model:`, `method:` (no nodes with these ids).
- Do not use `prefix:` strings in `universe.json` node ids (avoid collisions).
- Avoid double forms like `tag:cap:*` unless explicitly needed later.

### Normalization helpers
- `normalizeTag("cap:lipsync") -> { prefix: "cap", key: "lipsync" }`
- `tagToFallbackQuery("cap:lipsync") -> "lipsync"`

## Query Mode (Viewer)
Trigger: click a tag pill.
Behavior:
- Enables Query Mode (no route change).
- Query Mode is a global perception mode, currently rendered in Service panel.
- Service panel shows grouped results from catalog:
  Services / Models / Methods (+ Other if needed).
- Shows active tag and a reset button.

Optional:
- Mark participation in practices from `practice_participation.jsonl`.

## Hook point (future RAG)
Introduce a single resolver:
`resolveQuery(tag) -> { localResults, externalLinks }`

Today:
- `localResults` = JSONL filter by pointer_tags
- `externalLinks` = from registry or fallback query

Future:
- RAG resolver can be added without changing UI.

## Exports manifest
`contracts/public/manifests/assets.manifest.json` includes:
```
"exports": {
  "version": "1.0",
  "catalogs": [
    "exports/ai_catalog.jsonl",
    "exports/practice_participation.jsonl"
  ],
  "registries": [
    "exports/pointer_tags_registry.json",
    "exports/country_registry.json"
  ]
}
```

No schema inside the manifest — only presence and version.

## Composed Capability Tags

Композиционный тег — это capability‑tag, который разворачивается в набор базовых
capability‑тегов. Он не является категорией, Practice или Opportunity.

Пример (документально, не код):
`cap:storytelling` → `cap:text_generation` + `cap:image_generation` + `cap:voice_generation` + `cap:lipsync`

Правила:
- Для пользователя выглядит как один тег.
- Для системы разворачивается в OR/AND‑запрос.
- Для UI не отличается от обычного тега.
- Для канона не отражается.

Запреты:
- Не создавать узлы под композиционные теги.
- Не делать отдельный hub.
- Не путать с Practices.

## See also
- `PROJECTIONS_VOCABULARY.md`
- `CATALOG_ITEM_CONTRACT.md`
- `COUNTRY_CONTEXT.md`
