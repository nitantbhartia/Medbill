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


def refresh_asc_rates(csv_path: str) -> int:
    """
    Load Medicare ASC fee schedule rates from a CMS-format CSV file.
    Returns number of rows inserted.

    Accepted column aliases:
    - CPT code: HCPCS | CPT | CPT_CODE | CODE
    - Description: SHORT_DESCRIPTOR | DESCRIPTION | DESC
    - Rate: ASC_PAYMENT_RATE | PAYMENT_RATE | RATE | MEDICARE_ASC_RATE
    - Year: EFFECTIVE_YEAR | YEAR
    - Coverage indicator (optional):
      FACILITY_INDICATOR | COVERED_INDICATOR | ASC_COVERED | PAYMENT_INDICATOR
    """
    import csv

    def _cell(row: dict, *names: str) -> str:
        for name in names:
            value = row.get(name)
            if value is not None and str(value).strip():
                return str(value).strip()
        return ""

    rows = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cpt_code = _cell(row, "HCPCS", "CPT", "CPT_CODE", "CODE")
            if not cpt_code:
                continue
            year_raw = _cell(row, "EFFECTIVE_YEAR", "YEAR")
            try:
                effective_year = int(year_raw) if year_raw else date.today().year
            except ValueError:
                effective_year = date.today().year
            indicator = _cell(
                row,
                "FACILITY_INDICATOR",
                "COVERED_INDICATOR",
                "ASC_COVERED",
                "PAYMENT_INDICATOR",
            ).upper()
            is_covered = indicator not in {"N", "NO", "0", "NONCOVERED", "NOT COVERED"}
            rows.append(
                (
                    cpt_code,
                    _cell(row, "SHORT_DESCRIPTOR", "DESCRIPTION", "DESC"),
                    _parse_float(_cell(row, "ASC_PAYMENT_RATE", "PAYMENT_RATE", "RATE", "MEDICARE_ASC_RATE")),
                    effective_year,
                    1 if is_covered else 0,
                )
            )

    if not rows:
        log.warning("No ASC rows parsed from %s", csv_path)
        return 0

    with get_db() as db:
        db.execute("DELETE FROM asc_medicare_rates WHERE effective_year = ?", (rows[0][3],))
        db.executemany(
            """
            INSERT INTO asc_medicare_rates (
                cpt_code, description, medicare_asc_rate, effective_year, is_covered_asc_procedure
            ) VALUES (?, ?, ?, ?, ?)
            """,
            rows,
        )

    log.info("Loaded %d ASC rates from %s", len(rows), csv_path)
    return len(rows)


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
        "asc_rates.csv": refresh_asc_rates,
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


def refresh_enrichment_weekly() -> dict:
    """
    Weekly scheduled job: re-fetch CMS Care Compare star ratings.
    Logs any hospitals whose star rating changed.

    Schedule: every week (e.g., Sunday 2am UTC)
    Run: python data_refresh.py enrich-weekly
    """
    from enrichment import fetch_care_compare_ratings, coverage_report

    updated = fetch_care_compare_ratings()
    cov = coverage_report()

    with get_db() as db:
        db.execute(
            "INSERT INTO data_refresh_log (source, records_updated, status, notes) VALUES (?, ?, ?, ?)",
            ("care_compare_weekly", updated, "ok", f"stars_known={cov.get('stars_known')}"),
        )
    log.info("Weekly enrichment: %d star ratings updated", updated)
    return {"updated": updated, "coverage": cov}


def refresh_enrichment_quarterly(pos_csv_path: str) -> dict:
    """
    Quarterly scheduled job (Jan/Apr/Jul/Oct): re-download CMS POS file,
    update ownership, coordinates, bed counts, and standardize addresses.

    Schedule: 1st of January, April, July, October
    Run: python data_refresh.py enrich-quarterly <pos_csv_path>
    """
    from enrichment import (
        load_pos_file, match_pos_to_hospitals, update_ownership_from_pos,
        update_coordinates_from_pos, update_beds_from_pos,
        standardize_addresses_from_pos, coverage_report, extract_asc_and_imaging_from_pos,
    )

    pos_count = load_pos_file(pos_csv_path)
    matched = match_pos_to_hospitals()
    ownership_updated = update_ownership_from_pos(matched)
    coords_updated, _ = update_coordinates_from_pos(matched)
    beds_updated = update_beds_from_pos(matched)
    addr_updated = standardize_addresses_from_pos(matched)
    non_hospital = extract_asc_and_imaging_from_pos(pos_csv_path)
    cov = coverage_report()

    with get_db() as db:
        db.execute(
            "INSERT INTO data_refresh_log (source, records_updated, status, notes) VALUES (?, ?, ?, ?)",
            (
                "cms_pos_quarterly",
                ownership_updated + coords_updated + beds_updated,
                "ok",
                f"pos_loaded={pos_count} matched={len(matched)} ownership={ownership_updated} coords={coords_updated} asc={non_hospital.get('asc', 0)} imaging={non_hospital.get('imaging_center', 0)}",
            ),
        )
    log.info("Quarterly enrichment complete: %d matched, %d ownership, %d coords", len(matched), ownership_updated, coords_updated)
    return {
        "pos_records_loaded": pos_count,
        "hospitals_matched": len(matched),
        "ownership_updated": ownership_updated,
        "coordinates_updated": coords_updated,
        "beds_updated": beds_updated,
        "addresses_updated": addr_updated,
        "non_hospital_facilities": non_hospital,
        "coverage": cov,
    }


def refresh_enrichment_annual(hcris_csv_path: str) -> dict:
    """
    Annual scheduled job (January/February): reload HCRIS cost reports
    and recalculate charity care percentages.

    Schedule: February 1st each year (HCRIS data typically released Jan/Feb for prior year)
    Run: python data_refresh.py enrich-annual <hcris_csv_path>
    """
    from enrichment import load_hcris_charity_care, coverage_report

    updated = load_hcris_charity_care(hcris_csv_path)
    cov = coverage_report()

    with get_db() as db:
        db.execute(
            "INSERT INTO data_refresh_log (source, records_updated, status, notes) VALUES (?, ?, ?, ?)",
            ("hcris_annual", updated, "ok", f"charity_known={cov.get('charity_known')}"),
        )
    log.info("Annual HCRIS enrichment: %d hospitals updated", updated)
    return {"updated": updated, "coverage": cov}


def refresh_compliance_after_parse(facility_id: str) -> None:
    """
    On-demand: recalculate compliance_status for a single hospital
    after their price transparency file is re-parsed.
    """
    from enrichment import update_compliance_status
    from db import get_db

    with get_db() as db:
        tf = db.execute(
            "SELECT parse_status, procedures_extracted, has_standard_codes FROM transparency_files WHERE facility_id = ?",
            (facility_id,),
        ).fetchone()

        if tf is None:
            status, procs = "Unverified", None
        elif tf["parse_status"] == "error" or not tf.get("procedures_extracted"):
            status, procs = "Non-compliant", 0
        else:
            procs = tf["procedures_extracted"] or 0
            if procs >= 50 and tf.get("has_standard_codes"):
                status = "Compliant"
            elif procs > 0:
                status = "Partial"
            else:
                status = "Non-compliant"

        db.execute(
            """
            UPDATE hospitals
            SET compliance_status = ?, procedures_in_file = ?, compliance_last_checked = CURRENT_DATE
            WHERE facility_id = ?
            """,
            (status, procs, facility_id),
        )


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
            "Commands: health-check, refresh-pfs, refresh-opps, refresh-asc, refresh-ncci, "
            "refresh-benchmarks, refresh-zip-localities, refresh-all, "
            "enrich-weekly, enrich-quarterly <pos_csv>, enrich-annual <hcris_csv>"
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

    elif cmd == "enrich-weekly":
        result = refresh_enrichment_weekly()
        print(f"Weekly enrichment complete: {result['updated']} star ratings updated")

    elif cmd == "enrich-quarterly" and len(sys.argv) == 3:
        result = refresh_enrichment_quarterly(sys.argv[2])
        print("Quarterly enrichment complete:")
        for key, val in result.items():
            if key != "coverage":
                print(f"  - {key}: {val}")

    elif cmd == "enrich-annual" and len(sys.argv) == 3:
        result = refresh_enrichment_annual(sys.argv[2])
        print(f"Annual HCRIS enrichment complete: {result['updated']} hospitals updated")

    elif cmd == "refresh-pfs" and len(sys.argv) == 3:
        count = refresh_medicare_rates(sys.argv[2])
        print(f"Loaded {count} Medicare PFS rates.")

    elif cmd == "refresh-opps" and len(sys.argv) == 3:
        count = refresh_opps_rates(sys.argv[2])
        print(f"Loaded {count} OPPS rates.")

    elif cmd == "refresh-asc" and len(sys.argv) == 3:
        count = refresh_asc_rates(sys.argv[2])
        print(f"Loaded {count} ASC rates.")

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
            "Unknown command. Use: health-check, refresh-pfs, refresh-opps, refresh-asc, "
            "refresh-ncci, refresh-benchmarks, refresh-zip-localities, refresh-all, "
            "enrich-weekly, enrich-quarterly <pos_csv>, enrich-annual <hcris_csv>"
        )
        sys.exit(1)
