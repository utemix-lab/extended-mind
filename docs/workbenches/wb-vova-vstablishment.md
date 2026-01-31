# Workbench: VSTablishment

**ID:** wb-vova-vstablishment  
**Character:** Вова  
**Domain focus:** Software & Digital Tools / Music
**Type:** domain / tool radar
**Slogan:** —

## Purpose
Отслеживание и навигация по миру VST-плагинов и музыкального софта.

## Inputs
- Релизы плагинов
- Обновления производителей
- Обзоры и тесты
- Пользовательский опыт

## Practices
- `practice-curation` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-research-thinking` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-possibility-navigation` (см. `docs/specs/PRACTICES_SPEC.md`)

## Outputs
- signals.jsonl (новые плагины, апдейты)
- curated_sets.jsonl (рекомендованные наборы инструментов)
- ai_catalog.jsonl / tools_catalog.jsonl (в перспективе)

## Preset Context

domain:music  
domain:tools

## Boundaries
- Не создаёт полный каталог всех VST.
- Не хранит бинарные файлы или пресеты.
- Фокус на навигации и сравнении.

## UI Reflection (Visitor)
- **Story:** Авторские подборки инструментов.
- **Service:** Query Mode по cap: / provider: / type:.
- **System:** Связи с AI Music Signals.

## Risks
- Разрастание до “магазина плагинов”.
- Потеря актуальности без сигналов.
# Workbench v1

workbench_id: wb-vova-vstablishment
owner_character_id: character-vova
title: VSTablishment
one_liner: Ищет новые инструменты и плагины и превращает их в быстрые маршруты поиска.

## Focus & boundaries
primary_domains: Music & Sound; Software & Tools
secondary_domains: —
related_practices: curation; signal-scanning
non_goals:
- полный каталог всех плагинов
- хранение медиа‑библиотек
- обзоры “топ‑10”

## Inputs
inputs.sources: plugin boutiques, dev blogs, release notes, forums
inputs.signals: release; update; new-maker; unusual-instrument
inputs.query_context: cap:synth; cap:reverb; cap:delay; provider:*

## Preset context
preset_context.description: Query preset for VST discovery
preset_context.projections:
- domain:music
- cap:synth
- cap:reverb
- cap:delay
preset_context.default_refines:
- kind:plugin
preset_context.output_actions:
- open-query-mode

## Pipeline
pipeline.steps:
- scan sources
- shortlist signals
- compare via quick tests
- extract tags/caps
- create/update catalog rows
pipeline.frequency: weekly
pipeline.quality_bar: 3–5 сильных находок за цикл, без “мелкой пыли”

## Outputs
outputs.catalog_rows: tools_catalog.jsonl
outputs.signals: signals.jsonl
outputs.curated_sets: —
outputs.story_nodes: новый паттерн; неожиданный инструмент; смена тренда
outputs.content: short post; digest script

## UI reflection
ui.story: “кадры виртуальной жизни” + краткий манифест радара
ui.system: контекст по доменам Music/Tools + caps
ui.service: preset Query Mode “VSTablishment”

## Risks & guardrails
risks: каталогизация; визуальный шум; медийный захват
guardrails: catalog rows ≠ nodes; terminal visuals only; top‑N only

## Workbench readiness (v1)
- [x] Чёткий фокус (1–2 домена)
- [x] Ясные входные сигналы
- [x] Конкретные выходы (catalog/story/content)
- [x] Ограничения (non_goals)
- [x] Preset Context определён
