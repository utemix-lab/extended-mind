# Practices Specification

## Определение

> **Practice** — устойчивый способ действия/мышления, который повторяем,  
> оставляет следы в системе и может быть "пройден" другим.

**Формула:**
> Practice = устойчивый путь через систему, а не раздел системы.

---

## Два режима (независимые)

### Структурный режим (для пользователя)

Practice как **способ действия**, привязанный к доменам и персонажам.

**Что видит пользователь:**
- Описание (story/system/service)
- Связанные домены
- Связанные персонажи
- Связанные конструкции (в будущем)

**Источник:** universe.json + edges

**❗ Никаких story-nodes в этом режиме.**

### Нарративный режим (для системы/автора)

Practice как **траектория**, проявляющаяся через story-nodes.

**Что делает система:**
- Собирает story-nodes по `related_practices`
- Строит временную линию
- Генерирует контент (посты, портфолио, презентации)

**Источник:** story-nodes

**❗ Practice не "знает" своих story-nodes.**

---

## Правила

### 1. Плоский уровень (строго)

Practices **не имеют подуровней**.

Если Practice кажется "слишком большой" — это семейство практик, и его не нужно оформлять узлом.

### 2. Критерии ввода Practice как узла

Practice становится узлом, если:

1. ✅ Есть минимум 1 story-node, который можно к ней отнести
2. ✅ Можно сформулировать в одном предложении как "способ делать"

Если практика существует только "в голове" — она остаётся латентной.

### 3. Структурные связи (обязательные)

```
practice ↔ domain    (relates)
practice ↔ character (relates)
practice ↔ practice  (редко, relates)
```

Эти связи:
- Не зависят от story-nodes
- Существуют даже если story-nodes отсутствуют

### 4. Нарративные связи (опциональные)

```markdown
# В story-node.md:
**Related Practices:**
- `practice-xxx`
```

Practice **не содержит** обратных ссылок.

### 5. Защитное правило

> ❗ Никогда не использовать story-nodes для определения структуры Practices.  
> ❗ Никогда не выводить story-nodes в пользовательском чтении Practices.

---

## Способы "дробления" (без подуровней)

| Способ | Описание |
|--------|----------|
| **Через story-nodes** | Одна practice → несколько story-nodes (этапы, применения) |
| **Через связи** | practice A ↔ practice B (перекрытие, соседство) |
| **Через персонажей** | Одна practice проявляется по-разному у разных проводников |

---

## Типы Practices

Practices могут относиться к разным слоям системы:

| Слой | Примеры | Владелец |
|------|---------|----------|
| **Архитектурный** | system-thinking, anti-taxonomy, direction, branding | Система |
| **Художественный** | Киберантика (будущее) | Персонаж (Дизи) |
| **Инструментальный** | ComfyUI workflow (будущее) | Персонаж |

---

## Текущие Practices

| ID | Название | Связанные домены |
|----|----------|------------------|
| `practice-system-thinking` | Системное мышление | knowledge-systems, ai, architecture |
| `practice-anti-taxonomy` | Антитаксономическая навигация | knowledge-systems, software, ai |
| `practice-research-thinking` | Исследовательское мышление | ai, interactive-systems, knowledge |
| `practice-direction` | Режиссура | visual, design, interactive |
| `practice-systems-design` | Дизайн систем | design, software, architecture |
| `practice-architectural-design` | Архитектурное проектирование | architecture, software, ai |
| `practice-visual-thinking` | Визуальное мышление | visual, design, interactive |
| `practice-sound-thinking` | Звуковое мышление | music-sound, interactive |
| `practice-interactive-thinking` | Интерактивное мышление | interactive-systems, games, ui |
| `practice-branding` | Брендинг | design, visual, software |
| `practice-ecosystem-thinking` | Экосистемное мышление | ai, software, knowledge |
| `practice-curation` | Кураторство и отбор | all |
| `practice-reflection-fixation` | Рефлексия и фиксация | knowledge-systems |
| `practice-possibility-navigation` | Навигация по возможностям | all |

---

## Модель

```
      Domains ───────┐
                     │
      Characters ──── Practice ──── (future constructs)
                     │
      (independent)  │
                     │
               Story-nodes
             (narrative only)
```

---

## Ключевая формула

> Один и тот же Practice:  
> для Автора — путь во времени,  
> для пользователя — карта возможностей.
