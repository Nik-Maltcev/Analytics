"""
Форматтер данных из PIKABU Topic Analyzer в текст для MiroFish.

Принимает JSON с постами и комментариями от PIKABU парсера
и форматирует в аналитический текст, пригодный для построения
графа знаний и симуляции.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime

from ..utils.logger import get_logger

logger = get_logger('mirofish.pikabu_formatter')


class PikabuFormatter:
    """
    Форматирует спарсенные данные из PIKABU/Habr/VC.ru
    в текстовый документ для пайплайна MiroFish.
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

        Args:
            posts: Список постов в формате PIKABU API:
                [{
                    "title": "...",
                    "body": "...",
                    "published_at": "2025-01-15T12:00:00",
                    "rating": 150,
                    "comments_count": 42,
                    "url": "https://pikabu.ru/...",
                    "comments": [
                        {"body": "...", "published_at": "...", "rating": 5},
                        ...
                    ]
                }]
            topic_name: Название темы/сообщества
            source: Источник данных (pikabu, habr, vcru, pikabu+habr, ...)
            simulation_requirement: Описание задачи симуляции

        Returns:
            Форматированный текст для MiroFish
        """
        if not posts:
            return ""

        parts = []

        # Заголовок документа
        source_label = PikabuFormatter._source_label(source)
        header = f"# Анализ контента: {topic_name or 'Без темы'}\n"
        header += f"Источник: {source_label}\n"
        header += f"Количество постов: {len(posts)}\n"

        total_comments = sum(len(p.get("comments", [])) for p in posts)
        header += f"Количество комментариев: {total_comments}\n"

        # Диапазон дат
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

        # Сортируем посты по рейтингу (самые обсуждаемые первыми)
        sorted_posts = sorted(posts, key=lambda p: p.get("rating", 0), reverse=True)

        for i, post in enumerate(sorted_posts, 1):
            post_text = PikabuFormatter._format_single_post(post, i)
            if post_text:
                parts.append(post_text)

        result = "\n\n".join(parts)
        logger.info(
            f"Отформатировано: {len(posts)} постов, {total_comments} комментариев, "
            f"{len(result)} символов"
        )
        return result

    @staticmethod
    def _format_single_post(post: Dict[str, Any], index: int) -> str:
        """Форматирует один пост с комментариями."""
        title = post.get("title", "Без заголовка")
        body = (post.get("body") or "").strip()
        rating = post.get("rating", 0)
        url = post.get("url", "")
        published = post.get("published_at", "")
        comments = post.get("comments", [])

        lines = [f"## Пост {index}: {title}"]
        if published:
            lines.append(f"Дата: {published}")
        lines.append(f"Рейтинг: {rating} | Комментариев: {len(comments)}")
        if url:
            lines.append(f"Ссылка: {url}")

        if body:
            # Ограничиваем тело поста разумным размером
            truncated = body[:3000]
            if len(body) > 3000:
                truncated += "..."
            lines.append(f"\n{truncated}")

        # Комментарии — берём топ по рейтингу
        if comments:
            sorted_comments = sorted(
                comments,
                key=lambda c: c.get("rating", 0),
                reverse=True,
            )
            # Берём до 15 самых рейтинговых комментариев
            top_comments = sorted_comments[:15]
            lines.append(f"\n### Комментарии (топ {len(top_comments)} из {len(comments)}):")
            for c in top_comments:
                c_body = (c.get("body") or "").strip()
                if not c_body:
                    continue
                c_rating = c.get("rating", 0)
                # Ограничиваем длину комментария
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
            "pikabu,habr": "Pikabu + Habr",
            "pikabu,habr,vcru": "Pikabu + Habr + VC.ru",
            "both": "Pikabu + Habr",
            "all": "Pikabu + Habr + VC.ru",
        }
        return labels.get(source, source)

    @staticmethod
    def estimate_text_size(posts: List[Dict[str, Any]]) -> Dict[str, int]:
        """Оценивает размер данных перед форматированием."""
        total_posts = len(posts)
        total_comments = sum(len(p.get("comments", [])) for p in posts)
        # Грубая оценка: ~200 символов на пост + ~100 на комментарий
        estimated_chars = total_posts * 200 + total_comments * 100
        return {
            "posts": total_posts,
            "comments": total_comments,
            "estimated_chars": estimated_chars,
        }
