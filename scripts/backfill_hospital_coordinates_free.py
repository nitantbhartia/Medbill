"""Backfill hospital lat/lon using free geocoders.

Primary source: US Census Geocoder (free).
Fallback: Nominatim (OpenStreetMap), optional and throttled.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus
from urllib.request import Request, urlopen

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import config
import db
from db import get_db
from hospital_seo import log_refresh

CENSUS_ENDPOINT = (
    "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress"
    "?address={address}&benchmark=Public_AR_Current&format=json"
)
NOMINATIM_ENDPOINT = (
    "https://nominatim.openstreetmap.org/search"
    "?q={address}&format=jsonv2&limit=1&countrycodes=us"
)
DEFAULT_CACHE_PATH = Path("data/hospitals/geocode_cache.json")


def _load_cache(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except Exception:
        return {}


def _save_cache(path: Path, cache: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, indent=2, sort_keys=True))


def _full_address(row: dict) -> str:
    parts = [row.get("address"), row.get("city"), row.get("state"), row.get("zip")]
    return ", ".join([str(x).strip() for x in parts if x and str(x).strip()])


def _fetch_json(url: str, user_agent: str = "BillKarma-Geocoder/1.0") -> dict | list | None:
    req = Request(url, headers={"User-Agent": user_agent})
    try:
        with urlopen(req, timeout=25) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return None


def _geocode_census(address: str) -> tuple[float, float] | None:
    payload = _fetch_json(CENSUS_ENDPOINT.format(address=quote_plus(address)))
    if not payload or not isinstance(payload, dict):
        return None
    matches = (((payload.get("result") or {}).get("addressMatches")) or [])
    if not matches:
        return None
    coords = (matches[0].get("coordinates") or {})
    x = coords.get("x")
    y = coords.get("y")
    if x is None or y is None:
        return None
    try:
        return float(y), float(x)
    except (TypeError, ValueError):
        return None


def _geocode_nominatim(address: str) -> tuple[float, float] | None:
    payload = _fetch_json(NOMINATIM_ENDPOINT.format(address=quote_plus(address)))
    if not payload or not isinstance(payload, list) or not payload:
        return None
    row = payload[0]
    try:
        return float(row.get("lat")), float(row.get("lon"))
    except (TypeError, ValueError):
        return None


def backfill(limit: int | None, cache_path: Path, delay_ms: int) -> dict:
    db.init_db()
    cache = _load_cache(cache_path)
    delay_sec = max(0.0, delay_ms / 1000.0)
    rows_updated = 0
    used_cache = 0
    census_hits = 0
    nominatim_hits = 0
    failures = 0

    with get_db() as conn:
        query = (
            "SELECT facility_id, address, city, state, zip "
            "FROM hospitals "
            "WHERE (lat IS NULL OR lon IS NULL) "
            "AND COALESCE(address, '') != '' "
            "AND COALESCE(city, '') != '' "
            "AND COALESCE(state, '') != '' "
            "ORDER BY facility_id"
        )
        if limit:
            query += f" LIMIT {int(limit)}"
        hospitals = [dict(r) for r in conn.execute(query).fetchall()]

    for row in hospitals:
        address = _full_address(row)
        if not address:
            failures += 1
            continue

        coords = None
        cache_key = address.lower()
        if cache_key in cache and cache[cache_key]:
            val = cache[cache_key]
            try:
                coords = (float(val["lat"]), float(val["lon"]))
                used_cache += 1
            except (TypeError, ValueError, KeyError):
                coords = None

        if coords is None:
            coords = _geocode_census(address)
            if coords:
                census_hits += 1
            elif config.GEOCODER_FALLBACK_ENABLED:
                coords = _geocode_nominatim(address)
                if coords:
                    nominatim_hits += 1
            cache[cache_key] = {"lat": coords[0], "lon": coords[1]} if coords else None
            if delay_sec > 0:
                time.sleep(delay_sec)

        if not coords:
            failures += 1
            continue

        with get_db() as conn:
            conn.execute(
                "UPDATE hospitals SET lat = ?, lon = ?, updated_at = CURRENT_TIMESTAMP WHERE facility_id = ?",
                (coords[0], coords[1], row["facility_id"]),
            )
        rows_updated += 1

    _save_cache(cache_path, cache)
    log_refresh(
        source="hospital_geo_free",
        records_updated=rows_updated,
        status="success",
        notes=f"census_hits={census_hits};nominatim_hits={nominatim_hits};cache_hits={used_cache};failures={failures}",
    )
    return {
        "processed": len(hospitals),
        "updated": rows_updated,
        "cache_hits": used_cache,
        "census_hits": census_hits,
        "nominatim_hits": nominatim_hits,
        "failures": failures,
        "cache_path": str(cache_path),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--cache-path", default=str(DEFAULT_CACHE_PATH))
    parser.add_argument("--delay-ms", type=int, default=config.GEOCODER_REQUEST_DELAY_MS)
    args = parser.parse_args()
    summary = backfill(limit=args.limit, cache_path=Path(args.cache_path), delay_ms=args.delay_ms)
    print(summary)


if __name__ == "__main__":
    main()
