---
title: Extended-mind Index
version: 0.1
type: index
status: foundational
tags: [index, navigation, ontology, structure]
lastmod: 2025-12-10
description: "Главная навигационная карта репозитория extended-mind."
---

# Extended-mind Index  
Версия 0.1

Этот документ — карта системы.  
Он связывает все ключевые элементы extended-mind v0.1  
и показывает, как ориентироваться внутри репозитория.

Extended-mind — это системное пространство мышления.  
Его документы распределены по ролям: определения → принципы → паттерны → решения → проекты.

---

# 1. Основная логика репозитория

Вся архитектура extended-mind строится вокруг цепочки смыслов:

**Story-layer → Тезисы → Линии → Карты смыслов → Архитектура (ADR) → Проекты → Публичные слои**

Каждый раздел репозитория отражает один из этапов этого процесса.

---

# 2. Definitions — фундамент онтологии

**Путь:** `docs/definitions/`

Definition Pack — основа для RAG и структурного мышления.  
Без чётких определений extended-mind не может устойчиво мыслить.

### Ключевые документы:
- `definition-pack-v0.1.md` — базовая онтология v0.1  
- `story-layer.md` — определение story-layer  
- `value-of-story-node.md` — ценность story-node

---

# 3. Principles — культура мышления

**Путь:** `docs/principles/`

Принципы задают “психологию” extended-mind — как он себя ведёт, что считает важным, чего избегает.

### Ключевые документы:
- `honesty-and-anti-speculation.md` — честность и анти-спекулятивность  
- `structure-vs-chaos.md` — принцип перехода от хаоса к структуре  

---

# 4. Manifest — как мыслит система

**Путь:** `docs/manifest/`

Манифесты определяют позицию extended-mind в диалоге с автором.

### Ключевые документы:
- `how-extended-mind-thinks.md` — единый голос, логика и поведение  
- `author-and-machine.md` — распределение ролей между человеком и системой  
- `why-extended-mind.md` — (в разработке) смысл существования extended-mind  

---

# 5. ADR (Architecture Decision Records)

**Путь:** `docs/adr/`

ADR фиксируют ключевые архитектурные решения — точки, где система “кристаллизуется”.

### Принятые решения:
- `adr-0001.md` — (появится позже: базовая структура)  
- `adr-0003-rag-first-graph-later.md`  
- `adr-0004-post-digital-honesty.md`  
- `adr-0005-characters-as-actors-mir3.md`  
- `adr-0006-single-agent-architecture.md`  
- `adr-0007-story-layer-separation.md`  
- `adr-0008-role-of-definition-pack.md`  
- `adr-0009-why-extended-mind-must-speak-in-first-person.md`  
- `adr-0010-why-projects-must-be-modular.md`  
- `adr-0011-separation-of-author-line-and-machine-log.md`  
- `adr-0012-what-cannot-be-automated.md`  

ADR — это самые устойчивые решения системы.  
Они определяют поведение extended-mind так же, как стандарты определяют поведение языка программирования.

---

# 6. Patterns — механика мышления

**Путь:** `docs/patterns/`

Паттерны описывают, *как extended-mind действует*:

- как извлекает смысл из хаоса,  
- как превращает мысль в структуру,  
- как проверяет устойчивость,  
- как оформляет проекты.

### Ключевые документы:
- `storynode-to-thesis.md` — преобразование сырья в тезис  
- `thesis-to-adr.md` — путь к архитектурному решению  
- `thesis-decomposition.md` — разложение сложных тезисов  
- `line-consolidation.md` — объединение линий  
- `stability-check.md` — проверка устойчивости  
- `project-framing.md` — превращение идеи в проект  
- `bias-detection.md` — обнаружение искажений  

---

# 7. Projects — первый уровень применения

**Путь:** `docs/projects/`

Каждый проект utemix-lab — отдельный модуль:  
он имеет миссию, границы, синхронизацию с extended-mind.

### Документы:
- `extended-mind-overview.md` — структура центрального проекта  

(Дочерние проекты будут добавляться постепенно.)

---

# 8. Шаблоны — строительные блоки

**Путь:** `docs/templates/`

Шаблоны делают систему машиночитаемой и единообразной.

- `project-template.md`  
- `story-node-template.md`  
- `character-template.md`  

Используются для автоматизации и единого формата.

---

# 9. Как читать репозиторий новичку

1. Прочитать `README.md`  
2. Прочитать этот файл (`docs/index.md`)  
3. Изучить Definitions  
4. Пройтись по Principles  
5. Понять Manifest  
6. Посмотреть ADR — как принимались решения  
7. Изучить Patterns — как система думает  
8. Перейти к проектам

---

# 10. Как этим пользуется машина

RAG использует этот репозиторий как:

- онтологию,
