"""Read California hospitals' charity care policies from HCAI. Skips a policy whose file hasn't changed.

  python scripts/refresh_assistance_policies.py --city "San Diego" --city "Los Angeles" --limit 20"""

import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import assistance_policies
import config
import hcai_policies
from db import get_db, init_db


def refresh_one(hospital: dict) -> str:
    """Returns what happened: new, unchanged, or why it was skipped."""
    if not hospital["charity_policy"]:
        return "skipped: no charity care policy on the page"
    url, effective = hospital["charity_policy"]
    try:
        sha256, text = assistance_policies.fetch_policy(url)
        if hospital["discount_policy"] and hospital["discount_policy"][0] != url:
            sha2, text2 = assistance_policies.fetch_policy(hospital["discount_policy"][0])
            sha256, text = sha256 + sha2, text + "\n\n" + text2
    except Exception as exc:
        return f"skipped: could not read the policy file ({exc})"
    if len(text.strip()) < 200:
        return "skipped: the file has no readable text (scanned image)"
    if assistance_policies.latest_hash(hospital["license"]) == sha256:
        return "unchanged"
    hospital["facility_id"] = assistance_policies.match_facility_id(hospital["name"], hospital["zip"])
    terms, evidence = assistance_policies.extract_policy_terms(text)
    terms = assistance_policies.apply_legal_floors(terms, evidence)
    assistance_policies.save_policy(hospital, url, sha256, effective, terms, evidence)
    return f"new: {len(terms)} terms with quotes"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", action="append", default=[], help="only hospitals in these cities")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    init_db()
    done = 0
    for url in hcai_policies.hospital_page_urls():
        hospital = hcai_policies.fetch_hospital(url)
        time.sleep(config.POLICY_FETCH_DELAY_SECONDS)
        if args.city and (hospital["city"] or "").lower() not in {c.lower() for c in args.city}:
            continue
        result = refresh_one(hospital)
        print(f"{hospital['name']} ({hospital['city']}): {result}")
        done += 1
        if args.limit and done >= args.limit:
            break
    with get_db() as db:
        db.execute("INSERT INTO data_refresh_log (source, records_updated, status, notes) VALUES (?, ?, 'ok', ?)",
                   ("hcai_assistance_policies", done, f"cities={args.city}"))


if __name__ == "__main__":
    main()
