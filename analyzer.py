import json
import logging
import time

import config
from db import get_db
from validators.pricing import check_pricing, get_medicare_locality, get_medicare_rate, validate_geo_match
from validators.duplicates import find_duplicates
from validators.unbundling import check_unbundling
from validators.upcoding import check_upcoding
from validators.nsa import check_no_surprises_act
from validators.extraction import validate_extraction, validate_cpt_description
from validators.benchmarks import check_benchmark
from validators.eob import check_eob_reconciliation
from data_freshness import get_data_freshness_warnings, get_data_freshness

log = logging.getLogger(__name__)


def merge_eob_into_extracted(extracted: dict, eob_data: dict) -> dict:
    """
    Enrich bill extraction with insurance fields from an uploaded EOB.
    Matches by CPT first, then by line index fallback.
    """
    merged = dict(extracted or {})
    bill_items = list(merged.get("line_items") or [])
    eob_items = list((eob_data or {}).get("line_items") or [])
    if not bill_items or not eob_items:
        return merged

    eob_by_cpt: dict[str, list[tuple[int, dict]]] = {}
    for i, row in enumerate(eob_items):
        code = (row.get("cpt_code") or "").strip()
        if not code:
            continue
        eob_by_cpt.setdefault(code, []).append((i, row))

    used_indices: set[int] = set()
    for idx, item in enumerate(bill_items):
        candidate = None
        code = (item.get("cpt_code") or "").strip()
        if code and eob_by_cpt.get(code):
            for eob_idx, eob in eob_by_cpt[code]:
                if eob_idx not in used_indices:
                    candidate = eob
                    used_indices.add(eob_idx)
                    break
        if candidate is None and idx < len(eob_items) and idx not in used_indices:
            candidate = eob_items[idx]

        if candidate is None:
            continue
        for fld in ("insurance_paid", "insurance_adjustment", "patient_responsibility"):
            if item.get(fld) is None and candidate.get(fld) is not None:
                item[fld] = candidate[fld]
        if item.get("date_of_service") is None and candidate.get("date_of_service"):
            item["date_of_service"] = candidate["date_of_service"]

    merged["line_items"] = bill_items
    merged["_eob_merge"] = {
        "bill_lines": len(bill_items),
        "eob_lines": len(eob_items),
    }
    return merged


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
    "eob_mismatch": "high",  # arithmetic consistency check
}

RULE_ID_BY_TYPE = {
    "duplicate_charge": "RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT",
    "price_markup": "RULE_MARKUP_VS_MEDICARE",
    "unbundling": "RULE_NCCI_UNBUNDLING",
    "upcoding": "RULE_ER_LEVEL_UPCODING_HEURISTIC",
    "quantity_flag": "RULE_HIGH_QUANTITY_CHECK",
    "no_surprises_act": "RULE_NO_SURPRISES_ACT_HEURISTIC",
    "benchmark_outlier": "RULE_REGIONAL_BENCHMARK_OUTLIER",
    "eob_mismatch": "RULE_EOB_RECONCILIATION",
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

    if ftype == "eob_mismatch":
        return "high"

    return "low"


def _get_outcome_precision_by_type() -> dict:
    with get_db() as db:
        rows = db.execute(
            "SELECT f.finding_type, "
            "COUNT(DISTINCT d.id) AS outcomes, "
            "SUM(CASE WHEN COALESCE(d.actual_savings, d.original_patient_owes - d.final_patient_owes, 0) > 0 "
            "THEN 1 ELSE 0 END) AS successes "
            "FROM findings f "
            "JOIN dispute_outcomes d ON d.bill_id = f.bill_id "
            "GROUP BY f.finding_type"
        ).fetchall()
    precision = {}
    for row in rows:
        outcomes = int(row["outcomes"] or 0)
        successes = int(row["successes"] or 0)
        precision[row["finding_type"]] = (successes / outcomes) if outcomes else 0.0
    return precision


_adaptive_cache: dict = {}
_adaptive_cache_ts: float = 0.0


def _invalidate_adaptive_cache() -> None:
    global _adaptive_cache_ts
    _adaptive_cache_ts = 0.0


def _get_adaptive_thresholds() -> dict:
    """
    Outcome loop v1: raise trigger thresholds slightly when precision is weak.
    Cached for ADAPTIVE_THRESHOLDS_CACHE_TTL_SECONDS to avoid a DB query per analysis.
    """
    global _adaptive_cache, _adaptive_cache_ts
    now = time.monotonic()
    if _adaptive_cache and (now - _adaptive_cache_ts) < config.ADAPTIVE_THRESHOLDS_CACHE_TTL_SECONDS:
        return _adaptive_cache

    precision = _get_outcome_precision_by_type()
    pricing_precision = precision.get("price_markup")
    benchmark_precision = precision.get("benchmark_outlier")

    pricing_markup_threshold = 3.0
    pricing_high_threshold = 5.0
    benchmark_multiplier = 1.0

    if pricing_precision is not None and pricing_precision < 0.35:
        pricing_markup_threshold = 3.5
        pricing_high_threshold = 5.5
    if benchmark_precision is not None and benchmark_precision < 0.35:
        benchmark_multiplier = 1.1

    _adaptive_cache = {
        "pricing_markup_threshold": pricing_markup_threshold,
        "pricing_high_threshold": pricing_high_threshold,
        "benchmark_multiplier": benchmark_multiplier,
        "precision_by_type": precision,
    }
    _adaptive_cache_ts = now
    return _adaptive_cache


def _ensure_evidence_panel(finding: dict, freshness: dict) -> None:
    """
    Standard evidence object for UI evidence panels.
    """
    existing = finding.get("evidence") if isinstance(finding.get("evidence"), dict) else {}
    source = existing.get("source")
    if not source:
        source = {
            "price_markup": "cms_medicare_pfs_opps",
            "benchmark_outlier": "regional_benchmark_dataset",
            "unbundling": "cms_ncci_ptp",
            "duplicate_charge": "line_item_identity_match",
            "upcoding": "er_level_heuristic",
            "quantity_flag": "line_item_quantity_check",
            "no_surprises_act": "nsa_rule_heuristic",
            "eob_mismatch": "insurance_reconciliation",
        }.get(finding.get("type"), "internal_rule")

    data_date = (
        str(freshness.get("medicare_pfs", {}).get("latest_year"))
        if source in ("cms_medicare_pfs_opps", "cms_ncci_ptp")
        else None
    )
    sample_size = existing.get("sample_size", finding.get("sample_size"))
    limitations = existing.get("limitations")
    if not limitations:
        limitations = "This finding may need human review and source document confirmation."

    finding["evidence"] = {
        "source": source,
        "data_date": data_date,
        "sample_size": sample_size,
        "confidence": finding.get("confidence"),
        "limitations": limitations,
        "source_anchor": (finding.get("line_item") or {}).get("source_anchor"),
    }


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


def _prorate_patient_responsibility(extracted_data: dict) -> None:
    """Fill missing per-line patient_responsibility from bill-level total_patient_owes.

    Most hospital bills show a "you owe" total but not per-line patient shares.
    Without this, savings are computed against the full charge instead of what the
    patient actually owes. Proration assigns each line item a share proportional
    to its charged_amount.
    """
    line_items = extracted_data.get("line_items", [])
    total_patient_owes = extracted_data.get("total_patient_owes")
    if not line_items or not total_patient_owes:
        return

    total_patient_owes = float(total_patient_owes)
    if total_patient_owes <= 0:
        return

    # Skip if any line already has patient_responsibility — the data is already present
    has_any = any(item.get("patient_responsibility") is not None for item in line_items)
    if has_any:
        return

    total_charged = sum(float(item.get("charged_amount") or 0) for item in line_items)
    if total_charged <= 0:
        return

    for item in line_items:
        charged = float(item.get("charged_amount") or 0)
        if charged > 0:
            item["patient_responsibility"] = round(
                total_patient_owes * (charged / total_charged), 2
            )
            item["_patient_resp_prorated"] = True


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
    adaptive = _get_adaptive_thresholds()

    line_items = extracted_data.get("line_items", [])

    # Prorate bill-level patient_owes to line items so savings are patient-centric
    _prorate_patient_responsibility(extracted_data)

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
        pricing_finding = check_pricing(
            item,
            locality,
            markup_threshold=adaptive["pricing_markup_threshold"],
            high_markup_threshold=adaptive["pricing_high_threshold"],
        )
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
        benchmark_finding = check_benchmark(
            item,
            zip_code,
            extracted_data.get("provider_address"),
            percentile_multiplier=adaptive["benchmark_multiplier"],
        )
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

    # CHECK 8: EOB math reconciliation
    eob_findings = check_eob_reconciliation(extracted_data)
    for eob_finding in eob_findings:
        _apply_evidence_policy(eob_finding, freshness)
        _apply_patient_impact_savings(eob_finding, extracted_data.get("total_patient_owes"))
        findings.append(eob_finding)
        total_potential_savings += eob_finding.get("potential_savings", 0)

    bill_patient_owes = extracted_data.get("total_patient_owes")
    if bill_patient_owes is not None:
        total_potential_savings = min(total_potential_savings, float(bill_patient_owes))

    # Assign confidence to each finding
    for finding in findings:
        finding["rule_id"] = RULE_ID_BY_TYPE.get(finding.get("type"), "RULE_GENERIC_HEURISTIC")
        finding["confidence"] = _assign_confidence(finding)
        _ensure_evidence_panel(finding, freshness)

    findings.sort(key=lambda f: SEVERITY_ORDER.get(f.get("severity", "low"), 2))

    has_patient_data = any(
        item.get("patient_responsibility") is not None for item in line_items
    )
    savings_prorated = any(
        item.get("_patient_resp_prorated") for item in line_items
    )

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
        "has_patient_data": has_patient_data,
        "savings_prorated": savings_prorated,
        "adaptive_thresholds": {
            "pricing_markup_threshold": adaptive["pricing_markup_threshold"],
            "pricing_high_threshold": adaptive["pricing_high_threshold"],
            "benchmark_percentile_multiplier": adaptive["benchmark_multiplier"],
        },
    }


def save_bill_and_findings(user_id: int | None, extracted: dict, analysis: dict, zip_code: str = "") -> int:
    """Persist a scanned bill, its line items, and findings to the database."""
    global _stats_cache_ts
    _stats_cache_ts = 0.0  # invalidate stats cache so next call reflects new data

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

        for finding in analysis.get("findings", []):
            db.execute(
                "INSERT INTO findings (bill_id, finding_type, rule_id, severity, confidence, "
                "evidence_source, evidence_json, potential_savings, message, details) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    bill_id,
                    finding["type"],
                    finding.get("rule_id"),
                    finding["severity"],
                    finding.get("confidence"),
                    (finding.get("evidence") or {}).get("source"),
                    json.dumps(finding.get("evidence") or {}),
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

    normalized_findings = []
    for row in findings:
        finding = dict(row)
        try:
            parsed = json.loads(finding.get("details") or "{}")
        except json.JSONDecodeError:
            parsed = {}
        finding["parsed_details"] = parsed
        finding["confidence"] = finding.get("confidence") or parsed.get("confidence")
        finding["rule_id"] = finding.get("rule_id") or parsed.get("rule_id")
        evidence = parsed.get("evidence") or {}
        if not finding.get("evidence_source"):
            finding["evidence_source"] = evidence.get("source")
        finding["estimated_patient_savings"] = parsed.get(
            "estimated_patient_savings", finding.get("potential_savings", 0)
        )
        normalized_findings.append(finding)

    li_dicts = [dict(li) for li in line_items]
    has_patient_data = any(li.get("patient_responsibility") is not None for li in li_dicts)
    has_insurance_data = any(li.get("insurance_paid") is not None for li in li_dicts)

    total_gross = sum(
        float(f.get("parsed_details", {}).get("gross_potential_savings") or f.get("potential_savings") or 0)
        for f in normalized_findings
    )

    return {
        "bill": dict(bill),
        "line_items": li_dicts,
        "findings": normalized_findings,
        "has_patient_data": has_patient_data,
        "has_insurance_data": has_insurance_data,
        "total_gross_potential_savings": round(total_gross, 2),
    }


_stats_cache: dict = {}
_stats_cache_ts: float = 0.0


def get_stats() -> dict:
    """Get aggregate stats for the live counter, cached for STATS_CACHE_TTL_SECONDS."""
    global _stats_cache, _stats_cache_ts
    now = time.monotonic()
    if _stats_cache and (now - _stats_cache_ts) < config.STATS_CACHE_TTL_SECONDS:
        return _stats_cache

    with get_db() as db:
        row = db.execute(
            "SELECT COUNT(*) as bills_scanned, "
            "COALESCE(SUM(total_potential_savings), 0) as total_found, "
            "COALESCE(AVG(total_potential_savings), 0) as avg_savings, "
            "(SELECT COALESCE(SUM(actual_savings), 0) FROM dispute_outcomes) as realized_savings, "
            "(SELECT COUNT(*) FROM dispute_outcomes) as dispute_outcomes_count "
            "FROM bills WHERE total_findings > 0"
        ).fetchone()
    _stats_cache = dict(row)
    _stats_cache_ts = now
    return _stats_cache


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
