from validators.pricing import get_medicare_rate

ER_VISIT_LEVELS = {
    "99281": {
        "level": 1,
        "description": "Self-limited or minor problem",
        "examples": "small cut, minor rash",
    },
    "99282": {
        "level": 2,
        "description": "Low to moderate severity",
        "examples": "sprained ankle, ear infection",
    },
    "99283": {
        "level": 3,
        "description": "Moderate severity",
        "examples": "abdominal pain, asthma attack, broken bone",
    },
    "99284": {
        "level": 4,
        "description": "High severity, urgent evaluation",
        "examples": "chest pain, severe allergic reaction",
    },
    "99285": {
        "level": 5,
        "description": "High severity, immediate threat to life",
        "examples": "heart attack, stroke, major trauma",
    },
}


def check_upcoding(item: dict) -> dict | None:
    """
    Flag potential upcoding for ER visits.
    Level 4 and 5 visits are frequently billed when Level 3 was appropriate.
    """
    if not item.get("cpt_code") or item["cpt_code"] not in ("99284", "99285"):
        return None

    billed_level = ER_VISIT_LEVELS[item["cpt_code"]]["level"]
    likely_level = billed_level - 1
    likely_code = f"9928{likely_level}"

    correct_rate = get_medicare_rate(likely_code)
    billed_rate = item.get("charged_amount", 0)

    if not correct_rate:
        correct_rate = billed_rate * 0.6

    savings = max(0, billed_rate - correct_rate)

    return {
        "type": "upcoding",
        "severity": "medium",
        "line_item": item,
        "likely_correct_code": likely_code,
        "billed_level": billed_level,
        "likely_level": likely_level,
        "correct_code": likely_code,
        "correct_rate": correct_rate,
        "potential_savings": round(savings, 2),
        "message": (
            f"You were billed for a Level {billed_level} visit "
            f"(${billed_rate:,.2f}), but many visits billed at this level "
            f"are actually Level {likely_level} (${correct_rate:,.2f}). "
            f"Potential overcharge: ${savings:,.2f}."
        ),
    }
