# Cosmos Map Schema v0.2

## Node

Core fields:
- `id` (string)
- `label` (string)
- `type` (project | layer | artifact | actor | system)
- `status` (draft | active | stable | archived)
- `notes` (string, optional)
- `tags` (string[], optional)
- `importance` (1..5)
- `refs` (array of {kind,title,url})

Custom fields:
- `props` (object, optional)
- `props_meta` (object, optional; per-key metadata)

## Edge

Fields:
- `id` (string, optional)
- `source` (node id)
- `target` (node id)
- `kind` (string)
- `weight` (1..5)
- `directed` (bool)
- `notes` (string, optional)

## Versioning

- Map file version in name: `cosmos-map.vX.Y.json`
- Schema file version in name: `schema.vX.Y.json` + `schema.vX.Y.md`
- Minor for additive changes, major for breaking changes.
