# Workbench: Музыка в целом

**ID:** wb-vova-music-general  
**Character:** Вова  
**Domain focus:** Music & Sound Culture
**Type:** domain / cultural radar
**Slogan:** —

## Purpose
Исследование музыки как культурного и исторического феномена: стили, артисты, сцены, альбомы, студии, эпохи.

## Inputs
- Музыкальные релизы
- Критические статьи и обзоры
- Плейлисты и подборки
- Исторические справки и контексты

## Practices
- `practice-curation` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-sound-thinking` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-research-thinking` (см. `docs/specs/PRACTICES_SPEC.md`)

## Outputs
- curated_sets.jsonl (плейлисты, авторские подборки)
- signals.jsonl (упоминания новых релизов или событий)
- pointer_tags (жанры, эпохи, настроения)

## Preset Context

domain:music

## Boundaries
- Не строит полную базу артистов или альбомов.
- Не заменяет стриминговые сервисы.
- Фокус на кураторстве, а не энциклопедии.

## UI Reflection (Visitor)
- **Story:** Золотые плейлисты, визуальная сцена Вовы.
- **Service:** Query Mode по жанрам/эпохам/настроениям.
- **System:** Связь с другими доменами (AI, Visual).

## Risks
- Скатиться в “музыкальную википедию”.
- Потерять авторский голос.
# Workbench v1

workbench_id: wb-vova-music-general
owner_character_id: character-vova
title: Музыка в целом
one_liner: Отслеживает музыку как культуру и карту вкуса, а не как каталог объектов.

## Focus & boundaries
primary_domains: Music & Sound
secondary_domains: Culture; History
related_practices: curation; sensemaking
non_goals:
- энциклопедия артистов и альбомов
- полный каталог жанров
- “топы ради топов”

## Inputs
inputs.sources: playlists, label notes, reviews, podcasts, interviews
inputs.signals: trend; rediscovery; scene-shift; context
inputs.query_context: domain:music; mood:*; era:*

## Preset context
preset_context.description: Query preset for music culture navigation
preset_context.projections:
- domain:music
preset_context.default_refines:
- kind:artist
- kind:album
preset_context.output_actions:
- open-query-mode

## Pipeline
pipeline.steps:
- scan sources
- detect cultural signals
- map to themes
- extract tags
- create signal rows
pipeline.frequency: weekly
pipeline.quality_bar: 2–3 сильных культурных сигнала без “потока шума”

## Outputs
outputs.catalog_rows: —
outputs.signals: signals.jsonl
outputs.curated_sets: curated_sets.jsonl
outputs.story_nodes: новый сдвиг; связка эпох; культурный контекст
outputs.content: digest script; short post

## UI reflection
ui.story: “золотой фонд” (2–3 curated sets) + короткий манифест
ui.system: домен Music + контекстные теги
ui.service: preset Query Mode “Музыка в целом”

## Risks & guardrails
risks: каталогизация; медийный захват
guardrails: catalog rows ≠ nodes; content is derivative; top‑N only

## Workbench readiness (v1)
- [x] Чёткий фокус (1–2 домена)
- [x] Ясные входные сигналы
- [x] Конкретные выходы (catalog/story/content)
- [x] Ограничения (non_goals)
- [x] Preset Context определён
