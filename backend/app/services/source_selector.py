"""
Source Selector — AI-powered selection of data sources for market research.

Loads all available sources from CSV files (Twitter accounts, Reddit subreddits,
X communities, forums, Telegram channels) into a unified catalog.

When a client provides a research brief, uses LLM to select the most relevant
sources from the catalog.

Flow:
  1. Load CSVs from Sources/ folder → normalize to unified format
  2. Client sends brief → LLM picks relevant source IDs
  3. Return selected sources to frontend for confirmation
"""

import os
import csv
import json
import hashlib
from typing import List, Dict, Any, Optional

from ..utils.llm_client import LLMClient
from ..utils.logger import get_logger
from ..config import Config

logger = get_logger('mirofish.source_selector')

# Path to Sources folder (relative to backend/app/services/)
SOURCES_DIR = os.path.join(os.path.dirname(__file__), '../../../Sources')


def _make_id(platform: str, name: str) -> str:
    """Generate a stable short ID from platform + name."""
    raw = f"{platform}:{name}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]


class SourceSelector:
    """
    Loads and manages the unified source catalog.
    Provides AI-powered source selection based on client brief.
    """

    def __init__(self):
        self._catalog: List[Dict[str, Any]] = []
        self._loaded = False

    def _ensure_loaded(self):
        """Lazy-load the catalog on first access."""
        if not self._loaded:
            self._catalog = self._load_all_sources()
            self._loaded = True
            logger.info(f"Source catalog loaded: {len(self._catalog)} sources")

    def _load_all_sources(self) -> List[Dict[str, Any]]:
        """Load all CSV files and normalize into unified format."""
        sources = []

        sources_dir = os.path.normpath(SOURCES_DIR)
        if not os.path.isdir(sources_dir):
            logger.warning(f"Sources directory not found: {sources_dir}")
            return sources

        # 1. subreddits.csv
        subreddits_path = os.path.join(sources_dir, 'subreddits.csv')
        if os.path.exists(subreddits_path):
            sources.extend(self._load_subreddits(subreddits_path))

        # 2. twibs-accounts.csv (large media/brand accounts)
        twibs_path = os.path.join(sources_dir, 'twibs-accounts.csv')
        if os.path.exists(twibs_path):
            sources.extend(self._load_twibs(twibs_path))

        # 3. twitter-accounts (1).csv (topic-based accounts: indie hackers, AI, etc.)
        topic_accounts_path = os.path.join(sources_dir, 'twitter-accounts (1).csv')
        if os.path.exists(topic_accounts_path):
            sources.extend(self._load_topic_twitter(topic_accounts_path))

        # 4. twitter-accounts.csv (X communities)
        communities_path = os.path.join(sources_dir, 'twitter-accounts.csv')
        if os.path.exists(communities_path):
            sources.extend(self._load_x_communities(communities_path))

        return sources

    def _load_subreddits(self, path: str) -> List[Dict[str, Any]]:
        """Load subreddits.csv → unified format."""
        results = []
        try:
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    name = row.get('name', '').strip()
                    if not name:
                        continue
                    topics_raw = row.get('topics', '')
                    topics = [t.strip() for t in topics_raw.split(',') if t.strip()]
                    results.append({
                        'id': _make_id('reddit', name),
                        'name': name.replace('r/', ''),
                        'display_name': name,
                        'type': 'reddit',
                        'url': row.get('url', ''),
                        'topics': topics,
                        'members': self._parse_int(row.get('members', '0')),
                        'description': row.get('description', '')[:200],
                    })
        except Exception as e:
            logger.error(f"Failed to load subreddits: {e}")
        return results

    def _load_twibs(self, path: str) -> List[Dict[str, Any]]:
        """Load twibs-accounts.csv → unified format."""
        results = []
        try:
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    handle = row.get('handle', '').strip()
                    if not handle:
                        continue
                    # Parse category into topics
                    category_raw = row.get('category', '')
                    topics = []
                    for part in category_raw.split(';'):
                        part = part.strip()
                        if '/' in part:
                            topics.append(part.split('/')[-1].strip().lower())
                        elif part:
                            topics.append(part.lower())
                    results.append({
                        'id': _make_id('twitter', handle),
                        'name': handle,
                        'display_name': row.get('name', handle),
                        'type': 'twitter',
                        'url': row.get('url', f'https://x.com/{handle}'),
                        'topics': topics,
                        'members': self._parse_int(row.get('followers', '0')),
                        'description': row.get('description', '')[:200],
                    })
        except Exception as e:
            logger.error(f"Failed to load twibs accounts: {e}")
        return results

    def _load_topic_twitter(self, path: str) -> List[Dict[str, Any]]:
        """Load twitter-accounts (1).csv → unified format."""
        results = []
        try:
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    handle = row.get('handle', '').strip()
                    if not handle:
                        continue
                    topics_raw = row.get('topic', '')
                    topics = [t.strip() for t in topics_raw.split(',') if t.strip()]
                    results.append({
                        'id': _make_id('twitter', handle),
                        'name': handle,
                        'display_name': row.get('name', handle),
                        'type': 'twitter',
                        'url': row.get('url', f'https://x.com/{handle}'),
                        'topics': topics,
                        'members': self._parse_int(row.get('followers', '0')),
                        'description': row.get('description', '')[:200],
                    })
        except Exception as e:
            logger.error(f"Failed to load topic twitter accounts: {e}")
        return results

    def _load_x_communities(self, path: str) -> List[Dict[str, Any]]:
        """Load twitter-accounts.csv (X communities) → unified format."""
        results = []
        try:
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    name = row.get('name', '').strip()
                    if not name:
                        continue
                    topics_raw = row.get('topics', '')
                    topics = [t.strip() for t in topics_raw.split(',') if t.strip()]
                    results.append({
                        'id': _make_id('x-community', name),
                        'name': name,
                        'display_name': name,
                        'type': 'twitter',
                        'url': row.get('url', ''),
                        'topics': topics,
                        'members': self._parse_int(row.get('members', '0')),
                        'description': row.get('description', '')[:200],
                    })
        except Exception as e:
            logger.error(f"Failed to load X communities: {e}")
        return results

    @staticmethod
    def _parse_int(val: str) -> int:
        """Parse integer from string, handling commas and empty values."""
        try:
            return int(str(val).replace(',', '').replace(' ', '').strip())
        except (ValueError, TypeError):
            return 0

    def get_all_sources(self) -> Dict[str, Any]:
        """Return all sources without AI filtering."""
        self._ensure_loaded()
        return {
            'sources': self._catalog,
            'recommended_ids': [],
            'total': len(self._catalog),
        }

    def select_sources(self, brief: str) -> Dict[str, Any]:
        """
        Use LLM to select relevant sources based on client brief.

        Returns dict with:
          - sources: full catalog (for browsing)
          - recommended_ids: AI-selected source IDs
          - reasoning: LLM explanation
        """
        self._ensure_loaded()

        if not self._catalog:
            return {'sources': [], 'recommended_ids': [], 'reasoning': 'No sources available'}

        # Build a compact summary of available sources for the LLM
        # Group by type and list topics
        summary_lines = []
        for src in self._catalog:
            line = f"[{src['id']}] {src['type']}:{src['name']} topics={','.join(src['topics'][:5])} members={src['members']}"
            summary_lines.append(line)

        # Limit to avoid token overflow — send top sources by members + all unique topics
        # Strategy: send all sources but truncated (ID + type + name + topics only)
        catalog_text = "\n".join(summary_lines)

        # If catalog is too large (>50K chars), truncate intelligently
        if len(catalog_text) > 50000:
            # Sort by members desc, take top 500
            sorted_sources = sorted(self._catalog, key=lambda s: s['members'], reverse=True)[:500]
            summary_lines = []
            for src in sorted_sources:
                line = f"[{src['id']}] {src['type']}:{src['name']} topics={','.join(src['topics'][:5])}"
                summary_lines.append(line)
            catalog_text = "\n".join(summary_lines)

        prompt = f"""You are a market research analyst. A client wants to conduct research with this brief:

"{brief}"

Below is a catalog of available data sources (Twitter accounts, Reddit subreddits, X communities).
Each line: [ID] type:name topics=...

Select 10-25 most relevant sources for this research. Consider:
- Topic relevance to the brief
- Source authority (prefer larger communities for broad topics)
- Diversity of perspectives (mix of platforms and viewpoints)
- Both direct matches and adjacent/complementary sources

CATALOG:
{catalog_text}

Return a JSON object:
{{
  "selected_ids": ["id1", "id2", ...],
  "reasoning": "Brief explanation of selection logic (1-2 sentences)"
}}

Return ONLY valid JSON, no markdown."""

        llm = LLMClient()
        try:
            response = llm.chat(
                messages=[
                    {"role": "system", "content": "You are a market research source selection AI. Return only valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000,
            )

            # Parse LLM response
            # Strip markdown code fences if present
            cleaned = response.strip()
            if cleaned.startswith('```'):
                cleaned = cleaned.split('\n', 1)[-1]
                if cleaned.endswith('```'):
                    cleaned = cleaned[:-3]
                cleaned = cleaned.strip()

            result = json.loads(cleaned)
            selected_ids = result.get('selected_ids', [])
            reasoning = result.get('reasoning', '')

            logger.info(f"AI selected {len(selected_ids)} sources for brief: {brief[:60]}...")

            return {
                'sources': self._catalog,
                'recommended_ids': selected_ids,
                'reasoning': reasoning,
                'total': len(self._catalog),
            }

        except Exception as e:
            logger.error(f"AI source selection failed: {e}")
            # Fallback: return top sources by member count
            top_sources = sorted(self._catalog, key=lambda s: s['members'], reverse=True)[:15]
            return {
                'sources': self._catalog,
                'recommended_ids': [s['id'] for s in top_sources],
                'reasoning': f'AI selection failed ({str(e)[:50]}), showing top sources by popularity',
                'total': len(self._catalog),
            }
