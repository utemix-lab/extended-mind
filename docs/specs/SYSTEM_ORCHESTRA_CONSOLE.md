# SYSTEM ORCHESTRA CONSOLE v0

Статус: **рабочий спец‑контур** (developer/author‑facing).  
Это не новая онтология и не новый слой данных. Это мета‑словарь, который дисциплинирует проектирование UI/режимов и самоописание системы.

## 1) Базовые определения

**ACTORS** — “на что смотрим”  
Канонические узлы/идентичности.

**INSTRUMENTS** — “что делаем”  
Режимы, возможности, пресеты, действия.

**MATTER** — “что отвечает мир”  
Каталоги, строки JSONL, выдача.

## 2) Мэппинг на слои системы

| Слой | Роль |
| --- | --- |
| Canon (`universe.json`) | Actors |
| UI Modes / Actions | Instruments |
| Exports / Catalogs / Registries | Matter |

## 3) Правило миграции

Practice может быть **Actor** или **Instrument**.  
Статус зависит от роли в истории/маршрутах, а не от природы понятия.

## 4) Интерфейс пульта (минимальный контур)

Пульт нужен, чтобы быстро видеть:
1) **Где что живёт** (canon / narrative / rules / language / exports / ui modes).  
2) **Что мы сейчас видим/мыслим** (Actor / Instrument / Matter).  
3) **Как мы это делаем** (какие режимы и контексты активны).

### Минимальные панели/виды
- **Actors:** хабы и ключевые узлы канона (characters/domains/practices/system) + id.
- **Instruments:** режимы UI (Query Mode сейчас; место под будущие).
- **Matter:** exports из manifest (каталоги и реестры).

Важно: это **read‑only**, не редактор.

## 5) Проекция на dev‑режим

Visitor показывает Actors + вызовы Instruments + выдачу Matter.  
Dev‑режим показывает **проекцию пульта**:
- откуда берётся canon,
- какие exports загружены,
- активные контексты (projection/entity stack),
- какие режимы доступны.

Dev — это не “ещё один сайт”, а **режим освещения сцены**.

## 6) DoD (минимально)

- Есть `SYSTEM_ORCHESTRA_CONSOLE.md`.
- Есть `SYSTEM_ATLAS.md`.
- В `SYSTEM_LANGUAGE_LAYER.md` есть ссылка на A/I/M и на этот документ.
