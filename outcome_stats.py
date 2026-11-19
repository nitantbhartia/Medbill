"""What actually happened for BillKarma users at a hospital, counting only outcomes verified with a new statement."""

from __future__ import annotations

import json
import statistics

import config
from db import get_db


def get_hospital_outcomes(hospital_id: str) -> dict:
    """Per rule: verified outcomes, the share that got money off, and the median reduction.
    A rule with fewer than OUTCOME_MIN_SAMPLE verified outcomes is left out (a privacy and honesty rule)."""
    with get_db() as db:
        rows = db.execute("SELECT rule_ids, actual_savings FROM dispute_outcomes WHERE verified = 1 AND facility_id = ?",
                          (hospital_id,)).fetchall()
    by_rule: dict[str, list[float]] = {}
    for row in rows:
        for rule_id in set(json.loads(row["rule_ids"] or "[]")):
            by_rule.setdefault(rule_id, []).append(float(row["actual_savings"] or 0))
    stats = {}
    for rule_id, savings in by_rule.items():
        if len(savings) < config.OUTCOME_MIN_SAMPLE:
            continue
        wins = [amount for amount in savings if amount > 0]
        stats[rule_id] = {"verified": len(savings), "succeeded": len(wins),
                          "success_rate": round(len(wins) / len(savings), 2),
                          "median_reduction": round(statistics.median(wins), 2) if wins else 0.0}
    return stats


RULE_PHRASES = {
    "RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT": "duplicate charges",
    "RULE_NCCI_UNBUNDLING": "unbundled charges",
    "RULE_MARKUP_VS_MEDICARE": "prices far above Medicare",
    "RULE_INSURER_CONTRACTED_RATE": "charges above the insurer's rate",
    "RULE_EOB_RECONCILIATION": "balances that didn't match the insurance statement",
    "RULE_ER_LEVEL_UPCODING_HEURISTIC": "ER visit levels",
    "RULE_HIGH_QUANTITY_CHECK": "quantities",
    "RULE_REGIONAL_BENCHMARK_OUTLIER": "high charges",
}


def outcome_line(hospital_name: str, hospital_id: str | None, rule_ids: list[str]) -> str | None:
    """"Harbor View corrected duplicate charges for 8 of 10 BillKarma users", for the rule on this bill with the best record."""
    if not hospital_id:
        return None
    stats = {rule: s for rule, s in get_hospital_outcomes(hospital_id).items() if rule in rule_ids and s["succeeded"] > 0}
    if not stats:
        return None
    rule, best = max(stats.items(), key=lambda pair: pair[1]["success_rate"])
    return f"{hospital_name} corrected {RULE_PHRASES.get(rule, 'charges')} for {best['succeeded']} of {best['verified']} BillKarma users"
