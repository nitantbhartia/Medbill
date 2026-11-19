import json
import shutil

import accuracy_gate


def suites(tmp_path):
    shutil.copytree("data/ocr_benchmark", tmp_path / "bench")
    return [("synthetic", str(tmp_path / "bench/manifest.json"), str(tmp_path / "bench/baseline.json"))]


def test_gate_passes_against_its_own_baseline_and_fails_when_predictions_get_worse(tmp_path):
    chosen = suites(tmp_path)
    assert accuracy_gate.run_gate(chosen, accept=True) == []
    assert accuracy_gate.run_gate(chosen) == []
    prediction = tmp_path / "bench/sample_clean_1.pred.json"
    data = json.loads(prediction.read_text())
    for item in data["line_items"]:
        item["charged_amount"] = (item.get("charged_amount") or 0) + 7.77
    prediction.write_text(json.dumps(data))
    failures = accuracy_gate.run_gate(chosen)
    assert failures and "amount_accuracy dropped" in failures[0]


def test_a_missing_golden_set_is_skipped_not_an_error(tmp_path):
    assert accuracy_gate.run_gate([("golden", str(tmp_path / "none.json"), str(tmp_path / "b.json"))]) == []
