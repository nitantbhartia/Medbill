import json
import logging

from db import get_db
from validators.pricing import check_pricing, get_medicare_locality, get_medicare_rate
from validators.duplicates import find_duplicates
from validators.unbundling import check_unbundling
from validators.upcoding import check_upcoding
from validators.nsa import check_no_surprises_act

log = logging.getLogger(__name__)

SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def analyze_bill(extracted_data: dict, zip_code: str) -> dict:
    """
    Run all analysis checks against extracted bill data.
    Returns findings sorted by severity.
    """
    findings = []
    total_potential_savings = 0.0
    locality = get_medicare_locality(zip_code)

    line_items = extracted_data.get("line_items", [])

    for item in line_items:
        # CHECK 1: Price vs Medicare rate
        pricing_finding = check_pricing(item, locality)
        if pricing_finding:
            findings.append(pricing_finding)
            total_potential_savings += pricing_finding["potential_savings"]

        # CHECK 2: Duplicate charges
        dup_finding = find_duplicates(item, line_items)
        if dup_finding:
            findings.append(dup_finding)
            total_potential_savings += dup_finding["potential_savings"]

        # CHECK 3: Unbundling detection
        unbundle_finding = check_unbundling(item, line_items)
        if unbundle_finding:
            findings.append(unbundle_finding)
            total_potential_savings += unbundle_finding["potential_savings"]

        # CHECK 4: Upcoding detection
        upcode_finding = check_upcoding(item)
        if upcode_finding:
            findings.append(upcode_finding)
            total_potential_savings += upcode_finding["potential_savings"]

        # CHECK 5: Quantity flags
        if item.get("quantity") and item["quantity"] > 1 and item.get("charged_amount"):
            extra = item["charged_amount"] * (item["quantity"] - 1) / item["quantity"]
            findings.append(
                {
                    "type": "quantity_flag",
                    "severity": "low",
                    "line_item": item,
                    "potential_savings": round(extra, 2),
                    "message": (
                        f"You were billed for {item['quantity']} units of "
                        f"'{item['description']}'. If only 1 was administered, "
                        f"the extra units add ${extra:,.2f}."
                    ),
                }
            )

    # CHECK 6: No Surprises Act
    nsa_finding = check_no_surprises_act(extracted_data)
    if nsa_finding:
        findings.append(nsa_finding)
        total_potential_savings += nsa_finding.get("potential_savings", 0)

    findings.sort(key=lambda f: SEVERITY_ORDER.get(f.get("severity", "low"), 2))

    return {
        "total_findings": len(findings),
        "total_potential_savings": round(total_potential_savings, 2),
        "findings": findings,
        "bill_total": extracted_data.get("total_charged"),
        "patient_owes": extracted_data.get("total_patient_owes"),
    }


def save_bill_and_findings(user_id: int | None, extracted: dict, analysis: dict) -> int:
    """Persist a scanned bill, its line items, and findings to the database."""
    with get_db() as db:
        cursor = db.execute(
            "INSERT INTO bills (user_id, provider_name, provider_address, bill_date, "
            "total_charged, total_patient_owes, total_findings, total_potential_savings, status) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'analyzed')",
            (
                user_id,
                extracted.get("provider_name"),
                extracted.get("provider_address"),
                extracted.get("bill_date"),
                extracted.get("total_charged"),
                extracted.get("total_patient_owes"),
                analysis["total_findings"],
                analysis["total_potential_savings"],
            ),
        )
        bill_id = cursor.lastrowid

        for item in extracted.get("line_items", []):
            medicare_rate = get_medicare_rate(item.get("cpt_code", "")) if item.get("cpt_code") else None
            markup = (
                round(item["charged_amount"] / medicare_rate, 2)
                if medicare_rate and item.get("charged_amount")
                else None
            )
            db.execute(
                "INSERT INTO line_items (bill_id, date_of_service, cpt_code, description, "
                "quantity, charged_amount, insurance_paid, insurance_adjustment, "
                "patient_responsibility, medicare_rate, markup_multiple, extraction_confidence) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    bill_id,
                    item.get("date_of_service"),
                    item.get("cpt_code"),
                    item.get("description"),
                    item.get("quantity", 1),
                    item.get("charged_amount"),
                    item.get("insurance_paid"),
                    item.get("insurance_adjustment"),
                    item.get("patient_responsibility"),
                    medicare_rate,
                    markup,
                    item.get("confidence", "high"),
                ),
            )
            line_item_id = cursor.lastrowid

        for finding in analysis.get("findings", []):
            db.execute(
                "INSERT INTO findings (bill_id, finding_type, severity, "
                "potential_savings, message, details) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    bill_id,
                    finding["type"],
                    finding["severity"],
                    finding.get("potential_savings", 0),
                    finding["message"],
                    json.dumps(finding),
                ),
            )

    return bill_id


def get_bill_results(bill_id: int) -> dict | None:
    """Load a bill and its findings from the database."""
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            return None

        line_items = db.execute(
            "SELECT * FROM line_items WHERE bill_id = ? ORDER BY id", (bill_id,)
        ).fetchall()

        findings = db.execute(
            "SELECT * FROM findings WHERE bill_id = ? ORDER BY "
            "CASE severity WHEN 'high' THEN 0 WHEN 'medium' THEN 1 ELSE 2 END",
            (bill_id,),
        ).fetchall()

    return {
        "bill": dict(bill),
        "line_items": [dict(li) for li in line_items],
        "findings": [dict(f) for f in findings],
    }


def get_stats() -> dict:
    """Get aggregate stats for the live counter."""
    with get_db() as db:
        row = db.execute(
            "SELECT COUNT(*) as bills_scanned, "
            "COALESCE(SUM(total_potential_savings), 0) as total_found, "
            "COALESCE(AVG(total_potential_savings), 0) as avg_savings "
            "FROM bills WHERE total_findings > 0"
        ).fetchone()
    return dict(row)
