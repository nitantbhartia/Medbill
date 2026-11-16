"""Hospital billing grades as public data: CSV rows, the SVG badge and the embed snippet."""

from __future__ import annotations

import csv
import html
import io
from collections.abc import Iterator

import config
from db import get_db
from hospital_seo import MAP_GRADE_COLORS, _display_city, _display_name, _truncate_name

CSV_HEADER = (
    "facility_id", "name", "city", "state", "ownership",
    "billing_grade", "avg_markup_vs_medicare", "procedures_compared", "profile_url",
)

_GRADED_SQL = """
    SELECT h.facility_id, h.name, h.city, h.state, h.ownership, h.slug, h.state_slug, h.city_slug,
           m.billing_grade, m.avg_markup_vs_medicare, m.procedures_compared
    FROM hospitals h
    JOIN billing_metrics m ON m.facility_id = h.facility_id
    WHERE m.billing_grade IN ('A', 'B', 'C', 'D', 'F')
"""


def profile_url(hospital: dict) -> str:
    return (
        f"{config.APP_URL.rstrip('/')}/hospitals/"
        f"{hospital['state_slug']}/{hospital['city_slug']}/{hospital['slug']}/"
    )


def _graded_row_to_dict(row) -> dict:
    hospital = dict(row)
    hospital["name"] = _display_name(hospital["name"], hospital["facility_id"])
    hospital["city"] = _display_city(hospital["city"])
    hospital["profile_url"] = profile_url(hospital)
    return hospital


def get_graded_hospitals() -> list[dict]:
    with get_db() as db:
        rows = db.execute(_GRADED_SQL + " ORDER BY h.state, h.name, h.facility_id").fetchall()
    return [_graded_row_to_dict(row) for row in rows]


def get_graded_hospital(facility_id: str) -> dict | None:
    with get_db() as db:
        row = db.execute(_GRADED_SQL + " AND h.facility_id = ?", (facility_id,)).fetchone()
    return _graded_row_to_dict(row) if row else None


def _csv_fields(hospital: dict) -> list:
    return [
        hospital["facility_id"],
        hospital["name"],
        hospital["city"],
        hospital["state"],
        hospital["ownership"] or "",
        hospital["billing_grade"],
        round(hospital["avg_markup_vs_medicare"], config.CSV_MARKUP_DECIMALS),
        hospital["procedures_compared"],
        hospital["profile_url"],
    ]


def iter_grades_csv(hospitals: list[dict]) -> Iterator[str]:
    """Yield the CSV one line at a time so the response streams."""
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    lines = [CSV_HEADER, *(_csv_fields(hospital) for hospital in hospitals)]
    for line in lines:
        writer.writerow(line)
        yield buffer.getvalue()
        buffer.seek(0)
        buffer.truncate()


def render_badge_svg(hospital: dict) -> str:
    grade = html.escape(hospital["billing_grade"])
    color = html.escape(MAP_GRADE_COLORS[hospital["billing_grade"]])
    name = html.escape(_truncate_name(hospital["name"], config.BADGE_NAME_MAX_CHARS))
    markup = html.escape(f"{hospital['avg_markup_vs_medicare']:.{config.BADGE_MARKUP_DECIMALS}f}x")
    width, height, text_x = config.BADGE_WIDTH, config.BADGE_HEIGHT, config.BADGE_TEXT_X
    font = 'font-family="Arial, Helvetica, sans-serif"'
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="BillKarma billing grade: {grade}">'
        f"<title>BillKarma billing grade: {grade}, {name}</title>"
        f'<rect width="{width}" height="{height}" fill="#ffffff" stroke="#D1D5DB"/>'
        f'<rect width="{config.BADGE_ACCENT_WIDTH}" height="{height}" fill="{color}"/>'
        f'<text x="{text_x}" y="24" {font} font-size="13" font-weight="700" fill="#111827">'
        f"BillKarma billing grade: {grade}</text>"
        f'<text x="{text_x}" y="44" {font} font-size="12" fill="#374151">{name}</text>'
        f'<text x="{text_x}" y="62" {font} font-size="11" fill="#4B5563">'
        f"Average markup vs Medicare: {markup}</text>"
        "</svg>"
    )


def build_embed_snippet(hospital: dict) -> str | None:
    """HTML a site owner can paste to show the badge and link to the profile. None if ungraded."""
    if hospital.get("billing_grade") not in config.GRADED_LETTERS:
        return None
    link = html.escape(profile_url(hospital), quote=True)
    image = html.escape(f"{config.APP_URL.rstrip('/')}/badge/{hospital['facility_id']}.svg", quote=True)
    alt = html.escape(f"BillKarma billing grade {hospital['billing_grade']} for {hospital['name']}", quote=True)
    return (
        f'<a href="{link}" rel="noopener"><img src="{image}" alt="{alt}" '
        f'width="{config.BADGE_WIDTH}" height="{config.BADGE_HEIGHT}"></a>'
    )
