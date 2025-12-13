---
title: RAG Query Specification v0.1
version: 0.1
type: spec
status: draft-core
tags: [rag, query, specification]
lastmod: 2025-12-13
description: "Спецификация того, как extended-mind формулирует запросы к RAG-индексу."
---

# RAG Query Specification v0.1

Этот документ описывает, **как extended-mind должен задавать вопросы** к векторному индексу:

- какие бывают типы запросов,
- какие фильтры использовать,
- какой глубины retrieval нужен,
- как выглядят параметры запроса.

---

## 1. Общее устройство запроса

Логический запрос к индексу состоит из:

```jsonc
{
  "query_text": "естественный язык",
  "mode": "fast" | "deep" | "architect",
  "filters": {
    "type_in": [...],
    "status_not_in": [...],
    "tags_any": [...],
    "project": "optional"
  },
  "top_k": 8
}
Физически это может быть словарь/объект в Python,
но на уровне спецификации важно содержимое полей.

2. Типы вопросов (semantic intent)
Extended-mind должен различать хотя бы 4 базовых типа вопросов:

Definition — “что это?” / “кто это?”

пример: “Что такое story-layer?”

пример: “Кто такой author-line?”

Decision/Reasoning (ADR) — “почему так?” / “зачем так решили?”

пример: “Почему мы сначала делаем RAG, а не граф?”

пример: “Почему extended-mind говорит от первого лица?”

Pattern/Process — “как это делается?” / “что делать в такой ситуации?”

пример: “Как превратить story-node в тезисы?”

пример: “Как отделять Мир-2 от Мира-3 при структурировании?”

Project/Context — “где граница?” / “как это связано с …?”

пример: “Где граница между extended-mind и V&P?”

пример: “Что такое thin-tank внутри V&P?”

На v0.1 extended-mind может определять тип эвристически
или просто руками (ты сам знаешь, что сейчас спрашиваешь).

3. Маппинг типа вопроса → фильтры
3.1. Definition
jsonc
Копировать код
{
  "mode": "fast",
  "filters": {
    "type_in": ["definition", "concept-map", "core"],
    "status_not_in": ["draft-raw", "private"]
  },
  "top_k": 5
}
цель: короткий, точный ответ,

источник: определения, концепты, system-prompt.

3.2. Decision (ADR)
jsonc
Копировать код
{
  "mode": "deep",
  "filters": {
    "type_in": ["adr", "principle", "manifest"],
    "status_not_in": ["draft-raw", "private"]
  },
  "top_k": 10
}
цель: “почему так решили”,

источник: ADR, принципы, манифест.

3.3. Pattern / Process
jsonc
Копировать код
{
  "mode": "deep",
  "filters": {
    "type_in": ["pattern", "project", "definition"],
    "status_not_in": ["draft-raw", "private"]
  },
  "top_k": 12
}
цель: “как действовать”,

источник: паттерны, описания проектов, иногда определения.

3.4. Project / Context
jsonc
Копировать код
{
  "mode": "deep",
  "filters": {
    "type_in": ["project", "concept-map", "manifest", "definition"],
    "status_not_in": ["draft-raw", "private"],
    "tags_any": ["vova-and-petrova"]   // если вопрос про V&P
  },
  "top_k": 12
}
цель: границы проекта, связи, контекст,

источник: project-frame, концепт-карты, манифест.

4. Режимы retrieval (mode)
4.1. fast
top_k: 3–6

Используется для:

определений,

простых терминов,

быстрых уточнений.

4.2. deep
top_k: 8–15

Используется для:

архитектурных вопросов,

описаний проектов,

поиска паттернов.

4.3. architect
top_k: 12–20

Та же техника, что deep, но:

допускается больше типовых источников,

меньше фильтрации,

больше “обзорных” чанков (manifest, principles, concept-maps).

Используется, когда вопрос:

явно затрагивает архитектуру и философию одновременно,

например: “Как extended-mind должен относиться к story-layer, чтобы не сойти с ума?”

5. Примеры запросов (логически)
Пример 1: Определение story-layer
Вопрос:

“Что такое story-layer в extended-mind?”

Запрос:

jsonc
Копировать код
{
  "query_text": "определение story-layer в extended-mind",
  "mode": "fast",
  "filters": {
    "type_in": ["definition", "concept-map", "core"],
    "status_not_in": ["draft-raw", "private"],
    "tags_any": ["story-layer"]
  },
  "top_k": 5
}
Пример 2: Почему RAG раньше графа?
Вопрос:

“Почему мы решили начинать с RAG, а не с графа?”

Запрос:

jsonc
Копировать код
{
  "query_text": "почему extended-mind сначала использует RAG, а не графовые БД",
  "mode": "deep",
  "filters": {
    "type_in": ["adr", "principle"],
    "status_not_in": ["draft-raw", "private"],
    "tags_any": ["rag", "graph"]
  },
  "top_k": 10
}
Пример 3: Как выделять story-node
Вопрос:

“Как правильно выделять story-node из чата?”

Запрос:

jsonc
Копировать код
{
  "query_text": "шаги и правила выделения story-node из чатов",
  "mode": "deep",
  "filters": {
    "type_in": ["pattern", "definition"],
    "status_not_in": ["draft-raw", "private"],
    "tags_any": ["story-node", "story-layer"]
  },
  "top_k": 12
}
Пример 4: Граница между extended-mind и V&P
Вопрос:

“Где проходит граница между extended-mind и проектом «Вова и Петрова»?”

Запрос:

jsonc
Копировать код
{
  "query_text": "граница между extended-mind и проектом «Вова и Петрова»",
  "mode": "deep",
  "filters": {
    "type_in": ["project", "concept-map", "manifest"],
    "status_not_in": ["draft-raw", "private"],
    "tags_any": ["extended-mind", "vova-and-petrova"]
  },
  "top_k": 12
}
6. Как extended-mind должен “думать” до запроса
Перед тем, как дергать индекс, extended-mind должен:

Попробовать классифицировать вопрос:

“что такое...” → definition,

“почему...” → adr/decision,

“как...” → pattern,

“где граница/какова роль...” → project/context.

Выбрать режим:

definition → fast,

adr/pattern/project → deep,

сложные комбинированные вопросы → architect.

Сформировать фильтры:

по type_in,

по tags_any (если вопрос явно про V&P, evoquant и т.п.),

всегда исключать draft-raw, private.

7. Статус и развитие
v0.1:

всё делается вручную или очень простыми эвристиками,

допускается, что автор сам знает, какой тип вопроса он задаёт.

В будущих версиях:

можно ввести:

классификатор типа вопроса,

более умные фильтры,

разные индексы для разных классов данных.

Но уже v0.1 даёт extended-mind понятный способ общения с индексом,
а не “просто подобрали топ-10 похожих текстов и склеили ответ”.
