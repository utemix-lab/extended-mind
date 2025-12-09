---
title: Repository Structure — v0.1
version: 0.1
type: documentation
status: draft
tags: [structure, repository, onboarding]
lastmod: 2025-01-01
description: "Структура репозитория extended-mind и назначение основных каталогов."
---

# Repository Structure — v0.1

Документ описывает структуру каталога extended-mind и функции каждой части.

---

## Корневая структура

/
├─ README.md
├─ docs/
│ ├─ definitions/
│ ├─ manifest/
│ ├─ templates/
│ ├─ principles/
│ ├─ patterns/
│ ├─ projects/
│ ├─ characters/
│ ├─ adr/
│ ├─ knowledge-base/
│ ├─ rag/
│ ├─ graph/
│ └─ experiments/

markdown
Копировать код

---

## Описание каталогов

### `docs/definitions/`
Базовые определения, словарь, онтология, system prompt, object types.  
Служит источником истины для extended-mind.

### `docs/manifest/`
Философия проекта, позиция post-digital, миссия extended-mind.

### `docs/templates/`
Шаблоны документов:
- project,  
- character,  
- story-node,  
- ADR.

### `docs/principles/`
Метапринципы культуры мышления и разработки.

### `docs/patterns/`
Описание процессов:
- story-node → тезис,  
- обсуждение → ADR,  
- идея → проект.

### `docs/projects/`
Описание всех проектов utemix-lab.

### `docs/characters/`
Описание функциональных акторов (Персонажей) как объектов Мира-3.

### `docs/adr/`
Архитектурные решения.

### `docs/knowledge-base/`
Материалы, подготовленные для RAG:
- чистые чанки,
- отобранные фрагменты,
- будущие индексы.

### `docs/rag/`
Промпты, конфигурации, CLI-скрипты.

### `docs/graph/`
Будущий слой GraphRAG:
- связи,
- сущности,
- уровни абстракции.

### `docs/experiments/`
Песочница для исследований, тестов, прототипов.

---

## Принципы структуры

1. **Каждый документ знает своё место.**  
2. **Хранить только Мир-3.**  
3. **Story-node фиксируются, но не смешиваются со структурой.**  
4. **RAG-папки — всегда отдельны.**  
5. **Расширяемость без ломки основы.**
