# SYSTEM GUARDRAILS

## Core rules (must)
- not a “second internet”
- catalog rows ≠ nodes
- projections ≠ entities
- UI is read‑only in renderers
- large texts are not stored in canon
- practices as nodes are rare (explicitly justified)

## Architecture vs Narrative (hard split)
- Architecture defines structure and constraints.
- Narrative interprets experience and can be subjective.
- Narrative must not change structure, definitions, or canon.
- Architecture must not cite or depend on narrative texts.
- One‑way link: narrative → architecture, never the reverse.

## Anti‑patterns → What to do instead
### “Let’s add a node for every service”
**Почему плохо:** канон раздувается, смысл теряется.  
**Вместо:** добавить строку в каталог + pointer_tags.

### “Tag becomes a practice”
**Почему плохо:** смешение слоёв.  
**Вместо:** оставить тегом или сделать отдельную практику только при явном методологическом смысле.

### “Country page in the graph”
**Почему плохо:** страны — контекст, не сущности.  
**Вместо:** country:* projection + flags as assets.

### “UI equals navigation route”
**Почему плохо:** UI начинает менять канон.  
**Вместо:** Query/Inspect как режимы, не узлы.

### “Long descriptions in canon”
**Почему плохо:** канон становится хранилищем.  
**Вместо:** refs + внешние summaries (future RAG).

## Escalation rule
Если нарушение guardrails необходимо:
1) ADR с явным обоснованием
2) запись в `DECISION_BACKBONE.md`
3) проверка через `SYSTEM_CHECKS.md`

## See also
- `SYSTEM_INTENT.md`
- `SYSTEM_CHECKS.md`
