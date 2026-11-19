"""Score every rule on the 200 synthetic bills in data/rule_benchmark, in a throwaway database (no OCR, no network).

  python scripts/rule_benchmark.py                 # per-rule report
  python scripts/rule_benchmark.py --gate          # exit 1 if a rule got worse than the baseline
  python scripts/rule_benchmark.py --accept        # save the current scores as the baseline
  python scripts/rule_benchmark.py --generate [--images]   # (re)make the bills; --images also renders them in 3 layouts for the OCR benchmark"""

import argparse
import json
import os
import sys

os.environ["DB_PATH"] = ":memory:"
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import rule_benchmark
from db import init_db


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate", action="store_true")
    parser.add_argument("--accept", action="store_true")
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--images", action="store_true")
    args = parser.parse_args()
    if args.generate:
        import generate_ocr_benchmark_samples
        generate_ocr_benchmark_samples.write_rule_bills(images=args.images)
        return
    init_db()
    rule_benchmark.prepare_database()
    report = rule_benchmark.run(rule_benchmark.load())
    print(json.dumps(report, indent=2))
    if args.accept or not rule_benchmark.BASELINE_FILE.exists():
        rule_benchmark.BASELINE_FILE.write_text(json.dumps(report, indent=2) + "\n")
        print("Baseline saved.")
        return
    failures = rule_benchmark.regressions(report, json.loads(rule_benchmark.BASELINE_FILE.read_text()))
    if failures and args.gate:
        sys.exit("RULE BENCHMARK GATE FAILED\n" + "\n".join(failures))
    print("\n".join(failures) or "No rule got worse.")


if __name__ == "__main__":
    main()
