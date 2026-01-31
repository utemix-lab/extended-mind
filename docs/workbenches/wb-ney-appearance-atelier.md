# Workbench: Appearance Atelier

**ID:** wb-ney-appearance-atelier  
**Character:** Нэй  
**Domain focus:** Generative Visual Systems
**Type:** domain-spanning / infrastructural
**Slogan:** Красота — побочный эффект воспроизводимости.

## Purpose
Генеративный визуал как технология проявления: не “красиво”, а “как это работает”.

## Focus
- ComfyUI и графовые пайплайны
- Модели и LoRA
- Сервисы и инференс‑цепочки
- Сборка воспроизводимых процедур

## Inputs
- Новые модели и релизы
- Пайплайны и рецепты
- Технические разборы
- Ошибки и странности генерации

## Practices
- `practice-research-thinking` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-system-thinking` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-visual-thinking` (см. `docs/specs/PRACTICES_SPEC.md`)

## Outputs
- signals.jsonl (релизы, патчи, модели)
- curated_sets.jsonl (пайплайны, рецепты, сборки)
- pointer_tags (model, stack, cap, provider)

## Preset Context

domain:visual
domain:ai
cap:gen

## Boundaries
- Не про “искусство ради искусства”.
- Не про галереи и выставки.
- Фокус на инженерии проявления.

## UI Reflection (Visitor)
- **Story:** “Как выглядит, и почему так”.
- **Service:** Query Mode по моделям/пайплайнам.
- **System:** Сквозная техническая оптика по всем сценам.

## Risks
- Скатиться в каталог моделей.
- Потерять человеческое объяснение.
