"""Generate deterministic hospital dispute-tips and SEO metadata."""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import db
from hospital_seo import generate_and_save_hospital_content, log_refresh


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate deterministic hospital content")
    parser.add_argument("--limit", type=int, help="Optional max hospitals to generate")
    args = parser.parse_args()

    db.init_db()
    created = generate_and_save_hospital_content(limit=args.limit)
    log_refresh("hospital_content", created, "success", "deterministic-template-v1")
    print({"generated": created})


if __name__ == "__main__":
    main()
