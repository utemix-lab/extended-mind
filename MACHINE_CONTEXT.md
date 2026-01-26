# MACHINE_CONTEXT.md

> Каноническая точка входа контекста для LLM / IDE-агентов

**version:** 1.2  
**last_updated:** 2026-01-26  
**canon_nodes:** 26  
**canon_edges:** 46

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
│   └── character-petrova
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

## 11. Главная директива

> Не оптимизировать на полноту.  
> Оптимизировать на **понятность системы самой себе**.

Система должна быть читаема машинами раньше, чем станет выразительной для человека.

---

## 12. Checkpoints

Последний checkpoint: `2026-01-26-machine-view-shift.md`

Ключевое: система вошла в фазу саморазворачивания, человек — корректор траектории.
