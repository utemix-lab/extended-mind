# Character Specification

## Определение

> **Character** — это не набор характеристик, а потенциальная траектория внутри системы,  
> которая со временем может проявиться через Practices, Styles, Labs и Story-nodes.

**Формула:**
> Персонаж = точка сборки будущих ростков, не готовый образ.

### Расширение v1 (субъект и проекции)

- Персонаж — устойчивый агент мышления с собственными практиками и языком
- Узел персонажа в `universe.json` — якорь, не вся сущность
- Проекции персонажа — следы присутствия (внутренние и внешние)
- Верстаки — способы работы и сцены, не узлы канона

**Короткая формула:**
> Персонаж — субъект. Узел — якорь. Проекции — следы. Верстаки — способы работы.

---

## Принципы

### 1. Плоский уровень

- `type: character`
- Без подтипов
- Без иерархий между персонажами

### 1.5. Асимметрия как системное преимущество

- Персонажи могут различаться по функциям, объёму и типам workbench’ей.
- Один живёт в доменах, другой — над доменами, третий — между ними.
- Асимметрия усиливает глубину системы, но не вводит иерархий.

### 2. Персонаж как контейнер (не контент)

Персонаж — это носитель будущих:
- Практик
- Стилей
- Лабораторий
- Проектов
- Нарративов

**Не заполнять заранее, а резервировать.**

### 3. Персонаж как траектория

Персонаж проявляется через следы:
- Story-nodes, где он упоминается
- Practices, которые он использует
- Стили, которыми он владеет

---

## Допустимые связи (интерфейс)

| Связь | Тип | Статус |
|-------|-----|--------|
| `character → practice` | relates | Активна |
| `character → domain` | relates | Активна |
| `character → style` | owns | Будущее |
| `character → lab` | owns | Будущее |
| `character → project` | owns | Будущее |
| `story-node → character` | appears_in | Односторонне |

**Это контракт будущего, не требование наполнения.**

---

## Текущие персонажи

| ID | Имя | Связанные домены | Связанные практики |
|----|-----|------------------|-------------------|
| `character-vova` | Вова | music, tools | sound-thinking, curation |
| `character-petrova` | Петрова | visual, design | direction, branding |
| `character-vasya` | Вася | visual, interactive | direction, interactive-thinking |
| `character-ney` | Нэй | visual, ai | research-thinking, system-thinking |
| `character-cadrik` | CADрик | design, physical | architectural-design, systems-design |
| `character-runa` | Руна | ai, software | research-thinking, system-thinking |
| `character-hinto` | Hinto | software, ai | research-thinking, ecosystem-thinking |
| `character-ancy` | Ancy | knowledge | reflection-fixation, research-thinking |
| `character-gamych` | Геймыч | games, math | interactive-thinking, system-thinking |
| `character-dizy` | Дизи | design | visual-thinking, systems-design |
| `character-ai` | ИИ | ai | system-thinking, research-thinking |
| `character-author` | Автор | system | reflection-fixation, curation |

---

## Будущие владения (не реализованы)

| Персонаж | Стиль | Лаборатория |
|----------|-------|-------------|
| Дизи | Киберантика | ComfyUI workflow |
| Ancy | — | minds-lorgnette |
| Руна | — | code/agents |

---

## Что НЕ делать

- ❌ Не добавлять подтипы персонажей
- ❌ Не описывать характеры и биографии
- ❌ Не делать "персонаж = профессия"
- ❌ Не визуализировать портфолио заранее
- ❌ Не превращать workbench в узел канона

---

## Ключевая формула

> Система растёт через Practices и Story-nodes.  
> Персонажи — это точки сборки этих ростков.  
> Мы закладываем точки сборки, но не выращиваем их заранее.

## See also
- `CHARACTER_WORKBENCH_SPEC.md`
- `docs/narrative/story-nodes/story-node-020-character-portraits-and-naming.md`
