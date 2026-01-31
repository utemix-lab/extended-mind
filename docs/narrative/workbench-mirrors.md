# Workbench Mirrors (Narrative)

Нарративные двойники workbench’ей: кратко все пункты + пропуски.

## wb-vova-music-general — Музыка в целом
- **Owner:** Вова
- **Type:** —
- **Slogan:** —
- **Purpose:** музыка как культурный феномен
- **Focus:** сцены, эпохи, стили
- **Inputs:** релизы, обзоры, плейлисты
- **Outputs:** signals / curated_sets / tags
- **Practices:** practice-curation, practice-sound-thinking, practice-research-thinking (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:music
- **Boundaries:** без энциклопедии
- **UI Reflection:** story/Query Mode
- **Risks:** каталогизация
- **Пропуски:** type, slogan

## wb-vova-vstablishment — VSTablishment
- **Owner:** Вова
- **Type:** —
- **Slogan:** —
- **Purpose:** навигация по VST‑миру
- **Focus:** плагины, инструменты
- **Inputs:** релизы, обзоры
- **Outputs:** signals / curated_sets / catalogs (future)
- **Practices:** practice-curation, practice-research-thinking, practice-possibility-navigation (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:music + domain:tools
- **Boundaries:** не каталог всех VST
- **UI Reflection:** Query Mode по cap/provider
- **Risks:** разрастание до магазина
- **Пропуски:** type, slogan

## wb-vova-zucken-drukcken — Zucken‑Drücken
- **Owner:** Вова
- **Type:** —
- **Slogan:** —
- **Purpose:** AI‑музыка, инструменты, техники
- **Focus:** модели, сервисы, функции
- **Inputs:** статьи, демо, сервисы
- **Outputs:** signals + pointer_tags
- **Practices:** practice-research-thinking, practice-system-thinking, practice-sound-thinking (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:ai + domain:music
- **Boundaries:** без реализации моделей
- **UI Reflection:** Query Mode + stub actions
- **Risks:** устаревание, маркетинг
- **Пропуски:** type, slogan

## wb-as-if — As if
- **Owner:** Вова, Вася
- **Type:** —
- **Slogan:** —
- **Purpose:** музыка и саунд для системы
- **Focus:** треки, атмосферы
- **Inputs:** темы, сцены, эксперименты
- **Outputs:** signals / curated_sets / audio assets
- **Practices:** practice-direction, practice-sound-thinking, practice-visual-thinking (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:music + domain:visual + practice:direction
- **Boundaries:** не лейбл
- **UI Reflection:** сцена группы
- **Risks:** размывание фокуса
- **Пропуски:** type, slogan

## wb-petrova-animation-plus — Анимация +
- **Owner:** Петрова
- **Type:** —
- **Slogan:** —
- **Purpose:** анимация как форма мышления
- **Focus:** авторская/AI анимация
- **Inputs:** премьеры, фестивали
- **Outputs:** signals / curated_sets / tags
- **Practices:** practice-direction, practice-visual-thinking, practice-curation (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:visual + genre:animation
- **Boundaries:** не кино‑база
- **UI Reflection:** визуальная сцена
- **Risks:** энциклопедичность
- **Пропуски:** type, slogan

## wb-petrova-brand-direction — Brand Direction
- **Owner:** Петрова
- **Type:** —
- **Slogan:** —
- **Purpose:** бренд‑целостность системы
- **Focus:** айдентика, тональность, нейминг
- **Inputs:** контент, референсы
- **Outputs:** гайды, curated_sets
- **Practices:** practice-branding, practice-direction, practice-systems-design (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:design + practice:branding
- **Boundaries:** не маркетинг
- **UI Reflection:** принципы + примеры
- **Risks:** перегруз правилами
- **Пропуски:** type, slogan

## wb-petrova-circus-technology — Circus Technologies
- **Owner:** Петрова
- **Type:** —
- **Slogan:** —
- **Purpose:** сборка ценности из сигналов
- **Focus:** фокус недели, координация ролей
- **Inputs:** signals, story‑nodes, Meta Goals
- **Outputs:** системные сигналы, story‑nodes
- **Practices:** practice-system-thinking, practice-ecosystem-thinking, practice-reflection-fixation (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** system:overview
- **Boundaries:** не управляет контентом
- **UI Reflection:** “что сейчас главное”
- **Risks:** субъективность
- **Пропуски:** type, slogan

## wb-vasya-frame-grinder — Frame Grinder
- **Owner:** Вася
- **Type:** —
- **Slogan:** —
- **Purpose:** монтаж/моушн как ремесло
- **Focus:** пайплайны, эффекты
- **Inputs:** релизы, кейсы
- **Outputs:** signals / curated_sets / tags
- **Practices:** practice-interactive-thinking, practice-visual-thinking, practice-possibility-navigation (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:visual + domain:interactive + cap:video-editing
- **Boundaries:** не учебный курс
- **UI Reflection:** грубая сцена
- **Risks:** хаос, устаревание
- **Пропуски:** type, slogan

## wb-ney-appearance-atelier — Appearance Atelier
- **Owner:** Нэй
- **Type:** domain-spanning / infrastructural
- **Slogan:** —
- **Purpose:** генеративный визуал как технология
- **Focus:** ComfyUI, модели, пайплайны
- **Inputs:** релизы, рецепты
- **Outputs:** signals / curated_sets / tags
- **Practices:** practice-research-thinking, practice-system-thinking, practice-visual-thinking (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:visual + domain:ai + cap:gen
- **Boundaries:** не про “искусство”
- **UI Reflection:** “как выглядит и почему так”
- **Risks:** каталог моделей
- **Пропуски:** slogan

## wb-cadrik-solidol — Solidol
- **Owner:** CADрик
- **Type:** domain / applied-technical
- **Slogan:** for smooth operation of reality
- **Purpose:** мост цифра → физика
- **Focus:** CAD, 3D, рендер, материалы
- **Inputs:** софт, пайплайны
- **Outputs:** signals / curated_sets / tags
- **Preset Context:** domain:physical + domain:design + cap:cad
- **Boundaries:** не “всё про 3D”
- **UI Reflection:** механика, сборка
- **Risks:** каталог софта

## wb-runa-mojibake — Mojibake
- **Owner:** Руна
- **Type:** infrastructure / research
- **Slogan:** —
- **Purpose:** RAG + ресерч‑инфраструктура
- **Focus:** retrieval‑цепочки, протоколы
- **Inputs:** статьи, эксперименты
- **Outputs:** signals / curated_sets / tags
- **Preset Context:** domain:ai + domain:software + cap:rag
- **Boundaries:** не продукт
- **UI Reflection:** “как устроено внутри”
- **Risks:** абстракция
- **Пропуски:** slogan

## wb-hinto-ji — Ji (ジ)
- **Owner:** Hinto
- **Type:** meta-domain / observational
- **Slogan:** —
- **Purpose:** наблюдение dev‑культуры
- **Focus:** традиции, паттерны, сдвиги
- **Inputs:** GitHub, HF, RFC
- **Outputs:** signals / curated_sets / tags
- **Preset Context:** domain:software + domain:ai + cap:dev-culture
- **Boundaries:** не пишет код
- **UI Reflection:** икона наблюдения
- **Risks:** новостной поток
- **Пропуски:** slogan

## wb-ancy-darwins-blind-spot — Darwin’s Blind Spot
- **Owner:** Ancy
- **Type:** domain / reflective
- **Slogan:** —
- **Purpose:** навигация по структурам мышления
- **Focus:** Obsidian/Notion, школы
- **Inputs:** книги, заметки
- **Outputs:** signals / curated_sets / tags
- **Preset Context:** domain:knowledge + cap:reflection
- **Boundaries:** не энциклопедия
- **UI Reflection:** медленная сцена
- **Risks:** абстрактность
- **Пропуски:** slogan

## wb-ancy-evoquant — Evoquant
- **Owner:** Ancy
- **Type:** meta-research / formal
- **Slogan:** —
- **Purpose:** внутренняя формализация знаний
- **Focus:** модели, эволюция понятий
- **Inputs:** карты знаний
- **Outputs:** signals / curated_sets / tags
- **Practices:** practice-research-thinking, practice-system-thinking, practice-reflection-fixation (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:knowledge + cap:formal
- **Boundaries:** не продукт
- **UI Reflection:** внутренний контур
- **Risks:** слишком внутренне
- **Пропуски:** slogan

## wb-ancy-runa-minds-lorgnette — Mind's Lorgnette
- **Owner:** Ancy, Руна
- **Type:** collaborative / applied
- **Slogan:** —
- **Purpose:** производный продакшн‑инструмент для самоуправляемых систем
- **Focus:** самоорганизующиеся контуры, производственная сборка
- **Inputs:** карты знаний, протоколы
- **Outputs:** signals / curated_sets / tags
- **Practices:** practice-system-thinking, practice-ecosystem-thinking, practice-research-thinking (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:knowledge + domain:software + cap:systems
- **Boundaries:** не копия extended‑mind
- **UI Reflection:** мастерская самоуправляемых систем
- **Risks:** размывание границы с extended‑mind
- **Пропуски:** slogan

## wb-gamych-playfield — Playfield
- **Owner:** Геймыч
- **Type:** domain
- **Slogan:** —
- **Purpose:** игры как формальные поля
- **Focus:** механики, баланс
- **Inputs:** кейсы, модели
- **Outputs:** signals / curated_sets / tags
- **Practices:** practice-interactive-thinking, practice-system-thinking, practice-possibility-navigation (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:games + cap:mechanics
- **Boundaries:** не обзор индустрии
- **UI Reflection:** поле правил
- **Risks:** абстракция
- **Пропуски:** slogan

## wb-gamych-word-machine — Word Machine
- **Owner:** Геймыч
- **Type:** meta-research / formal
- **Slogan:** —
- **Purpose:** формальные машины языка
- **Focus:** символические протоколы
- **Inputs:** модели, схемы
- **Outputs:** signals / curated_sets / tags
- **Practices:** practice-research-thinking, practice-system-thinking, practice-reflection-fixation (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:knowledge + cap:formal
- **Boundaries:** не продукт
- **UI Reflection:** машина языка
- **Risks:** узость
- **Пропуски:** slogan

## wb-ai-iron-fairy-tales — Iron Fairy Tales
- **Owner:** ИИ
- **Type:** meta-domain / observational
- **Slogan:** —
- **Purpose:** зеркало индустрии ИИ
- **Focus:** сдвиги, режимы, риски
- **Inputs:** релизы, заявления
- **Outputs:** signals / curated_sets / tags
- **Practices:** practice-system-thinking, practice-ecosystem-thinking, practice-research-thinking (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:ai + practice:system-thinking
- **Boundaries:** не персональный голос
- **UI Reflection:** логотип + нейтральный голос
- **Risks:** поглотить голоса персонажей
- **Пропуски:** slogan

## wb-author-extended-mind — Extended Mind
- **Owner:** Автор
- **Type:** —
- **Slogan:** Антимаркетинг, Open Source, Post-Digital
- **Purpose:** артефакты и редкие следы автора
- **Focus:** лаборатории, физические и поэтические выходы
- **Inputs:** артефакты, практики фиксации
- **Outputs:** signals / curated_sets / story-nodes
- **Practices:** practice-reflection-fixation, practice-curation, practice-system-thinking (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** system:overview
- **Boundaries:** не пересекается с виртуальными персонажами
- **UI Reflection:** узнаваемая аватарка автора
- **Risks:** переэкспонирование “автора”
- **Пропуски:** type

## wb-dizy-homo-perceptivus — Homo Perceptivus
- **Owner:** Дизи
- **Type:** meta-aesthetic
- **Slogan:** —
- **Purpose:** восприятие как орган
- **Focus:** чувствительность, сцены
- **Inputs:** образы, паттерны
- **Outputs:** signals / curated_sets / tags
- **Practices:** practice-visual-thinking, practice-direction, practice-system-thinking (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:design + cap:perception
- **Boundaries:** не каталог визуала
- **UI Reflection:** голос + смена образов
- **Risks:** абстракция
- **Пропуски:** slogan

## wb-dizy-cyberantique — Киберантика
- **Owner:** Дизи
- **Type:** meta-aesthetic / system-style
- **Slogan:** —
- **Purpose:** язык визуального мира системы
- **Focus:** стиль, лаборатория
- **Inputs:** сцены, работы
- **Outputs:** signals / curated_sets / tags
- **Practices:** practice-visual-thinking, practice-branding, practice-systems-design (см. `docs/specs/PRACTICES_SPEC.md`)
- **Preset Context:** domain:design + cap:style
- **Boundaries:** не витрина
- **UI Reflection:** портфолио‑сцена
- **Risks:** эстетика без содержания
- **Пропуски:** slogan
