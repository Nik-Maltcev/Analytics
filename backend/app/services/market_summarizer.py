"""
Суммаризатор данных для маркетингового исследования.

Сжимает сырые посты/комменты через LLM перед отправкой в Zep,
сокращая потребление Zep-токенов в 10-20 раз.

Флоу: сырые посты → чанки → LLM суммаризация каждого чанка → финальная сводка → Zep
"""

import json
import re
from typing import List, Dict, Any

from ..utils.llm_client import LLMClient
from ..utils.logger import get_logger

logger = get_logger('mirofish.market_summarizer')

CHUNK_SUMMARY_PROMPT = """\
Ты — аналитик маркетинговых данных. Тебе дан блок постов и комментариев \
с форумов (Pikabu, Habr, VC.ru).

Извлеки и сжато опиши:
1. Ключевые темы и тренды (что обсуждают)
2. Боли и проблемы пользователей (на что жалуются)
3. Упомянутые продукты, компании, бренды
4. Ценовые ожидания и бюджеты (если есть)
5. Сегменты аудитории (кто пишет, какие роли)

Пиши компактно, по делу, на русском. Сохраняй конкретику: цифры, названия, цитаты.
Не пиши вводных фраз. Максимум 2000 символов.

Данные:
"""

FINAL_MERGE_PROMPT = """\
Ты — аналитик маркетинговых данных. Тебе даны сводки по нескольким блокам данных \
из форумов (Pikabu, Habr, VC.ru) по теме маркетингового исследования.

Бриф клиента: {brief}

Объедини сводки в единый аналитический документ для построения графа знаний. \
Документ должен содержать:

1. **Обзор рынка** — основные тренды, размер обсуждений, настроения
2. **Ключевые игроки** — компании, продукты, бренды с контекстом
3. **Целевая аудитория** — сегменты, их боли, потребности, бюджеты
4. **Конкурентная среда** — кто с кем конкурирует, преимущества/недостатки
5. **Каналы и точки контакта** — где аудитория, как продвигаются
6. **Инсайты и возможности** — неочевидные находки, незанятые ниши

Пиши структурированно с заголовками. Сохраняй конкретику. На русском.
Максимум 8000 символов.

Сводки:
"""


def _estimate_tokens(text: str) -> int:
    """Грубая оценка токенов (4 символа ≈ 1 токен для русского)."""
    return len(text) // 4


def _split_into_chunks(text: str, max_chars: int = 60000) -> List[str]:
    """Разбивает текст на чанки по границам постов (## Пост)."""
    if len(text) <= max_chars:
        return [text]

    chunks = []
    current = ""

    for line in text.split("\n"):
        if line.startswith("## Пост ") and len(current) > max_chars * 0.7:
            chunks.append(current)
            current = line + "\n"
        else:
            current += line + "\n"

    if current.strip():
        chunks.append(current)

    return chunks if chunks else [text]


def summarize_market_data(
    document_text: str,
    brief: str = "",
    llm_client: LLMClient | None = None,
) -> str:
    """
    Суммаризирует сырые данные маркетингового исследования.

    Args:
        document_text: Полный текст от PikabuFormatter (сырые посты + комменты)
        brief: Бриф клиента
        llm_client: LLM-клиент (создаётся автоматически если не передан)

    Returns:
        Компактный аналитический документ (~5-10K символов)
    """
    if not document_text or len(document_text) < 500:
        return document_text

    if llm_client is None:
        llm_client = LLMClient()

    original_size = len(document_text)
    logger.info(f"Суммаризация: входной текст {original_size} символов (~{_estimate_tokens(document_text)} токенов)")

    # Разбиваем на чанки
    chunks = _split_into_chunks(document_text, max_chars=60000)
    logger.info(f"Разбито на {len(chunks)} чанков для суммаризации")

    # Суммаризируем каждый чанк
    summaries = []
    for i, chunk in enumerate(chunks):
        logger.info(f"Суммаризация чанка {i+1}/{len(chunks)} ({len(chunk)} символов)...")
        try:
            summary = llm_client.chat(
                messages=[{"role": "user", "content": CHUNK_SUMMARY_PROMPT + chunk}],
                temperature=0.3,
                max_tokens=2048,
            )
            summaries.append(summary.strip())
            logger.info(f"  Чанк {i+1}: {len(chunk)} → {len(summary)} символов")
        except Exception as e:
            logger.warning(f"  Ошибка суммаризации чанка {i+1}: {e}")
            # Fallback: берём первые 2000 символов чанка
            summaries.append(chunk[:2000])

    # Если один чанк — возвращаем его сводку
    if len(summaries) == 1:
        result = summaries[0]
        logger.info(f"Суммаризация завершена: {original_size} → {len(result)} символов (x{original_size // max(len(result), 1)} сжатие)")
        return result

    # Объединяем сводки в финальный документ
    merged_summaries = "\n\n---\n\n".join(
        f"### Блок {i+1}\n{s}" for i, s in enumerate(summaries)
    )

    logger.info(f"Финальное объединение {len(summaries)} сводок ({len(merged_summaries)} символов)...")
    try:
        prompt = FINAL_MERGE_PROMPT.format(brief=brief or "Не указан") + merged_summaries
        result = llm_client.chat(
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=4096,
        )
        result = result.strip()
    except Exception as e:
        logger.warning(f"Ошибка финального объединения: {e}")
        result = merged_summaries

    logger.info(f"Суммаризация завершена: {original_size} → {len(result)} символов (x{original_size // max(len(result), 1)} сжатие)")
    return result
