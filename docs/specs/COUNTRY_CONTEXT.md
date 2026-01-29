# COUNTRY CONTEXT

## Purpose
Country is a context marker, not an ontology node.
It can be used as an additive filter for Query Mode.

## Principles
- No country nodes in the canon.
- Countries live in exports registry only.
- `country:*` behaves like a projection tag (context only).
- Flags are assets, not nodes.

## Example
`country:us` — context marker for regional filtering.

## Flags assets
- Location: `contracts/public/assets/flags/*.png`
- Naming: ISO2 lowercase (`us.png`, `ru.png`)

## See also
- `PROJECTIONS_VOCABULARY.md`
- `CATALOG_ITEM_CONTRACT.md`
