# KB Pipeline (GitHub → Hugging Face)

Цель: превратить содержимое репозитория `extended-mind` в обновляемую “память”:
- нарезанные фрагменты (chunks),
- эмбеддинги,
- поисковый индекс.

## Источники

В v0 индексируются папки:

- `manifest/`
- `patterns/`
- `adr/`
- `docs/`

Идея: сначала индексируем “тяжёлое и нормативное”, без шумных архивов.

## Артефакты

Сборка генерирует:

- `chunks.jsonl` — по одной строке на чанк:
  - `rel_path` (путь файла в репо)
  - `title_path` (цепочка заголовков)
  - `text` (текст чанка)
  - `chunk_id` / `sha1` (стабильный id)
- `embeddings.npy` — float32 матрица (N x D), нормализованные эмбеддинги
- `faiss.index` — индекс для поиска по cosine (через inner product)
- `build_info.json` — метаданные сборки (дата, git sha, параметры)

## Публикация

Артефакты пушатся в Hugging Face Dataset:

- `utemix/extended-mind-kb`

Это версионируемое хранилище “памяти”.

## Обновление

Workflow GitHub Actions запускается при пуше в `main`,
если изменения затронули источники или инструменты сборки.

## Отладка

Если workflow упал:

1. открыть GitHub Actions run и взять лог
2. сравнить с `docs/machine-log/` (если вели записи)
3. локально воспроизвести:

```bash
export HF_TOKEN="..."
python tools/kb_build/build_kb.py --dataset-repo "utemix/extended-mind-kb"
