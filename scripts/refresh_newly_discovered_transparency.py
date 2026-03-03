"""Refresh transparency parsing only for hospitals discovered by the URL crawler."""

from __future__ import annotations

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from db import init_db  # noqa: E402
from hospital_etl import refresh_facility_transparency  # noqa: E402
from hospital_seo import recompute_billing_metrics, recompute_benchmarks, recompute_facility_billing_metrics  # noqa: E402
from transparency_discovery import select_newly_discovered_hospitals  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh transparency parsing for newly discovered hospitals")
    parser.add_argument("--files-dir", default="", help="Directory containing local transparency files")
    parser.add_argument("--year", type=int, default=None, help="Data year for stored rows")
    parser.add_argument("--limit", type=int, default=None, help="Optional hospital limit")
    parser.add_argument(
        "--recompute-metrics",
        action="store_true",
        help="Recompute billing metrics after refresh",
    )
    args = parser.parse_args()

    init_db()
    selected = select_newly_discovered_hospitals(limit=args.limit)
    summary = refresh_facility_transparency(
        selected=selected,
        files_dir=args.files_dir,
        data_year=args.year,
    )
    if args.recompute_metrics:
        summary["benchmarks"] = recompute_benchmarks()
        summary["metrics"] = recompute_billing_metrics()
        summary["facility_metrics"] = recompute_facility_billing_metrics()
    print(summary)


if __name__ == "__main__":
    main()
