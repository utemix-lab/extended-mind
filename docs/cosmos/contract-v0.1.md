# Cosmos Map — Data Contract v0.1

**Статус:** active  
**Версия схемы:** `cosmos-map.v0.1`  
**Source of Truth:** Cosmos Map (extended-mind)  
**Consumers:** dream-graph, future visualizers, RAG / Graph-RAG layers

---

## Назначение

Этот документ фиксирует **контракт данных** между:

- **Cosmos Map** — инструментом авторинга и смысловой сборки графа
- **Graph Renderers** (например, dream-graph) — визуальными и интерактивными представлениями

Контракт гарантирует, что:
- визуализация может свободно развиваться,
- смысловая структура не разрушается,
- новые поля добавляются без поломки существующих инструментов.

---

## Общая структура JSON

```json
{
  "schema": "cosmos-map.v0.1",
  "meta": { ... },
  "nodes": [ ... ],
  "links": [ ... ]
}

Meta (необязательное, но рекомендовано)

```json
"meta": {
  "title": "Extended-Mind Cosmos",
  "description": "Conceptual map of the ecosystem",
  "updated_at": "2024-XX-XX",
  "author": "utemix-lab"
}

meta не участвует в визуальной логике напрямую, но может использоваться для:

заголовков сцен,

экспорта,

версионирования.

Nodes
Обязательные поля

```json
{
  "id": "layer:story-layer",
  "label": "story-layer",
  "type": "layer",
  "status": "active"
}

Поле	Тип	Описание
id	string	Уникальный идентификатор (никогда не меняется)
label	string	Человеко-читаемое имя
type	string	Тип сущности (см. ниже)
status	string	Жизненный статус узла

Рекомендуемые поля

```json
{
  "notes": "",
  "importance": 0.6,
  "tags": ["core", "architecture"]
}

Поле	Тип	Назначение
notes	string	Свободное описание / комментарий
importance	number (0..1)	Вес узла для визуализации
tags	array<string>	Доп. классификация

Типы узлов (open set)
Контракт не ограничивает список типов.

Примеры:

layer

project

character

concept

tool

experiment

unknown

Новые типы можно добавлять без изменения схемы.

Status (recommended enum)
active

draft

archived

hypothesis

Links
Обязательные поля

```json
{
  "source": "layer:story-layer",
  "target": "layer:core",
  "type": "connects"
}

Поле	Тип	Описание
source	string	id узла-источника
target	string	id узла-приемника
type	string	Тип связи

Рекомендуемые поля

```json
{
  "weight": 0.8,
  "direction": "forward",
  "notes": ""
}

Поле	Тип	Назначение
weight	number (0..1)	Сила/важность связи
direction	string	forward, backward, bidirectional
notes	string	Комментарий

Типы связей (open set)
Примеры:

connects

depends-on

influences

implements

references

Расширяемость
Принцип
Добавлять поля можно

Удалять или менять смысл существующих — нельзя

Визуализаторы должны игнорировать неизвестные поля

Это позволяет:

вводить экспериментальные параметры,

откладывать формализацию,

возвращаться к ним позже без потери данных.

Совместимость
Любой JSON с schema: cosmos-map.v0.1 обязан:

содержать nodes[].id

содержать links[].source / target, указывающие на существующие id

Если условия выполнены — визуализация обязана работать, даже если часть данных игнорируется.

Роли компонентов
Cosmos Map

редактирование

смысловая структура

версии и PR

Graph Renderer (dream-graph)

визуал

физика

звук

интеракция

не меняет источник данных напрямую

Примечание
Этот контракт умышленно минимален.
Он фиксирует форму, но не навязывает смысл.

Смысл рождается в работе с графом,
а не в попытке описать его заранее.
