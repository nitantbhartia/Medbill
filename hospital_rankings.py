"""State rankings of hospitals by how far list prices run above Medicare."""

from __future__ import annotations

import statistics

import config
from db import get_db
from hospital_seo import _display_city, _display_name, state_display_name

_RANKED_SQL = """
    SELECT h.name, h.facility_id, h.city, h.state, h.ownership, h.slug, h.state_slug, h.city_slug,
           m.avg_markup_vs_medicare AS markup, m.billing_grade AS grade,
           m.procedures_compared AS procedures, m.computed_at
    FROM hospitals h
    JOIN billing_metrics m ON m.facility_id = h.facility_id
    WHERE h.state_slug = ? AND m.avg_markup_vs_medicare > 0 AND m.procedures_compared >= ?
    ORDER BY m.avg_markup_vs_medicare DESC, h.name
"""


def _ranked_hospitals(state_slug: str) -> list[dict]:
    with get_db() as db:
        rows = db.execute(_RANKED_SQL, (state_slug, config.RANKING_MIN_PROCEDURES)).fetchall()
    hospitals = []
    for row in rows:
        item = dict(row)
        item["name"] = _display_name(item["name"], item["facility_id"])
        item["city"] = _display_city(item["city"])
        hospitals.append(item)
    return hospitals


def get_state_ranking(state_slug: str) -> dict | None:
    """Most and least expensive hospitals in a state, or None if too few are ranked."""
    hospitals = _ranked_hospitals(state_slug)
    if len(hospitals) < config.RANKING_MIN_HOSPITALS:
        return None
    for rank, hospital in enumerate(hospitals, start=1):
        hospital["rank"] = rank
    bottom = hospitals[-config.RANKING_BOTTOM_COUNT:] if len(hospitals) > config.RANKING_TOP_COUNT else []
    as_of = max(str(h["computed_at"] or "") for h in hospitals)[:10] or None
    return {
        "state_name": state_display_name(hospitals[0]["state"]),
        "state_slug": state_slug,
        "ranked_count": len(hospitals),
        "median_markup": statistics.median(h["markup"] for h in hospitals),
        "most_expensive": hospitals[: config.RANKING_TOP_COUNT],
        "least_expensive": list(reversed(bottom)),
        "as_of": as_of,
    }


def get_ranked_state_slugs() -> list[str]:
    with get_db() as db:
        rows = db.execute(
            """
            SELECT h.state_slug
            FROM hospitals h
            JOIN billing_metrics m ON m.facility_id = h.facility_id
            WHERE m.avg_markup_vs_medicare > 0 AND m.procedures_compared >= ?
            GROUP BY h.state_slug
            HAVING COUNT(*) >= ?
            ORDER BY h.state_slug
            """,
            (config.RANKING_MIN_PROCEDURES, config.RANKING_MIN_HOSPITALS),
        ).fetchall()
    return [row["state_slug"] for row in rows]


def ranking_title(ranking: dict) -> str:
    state = ranking["state_name"]
    year = (ranking["as_of"] or "")[:4]
    options = [f"Most Expensive Hospitals in {state} ({year})"] if year else []
    options.append(f"Most Expensive Hospitals in {state}")
    for title in options:
        if len(title) <= config.SEO_TITLE_MAX_CHARS:
            return title
    return options[-1]


def ranking_description(ranking: dict) -> str:
    top = ranking["most_expensive"][0]
    text = (
        f"{ranking['ranked_count']} {ranking['state_name']} hospitals ranked by how far list prices run above Medicare. "
        f"Highest: {top['name']} at {top['markup']:.1f}x. State median: {ranking['median_markup']:.1f}x."
    )
    if len(text) <= config.SEO_META_MAX_CHARS:
        return text
    return text[: text.rfind(". Highest") + 1]
