# MiroFish — Полная документация проекта

> Универсальный движок коллективного интеллекта, прогнозирующий всё.
> A Simple and Universal Swarm Intelligence Engine, Predicting Anything.

## 1. Обзор проекта

MiroFish — AI-движок прогнозирования нового поколения на основе мультиагентных технологий. Из неструктурированных данных (новости, отчёты, романы, политические документы) автоматически строится высокоточный параллельный цифровой мир, в котором тысячи интеллектуальных агентов с уникальными личностями, долгосрочной памятью и поведенческой логикой свободно взаимодействуют и эволюционируют. Пользователь может динамически вводить переменные с «позиции бога» и точно моделировать будущие сценарии.

**Ключевые характеристики:**
- Стоимость ~$5 за симуляцию
- Масштаб до 1 000 000 агентов
- Поддержка двух платформ (Twitter + Reddit) параллельно
- Лицензия: AGPL-3.0

**Репозиторий:** [github.com/666ghj/MiroFish](https://github.com/666ghj/MiroFish)

---

## 2. Технологический стек

### Backend
| Технология | Версия | Назначение |
|---|---|---|
| Python | ≥3.11, ≤3.12 | Язык бэкенда |
| Flask | ≥3.0.0 | Web-фреймворк |
| Flask-CORS | ≥6.0.0 | Поддержка CORS |
| OpenAI SDK | ≥1.0.0 | Клиент LLM API (OpenAI-совместимый формат) |
| Zep Cloud | 3.13.0 | Графовая память, извлечение сущностей, GraphRAG |
| CAMEL-OASIS | 0.2.5 | Движок мультиагентной симуляции |
| CAMEL-AI | 0.2.78 | Фреймворк AI-агентов |
| PyMuPDF | ≥1.24.0 | Извлечение текста из PDF |
| Pydantic | ≥2.0.0 | Валидация данных |
| uv | latest | Менеджер пакетов Python |

### Frontend
| Технология | Версия | Назначение |
|---|---|---|
| Vue.js | 3.5.24 | UI-фреймворк |
| Vite | 7.2.4 | Сборщик и dev-сервер |
| Vue Router | 4.6.3 | Маршрутизация SPA |
| Axios | 1.13.2 | HTTP-клиент с retry-механизмом |
| D3.js | 7.9.0 | Визуализация графов знаний |

### Внешние сервисы
| Сервис | Назначение |
|---|---|
| LLM API (OpenAI-формат) | Генерация онтологий, профилей, конфигураций, отчётов, чат |
| Zep Cloud | Графовая память, хранение сущностей и связей, семантический поиск |
| OASIS (CAMEL-AI) | Движок социальной симуляции (Twitter + Reddit) |

### Деплой
| Инструмент | Файл |
|---|---|
| Docker | `Dockerfile`, `docker-compose.yml` |
| Railway | `Dockerfile.railway`, `railway.json` |

---

## 3. Архитектура проекта

```
MiroFish/
├── backend/                    # Python бэкенд (Flask)
│   ├── app/
│   │   ├── __init__.py         # Flask Application Factory
│   │   ├── config.py           # Конфигурация (.env)
│   │   ├── api/                # REST API маршруты
│   │   │   ├── graph.py        # /api/graph/* — графы, проекты, онтологии
│   │   │   ├── simulation.py   # /api/simulation/* — сущности, симуляции
│   │   │   └── report.py       # /api/report/* — отчёты, чат
│   │   ├── services/           # Бизнес-логика
│   │   │   ├── graph_builder.py              # Построение графа через Zep
│   │   │   ├── ontology_generator.py         # LLM-генерация онтологий
│   │   │   ├── text_processor.py             # Обработка и чанкинг текста
│   │   │   ├── zep_entity_reader.py          # Чтение сущностей из Zep
│   │   │   ├── oasis_profile_generator.py    # Генерация профилей агентов
│   │   │   ├── simulation_config_generator.py # LLM-генерация конфигурации
│   │   │   ├── simulation_manager.py         # Управление состоянием симуляции
│   │   │   ├── simulation_runner.py          # Запуск и мониторинг процессов
│   │   │   ├── simulation_ipc.py             # IPC для управления процессами
│   │   │   ├── report_agent.py               # ReACT-агент генерации отчётов
│   │   │   ├── zep_tools.py                  # Инструменты поиска по графу
│   │   │   └── zep_graph_memory_updater.py   # Обновление памяти графа
│   │   ├── models/             # Модели данных
│   │   │   ├── project.py      # Управление проектами
│   │   │   └── task.py         # Асинхронные задачи
│   │   └── utils/              # Утилиты
│   │       ├── llm_client.py   # Обёртка OpenAI API
│   │       ├── file_parser.py  # Парсинг PDF/MD/TXT
│   │       ├── logger.py       # Логирование
│   │       ├── retry.py        # Retry-механизм
│   │       └── zep_paging.py   # Пагинация Zep API
│   ├── scripts/                # Скрипты запуска симуляций
│   │   ├── run_parallel_simulation.py  # Параллельная (Twitter+Reddit)
│   │   ├── run_twitter_simulation.py   # Только Twitter
│   │   ├── run_reddit_simulation.py    # Только Reddit
│   │   └── action_logger.py           # Логирование действий агентов
│   ├── run.py                  # Точка входа бэкенда
│   └── pyproject.toml          # Зависимости Python
├── frontend/                   # Vue.js фронтенд
│   ├── src/
│   │   ├── App.vue             # Корневой компонент
│   │   ├── main.js             # Точка входа
│   │   ├── router/index.js     # Маршруты SPA
│   │   ├── api/                # API-клиент
│   │   │   ├── index.js        # Axios instance + retry
│   │   │   ├── graph.js        # API графов
│   │   │   ├── simulation.js   # API симуляций
│   │   │   └── report.js       # API отчётов
│   │   ├── views/              # Страницы
│   │   │   ├── Home.vue        # Главная: загрузка файлов, история
│   │   │   ├── Process.vue     # Построение графа (устаревший)
│   │   │   ├── MainView.vue    # Основной рабочий процесс (5 шагов)
│   │   │   ├── SimulationView.vue    # Настройка симуляции
│   │   │   ├── SimulationRunView.vue # Мониторинг симуляции в реальном времени
│   │   │   ├── ReportView.vue        # Просмотр отчёта
│   │   │   └── InteractionView.vue   # Глубокое взаимодействие с агентами
│   │   ├── components/         # Компоненты
│   │   │   ├── GraphPanel.vue          # D3.js визуализация графа
│   │   │   ├── Step1GraphBuild.vue     # Шаг 1: Построение графа
│   │   │   ├── Step2EnvSetup.vue       # Шаг 2: Настройка среды
│   │   │   ├── Step3Simulation.vue     # Шаг 3: Запуск симуляции
│   │   │   ├── Step4Report.vue         # Шаг 4: Генерация отчёта
│   │   │   ├── Step5Interaction.vue    # Шаг 5: Взаимодействие
│   │   │   └── HistoryDatabase.vue     # История проектов
│   │   └── store/
│   │       └── pendingUpload.js # Хранилище загружаемых файлов
│   ├── vite.config.js          # Конфигурация Vite + proxy
│   └── package.json
├── .env.example                # Шаблон переменных окружения
├── docker-compose.yml          # Docker Compose
├── Dockerfile                  # Docker-образ
├── package.json                # Корневые скрипты (dev, build, setup)
└── README.md / README-EN.md    # Документация
```

---

## 4. Рабочий процесс (5 шагов)

### Шаг 1: Построение графа знаний
1. Пользователь загружает документы (PDF, MD, TXT) или использует prompt-only режим
2. LLM анализирует текст и генерирует онтологию (типы сущностей + типы связей)
3. Текст разбивается на чанки (`TextProcessor`)
4. Чанки отправляются в Zep для построения графа (`GraphBuilderService`)
5. Zep извлекает сущности и связи, строит GraphRAG
6. Фронтенд визуализирует граф в реальном времени через D3.js

**API:**
- `POST /api/graph/ontology/generate` — загрузка файлов + генерация онтологии
- `POST /api/graph/ontology/generate-from-prompt` — prompt-only режим
- `POST /api/graph/build` — асинхронное построение графа
- `GET /api/graph/task/<task_id>` — статус задачи
- `GET /api/graph/data/<graph_id>` — данные графа (узлы + рёбра)

### Шаг 2: Настройка среды симуляции
1. Чтение и фильтрация сущностей из Zep-графа (`ZepEntityReader`)
2. Для каждой сущности LLM генерирует детальный профиль агента (`OasisProfileGenerator`):
   - Биография, персона (2000 слов), возраст, пол, MBTI, профессия, интересы
   - Различение индивидуальных и групповых/организационных сущностей
   - Обогащение через Zep-поиск для более точных профилей
3. LLM генерирует конфигурацию симуляции (`SimulationConfigGenerator`):
   - Временные параметры, активность, частота публикаций, события
4. Сохранение профилей (JSON для Reddit, CSV для Twitter) и конфигурации

**API:**
- `GET /api/simulation/entities/<graph_id>` — получение сущностей
- `POST /api/simulation/create` — создание симуляции
- `POST /api/simulation/prepare` — подготовка среды (асинхронно)

### Шаг 3: Запуск симуляции
1. `SimulationRunner` запускает OASIS-скрипт как subprocess
2. Поддержка трёх режимов: Twitter, Reddit, Parallel (оба)
3. Мониторинг через чтение `actions.jsonl` логов в реальном времени
4. Каждое действие агента записывается: посты, лайки, репосты, комментарии
5. Опциональное обновление Zep-графа в реальном времени (`ZepGraphMemoryManager`)
6. Кроссплатформенное завершение процессов (Windows taskkill / Unix SIGTERM)

**API:**
- `POST /api/simulation/run` — запуск симуляции
- `GET /api/simulation/run/<simulation_id>/status` — статус в реальном времени
- `POST /api/simulation/run/<simulation_id>/stop` — остановка

### Шаг 4: Генерация отчёта
1. `ReportAgent` использует ReACT-паттерн (Reasoning + Acting)
2. Фаза планирования: LLM создаёт структуру отчёта (2-5 разделов)
3. Фаза генерации: для каждого раздела 3-5 вызовов инструментов:
   - `insight_forge` — глубокий анализ с декомпозицией на подвопросы
   - `panorama_search` — панорамный поиск с историей изменений
   - `quick_search` — быстрый поиск конкретных фактов
   - `interview_agents` — реальное интервью агентов через OASIS API
4. Каждый раздел содержит цитаты агентов, факты из графа, аналитику
5. Детальное логирование: `agent_log.jsonl` + `console_log.txt`

**API:**
- `POST /api/report/generate` — генерация отчёта (асинхронно)
- `GET /api/report/<report_id>` — получение отчёта
- `GET /api/report/<report_id>/progress` — прогресс генерации
- `GET /api/report/<report_id>/sections` — разделы отчёта
- `GET /api/report/<report_id>/download` — скачать Markdown

### Шаг 5: Глубокое взаимодействие
1. Чат с ReportAgent — задавайте вопросы по отчёту
2. Чат с любым агентом симулированного мира
3. ReportAgent может вызывать инструменты поиска для ответов

**API:**
- `POST /api/report/chat` — чат с агентом

---

## 5. Ключевые фичи

### Ядро
- **Prompt-only режим** — LLM генерирует сценарий без загрузки файлов
- **Автоматическая генерация онтологий** — LLM анализирует документ и создаёт типы сущностей/связей
- **GraphRAG через Zep** — семантический поиск, извлечение сущностей, временные метки фактов
- **Двухплатформенная симуляция** — Twitter + Reddit параллельно через OASIS
- **Интеллектуальная генерация профилей** — LLM создаёт детальные персоны (2000 слов) с обогащением через Zep
- **ReACT-агент отчётов** — многошаговое рассуждение с инструментами поиска
- **Интервью агентов** — реальный опрос агентов через OASIS API

### Инфраструктура
- **Асинхронные задачи** — долгие операции не блокируют UI, прогресс в реальном времени
- **Визуализация графа** — D3.js с интерактивным выбором узлов/рёбер
- **Персистентность проектов** — сохранение и возобновление проектов
- **Retry-механизмы** — на уровне API-клиента, Zep-вызовов, LLM-генерации
- **Кроссплатформенность** — корректная работа на Windows и Unix
- **Docker-деплой** — одна команда для запуска всего стека

### Безопасность и устойчивость
- **Автоматическое определение кодировки** — charset-normalizer + chardet для не-UTF-8 файлов
- **Восстановление JSON** — автоматическое исправление обрезанного/повреждённого JSON от LLM
- **Graceful shutdown** — корректное завершение всех subprocess при остановке сервера
- **Fallback-поиск** — локальный keyword-matching при недоступности Zep Search API

---

## 6. API Reference

### Graph API (`/api/graph/`)

| Метод | Путь | Описание |
|---|---|---|
| GET | `/project/<project_id>` | Получить проект |
| GET | `/project/list` | Список проектов |
| DELETE | `/project/<project_id>` | Удалить проект |
| POST | `/project/<project_id>/reset` | Сбросить проект |
| POST | `/ontology/generate` | Загрузить файлы + сгенерировать онтологию |
| POST | `/ontology/generate-from-prompt` | Prompt-only генерация |
| POST | `/build` | Построить граф (async) |
| GET | `/task/<task_id>` | Статус задачи |
| GET | `/data/<graph_id>` | Данные графа |
| DELETE | `/delete/<graph_id>` | Удалить граф |

### Simulation API (`/api/simulation/`)

| Метод | Путь | Описание |
|---|---|---|
| GET | `/entities/<graph_id>` | Сущности графа (фильтрованные) |
| GET | `/entities/<graph_id>/<entity_uuid>` | Детали сущности |
| GET | `/entities/<graph_id>/by-type/<type>` | Сущности по типу |
| POST | `/create` | Создать симуляцию |
| POST | `/prepare` | Подготовить среду (async) |
| POST | `/prepare/status` | Статус подготовки |
| GET | `/<simulation_id>` | Состояние симуляции |
| GET | `/list` | Список симуляций |
| GET | `/history` | История с деталями проектов |
| POST | `/run` | Запустить симуляцию |
| GET | `/run/<id>/status` | Статус выполнения |
| POST | `/run/<id>/stop` | Остановить |

### Report API (`/api/report/`)

| Метод | Путь | Описание |
|---|---|---|
| POST | `/generate` | Сгенерировать отчёт (async) |
| POST | `/generate/status` | Статус генерации |
| GET | `/<report_id>` | Получить отчёт |
| GET | `/by-simulation/<sim_id>` | Отчёт по симуляции |
| GET | `/list` | Список отчётов |
| GET | `/<report_id>/download` | Скачать Markdown |
| POST | `/chat` | Чат с агентом |
| GET | `/<report_id>/progress` | Прогресс генерации |
| GET | `/<report_id>/sections` | Разделы отчёта |
| GET | `/<report_id>/section/<index>` | Один раздел |
| GET | `/<report_id>/agent-log` | Лог агента (JSONL) |
| GET | `/<report_id>/console-log` | Консольный лог |

---

## 7. Конфигурация

### Переменные окружения (`.env`)

```env
# Обязательные
LLM_API_KEY=your_api_key           # Ключ LLM API
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1  # URL LLM API
LLM_MODEL_NAME=qwen-plus           # Модель LLM
ZEP_API_KEY=your_zep_api_key       # Ключ Zep Cloud

# Опциональные
LLM_BOOST_API_KEY=...              # Ускоренный LLM (опционально)
LLM_BOOST_BASE_URL=...
LLM_BOOST_MODEL_NAME=...
FLASK_DEBUG=True                   # Режим отладки
FLASK_HOST=0.0.0.0                 # Хост
PORT=5001                          # Порт бэкенда
OASIS_DEFAULT_MAX_ROUNDS=10        # Макс. раундов симуляции по умолчанию
```

### Порты
- Frontend: `3000`
- Backend: `5001`
- Vite proxy: `/api` → `localhost:5001`

---

## 8. Запуск

### Из исходников (рекомендуется)

```bash
# 1. Настроить переменные окружения
cp .env.example .env
# Заполнить LLM_API_KEY и ZEP_API_KEY

# 2. Установить зависимости
npm run setup:all

# 3. Запустить
npm run dev
```

### Docker

```bash
cp .env.example .env
docker compose up -d
```

### Отдельный запуск

```bash
npm run backend    # Только бэкенд
npm run frontend   # Только фронтенд
```

---

## 9. Поток данных

```
Пользователь загружает документ
        ↓
  [Home.vue] → POST /api/graph/ontology/generate
        ↓
  LLM генерирует онтологию (типы сущностей + связей)
        ↓
  POST /api/graph/build → GraphBuilderService
        ↓
  Текст → чанки → Zep → граф знаний
        ↓
  POST /api/simulation/create + /prepare
        ↓
  ZepEntityReader → OasisProfileGenerator → SimulationConfigGenerator
        ↓
  POST /api/simulation/run → SimulationRunner (subprocess)
        ↓
  OASIS: Twitter + Reddit параллельно
  actions.jsonl ← мониторинг в реальном времени
        ↓
  POST /api/report/generate → ReportAgent (ReACT)
        ↓
  insight_forge / panorama_search / interview_agents
        ↓
  Markdown-отчёт + чат с агентами
```
