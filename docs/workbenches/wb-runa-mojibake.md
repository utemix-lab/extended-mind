# Workbench: Mojibake

**ID:** wb-runa-mojibake  
**Character:** Руна  
**Domain focus:** Code & Research Infrastructure
**Type:** infrastructure / research
**Slogan:** —

## Purpose
Код и исследование как инфраструктура: RAG, ресерч‑пайплайны, системные сборки.

## Focus
- RAG и retrieval‑цепочки
- Инструменты ресерча
- Протоколы и интеграции
- Сквозные пайплайны для системы

## Inputs
- Новые библиотеки и статьи
- Эксперименты с retrieval
- Внутрисистемные контуры (dream-graph, contracts)
- Технические провалы и инсайты

## Practices
- `practice-research-thinking` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-system-thinking` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-ecosystem-thinking` (см. `docs/specs/PRACTICES_SPEC.md`)

## Outputs
- signals.jsonl (релизы, паттерны, открытия)
- curated_sets.jsonl (toolchains, подходы, рецепты)
- pointer_tags (cap:rag, cap:retrieval, stack:*, method:*)

## Preset Context

domain:ai
domain:software
cap:rag

## Boundaries
- Не продуктовая разработка.
- Не “всё про LLM”.
- Фокус на инфраструктуре и исследовании.

## UI Reflection (Visitor)
- **Story:** “как устроено внутри”.
- **Service:** Query Mode по методам и стекам.
- **System:** Курирует контуры `dream-graph` и `contracts`.

## Risks
- Слишком абстрактно для внешней сцены.
- Уход в детали без полезных следов.
