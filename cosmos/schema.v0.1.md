# Cosmos Map Schema v0.1

## Node

Required fields:
- `id` (string): unique id, recommended prefix (e.g. `project:extended-mind`)
- `label` (string): display name
- `type` (string): one of `project | layer | artifact | actor | system`
- `status` (string): one of `draft | active | stable | archived`

Optional fields:
- `notes` (string)
- `tags` (array of strings)
- `meta` (object)

## Edge

Required fields:
- `id` (string): unique id
- `source` (string): node id
- `target` (string): node id
- `type` (string): relation (free string)
- `status` (string): one of `draft | active | stable | archived`

Optional fields:
- `notes` (string)
- `meta` (object)

## Versioning

- Map file version in name: `cosmos-map.vX.Y.json`
- Schema file version in name: `schema.vX.Y.md`
- Bump minor for additive fields, major for breaking changes.
