# CATALOG ITEM CONTRACT (v0)

## Purpose
Catalog items are **rows**, not nodes. They live in JSONL exports and never become canonical entities.

## Minimal JSONL record
```json
{
  "id": "service:krea",
  "kind": "service",
  "title": "KreaAI",
  "pointer_tags": ["cap:image_to_image", "cap:lipsync", "provider:krea", "country:us"],
  "external_refs": { "home": "https://example.com", "hf": "...", "pwc": "..." }
}
```

## Required fields
- `id` — string, format `<kind>:<slug>`
- `kind` — string, required
- `title` — string, short display name
- `pointer_tags` — array of strings (key required, may be empty)

## Optional fields
- `external_refs` — object: string keys → URL strings

## Normalization rules
### `id`
Format: `<kind>:<slug>`
- `kind`: lowercase identifier (`service`, `model`, `method`, ...)
- `slug`: lowercase, hyphenated, `[a-z0-9-]`, no spaces

Examples:
- `service:krea`
- `model:sdxl`
- `method:consistency-models`

### `pointer_tags`
- Key is required.
- Array may be empty, but production rows should have ≥1 tag.
- `country:*` is a projection context, not a canonical entity.

### `external_refs`
- Values are URLs only.
- No long text, no markdown, no embedded descriptions.
- Depth comes from external refs or future RAG summaries.

## Non-goals
- No catalog item becomes a canon node.
- No expansion of the universe graph from catalog rows.

## See also
- `PROJECTIONS_VOCABULARY.md`
- `POINTER_TAGS_AND_QUERY_MODE.md`
- `COUNTRY_CONTEXT.md`
