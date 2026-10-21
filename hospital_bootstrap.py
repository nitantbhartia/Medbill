"""Production bootstrap for hospital directory/pricing data."""

from __future__ import annotations

import json
import logging
import os
import re
import urllib.parse
import urllib.request

import config
from cms_loader import download_cms_2026, load_transformed_cms_2026, transform_cms_2026
from db import get_db
from hospital_etl import load_cms_general, load_medicare_rates
from hospital_seo import (
    generate_and_save_hospital_content,
    get_state_index_stats,
    log_refresh,
    recompute_benchmarks,
    recompute_billing_metrics,
    upsert_hospital_row,
)
from scripts.load_pricing_from_dolthub import load_prices_for_matches, match_hospitals


log = logging.getLogger(__name__)

API_BASE = "https://www.dolthub.com/api/v1alpha1/dolthub/hospital-price-transparency/master"
# Bump this to rerun the full bootstrap on the next deploy.
BOOTSTRAP_SOURCE = "hospital_bootstrap_v2"


def _api_query(sql: str) -> list[dict]:
    url = f"{API_BASE}?{urllib.parse.urlencode({'q': sql})}"
    with urllib.request.urlopen(url, timeout=90) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    return payload.get("rows", [])


def _slug(value: str | None) -> str:
    txt = (value or "").strip().lower()
    txt = re.sub(r"[^a-z0-9]+", "-", txt)
    return txt.strip("-")


def _seed_hospitals_from_dolthub() -> int:
    created = 0
    offset = 0
    page = 500
    while True:
        rows = _api_query(
            f"SELECT npi_number, name, city, state, street_address, zip_code FROM hospitals LIMIT {page} OFFSET {offset}"
        )
        if not rows:
            break
        for row in rows:
            npi = row.get("npi_number")
            name = row.get("name")
            city = row.get("city")
            state = row.get("state")
            if not (npi and name and city and state):
                continue
            city = str(city).strip()
            state = str(state).strip().upper()
            name = str(name).strip()
            upsert_hospital_row(
                {
                    "facility_id": str(npi).strip(),
                    "name": name,
                    "address": row.get("street_address"),
                    "city": city,
                    "state": state,
                    "zip": str(row.get("zip_code") or "").strip()[:10],
                    "slug": _slug(f"{name}-{city}"),
                    "state_slug": _slug(state),
                    "city_slug": _slug(city),
                }
            )
            created += 1
        offset += page
        if len(rows) < page:
            break
    return created


def _bootstrap_done() -> bool:
    with get_db() as db:
        row = db.execute(
            "SELECT 1 FROM data_refresh_log WHERE source = ? AND status = 'success' LIMIT 1",
            (BOOTSTRAP_SOURCE,),
        ).fetchone()
    return row is not None


def _is_cms_facility_id(facility_id: str) -> bool:
    # CMS ids are 6-character CCNs; DoltHub-seeded rows use 10-digit NPIs.
    return len(facility_id) < 10


def _exact_dolthub_duplicates() -> list[str]:
    """DoltHub-seeded hospitals with the same name, city and state as a CMS hospital."""
    with get_db() as db:
        rows = db.execute(
            """
            SELECT DISTINCT d.facility_id
            FROM hospitals d
            JOIN hospitals c
              ON UPPER(c.name) = UPPER(d.name) AND UPPER(c.city) = UPPER(d.city) AND c.state = d.state
            WHERE LENGTH(d.facility_id) = 10 AND d.facility_id NOT GLOB '*[^0-9]*'
              AND LENGTH(c.facility_id) < 10
            """
        ).fetchall()
    return [row["facility_id"] for row in rows]


def _matched_dolthub_duplicates(matches: dict[str, dict]) -> list[str]:
    """DoltHub-seeded hospitals whose NPI a CMS hospital was matched to, even under a different name."""
    npis = {m["npi"] for fid, m in matches.items() if _is_cms_facility_id(fid)}
    with get_db() as db:
        existing = {row["facility_id"] for row in db.execute("SELECT facility_id FROM hospitals")}
    return sorted(npis & existing)


def _delete_hospitals(facility_ids: list[str]) -> int:
    """Delete hospitals and every row any table holds for them."""
    with get_db() as db:
        tables = [
            row["name"]
            for row in db.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name != 'hospitals'")
            if any(col["name"] == "facility_id" for col in db.execute(f"PRAGMA table_info({row['name']})"))
        ]
        for facility_id in facility_ids:
            for table in tables:
                db.execute(f"DELETE FROM {table} WHERE facility_id = ?", (facility_id,))
            db.execute("DELETE FROM hospitals WHERE facility_id = ?", (facility_id,))
    return len(facility_ids)


def _load_cms_directory() -> int:
    """Download CMS Hospital General Information (~5,400 hospitals) and upsert it into hospitals."""
    os.makedirs(os.path.dirname(config.CMS_HOSPITAL_GENERAL_CSV_PATH), exist_ok=True)
    try:
        urllib.request.urlretrieve(config.CMS_HOSPITAL_GENERAL_CSV_URL, config.CMS_HOSPITAL_GENERAL_CSV_PATH)
    except OSError as exc:
        log.error("CMS hospital directory download failed from %s: %s", config.CMS_HOSPITAL_GENERAL_CSV_URL, exc)
        return 0
    return load_cms_general(config.CMS_HOSPITAL_GENERAL_CSV_PATH)


def ensure_hospital_data_bootstrap() -> None:
    if _bootstrap_done():
        return

    log.warning("Hospital bootstrap %s not done, running it.", BOOTSTRAP_SOURCE)
    removed = _delete_hospitals(_exact_dolthub_duplicates())
    log.warning("Removed %s DoltHub hospitals with the same name as a CMS hospital", removed)
    loaded_cms = _load_cms_directory()
    log.warning("Loaded %s hospitals from CMS directory", loaded_cms)
    if loaded_cms == 0:
        seeded = _seed_hospitals_from_dolthub()
        log.warning("CMS directory unavailable, seeded %s hospitals from DoltHub instead", seeded)

    try:
        download_cms_2026("data/cms/raw")
        transform_cms_2026("data/cms/raw", "data/cms/processed")
        load_transformed_cms_2026("data/cms/processed")
    except Exception as exc:
        log.warning("CMS bulk load failed during bootstrap: %s", exc)
        # Keep at least Medicare rates available where possible.
        try:
            load_medicare_rates("data/cms/processed/medicare_pfs_2026.csv", effective_year=2026)
        except Exception:
            pass

    matches, _ = match_hospitals(limit=10000)
    matched_duplicates = _matched_dolthub_duplicates(matches) if loaded_cms > 0 else []
    if matched_duplicates:
        _delete_hospitals(matched_duplicates)
        # Reload so CMS hospitals take back the plain slugs the deleted rows held.
        load_cms_general(config.CMS_HOSPITAL_GENERAL_CSV_PATH)
        log.warning("Removed %s DoltHub hospitals matched to a CMS hospital", len(matched_duplicates))
    deleted = set(matched_duplicates)
    matches = {fid: m for fid, m in matches.items() if fid not in deleted}
    loaded = load_prices_for_matches(matches, year=2026)
    recompute_benchmarks()
    recompute_billing_metrics()
    generate_and_save_hospital_content()
    if loaded_cms > 0:
        log_refresh(BOOTSTRAP_SOURCE, loaded_cms, "success")
    log.warning(
        "Hospital bootstrap complete. states=%s matched=%s loaded_facilities=%s rows=%s",
        len(get_state_index_stats()),
        len(matches),
        loaded.get("facilities", 0),
        loaded.get("rows", 0),
    )
