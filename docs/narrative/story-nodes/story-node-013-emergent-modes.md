# story-node-013

## Название
Несущности проявляются

## Что произошло
Зафиксирован принцип Emergent Modes: Practices и Opportunities возникают контекстно, а не вызываются напрямую.

## Почему это было необходимо
Прямой вызов превращал бы практики и возможности в сущности или кнопки, ломая сцену и смешивая онтологию с восприятием.

## Принятое решение
Считать practices/opportunities несущностями и показывать их только как реакцию на контекст (Query Mode, выбор сервиса).

## Что изменилось в системе
- Введён контекстный hint практики при активном Query Mode.
- Opportunities появляются как stub только после клика по сервису.
- Query Mode отвязан от конкретного окна и остаётся режимом восприятия.

## Открытый вопрос
Какие ещё режимы должны проявляться контекстно, чтобы не закреплять окна преждевременно?

## Что это закладывает
Сцену, где режимы меняются как состояние восприятия, а не как страницы или сущности.

---

## Narrative (опционально)

**evidence:**
- ADR: `010-emergent-modes`
- viewer URL: https://utemix-lab.github.io/dream-graph/visitor.html

**moment:**
Практика перестала быть кнопкой и стала атмосферой сцены.

**voice_hint:**
<!-- narrator: author | system | petrova | vova | neutral -->
<!-- tone: technical | essay | diary | cinematic -->

---

**Related Practices:**
- `practice-direction`

**Refs:**
- ADR: `010-emergent-modes`
- checkpoint: `2026-01-emergent-modes`
