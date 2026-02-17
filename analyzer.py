import json
import logging

from db import get_db
from validators.pricing import check_pricing, get_medicare_locality, get_medicare_rate, validate_geo_match
from validators.duplicates import find_duplicates
from validators.unbundling import check_unbundling
from validators.upcoding import check_upcoding
from validators.nsa import check_no_surprises_act
from validators.extraction import validate_extraction, validate_cpt_description
from validators.benchmarks import check_benchmark
from data_freshness import get_data_freshness_warnings, get_data_freshness

log = logging.getLogger(__name__)

SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2, "informational": 3}

# Confidence scoring rules for findings
CONFIDENCE_RULES = {
    "duplicate_charge": "high",  # same code, date, amount — very reliable
    "price_markup": None,  # depends on markup level
    "unbundling": None,  # depends on modifier indicator
    "upcoding": "medium",  # can't confirm without medical record
    "quantity_flag": "low",  # might be correct
    "no_surprises_act": "low",  # needs more context to confirm
    "benchmark_outlier": "medium",  # statistical comparison, informational
}


def _assign_confidence(finding: dict) -> str:
    """Assign a confidence level to a finding based on type and details."""
    if finding.get("evidence_level") == "low":
        return "low"

    ftype = finding.get("type")

    if ftype == "duplicate_charge":
        return "high"

    if ftype == "price_markup":
        markup = finding.get("markup_multiple", 0)
        if markup > 5:
            return "high"
        return "medium"

    if ftype == "unbundling":
        mod = finding.get("modifier_indicator")
        if mod == "0":
            return "high"
        if mod == "1":
            return "medium"
        return "medium"

    if ftype == "upcoding":
        return "medium"

    if ftype == "benchmark_outlier":
        return "medium"

    return "low"


def _downgrade_severity(severity: str) -> str:
    if severity == "high":
        return "medium"
    if severity == "medium":
        return "low"
    if severity == "low":
        return "informational"
    return severity


def _sum_patient_responsibility(items: list[dict]) -> float | None:
    values = []
    for it in items:
        val = it.get("patient_responsibility")
        if val is not None:
            values.append(float(val))
    if not values:
        return None
    return max(0.0, round(sum(values), 2))


def _apply_patient_impact_savings(finding: dict, bill_patient_owes: float | None) -> None:
    """Convert raw savings into patient-impact estimate when possible."""
    gross = float(finding.get("potential_savings") or 0.0)
    finding["gross_potential_savings"] = round(gross, 2)

    line_items = []
    if isinstance(finding.get("line_item"), dict):
        line_items.append(finding["line_item"])
    if isinstance(finding.get("related_items"), list):
        line_items.extend([i for i in finding["related_items"] if isinstance(i, dict)])

    patient_cap = _sum_patient_responsibility(line_items)
    if patient_cap is None and bill_patient_owes is not None:
        patient_cap = max(0.0, float(bill_patient_owes))

    if patient_cap is None:
        finding["estimated_patient_savings"] = round(gross, 2)
        return

    patient_est = min(gross, patient_cap)
    finding["estimated_patient_savings"] = round(patient_est, 2)
    finding["potential_savings"] = round(patient_est, 2)


def _apply_evidence_policy(finding: dict, freshness: dict) -> None:
    """Adjust severity when supporting evidence is sparse or stale."""
    ftype = finding.get("type")
    finding["evidence_level"] = "medium"

    if ftype == "benchmark_outlier":
        sample_size = int(finding.get("sample_size") or 0)
        if sample_size < 500:
            finding["evidence_level"] = "low"
            finding["severity"] = _downgrade_severity(finding.get("severity", "low"))
            finding["message"] += " Benchmark sample size is limited for this comparison."
        elif sample_size >= 2000:
            finding["evidence_level"] = "high"

    if ftype == "upcoding":
        # Without clinical documentation, this should remain a softer signal.
        finding["evidence_level"] = "low"
        finding["severity"] = _downgrade_severity(finding.get("severity", "medium"))
        finding["message"] += " This is an informational flag and requires chart-level review."

    stale_rate_data = not freshness.get("medicare_pfs", {}).get("fresh", True)
    stale_ncci = not freshness.get("ncci_edits", {}).get("fresh", True)
    if ftype in ("price_markup", "benchmark_outlier") and stale_rate_data:
        finding["evidence_level"] = "low"
        finding["severity"] = _downgrade_severity(finding.get("severity", "low"))
    if ftype == "unbundling" and stale_ncci:
        finding["evidence_level"] = "low"
        finding["severity"] = _downgrade_severity(finding.get("severity", "low"))


def analyze_bill(extracted_data: dict, zip_code: str) -> dict:
    """
    Run all analysis checks against extracted bill data.
    Returns findings sorted by severity, with confidence scoring,
    extraction validation, geo checks, and data freshness warnings.
    """
    findings = []
    warnings = []
    total_potential_savings = 0.0
    locality = get_medicare_locality(zip_code, extracted_data.get("provider_address"))
    freshness = get_data_freshness()

    line_items = extracted_data.get("line_items", [])

    # Pre-analysis: validate extraction quality
    extraction_issues = validate_extraction(extracted_data)
    if extraction_issues:
        warnings.extend(extraction_issues)

    # Pre-analysis: geo match check
    geo_warning = validate_geo_match(zip_code, extracted_data.get("provider_address"))
    if geo_warning:
        warnings.append(geo_warning)

    # Pre-analysis: data freshness check
    dos_dates = [item.get("date_of_service") for item in line_items if item.get("date_of_service")]
    if dos_dates:
        freshness_warnings = get_data_freshness_warnings(dos_dates[0])
        warnings.extend(freshness_warnings)

    # Pre-analysis: CPT description cross-check
    for item in line_items:
        if item.get("cpt_code") and item.get("description"):
            if not validate_cpt_description(item["cpt_code"], item["description"]):
                warnings.append(
                    f"CPT {item['cpt_code']} description doesn't match our records "
                    f"for '{item['description']}'. The code may be misread."
                )

    for item in line_items:
        # CHECK 1: Price vs Medicare rate
        pricing_finding = check_pricing(item, locality)
        if pricing_finding:
            _apply_evidence_policy(pricing_finding, freshness)
            _apply_patient_impact_savings(pricing_finding, extracted_data.get("total_patient_owes"))
            findings.append(pricing_finding)
            total_potential_savings += pricing_finding["potential_savings"]

        # CHECK 2: Duplicate charges
        dup_finding = find_duplicates(item, line_items)
        if dup_finding:
            _apply_evidence_policy(dup_finding, freshness)
            _apply_patient_impact_savings(dup_finding, extracted_data.get("total_patient_owes"))
            findings.append(dup_finding)
            total_potential_savings += dup_finding["potential_savings"]

        # CHECK 3: Unbundling detection
        unbundle_finding = check_unbundling(item, line_items)
        if unbundle_finding:
            _apply_evidence_policy(unbundle_finding, freshness)
            _apply_patient_impact_savings(unbundle_finding, extracted_data.get("total_patient_owes"))
            findings.append(unbundle_finding)
            total_potential_savings += unbundle_finding["potential_savings"]

        # CHECK 4: Upcoding detection
        upcode_finding = check_upcoding(item)
        if upcode_finding:
            _apply_evidence_policy(upcode_finding, freshness)
            _apply_patient_impact_savings(upcode_finding, extracted_data.get("total_patient_owes"))
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
            _apply_evidence_policy(findings[-1], freshness)
            _apply_patient_impact_savings(findings[-1], extracted_data.get("total_patient_owes"))
            total_potential_savings += findings[-1]["potential_savings"]

        # CHECK 6: Regional benchmark comparison
        benchmark_finding = check_benchmark(item, zip_code, extracted_data.get("provider_address"))
        if benchmark_finding:
            _apply_evidence_policy(benchmark_finding, freshness)
            _apply_patient_impact_savings(benchmark_finding, extracted_data.get("total_patient_owes"))
            findings.append(benchmark_finding)
            total_potential_savings += benchmark_finding["potential_savings"]

    # CHECK 7: No Surprises Act
    nsa_finding = check_no_surprises_act(extracted_data)
    if nsa_finding:
        _apply_evidence_policy(nsa_finding, freshness)
        _apply_patient_impact_savings(nsa_finding, extracted_data.get("total_patient_owes"))
        findings.append(nsa_finding)
        total_potential_savings += nsa_finding.get("potential_savings", 0)

    bill_patient_owes = extracted_data.get("total_patient_owes")
    if bill_patient_owes is not None:
        total_potential_savings = min(total_potential_savings, float(bill_patient_owes))

    # Assign confidence to each finding
    for finding in findings:
        finding["confidence"] = _assign_confidence(finding)

    findings.sort(key=lambda f: SEVERITY_ORDER.get(f.get("severity", "low"), 2))

    return {
        "total_findings": len(findings),
        "total_potential_savings": round(total_potential_savings, 2),
        "total_gross_potential_savings": round(
            sum(float(f.get("gross_potential_savings", f.get("potential_savings", 0) or 0)) for f in findings), 2
        ),
        "findings": findings,
        "warnings": warnings,
        "bill_total": extracted_data.get("total_charged"),
        "patient_owes": extracted_data.get("total_patient_owes"),
    }


def save_bill_and_findings(user_id: int | None, extracted: dict, analysis: dict, zip_code: str = "") -> int:
    """Persist a scanned bill, its line items, and findings to the database."""
    with get_db() as db:
        cursor = db.execute(
            "INSERT INTO bills (user_id, provider_name, provider_address, bill_date, zip_code, "
            "total_charged, total_patient_owes, total_findings, total_potential_savings, status) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'analyzed')",
            (
                user_id,
                extracted.get("provider_name"),
                extracted.get("provider_address"),
                extracted.get("bill_date"),
                zip_code,
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
            "COALESCE(AVG(total_potential_savings), 0) as avg_savings, "
            "(SELECT COALESCE(SUM(actual_savings), 0) FROM dispute_outcomes) as realized_savings, "
            "(SELECT COUNT(*) FROM dispute_outcomes) as dispute_outcomes_count "
            "FROM bills WHERE total_findings > 0"
        ).fetchone()
    return dict(row)


def get_effectiveness_metrics() -> dict:
    """
    Evaluate historical finding effectiveness using dispute outcomes.
    Precision here is a proxy: percentage of outcomes with realized savings.
    """
    with get_db() as db:
        overall = db.execute(
            "SELECT "
            "COUNT(DISTINCT d.id) AS outcomes, "
            "SUM(CASE WHEN COALESCE(d.actual_savings, d.original_patient_owes - d.final_patient_owes, 0) > 0 "
            "THEN 1 ELSE 0 END) AS successful_outcomes, "
            "COALESCE(AVG(CASE WHEN d.original_patient_owes > 0 "
            "THEN COALESCE(d.actual_savings, d.original_patient_owes - d.final_patient_owes, 0) / d.original_patient_owes "
            "END), 0) AS avg_recovery_rate "
            "FROM dispute_outcomes d"
        ).fetchone()

        by_type = db.execute(
            "SELECT f.finding_type, "
            "COUNT(DISTINCT d.id) AS outcomes, "
            "SUM(CASE WHEN COALESCE(d.actual_savings, d.original_patient_owes - d.final_patient_owes, 0) > 0 "
            "THEN 1 ELSE 0 END) AS successful_outcomes, "
            "COALESCE(AVG(CASE WHEN d.original_patient_owes > 0 "
            "THEN COALESCE(d.actual_savings, d.original_patient_owes - d.final_patient_owes, 0) / d.original_patient_owes "
            "END), 0) AS avg_recovery_rate "
            "FROM dispute_outcomes d "
            "JOIN findings f ON f.bill_id = d.bill_id "
            "GROUP BY f.finding_type "
            "ORDER BY outcomes DESC"
        ).fetchall()

    overall_dict = dict(overall)
    outcomes = int(overall_dict.get("outcomes") or 0)
    success = int(overall_dict.get("successful_outcomes") or 0)
    precision = (success / outcomes) if outcomes else 0.0
    overall_dict["precision_proxy"] = round(precision, 4)

    type_metrics = []
    for row in by_type:
        d = dict(row)
        o = int(d.get("outcomes") or 0)
        s = int(d.get("successful_outcomes") or 0)
        d["precision_proxy"] = round((s / o), 4) if o else 0.0
        type_metrics.append(d)

    return {"overall": overall_dict, "by_finding_type": type_metrics}
