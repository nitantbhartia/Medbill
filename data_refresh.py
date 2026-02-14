"""
Automated data refresh pipeline for CMS data sources.
Run as a cron job or management command.

Schedule:
  Medicare PFS rates   — annually, January 5
  NCCI PTP edits       — quarterly, Jan/Apr/Jul/Oct 5th
  NCCI MUE edits       — quarterly, Jan/Apr/Jul/Oct 5th
  Hospital chargemasters — check monthly
"""

import logging
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
        "ncci_edits": {
            "passed": freshness["ncci_edits"]["fresh"],
            "detail": f"Latest date: {freshness['ncci_edits']['latest_date']}, "
                      f"days old: {freshness['ncci_edits']['days_old']}",
        },
        "hospital_profiles": {
            "passed": freshness["hospital_profiles"]["fresh"],
            "detail": f"Count: {freshness['hospital_profiles']['count']}",
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
        print("Usage: python data_refresh.py [health-check|refresh-pfs <csv>|refresh-ncci <csv>]")
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
        print(f"Loaded {count} Medicare rates.")

    elif cmd == "refresh-ncci" and len(sys.argv) == 3:
        count = refresh_ncci_edits(sys.argv[2])
        print(f"Loaded {count} NCCI edits.")

    else:
        print("Unknown command. Use: health-check, refresh-pfs <csv>, refresh-ncci <csv>")
        sys.exit(1)
