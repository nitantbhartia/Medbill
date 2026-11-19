"""The hospital's side: a fixed table of what makes a flagged charge legitimate. A match can only downgrade a finding."""

import config
from validators.modifiers import modifiers_of

SEVERITY_DOWN = {"high": "medium", "medium": "low", "low": "informational"}


def _differs(items: list[dict], *fields: str) -> bool:
    for field in fields:
        values = {str(item[field]).strip().lower() for item in items if item.get(field)}
        if len(values) > 1:
            return True
    return False


def _is_drug_or_supply(item: dict) -> bool:
    code = (item.get("cpt_code") or "").upper()
    revenue = str(item.get("revenue_code") or "").strip()
    return code.startswith(config.DRUG_SUPPLY_CODE_PREFIXES) or revenue in config.DRUG_SUPPLY_REVENUE_CODES


def innocent_reason(finding: dict) -> str | None:
    """The key into rule_sources.HOSPITAL_REPLIES that explains this finding, or None."""
    item = finding.get("line_item") or {}
    kind = finding.get("type")
    if kind == "duplicate_charge":
        lines = [item, *(finding.get("duplicate_of") or [])]
        if _differs(lines, "time", "service_time", "room"):
            return "different_time_or_room"
        if _differs(lines, "revenue_code"):
            return "different_revenue_code"
    if kind == "unbundling":
        lines = [item, *(finding.get("related_items") or [])]
        if any(modifiers_of(line) & config.DISTINCT_SERVICE_MODIFIERS for line in lines):
            return "allowed_modifier"
        if _differs(lines, "date_of_service", "provider", "rendering_provider"):
            return "different_dates_or_providers"
    if kind in ("price_markup", "benchmark_outlier") and _is_drug_or_supply(item):
        return "drug_or_supply"
    return None


def apply_innocent_explanations(findings: list[dict]) -> None:
    """Downgrade each matching finding one level and record why. Nothing is ever added, upgraded or re-priced."""
    for finding in findings:
        reason = innocent_reason(finding)
        if not reason:
            continue
        finding["severity"] = SEVERITY_DOWN.get(finding.get("severity"), finding.get("severity"))
        finding["innocent_reason"] = reason
