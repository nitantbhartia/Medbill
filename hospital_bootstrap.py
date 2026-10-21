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
    recompute_benchmarks,
    recompute_billing_metrics,
    upsert_hospital_row,
)
from scripts.load_pricing_from_dolthub import load_prices_for_matches, match_hospitals


log = logging.getLogger(__name__)

API_BASE = "https://www.dolthub.com/api/v1alpha1/dolthub/hospital-price-transparency/master"


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


def _cms_directory_loaded() -> bool:
    with get_db() as db:
        row = db.execute(
            "SELECT 1 FROM data_refresh_log WHERE source = 'cms_general' AND status = 'success' LIMIT 1"
        ).fetchone()
    return row is not None


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
    if _cms_directory_loaded():
        return

    log.warning("CMS hospital directory not loaded, running bootstrap load.")
    loaded_cms = _load_cms_directory()
    log.warning("Loaded %s hospitals from CMS directory", loaded_cms)
    seeded = _seed_hospitals_from_dolthub()
    log.warning("Seeded/updated %s hospitals from DoltHub", seeded)

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
    loaded = load_prices_for_matches(matches, year=2026)
    recompute_benchmarks()
    recompute_billing_metrics()
    generate_and_save_hospital_content()
    log.warning(
        "Hospital bootstrap complete. states=%s matched=%s loaded_facilities=%s rows=%s",
        len(get_state_index_stats()),
        len(matches),
        loaded.get("facilities", 0),
        loaded.get("rows", 0),
    )
