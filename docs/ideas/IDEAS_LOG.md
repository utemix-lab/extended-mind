# ЖУРНАЛ ИДЕЙ

Каждая идея — карточка, связанная с целью и guardrails.

## Поля
- **ID**
- **Описание**
- **Goal link** (обязательно, `SYSTEM_GOALS.md`, минимум один UG или LG)
- **Functions** (ссылка на `SYSTEM_FUNCTIONS.md`)
- **Risks / guardrails**
- **Minimal experiment**
- **Status**: draft / tested / adopted / archived
- **Next step** (optional)

---

## Идеи

### IDEA‑001 — Лента сигналов
**Описание:** единый поток “сигналов” из каталогов и практик.  
**Goal link:** [UG-1], [MG-1]  
**Functions:** Navigation & Modes, Catalogs & Exports  
**Risks:** превращение в “второй интернет”  
**Minimal experiment:** 1 лента из 10 записей, без UI‑навигации  
**Status:** draft

### IDEA‑002 — Разделение capabilities и practices
**Описание:** формальное правило разделения capability tags и practice nodes.  
**Goal link:** [LG-2]  
**Functions:** Canon, Practices  
**Risks:** смешение уровней  
**Minimal experiment:** один пример “cap:*” vs “practice:*” в docs  
**Status:** draft

### IDEA‑003 — Флаги как контекст
**Описание:** флаги — только контекст/ассеты, без страниц стран.  
**Goal link:** [LG-2], [SG-2]  
**Functions:** Context Stack, Assets  
**Risks:** скрытая онтология стран  
**Minimal experiment:** registry + 3 флага без UI‑входа  
**Status:** adopted

### IDEA‑004 — Контракт виджетов
**Описание:** контракт виджетов UI как ассетов, не узлов.  
**Goal link:** [MG-1], [SG-2]  
**Functions:** Assets  
**Risks:** UI начнёт диктовать канон  
**Minimal experiment:** один widget spec без связей  
**Status:** draft

### IDEA‑005 — Ocean UI (not now)
**Описание:** “океан” тегов/сущностей для обзорной навигации.  
**Goal link:** [UG-2]  
**Functions:** Navigation & Modes  
**Risks:** перегруз, “второй интернет”  
**Minimal experiment:** заморожено, только реестр идеи  
**Status:** archived

### IDEA‑006 — Saved Paths v0
**Описание:** сохранение траекторий и результатов (не коллекций мира).  
**Goal link:** [UG-2], [UG-3]  
**Functions:** Saved Contexts / Saved Paths  
**Risks:** превращение в “второй интернет”  
**Minimal experiment:** 1 приватный сохранённый путь без соц‑слоя  
**Status:** draft

### IDEA‑007 — Narrative prehistory mystification
**Type:** narrative / prehistory mystification  
**Описание:** псевдо‑исторические документы о предыстории системы и персонажей как слой “живой книги”.  
**Goal link:** [UG-5], [LG-5]  
**Functions:** Story‑nodes / Characters  
**Risks:** театр становится каноном; смешение слоёв  
**Minimal experiment:** 2–3 документа в `docs/narrative/prehistory/` с маркировкой non‑canon  
**Status:** draft

### IDEA‑008 — Exportable system + minds‑lorgnette derivative
**Type:** system / exportable service / derivative  
**Описание:** сделать систему экспортируемой (BYO‑key / self‑host), а minds‑lorgnette — производной, агрегирующей разные форматы структурирования (Obsidian/Notion/майнд‑карты/таблицы/графики) в единый вид с ИИ и архитектурным “самопониманием”.  
**Goal link:** [UG-5], [LG-2]  
**Functions:** Catalogs & Exports, RAG hooks, Navigation & Modes  
**Risks:** сервис съедает архитектуру; проксирование ключей; онтологический дрейф  
**Minimal experiment:** README‑раздел BYO‑key + self‑host шаблон (docker‑compose) + локальный vault‑import.  
**Status:** draft

---

## См. также
- `SYSTEM_GOALS.md`
- `SYSTEM_FUNCTIONS.md`
- `SYSTEM_GUARDRAILS.md`
