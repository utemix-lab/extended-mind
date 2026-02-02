# SYSTEM PRACTICES MATRIX (v0)

Статус: **расширяемая таблица**.  
Назначение: фиксировать, что в архитектуре самобытно, что заимствовано, что похоже на веб, а что нет.  
Это не закон, а рабочая карта для сверки и контроля дрейфа.

## Как пользоваться
Записывай решения/паттерны, отмечай:
- **Категорию** (original / adapted / borrowed)
- **Соответствие общепринятым практикам** (align / partial / diverge)
- **Похожесть на веб** (yes / partial / no)
- **Почему** (коротко)
- **Риски**
- **Ссылки**

## Таблица (расширяемая)

| Решение / паттерн | Категория | Соответствие практикам | Похоже на веб | Почему | Риски | Ссылки |
| --- | --- | --- | --- | --- | --- | --- |
| Минимальный Canon + большие Catalogs | original | diverge | no | Карта ≠ территория, масштаб по строкам | потеря полноты в каноне | `SYSTEM_LANGUAGE_LAYER.md` |
| Query Mode как реакция, не страница | adapted | partial | partial | “контекст → выдача” без узлов | непонятность без UI‑индикаторов | `visitor.js`, `CODEX_MEMO_CORE_ARCHITECTURE.md` |
| Actors / Instruments / Matter | original | diverge | no | Роли важнее сущностей | смешение статусов | `SYSTEM_LANGUAGE_ACTORS_INSTRUMENTS_MATTER.md` |
| Внешняя навигация (HF/LastFM) | borrowed | align | yes | не дублировать рынки | зависимость от внешних | `pointer_tags_registry.json` |
| Read‑only UI (рендеры не пишут в канон) | adapted | partial | no | защита канона | неудобство редактирования | `SYSTEM_GUARDRAILS.md` |
| Пресеты как входы в Query Mode | adapted | align | partial | быстрые сценарии | превращение в “фильтры сайта” | `visitor.js` |
| Три окна UI = Actors/ Instruments/ Matter | original | diverge | no | сцена = роли, не страницы | слишком театрально без индикаторов | `SYSTEM_LANGUAGE_ACTORS_INSTRUMENTS_MATTER.md` |
| Контекст‑зависимая выдача (owner:* фильтр) | adapted | partial | partial | одна кнопка → разные результаты | магия без объяснения | `visitor.js` |
| Хабы как единственные “списки” узлов | adapted | align | no | узлы не размножаются | хабы перегружаются | `universe.json` |
| Узлы‑воркбенчи вместо пресетов | adapted | partial | no | темы не смешиваются | рост канона | `coverage-map-full.md` |
| Виджеты как навигация (без текста) | original | diverge | partial | чтение через образ | непонятность без легенды | `visitor.css` |

## YAML‑вариант (для быстрых правок)

```yaml
matrix:
  - decision: "Minimal canon + large catalogs"
    category: original
    alignment: diverge
    web_like: no
    why: "Карта ≠ территория, масштаб по строкам."
    risks: "Потеря полноты в каноне."
    refs: ["SYSTEM_LANGUAGE_LAYER.md"]
  - decision: "Query Mode as reaction"
    category: adapted
    alignment: partial
    web_like: partial
    why: "Контекст → выдача без узлов."
    risks: "Невидимость механики без индикаторов."
    refs: ["visitor.js", "CODEX_MEMO_CORE_ARCHITECTURE.md"]
  - decision: "Actors / Instruments / Matter"
    category: original
    alignment: diverge
    web_like: no
    why: "Роли важнее сущностей."
    risks: "Смешение статусов."
    refs: ["SYSTEM_LANGUAGE_ACTORS_INSTRUMENTS_MATTER.md"]
  - decision: "External navigation (HF/LastFM)"
    category: borrowed
    alignment: align
    web_like: yes
    why: "Не дублировать рынки."
    risks: "Зависимость от внешних."
    refs: ["pointer_tags_registry.json"]
  - decision: "Read-only UI renders"
    category: adapted
    alignment: partial
    web_like: no
    why: "Защита канона."
    risks: "Неудобство редактирования."
    refs: ["SYSTEM_GUARDRAILS.md"]
  - decision: "Presets as Query entrances"
    category: adapted
    alignment: align
    web_like: partial
    why: "Быстрые сценарии."
    risks: "Скатывание к фильтрам сайта."
    refs: ["visitor.js"]
  - decision: "Three UI windows = Actors/Instruments/Matter"
    category: original
    alignment: diverge
    web_like: no
    why: "Сцена = роли, не страницы."
    risks: "Театральность без индикаторов."
    refs: ["SYSTEM_LANGUAGE_ACTORS_INSTRUMENTS_MATTER.md"]
  - decision: "Context-sensitive results (owner:* filter)"
    category: adapted
    alignment: partial
    web_like: partial
    why: "Один маркер → разные выдачи."
    risks: "Невидимая магия без объяснения."
    refs: ["visitor.js"]
  - decision: "Hubs as only node lists"
    category: adapted
    alignment: align
    web_like: no
    why: "Узлы не размножаются."
    risks: "Хабы перегружаются."
    refs: ["universe.json"]
  - decision: "Workbenches as nodes (vs presets)"
    category: adapted
    alignment: partial
    web_like: no
    why: "Темы не смешиваются."
    risks: "Рост канона."
    refs: ["coverage-map-full.md"]
  - decision: "Widget-only navigation"
    category: original
    alignment: diverge
    web_like: partial
    why: "Чтение через образ."
    risks: "Непонятность без легенды."
    refs: ["visitor.css"]
```
