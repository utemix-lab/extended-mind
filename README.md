# extended-mind

**Авторский конструктор маршрутов и карт экосистемы.**

---

## Что это

extended-mind — это внутренний инструмент для:
- **Понимания системы как графа** (Universe Graph)
- **Проектирования маршрутов** (Route Graph)
- **Экспорта для витрины** (vovaipetrova-core)

Это не пользовательский UI, а **author cockpit** — кабина пилота для сборки экосистемы.

---

## Ключевые принципы

> См. полный [MANIFEST.md](./docs/graph/MANIFEST.md)

1. **Канон мал** — Universe Graph содержит только Projects, Repos, Concepts, Principles, Decisions, Roles
2. **Маршрут ≠ канон** — Route Graph ссылается на канон через refs
3. **3S = линзы** — Story / System / Service — режимы просмотра, не сущности
4. **Конечность обязательна** — каждый маршрут имеет проверяемые лимиты
5. **Витрина не диктует канон** — vovaipetrova-core читает, не пишет

---

## Структура

```
docs/graph/
  MANIFEST.md           # Инварианты экосистемы
  ROUTE_GRAPH_SPEC.md   # Спецификация маршрутов
  ROUTE_GRAPH.schema.json

examples/
  route_graph.demo.json # Пример маршрута

spaces/extended-mind-console/
  app.py                # Gradio UI
  universe-graph/       # Редактор графа
```

---

## Глобальная цель

> **Архитектура = контент**

- **Universe Graph** — карта мира (канон)
- **Route Graph** — конечный маршрут прохождения
- **extended-mind** — инструмент сборки маршрутов
- **vovaipetrova-core** — витрина для внешнего мира

**Ключевая метрика:** мгновенное интуитивное понимание системы через маршрут.

---

## Возможные производные

See docs/architecture/OVERVIEW.md for system-level architecture and intentions.

---

## Быстрый старт

```bash
# Локальный запуск
cd spaces/extended-mind-console
pip install -r requirements.txt
python app.py
```

Или используйте HuggingFace Space:  
https://huggingface.co/spaces/utemix/extended-mind-console

---

## Спецификации

- [MANIFEST.md](./docs/graph/MANIFEST.md) — инварианты
- [ROUTE_GRAPH_SPEC.md](./docs/graph/ROUTE_GRAPH_SPEC.md) — спецификация маршрутов
- [ROUTE_GRAPH.schema.json](./docs/graph/ROUTE_GRAPH.schema.json) — JSON Schema

---

## Версия

`route-graph-editor-v0.1`

---

## Лицензия

Open Source (лицензия будет определена дополнительно).
