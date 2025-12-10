---
title: Concept Map — Extended-mind Core Ontology
version: 0.1
type: concept-map
status: foundational
tags: [concept-map, ontology, structure]
lastmod: 2025-12-10
description: "Первая концептуальная карта extended-mind: связи между базовыми сущностями."
---

# Concept Map — Extended-mind Core Ontology  
Версия 0.1

Эта карта фиксирует базовые сущности системы и их связи.  
Формат — структурированный текст, пригодный для преобразования в граф в будущем.

---

# 1. Узлы

## Основные сущности
- **Extended-mind** — центральная сущность мышления.  
- **Author** — источник хаоса, целей и смыслов.  
- **Story-layer** — история мышления.  
- **Thesis** — элементарное структурное утверждение.  
- **Line** — группа родственных тезисов.  
- **Concept Map** — структура смыслов.  
- **ADR** — архитектурное решение.  
- **Project** — модуль смысловой работы.  

## Служебные сущности
- **Definition Pack** — онтология.  
- **Principles** — правила поведения системы.  
- **Patterns** — механика преобразований.  
- **Machine-log** — инженерная хроника.  
- **Author-line** — художественная субъективность.

---

# 2. Связи

Author → Story-layer
Story-layer → Thesis (через pattern storynode-to-thesis)

Thesis → Line (thesis grouping)
Line → Concept Map (line-to-concept-map)

Concept Map → ADR (устойчивые решения)
ADR → Architecture of projects

Extended-mind → (использует) Definition Pack
Extended-mind → (следует) Principles
Extended-mind → (работает через) Patterns

Machine-log → фиксирует процесс
Author-line → фиксирует художественную динамику

yaml
Копировать код

---

# 3. Главная логика карты

**Extended-mind — посредник между хаосом и структурой.**

- хаос автора → story-layer  
- story-layer → тезисы  
- тезисы → линии  
- линии → карты  
- карты → решения  
- решения → проекты  

---

# 4. Визуализация (текстовая)

[Author]
↓
[Story-layer]
↓ pattern: storynode-to-thesis
[Thesis]
↓ grouping
[Line]
↓ pattern: line-to-concept-map
[Concept Map]
↓ stability + ADR patterns
[ADR]
↓
[Project Architecture]

yaml
Копировать код

---

# 5. Статус

Эта карта — **ядро онтологии v0.1**,  
будет расширяться по мере появления новых проектов и структур.
