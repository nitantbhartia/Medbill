#!/usr/bin/env python3
"""Download, transform, and load official CMS 2026 datasets."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cms_loader import download_cms_2026, transform_cms_2026, load_transformed_cms_2026
from db import init_db
from data_refresh import data_health_check


def main() -> int:
    parser = argparse.ArgumentParser(description="Load CMS 2026 data into Medbill DB")
    parser.add_argument(
        "--skip-download",
        action="store_true",
        help="Skip downloading CMS source files (use existing files in data/cms/raw)",
    )
    parser.add_argument(
        "--raw-dir",
        default="data/cms/raw",
        help="Directory for raw downloaded source files",
    )
    parser.add_argument(
        "--processed-dir",
        default="data/cms/processed",
        help="Directory for transformed CSV outputs",
    )
    args = parser.parse_args()

    init_db()

    if not args.skip_download:
        downloaded = download_cms_2026(args.raw_dir)
        print("Downloaded source files:")
        print(json.dumps(downloaded, indent=2))

    transformed = transform_cms_2026(args.raw_dir, args.processed_dir)
    print("Transformed row counts:")
    print(json.dumps(transformed, indent=2))

    loaded = load_transformed_cms_2026(args.processed_dir)
    print("Loaded row counts:")
    print(json.dumps(loaded, indent=2))

    health = data_health_check()
    print("Data health check:")
    print(json.dumps(health, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
