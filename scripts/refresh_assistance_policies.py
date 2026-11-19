"""Read California hospitals' charity care policies from HCAI. Skips a policy whose file hasn't changed.

  python scripts/refresh_assistance_policies.py --city "San Diego" --city "Los Angeles" --limit 20"""

import argparse
import logging
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import policy_refresh
from db import init_db


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", action="append", default=[], help="only hospitals in these cities")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    init_db()
    policy_refresh.run(args.city, args.limit)


if __name__ == "__main__":
    main()
