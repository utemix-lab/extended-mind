# Universe Graph Specification

> Формат данных и правила построения канонического графа

---

## Обзор

Universe Graph — это JSON-файл, содержащий полное описание системы знаний:
- **Узлы** — понятия, объекты, сущности
- **Рёбра** — связи между узлами
- **3S контент** — Story/System/Service для каждого узла

---

## Формат файла

### Корневая структура

```json
{
  "meta": {
    "version": "1.0",
    "description": "Описание графа"
  },
  "nodes": [ ... ],
  "edges": [ ... ]
}
```

### Узел (Node)

```json
{
  "id": "unique-id",
  "label": "Отображаемое имя",
  "position": { "x": 400, "y": 300 },
  "story": "Нарративный контент для панели Story",
  "system": "Техническое описание для панели System",
  "service": "Действия и возможности для панели Service",
  "type": "concept",
  "visibility": "public",
  "status": "expandable",
  "semantics": { "role": "content", "abstraction": "medium" },
  "rag": { "index": true, "priority": 0.5 }
}
```

| Поле | Тип | Обязательное | Описание |
|------|-----|--------------|----------|
| `id` | string | ✅ | Уникальный идентификатор (kebab-case) |
| `label` | string | ✅ | Человекочитаемое имя |
| `position` | {x, y} | ❌ | Позиция в редакторе |
| `story` | string | ❌ | Контент для Story панели |
| `system` | string | ❌ | Контент для System панели |
| `service` | string | ❌ | Контент для Service панели |
| `type` | string | ❌ | Тип узла (см. enum ниже) |
| `visibility` | string | ❌ | Видимость узла |
| `status` | string | ❌ | Статус зрелости |
| `semantics` | object | ❌ | Семантическая роль и уровень абстракции |
| `rag` | object | ❌ | RAG настройки |

### Ребро (Edge)

```json
{
  "id": "edge-1",
  "source": "node-a",
  "target": "node-b"
}
```

| Поле | Тип | Обязательное | Описание |
|------|-----|--------------|----------|
| `id` | string | ✅ | Уникальный идентификатор |
| `source` | string | ✅ | ID исходного узла |
| `target` | string | ✅ | ID целевого узла |

### Node Contract v1 (enum + дефолты)

**type**:
`root | hub | domain | concept | character | module | spec | process | policy | artifact`  
**default:** `concept`

**visibility**:
`public | internal | hidden`  
**default:** `public`

**status**:
`core | expandable | frozen | deprecated`  
**default:** `expandable`

**semantics.role**:
`description | container | mediator | content`  
**default:** `content`

**semantics.abstraction**:
`high | medium | low`  
**default:** `medium`

**rag.index**:
`boolean`  
**default:** `true`

**rag.priority**:
`number (0.0–1.0)`  
**default:** `0.5`

### Edge types (рекомендация)

`structural | contains | relates | describes | implements | renders`  
**default:** `relates`

---

## 3S Framework

Каждый узел содержит три проекции контента:

### Story (Нарратив)

**Вопрос:** "Что это значит для меня?"

- Эмоциональный, вовлекающий текст
- История, контекст, мотивация
- Написан для человека, не для машины

**Пример:**
```
"Добро пожаловать в Universe — пространство, где все идеи связаны. 
Каждый узел — это дверь в новое понимание."
```

### System (Структура)

**Вопрос:** "Как это устроено?"

- Техническое описание
- Связи с другими элементами
- Формальные определения

**Пример:**
```
"Universe — корневой узел графа. От него исходят все остальные 
понятия через рёбра типа RELATED и CONTAINS."
```

### Service (Действия)

**Вопрос:** "Что я могу с этим сделать?"

- Доступные действия
- Навигационные подсказки
- Call-to-action

**Пример:**
```
"Выберите направление для исследования. 
Каждый путь ведёт к новым открытиям."
```

---

## Правила построения

### Идентификаторы

- Формат: `kebab-case` (слова через дефис)
- Только латиница, цифры, дефис
- Уникальность в пределах графа

**Хорошо:** `concept-mind-map`, `project-dream-graph`, `principle-modularity`

**Плохо:** `Concept Mind Map`, `проект-1`, `node_123`

### Связи

- Рёбра ненаправленные (для навигации)
- Один узел может иметь много связей
- Избегать изолированных узлов

### Контент

- 3S поля опциональны, но желательны
- Писать для человека, не для машины
- Краткость: 1-3 предложения на поле

---

## Типы узлов (рекомендация)

Хотя формально тип не указывается, рекомендуется следовать соглашениям:

| Тип | Префикс ID | Пример |
|-----|------------|--------|
| Понятие | `concept-` | `concept-ontology` |
| Проект | `project-` | `project-dream-graph` |
| Принцип | `principle-` | `principle-single-source` |
| Документ | `doc-` | `doc-architecture` |
| Персона | `persona-` | `persona-developer` |

---

## Пример минимального графа

```json
{
  "meta": {
    "version": "1.0",
    "description": "Минимальный пример"
  },
  "nodes": [
    {
      "id": "universe",
      "label": "Universe",
      "position": { "x": 400, "y": 300 },
      "story": "Начало всего.",
      "system": "Корневой узел.",
      "service": "Выбери направление.",
      "type": "root",
      "visibility": "public",
      "status": "core",
      "semantics": { "role": "container", "abstraction": "high" },
      "rag": { "index": true, "priority": 0.8 }
    },
    {
      "id": "concept-a",
      "label": "Concept A",
      "position": { "x": 550, "y": 250 },
      "story": "Первое понятие.",
      "system": "Связано с Universe.",
      "service": "Изучить подробнее.",
      "type": "concept",
      "visibility": "public",
      "status": "expandable",
      "semantics": { "role": "content", "abstraction": "medium" },
      "rag": { "index": true, "priority": 0.5 }
    }
  ],
  "edges": [
    {
      "id": "edge-1",
      "source": "universe",
      "target": "concept-a"
    }
  ]
}
```

---

## Валидация

### Обязательные проверки

1. Все `id` уникальны
2. Все `source` и `target` в рёбрах существуют как узлы
3. JSON синтаксически корректен

### Рекомендуемые проверки

1. Нет изолированных узлов (без рёбер)
2. Граф связный (можно добраться от любого узла к любому)
3. Все узлы имеют хотя бы `story` или `system`

---

## Версионирование

Файл хранится в Git. Каждое сохранение — потенциальный коммит.

**Рекомендация:** Периодически создавать именованные версии:
```
universe.json           # Текущая
universe.2026-01-21.json # Snapshot
```
