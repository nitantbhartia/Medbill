"""Load a hospital's published standard-charges file into hospital_prices.

The file is found through the cms-hpt.txt every hospital website must serve at its root, and is
read while it downloads, so a 600 MB file never sits in memory or on disk."""

from __future__ import annotations

import csv
import http.client
import io
import json
import logging
import os
import shutil
import sqlite3
import threading
from datetime import datetime
from urllib.error import URLError
from urllib.request import Request, urlopen

import config
import payer_rates
from db import get_db
from hospital_etl import (
    TARGET_PROCEDURES,
    _update_hospital_transparency_file,
    first,
    normalize_price_rows,
    read_csv_rows,
    summarize_by_code,
    upsert_facility_procedure_price,
)
from hospital_seo import (
    generate_and_save_hospital_content,
    log_refresh,
    normalize_facility_id,
    recompute_benchmarks,
    recompute_billing_metrics,
    recompute_facility_billing_metrics,
)
from transparency_discovery import USER_AGENT

log = logging.getLogger(__name__)

HPT_KEYS = ("location-name", "source-page-url", "mrf-url")
DATE_FORMATS = ("%Y-%m-%d", "%m/%d/%Y")
NOT_CSV_STARTS = (b"{", b"[", b"PK", b"<")  # JSON, a zip archive, an HTML error page
_load_running = threading.Lock()


def _open(url: str):
    return urlopen(Request(url, headers={"User-Agent": USER_AGENT}), timeout=config.MRF_SOCKET_TIMEOUT_SECONDS)


def parse_cms_hpt(text: str) -> list[dict]:
    """cms-hpt.txt lists one block per hospital location: location-name, source-page-url, mrf-url, contacts."""
    entries: list[dict] = []
    for line in text.splitlines():
        key, separator, value = line.partition(":")
        key = key.strip().lower()
        if not separator or key not in HPT_KEYS:
            continue
        if key == "location-name":
            entries.append({})
        if entries:
            entries[-1].setdefault(key, value.strip())
    return [entry for entry in entries if entry.get("mrf-url")]


def find_price_file(site: str, location_name: str) -> dict | None:
    """The cms-hpt.txt entry for one hospital location, or None when the site does not list it."""
    with _open(site.rstrip("/") + "/cms-hpt.txt") as response:
        text = response.read(config.CMS_HPT_MAX_BYTES).decode("utf-8-sig", errors="replace")
    wanted = location_name.strip().lower()
    return next((e for e in parse_cms_hpt(text) if e.get("location-name", "").lower() == wanted), None)


def file_date(value: str | None) -> str | None:
    """The file's last_updated_on as YYYY-MM-DD. Hospitals write it as 2026-03-30 or 4/1/2026."""
    text = (value or "").strip()
    for date_format in DATE_FORMATS:
        try:
            return datetime.strptime(text, date_format).date().isoformat()
        except ValueError:
            continue
    return text or None


def _is_plain_hospital_charge(row: dict) -> bool:
    """The hospital's own charge for the plain code: no modifier (professional component, with-procedure...)
    and not a row the file marks as a professional fee."""
    return not str(first(row, ("modifiers",)) or "").strip() and str(first(row, ("billing_class",)) or "").strip().lower() != "professional"


def read_price_csv(stream) -> tuple[list[dict], dict, str]:
    """One row per code, payer and plan for the procedures BillKarma tracks, the file's hospital-info
    preamble, and a status. Each file row is reduced to its prices as it arrives."""
    buffered = io.BufferedReader(stream)
    start = buffered.peek(config.MRF_SNIFF_BYTES)[:config.MRF_SNIFF_BYTES].lstrip(b"\xef\xbb\xbf \t\r\n")
    if not start:
        return [], {}, "empty_file"
    if start.startswith(NOT_CSV_STARTS):
        return [], {}, "unsupported_format"
    text = io.TextIOWrapper(buffered, encoding="utf-8-sig", errors="replace", newline="")
    preamble: dict = {}
    prices: list[dict] = []
    try:
        for row in read_csv_rows(text, TARGET_PROCEDURES, preamble):
            if _is_plain_hospital_charge(row):
                prices += [p for p in normalize_price_rows([row]) if p["cpt_code"] in TARGET_PROCEDURES]
    except csv.Error as exc:
        log.error("Price file is not readable CSV: %s", exc)
        return [], preamble, "malformed_file"
    for price in prices:  # Kaiser wraps descriptions in a second pair of quotes
        price["description"] = (price["description"] or "").strip('" ') or None
    return prices, preamble, "parsed" if prices else "no_standard_codes"


def load_hospital_prices(facility_id: str, site: str, location_name: str, data_year: int | None = None) -> dict:
    """Load one hospital. Nothing is stored unless the file gives a gross charge for a level 5 ER visit."""
    facility_id = normalize_facility_id(facility_id) or ""
    result = {"facility_id": facility_id, "location_name": location_name, "rows": 0}
    with get_db() as db:
        if not db.execute("SELECT 1 FROM hospitals WHERE facility_id = ?", (facility_id,)).fetchone():
            return {**result, "status": "unknown_hospital"}
    try:
        entry = find_price_file(site, location_name)
        if not entry:
            return {**result, "status": "not_listed_in_cms_hpt"}
        url = entry["mrf-url"]
        result["source_url"] = url
        with _open(url) as response:
            payer_rows, preamble, status = read_price_csv(response)
            # http.client reports a connection closed early as a normal end of file; the bytes still owed give it away.
            cut_short = bool(getattr(response, "length", 0))
    except (URLError, OSError, ValueError, http.client.HTTPException) as exc:
        log.error("Price file download failed for %s (%s): %s", facility_id, location_name, exc)
        return {**result, "status": "download_failed", "error": str(exc)}
    if status == "parsed" and cut_short:
        return {**result, "status": "download_incomplete"}
    if status != "parsed":
        return {**result, "status": status}

    prices = summarize_by_code(payer_rows)
    er_prices = {p["cpt_code"]: p["gross_charge"] for p in prices if p["cpt_code"] in config.ER_VISIT_CODES and p["gross_charge"]}
    if config.ER_LEVEL_5_CODE not in er_prices:
        return {**result, "status": "no_99285_gross_charge"}

    updated = file_date(preamble.get("last_updated_on"))
    for price in prices:
        upsert_facility_procedure_price(facility_id, {**price, "source_url": url, "source_updated": updated}, "hospital", data_year)
    payer_rates.save_payer_rates(facility_id, payer_rows, url, updated, data_year)
    with get_db() as db:
        _update_hospital_transparency_file(
            db, facility_id, url, file_format="csv", has_standard_codes=1, parse_status="parsed",
            row_count=len(payer_rows), procedures_extracted=len(prices),
        )
    return {**result, "status": "loaded", "rows": len(prices), "source_updated": updated, "er_gross_charges": er_prices}


def backup_database() -> str | None:
    """Copy the SQLite database next to itself before a load. Returns the copy's path, or None if it could not be made."""
    if config.DB_PATH == ":memory:":
        return None
    folder = os.path.join(os.path.dirname(config.DB_PATH) or ".", "backups")
    path = os.path.join(folder, f"app-before-price-load-{datetime.now():%Y%m%d-%H%M%S}.db")
    try:
        os.makedirs(folder, exist_ok=True)
        if shutil.disk_usage(folder).free < os.path.getsize(config.DB_PATH) * config.DB_BACKUP_FREE_SPACE_FACTOR:
            log.error("Not enough free disk space to copy the database before the price load")
            return None
        source = sqlite3.connect(config.DB_PATH)
        target = sqlite3.connect(path)
        with target:
            source.backup(target)
        target.close()
        source.close()
    except (OSError, sqlite3.Error) as exc:
        log.error("Database copy before the price load failed: %s", exc)
        return None
    return path


def run_price_load(targets: list[dict]) -> list[dict]:
    """Load each target hospital, then regrade with the existing grading logic. One load runs at a time."""
    if not _load_running.acquire(blocking=False):
        log.warning("Price load not started: another one is running")
        return []
    try:
        return _load_and_regrade(targets)
    except Exception:
        log.exception("Price load stopped on an unexpected error; rows loaded so far are kept")
        raise
    finally:
        _load_running.release()


def load_is_running() -> bool:
    return _load_running.locked()


def _load_and_regrade(targets: list[dict]) -> list[dict]:
    log.warning("Price load: database copy at %s", backup_database())
    results = []
    for target in targets:
        result = load_hospital_prices(target["facility_id"], target["site"], target["location_name"])
        log.warning("Price load: %s", json.dumps(result))
        results.append(result)
    loaded = [r for r in results if r["status"] == "loaded"]
    if loaded:
        recompute_benchmarks()
        recompute_billing_metrics()
        recompute_facility_billing_metrics()
        generate_and_save_hospital_content()
    log_refresh("mrf_price_load", len(loaded), "success" if len(loaded) == len(results) else "partial", json.dumps(results))
    return results
