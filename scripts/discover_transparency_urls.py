"""Discover missing or broken hospital transparency URLs from public web search."""

from __future__ import annotations

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from db import init_db  # noqa: E402
from transparency_discovery import discover_missing_hospital_urls  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Discover hospital transparency URLs from public web search")
    parser.add_argument("--limit", type=int, default=None, help="Optional hospital limit")
    parser.add_argument("--sleep-seconds", type=float, default=0.25, help="Delay between hospital lookups")
    parser.add_argument("--max-workers", type=int, default=6, help="Concurrent discovery workers")
    args = parser.parse_args()

    init_db()
    summary = discover_missing_hospital_urls(
        limit=args.limit,
        sleep_seconds=args.sleep_seconds,
        max_workers=args.max_workers,
    )
    print(summary)


if __name__ == "__main__":
    main()
