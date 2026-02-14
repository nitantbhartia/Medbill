from validators.pricing import get_medicare_rate

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

# Track which items have already been reported as part of an unbundling finding
_reported_items: set = set()


def check_unbundling(item: dict, all_items: list[dict]) -> dict | None:
    """
    Check if this item is part of an unbundling pair where both
    component codes appear on the same bill.
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
        total_charged = item["charged_amount"] + sum(
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
        descriptions = [item["description"]] + [
            r.get("description", "") for r in related
        ]

        return {
            "type": "unbundling",
            "severity": "medium",
            "line_item": item,
            "related_items": related,
            "bundled_code": rule["correct_code"],
            "potential_savings": round(savings, 2),
            "message": (
                f"These procedures ({', '.join(descriptions)}) are typically billed "
                f"as one bundled code ({rule['correct_code']}). Billing them separately "
                f"may have inflated your bill by ${savings:,.2f}."
            ),
        }

    return None
