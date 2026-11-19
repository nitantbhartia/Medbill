"""Turn a bill's findings into one row per charge for the results page.

One charge often triggers several findings (a markup, an upcoding flag and a regional
benchmark for the same ER visit). Each finding reports savings for that same charge, so
adding them up overstates what the patient can save. Here each charge counts once, at its
largest single estimate and never more than the charge itself, and the total never exceeds
what the patient owes."""

from __future__ import annotations

_SEVERITY_RANK = {"high": 3, "medium": 2, "low": 1, "informational": 0}

# Within one charge, the clearest errors lead: a duplicate beats a price comparison
_TYPE_ORDER = ["duplicate_charge", "unbundling", "quantity_flag", "insurer_rate", "upcoding", "price_markup",
               "eob_mismatch", "no_surprises_act", "benchmark_outlier"]

from analyzer import RULE_ID_BY_TYPE
from es_content import REASON_LABELS_ES
from rule_sources import basis_for, reply_for

# Objectively wrong on the bill itself. Everything else compares a price with a benchmark, which a
# hospital can reasonably decline to act on, so it is reported separately and never as "errors".
ERROR_TYPES = {"duplicate_charge", "unbundling", "quantity_flag", "eob_mismatch"}

# Findings that are questions or information, not errors: $0 in every total and never "strong". An ER level needs the
# medical record to prove, so it is never strong either.
NOTE_TYPES = {"quantity_question", "upcoding", "price_info"}

REASON_LABELS = {
    "quantity_question": "Quantity worth asking about",
    "price_info": "High list price, already discounted by your insurer",
    "duplicate_charge": "Billed more than once",
    "insurer_rate": "Above your insurer's contracted rate",
    "price_markup": "Far above what Medicare pays",
    "upcoding": "Visit level may be higher than the care",
    "unbundling": "Billed separately from a test that includes it",
    "quantity_flag": "Quantity looks wrong",
    "benchmark_outlier": "Above the typical charge in your region",
    "eob_mismatch": "Doesn't match your insurer's statement",
    "no_surprises_act": "May be protected by the No Surprises Act",
}


def _line_item(finding: dict) -> dict:
    details = finding.get("parsed_details") or {}
    return details.get("line_item") or {}


def _charge_key(finding: dict) -> tuple:
    item = _line_item(finding)
    return (item.get("cpt_code"), item.get("description"), item.get("date_of_service"), item.get("charged_amount"))


def group_findings_by_charge(findings: list[dict], amount_owed: float | None = None) -> dict:
    """Charges with their reasons, strongest first, plus a total that counts each charge once."""
    charges: dict[tuple, dict] = {}
    for finding in findings:
        key = _charge_key(finding)
        item = _line_item(finding)
        details = finding.get("parsed_details") or {}
        charge = charges.setdefault(key, {
            "code": item.get("cpt_code"),
            "description": item.get("description") or "The whole bill",
            "date": item.get("date_of_service"),
            "charged": item.get("charged_amount"),
            "medicare_rate": None,
            "markup": None,
            "savings": 0.0,
            "error_savings": 0.0,
            "markup_savings": 0.0,
            "severity": "informational",
            "reasons": [],
            "finding_ids": [],
            "not_checked": bool(item.get("needs_confirm")),
        })
        charge["finding_ids"].append(finding["id"])
        amount = 0.0 if finding.get("finding_type") in {"quantity_question", "price_info"} else float(finding.get("potential_savings") or 0)
        charge["savings"] = max(charge["savings"], amount)
        bucket = "error_savings" if finding.get("finding_type") in ERROR_TYPES else "markup_savings"
        charge[bucket] = max(charge[bucket], amount)
        if details.get("medicare_rate") and not charge["medicare_rate"]:
            charge["medicare_rate"] = details["medicare_rate"]
            charge["markup"] = details.get("markup_multiple")
        severity = finding.get("severity") or "low"
        if _SEVERITY_RANK.get(severity, 0) > _SEVERITY_RANK[charge["severity"]]:
            charge["severity"] = severity
        if any(r["type"] == finding.get("finding_type") for r in charge["reasons"]):
            continue
        basis = basis_for(finding.get("rule_id") or RULE_ID_BY_TYPE.get(finding.get("finding_type")), details)
        if basis and details.get("code_source_note"):
            basis = {**basis, "explanation": f"{basis['explanation']} {details['code_source_note']}"}
        charge["reasons"].append({
            "type": finding.get("finding_type"),
            "label_es": REASON_LABELS_ES.get(finding.get("finding_type"), ""),
            "label": REASON_LABELS.get(finding.get("finding_type"), (finding.get("finding_type") or "Flagged").replace("_", " ").capitalize()),
            "message": finding.get("message") or "",
            "severity": severity,
            "basis": basis,
            "hospital_may_say": (reply_for(details.get("innocent_reason")) or {}).get("may_say"),
            "say_back": (reply_for(details.get("innocent_reason")) or {}).get("say_back"),
        })

    rows = sorted(charges.values(), key=lambda c: (-_SEVERITY_RANK[c["severity"]], -c["savings"]))
    for row in rows:
        row["reasons"].sort(key=lambda r: (
            -_SEVERITY_RANK.get(r["severity"], 0),
            _TYPE_ORDER.index(r["type"]) if r["type"] in _TYPE_ORDER else len(_TYPE_ORDER),
        ))
        row["note_only"] = all(reason["type"] in NOTE_TYPES for reason in row["reasons"])
        row["strong"] = row["severity"] in ("high", "medium") and not row["not_checked"] and not row["note_only"]
        if row["charged"]:
            for key in ("savings", "error_savings", "markup_savings"):
                row[key] = min(row[key], float(row["charged"]))
        # Price comparisons only count for the part not already explained by an error on the same charge.
        row["markup_savings"] = max(row["markup_savings"] - row["error_savings"], 0.0)
    # A whole-bill finding (no line item) covers the same money as the line findings, so the
    # two are alternatives, not a sum.
    # A line the user skipped confirming is shown as "not checked" and left out of every total.
    counted = [row for row in rows if not row["not_checked"] and not row["note_only"]]
    line_total = sum(row["savings"] for row in counted if row["charged"])
    bill_total = sum(row["savings"] for row in counted if not row["charged"])
    total = max(line_total, bill_total)
    errors = sum(row["error_savings"] for row in counted if row["charged"])
    pricing = sum(row["markup_savings"] for row in counted if row["charged"])
    if amount_owed:
        total = min(total, amount_owed)
        errors = min(errors, amount_owed)
        pricing = min(pricing, max(amount_owed - errors, 0.0))
    # The headline claims errors when there are any. A price comparison alone is shown as that, not as errors.
    kind = "errors" if errors > 0 else "pricing"
    return {
        "charges": rows,
        "total_savings": round(total, 2),
        "error_savings": round(errors, 2),
        "markup_savings": round(pricing, 2),
        "headline_kind": kind,
        "headline_amount": round(errors if errors > 0 else total, 2),
        "strong_count": sum(1 for row in counted if row["strong"]),
        # Every finding is a price that an insurer already discounted: nothing for the patient to dispute.
        "info_only": bool(rows) and all(reason["type"] == "price_info" for row in rows for reason in row["reasons"]),
    }
