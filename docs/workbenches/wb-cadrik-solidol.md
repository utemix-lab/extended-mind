# Workbench: Solidol

**ID:** wb-cadrik-solidol  
**Character:** CADрик  
**Domain focus:** CAD & 3D / Physical Systems
**Type:** domain / applied-technical
**Slogan:** Солидно. Solid.

## Purpose
Соединить цифру и физику: CAD, 3D, рендер и материальная реализация.

## Focus
- CAD / САПР
- 3D‑моделирование и сцены
- Текстуры, рендеры, материалы
- Инструменты моста “цифра → физика”

## Inputs
- Новые версии софта
- Пайплайны моделинга и рендера
- Скрипты, аддоны, плагины
- Практики физической сборки

## Practices
- `practice-architectural-design` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-systems-design` (см. `docs/specs/PRACTICES_SPEC.md`)
- `practice-visual-thinking` (см. `docs/specs/PRACTICES_SPEC.md`)

## Outputs
- signals.jsonl (релизы, апдейты, находки)
- curated_sets.jsonl (наборы инструментов, пайплайны)
- pointer_tags (cap:cad, cap:render, cap:model, tool:*)

## Preset Context

domain:physical
domain:design
cap:cad

## Boundaries
- Не “всё про 3D”.
- Не учебный курс.
- Не витрина чужих портфолио.

## UI Reflection (Visitor)
- **Story:** Механика, сборка, детали.
- **Service:** Query Mode по инструментам и пайплайнам.
- **System:** Мост к физическим сценам и объектам.

## Risks
- Скатиться в каталог софта.
- Потерять связь с реализацией.
