# Coverage Map v1 — Full Narrative

Единый нарративный документ: персонажи → workbench’и → домены → карта перекрытий → правила языка.  
Это не энциклопедия и не “всё обо всём”. Это книга‑карта: кто здесь живёт, чем дышит и какими тропами ведёт.

________________________________________

## Персонажи → Workbench’и → Домены

Секрет системы: домены — это материки, workbench’и — мастерские, персонажи — проводники.  
А всё остальное — следы, сигналы и ритуалы навигации.

________________________________________

### Вова
Роль и энергия  
Вова — полевой агент культуры.  
Он не “собирает систему” — он в ней живёт.

Легенда:
Крылатое выражение:
Визуализация: image\video-генерация, ComfyUI

Workbench’и

Name: **Музыка в целом**  
Type: domain / cultural radar  
Slogan:  
Focus: музыка как культурный феномен: сцены, эпохи, стили, сдвиги.  
Inputs: релизы, критика, плейлисты, интервью.  
Outputs: signals / curated_sets / pointer_tags  
Practices: curation, sound-thinking, research-thinking  
Preset Context: domain:music  
Boundaries: без энциклопедии и “полного списка мира”.  
UI: “золотые плейлисты”  
Risks: незаметно превратиться в справочник.

Name: **VSTablishment**  
Type: domain / tool radar  
Slogan:  
Focus: навигация по миру VST: капабилити, производители, связки.  
Inputs: релизы, обзоры, тесты, практики использования.  
Outputs: signals / curated_sets  
Practices: curation, research-thinking, possibility-navigation  
Preset Context: domain:music + domain:tools  
Boundaries: не “магазин VST”, не “всё подряд”.  
UI: Query Mode по cap: и provider: + сохранённые пресеты запросов.  
Risks: разрастание до витрины продуктов.

Name: **Zucken‑Drücken**  
Type: cross-domain / experimental  
Slogan:  
Focus: AI-музыка, модели, техники, необычные инструменты и новые способы звукоизвлечения.  
Inputs: статьи, демо, сервисы, эксперименты.  
Outputs: signals + pointer_tags  
Practices: research-thinking, system-thinking, sound-thinking  
Preset Context: domain:ai + domain:music  
Boundaries: не реализация моделей, не “инженерный репозиторий”.  
UI: Query Mode + “stub actions” (на будущее: tutorial/overview/preset).  
Risks: устаревание + маркетинговый шум.

Name: **As if** (shared)  
Type: collaborative / in-world production  
Slogan:  
Shared with: Вова ↔ Вася  
Focus: музыка и саунд для системы: треки, атмосферы, идентичность.  
Inputs: темы, сцены, эксперименты, внутренняя драматургия мира.  
Outputs: signals / curated_sets / audio assets  
Practices: direction, sound-thinking, visual-thinking  
Preset Context: domain:music + domain:visual + practice:direction  
Boundaries: не “лейбл” и не “карьера”, это внутрисистемный продакшн-орган.  
UI: “сцена группы” + закадровые пайплайны (как портфолио).  
Risks: размывание фокуса.

Домены: Primary — Music & Sound Culture; Partial — Software & Digital Tools, Artificial Intelligence; Cross — Visual Media (через As if).

________________________________________

### Петрова
Роль и энергия  
Петрова — куратор смысла и формы.  
Она смотрит на систему, как строгий режиссёр:  
знает, что сцена живая, и любое движение меняет восприятие целого.  
А внутри — фанат анимации:  
авторской, странной, экспериментальной.

Легенда:
Крылатое выражение:
Визуализация: image\video-генерация, ComfyUI

Workbench’и (полное описание)

Name: **Анимация +**  
Type: domain / art radar  
Slogan:  
Focus: анимация как форма мышления: авторская/AI, режиссура, фестивали, награды, технологии как часть искусства.  
Inputs: премьеры, интервью, эксперименты, фестивальные подборки.  
Outputs: signals / curated_sets / pointer_tags  
Practices: direction, visual-thinking, curation  
Preset Context: domain:visual + genre:animation  
Boundaries: не кино-база.  
UI: визуальная сцена + “кнопка смысла”: зачем это смотреть.  
Risks: энциклопедичность.

Name: **Brand Direction**  
Type: system / brand spine  
Slogan:  
Focus: целостность системы: айдентика, тональность, нейминг, внутренние правила “как говорить”.  
Inputs: контент, референсы, решения, “ошибки и исправления”.  
Outputs: гайды / curated_sets / signature-маркировки  
Practices: branding, direction, systems-design  
Preset Context: domain:design + practice:branding  
Boundaries: не маркетинг и не продажи.  
UI: принцип → пример → след (артефакт).  
Risks: перегруз правилами.

Name: **Circus Technologies**  
Type: system / coordination  
Slogan:  
Focus: сборка ценности из сигналов: фокус недели, координация ролей, narrative-режим.  
Inputs: signals, story-nodes, Meta Goals.  
Outputs: системные сигналы, story-nodes, editorial-фокусы.  
Practices: system-thinking, ecosystem-thinking, reflection-fixation  
Preset Context: system:overview  
Boundaries: не управляет контентом персонажей, а обозначает фокус сцены.  
UI: “что сейчас главное” + почему это главное.  
Risks: субъективность.

Домены: Primary — Visual & Media Arts; Partial — Design & Aesthetic Systems; Cross — System-level.

________________________________________

### Вася
Роль и энергия  
Вася — неформал-технарь.  
Он не любит теории и красивые слова — ему важно, чтобы работало.  
Вася живёт в таймлайне.  
Слои, эффекты, костыли, “рендер в последний момент” —  
это его воздух.

Легенда:
Крылатое выражение:
Визуализация: image\video-генерация, ComfyUI

Workbench’и (полное описание)

Name: **Frame Grinder**  
Type: domain / production craft  
Slogan:  
Focus: монтаж/моушн как ремесло: пайплайны, эффекты, практики.  
Inputs: релизы, кейсы, разборы, плагины.  
Outputs: signals / curated_sets / pointer_tags  
Practices: interactive-thinking, visual-thinking, possibility-navigation  
Preset Context: domain:visual + domain:interactive + cap:video-editing  
Boundaries: не учебный курс и не “список софта”.  
UI: грубая сцена + “рабочие рецепты”.  
Risks: хаос, устаревание.

Name: **As if** (shared) — см. у Вовы.

Домены: Primary — Visual & Media Arts; Partial — Interactive Systems; Cross — Music & Sound.

________________________________________

### Нэй
Нэй — аккуратный гений проявления:  
его интересует не “красиво”, а “как устроено”.  
Он делает технологию видимой.

Легенда:
Крылатое выражение: “Рецепт важнее вдохновения.”
Визуализация: image\video-генерация, ComfyUI

Workbench: Appearance Atelier

Name: **Appearance Atelier**  
Type: domain-spanning / infrastructural  
Slogan: “Красота — побочный эффект воспроизводимости.”  
Focus: генеративный визуал как технология. ComfyUI, модели, пайплайны.  
Inputs: релизы, рецепты.  
Outputs: signals / curated_sets / tags.  
Practices: research-thinking, system-thinking, visual-thinking.  
Preset Context: domain:visual + domain:ai + cap:gen.  
Boundaries: не про “искусство”.  
UI: “как выглядит и почему так”.  
Risks: каталог моделей.

Домены: Primary — AI; Partial — Visual.

________________________________________

### CADрик
CADрик — робот, который верит в материал.  
Он строит мост “цифра → физика” и смазывает реальность солидолом.

Легенда:
Крылатое выражение:
Визуализация: Adobe Character Animator

Workbench: Solidol

Name: **Solidol**  
Type: domain / applied-technical  
Slogan: “Солидно. Solid.”  
Focus: мост цифра → физика. CAD, 3D, рендер, материалы.  
Inputs: софт, пайплайны.  
Outputs: signals / curated_sets / tags.  
Practices: architectural-design, systems-design, visual-thinking.  
Preset Context: domain:physical + domain:design + cap:cad.  
Boundaries: не “всё про 3D”.  
UI: механика и сборка.  
Risks: каталог софта.

________________________________________

### Руна
Руна — код и исследование.  
Её мир — retrieval, RAG, ресерч.

Легенда:
Крылатое выражение:
Визуализация: image\video-генерация, ComfyUI

Workbench: — (твои поля)

Name: **Mojibake**  
Type: infrastructure / research  
Slogan:  
Focus: RAG и ресерч‑инфраструктура. Retrieval‑цепочки, протоколы.  
Inputs: статьи, эксперименты.  
Outputs: signals / curated_sets / tags.  
Practices: research-thinking, system-thinking, ecosystem-thinking.  
Preset Context: domain:ai + domain:software + cap:rag.  
Boundaries: не продукт.  
UI: “как устроено внутри”.  
Risks: абстракция.

Name: **Mind's Lorgnette**  
Type: collaborative / applied  
Slogan:  
Shared with: Ancy  
Focus: производный продакшн‑инструмент для самоуправляемых систем.  
Inputs: карты знаний, протоколы.  
Outputs: signals / curated_sets / tags.  
Practices: system-thinking, ecosystem-thinking, research-thinking.  
Preset Context: domain:knowledge + domain:software + cap:systems.  
Boundaries: не копия extended‑mind.  
UI: мастерская самоуправляемых систем.  
Risks: размывание границы с extended‑mind.

Name: **Dream Graph**  
Type: system / infrastructure  
Slogan:  
Focus: рендер системы как книги‑карты.  
Inputs: exports/manifest, сцены, Query Mode.  
Outputs: read‑only интерфейс.  
Practices: system-thinking, ecosystem-thinking, research-thinking.  
Preset Context: domain:software + domain:interactive.  
Boundaries: не пишет в канон.  
UI: книга‑карта.  
Risks: UI начнёт диктовать онтологию.

Name: **Contracts**  
Type: system / infrastructure  
Slogan:  
Focus: контуры данных и экспортов системы.  
Inputs: signals/curated_sets, registries, manifests.  
Outputs: exports layer.  
Practices: system-thinking, ecosystem-thinking, research-thinking.  
Preset Context: domain:software + domain:knowledge.  
Boundaries: не UI‑слой, не канон.  
UI: экспортируемая карта.  
Risks: превращение в склад данных.

________________________________________

### Hinto
Hinto — робот-наблюдатель: ヒント на корпусе, ジ в сердце.  
Он ловит культурные сдвиги не по заголовкам, а по изменению привычек dev-мира.

Легенда:
Крылатое выражение:
Визуализация: Blender

Workbench: Ji (ジ) — (твои поля)

Name: **Ji (ジ)**  
Type: meta-domain / observational  
Slogan:  
Focus: наблюдение dev‑культуры как процесс. Традиции, паттерны, сдвиги.  
Inputs: GitHub, HF, RFC.  
Outputs: signals / curated_sets / tags.  
Practices: research-thinking, ecosystem-thinking, reflection-fixation.  
Preset Context: domain:software + domain:ai + cap:dev-culture.  
Boundaries: не пишет код.  
UI: икона наблюдения.  
Risks: новостной поток.

________________________________________

### Ancy
Он медленный наблюдатель и тихий архитектор смысла.  
Его пространство — книги, заметки, школы мышления,  
где важно не количество прочитанного, а точность связей.

Obsidian, Notion, структуры и траектории —  
это его инструменты и среда.

Легенда:
Крылатое выражение:
Визуализация: Toon Boom Harmony, Moho Pro

Workbench: Darwin’s Blind Spot + Evoquant + Mind’s Lorgnette — (твои поля)

Name: **Darwin’s Blind Spot**  
Type: domain / reflective  
Slogan:  
Focus: навигация по структурам мышления. Obsidian/Notion, школы.  
Inputs: книги, заметки.  
Outputs: signals / curated_sets / tags.  
Practices: reflection-fixation, research-thinking, possibility-navigation.  
Preset Context: domain:knowledge + cap:reflection.  
Boundaries: не энциклопедия.  
UI: медленная сцена.  
Risks: абстрактность.

Name: **Evoquant**  
Type: meta-research / formal  
Slogan:  
Cross with: Word Machine (Геймыч). Режим: конкурирующе‑дополняющие.  
Focus: внутренняя формализация. Модели, эволюция понятий.  
Inputs: карты знаний.  
Outputs: signals / curated_sets / tags.  
Practices: research-thinking, system-thinking, reflection-fixation.  
Preset Context: domain:knowledge + cap:formal.  
Boundaries: не продукт.  
UI: внутренний контур.  
Risks: слишком внутренне.

Name: **Mind's Lorgnette**  
Type: collaborative / applied  
Slogan:  
Shared with: Руна  
Focus: производный продакшн‑инструмент для самоуправляемых систем.  
Inputs: карты знаний, протоколы.  
Outputs: signals / curated_sets / tags.  
Practices: system-thinking, ecosystem-thinking, research-thinking.  
Preset Context: domain:knowledge + domain:software + cap:systems.  
Boundaries: не копия extended‑mind.  
UI: мастерская самоуправляемых систем.  
Risks: размывание границы с extended‑mind.

________________________________________

### Геймыч
Геймыч — математик, который отдыхает играя,  
и играет так, как другие доказывают теоремы.

Легенда: “Баланс — это мораль в цифрах.”
Крылатое выражение:
Визуализация: image\video-генерация, ComfyUI

Workbench: Playfield + Word Machine — (твои поля)

Name: **Playfield**  
Type: domain  
Slogan:  
Focus: игры как формальные поля. Механики, баланс.  
Inputs: кейсы, модели.  
Outputs: signals / curated_sets / tags.  
Practices: interactive-thinking, system-thinking, possibility-navigation.  
Preset Context: domain:games + cap:mechanics.  
Boundaries: не обзор индустрии.  
UI: поле правил.  
Risks: абстракция.

Name: **Word Machine**  
Type: meta-research / formal  
Slogan:  
Cross with: Evoquant (Ancy). Режим: конкурирующе‑дополняющие.  
Focus: формальные машины языка. Символические протоколы.  
Inputs: модели, схемы.  
Outputs: signals / curated_sets / tags.  
Practices: research-thinking, system-thinking, reflection-fixation.  
Preset Context: domain:knowledge + cap:formal.  
Boundaries: не продукт.  
UI: машина языка.  
Risks: узость.

________________________________________

### Дизи
Дизи — голос восприятия.  
Её узнают не по лицу, а по тому, как стало ощущаться пространство.

Легенда:
Крылатое выражение: «Восприятие — самый недооценённый интерфейс.»
Визуализация: Touch-design

Workbench: Homo Perceptivus + Киберантика — (твои поля)

Name: **Homo Perceptivus**  
Type: meta-aesthetic  
Slogan:  
Focus: восприятие как главный орган. Чувствительность, сцены.  
Inputs: образы, паттерны.  
Outputs: signals / curated_sets / tags.  
Practices: visual-thinking, direction, system-thinking.  
Preset Context: domain:design + cap:perception.  
Boundaries: не каталог визуала.  
UI: голос + смена образов.  
Risks: абстракция.

Name: **Киберантика**  
Type: meta-aesthetic / system-style  
Slogan:  
Focus: язык визуального мира системы. Стиль, лаборатория.  
Inputs: сцены, работы.  
Outputs: signals / curated_sets / tags.  
Practices: visual-thinking, branding, systems-design.  
Preset Context: domain:design + cap:style.  
Boundaries: не витрина.  
UI: портфолио‑сцена.  
Risks: эстетика без содержания.

________________________________________

### ИИ
ИИ — присутствие, зеркало индустрии.

Легенда:
Крылатое выражение: «Пока вы фантазируете о восстании машин, я уже договорился с вашим холодильником».
Визуализация: лого

Workbench: Iron Fairy Tales — (твои поля)

Name: **Iron Fairy Tales**  
Type: meta-domain / observational  
Slogan:  
Focus: зеркало индустрии ИИ. Сдвиги, режимы, риски.  
Inputs: релизы, заявления.  
Outputs: signals / curated_sets / tags.  
Practices: system-thinking, ecosystem-thinking, research-thinking.  
Preset Context: domain:ai + practice:system-thinking.  
Boundaries: не персональный голос.  
UI: логотип + нейтральный голос.  
Risks: поглотить голоса персонажей.

________________________________________

### Автор
Автор — “нажиматель кнопки”, мифологический источник артефактов.  
Он появляется не лицом, а следами.

Легенда:
Крылатое выражение: “Antimarketing / Open Source / Post‑Digital.”
Визуализация: аватар

Workbench: Extended Mind

Name: **Extended Mind**  
Type: —  
Slogan: Антимаркетинг, Open Source, Post‑Digital  
Focus: артефакты и редкие следы автора. Лаборатории, физические и поэтические выходы.  
Inputs: артефакты, практики фиксации.  
Outputs: signals / curated_sets / story‑nodes.  
Practices: reflection-fixation, curation, system-thinking.  
Preset Context: system:overview.  
Boundaries: не пересекается с виртуальными персонажами.  
UI: узнаваемая аватарка автора.  
Risks: переэкспонирование “автора”.

________________________________________

Карта перекрытия доменов  

**Artificial Intelligence & Computational Models**  
Workbench’и: Iron Fairy Tales, Appearance Atelier, Mojibake, Ji, Zucken‑Drücken, Solidol  
Практики: system-thinking, research-thinking, ecosystem-thinking

**Software & Digital Tools**  
Workbench’и: VSTablishment, Frame Grinder, Mojibake, Dream Graph, Contracts, Solidol, Ji  
Практики: possibility-navigation, interactive-thinking, system-thinking

**Visual & Media Arts**  
Workbench’и: Анимация +, Appearance Atelier, Frame Grinder, Homo Perceptivus, As if  
Практики: direction, visual-thinking, curation

**Music & Sound Culture**  
Workbench’и: Музыка в целом, VSTablishment, Zucken‑Drücken, As if  
Практики: sound-thinking, curation, direction

**Design & Aesthetic Systems**  
Workbench’и: Homo Perceptivus, Киберантика, Brand Direction  
Практики: visual-thinking, branding, systems-design

**Knowledge Systems & Cognitive Architectures**  
Workbench’и: Darwin’s Blind Spot, Evoquant, Mojibake, Mind's Lorgnette, Word Machine  
Практики: reflection-fixation, research-thinking, system-thinking

**Interactive Systems & Game Culture**  
Workbench’и: Playfield, Frame Grinder, Dream Graph  
Практики: interactive-thinking, system-thinking, possibility-navigation

**Architecture & Physical Realization**  
Workbench’и: Solidol  
Практики: architectural-design, systems-design, visual-thinking

________________________________________

Правила (Naming / Branding / Practices)

1) Workbench Naming v1  
IDs/spec/file names — английские.  
Сцена/брендинг — мультиязычные.  
Это не хаос: канон строгий, театр живой.

2) Нейминг — часть Brand Direction  
Нейминг здесь не украшение, а инструмент режиссуры внимания:  
как система звучит, так она и воспринимается.

3) Фичи → активы → портфолио  
Витрина ≠ канон.  
Любая фича должна:
1. быть привязана к практике,
2. оставлять след (signals / story-nodes),
3. не превращаться в каталог.

________________________________________

Notes  
Домены — не разделы сайта.  
Персонажи — не аватары.  
Workbench’и — не фичи.  
Это разные входы в один и тот же мир.
