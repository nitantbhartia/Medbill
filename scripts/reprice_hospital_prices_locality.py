"""Recompute medicare_rate and markup_vs_medicare for existing hospital_prices rows
using facility ZIP -> locality mapping.

Usage:
  python3 scripts/reprice_hospital_prices_locality.py --year 2026
"""

from __future__ import annotations

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from db import get_db  # noqa: E402
from hospital_etl import get_medicare_rate_for_facility  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int)
    args = parser.parse_args()

    with get_db() as db:
        if args.year:
            rows = db.execute(
                "SELECT id, facility_id, cpt_code, gross_charge FROM hospital_prices WHERE data_year = ?",
                (args.year,),
            ).fetchall()
        else:
            rows = db.execute("SELECT id, facility_id, cpt_code, gross_charge FROM hospital_prices").fetchall()

        updated = 0
        for r in rows:
            medicare = get_medicare_rate_for_facility(r["facility_id"], r["cpt_code"])
            gross = r["gross_charge"]
            markup = (float(gross) / float(medicare)) if (gross is not None and medicare and medicare > 0) else None
            db.execute(
                "UPDATE hospital_prices SET medicare_rate = ?, markup_vs_medicare = ? WHERE id = ?",
                (medicare, markup, r["id"]),
            )
            updated += 1

    print(f"Repriced rows: {updated}")


if __name__ == "__main__":
    main()
