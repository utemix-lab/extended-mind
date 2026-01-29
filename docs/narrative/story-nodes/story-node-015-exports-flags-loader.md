# story-node-015

## Название
Exports + flags + loadExports

## Что произошло
Мы перевели exports на структурированный manifest, подготовили флаги как ассеты и сделали единый загрузчик `loadExports()` с fallback.

## Почему это было необходимо
Без единой точки загрузки и стандарта экспортов система не масштабируется и теряет предсказуемость.

## Принятое решение
Exports описываются в manifest (`catalogs`/`registries`), флаги живут в `assets/flags/*.png`, загрузка идёт через `loadExports()`.

## Что изменилось в системе
– единый формат `exports` в `assets.manifest.json`  
– централизованный загрузчик экспортов  
– флаги приведены к ISO2 PNG

## Открытый вопрос
Нужно ли добавлять в manifest строгую схему в CI?

## Что это закладывает
Масштабируемую загрузку каталогов и контекстных ассетов без роста канона.

---

## Narrative (опционально)

**evidence:**
- viewer: dream-graph / Query Mode

**moment:**
Стало ясно, что каталоги можно подключать как модули, не трогая граф.

**voice_hint:**
<!-- narrator: author | system | petrova | vova | neutral -->
<!-- tone: technical | essay | diary | cinematic -->

---

**Related Practices:**
- `practice-architectural-design`
- `practice-system-thinking`

**Refs:**
- checkpoint: `2026-01-30`
