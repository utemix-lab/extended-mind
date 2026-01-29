# story-node-017

## Название
Media pipeline + TG batch

## Что произошло
Мы закрепили правила медиа‑пайплайна и добавили пакетную генерацию TG‑постов по дате checkpoint.

## Почему это было необходимо
System Fix собирает много изменений, а внешним аудиториям нужны компактные новости без ручной перегонки.

## Принятое решение
Генератор читает story‑nodes по `checkpoint` и выдаёт 1–N постов, разделённых `---`.

## Что изменилось в системе
– добавлен `MEDIA_PIPELINE.md`  
– TG‑генератор поддерживает batch по checkpoint

## Открытый вопрос
Нужен ли авто‑отбор top‑3 story‑nodes по “весу”?

## Что это закладывает
Стабильный канал самоописания системы для внешнего мира.

---

## Narrative (опционально)

**evidence:**
- docs/system/MEDIA_PIPELINE.md
- spaces/telegram-content/app.py

**moment:**
Система впервые начала “говорить” пакетом, а не единичной заметкой.

**voice_hint:**
<!-- narrator: author | system | petrova | vova | neutral -->
<!-- tone: technical | essay | diary | cinematic -->

---

**Related Practices:**
- `practice-reflection-fixation`
- `practice-possibility-navigation`

**Refs:**
- checkpoint: `2026-01-30`
