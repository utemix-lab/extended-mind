# Visual Guardrails v1

Визуал событийный, а не структурный.  
Навигация остаётся абстрактной, визуал — сценой.

## Термины

- **Story = сцена** (нарратив/образы/фоны/аллегории)
- **System = карта** (где я и какие связи)
- **Service = действие** (Query Mode, генерация, сохранение)
- **Terminal Visual** — логотипы/обложки/постеры показываются только в terminal‑точке

## Правила

1. **No visual catalogs**  
   Нельзя делать сетки логотипов/обложек как основной UI‑навигации.
2. **Terminal Visual only**  
   Визуал показывается только в выбранной карточке/terminal‑точке.
3. **Anchor visuals only**  
   Постоянные якоря — только для верхнего уровня (Domains, Characters, Countries, core Practices).
4. **Assets via manifest**  
   Визуальные ассеты подключаются из `contracts/public/assets/...` через manifest.

## Привязка к целям

- [UG-3] карта без утопления
- [SG-1] рост без ломки
- [LG-1] лаборатория сценографии
- [MG-1] визуал как пред‑контент

## See also
- `PERCEPTUAL_SCENOGRAPHY.md`
- `SYSTEM_GOALS.md`
- `SYSTEM_GUARDRAILS.md`
