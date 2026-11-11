"""Turn a bill's findings into one row per charge for the results page.

One charge often triggers several findings (a markup, an upcoding flag and a regional
benchmark for the same ER visit). Each finding reports savings for that same charge, so
adding them up overstates what the patient can save. Here each charge counts once, at its
largest single estimate, and the total never exceeds what the patient owes."""

from __future__ import annotations

_SEVERITY_RANK = {"high": 3, "medium": 2, "low": 1, "informational": 0}

# Within one charge, the clearest errors lead: a duplicate beats a price comparison
_TYPE_ORDER = ["duplicate_charge", "unbundling", "quantity_flag", "upcoding", "price_markup",
               "eob_mismatch", "no_surprises_act", "benchmark_outlier"]

REASON_LABELS = {
    "duplicate_charge": "Billed more than once",
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
            "description": item.get("description") or "Charge",
            "date": item.get("date_of_service"),
            "charged": item.get("charged_amount"),
            "medicare_rate": None,
            "markup": None,
            "savings": 0.0,
            "severity": "informational",
            "reasons": [],
            "finding_ids": [],
        })
        charge["finding_ids"].append(finding["id"])
        charge["savings"] = max(charge["savings"], float(finding.get("potential_savings") or 0))
        if details.get("medicare_rate") and not charge["medicare_rate"]:
            charge["medicare_rate"] = details["medicare_rate"]
            charge["markup"] = details.get("markup_multiple")
        severity = finding.get("severity") or "low"
        if _SEVERITY_RANK.get(severity, 0) > _SEVERITY_RANK[charge["severity"]]:
            charge["severity"] = severity
        if any(r["type"] == finding.get("finding_type") for r in charge["reasons"]):
            continue
        charge["reasons"].append({
            "type": finding.get("finding_type"),
            "label": REASON_LABELS.get(finding.get("finding_type"), (finding.get("finding_type") or "Flagged").replace("_", " ").capitalize()),
            "message": finding.get("message") or "",
            "severity": severity,
        })

    rows = sorted(charges.values(), key=lambda c: (-_SEVERITY_RANK[c["severity"]], -c["savings"]))
    for row in rows:
        row["reasons"].sort(key=lambda r: (
            -_SEVERITY_RANK.get(r["severity"], 0),
            _TYPE_ORDER.index(r["type"]) if r["type"] in _TYPE_ORDER else len(_TYPE_ORDER),
        ))
        row["strong"] = row["severity"] in ("high", "medium")
    total = sum(row["savings"] for row in rows)
    if amount_owed:
        total = min(total, amount_owed)
    return {
        "charges": rows,
        "total_savings": round(total, 2),
        "strong_count": sum(1 for row in rows if row["strong"]),
    }
