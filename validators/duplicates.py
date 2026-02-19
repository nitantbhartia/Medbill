def find_duplicates(item: dict, all_items: list[dict]) -> dict | None:
    """
    Find duplicate charges: same CPT code + same non-null date + same quantity + same amount.
    Requires both items to have a date_of_service — null dates cannot be confirmed as same-day
    duplicates and would produce false positives when OCR misses date fields.
    Only report the first occurrence to avoid double-reporting.
    """
    if not item.get("cpt_code"):
        return None
    if not item.get("date_of_service"):
        return None  # can't confirm duplicates without a date

    matches = [
        other
        for other in all_items
        if other is not item
        and other.get("cpt_code") == item["cpt_code"]
        and other.get("date_of_service") == item["date_of_service"]  # both non-null (item checked above)
        and other.get("quantity") == item["quantity"]
        and other.get("charged_amount") == item["charged_amount"]
    ]

    if not matches:
        return None

    # Only report from the first occurrence (by position in list) to avoid dupes
    first_index = next(i for i, x in enumerate(all_items) if x is item)
    for match in matches:
        match_index = next(i for i, x in enumerate(all_items) if x is match)
        if match_index < first_index:
            return None  # already reported from the earlier item

    description = item.get("description") or item.get("cpt_code") or "this service"
    date_str = item.get("date_of_service") or "the same date"

    return {
        "type": "duplicate_charge",
        "severity": "high",
        "line_item": item,
        "duplicate_of": matches,
        "potential_savings": item["charged_amount"],
        "message": (
            f"'{description}' appears to be billed {len(matches) + 1} times "
            f"on {date_str}. "
            f"This could save you ${item['charged_amount']:,.2f}."
        ),
    }
