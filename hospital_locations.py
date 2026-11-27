"""A hospital's city and state come from its own CMS record, never a health system's billing address.

A hospital keyed by CMS Certification Number uses its row in CMS Hospital General Information.
A hospital keyed by NPI (seeded from DoltHub, where the city is often the system's office) uses the
practice location, not the mailing address, that CMS's NPI registry holds for that NPI."""

from __future__ import annotations

import csv
import json
import logging
import os
import sqlite3
import time
import urllib.request
from urllib.error import URLError

import config
from db import get_db
from hospital_seo import city_slug_from_name, log_refresh, normalize_facility_id, normalize_state_code, state_slug_from_code
from transparency_discovery import USER_AGENT

log = logging.getLogger(__name__)


def read_cms_directory(path: str) -> dict[str, dict]:
    """CMS Hospital General Information as {CCN: address, city, state, zip}."""
    with open(path, newline="", encoding="utf-8-sig") as f:
        return {
            normalize_facility_id(row["Facility ID"]): {
                "address": row["Address"].strip(), "city": row["City/Town"].strip(),
                "state": row["State"].strip(), "zip": row["ZIP Code"].strip(),
            }
            for row in csv.DictReader(f) if row.get("Facility ID")
        }


def npi_practice_location(npi: str) -> dict | None:
    """Where CMS's NPI registry says this NPI practices. None when the registry has no such location."""
    request = urllib.request.Request(f"{config.NPI_REGISTRY_URL}?version=2.1&number={npi}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=config.NPI_REGISTRY_TIMEOUT_SECONDS) as response:
        payload = json.load(response)
    for result in payload.get("results") or []:
        for address in result.get("addresses") or []:
            if address.get("address_purpose") == "LOCATION" and address.get("city") and address.get("state"):
                return {"address": address.get("address_1", "").strip(), "city": address["city"].strip(),
                        "state": address["state"].strip(), "zip": (address.get("postal_code") or "")[:5]}
    return None


def is_npi(facility_id: str) -> bool:
    return len(facility_id) == 10 and facility_id.isdigit()


def _same_place(hospital, record: dict) -> bool:
    same_city = " ".join(hospital["city"].upper().split()) == " ".join(record["city"].upper().split())
    return same_city and hospital["state"].upper() == record["state"].upper()


def location_mismatches(cms_records: dict[str, dict]) -> list[dict]:
    """Hospitals whose city or state disagrees with their CMS record."""
    with get_db() as db:
        hospitals = db.execute("SELECT facility_id, name, city, state FROM hospitals ORDER BY facility_id").fetchall()
    return [
        {**dict(hospital), "cms": cms_records[hospital["facility_id"]]}
        for hospital in hospitals
        if hospital["facility_id"] in cms_records and not _same_place(hospital, cms_records[hospital["facility_id"]])
    ]


def repair_hospital_locations(cms_records: dict[str, dict]) -> int:
    """Move each mismatched hospital to the address in its CMS record. Returns how many were fixed."""
    fixed = 0
    for hospital in location_mismatches(cms_records):
        record = hospital["cms"]
        state = normalize_state_code(record["state"], record["zip"])
        if not state:
            log.error("Hospital %s (%s): CMS record has state %r; left unchanged", hospital["facility_id"], hospital["name"], record["state"])
            continue
        place = (record["address"], record["city"], state, record["zip"], city_slug_from_name(record["city"]),
                 state_slug_from_code(state), hospital["facility_id"])
        try:
            with get_db() as db:
                # facilities mirrors hospitals for the facility pages, so both move together.
                for table in ("hospitals", "facilities"):
                    db.execute(
                        f"UPDATE {table} SET address = ?, city = ?, state = ?, zip = ?, city_slug = ?, state_slug = ?, "
                        "updated_at = CURRENT_TIMESTAMP WHERE facility_id = ?",
                        place,
                    )
        except sqlite3.IntegrityError:
            log.error("Hospital %s (%s): moving it to %s, %s would duplicate another hospital's page address",
                      hospital["facility_id"], hospital["name"], record["city"], state)
            continue
        log.warning("Hospital %s (%s) moved from %s, %s to %s, %s", hospital["facility_id"], hospital["name"],
                    hospital["city"], hospital["state"], record["city"], state)
        fixed += 1
    return fixed


def moved_profile_path(hospital_slug: str) -> str | None:
    """Where a hospital's page lives now, for a request to the address it had before its location was fixed."""
    with get_db() as db:
        rows = db.execute("SELECT state_slug, city_slug, slug FROM hospitals WHERE slug = ? LIMIT 2", (hospital_slug,)).fetchall()
    if len(rows) != 1:
        return None
    return f"/hospitals/{rows[0]['state_slug']}/{rows[0]['city_slug']}/{rows[0]['slug']}/"


def fetch_cms_records() -> dict[str, dict]:
    """The CMS record for every hospital we list: the CMS directory for CCNs, the NPI registry for NPIs."""
    os.makedirs(os.path.dirname(config.CMS_HOSPITAL_GENERAL_CSV_PATH), exist_ok=True)
    urllib.request.urlretrieve(config.CMS_HOSPITAL_GENERAL_CSV_URL, config.CMS_HOSPITAL_GENERAL_CSV_PATH)
    records = read_cms_directory(config.CMS_HOSPITAL_GENERAL_CSV_PATH)
    with get_db() as db:
        npis = [row["facility_id"] for row in db.execute("SELECT facility_id FROM hospitals") if is_npi(row["facility_id"])]
    for npi in npis:
        try:
            location = npi_practice_location(npi)
        except (URLError, OSError, ValueError) as exc:
            log.error("NPI registry lookup failed for %s: %s", npi, exc)
            continue
        if location:
            records[npi] = location
        time.sleep(config.NPI_REGISTRY_PAUSE_SECONDS)
    return records


def run_location_repair() -> dict:
    """One-off: fix every hospital whose city or state disagrees with its CMS record."""
    try:
        records = fetch_cms_records()
        summary = {"fixed": repair_hospital_locations(records), "still_mismatched": len(location_mismatches(records))}
    except Exception:
        log.exception("Hospital location repair stopped on an unexpected error")
        raise
    log_refresh("hospital_location_repair", summary["fixed"], "success", json.dumps(summary))
    log.warning("Hospital location repair: %s", json.dumps(summary))
    return summary
