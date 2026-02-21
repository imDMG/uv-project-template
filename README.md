# UV Template

Boilerplate для Python-проектов с строгой типизацией на базе `uv`, `ruff` и `basedpyright`.

## Требования

- [uv](https://github.com/astral-sh/uv) — менеджер пакетов и проектов для Python
- Python 3.13+ (устанавливается автоматически через `uv`)

## Быстрый старт

### 1. Клонирование

```cmd
git clone https://github.com/imDMG/uv-project-template myproject
cd myproject
```

### 2. Установка зависимостей

```cmd
uv sync
```

Эта команда:
- Создаст виртуальное окружение `.venv`
- Установит все зависимости из `pyproject.toml`
- Создаст/обновит `uv.lock`

### 3. Запуск проекта

```cmd
run
```

Или вручную:
```cmd
uv run main.py
```

## Доступные команды

| Команда | Описание |
|---------|----------|
| `run` | Запустить `main.py` |
| `uv run ruff check .` | Проверить код линтером |
| `uv run ruff format .` | Отформатировать код |
| `uv run basedpyright` | Проверить типы |

## Структура проекта

```
.
├── main.py                 # Точка входа
├── pyproject.toml          # Конфигурация проекта и зависимостей
├── .python-version         # Версия Python (для uv)
├── README.md               # Этот файл
└── main.py                 # Точка входа
```

## Настройки

### Ruff

- Линия: 79 символов
- Строгий режим проверки
- Автоформатирование docstrings

### Basedpyright

- `typeCheckingMode: strict`
- Python 3.13
- Проверка всех аннотаций типов

## Добавление зависимостей

```cmd
# Обычная зависимость
uv add <package>

# Dev-зависимость
uv add --dev <package>
```

## Лицензия

MIT
