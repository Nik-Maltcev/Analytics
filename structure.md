# MiroFish Market Research — Структура проекта

## Текущая архитектура (до рефакторинга)

```
MiroFish/
├── backend/                          # Flask 3.0 + Python 3.11
│   ├── app/
│   │   ├── __init__.py               # Application Factory
│   │   ├── config.py                 # Конфигурация (.env)
│   │   ├── api/
│   │   │   ├── __init__.py           # Blueprint-ы: graph_bp, simulation_bp, report_bp
│   │   │   ├── graph.py              # /api/graph/* — проекты, онтологии, графы
│   │   │   ├── simulation.py         # /api/simulation/* — OASIS симуляции
│   │   │   └── report.py             # /api/report/* — отчёты, чат
│   │   ├── services/
│   │   │   ├── graph_builder.py      # Zep GraphRAG
│   │   │   ├── ontology_generator.py # LLM онтология — РЕФАКТОРИНГ (бизнес-сущности)
│   │   │   ├── report_agent.py       # ReACT-агент — ПОЛНАЯ ПЕРЕРАБОТКА
│   │   │   ├── text_processor.py     # Чанкинг текста
│   │   │   ├── pikabu_formatter.py   # Форматтер данных из PIKABU
│   │   │   ├── zep_tools.py          # Инструменты поиска по графу
│   │   │   ├── zep_entity_reader.py  # Чтение сущностей из Zep
│   │   │   ├── simulation_manager.py # OASIS менеджер — ОСТАЁТСЯ
│   │   │   ├── simulation_runner.py  # OASIS раннер — ОСТАЁТСЯ
│   │   │   ├── simulation_ipc.py     # IPC — ОСТАЁТСЯ
│   │   │   ├── simulation_config_generator.py  # ОСТАЁТСЯ
│   │   │   ├── oasis_profile_generator.py      # ОСТАЁТСЯ
│   │   │   └── zep_graph_memory_updater.py     # ОСТАЁТСЯ
│   │   ├── models/
│   │   │   ├── project.py            # Управление проектами
│   │   │   └── task.py               # Асинхронные задачи
│   │   └── utils/
│   │       ├── llm_client.py         # OpenAI-совместимый клиент
│   │       ├── file_parser.py        # PDF/MD/TXT парсинг — ОСТАЁТСЯ (fallback)
│   │       ├── logger.py             # Логирование
│   │       ├── retry.py              # Retry-механизм
│   │       └── zep_paging.py         # Пагинация Zep API
│   ├── scripts/                      # OASIS скрипты — ОСТАЮТСЯ
│   ├── run.py                        # Точка входа
│   └── pyproject.toml                # Зависимости
├── frontend/                         # Vue.js 3.5 + Vite 7.2
│   ├── src/
│   │   ├── views/
│   │   │   ├── Home.vue              # Главная — РЕФАКТОРИНГ (dropdown + upload)
│   │   │   ├── MainView.vue          # Рабочий процесс — РЕФАКТОРИНГ (новый flow)
│   │   │   ├── ReportView.vue        # Отчёт — РЕФАКТОРИНГ (прогресс по главам)
│   │   │   ├── InteractionView.vue   # Чат с агентом — ОСТАЁТСЯ
│   │   │   ├── SimulationView.vue    # Симуляция — ОСТАЁТСЯ (опционально)
│   │   │   └── SimulationRunView.vue # Запуск симуляции — ОСТАЁТСЯ
│   │   ├── components/
│   │   │   ├── GraphPanel.vue        # D3.js визуализация — ОСТАЁТСЯ
│   │   │   ├── Step1GraphBuild.vue   # Шаг 1 — РЕФАКТОРИНГ (dropdown + upload)
│   │   │   ├── Step2EnvSetup.vue     # Шаг 2 — ОСТАЁТСЯ (опционально)
│   │   │   ├── Step3Simulation.vue   # Шаг 3 — ОСТАЁТСЯ (опционально)
│   │   │   ├── Step4Report.vue       # Генерация отчёта — РЕФАКТОРИНГ
│   │   │   ├── Step5Interaction.vue  # Чат — ОСТАЁТСЯ
│   │   │   └── HistoryDatabase.vue   # История — ОСТАЁТСЯ
│   │   ├── api/
│   │   │   ├── index.js              # Axios instance
│   │   │   ├── graph.js              # API графов
│   │   │   ├── simulation.js         # API симуляций — ОСТАЁТСЯ
│   │   │   └── report.js             # API отчётов
│   │   ├── router/index.js           # Маршруты — ОСТАЁТСЯ
│   │   └── store/pendingUpload.js    # Состояние загрузки
│   └── vite.config.js
├── PIKABU/                           # Topic Analyzer (отдельный репозиторий)
│   └── backend/
│       └── app/
│           ├── api/router.py         # GET /api/topics, POST /api/export/mirofish
│           ├── models/database.py    # ORM: Topic, Post, Comment
│           └── services/
│               └── mirofish_sender.py # Отправка данных в MiroFish
└── .env.example
```

## Целевая архитектура (после рефакторинга)

### Пользовательский flow — два режима

**Режим A: Маркетинговое исследование (НОВЫЙ)**
```
Шаг 1: Выбор темы из Topic Analyzer (dropdown)
  → MiroFish дёргает Topic Analyzer API
  → Данные (посты/комменты) приходят через существующий
    POST /api/graph/ontology/generate-from-pikabu
  → Бизнес-онтология → Zep GraphRAG → визуализация

Шаг 2: Генерация маркетингового отчёта
  → ReACT-агент с бизнес-инструментами
  → 5 глав: Executive Summary, Ёмкость рынка, SWOT, ЦА, PEST
  → Прогресс-бар по главам

Шаг 3: Взаимодействие
  → Чат с ReportAgent по готовому отчёту
```

**Режим B: Классический MiroFish (ОСТАЁТСЯ)**
```
Загрузка файлов / prompt-only → онтология → граф
  → Настройка среды → OASIS симуляция
  → Генерация отчёта → Взаимодействие
```

### Новые/изменённые файлы

| Файл | Действие | Описание |
|---|---|---|
| `backend/app/services/market_tools.py` | НОВЫЙ | swot_builder, market_volume_calculator, segmentation_matrix |
| `backend/app/services/ontology_generator.py` | РЕФАКТОРИНГ | Добавить бизнес-режим онтологии |
| `backend/app/services/report_agent.py` | РЕФАКТОРИНГ | Добавить маркетинговый режим (промпты, temperature, структура) |
| `backend/app/api/graph.py` | РЕФАКТОРИНГ | Новый эндпоинт для проксирования тем из Topic Analyzer |
| `backend/app/config.py` | ИЗМЕНЕНИЕ | Добавить TOPIC_ANALYZER_API_URL |
| `frontend/src/views/Home.vue` | РЕФАКТОРИНГ | Добавить dropdown для выбора темы |
| `frontend/src/components/Step1GraphBuild.vue` | РЕФАКТОРИНГ | Dropdown + существующий upload |
| `frontend/src/views/ReportView.vue` | РЕФАКТОРИНГ | Прогресс по главам |

### Связь между проектами (через API)

```
Frontend (Vue.js, порт 3000)
    │
    ├── MiroFish Backend (Flask, порт 5001)
    │   ├── Zep Cloud API (графы, поиск)
    │   └── → HTTP → Topic Analyzer API (порт 8000)
    │                  └── PostgreSQL (посты, комменты)
    │
    └── Topic Analyzer API (порт 8000) [для списка тем]
```
