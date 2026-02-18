"""Parse transparency files for top-300 hospitals by bed count."""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import db
from hospital_etl import refresh_top300_transparency


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh top-300 transparency pricing")
    parser.add_argument("--files-dir", default="", help="Directory containing local transparency files")
    parser.add_argument("--year", type=int, help="Data year override for hospital_prices")
    args = parser.parse_args()

    db.init_db()
    summary = refresh_top300_transparency(files_dir=args.files_dir, data_year=args.year)
    print(summary)


if __name__ == "__main__":
    main()
