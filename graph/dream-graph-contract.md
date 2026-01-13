# Договор о связке extended-mind и dream-graph

Документ фиксирует разделение ответственности и формат обмена данными между двумя репозиториями.

## Разделение ответственности

### extended-mind отвечает за:

1. **Метамодель графа**
   - Схема типов узлов и связей (`graph/schema.graph.yml`)
   - Определение `node_kinds` и `edge_kinds`
   - Минимальный набор типов для представления экосистемы

2. **Идентификаторы узлов и связей**
   - Формат идентификаторов: `kind:id` (например, `project:extended-mind`)
   - Уникальность идентификаторов в рамках экосистемы
   - Семантическая структура идентификаторов

3. **Двуполярные описания**
   - `front_label` — метка "с начала" (для пользователя, понятная)
   - `back_label` — метка "с конца" (техническая, структурированная)
   - Поддержка двуполярности в фронтматтерах документов

4. **Генерация графа из документов**
   - Извлечение графовых метаданных из фронтматтеров
   - Формирование узлов и связей на основе структуры репозитория
   - Экспорт в формате Cosmos Map v0.1

### dream-graph отвечает за:

1. **Визуальные layout'ы и физику**
   - Реализация различных режимов визуализации (planetary, mlp, dna, metro, lattice)
   - Физическая симуляция графа (силы, анимации)
   - Интерактивность (вращение, зум, переходы)

2. **Интерпретация visual props**
   - `props.visual_hint` — подсказки для формы узлов (sphere, box, cylinder)
   - `props.size` — размер узлов
   - `props.color` — цвет узлов
   - `props.opacity` — прозрачность связей

3. **Режимы отображения**
   - Переключение между layout'ами
   - Анимации переходов
   - Адаптация к размеру графа

## Формат обмена данными

### Текущий формат (первый шаг)

Один JSON файл, содержащий:

```json
{
  "schema": "cosmos-map.v0.1",
  "meta": {
    "source": "extended-mind",
    "version": "0.1",
    "generated_at": "2026-01-12T12:00:00Z"
  },
  "nodes": [
    {
      "id": "project:extended-mind",
      "label": "Extended Mind",
      "type": "project",
      "status": "active",
      "props": {
        "visual_hint": "sphere",
        "size": 1.5,
        "color": "#667eea"
      },
      "graph": {
        "node_id": "project:extended-mind",
        "node_kind": "project",
        "tags": ["core", "metamodel"],
        "front_label": "Центральное смысловое ядро utemix-lab",
        "back_label": "project.extended-mind"
      }
    }
  ],
  "links": [
    {
      "id": "l1",
      "source": "project:extended-mind",
      "target": "document:definition-pack-v0.1",
      "type": "narrates",
      "status": "active",
      "weight": 0.9,
      "props": {
        "visual_hint": "curve",
        "opacity": 0.8
      }
    }
  ]
}
```

### Ключевые поля

**Узлы:**
- `id` — уникальный идентификатор (формат: `kind:id`)
- `label` — краткое название
- `type` — тип узла (из `schema.graph.yml`)
- `status` — статус (active, draft, stable, archived)
- `props.visual_*` — визуальные свойства для dream-graph
- `graph.node_id` — идентификатор в графе extended-mind
- `graph.node_kind` — тип узла согласно схеме
- `graph.tags` — теги для фильтрации
- `graph.front_label` — метка "с начала"
- `graph.back_label` — метка "с конца"

**Связи:**
- `id` — уникальный идентификатор связи
- `source` / `target` — ID узлов
- `type` — тип связи (из `schema.graph.yml`)
- `status` — статус связи
- `weight` — вес связи (0.0 - 1.0)
- `props.visual_*` — визуальные свойства

## Текущее состояние

### Реализовано

- ✅ Схема метамодели (`graph/schema.graph.yml`)
- ✅ Seed файл для начальной структуры (`graph/ecosystem.seed.yml`)
- ✅ Графовые блоки во фронтматтерах ключевых документов
- ✅ Спецификация входного формата (`dream-graph/docs/cosmos-input-format.md`)
- ✅ Абстракция загрузки графа (`dream-graph/src/graph/loadGraphConfig.js`)

### Не реализовано (пока)

- ❌ Генератор графа из фронтматтеров в extended-mind
- ❌ Экспорт графа в формате Cosmos Map
- ❌ Загрузка графа из extended-mind в dream-graph
- ❌ API или механизм передачи данных между репозиториями

## Ссылки

- **Схема метамодели:** `graph/schema.graph.yml`
- **Seed файл:** `graph/ecosystem.seed.yml`
- **Спецификация формата:** `dream-graph/docs/cosmos-input-format.md`
- **Абстракция загрузки:** `dream-graph/src/graph/loadGraphConfig.js`

## Примечания

- Формат обмена основан на Cosmos Map v0.1
- Расширяет его графовыми метаданными из extended-mind
- dream-graph интерпретирует `props.visual_*` для визуализации
- `graph.front_label` и `graph.back_label` поддерживают двуполярное описание
- Интеграция пока концептуальная, не реализована
