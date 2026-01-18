# ROUTE_GRAPH_SPEC.md — Спецификация Route Graph

> Route Graph = конечный маршрут прохождения Universe Graph

---

## Обзор

**Route Graph** — это отдельный объект, описывающий конечный путь через экосистему. Он не является частью канона (Universe Graph), а лишь ссылается на него через `refs`.

### Ключевые принципы

1. **Конечность** — каждый маршрут имеет лимиты (nodes, edges, depth)
2. **Ссылки, не копии** — узлы содержат `refs` на канон, не дублируют его
3. **Три проекции** — каждый шаг раскрывается через Story/System/Service
4. **Проходимость** — NEXT-рёбра образуют путь от start до конца

---

## Структура RouteGraph

```typescript
interface RouteGraph {
  id: string;                    // Уникальный ID маршрута
  title: string;                 // Название маршрута
  created_at: string;            // ISO timestamp
  updated_at: string;            // ISO timestamp
  
  start_node_id: string;         // ID начального узла
  
  nodes: RouteNode[];            // Узлы маршрута
  edges: RouteEdge[];            // Связи между узлами
  
  limits: {
    max_nodes: number;           // Лимит узлов (default: 50)
    max_edges: number;           // Лимит рёбер (default: 100)
    max_depth: number;           // Максимальная глубина от start (default: 10)
  };
  
  meta?: {
    project_id?: string;         // Связанный проект
    notes?: string;              // Заметки автора
    version?: string;            // Версия маршрута
  };
}
```

---

## RouteNode (Step)

**RouteNode** — это шаг пути, а не сущность мира. Каждый шаг раскрывается в трёх проекциях.

```typescript
interface RouteNode {
  id: string;                    // Уникальный ID узла
  label: string;                 // Краткое название (1-5 слов)
  
  // Три проекции (линзы)
  story: StoryView;              // Что происходит
  system: SystemView;            // Как устроено
  service: ServiceView;          // Что можно сделать
  
  refs: Reference[];             // Ссылки на канон
  
  position?: { x: number; y: number };  // Позиция на canvas
}
```

### StoryView — нарратив

```typescript
interface StoryView {
  text: string;                  // Короткий текст (1-3 строки)
  refs?: Reference[];            // Персонажи, проекты, контент, каналы
}
```

### SystemView — архитектура

```typescript
interface SystemView {
  text: string;                  // Объяснение "как это устроено"
  refs?: Reference[];            // Repos, ADR, specs, архитектурные решения
}
```

### ServiceView — действия

```typescript
interface ServiceView {
  text: string;                  // Описание возможных действий
  actions?: DemoAction[];        // Демо-действия
  refs?: Reference[];            // Связанные инструменты
}

interface DemoAction {
  id: string;
  label: string;
  type: 'generate' | 'export' | 'compare' | 'navigate' | 'custom';
  target?: string;               // URL или ID
}
```

---

## Reference — ссылка на канон

```typescript
interface Reference {
  type: 'internal' | 'external';
  
  // Для internal
  entity_type?: 'project' | 'repo' | 'doc' | 'term' | 'decision' | 'principle';
  entity_id?: string;
  
  // Для external
  url?: string;
  pointer_tag?: string;
  
  label?: string;                // Отображаемый текст
}
```

---

## RouteEdge — связь между узлами

```typescript
interface RouteEdge {
  id: string;
  source: string;                // ID исходного узла
  target: string;                // ID целевого узла
  type: 'NEXT' | 'BRANCH' | 'RELATED';
  label?: string;
}
```

### Типы рёбер

| Тип | Назначение | Визуализация |
|-----|------------|--------------|
| `NEXT` | Основной путь | Сплошная линия, стрелка |
| `BRANCH` | Альтернативный путь | Пунктирная линия |
| `RELATED` | Мягкая связь | Тонкая линия, без стрелки |

### Инварианты

1. `NEXT` образует проходимый путь от `start_node_id`
2. Все `source` и `target` должны существовать в `nodes`
3. Не допускаются циклы в `NEXT` (DAG)

---

## Валидация

### Обязательные проверки (errors)

- [ ] `start_node_id` существует в nodes
- [ ] Все edges ссылаются на существующие nodes
- [ ] `nodes.length <= limits.max_nodes`
- [ ] `edges.length <= limits.max_edges`
- [ ] Depth от start <= `limits.max_depth`
- [ ] NEXT-путь проходим (нет изолированных узлов на пути)

### Рекомендации (warnings)

- [ ] Каждый узел имеет непустой `story.text`
- [ ] Каждый узел имеет непустой `system.text`
- [ ] Каждый узел имеет хотя бы один `ref`

---

## Экспорт

### Файловая структура

```
public/routes/
  <route_id>.json           # Экспортированный маршрут
  
sessions/
  <session_id>.json         # Сессия (derived, read-only)
```

### Статусы

| Статус | Описание |
|--------|----------|
| `draft` | Редактируется, не экспортирован |
| `exported` | Экспортирован в файл |
| `published` | Опубликован как часть витрины |

---

## Пример

См. `examples/route_graph.demo.json`
