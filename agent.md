# MiroFish — Agent Guide

## Что это

MiroFish — AI-движок прогнозирования на основе мультиагентных технологий. Из неструктурированных данных (PDF, MD, TXT) автоматически строится параллельный цифровой мир с тысячами агентов, которые взаимодействуют на платформах Twitter и Reddit. Результат — прогнозный отчёт и интерактивный мир для глубокого анализа.

## Стек

**Backend:** Python 3.11-3.12, Flask 3.0+, OpenAI SDK, Zep Cloud 3.13.0, CAMEL-OASIS 0.2.5, PyMuPDF, Pydantic 2.0+, uv
**Frontend:** Vue.js 3.5, Vite 7.2, Vue Router 4.6, Axios, D3.js 7.9
**Внешние сервисы:** LLM API (OpenAI-формат, рекомендуется Qwen-plus), Zep Cloud (GraphRAG), OASIS (CAMEL-AI)
**Деплой:** Docker, Docker Compose, Railway

## Структура

```
backend/app/
  api/          — REST API (graph.py, simulation.py, report.py)
  services/     — Бизнес-логика (12 сервисов)
  models/       — Данные (project.py, task.py)
  utils/        — Утилиты (llm_client, file_parser, logger, retry, zep_paging)
backend/scripts/ — Скрипты запуска OASIS-симуляций

frontend/src/
  views/        — 7 страниц (Home, MainView, SimulationView, SimulationRunView, ReportView, InteractionView, Process)
  components/   — 7 компонентов (GraphPanel, Step1-5, HistoryDatabase)
  api/          — HTTP-клиент (index.js + graph/simulation/report)
  router/       — SPA-маршрутизация
  store/        — Состояние загрузки файлов
```

## Рабочий процесс (5 шагов)

1. **Построение графа** — загрузка документов → LLM-онтология → Zep GraphRAG → D3.js визуализация
2. **Настройка среды** — извлечение сущностей → LLM-генерация профилей агентов (2000 слов каждый) → конфигурация симуляции
3. **Симуляция** — OASIS subprocess (Twitter + Reddit параллельно) → мониторинг actions.jsonl → опциональное обновление графа
4. **Отчёт** — ReACT-агент с 4 инструментами (insight_forge, panorama_search, quick_search, interview_agents) → Markdown-отчёт
5. **Взаимодействие** — чат с ReportAgent и агентами мира

## Ключевые фичи

- Prompt-only режим (без загрузки файлов)
- Автоматическая генерация онтологий через LLM
- GraphRAG через Zep Cloud (семантический поиск, временные метки фактов)
- Двухплатформенная параллельная симуляция (Twitter + Reddit)
- Интеллектуальная генерация профилей с обогащением через Zep
- ReACT-агент отчётов с реальным интервью агентов через OASIS API
- Асинхронные задачи с прогрессом в реальном времени
- Retry-механизмы на всех уровнях
- Кроссплатформенность (Windows + Unix)
- Docker-деплой одной командой

## API

- `/api/graph/*` — проекты, онтологии, построение графов, данные графов
- `/api/simulation/*` — сущности, создание/подготовка/запуск симуляций, мониторинг
- `/api/report/*` — генерация отчётов, прогресс, разделы, скачивание, чат, логи

## Конфигурация

Переменные окружения в `.env`:
- `LLM_API_KEY`, `LLM_BASE_URL`, `LLM_MODEL_NAME` — LLM API
- `ZEP_API_KEY` — Zep Cloud
- Порты: frontend 3000, backend 5001

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
- Zep-клиент с retry и fallback на локальный поиск
- Профили агентов: JSON (Reddit) / CSV (Twitter)
- ReportAgent логирует в `agent_log.jsonl` (структурированный) и `console_log.txt`
