# MiroFish — Agent Guide

## Что это

MiroFish — AI-движок прогнозирования и маркетинговых исследований на основе мультиагентных технологий. Два режима работы:
- **Классический** — загрузка файлов или промпт → параллельный цифровой мир с агентами (Twitter + Reddit) → прогнозный отчёт
- **Маркетинговый** — выбор тем из Topic Analyzer (Pikabu, Habr, VC.ru) + бриф → бизнес-онтология → маркетинговый отчёт (50-80 стр.)

## Стек

**Backend:** Python 3.11-3.12, Flask 3.0+, OpenAI SDK 1.0+, Zep Cloud 3.13.0, CAMEL-OASIS 0.2.5, CAMEL-AI 0.2.78, PyMuPDF, Pydantic 2.0+, requests, uv
**Frontend:** Vue.js 3.5, Vite 7.3, Vue Router 4.6, Axios 1.13, D3.js 7.9, Tailwind CSS 4.2
**Внешние сервисы:** LLM API (OpenAI-формат, рекомендуется Qwen-plus), Zep Cloud (GraphRAG), OASIS (CAMEL-AI), Topic Analyzer API, Tavily API (опционально)
**Деплой:** Docker, Docker Compose, Railway

## Структура

```
backend/app/
  api/          — REST API (graph.py, simulation.py, report.py)
  services/     — Бизнес-логика (16 сервисов)
  models/       — Данные (project.py, task.py)
  utils/        — Утилиты (llm_client, file_parser, logger, retry, zep_paging)
backend/scripts/ — Скрипты запуска OASIS-симуляций

frontend/src/
  views/        — 10 страниц (Home, ResearchStart, MainView, SimulationView, SimulationRunView, ReportView, InteractionView, Process, Privacy, Terms)
  components/   — 7 компонентов (GraphPanel, Step1-5, HistoryDatabase)
  api/          — HTTP-клиент (index.js + graph/simulation/report)
  router/       — SPA-маршрутизация
  store/        — Состояние загрузки файлов
```

## Два режима работы

### Режим A: Маркетинговое исследование
1. **Выбор тем** — оператор выбирает 1-5 тем из Topic Analyzer (Pikabu/Habr/VC.ru) + пишет бриф
2. **Обработка данных** — посты/комменты → PikabuFormatter (теги [source:pikabu/habr/vc]) → MarketSummarizer (LLM-сжатие 10-20x) → опциональный WebResearcher (Tavily)
3. **Построение графа** — бизнес-онтология (Competitor, Product, TargetSegment, PainPoint...) → Zep GraphRAG → D3.js
4. **Отчёт** — ReACT-агент с бизнес-инструментами (swot_builder, market_volume_calculator, segmentation_matrix) → 5 глав, temperature=0.1
5. **Взаимодействие** — чат с ReportAgent по готовому отчёту

### Режим B: Классический MiroFish (прогнозирование)
1. **Построение графа** — загрузка файлов / prompt-only → LLM-онтология (social mode) → Zep GraphRAG → D3.js
2. **Настройка среды** — извлечение сущностей → LLM-генерация профилей агентов → конфигурация симуляции
3. **Симуляция** — OASIS subprocess (Twitter + Reddit параллельно) → мониторинг actions.jsonl → обновление графа
4. **Отчёт** — ReACT-агент с инструментами (insight_forge, panorama_search, quick_search, interview_agents) → Markdown-отчёт
5. **Взаимодействие** — чат с ReportAgent и агентами мира

## Ключевые фичи

- Два режима: маркетинговое исследование (B2B) и прогнозирование
- Мультиселект тем из Topic Analyzer (Pikabu 22 темы, Habr 3 потока, VC.ru 38 категорий)
- Тегирование источников данных ([source:pikabu], [source:habr], [source:vc])
- LLM-суммаризация сырых данных (MarketSummarizer, сжатие 10-20x)
- Веб-обогащение через Tavily API (опционально)
- Два режима онтологий: social (люди, организации, медиа) и market_research (конкуренты, продукты, сегменты ЦА, боли)
- Маркетинговые инструменты ReportAgent: SWOT-анализ, оценка ёмкости рынка, сегментация ЦА
- Prompt-only режим — генерация сценария без загрузки файлов
- GraphRAG через Zep Cloud (семантический поиск, ротация ключей)
- Двухплатформенная параллельная симуляция (Twitter + Reddit)
- Интеллектуальная генерация профилей с обогащением через Zep
- ReACT-агент отчётов с реальным интервью агентов через OASIS API
- Структурированное логирование (agent_log.jsonl + console_log.txt)
- Асинхронные задачи с прогрессом в реальном времени
- Retry-механизмы на всех уровнях
- Кроссплатформенность (Windows + Unix)
- Docker-деплой одной командой

## Сервисы (backend/app/services/)

| Сервис | Назначение |
|---|---|
| `report_agent.py` | ReACT-агент отчётов (social + market_research), чат, логирование |
| `market_tools.py` | swot_builder, market_volume_calculator, segmentation_matrix |
| `market_summarizer.py` | LLM-сжатие сырых данных перед Zep |
| `web_researcher.py` | Tavily API — обогащение данных из интернета |
| `pikabu_formatter.py` | Форматтер данных Topic Analyzer → текст с тегами источников |
| `ontology_generator.py` | LLM-генерация онтологий (social / market_research) |
| `graph_builder.py` | Zep GraphRAG — построение графа знаний |
| `zep_tools.py` | Инструменты поиска по графу (insight_forge, panorama_search, quick_search, interview_agents) |
| `zep_entity_reader.py` | Чтение и фильтрация сущностей из Zep |
| `zep_graph_memory_updater.py` | Обновление графа после симуляции |
| `simulation_manager.py` | Управление состоянием симуляций |
| `simulation_runner.py` | Запуск OASIS subprocess |
| `simulation_ipc.py` | IPC с OASIS-процессом |
| `simulation_config_generator.py` | Генерация конфигурации симуляции |
| `oasis_profile_generator.py` | Генерация профилей агентов |
| `text_processor.py` | Чанкинг текста |

## API

### /api/graph/*
- `GET /project/<id>`, `GET /project/list`, `DELETE /project/<id>`, `POST /project/<id>/reset` — управление проектами
- `POST /ontology/generate` — загрузка файлов + генерация онтологии
- `POST /ontology/generate-from-prompt` — prompt-only режим
- `POST /ontology/generate-from-pikabu` — приём данных из Topic Analyzer
- `POST /ontology/generate-from-market-research` — мультитемное маркетинговое исследование (async)
- `GET /topics/external` — проксирование списка тем из Topic Analyzer
- `POST /build` — построение графа

### /api/simulation/*
- `POST /create`, `POST /prepare`, `POST /prepare/status` — создание и подготовка
- `GET /<id>`, `GET /list`, `GET /history` — состояние и история
- `GET /entities/<graph_id>`, `GET /entities/<graph_id>/<uuid>` — сущности графа
- Запуск, мониторинг, профили, интервью агентов

### /api/report/*
- `POST /generate`, `POST /generate/status` — генерация отчёта (async)
- `GET /<id>`, `GET /by-simulation/<id>` — получение отчёта
- `GET /<id>/progress`, `GET /<id>/sections`, `GET /<id>/section/<index>` — прогресс и разделы
- `GET /<id>/agent-log`, `GET /<id>/console-log` — логи (инкрементальные)
- `POST /chat` — чат с ReportAgent
- `GET /check/<simulation_id>` — проверка наличия отчёта

## Маршруты фронтенда

| Путь | Компонент | Назначение |
|---|---|---|
| `/` | Home | Лендинг, выбор режима |
| `/research` | ResearchStart | Маркетинговое исследование: бриф + выбор тем |
| `/process/:projectId` | MainView | Рабочий процесс: граф + настройка |
| `/simulation/:simulationId` | SimulationView | Настройка симуляции |
| `/simulation/:simulationId/start` | SimulationRunView | Запуск и мониторинг симуляции |
| `/report/:reportId` | ReportView | Генерация и просмотр отчёта |
| `/interaction/:reportId` | InteractionView | Чат с ReportAgent и агентами |
| `/privacy` | Privacy | Политика конфиденциальности |
| `/terms` | Terms | Условия использования |

## Конфигурация

Переменные окружения в `.env`:

| Переменная | Назначение | Обязательность |
|---|---|---|
| `LLM_API_KEY` | Ключ LLM API | Обязательно |
| `LLM_BASE_URL` | URL LLM API | Обязательно |
| `LLM_MODEL_NAME` | Модель LLM | Обязательно |
| `ZEP_API_KEY` | Zep Cloud (основной) | Обязательно |
| `ZEP_API_KEY_2`, `ZEP_API_KEY_3` | Zep Cloud (ротация) | Опционально |
| `LLM_BOOST_API_KEY/BASE_URL/MODEL_NAME` | Ускоренная LLM | Опционально |
| `TOPIC_ANALYZER_API_URL` | URL Topic Analyzer | Для маркетинговых исследований |
| `TAVILY_API_KEY` | Tavily Web Search | Опционально (обогащение данных) |

Порты: frontend 3000, backend 5001, Topic Analyzer 8000

## Запуск

```bash
cp .env.example .env   # Заполнить ключи
npm run setup:all      # Установить зависимости
npm run dev            # Запустить frontend + backend
```

## Важные детали для разработки

- Flask Application Factory в `backend/app/__init__.py`
- Vite proxy `/api` → `localhost:5001` в `frontend/vite.config.js`
- Симуляции запускаются как subprocess из `backend/scripts/`
- Логи симуляций: `backend/uploads/simulations/<sim_id>/`
- Отчёты: `backend/uploads/reports/<report_id>/`
- LLM-клиент поддерживает любой OpenAI-совместимый API
- Zep-клиент с retry, ротацией ключей и fallback на локальный поиск
- Профили агентов: JSON (Reddit) / CSV (Twitter)
- ReportAgent логирует в `agent_log.jsonl` (структурированный) и `console_log.txt`
- Онтология автоопределяет режим (social/market_research) по тегам данных
- MarketSummarizer сжимает данные в 10-20 раз перед отправкой в Zep
- Маркетинговые отчёты: temperature=0.1, обязательное цитирование, теги источников
- Генерация отчёта по главам: каждая глава — отдельный ReACT-цикл (3-5 вызовов инструментов)
