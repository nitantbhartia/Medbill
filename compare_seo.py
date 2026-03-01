"""Auto-generated hospital comparison SEO pages with human-readable slugs."""

from __future__ import annotations

from db import get_db
from hospital_seo import slugify, _display_name


def resolve_comparison_slugs(slug_a: str, slug_b: str) -> tuple[str, str] | None:
    """Resolve human-readable hospital slugs to facility IDs.

    Returns (facility_id_a, facility_id_b) or None if either slug is not found.
    """
    fid_a = _slug_to_facility_id(slug_a)
    fid_b = _slug_to_facility_id(slug_b)
    if not fid_a or not fid_b:
        return None
    return (fid_a, fid_b)


def _slug_to_facility_id(slug: str) -> str | None:
    """Look up a facility_id by its URL slug."""
    with get_db() as db:
        row = db.execute(
            "SELECT facility_id FROM hospitals WHERE slug = ? LIMIT 1",
            (slug,),
        ).fetchone()
        if row:
            return str(row["facility_id"])
        row = db.execute(
            "SELECT facility_id FROM facilities WHERE slug = ? LIMIT 1",
            (slug,),
        ).fetchone()
        if row:
            return str(row["facility_id"])
    return None


def get_popular_comparisons(limit: int = 50) -> list[dict]:
    """Return popular hospital pairs for auto-generated comparison pages.

    Picks hospitals with billing grades that are in the same city/state
    so comparisons are geographically relevant.
    """
    with get_db() as db:
        rows = db.execute(
            """
            SELECT
                a.facility_id AS fid_a, a.name AS name_a, a.slug AS slug_a,
                b.facility_id AS fid_b, b.name AS name_b, b.slug AS slug_b,
                a.city, a.state,
                ma.billing_grade AS grade_a, mb.billing_grade AS grade_b,
                ma.avg_markup_vs_medicare AS markup_a, mb.avg_markup_vs_medicare AS markup_b
            FROM hospitals a
            JOIN hospitals b ON b.city = a.city AND b.state = a.state AND b.facility_id > a.facility_id
            JOIN billing_metrics ma ON ma.facility_id = a.facility_id
            JOIN billing_metrics mb ON mb.facility_id = b.facility_id
            WHERE ma.billing_grade IS NOT NULL
              AND mb.billing_grade IS NOT NULL
              AND a.slug IS NOT NULL AND a.slug != ''
              AND b.slug IS NOT NULL AND b.slug != ''
            ORDER BY
                ABS(
                    CASE ma.billing_grade
                        WHEN 'A' THEN 1 WHEN 'B' THEN 2 WHEN 'C' THEN 3
                        WHEN 'D' THEN 4 WHEN 'F' THEN 5 ELSE 3
                    END
                    -
                    CASE mb.billing_grade
                        WHEN 'A' THEN 1 WHEN 'B' THEN 2 WHEN 'C' THEN 3
                        WHEN 'D' THEN 4 WHEN 'F' THEN 5 ELSE 3
                    END
                ) DESC,
                a.city ASC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    return [dict(r) for r in rows]


def get_comparison_sitemap_paths() -> list[str]:
    """Return URL paths for all auto-generated comparison pages."""
    pairs = get_popular_comparisons(limit=100)
    paths = []
    for pair in pairs:
        slug_a = pair.get("slug_a", "")
        slug_b = pair.get("slug_b", "")
        if slug_a and slug_b:
            paths.append(f"/compare/{slug_a}-vs-{slug_b}/")
    return paths
