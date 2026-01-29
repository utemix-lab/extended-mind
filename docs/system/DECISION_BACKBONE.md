# DECISION BACKBONE

Скелет ключевых решений. Каждая запись — краткая формула + ссылки на ADR и story‑nodes.

## Signature decisions (index)

| ID | Decision (one line) | ADR | Story‑node | Enables |
|---|---|---|---|---|
| SD‑001 | Canon stays minimal; catalogs carry scale | `docs/adr/001-avoid-taxonomy-trap.md` | — | Scale without ontology growth |
| SD‑002 | Renderers are read‑only consumers | `docs/adr/002-read-only-consumer-pattern.md` | — | Safe UI evolution |
| SD‑003 | Projections are visual contexts, not nodes | `docs/adr/003-visual-projections.md` | — | Query Mode without canon drift |
| SD‑004 | Signatures exist as separate layer | `docs/adr/005-signature-decisions.md` | — | Stable narrative of decisions |
| SD‑005 | Architecture is law; narrative is life within law | — | — | Prevents canon drift |

## How to update
- New strategic decision → ADR + add a row here
- Decision changed → update row + add reason in ADR

## See also
- `SYSTEM_GUARDRAILS.md`
- `SYSTEM_CHECKS.md`
