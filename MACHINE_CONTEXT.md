# MACHINE_CONTEXT.md

> Каноническая точка входа контекста для LLM / IDE-агентов

**version:** 1.3  
**last_updated:** 2026-01-28  
**canon_nodes:** 37  
**canon_edges:** 57

---

## 0. Как использовать этот документ

Этот файл — **контракт** для любого LLM или агента.

- Копируй целиком в начало сессии
- Не выводи замысел из истории чатов или устаревших файлов
- При противоречии с другими документами — этот файл приоритетнее

---

## 1. Фаза системы (КРИТИЧЕСКИ ВАЖНО)

Система в фазе **саморазворачивания и наблюдения**.

- Фундаментальная архитектура ЗАВЕРШЕНА и ЗАМОРОЖЕНА
- Машинная логика роста оказалась яснее человеческого замысла
- Роль человека — **наблюдатель и корректор траектории**

⚠️ Запрещено продолжать реализацию ранних архитектурных идей без явного подтверждения.

---

## 2. Единственный источник истины (SSoT)

```
contracts/public/graph/universe.json
```

Этот файл определяет:
- узлы (nodes)
- связи (edges)
- метаданные (Node Contract v1)

**Ни один README или Playbook не определяет структуру системы.**

---

## 3. Один граф — множество проекций

В системе **ОДИН граф**.

- Views (Knowledge / System / All) — это фильтры, не копии
- Запрещено создавать мета-граф, граф графов, отдельный граф для UI

---

## 4. Роли репозиториев

| Репо | Роль | Права |
|------|------|-------|
| **extended-mind** | Редактор, интроспекция | WRITE канон |
| **contracts** | Данные: канон, ассеты, тексты | READ-ONLY |
| **dream-graph** | Web-рендер | READ-ONLY |
| **godot-sandbox** | Опциональная песочница | READ-ONLY, может быть удалён |

---

## 5. Node Contract v1 (инвариант)

Каждый узел обязан иметь:

| Поле | Примеры | Дефолт |
|------|---------|--------|
| id | глобальный, неизменяемый | — |
| type | root, hub, domain, concept, character, module, spec, process, policy, practice | concept |
| visibility | public, internal, hidden | public |
| status | core, expandable, frozen, deprecated | expandable |
| semantics.role | container, mediator, content, description | content |

❗ Расширять контракт без явного разрешения запрещено.

---

## 6. Текущая структура графа

```
universe (root)
├── system (root)
│   └── system-graph (hub)
│       ├── module-extended-mind
│       ├── module-dream-graph
│       ├── module-contracts
│       ├── module-godot-sandbox
│       ├── policy-ssot
│       ├── process-edit-to-render
│       ├── spec-universe-graph
│       └── spec-contracts-public
├── characters (hub)
│   ├── character-vova
│   ├── character-petrova
│   ├── character-ai
│   ├── character-runa
│   ├── character-hinto
│   ├── character-ancy
│   ├── character-ney
│   ├── character-dizi
│   ├── character-cadrik
│   ├── character-geymych
│   ├── character-author
│   └── character-vasya
├── domains (hub)
│   ├── domain-ai (AI & Computational Models)
│   ├── domain-music (Music & Sound Culture)
│   ├── domain-visual (Visual & Media Arts)
│   ├── domain-knowledge (Knowledge & Cognitive Systems)
│   ├── domain-dev (Software & Digital Tools)
│   ├── domain-design (Design & Aesthetic Systems)
│   ├── domain-physical (Physical & Fabrication)
│   └── domain-interactive (Interactive & Game Culture)
└── practices (hub)
    ├── practice-direction (Режиссура)
    └── practice-branding (Брендинг)
```

---

## 7. Персонажи и домены

**Персонажи** — медиаторы, не категории. "Знают дорогу" по графу.

**Домены** — крупные континенты знаний, без поддоменов на этой фазе.

---

## 8. 3S-окна (Story/System/Service)

**НЕ являются проекциями графа.**

Это:
- театральный / сценографический слой
- область эксперимента
- намеренно нестабильный

Канон даёт контент, рендеры решают как показывать.

---

## 9. Что заморожено

До отдельного решения ЗАПРЕЩЕНО:
- ❄️ валидаторы
- ❄️ content refs
- ❄️ CI / deploy
- ❄️ улучшения editor
- ❄️ новые типы узлов/рёбер
- ❄️ сложные политики

---

## 10. Инструкция агенту

1. Прочитать этот документ
2. Прочитать последний checkpoint в `extended-mind/docs/checkpoints/`
3. Действовать консервативно:
   - небольшие добавления
   - следовать существующей структуре
   - избегать концептуальных скачков

При новой структурной идее → ОСТАНОВИТЬСЯ → зафиксировать → ждать подтверждения.

---

## 11. Модель совместной работы (рекомендации)

- Есть внешний нарративный партнёр (без репо), с которым обсуждаются общие вопросы.
- IDE-агент переводит эти идеи в реалии системы, а не исполняет их буквально.
- Человек корректирует курс, агент объясняет решения по запросу.
- Существенные сдвиги фиксируются в story-node и предлагаются к публикации.
- Публикация — по команде автора; рекомендация агента допустима.

---

## 12. Быстрый старт для нового кодера

1. `MACHINE_CONTEXT.md` (этот файл)
2. `docs/SINGLE-SOURCE-PLAYBOOK.md`
3. Последний checkpoint в `docs/checkpoints/`
4. Канон: `contracts/public/graph/universe.json`
5. Narrative: `docs/narrative/NARRATIVE_LAYER.md`
6. Шаблон story-node: `docs/narrative/templates/story-node.md`
7. UI правила: `contracts/public/ui/INTERACTION_RULES.md`, `SCENOGRAPHY_RULES.md`

---

## 13. Главная директива

> Не оптимизировать на полноту.  
> Оптимизировать на **понятность системы самой себе**.

Система должна быть читаема машинами раньше, чем станет выразительной для человека.

---

## 14. Checkpoints

Последний checkpoint: `2026-01-28.md`

Ключевое: система вошла в фазу саморазворачивания, человек — корректор траектории.
