"""Check auto-read policies against their quotes, one at a time: y = reviewed, n = rejected, anything else = skip."""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db


def main() -> None:
    with get_db() as db:
        rows = db.execute("SELECT * FROM hospital_assistance_policies WHERE review_status = 'auto' ORDER BY id").fetchall()
        for row in rows:
            print(f"\n=== {row['hospital_name']} ({row['city']}), effective {row['effective_date']}\n{row['source_url']}")
            for field, quote in json.loads(row["evidence"]).items():
                print(f"- {field} = {row[field] if field in row.keys() else ''}\n    \"{quote}\"")
            answer = input("Correct? [y/n/skip] ").strip().lower()
            if answer in ("y", "n"):
                db.execute("UPDATE hospital_assistance_policies SET review_status = ? WHERE id = ?",
                           ("reviewed" if answer == "y" else "rejected", row["id"]))


if __name__ == "__main__":
    main()
