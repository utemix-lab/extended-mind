# story-node-021-domain-coverage-check

## Название
Проверка покрытия 8 доменов персонажами и workbench’ами

## Что произошло
Сделана ревизия покрытия доменов персонажами и их workbench’ами с оценкой плотности.

## Почему это было необходимо
Покрытие доменов показывает, не образовались ли “дыры” и не нарушена ли асимметрия системы.

## Принятое решение
Зафиксировать покрытие как живую карту: асимметричное, но полное.

## Что изменилось в системе
- Утверждён список доменов и их носителей.
- Зафиксирован принцип: персонажи и workbench’и — входы, а не разделы.

## Открытый вопрос
Нужны ли дополнительные точки входа в домен Interactive Systems без перегруза?

## Что это закладывает
Контроль плотности без симметрии: система остаётся живой экосистемой, а не каталогом.

---

## Narrative (опционально)

**evidence:**
- `docs/CHARACTERS.md`
- `docs/workbenches/WORKBENCH_INDEX.md`

**moment:**
Покрытие стало читабельной картой, а не списком.

**voice_hint:**
<!-- narrator: author | system | petrova | vova | neutral -->
<!-- tone: technical | essay | diary | cinematic -->
narrator: system
tone: technical

---

**Related Practices:**
- `practice-system-thinking`
- `practice-ecosystem-thinking`

**Refs:**
- checkpoint: `2026-01-28`

---

## Coverage (v1)

**1. Artificial Intelligence & Computational Models** — covered (strong)  
AI → Iron Fairy Tales  
Ney → Appearance Atelier  
Runa → Mojibake  
Hinto → Ji  
Vova → Zucken‑Drücken  
CADrik → Solidol

**2. Software & Digital Tools** — covered (strong)  
Vova → VSTablishment  
Vasya → Frame Grinder  
Runa → Mojibake  
CADrik → Solidol  
Hinto → Ji

**3. Visual & Media Arts** — covered (strong)  
Petrova → Анимация +  
Ney → Appearance Atelier  
Vasya → Frame Grinder  
Dizy → Homo Perceptivus  
As if → clips/visual

**4. Music & Sound Culture** — covered (deep)  
Vova → Музыка в целом / VSTablishment / Zucken‑Drücken  
Vasya ↔ Vova → As if

**5. Design & Aesthetic Systems** — covered (strong)  
Dizy → Homo Perceptivus / Киберантика  
Petrova → Brand Direction  
Ney → appearance as tech

**6. Knowledge Systems & Cognitive Architectures** — covered (strong)  
Ancy → Darwin’s Blind Spot / Evoquant / Mind's Lorgnette  
Runa → Mojibake / Mind's Lorgnette  
Gamych → Word-machine

**7. Interactive Systems & Game Culture** — covered (soft)  
Gamych → Playfield  
Vasya → interactive storytelling (production optics)  
Petrova → interactive narratives in animation

**8. Architecture & Physical Realization** — covered (pointed)  
CADrik → Solidol

**Key note:** domains are not sections; characters are not avatars; workbench’и are not features.  
They are different entry points into one world.
