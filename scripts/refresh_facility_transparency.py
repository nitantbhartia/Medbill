"""Parse transparency files across hospitals, ASCs, and imaging centers."""

from __future__ import annotations

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from db import init_db  # noqa: E402
from hospital_etl import refresh_facility_transparency  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh transparency parsing for facilities")
    parser.add_argument("--files-dir", default="", help="Directory containing local transparency files")
    parser.add_argument("--year", type=int, default=None, help="Data year for stored rows")
    parser.add_argument(
        "--types",
        default="hospital,asc,imaging_center",
        help="Comma-separated facility types to refresh",
    )
    parser.add_argument("--limit", type=int, default=None, help="Optional limit")
    args = parser.parse_args()

    init_db()
    types = tuple(t.strip() for t in args.types.split(",") if t.strip())
    summary = refresh_facility_transparency(
        files_dir=args.files_dir,
        data_year=args.year,
        facility_types=types,
        limit=args.limit,
    )
    print(summary)


if __name__ == "__main__":
    main()
