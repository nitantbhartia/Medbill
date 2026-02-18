"""Hospital SEO profile queries and URL helpers."""

from __future__ import annotations

import re
from collections import defaultdict

from db import get_db


def slugify(value: str) -> str:
    text = (value or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def state_slug_from_code(state_code: str) -> str:
    return slugify(state_code or "")


def upsert_hospital_directory_row(row: dict) -> None:
    with get_db() as db:
        db.execute(
            """
            INSERT INTO hospital_directory (
                facility_id, name, address, city, state, zip, county, phone,
                hospital_type, ownership, emergency_services, overall_rating,
                bed_count, teaching_status, system_affiliation, slug, state_slug, last_updated
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, COALESCE(?, CURRENT_DATE))
            ON CONFLICT(facility_id) DO UPDATE SET
                name=excluded.name,
                address=excluded.address,
                city=excluded.city,
                state=excluded.state,
                zip=excluded.zip,
                county=excluded.county,
                phone=excluded.phone,
                hospital_type=excluded.hospital_type,
                ownership=excluded.ownership,
                emergency_services=excluded.emergency_services,
                overall_rating=excluded.overall_rating,
                bed_count=excluded.bed_count,
                teaching_status=excluded.teaching_status,
                system_affiliation=excluded.system_affiliation,
                slug=excluded.slug,
                state_slug=excluded.state_slug,
                last_updated=excluded.last_updated
            """,
            (
                row.get("facility_id"),
                row.get("name"),
                row.get("address"),
                row.get("city"),
                row.get("state"),
                row.get("zip"),
                row.get("county"),
                row.get("phone"),
                row.get("hospital_type"),
                row.get("ownership"),
                row.get("emergency_services"),
                row.get("overall_rating"),
                row.get("bed_count"),
                row.get("teaching_status"),
                row.get("system_affiliation"),
                row.get("slug"),
                row.get("state_slug"),
                row.get("last_updated"),
            ),
        )


def get_state_hospitals(state_slug: str, limit: int = 200) -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            """
            SELECT facility_id, name, city, state, ownership, overall_rating, slug, state_slug
            FROM hospital_directory
            WHERE state_slug = ?
            ORDER BY name
            LIMIT ?
            """,
            (state_slug, limit),
        ).fetchall()
    return [dict(r) for r in rows]


def get_hospital_profile(state_slug: str, hospital_slug: str) -> dict | None:
    with get_db() as db:
        hospital = db.execute(
            """
            SELECT *
            FROM hospital_directory
            WHERE state_slug = ? AND slug = ?
            """,
            (state_slug, hospital_slug),
        ).fetchone()
        if not hospital:
            return None

        quality = db.execute(
            "SELECT * FROM hospital_quality WHERE facility_id = ?",
            (hospital["facility_id"],),
        ).fetchone()
        financials = db.execute(
            "SELECT * FROM hospital_financials WHERE facility_id = ?",
            (hospital["facility_id"],),
        ).fetchone()
        prices = db.execute(
            """
            SELECT cpt_code, description, gross_charge, cash_price, medicare_rate,
                   avg_negotiated_rate, min_negotiated_rate, max_negotiated_rate,
                   state_avg_rate, last_updated
            FROM hospital_procedure_prices
            WHERE facility_id = ?
            ORDER BY gross_charge DESC
            LIMIT 30
            """,
            (hospital["facility_id"],),
        ).fetchall()

    hospital_d = dict(hospital)
    quality_d = dict(quality) if quality else {}
    financials_d = dict(financials) if financials else {}
    prices_d = [dict(r) for r in prices]

    multipliers = []
    for row in prices_d:
        gross = row.get("gross_charge")
        medicare = row.get("medicare_rate")
        if gross and medicare and medicare > 0:
            multipliers.append(float(gross) / float(medicare))
    markup_multiple = round(sum(multipliers) / len(multipliers), 2) if multipliers else None

    issues = []
    if markup_multiple and markup_multiple >= 5:
        issues.append("High average markup vs Medicare")
    if hospital_d.get("overall_rating") in (1, 2):
        issues.append("Low CMS overall star rating")
    if financials_d.get("charity_care_pct") is not None and float(financials_d["charity_care_pct"]) < 1.0:
        issues.append("Low charity-care share")
    if not issues:
        issues.append("No major outlier detected from currently loaded public data")

    return {
        "hospital": hospital_d,
        "quality": quality_d,
        "financials": financials_d,
        "prices": prices_d,
        "markup_multiple": markup_multiple,
        "issues": issues,
    }


def get_state_index_stats() -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            """
            SELECT state_slug, state, COUNT(*) AS hospitals
            FROM hospital_directory
            GROUP BY state_slug, state
            ORDER BY hospitals DESC, state
            """
        ).fetchall()
    return [dict(r) for r in rows]


def get_hospital_sitemap_paths() -> list[str]:
    with get_db() as db:
        rows = db.execute(
            """
            SELECT state_slug, slug
            FROM hospital_directory
            WHERE state_slug IS NOT NULL AND slug IS NOT NULL
            ORDER BY state_slug, slug
            """
        ).fetchall()
    by_state = defaultdict(list)
    for row in rows:
        by_state[row["state_slug"]].append(f"/hospital/{row['state_slug']}/{row['slug']}")
    paths = ["/"]
    for state in sorted(by_state):
        paths.append(f"/hospital/{state}")
        paths.extend(by_state[state])
    return paths
