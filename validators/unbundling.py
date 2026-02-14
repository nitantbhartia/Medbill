from validators.pricing import get_medicare_rate
from db import get_db

# Common unbundling pairs from CMS NCCI edits
UNBUNDLING_RULES = [
    {
        "component_codes": ["80048", "80053"],
        "correct_code": "80053",
        "name": "Comprehensive Metabolic Panel",
        "description": (
            "Basic metabolic panel (80048) is a subset of comprehensive "
            "metabolic panel (80053). Should not be billed separately."
        ),
    },
    {
        "component_codes": ["85025", "85027"],
        "correct_code": "85025",
        "name": "CBC with Differential",
        "description": (
            "CBC without differential (85027) is included in "
            "CBC with differential (85025)."
        ),
    },
    {
        "component_codes": ["36415", "36416"],
        "correct_code": "36415",
        "name": "Blood draw",
        "description": (
            "Capillary blood draw should not be billed alongside "
            "venipuncture for the same collection."
        ),
    },
    {
        "component_codes": ["99283", "99284", "99285"],
        "correct_code": "highest_only",
        "name": "ER Visit Level",
        "description": (
            "Only one ER visit level code should be billed per encounter. "
            "Multiple levels suggest upcoding or duplicate billing."
        ),
    },
    {
        "component_codes": ["27447", "27486"],
        "correct_code": "27447",
        "name": "Total Knee Arthroplasty",
        "description": (
            "Components of knee replacement should not be billed "
            "separately from the primary procedure code."
        ),
    },
    {
        "component_codes": ["93000", "93005", "93010"],
        "correct_code": "93000",
        "name": "ECG/EKG",
        "description": (
            "EKG with interpretation (93000) includes tracing (93005) "
            "and interpretation (93010). Should not be billed separately."
        ),
    },
    {
        "component_codes": ["76700", "76705"],
        "correct_code": "76700",
        "name": "Abdominal Ultrasound",
        "description": (
            "Complete abdominal ultrasound (76700) includes limited "
            "ultrasound (76705). Both should not be billed together."
        ),
    },
]

def _check_ncci_modifier(code1: str, code2: str) -> str | None:
    """
    Check NCCI edit modifier indicator for a code pair.
    Returns "0" (never allowed), "1" (allowed with modifier), or None (no edit found).
    """
    with get_db() as db:
        row = db.execute(
            "SELECT modifier_indicator FROM ncci_edits "
            "WHERE column_1_code = ? AND column_2_code = ? "
            "AND (deletion_date IS NULL OR deletion_date > date('now')) "
            "ORDER BY effective_date DESC LIMIT 1",
            (code1, code2),
        ).fetchone()
        if row:
            return row["modifier_indicator"]

        row = db.execute(
            "SELECT modifier_indicator FROM ncci_edits "
            "WHERE column_1_code = ? AND column_2_code = ? "
            "AND (deletion_date IS NULL OR deletion_date > date('now')) "
            "ORDER BY effective_date DESC LIMIT 1",
            (code2, code1),
        ).fetchone()
        return row["modifier_indicator"] if row else None


def check_unbundling(item: dict, all_items: list[dict]) -> dict | None:
    """
    Check if this item is part of an unbundling pair where both
    component codes appear on the same bill.
    Respects NCCI modifier indicators — modifier_indicator "1" reduces severity
    since the codes may be legitimate with proper modifier (e.g., modifier 59).
    """
    if not item.get("cpt_code"):
        return None

    for rule in UNBUNDLING_RULES:
        if item["cpt_code"] not in rule["component_codes"]:
            continue

        other_codes_on_bill = [
            i["cpt_code"] for i in all_items if i is not item and i.get("cpt_code")
        ]
        matching = [
            c
            for c in rule["component_codes"]
            if c in other_codes_on_bill and c != item["cpt_code"]
        ]

        if not matching:
            continue

        # Avoid double-reporting: only report from the first code in the rule
        item_idx = rule["component_codes"].index(item["cpt_code"])
        for m in matching:
            if rule["component_codes"].index(m) < item_idx:
                return None

        related = [i for i in all_items if i.get("cpt_code") in matching]
        total_charged = item.get("charged_amount", 0) + sum(
            r.get("charged_amount", 0) for r in related
        )

        if rule["correct_code"] == "highest_only":
            correct_rate = max(
                item.get("charged_amount", 0),
                *(r.get("charged_amount", 0) for r in related),
            )
        else:
            correct_rate = get_medicare_rate(rule["correct_code"]) or (
                total_charged * 0.6
            )

        savings = max(0, total_charged - correct_rate)
        descriptions = [item.get("description", "")] + [
            r.get("description", "") for r in related
        ]

        # Check NCCI modifier indicator
        modifier_ind = _check_ncci_modifier(item["cpt_code"], matching[0])
        if modifier_ind == "1":
            severity = "low"
            caveat = (
                " Note: NCCI allows these codes together with a proper modifier "
                "(e.g., modifier 59). If the bill shows a modifier, this may be legitimate."
            )
        else:
            severity = "medium"
            caveat = ""

        return {
            "type": "unbundling",
            "severity": severity,
            "line_item": item,
            "related_items": related,
            "bundled_code": rule["correct_code"],
            "modifier_indicator": modifier_ind,
            "potential_savings": round(savings, 2),
            "message": (
                f"These procedures ({', '.join(descriptions)}) are typically billed "
                f"as one bundled code ({rule['correct_code']}). Billing them separately "
                f"may have inflated your bill by ${savings:,.2f}.{caveat}"
            ),
        }

    return None
