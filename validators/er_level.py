"""ER visit level: a level 4 or 5 is worth asking about only when the bill's other services don't support it."""

import config
from validators.modifiers import is_lab_code

ER_LEVELS = {"99284": 4, "99285": 5}


def _in_ranges(code: str, ranges) -> bool:
    return code.isdigit() and len(code) == 5 and any(low <= int(code) <= high for low, high in ranges)


def supporting_services(items: list[dict]) -> int:
    """How many kinds of support the same-day services show: advanced imaging, IV push or infusion, critical care, a lab panel."""
    codes = [str(i.get("cpt_code") or "") for i in items]
    kinds = 0
    kinds += any(_in_ranges(c, config.ER_ADVANCED_IMAGING_RANGES) for c in codes)
    kinds += any(_in_ranges(c, [config.ER_IV_RANGE]) for c in codes)
    kinds += any(c in config.ER_CRITICAL_CARE_CODES for c in codes)
    kinds += sum(is_lab_code(c) for c in codes) >= config.ER_LAB_PANEL_MIN_CODES
    return kinds


def check_er_level_v2(item: dict, all_items: list[dict]) -> dict | None:
    """99285 with no support is worth asking about; 99285 with one kind of support, or 99284 with none, is a note.
    Everything else is fine. Always $0: the evidence is in the medical record, not on the bill."""
    code = item.get("cpt_code")
    if code not in ER_LEVELS:
        return None
    same_day = [i for i in all_items if i.get("date_of_service") == item.get("date_of_service")]
    support = supporting_services(same_day)
    asks = (code == "99285" and support <= 1) or (code == "99284" and support == 0)
    if not asks:
        return None
    level = ER_LEVELS[code]
    return {
        "type": "upcoding", "severity": "low", "line_item": item, "potential_savings": 0, "billed_level": level,
        "message": f"The bill shows a level {level} ER visit. Please send the documentation that supports a level {level} visit.",
    }
