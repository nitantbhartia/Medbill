"""Score OCR extraction. Default: saved predictions. --live: run the real scanner (needs GEMINI_API_KEY) and exit 1 below the minimum score."""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import config
from ocr_benchmark import run_live, run_manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="data/ocr_benchmark/manifest.json")
    parser.add_argument("--live", action="store_true")
    args = parser.parse_args()
    if not args.live:
        print(json.dumps(run_manifest(args.manifest), indent=2))
        return
    if not config.GEMINI_API_KEY:
        sys.exit("GEMINI_API_KEY is not set; live OCR benchmark cannot run.")
    from scanner import process_bill_image

    result = run_live(config.OCR_BENCHMARK_TRUTH_FILE, process_bill_image)
    print(json.dumps(result, indent=2))
    if result["aggregate"]["overall_score"] < config.OCR_BENCHMARK_MIN_SCORE:
        sys.exit(f"OCR score {result['aggregate']['overall_score']} is below minimum {config.OCR_BENCHMARK_MIN_SCORE}")


if __name__ == "__main__":
    main()
