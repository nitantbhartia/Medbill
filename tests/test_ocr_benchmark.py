import json
from pathlib import Path

import config
from ocr_benchmark import run_live, run_manifest, score_extraction


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



def test_score_ignores_line_order_and_penalizes_wrong_amount():
    truth = {"provider_name": "A", "total_charged": 300.0, "line_items": [
        {"cpt_code": "99214", "charged_amount": 186.54}, {"cpt_code": "71046", "charged_amount": 113.46}]}
    pred = {"provider_name": "A", "total_charged": 300.0, "line_items": [
        {"cpt_code": "71046", "charged_amount": 113.0}, {"cpt_code": "99214", "charged_amount": 186.54}]}
    result = score_extraction(pred, truth)
    assert result.cpt_accuracy == 1.0
    assert result.amount_accuracy == 0.5


def test_run_live_scores_synthetic_baseline_with_perfect_extractor():
    truth_by_file = {}
    for line in Path(config.OCR_BENCHMARK_TRUTH_FILE).read_text().splitlines():
        row = json.loads(line)
        truth_by_file[row["file"]] = row

    calls = iter(truth_by_file.values())
    result = run_live(config.OCR_BENCHMARK_TRUTH_FILE, lambda image_bytes, mime: next(calls))
    assert result["aggregate"]["count"] == 18
    assert result["aggregate"]["overall_score"] == 1.0
