# story-node-018-vova-workbenches-signals

## Название
Вова как продакшн-организм: workbench’и, сигналы, curated sets

## Что произошло
Описаны workbench’и Вовы v2 и введены JSONL-форматы signals/curated_sets как следы, а не сущности.

## Почему это было необходимо
Без форматов следов и чётких workbench’ей персонаж превращается в абстракцию, а система не может фиксировать живые сигналы без онтологического разрастания.

## Принятое решение
Сделать workbench’и Вовы в v2-форме и хранить сигналы/коллекции как rows в exports, без узлов в каноне.

## Что изменилось в системе
- Workbench’и Вовы зафиксированы как производственные циклы (music / vst / ai).
- Введены seed-форматы signals.jsonl и curated_sets.jsonl.
- Каталожные следы отделены от канона и оформлены как rows.

## Открытый вопрос
Какие минимальные правила качества удержат сигналы живыми, но не превратят слой в “медиа‑поток”?

## Что это закладывает
Персонаж становится реальным операционным организмом, а не просто узлом: сигналы и коллекции дают маршрут и память без онтологии.

---

## Narrative (опционально)

**evidence:**
- `docs/workbenches/wb-vova-music-general.md`
- `contracts/public/exports/signals.jsonl`
- `contracts/public/exports/curated_sets.jsonl`

**moment:**
Появилась первая “живая” петля: сигнал → контекст → curated set.

**voice_hint:**
<!-- narrator: author | system | petrova | vova | neutral -->
<!-- tone: technical | essay | diary | cinematic -->
narrator: system
tone: essay

---

**Related Practices:**
- `practice-curation`

**Refs:**
- universe.json: `character-vova`
- checkpoint: `2026-01-28`
