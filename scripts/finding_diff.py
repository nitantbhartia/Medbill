"""Show what the B16 rule changes would do to real bills before any flag is turned on. Writes a CSV, changes nothing.

  python scripts/finding_diff.py --out finding_diff.csv"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import finding_diff
from db import init_db


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="finding_diff.csv")
    args = parser.parse_args()
    init_db()
    summary = finding_diff.run(finding_diff.stored_bills() + finding_diff.benchmark_bills(), args.out)
    print(json.dumps(summary, indent=2))
    print(f"Per-bill detail: {args.out}. Read the 20 biggest changes before turning a flag on.")


if __name__ == "__main__":
    main()
