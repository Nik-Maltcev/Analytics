"""
Веб-ресёрчер для обогащения маркетинговых данных.

Этап перед загрузкой в Zep:
1. LLM генерирует поисковые запросы по брифу
2. Tavily API ищет актуальную информацию
3. Результаты форматируются и добавляются к документу

Агенты в симуляции получают обогащённые данные.
"""

import os
import json
import requests
from typing import List, Dict

from ..utils.llm_client import LLMClient
from ..utils.logger import get_logger

logger = get_logger('mirofish.web_researcher')

TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY', '')

QUERY_GENERATION_PROMPT = """\
Ты — аналитик маркетинговых исследований. На основе брифа клиента \
сгенерируй 5-8 поисковых запросов для веб-поиска, которые помогут \
собрать актуальную рыночную информацию.

Бриф: {brief}

Запросы должны покрывать:
- Объём и динамика рынка (TAM, рост)
- Ключевые конкуренты и их доли
- Ценообразование в нише
- Тренды и прогнозы
- Барьеры входа
- Целевая аудитория и её поведение

Верни JSON: {{"queries": ["запрос 1", "запрос 2", ...]}}
Запросы на русском, конкретные, пригодные для поиска в Google.
"""


def _search_tavily(query: str, max_results: int = 3) -> List[Dict]:
    """Поиск через Tavily API."""
    if not TAVILY_API_KEY:
        return []

    try:
        resp = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY_API_KEY,
                "query": query,
                "max_results": max_results,
                "search_depth": "basic",
                "include_answer": True,
            },
            timeout=15,
        )
        if resp.status_code == 200:
            data = resp.json()
            results = []
            # Добавляем AI-ответ если есть
            if data.get("answer"):
                results.append({
                    "title": "AI Summary",
                    "content": data["answer"],
                    "url": "",
                })
            # Добавляем результаты поиска
            for r in data.get("results", [])[:max_results]:
                results.append({
                    "title": r.get("title", ""),
                    "content": r.get("content", ""),
                    "url": r.get("url", ""),
                })
            return results
        else:
            logger.warning(f"Tavily API error {resp.status_code}: {resp.text[:200]}")
            return []
    except Exception as e:
        logger.warning(f"Tavily search failed for '{query}': {e}")
        return []


def enrich_with_web_research(
    document_text: str,
    brief: str,
    llm_client: LLMClient | None = None,
) -> str:
    """
    Обогащает документ данными из веб-поиска.

    Args:
        document_text: Суммаризированный аналитический документ
        brief: Бриф клиента
        llm_client: LLM-клиент

    Returns:
        Документ с добавленной секцией веб-ресёрча
    """
    if not TAVILY_API_KEY:
        logger.info("TAVILY_API_KEY не настроен — пропускаем веб-ресёрч")
        return document_text

    if llm_client is None:
        llm_client = LLMClient()

    # 1. Генерируем поисковые запросы
    logger.info("Генерация поисковых запросов по брифу...")
    try:
        prompt = QUERY_GENERATION_PROMPT.format(brief=brief or "Общий анализ рынка")
        queries_json = llm_client.chat_json(
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1024,
        )
        queries = queries_json.get("queries", [])[:8]
    except Exception as e:
        logger.warning(f"Ошибка генерации запросов: {e}")
        return document_text

    if not queries:
        logger.info("Нет запросов для поиска")
        return document_text

    logger.info(f"Сгенерировано {len(queries)} запросов: {queries}")

    # 2. Ищем по каждому запросу
    all_findings = []
    for i, query in enumerate(queries):
        logger.info(f"Поиск [{i+1}/{len(queries)}]: {query}")
        results = _search_tavily(query, max_results=3)
        if results:
            finding = f"### {query}\n"
            for r in results:
                title = r.get("title", "")
                content = r.get("content", "")
                url = r.get("url", "")
                if content:
                    finding += f"- **{title}**: {content[:500]}"
                    if url:
                        finding += f" ({url})"
                    finding += "\n"
            all_findings.append(finding)

    if not all_findings:
        logger.info("Веб-поиск не дал результатов")
        return document_text

    # 3. Добавляем к документу
    web_section = (
        "\n\n---\n\n"
        "## Дополнительные данные из веб-ресёрча\n\n"
        "Актуальная информация из открытых источников, собранная автоматически:\n\n"
        + "\n".join(all_findings)
    )

    enriched = document_text + web_section
    logger.info(
        f"Документ обогащён: {len(document_text)} → {len(enriched)} символов "
        f"(+{len(web_section)} из {len(all_findings)} запросов)"
    )
    return enriched
