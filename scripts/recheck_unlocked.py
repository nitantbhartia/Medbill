"""List unlocked bills from the last 90 days whose strong findings change under the current rules.
Writes nothing unless --apply, which updates each report and records a dated notice.

  python scripts/recheck_unlocked.py [--apply]"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import report_recheck
from db import init_db


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    init_db()
    changes = report_recheck.recheck_unlocked()
    for change in changes:
        print(f"bill {change['bill_id']}: new {change['added']} withdrawn {change['withdrawn']} letter sent: {change['letter_sent']}")
        if args.apply:
            report_recheck.apply_change(change)
    print(f"{len(changes)} bills changed" + (" and updated." if args.apply else ". Nothing written; run with --apply to update them and add notices."))


if __name__ == "__main__":
    main()
