"""OCR benchmark harness for field-level extraction quality."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
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

    cpt_hits = 0
    amount_hits = 0
    line_hits = 0
    unused = list(pred_items)
    for t in truth_items:
        same_cpt = [p for p in unused if _norm_text(p.get("cpt_code")) == _norm_text(t.get("cpt_code"))]
        if not same_cpt:
            continue
        cpt_hits += 1
        exact = [p for p in same_cpt if _norm_amount(p.get("charged_amount")) == _norm_amount(t.get("charged_amount"))]
        if not exact:
            unused.remove(same_cpt[0])
            continue
        amount_hits += 1
        line_hits += 1
        unused.remove(exact[0])

    line_rate = line_hits / len(truth_items)
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


def run_live(truth_jsonl: str | Path, extract) -> dict:
    """Run `extract(image_bytes, mime_type) -> dict` over every file in a ground-truth JSONL and score it."""
    truth_file = Path(truth_jsonl)
    rows = []
    for line in truth_file.read_text().splitlines():
        truth = json.loads(line)
        image_path = truth_file.parent / truth["file"]
        mime_type = "application/pdf" if image_path.suffix == ".pdf" else f"image/{image_path.suffix.lstrip('.')}"
        score = score_extraction(extract(image_path.read_bytes(), mime_type), truth)
        rows.append({"id": image_path.stem, **asdict(score)})
    return _summarize(rows)


def _summarize(rows: list[dict]) -> dict:
    avg = lambda key: round(sum(r[key] for r in rows) / len(rows), 4) if rows else 0.0
    keys = ("provider_name_accuracy", "total_charged_accuracy", "line_match_rate", "cpt_accuracy", "amount_accuracy", "overall_score")
    return {"samples": rows, "aggregate": {"count": len(rows), **{k: avg(k) for k in keys}}}


def run_manifest(manifest_path: str | Path) -> dict:
    manifest_file = Path(manifest_path)
    payload = json.loads(manifest_file.read_text())
    root = manifest_file.parent
    rows = []
    for sample in payload.get("samples", []):
        truth = json.loads((root / sample["truth_json"]).read_text())
        pred = json.loads((root / sample["prediction_json"]).read_text())
        rows.append({"id": sample["id"], **asdict(score_extraction(pred, truth))})
    return _summarize(rows)
