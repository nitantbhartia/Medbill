"""Before/after: re-run the analyzer with the B16 rule flags on, over stored bills and the benchmark bills, and compare
with what is stored. Nothing is written."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

import analyzer
import config
from charge_summary import group_findings_by_charge
from db import get_db

FLAGS = ("QUANTITY_RULE_V2", "ER_LEVEL_RULE_V2", "DUPLICATE_MODIFIERS", "INSURED_PRICE_INFO_ONLY")
BENCHMARK_DIR = Path("data/ocr_benchmark")


def stored_bills() -> list[dict]:
    """Every saved bill, rebuilt from its stored line items, with its stored findings."""
    bills = []
    with get_db() as db:
        for bill in db.execute("SELECT * FROM bills").fetchall():
            items = [dict(row) for row in db.execute("SELECT * FROM line_items WHERE bill_id = ? ORDER BY id", (bill["id"],))]
            findings = [dict(row) for row in db.execute("SELECT * FROM findings WHERE bill_id = ?", (bill["id"],))]
            bills.append({"id": f"bill-{bill['id']}", "bill": dict(bill), "line_items": items, "stored": findings})
    return bills


def benchmark_bills() -> list[dict]:
    """The benchmark truth files have no stored findings: they are analyzed as if never flagged, so everything shows as added."""
    bills = []
    for truth in sorted(BENCHMARK_DIR.glob("*.truth.json")):
        data = json.loads(truth.read_text())
        bills.append({"id": truth.stem.replace(".truth", ""), "bill": data, "line_items": data.get("line_items", []), "stored": []})
    return bills


def _normalized(findings: list[dict]) -> list[dict]:
    return [{"id": i, "finding_type": f.get("finding_type") or f["type"], "rule_id": f.get("rule_id"), "severity": f.get("severity"),
             "potential_savings": f.get("potential_savings") or 0, "message": f.get("message") or "",
             "parsed_details": f if "type" in f else json.loads(f.get("details") or "{}")} for i, f in enumerate(findings)]


def headline(findings: list[dict], owed) -> float:
    return group_findings_by_charge(_normalized(findings), owed or None)["headline_amount"]


def _keyed(findings: list[dict]) -> dict:
    keys = defaultdict(list)
    for f in findings:
        item = (f.get("line_item") or json.loads(f.get("details") or "{}").get("line_item") or {})
        keys[(f.get("finding_type") or f["type"], item.get("cpt_code"), item.get("date_of_service"))].append(f)
    return {key: values[0] for key, values in keys.items()}


def diff_bill(entry: dict) -> tuple[list[dict], float, float]:
    bill = entry["bill"]
    extracted = {key: bill.get(key) for key in ("provider_name", "provider_address", "bill_date", "total_charged", "total_patient_owes", "insurer_name")}
    extracted["line_items"] = entry["line_items"]
    after = analyzer.analyze_bill(extracted, bill.get("zip_code") or "")["findings"]
    before_keyed, after_keyed = _keyed(entry["stored"]), _keyed(after)
    rows = []
    for key in sorted(set(before_keyed) | set(after_keyed), key=str):
        old, new = before_keyed.get(key), after_keyed.get(key)
        change = "added" if not old else "removed" if not new else "changed" if old.get("severity") != new.get("severity") else None
        if change:
            rows.append({"bill": entry["id"], "rule": key[0], "code": key[1], "change": change,
                         "severity_before": old.get("severity") if old else "", "severity_after": new.get("severity") if new else "",
                         "savings_before": (old or {}).get("potential_savings") or 0, "savings_after": (new or {}).get("potential_savings") or 0})
    owed = bill.get("total_patient_owes")
    return rows, headline(entry["stored"], owed) if entry["stored"] else 0.0, headline(after, owed)


def run(entries: list[dict], out_csv: str) -> dict:
    """Turns the flags on for the run, writes the per-bill CSV and returns the totals by rule."""
    saved = {flag: getattr(config, flag) for flag in FLAGS}
    for flag in FLAGS:
        setattr(config, flag, True)
    try:
        all_rows, before_total, after_total, by_rule = [], 0.0, 0.0, defaultdict(float)
        for entry in entries:
            rows, before, after = diff_bill(entry)
            for row in rows:
                row.update(headline_before=before, headline_after=after)
                by_rule[row["rule"]] += row["savings_after"] - row["savings_before"]
            all_rows += rows
            before_total, after_total = before_total + before, after_total + after
    finally:
        for flag, value in saved.items():
            setattr(config, flag, value)
    fields = ["bill", "rule", "code", "change", "severity_before", "severity_after", "savings_before", "savings_after", "headline_before", "headline_after"]
    with open(out_csv, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_rows)
    return {"bills": len(entries), "changes": len(all_rows), "headline_before": round(before_total, 2),
            "headline_after": round(after_total, 2), "savings_change_by_rule": dict(by_rule)}
