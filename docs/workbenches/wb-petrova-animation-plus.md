# Workbench: Анимация +

**ID:** wb-petrova-animation-plus  
**Character:** Петрова  
**Domain focus:** Visual & Media Arts
**Type:** domain / art radar
**Slogan:** —

## Purpose
Исследование анимации и визуального искусства как формы мышления, авторского высказывания и культурного процесса.

## Focus
- Авторская анимация
- Короткометражные и полнометражные фильмы
- Режиссёры, художники, студии
- Фестивали и награды
- Экспериментальная и AI-анимация

## Inputs
- Премьеры мультфильмов
- Фестивальные программы
- Интервью с авторами
- Визуальные эксперименты и новые технологии

## Practices
- `practice-direction` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-visual-thinking` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-curation` (см. `docs/specs/PRACTICES_SPEC.md`)

## Outputs
- signals.jsonl (премьеры, награды, фестивальные события)
- curated_sets.jsonl (подборки фильмов, авторов, направлений)
- pointer_tags (format, genre, festival, tech)

## Preset Context

domain:visual
genre:animation

## Boundaries
- Не строит полную онтологию анимации.
- Не является кино-базой или каталогом студий.
- Работает через кураторство и авторский взгляд.

## UI Reflection (Visitor)
- **Story:** Визуальная сцена — кадры, образы, настроение.
- **Service:** Query Mode по фестивалям, авторам, форматам.
- **System:** Связь с практиками режиссуры и визуального сторителлинга.

## Risks
- Скатиться в энциклопедичность.
- Потерять авторский фокус.
