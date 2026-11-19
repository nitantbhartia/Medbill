"""Quantities, judged against CMS's medically unlikely edits (the most units of a code in one day)."""

import config
from db import get_db

MUE_URL = "https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medically-unlikely-edits"


def mue_limit(code: str) -> tuple[int, str] | None:
    """The highest daily limit CMS publishes for a code in any setting (the most generous, so flags stay conservative)."""
    with get_db() as db:
        row = db.execute("SELECT max_units, version FROM mue_limits WHERE code = ? ORDER BY max_units DESC LIMIT 1", (code,)).fetchone()
    return (row["max_units"], row["version"]) if row else None


def check_quantities_v2(line_items: list[dict]) -> list[dict]:
    """Over a code's daily limit: a finding for the excess. No limit but a high quantity: a $0 note. Otherwise nothing.
    Lines with the same code and date are summed first, since bills often split units."""
    groups: dict[tuple, list[dict]] = {}
    for item in line_items:
        if item.get("cpt_code") and item.get("quantity"):
            groups.setdefault((item["cpt_code"], item.get("date_of_service")), []).append(item)
    findings = []
    for (code, date), items in groups.items():
        total = sum(int(i["quantity"]) for i in items)
        charged = sum(float(i.get("charged_amount") or 0) for i in items)
        first = {**items[0], "quantity": total, "charged_amount": charged or items[0].get("charged_amount")}
        limit = mue_limit(code)
        if limit and total > limit[0]:
            unit_price = charged / total if total else 0
            findings.append({
                "type": "quantity_flag", "severity": "medium", "line_item": first, "rule_id": "RULE_QUANTITY_OVER_MUE",
                "mue_limit": limit[0], "source_version": limit[1], "billed_quantity": total,
                "potential_savings": round(min((total - limit[0]) * unit_price, charged), 2),
                "message": f"Medicare's limit for code {code} is {limit[0]} per day; you were billed {total}.",
            })
        elif not limit and total > config.HIGH_QUANTITY_FLAG:
            findings.append({
                "type": "quantity_question", "severity": "low", "line_item": first, "potential_savings": 0,
                "message": f"You were billed {total} units of code {code}. If fewer were given, ask the hospital to explain.",
            })
    return findings
