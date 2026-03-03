"""Parse transparency files for hospitals.

Defaults to top-300 hospitals by bed count, but can refresh all hospitals.
"""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import db
from hospital_etl import refresh_hospital_transparency, refresh_top300_transparency


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh hospital transparency pricing")
    parser.add_argument("--files-dir", default="", help="Directory containing local transparency files")
    parser.add_argument("--year", type=int, help="Data year override for hospital_prices")
    parser.add_argument("--all-hospitals", action="store_true", help="Refresh all hospitals instead of top-300")
    parser.add_argument("--limit", type=int, help="Optional limit when using --all-hospitals")
    args = parser.parse_args()

    db.init_db()
    if args.all_hospitals:
        summary = refresh_hospital_transparency(files_dir=args.files_dir, data_year=args.year, limit=args.limit)
    else:
        summary = refresh_top300_transparency(files_dir=args.files_dir, data_year=args.year)
    print(summary)


if __name__ == "__main__":
    main()
