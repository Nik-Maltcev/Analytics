"""
Маркетинговые инструменты для ReportAgent.

Три специализированных инструмента для генерации маркетинговых исследований:
1. swot_builder — SWOT-анализ конкурента
2. market_volume_calculator — оценка ёмкости рынка
3. segmentation_matrix — сегментация целевой аудитории

Все инструменты работают поверх Zep GraphRAG и учитывают теги источников.
"""

import re
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

from ..config import Config
from ..utils.llm_client import LLMClient
from ..utils.logger import get_logger
from .zep_tools import ZepToolsService, SearchResult

logger = get_logger('mirofish.market_tools')


@dataclass
class SwotResult:
    """Результат SWOT-анализа."""
    competitor_name: str
    strengths: List[str] = field(default_factory=list)
    weaknesses: List[str] = field(default_factory=list)
    opportunities: List[str] = field(default_factory=list)
    threats: List[str] = field(default_factory=list)
    source_facts: List[str] = field(default_factory=list)

    def to_text(self) -> str:
        parts = [
            f"## SWOT-анализ: {self.competitor_name}",
            f"\n**Strengths (Сильные стороны):** {len(self.strengths)}",
        ]
        for s in self.strengths:
            parts.append(f"- {s}")
        parts.append(f"\n**Weaknesses (Слабые стороны):** {len(self.weaknesses)}")
        for w in self.weaknesses:
            parts.append(f"- {w}")
        parts.append(f"\n**Opportunities (Возможности):** {len(self.opportunities)}")
        for o in self.opportunities:
            parts.append(f"- {o}")
        parts.append(f"\n**Threats (Угрозы):** {len(self.threats)}")
        for t in self.threats:
            parts.append(f"- {t}")
        if self.source_facts:
            parts.append(f"\n**Исходные факты из графа:** {len(self.source_facts)}")
            for i, f_ in enumerate(self.source_facts[:10], 1):
                parts.append(f'{i}. "{f_}"')
        return "\n".join(parts)


@dataclass
class MarketVolumeResult:
    """Результат оценки ёмкости рынка."""
    query: str
    numeric_mentions: List[Dict[str, str]] = field(default_factory=list)
    market_facts: List[str] = field(default_factory=list)
    summary: str = ""

    def to_text(self) -> str:
        parts = [
            f"## Оценка ёмкости рынка",
            f"Запрос: {self.query}",
        ]
        if self.numeric_mentions:
            parts.append(f"\n**Числовые упоминания:** {len(self.numeric_mentions)}")
            for m in self.numeric_mentions:
                parts.append(f'- {m.get("value", "?")} — "{m.get("context", "")}"')
        if self.market_facts:
            parts.append(f"\n**Факты о рынке:** {len(self.market_facts)}")
            for i, f_ in enumerate(self.market_facts, 1):
                parts.append(f'{i}. "{f_}"')
        if self.summary:
            parts.append(f"\n**Сводка:** {self.summary}")
        return "\n".join(parts)


@dataclass
class SegmentationResult:
    """Результат сегментации аудитории."""
    query: str
    segments: List[Dict[str, Any]] = field(default_factory=list)
    pain_facts: List[str] = field(default_factory=list)

    def to_text(self) -> str:
        parts = [
            f"## Сегментация целевой аудитории",
            f"Запрос: {self.query}",
        ]
        if self.segments:
            parts.append(f"\n**Выявлено сегментов:** {len(self.segments)}")
            for seg in self.segments:
                parts.append(f'\n**Сегмент: {seg.get("name", "?")}**')
                parts.append(f'- Описание: {seg.get("description", "")}')
                parts.append(f'- Размер (упоминаний): {seg.get("mentions", 0)}')
                if seg.get("barriers"):
                    parts.append(f'- Барьеры: {", ".join(seg["barriers"])}')
                if seg.get("quotes"):
                    for q in seg["quotes"][:3]:
                        parts.append(f'  > "{q}"')
        if self.pain_facts:
            parts.append(f"\n**Исходные боли/жалобы:** {len(self.pain_facts)}")
            for i, f_ in enumerate(self.pain_facts[:15], 1):
                parts.append(f'{i}. "{f_}"')
        return "\n".join(parts)


# ═══════════════════════════════════════════════════════════════
# Описания инструментов для промптов ReportAgent
# ═══════════════════════════════════════════════════════════════

TOOL_DESC_SWOT_BUILDER = """\
【SWOT-анализ конкурента】
Строит SWOT-матрицу для указанного конкурента на основе данных графа.

Процесс:
1. Ищет все факты о конкуренте в графе знаний
2. Классифицирует факты: позитивные → Strengths, негативные → Weaknesses
3. Внешние факторы → Opportunities / Threats
4. Возвращает структурированный SWOT с цитатами из источников

【Параметры】
- competitor_name: название компании-конкурента

【Возвращает】
- Strengths, Weaknesses, Opportunities, Threats с цитатами
- Исходные факты из графа"""

TOOL_DESC_MARKET_VOLUME = """\
【Оценка ёмкости рынка】
Ищет числовые данные о рынке: объёмы, выручка, доли, рост.

Процесс:
1. Ищет в графе упоминания объёмов рынка, выручки, долей
2. Приоритет: данные с тегом [source:vc] (бизнес-аналитика)
3. Извлекает числовые значения и контекст
4. Сводит в единую оценку

【Параметры】
- query: запрос о рынке (например "объём рынка мобильного банкинга")

【Возвращает】
- Числовые упоминания с контекстом
- Факты о рынке
- Сводную оценку"""

TOOL_DESC_SEGMENTATION = """\
【Сегментация целевой аудитории】
Группирует пользователей по их проблемам и болям.

Процесс:
1. Ищет боли и жалобы пользователей в графе
2. Приоритет: данные с тегом [source:pikabu] (пользовательские обсуждения)
3. Группирует по типам проблем
4. Для каждого сегмента: описание, размер, барьеры, цитаты

【Параметры】
- query: запрос о целевой аудитории (например "проблемы пользователей банковских приложений")

【Возвращает】
- Матрицу сегментов с описаниями
- Исходные боли/жалобы с цитатами"""


class MarketToolsService:
    """
    Сервис маркетинговых инструментов.
    Работает поверх ZepToolsService, добавляя бизнес-логику.
    """

    def __init__(
        self,
        graph_id: str,
        simulation_requirement: str,
        zep_tools: Optional[ZepToolsService] = None,
        llm_client: Optional[LLMClient] = None,
    ):
        self.graph_id = graph_id
        self.simulation_requirement = simulation_requirement
        self.zep_tools = zep_tools or ZepToolsService()
        self.llm = llm_client or LLMClient()

    def swot_builder(self, competitor_name: str) -> SwotResult:
        """
        Строит SWOT-анализ для конкурента.
        Ищет факты в графе и классифицирует через LLM.
        """
        logger.info(f"SWOT builder: {competitor_name}")

        # Поиск фактов о конкуренте
        search = self.zep_tools.search_graph(
            graph_id=self.graph_id,
            query=f"{competitor_name} преимущества недостатки конкуренция продукт",
            limit=30,
            scope="edges",
        )

        facts = search.facts[:25]
        if not facts:
            return SwotResult(
                competitor_name=competitor_name,
                source_facts=[],
                strengths=["Недостаточно данных в графе"],
            )

        # Классификация через LLM
        facts_text = "\n".join(f"{i+1}. {f}" for i, f in enumerate(facts))
        classification = self.llm.chat(
            messages=[
                {"role": "system", "content": (
                    "Вы аналитик. Классифицируйте факты о компании по SWOT-категориям. "
                    "Выведите JSON: {\"S\": [...], \"W\": [...], \"O\": [...], \"T\": [...]}\n"
                    "Каждый элемент — краткая формулировка на русском (1-2 предложения). "
                    "Если факт не относится ни к одной категории — пропустите."
                )},
                {"role": "user", "content": (
                    f"Компания: {competitor_name}\n\nФакты:\n{facts_text}"
                )},
            ],
            temperature=0.1,
            max_tokens=2000,
            response_format={"type": "json_object"},
        )

        try:
            import json
            swot = json.loads(classification)
        except Exception:
            swot = {"S": [], "W": [], "O": [], "T": []}

        return SwotResult(
            competitor_name=competitor_name,
            strengths=swot.get("S", [])[:8],
            weaknesses=swot.get("W", [])[:8],
            opportunities=swot.get("O", [])[:6],
            threats=swot.get("T", [])[:6],
            source_facts=facts,
        )

    def market_volume_calculator(self, query: str) -> MarketVolumeResult:
        """
        Ищет числовые данные о рынке в графе.
        Приоритет: данные с тегом [source:vc].
        """
        logger.info(f"Market volume: {query}")

        # Поиск с акцентом на бизнес-данные
        search = self.zep_tools.search_graph(
            graph_id=self.graph_id,
            query=f"{query} объём рынка выручка доля рост миллиард миллион процент",
            limit=30,
            scope="edges",
        )

        facts = search.facts[:25]

        # Извлечение числовых упоминаний
        numeric_mentions = []
        number_pattern = re.compile(
            r'(\d[\d\s,.]*\d*)\s*'
            r'(млрд|млн|тыс|%|процент|руб|долл|\$|€|₽|billion|million|thousand)',
            re.IGNORECASE,
        )

        for fact in facts:
            matches = number_pattern.findall(fact)
            for value, unit in matches:
                numeric_mentions.append({
                    "value": f"{value.strip()} {unit}",
                    "context": fact[:200],
                })

        # Фильтруем факты с VC.ru приоритетом
        vc_facts = [f for f in facts if "[source:vc]" in f.lower() or "vc.ru" in f.lower()]
        other_facts = [f for f in facts if f not in vc_facts]
        market_facts = vc_facts + other_facts

        return MarketVolumeResult(
            query=query,
            numeric_mentions=numeric_mentions[:15],
            market_facts=market_facts[:20],
            summary=f"Найдено {len(numeric_mentions)} числовых упоминаний в {len(facts)} фактах",
        )

    def segmentation_matrix(self, query: str) -> SegmentationResult:
        """
        Группирует пользователей по проблемам/болям.
        Приоритет: данные с тегом [source:pikabu].
        """
        logger.info(f"Segmentation: {query}")

        # Поиск болей и жалоб
        search = self.zep_tools.search_graph(
            graph_id=self.graph_id,
            query=f"{query} проблема боль жалоба неудобство баг ошибка дорого плохо",
            limit=30,
            scope="edges",
        )

        facts = search.facts[:25]
        if not facts:
            return SegmentationResult(
                query=query,
                pain_facts=[],
                segments=[{"name": "Недостаточно данных", "description": "Нет данных о болях пользователей", "mentions": 0}],
            )

        # Группировка через LLM
        facts_text = "\n".join(f"{i+1}. {f}" for i, f in enumerate(facts))
        segmentation = self.llm.chat(
            messages=[
                {"role": "system", "content": (
                    "Вы маркетолог-аналитик. Сгруппируйте жалобы/боли пользователей в сегменты ЦА. "
                    "Выведите JSON: {\"segments\": [{\"name\": \"...\", \"description\": \"...\", "
                    "\"mentions\": N, \"barriers\": [\"...\"], \"quotes\": [\"...\"]}]}\n"
                    "3-6 сегментов. mentions — примерное количество упоминаний. "
                    "quotes — 1-3 характерные цитаты из фактов. Всё на русском."
                )},
                {"role": "user", "content": (
                    f"Тема: {query}\n\nФакты (боли/жалобы пользователей):\n{facts_text}"
                )},
            ],
            temperature=0.1,
            max_tokens=2000,
            response_format={"type": "json_object"},
        )

        try:
            import json
            result = json.loads(segmentation)
            segments = result.get("segments", [])
        except Exception:
            segments = []

        # Pikabu-приоритет
        pikabu_facts = [f for f in facts if "[source:pikabu]" in f.lower() or "pikabu" in f.lower()]
        other_facts = [f for f in facts if f not in pikabu_facts]
        pain_facts = pikabu_facts + other_facts

        return SegmentationResult(
            query=query,
            segments=segments[:6],
            pain_facts=pain_facts[:20],
        )
