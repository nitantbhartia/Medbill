import json
from pathlib import Path

from ocr_benchmark import run_manifest, score_extraction


def test_score_extraction_returns_weighted_score():
    truth = {
        "provider_name": "Memorial Regional Hospital",
        "total_charged": 1000.0,
        "line_items": [{"cpt_code": "99283", "charged_amount": 1000.0}],
    }
    pred = {
        "provider_name": "Memorial Regional Hospital",
        "total_charged": 1000.0,
        "line_items": [{"cpt_code": "99283", "charged_amount": 1000.0}],
    }
    result = score_extraction(pred, truth)
    assert result.overall_score == 1.0


def test_run_manifest_reads_generated_samples():
    manifest = Path("data/ocr_benchmark/manifest.json")
    assert manifest.exists()
    data = run_manifest(manifest)
    assert data["aggregate"]["count"] >= 1
    assert "overall_score" in data["aggregate"]
    assert isinstance(data["samples"], list)

