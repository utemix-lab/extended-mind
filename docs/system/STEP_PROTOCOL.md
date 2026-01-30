# STEP PROTOCOL

Мягкая процессуальность без бюрократии: каждый шаг связывается с целью и оставляет след.

## Что считается шагом (Step)

**Step** — минимальная запись процесса, когда есть изменение в коде/контрактах/спеках.  
Это мост между целью и реализацией.

## Минимальный след (Step Record v1)

Файл в `docs/steps/` по шаблону `_template.step.md` с 10–15 строками:

- `step_id`
- `intent`
- `goals` (1–3 ссылки на UG/LG/MG/SG)
- `mechanisms_touched`
- `artifacts_changed`
- `user_visible_change`
- `guardrails_checked`
- `next_question`

## Связь с другими следами

- **Step** → что сделали и зачем  
- **Story‑node** → что это значит  
- **ADR** → почему так, а не иначе

## Ритуал (без CI)

Перед/после значимого изменения создаётся Step Record.  
Никаких линтеров/CI-валидаций — только дисциплина и краткость.

## Быстрый старт (опционально)

- `scripts/new-step.ps1`
- `scripts/new-step.sh`

## See also
- `SYSTEM_GOALS.md`
- `SYSTEM_CHECKS.md`
- `MECHANISMS_TO_GOALS.md`
- `DECISION_BACKBONE.md`
