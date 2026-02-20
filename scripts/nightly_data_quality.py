#!/usr/bin/env python3
"""Nightly data quality runner with coverage regression gating."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import db  # noqa: E402
from data_quality import (  # noqa: E402
    compare_coverage,
    compute_coverage,
    latest_quality_run,
    monitored_cpt_codes,
    run_consistency_checks,
    sampled_zips,
    save_quality_run,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run nightly data quality checks.")
    parser.add_argument("--sample-zips", type=int, default=250, help="Number of ZIPs to sample for coverage")
    parser.add_argument("--cpt-limit", type=int, default=20, help="Top CPTs to include in coverage checks")
    parser.add_argument("--radii", default="25,75", help="Comma-separated radius miles list")
    parser.add_argument("--max-drop-ratio", type=float, default=0.10, help="Max allowed coverage drop ratio")
    parser.add_argument("--write-json", default="data/quality/latest_data_quality.json")
    args = parser.parse_args()

    db.init_db()
    radii = [int(x.strip()) for x in args.radii.split(",") if x.strip()]
    zips = sampled_zips(limit=args.sample_zips)
    cpts = monitored_cpt_codes(limit=args.cpt_limit)
    coverage = compute_coverage(cpts, radii, zips)
    checks = run_consistency_checks()
    prev = latest_quality_run()
    regressions = compare_coverage(coverage, (prev or {}).get("coverage"), max_drop_ratio=args.max_drop_ratio)
    status = "PASS" if checks["all_passed"] and not regressions else "FAIL"
    notes = f"coverage_regressions={len(regressions)} sampled_zips={len(zips)} cpts={len(cpts)}"
    run_id = save_quality_run(status=status, coverage=coverage, checks={"consistency": checks, "regressions": regressions}, notes=notes)

    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "run_id": run_id,
        "status": status,
        "summary": {
            "sampled_zips": len(zips),
            "cpts": len(cpts),
            "radii": radii,
            "regressions": len(regressions),
            "all_consistency_checks_passed": checks["all_passed"],
        },
        "checks": checks,
        "coverage": coverage,
        "regressions": regressions,
    }
    out_path = args.write_json
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=True)
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

