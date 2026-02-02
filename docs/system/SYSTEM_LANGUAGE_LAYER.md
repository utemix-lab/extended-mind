# SYSTEM LANGUAGE LAYER v1

## Что это

**System Language Layer** — мета‑слой, который задаёт язык и конституцию системы:  
правила именования, распределения ролей, визуальной выразительности и способа говорить о себе.

Короткая формула:  
**Вы проектируете язык живой системы.**

## Что это не
- не продукт
- не UI
- не lore
- не сумма архитектуры и нарратива

Это слой, из которого уже могут рождаться продукты, интерфейсы, контент и сервисы.

## Три уровня именования (рабочие)

**A — Language of the System**  
Graph‑native narrative system language.  
Внутри: **System Language**.

**B — System Constitution**  
Constitution & Semantics Phase: определение границ, ролей и допустимых форм.

**C — Rules & фиксации**  
Конкретные правила и формулы (см. ниже).

## Ключевые правила (v1)

### 1) Role Attribution Rule
Фича не принадлежит системе напрямую — она проживается через персонажа.  
Персонаж = точка зрения + стиль + ограничения.

**Где живёт:** `SYSTEM_GUARDRAILS.md`  
**Связи:** `CHARACTER_WORKBENCH_SPEC.md`

### 2) Projection of Capability
Активы/портфолио/практики не «владение», а проекция возможностей.  
Персонаж — носитель демонстрации, а не «владелец».

**Где живёт:** `CHARACTER_WORKBENCH_SPEC.md`  
**Связи:** `PRACTICES_SPEC.md`, `DECISION_BACKBONE.md`

### 3) Expressive Coverage Principle
Разные персонажи показывают разные выразительные и технические возможности среды.  
Визуал — демонстрационный слой, связанный с брендом и портфолио.

**Где живёт:** `VISUAL_GUARDRAILS.md`  
**Связи:** `CHARACTERS.md`

### 4) Naming Guardrail v1
Системное — английское, нарративное — мультиязычное.  
Канон остаётся английским, витрина — живой.

**Где живёт:** `VISUAL_GUARDRAILS.md`, `NAMING_CANON.md`

## Actors / Instruments / Matter (ядро языка)
Базовый язык роли для проектирования UI и режимов:
- **Actors** — “на что смотрим” (канон/узлы).
- **Instruments** — “что делаем” (режимы/действия/пресеты).
- **Matter** — “что отвечает мир” (каталоги/выдача).

**См.** `SYSTEM_LANGUAGE_ACTORS_INSTRUMENTS_MATTER.md`  
**См.** `docs/specs/SYSTEM_ORCHESTRA_CONSOLE.md`

## Архитектура vs нарратив

Это **семантическая архитектура, выраженная через нарративные формы**.  
Нарратив здесь — не цель, а способ удерживать сложность.

## Зачем это нужно
- даёт единый язык для тебя, агентов и будущей LLM
- объясняет, что можно/нельзя превращать в узлы и фичи
- сохраняет минимальность канона при росте системы

## See also
- `SYSTEM_GUARDRAILS.md`
- `DECISION_BACKBONE.md`
- `CHARACTER_WORKBENCH_SPEC.md`
- `VISUAL_GUARDRAILS.md`
- `PRACTICES_SPEC.md`
- `NAMING_CANON.md`
- `docs/narrative/system-language-layer.md`
- `docs/system/SYSTEM_ATLAS.md`
- `docs/specs/SYSTEM_ORCHESTRA_CONSOLE.md`
- `docs/system/SYSTEM_PRACTICES_MATRIX.md`
