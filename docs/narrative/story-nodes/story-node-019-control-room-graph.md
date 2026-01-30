# story-node-019-control-room-graph

## Название
HF control room: граф и генератор в одном рабочем пульте

## Что произошло
В HF Space появился минимальный 2D-граф без физики рядом с генератором постов.

## Почему это было необходимо
Нужен операционный слой (пульт), который читает тот же контракт, но не превращается в отдельный канон и не дублирует витрину.

## Принятое решение
Сделать в Space две вкладки — Graph и Telegram Content — и читать universe.json напрямую.

## Что изменилось в системе
- В Space появился read-only 2D-граф как панель приборов.
- Генератор постов остался отдельной вкладкой.
- Контракты читаются напрямую из contracts без изменения канона.

## Открытый вопрос
Какие метрики и статусы стоит добавить в control room, не превращая его в “вторую систему”?

## Что это закладывает
Операционный режим для автора: контроль состояния без онтологической нагрузки.

---

## Narrative (опционально)

**evidence:**
- `spaces/telegram-content/app.py`
- https://huggingface.co/spaces/utemix/extended-mind-console

**moment:**
Появилась “мастерская”: тот же канон, другой угол зрения.

**voice_hint:**
<!-- narrator: author | system | petrova | vova | neutral -->
<!-- tone: technical | essay | diary | cinematic -->
narrator: neutral
tone: technical

---

**Related Practices:**
- `practice-direction`

**Refs:**
- checkpoint: `2026-01-28`
