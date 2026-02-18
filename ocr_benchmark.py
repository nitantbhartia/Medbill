"""OCR benchmark harness for field-level extraction quality."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path


def _norm_text(value) -> str:
    if value is None:
        return ""
    text = str(value).strip().lower()
    text = re.sub(r"\s+", " ", text)
    return text


def _norm_amount(value) -> float | None:
    if value is None:
        return None
    try:
        return round(float(value), 2)
    except (TypeError, ValueError):
        return None


@dataclass
class ScoreResult:
    provider_name_accuracy: float
    total_charged_accuracy: float
    line_match_rate: float
    cpt_accuracy: float
    amount_accuracy: float
    overall_score: float


def score_extraction(pred: dict, truth: dict) -> ScoreResult:
    provider_ok = _norm_text(pred.get("provider_name")) == _norm_text(truth.get("provider_name"))
    total_ok = _norm_amount(pred.get("total_charged")) == _norm_amount(truth.get("total_charged"))

    pred_items = list(pred.get("line_items") or [])
    truth_items = list(truth.get("line_items") or [])
    if not truth_items:
        return ScoreResult(
            provider_name_accuracy=float(provider_ok),
            total_charged_accuracy=float(total_ok),
            line_match_rate=1.0,
            cpt_accuracy=1.0,
            amount_accuracy=1.0,
            overall_score=1.0,
        )

    matched = 0
    cpt_hits = 0
    amount_hits = 0
    for i, t in enumerate(truth_items):
        if i >= len(pred_items):
            continue
        p = pred_items[i]
        matched += 1
        if _norm_text(p.get("cpt_code")) == _norm_text(t.get("cpt_code")):
            cpt_hits += 1
        if _norm_amount(p.get("charged_amount")) == _norm_amount(t.get("charged_amount")):
            amount_hits += 1

    line_rate = matched / len(truth_items)
    cpt_rate = cpt_hits / len(truth_items)
    amount_rate = amount_hits / len(truth_items)
    overall = (
        0.15 * float(provider_ok)
        + 0.15 * float(total_ok)
        + 0.2 * line_rate
        + 0.25 * cpt_rate
        + 0.25 * amount_rate
    )

    return ScoreResult(
        provider_name_accuracy=float(provider_ok),
        total_charged_accuracy=float(total_ok),
        line_match_rate=round(line_rate, 4),
        cpt_accuracy=round(cpt_rate, 4),
        amount_accuracy=round(amount_rate, 4),
        overall_score=round(overall, 4),
    )


def run_manifest(manifest_path: str | Path) -> dict:
    manifest_file = Path(manifest_path)
    payload = json.loads(manifest_file.read_text())
    root = manifest_file.parent
    rows = []
    for sample in payload.get("samples", []):
        truth = json.loads((root / sample["truth_json"]).read_text())
        pred = json.loads((root / sample["prediction_json"]).read_text())
        score = score_extraction(pred, truth)
        rows.append(
            {
                "id": sample["id"],
                "provider_name_accuracy": score.provider_name_accuracy,
                "total_charged_accuracy": score.total_charged_accuracy,
                "line_match_rate": score.line_match_rate,
                "cpt_accuracy": score.cpt_accuracy,
                "amount_accuracy": score.amount_accuracy,
                "overall_score": score.overall_score,
            }
        )

    avg = lambda key: round(sum(r[key] for r in rows) / len(rows), 4) if rows else 0.0
    return {
        "samples": rows,
        "aggregate": {
            "count": len(rows),
            "provider_name_accuracy": avg("provider_name_accuracy"),
            "total_charged_accuracy": avg("total_charged_accuracy"),
            "line_match_rate": avg("line_match_rate"),
            "cpt_accuracy": avg("cpt_accuracy"),
            "amount_accuracy": avg("amount_accuracy"),
            "overall_score": avg("overall_score"),
        },
    }
