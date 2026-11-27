"""Load hospitals' own published standard-charges files (CMS machine-readable CSV) into hospital_prices.

Prices are copied from the file as published. A hospital is skipped, with the reason logged, when its file
cannot be read or does not give one clear gross charge for the Level 5 ER visit."""

from __future__ import annotations

import csv
import http.client
import json
import logging
import os
import shutil
import sqlite3
import tempfile
import threading
from datetime import date, datetime
from urllib.request import Request, urlopen, urlretrieve

import config
from data_quality import hospitals_off_cms_location
from db import get_db
from hospital_etl import (
    TARGET_PROCEDURES,
    first,
    load_csv_rows,
    normalize_price_rows,
    summarize_by_code,
    upsert_facility_procedure_price,
)
from hospital_seo import log_refresh, recompute_billing_metrics, recompute_facility_billing_metrics

log = logging.getLogger(__name__)

SAN_DIEGO_LOAD_SOURCE = "san_diego_price_files_v2"  # v1 loaded nothing: every file had several charge lines for 99285
DATABASE_COPY_SUFFIX = ".before-san_diego_price_files_v1"
UPDATED_ON_FORMATS = ("%m/%d/%Y", "%Y-%m-%d")
LISTED_LOAD_SOURCE = "listed_price_files"
_load_running = threading.Lock()


def download_price_file(url: str, path: str) -> None:
    request = Request(url, headers={"User-Agent": config.PRICE_FILE_USER_AGENT})
    with urlopen(request, timeout=config.PRICE_FILE_TIMEOUT_SECONDS) as response, open(path, "wb") as out:
        while chunk := response.read(1024 * 1024):
            out.write(chunk)
            if out.tell() > config.PRICE_FILE_MAX_BYTES:
                raise ValueError("file is larger than the download limit")
        owed = getattr(response, "length", 0)  # http.client reports a connection closed early as a normal end of file
        if owed:
            raise ValueError(f"download ended {owed} bytes short")


def file_updated_on(path: str) -> str:
    """The last_updated_on date from the two hospital-info lines that open a CMS file, as YYYY-MM-DD."""
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        names, values = next(reader, []), next(reader, [])
    info = {name.strip().lower(): value.strip() for name, value in zip(names, values)}
    for fmt in UPDATED_ON_FORMATS:
        try:
            return datetime.strptime(info.get("last_updated_on", ""), fmt).date().isoformat()
        except ValueError:
            continue
    raise ValueError("no last_updated_on date in the file header")


def _is_hospital_list_price_row(row: dict) -> bool:
    """True for a row that can carry the hospital's base outpatient charge: not inpatient-only, not a physician fee, no modifier."""
    setting = str(first(row, ("setting",)) or "").strip().lower()
    billing_class = str(first(row, ("billing_class",)) or "").strip().lower()
    return setting != "inpatient" and billing_class != "professional" and not first(row, ("modifiers",))


def read_list_prices(path: str) -> list[dict]:
    """One row per tracked code with the file's gross charge and discounted cash price.

    ER visit codes are read only from base hospital rows. Where a code has several charge lines, the trauma,
    critical-care and left-without-being-seen lines are set aside; if the rest still disagree on the gross charge,
    the code is left out rather than guessed. Raises ValueError when that leaves no gross charge for the Level 5 visit."""
    rows = load_csv_rows(path, only_codes=TARGET_PROCEDURES)
    er_rows = [r for r in normalize_price_rows([r for r in rows if _is_hospital_list_price_row(r)]) if r["cpt_code"] in config.ER_VISIT_CODES]
    other_rows = [r for r in normalize_price_rows(rows) if r["cpt_code"] in TARGET_PROCEDURES and r["cpt_code"] not in config.ER_VISIT_CODES]

    for code in config.ER_VISIT_CODES:
        lines = [r for r in er_rows if r["cpt_code"] == code and r["gross_charge"]]
        if len({r["gross_charge"] for r in lines}) > 1:
            lines = [r for r in lines if not any(word in (r["description"] or "").upper() for word in config.ER_SPECIAL_LINE_WORDS)]
        if len({r["gross_charge"] for r in lines}) > 1:
            log.warning("%s lists %s with more than one plain visit charge, not loading that code: %s",
                        path, code, sorted({(r["gross_charge"], r["description"]) for r in lines}))
            lines = []
        er_rows = [r for r in er_rows if r["cpt_code"] != code] + lines
    if not any(r["cpt_code"] == config.ER_GRADE_CODE and r["gross_charge"] for r in er_rows):
        raise ValueError(f"no single gross charge for {config.ER_GRADE_CODE} in the file")
    return [price for price in summarize_by_code(er_rows + other_rows) if price["cpt_modifier"] is None]


def load_price_file(facility_id: str, path: str, source_url: str) -> dict:
    """Parse one downloaded file and save its prices, each with the file's URL and last-updated date."""
    try:
        updated_on = file_updated_on(path)
        prices = read_list_prices(path)
    except (OSError, ValueError, csv.Error) as error:
        log.error("Price file for hospital %s (%s) not loaded: %s", facility_id, source_url, error)
        return {"facility_id": facility_id, "status": "skipped", "reason": str(error)}

    year = date.today().year
    for price in prices:
        upsert_facility_procedure_price(facility_id, {**price, "source_url": source_url}, "hospital", data_year=year)
    with get_db() as db:
        db.executemany(
            "UPDATE hospital_prices SET source_url = ?, source_updated_on = ? WHERE facility_id = ? AND cpt_code = ? AND data_year = ?",
            [(source_url, updated_on, facility_id, price["cpt_code"], year) for price in prices],
        )
    er = {p["cpt_code"]: {"gross": p["gross_charge"], "cash": p["cash_price"]} for p in prices if p["cpt_code"] in config.ER_VISIT_CODES}
    return {"facility_id": facility_id, "status": "loaded", "codes": len(prices), "file_updated_on": updated_on, "er_prices": er}


def fetch_and_load(facility_id: str, name_phrase: str, source_url: str) -> dict:
    """Download a hospital's file and load it, but only onto the CMS hospital record it was listed for."""
    with get_db() as db:
        hospital = db.execute("SELECT name, city, state FROM hospitals WHERE facility_id = ?", (facility_id,)).fetchone()
    if not hospital or name_phrase not in hospital["name"].upper():
        log.error("Hospital %s is not on file as %r (found %s); price file not loaded", facility_id, name_phrase, hospital["name"] if hospital else None)
        return {"facility_id": facility_id, "status": "skipped", "reason": "CMS hospital record missing or a different hospital"}
    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, "standardcharges.csv")
        try:
            download_price_file(source_url, path)
        except (OSError, ValueError, http.client.HTTPException) as error:
            log.error("Price file download failed for hospital %s (%s): %s", facility_id, source_url, error)
            return {"facility_id": facility_id, "status": "skipped", "reason": f"download failed: {error}"}
        result = load_price_file(facility_id, path, source_url)
    return {**result, "name": hospital["name"], "city": hospital["city"], "state": hospital["state"]}


def parse_cms_hpt(text: str) -> dict[str, str]:
    """cms-hpt.txt lists a block per hospital location. Returns {location name, lower case: its first mrf-url}."""
    files: dict[str, str] = {}
    location = None
    for line in text.splitlines():
        key, separator, value = line.partition(":")
        key = key.strip().lower()
        if separator and key == "location-name":
            location = value.strip().lower()
        elif separator and key == "mrf-url" and location:
            files.setdefault(location, value.strip())
    return files


def listed_price_file(site: str, location_name: str) -> str | None:
    """The price file a hospital website's cms-hpt.txt lists for one location, or None if it is not listed."""
    request = Request(site.rstrip("/") + "/cms-hpt.txt", headers={"User-Agent": config.PRICE_FILE_USER_AGENT})
    with urlopen(request, timeout=config.PRICE_FILE_TIMEOUT_SECONDS) as response:
        text = response.read(config.CMS_HPT_MAX_BYTES).decode("utf-8-sig", errors="replace")
    return parse_cms_hpt(text).get(location_name.strip().lower())


def load_listed_hospital(target: dict) -> dict:
    """Find one hospital's file through cms-hpt.txt and load it. target: facility_id, name_phrase, site, location_name."""
    try:
        source_url = listed_price_file(target["site"], target["location_name"])
    except (OSError, ValueError, http.client.HTTPException) as error:
        log.error("cms-hpt.txt not read for hospital %s (%s): %s", target["facility_id"], target["site"], error)
        return {"facility_id": target["facility_id"], "status": "skipped", "reason": f"cms-hpt.txt not read: {error}"}
    if not source_url:
        return {"facility_id": target["facility_id"], "status": "skipped", "reason": f"{target['location_name']!r} is not listed in cms-hpt.txt"}
    return {**fetch_and_load(target["facility_id"], target["name_phrase"].upper(), source_url), "source_url": source_url}


def load_listed_hospitals(targets: list[dict]) -> list[dict]:
    """One-off started from POST /ops/load-hospital-prices; it can be run again. Loads each hospital, then regrades
    the ones it loaded with the existing grading logic. Only one load runs at a time."""
    if not _load_running.acquire(blocking=False):
        log.warning("Price load not started: another one is running")
        return []
    try:
        log.warning("Price load starting for %s hospitals; database copy: %s", len(targets), backup_database())
        results = []
        for target in targets:
            results.append(load_listed_hospital(target))
            log.warning("Price file: %s", json.dumps(results[-1]))
        loaded = {r["facility_id"] for r in results if r["status"] == "loaded"}
        if loaded:
            recompute_billing_metrics(only_facility_ids=loaded)
            recompute_facility_billing_metrics()
        log_refresh(LISTED_LOAD_SOURCE, len(loaded), "success" if loaded else "failed", json.dumps(results))
        log.warning("Price load finished: %s", json.dumps(results))
        return results
    except Exception:
        log.exception("Price load stopped on an unexpected error; hospitals loaded so far are kept")
        raise
    finally:
        _load_running.release()


def backup_database() -> str | None:
    """Copy the SQLite file beside itself before a bulk load. Skipped when the disk has no room for a second copy."""
    if not os.path.isfile(config.DB_PATH):
        return None
    if shutil.disk_usage(os.path.dirname(config.DB_PATH) or ".").free < 2 * os.path.getsize(config.DB_PATH):
        log.error("Not enough free disk to copy %s before the price load; loading without a copy", config.DB_PATH)
        return None
    target = config.DB_PATH + DATABASE_COPY_SUFFIX
    if os.path.exists(target):  # the v1 attempt made this copy and then loaded nothing
        return target
    source, copy = sqlite3.connect(config.DB_PATH), sqlite3.connect(target)
    try:
        source.backup(copy)
    finally:
        source.close()
        copy.close()
    return target


def log_location_mismatches() -> None:
    """Report hospitals whose city or state differs from CMS's record; nothing is changed."""
    os.makedirs(os.path.dirname(config.CMS_HOSPITAL_GENERAL_CSV_PATH), exist_ok=True)
    try:
        urlretrieve(config.CMS_HOSPITAL_GENERAL_CSV_URL, config.CMS_HOSPITAL_GENERAL_CSV_PATH)
    except OSError as error:
        log.error("CMS hospital directory download failed, locations not checked: %s", error)
        return
    try:
        mismatches = hospitals_off_cms_location(config.CMS_HOSPITAL_GENERAL_CSV_PATH)
    except (KeyError, csv.Error, ValueError) as error:
        log.error("CMS hospital directory not in the expected layout, locations not checked: %r", error)
        return
    wrong_place = [m for m in mismatches if m["cms_city"]]
    log.warning("Hospital locations checked against CMS: %s saved under a different city/state, %s graded hospitals with no CMS record",
                len(wrong_place), len(mismatches) - len(wrong_place))
    for mismatch in wrong_place[:config.LOCATION_MISMATCH_LOG_LIMIT]:
        log.warning("Location differs from CMS: %s", json.dumps(mismatch))


def load_san_diego_prices_once() -> list[dict] | None:
    """One-off production load of the San Diego price files. The attempt is recorded in data_refresh_log
    before it starts, so it runs on one deploy only even if that run fails. Returns None if already attempted."""
    with get_db() as db:
        attempted = db.execute("SELECT 1 FROM data_refresh_log WHERE source = ? LIMIT 1", (SAN_DIEGO_LOAD_SOURCE,)).fetchone()
    if attempted:
        return None
    log_refresh(SAN_DIEGO_LOAD_SOURCE, 0, "started")
    log.warning("San Diego price load starting; database copy: %s", backup_database())
    results = []
    for entry in config.SAN_DIEGO_PRICE_FILES:
        results.append(fetch_and_load(*entry))
        log.warning("San Diego price file: %s", json.dumps(results[-1]))
    loaded = {r["facility_id"] for r in results if r["status"] == "loaded"}
    if loaded:
        recompute_billing_metrics(only_facility_ids=loaded)
        with get_db() as db:
            grades = {row["facility_id"]: dict(row) for row in db.execute(
                "SELECT facility_id, billing_grade, avg_markup_vs_medicare, procedures_compared FROM billing_metrics")
                if row["facility_id"] in loaded}
        results = [{**r, **grades.get(r["facility_id"], {})} for r in results]
    log_refresh(SAN_DIEGO_LOAD_SOURCE, len(loaded), "success" if loaded else "failed", json.dumps(results))
    log.warning("San Diego price load finished: %s", json.dumps(results))
    log_location_mismatches()
    return results
