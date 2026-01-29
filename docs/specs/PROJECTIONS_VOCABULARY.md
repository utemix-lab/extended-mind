# PROJECTIONS VOCABULARY (v0)

## Purpose
A projection is a context axis for reading catalogs. It is **not** an entity and **not** a node.

Projection prefixes exist only as context keys for Query/Report modes.
They are labels for filters, not ontology.

## Prefixes (v0)
Minimal set — do not expand in this iteration:

- `domain:` (optional, e.g. `domain-ai`)
- `cap:` (capability / function)
- `provider:` (platform / vendor)
- `country:` (country context, flags)
- `tag:` (reserved for future free tags)

### Non-goals
- `kind:` is **not** a projection in v0. It is a required field on catalog items.
- If needed later, `kind:` may be introduced as a projection, but not now.

## Naming & normalization
- lowercase only
- hyphen separators
- no spaces
- `[a-z0-9-]` for keys

## Semantics
- Projection prefix ≠ entity / ≠ node.
- `pointer_tags` are keys for filters and contexts, not nodes.
- Projection keys do not create or imply canon structure.

## See also
- `CATALOG_ITEM_CONTRACT.md`
- `POINTER_TAGS_AND_QUERY_MODE.md`
- `COUNTRY_CONTEXT.md`
