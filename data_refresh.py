"""
Automated data refresh pipeline for CMS data sources.
Run as a cron job or management command.

Schedule:
  Medicare PFS rates        — annually, January 5
  Medicare OPPS rates       — annually, January 5
  NCCI PTP edits            — quarterly, Jan/Apr/Jul/Oct 5th
  Procedure benchmarks      — as new data becomes available
  ZIP locality map          — as CMS locality mappings update
  Hospital chargemasters    — check monthly
"""

import logging
import os
from datetime import date

from db import get_db
from data_freshness import get_data_freshness

log = logging.getLogger(__name__)


def refresh_medicare_rates(csv_path: str) -> int:
    """
    Load Medicare PFS rates from a CMS-format CSV file.
    Returns number of rows inserted.

    Expected CSV columns: HCPCS, DESCRIPTION, LOCALITY, STATE,
    NON_FACILITY_RATE, FACILITY_RATE, EFFECTIVE_YEAR
    """
    import csv

    count = 0
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            try:
                rows.append((
                    row.get("HCPCS", "").strip(),
                    row.get("DESCRIPTION", "").strip(),
                    row.get("LOCALITY", "0000000").strip(),
                    row.get("STATE", "").strip() or None,
                    _parse_float(row.get("NON_FACILITY_RATE")),
                    _parse_float(row.get("FACILITY_RATE")),
                    int(row.get("EFFECTIVE_YEAR", date.today().year)),
                ))
                count += 1
            except (ValueError, KeyError) as e:
                log.warning("Skipping bad row: %s — %s", row, e)

    with get_db() as db:
        db.execute("DELETE FROM medicare_rates WHERE effective_year = ?", (rows[0][6],))
        db.executemany(
            "INSERT OR REPLACE INTO medicare_rates "
            "(cpt_code, description, locality, state, non_facility_rate, facility_rate, effective_year) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            rows,
        )

    log.info("Loaded %d Medicare rates from %s", count, csv_path)
    return count


def refresh_ncci_edits(csv_path: str) -> int:
    """
    Load NCCI PTP edit pairs from a CMS-format CSV file.
    Returns number of rows inserted.

    Expected CSV columns: COLUMN_1, COLUMN_2, EFFECTIVE_DATE,
    DELETION_DATE, MODIFIER_INDICATOR
    """
    import csv

    count = 0
    rows = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                rows.append((
                    row["COLUMN_1"].strip(),
                    row["COLUMN_2"].strip(),
                    row.get("EFFECTIVE_DATE", "").strip() or None,
                    row.get("DELETION_DATE", "").strip() or None,
                    row.get("MODIFIER_INDICATOR", "").strip() or "0",
                ))
                count += 1
            except (ValueError, KeyError) as e:
                log.warning("Skipping bad NCCI row: %s — %s", row, e)

    with get_db() as db:
        db.executemany(
            "INSERT OR REPLACE INTO ncci_edits "
            "(column_1_code, column_2_code, effective_date, deletion_date, modifier_indicator) "
            "VALUES (?, ?, ?, ?, ?)",
            rows,
        )

    log.info("Loaded %d NCCI edits from %s", count, csv_path)
    return count


def refresh_opps_rates(csv_path: str) -> int:
    """
    Load Medicare OPPS rates from a CMS-format CSV file.
    Returns number of rows inserted.

    Expected CSV columns: HCPCS, APC, DESCRIPTION,
    NATIONAL_PAYMENT_RATE, EFFECTIVE_YEAR
    """
    import csv

    count = 0
    rows = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                rows.append((
                    row["HCPCS"].strip(),
                    row.get("APC", "").strip() or None,
                    row.get("DESCRIPTION", "").strip(),
                    _parse_float(row.get("NATIONAL_PAYMENT_RATE")),
                    int(row.get("EFFECTIVE_YEAR", date.today().year)),
                ))
                count += 1
            except (ValueError, KeyError) as e:
                log.warning("Skipping bad OPPS row: %s — %s", row, e)

    if not rows:
        log.warning("No OPPS rows parsed from %s", csv_path)
        return 0

    with get_db() as db:
        db.execute("DELETE FROM hospital_opps_rates WHERE effective_year = ?", (rows[0][4],))
        db.executemany(
            "INSERT OR REPLACE INTO hospital_opps_rates "
            "(cpt_code, apc, description, national_payment_rate, effective_year) "
            "VALUES (?, ?, ?, ?, ?)",
            rows,
        )

    log.info("Loaded %d OPPS rates from %s", count, csv_path)
    return count


def refresh_benchmarks(csv_path: str) -> int:
    """
    Load procedure benchmark data from a CSV file.
    Returns number of rows inserted.

    Expected CSV columns: CPT_CODE, REGION, SAMPLE_SIZE,
    AVG_CHARGED, MEDIAN_CHARGED, P25_CHARGED, P75_CHARGED,
    MIN_CHARGED, MAX_CHARGED, MEDICARE_RATE
    """
    import csv

    count = 0
    rows = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                rows.append((
                    row["CPT_CODE"].strip(),
                    row.get("REGION", "national").strip(),
                    int(row.get("SAMPLE_SIZE", 0)),
                    _parse_float(row.get("AVG_CHARGED")),
                    _parse_float(row.get("MEDIAN_CHARGED")),
                    _parse_float(row.get("P25_CHARGED")),
                    _parse_float(row.get("P75_CHARGED")),
                    _parse_float(row.get("MIN_CHARGED")),
                    _parse_float(row.get("MAX_CHARGED")),
                    _parse_float(row.get("MEDICARE_RATE")),
                ))
                count += 1
            except (ValueError, KeyError) as e:
                log.warning("Skipping bad benchmark row: %s — %s", row, e)

    if not rows:
        log.warning("No benchmark rows parsed from %s", csv_path)
        return 0

    with get_db() as db:
        db.executemany(
            "INSERT OR REPLACE INTO procedure_benchmarks "
            "(cpt_code, region, sample_size, avg_charged, median_charged, "
            "p25_charged, p75_charged, min_charged, max_charged, medicare_rate) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            rows,
        )

    log.info("Loaded %d procedure benchmarks from %s", count, csv_path)
    return count


def refresh_zip_localities(csv_path: str) -> int:
    """
    Load ZIP prefix -> locality/region mapping from a CSV file.
    Returns number of rows inserted.

    Expected CSV columns: ZIP_PREFIX, LOCALITY, STATE, REGION
    """
    import csv

    count = 0
    rows = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                prefix = row["ZIP_PREFIX"].strip()
                if not prefix:
                    continue
                rows.append((
                    prefix,
                    row.get("LOCALITY", "0000000").strip() or "0000000",
                    row.get("STATE", "").strip() or None,
                    row.get("REGION", "").strip() or None,
                ))
                count += 1
            except (ValueError, KeyError) as e:
                log.warning("Skipping bad ZIP locality row: %s — %s", row, e)

    if not rows:
        log.warning("No ZIP locality rows parsed from %s", csv_path)
        return 0

    with get_db() as db:
        db.executemany(
            "INSERT OR REPLACE INTO zip_locality_map "
            "(zip_prefix, locality, state, region) VALUES (?, ?, ?, ?)",
            rows,
        )

    log.info("Loaded %d ZIP locality rows from %s", count, csv_path)
    return count


def refresh_all_from_directory(data_dir: str) -> dict:
    """
    Refresh all known data sources from a directory of CSV files.
    Missing files are skipped.
    """
    loaders = {
        "medicare_pfs.csv": refresh_medicare_rates,
        "opps_rates.csv": refresh_opps_rates,
        "ncci_edits.csv": refresh_ncci_edits,
        "procedure_benchmarks.csv": refresh_benchmarks,
        "zip_locality_map.csv": refresh_zip_localities,
    }
    loaded = {}
    for filename, loader in loaders.items():
        path = os.path.join(data_dir, filename)
        if not os.path.exists(path):
            loaded[filename] = 0
            continue
        loaded[filename] = loader(path)
    return loaded


def data_health_check() -> dict:
    """
    Run a health check on all data sources.
    Returns dict with pass/fail status for each source.
    """
    freshness = get_data_freshness()
    current_year = date.today().year

    checks = {
        "medicare_rates": {
            "passed": freshness["medicare_pfs"]["fresh"],
            "detail": f"Latest year: {freshness['medicare_pfs']['latest_year']}, need: {current_year}",
        },
        "opps_rates": {
            "passed": freshness["opps_rates"]["fresh"],
            "detail": f"Latest year: {freshness['opps_rates']['latest_year']}, need: {current_year}",
        },
        "ncci_edits": {
            "passed": freshness["ncci_edits"]["fresh"],
            "detail": f"Latest date: {freshness['ncci_edits']['latest_date']}, "
                      f"days old: {freshness['ncci_edits']['days_old']}",
        },
        "procedure_benchmarks": {
            "passed": freshness["procedure_benchmarks"]["fresh"],
            "detail": f"Count: {freshness['procedure_benchmarks']['count']}",
        },
        "hospital_profiles": {
            "passed": freshness["hospital_profiles"]["fresh"],
            "detail": f"Count: {freshness['hospital_profiles']['count']}",
        },
        "zip_locality_map": {
            "passed": freshness["zip_locality_map"]["fresh"],
            "detail": f"Count: {freshness['zip_locality_map']['count']}",
        },
    }

    all_passed = all(c["passed"] for c in checks.values())
    stale = [name for name, c in checks.items() if not c["passed"]]

    if stale:
        log.warning("DATA STALE: %s", ", ".join(stale))

    return {"all_passed": all_passed, "checks": checks, "stale_sources": stale}


def _parse_float(val: str | None) -> float | None:
    if not val or val.strip() == "":
        return None
    try:
        return float(val.strip().replace(",", ""))
    except ValueError:
        return None


if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) < 2:
        print("Usage: python data_refresh.py <command> [csv_path]")
        print(
            "Commands: health-check, refresh-pfs, refresh-opps, refresh-ncci, "
            "refresh-benchmarks, refresh-zip-localities, refresh-all"
        )
        sys.exit(1)

    from db import init_db
    init_db()

    cmd = sys.argv[1]
    if cmd == "health-check":
        result = data_health_check()
        for name, check in result["checks"].items():
            status = "PASS" if check["passed"] else "FAIL"
            print(f"  [{status}] {name}: {check['detail']}")
        sys.exit(0 if result["all_passed"] else 1)

    elif cmd == "refresh-pfs" and len(sys.argv) == 3:
        count = refresh_medicare_rates(sys.argv[2])
        print(f"Loaded {count} Medicare PFS rates.")

    elif cmd == "refresh-opps" and len(sys.argv) == 3:
        count = refresh_opps_rates(sys.argv[2])
        print(f"Loaded {count} OPPS rates.")

    elif cmd == "refresh-ncci" and len(sys.argv) == 3:
        count = refresh_ncci_edits(sys.argv[2])
        print(f"Loaded {count} NCCI edits.")

    elif cmd == "refresh-benchmarks" and len(sys.argv) == 3:
        count = refresh_benchmarks(sys.argv[2])
        print(f"Loaded {count} procedure benchmarks.")

    elif cmd == "refresh-zip-localities" and len(sys.argv) == 3:
        count = refresh_zip_localities(sys.argv[2])
        print(f"Loaded {count} ZIP locality rows.")

    elif cmd == "refresh-all" and len(sys.argv) == 3:
        result = refresh_all_from_directory(sys.argv[2])
        print("Loaded data files:")
        for name, cnt in result.items():
            print(f"  - {name}: {cnt}")

    else:
        print(
            "Unknown command. Use: health-check, refresh-pfs, refresh-opps, "
            "refresh-ncci, refresh-benchmarks, refresh-zip-localities, refresh-all"
        )
        sys.exit(1)
