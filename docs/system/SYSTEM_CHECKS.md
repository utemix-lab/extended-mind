# SYSTEM CHECKS

Сверка текущих шагов с целями + интеграция с System Fix.

## 1) PR review checklist (машины / агенты)
- [ ] Есть ли связь с целями из `SYSTEM_GOALS.md`?
- [ ] Нарушает ли guardrails из `SYSTEM_GUARDRAILS.md`?
- [ ] Новая функция добавлена в `SYSTEM_FUNCTIONS.md`?
- [ ] Новое ограничение добавлено в `SYSTEM_GUARDRAILS.md`?
- [ ] Новая большая идея добавлена в `IDEAS_LOG.md` (Goal link с `[UG-*]` или `[LG-*]`)?
- [ ] Новый механизм добавлен в `MECHANISMS_TO_GOALS.md` с Goal links?
- [ ] Архитектурное изменение имеет narrative trace (story‑node)?
- [ ] Если решение меняет курс — есть ADR + запись в `DECISION_BACKBONE.md`?
- [ ] Архитектурный текст не ссылается на нарратив.

## 2) System Fix checklist (ритуал фиксации)
- [ ] Обновить `SYSTEM_OVERVIEW.md` (состояние)
- [ ] При необходимости обновить `PROJECT_OVERVIEW.md` (концепт)
- [ ] Прогнать checklist из этого документа
- [ ] Убедиться, что есть narrative trace на архитектурные изменения
- [ ] Создать `checkpoints/YYYY-MM-DD-system-fix.md`
- [ ] Commit + push

## 3) Checkpoint review (для человека)
- [ ] Не вырос ли канон без явного решения?
- [ ] Не появились ли “узлы‑каталоги”?
- [ ] Есть ли дрифт между UI и концептом?
- [ ] Все ли новые режимы имеют видимый индикатор в UI?

## 4) Story‑node зрелость (контент)
- [ ] Содержит “почему это важно” (не только “что”)
- [ ] Есть refs/доказательства
- [ ] Связан с практикой или персонажем
- [ ] Не дублирует каталог

## 5) Быстрая сверка целей (30 секунд)
- [ ] Для VISITOR: стало ли легче найти “что можно сделать”?
- [ ] Для LAB: канон остался минимальным?
- [ ] Для MEDIA: есть ли материал для истории/дайджеста?

## See also
- `SYSTEM_GOALS.md`
- `SYSTEM_GUARDRAILS.md`
- `IDEAS_LOG.md`
- `MECHANISMS_TO_GOALS.md`
