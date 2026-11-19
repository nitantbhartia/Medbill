"""Block a deploy that makes scan accuracy worse. Compares the benchmark with a saved baseline."""

from __future__ import annotations

import json
from pathlib import Path

import config
from ocr_benchmark import run_manifest


def measure(manifest_path: str) -> dict:
    aggregate = run_manifest(manifest_path)["aggregate"]
    return {metric: aggregate[metric] for metric in config.OCR_GATE_METRICS}


def drops(current: dict, baseline: dict) -> dict:
    """Points lost per metric (positive = worse), for the metrics that fell by more than the allowed drop."""
    lost = {metric: round((baseline[metric] - current[metric]) * 100, 2) for metric in config.OCR_GATE_METRICS}
    return {metric: points for metric, points in lost.items() if points > config.OCR_GATE_MAX_DROP_PCT}


def run_gate(suites=None, accept: bool = False) -> list[str]:
    """Check every benchmark that exists. Returns the failure messages (empty = pass). accept=True saves new baselines."""
    failures = []
    for name, manifest, baseline_path in suites or config.OCR_GATE_SUITES:
        if not Path(manifest).exists():
            continue
        current = measure(manifest)
        baseline_file = Path(baseline_path)
        if accept or not baseline_file.exists():
            baseline_file.write_text(json.dumps(current, indent=2) + "\n")
            print(f"{name}: baseline saved {current}")
            continue
        lost = drops(current, json.loads(baseline_file.read_text()))
        print(f"{name}: {current}")
        failures += [f"{name}: {metric} dropped {points} points (allowed {config.OCR_GATE_MAX_DROP_PCT})"
                     for metric, points in lost.items()]
    return failures
