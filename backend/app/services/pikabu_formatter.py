"""
Форматтер данных из Topic Analyzer в текст для MiroFish.

Принимает JSON с постами и комментариями от Topic Analyzer
и форматирует в аналитический текст с тегами источников,
пригодный для построения графа знаний и маркетинговых исследований.

Тегирование: каждый чанк помечается [source:pikabu], [source:habr] или [source:vc],
что позволяет ReportAgent фильтровать данные по источнику.
"""

from typing import Dict, Any, List
from datetime import datetime

from ..utils.logger import get_logger

logger = get_logger('mirofish.pikabu_formatter')

# Маппинг source → тег для Zep
SOURCE_TAGS = {
    "pikabu": "pikabu",
    "habr": "habr",
    "vcru": "vc",
    "vc": "vc",
}


class PikabuFormatter:
    """
    Форматирует спарсенные данные из Pikabu/Habr/VC.ru
    в текстовый документ с тегами источников для пайплайна MiroFish.
    """

    @staticmethod
    def format_posts_to_text(
        posts: List[Dict[str, Any]],
        topic_name: str = "",
        source: str = "pikabu",
        simulation_requirement: str = "",
    ) -> str:
        """
        Конвертирует список постов с комментариями в структурированный текст.
        Каждый пост помечается тегом источника [source:xxx].
        """
        if not posts:
            return ""

        parts = []
        source_tag = SOURCE_TAGS.get(source, source)

        # Заголовок документа
        source_label = PikabuFormatter._source_label(source)
        header = f"[source:{source_tag}] # Данные: {topic_name or 'Без темы'} ({source_label})\n"
        header += f"Количество постов: {len(posts)}\n"

        total_comments = sum(len(p.get("comments", [])) for p in posts)
        header += f"Количество комментариев: {total_comments}\n"

        dates = []
        for p in posts:
            pub = p.get("published_at", "")
            if pub:
                try:
                    dates.append(datetime.fromisoformat(pub.replace("Z", "+00:00")))
                except (ValueError, TypeError):
                    pass
        if dates:
            dates.sort()
            header += f"Период: {dates[0].strftime('%d.%m.%Y')} — {dates[-1].strftime('%d.%m.%Y')}\n"

        parts.append(header)

        sorted_posts = sorted(posts, key=lambda p: p.get("rating", 0), reverse=True)

        for i, post in enumerate(sorted_posts, 1):
            post_text = PikabuFormatter._format_single_post(post, i, source_tag)
            if post_text:
                parts.append(post_text)

        result = "\n\n".join(parts)
        logger.info(
            f"Отформатировано [{source_tag}]: {len(posts)} постов, "
            f"{total_comments} комментариев, {len(result)} символов"
        )
        return result

    @staticmethod
    def format_multi_source(
        topics_data: List[Dict[str, Any]],
        brief: str = "",
    ) -> str:
        """
        Форматирует данные из нескольких тем/источников в единый документ.

        Args:
            topics_data: Список словарей, каждый содержит:
                {
                    "topic_name": "Финтех",
                    "source": "vcru",
                    "posts": [...]
                }
            brief: Бриф клиента (описание задачи)

        Returns:
            Единый текст со всеми данными, тегированный по источникам
        """
        if not topics_data:
            return ""

        parts = []

        # Заголовок с брифом
        if brief:
            parts.append(f"# Бриф исследования\n{brief}\n")

        # Статистика
        total_posts = 0
        total_comments = 0
        sources_used = set()
        for td in topics_data:
            posts = td.get("posts", [])
            total_posts += len(posts)
            total_comments += sum(len(p.get("comments", [])) for p in posts)
            sources_used.add(td.get("source", "unknown"))

        parts.append(
            f"# Обзор данных\n"
            f"Источники: {', '.join(PikabuFormatter._source_label(s) for s in sources_used)}\n"
            f"Всего постов: {total_posts}\n"
            f"Всего комментариев: {total_comments}\n"
            f"Тем выбрано: {len(topics_data)}\n"
        )

        # Данные по каждой теме
        for td in topics_data:
            topic_text = PikabuFormatter.format_posts_to_text(
                posts=td.get("posts", []),
                topic_name=td.get("topic_name", ""),
                source=td.get("source", "pikabu"),
            )
            if topic_text:
                parts.append(topic_text)

        result = "\n\n---\n\n".join(parts)
        logger.info(
            f"Мультиисточник: {len(topics_data)} тем, {total_posts} постов, "
            f"{total_comments} комментариев, {len(result)} символов"
        )
        return result

    @staticmethod
    def _format_single_post(post: Dict[str, Any], index: int, source_tag: str = "") -> str:
        """Форматирует один пост с комментариями и тегом источника."""
        title = post.get("title", "Без заголовка")
        body = (post.get("body") or "").strip()
        rating = post.get("rating", 0)
        url = post.get("url", "")
        published = post.get("published_at", "")
        comments = post.get("comments", [])

        tag = f"[source:{source_tag}] " if source_tag else ""
        lines = [f"{tag}## Пост {index}: {title}"]
        if published:
            lines.append(f"Дата: {published}")
        lines.append(f"Рейтинг: {rating} | Комментариев: {len(comments)}")
        if url:
            lines.append(f"Ссылка: {url}")

        if body:
            truncated = body[:3000]
            if len(body) > 3000:
                truncated += "..."
            lines.append(f"\n{truncated}")

        if comments:
            sorted_comments = sorted(
                comments,
                key=lambda c: c.get("rating", 0),
                reverse=True,
            )
            top_comments = sorted_comments[:15]
            lines.append(f"\n### Комментарии (топ {len(top_comments)} из {len(comments)}):")
            for c in top_comments:
                c_body = (c.get("body") or "").strip()
                if not c_body:
                    continue
                c_rating = c.get("rating", 0)
                if len(c_body) > 500:
                    c_body = c_body[:500] + "..."
                lines.append(f"- [{c_rating:+d}] {c_body}")

        return "\n".join(lines)

    @staticmethod
    def _source_label(source: str) -> str:
        """Человекочитаемое название источника."""
        labels = {
            "pikabu": "Pikabu",
            "habr": "Habr",
            "vcru": "VC.ru",
            "vc": "VC.ru",
        }
        return labels.get(source, source)

    @staticmethod
    def estimate_text_size(posts: List[Dict[str, Any]]) -> Dict[str, int]:
        """Оценивает размер данных перед форматированием."""
        total_posts = len(posts)
        total_comments = sum(len(p.get("comments", [])) for p in posts)
        estimated_chars = total_posts * 200 + total_comments * 100
        return {
            "posts": total_posts,
            "comments": total_comments,
            "estimated_chars": estimated_chars,
        }

    @staticmethod
    def estimate_multi_source_size(topics_data: List[Dict[str, Any]]) -> Dict[str, int]:
        """Оценивает размер данных из нескольких источников."""
        total_posts = 0
        total_comments = 0
        for td in topics_data:
            posts = td.get("posts", [])
            total_posts += len(posts)
            total_comments += sum(len(p.get("comments", [])) for p in posts)
        return {
            "topics": len(topics_data),
            "posts": total_posts,
            "comments": total_comments,
            "estimated_chars": total_posts * 200 + total_comments * 100,
        }
