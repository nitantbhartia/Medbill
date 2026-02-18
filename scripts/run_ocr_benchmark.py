"""Run OCR benchmark manifest and print aggregate metrics."""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from ocr_benchmark import run_manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="data/ocr_benchmark/manifest.json")
    args = parser.parse_args()
    result = run_manifest(args.manifest)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
