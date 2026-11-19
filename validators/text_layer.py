"""A PDF's own text is exact. Compare what the image reading produced with it, fix a misread digit, and ask about the rest."""

import re

import config

NUMBER = re.compile(r"\$?\(?-?\d[\d,]*\.\d{2}\)?")
AMOUNT_FIELDS = ("charged_amount", "insurance_paid", "insurance_adjustment", "patient_responsibility")


def clean(text: str | None) -> str:
    """The text layer as the extraction prompt sees it: printable characters only, capped in length."""
    printable = "".join(ch for ch in (text or "") if ch.isprintable() or ch in "\n\t")
    return printable.strip()[:config.MAX_TEXT_LAYER_CHARS]


def _amounts(text: str) -> list[float]:
    return [float(token.strip("$()").replace(",", "")) for token in NUMBER.findall(text)]


def _digit_diffs(first: float, second: float) -> int | None:
    a, b = f"{first:.2f}", f"{second:.2f}"
    return sum(x != y for x, y in zip(a, b)) if len(a) == len(b) else None


def _line_amounts(text: str, code: str | None) -> list[float]:
    """Amounts on the text-layer lines that mention this billing code."""
    if not code:
        return []
    return [amount for line in text.splitlines() if code in line for amount in _amounts(line)]


def reconcile(extracted: dict, text_layer: str) -> int:
    """For each line amount that is not in the text layer: replace it with the one amount on that code's line that differs by at
    most TEXT_LAYER_FIX_MAX_DIGIT_DIFFS digits; otherwise ask the user to confirm the line. Returns how many amounts were fixed."""
    text = clean(text_layer)
    all_amounts = set(_amounts(text))
    fixed = 0
    for item in extracted.get("line_items") or []:
        candidates = _line_amounts(text, item.get("cpt_code"))
        for field in AMOUNT_FIELDS:
            value = item.get(field)
            if not isinstance(value, (int, float)) or round(value, 2) in all_amounts:
                continue
            near = [c for c in candidates if (_digit_diffs(value, c) or 99) <= config.TEXT_LAYER_FIX_MAX_DIGIT_DIFFS]
            if len(set(near)) == 1:
                item[field] = near[0]
                fixed += 1
            elif not item.get("needs_confirm"):
                item.update(needs_confirm=True, issue_kind="text_layer_mismatch", issue_field=field)
    return fixed
