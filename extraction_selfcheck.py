"""After a scan: re-read lines that look misread, and mark the ones still wrong so the user can confirm them."""

from __future__ import annotations

import logging

import config
import scanner
from validators.extraction import LINE_ISSUE_KINDS, line_issues

log = logging.getLogger(__name__)

NUMBER_FIELDS = ("quantity", "unit_price", "charged_amount", "insurance_paid", "insurance_adjustment", "patient_responsibility")
REREAD_FIELDS = ("cpt_code", "description") + NUMBER_FIELDS
# Arithmetic problems come first when there are more lines to confirm than we will ask about.
ISSUE_PRIORITY = {"line_math": 0, "payer_math": 1, "negative_amount": 2, "invalid_code": 3, "unknown_code": 4}


def _blocking(item: dict, index: int) -> list[dict]:
    return sorted((i for i in line_issues(item, index) if i["kind"] in LINE_ISSUE_KINDS),
                  key=lambda i: ISSUE_PRIORITY[i["kind"]])


def _page_for(item: dict, images: list[tuple[bytes, str]]) -> tuple[bytes, str] | None:
    if len(images) == 1:
        return images[0]
    page = item.get("page")
    return images[page - 1] if isinstance(page, int) and 1 <= page <= len(images) else None


def _merge(item: dict, reread: dict) -> dict:
    merged = dict(item)
    for field in REREAD_FIELDS:
        value = reread.get(field)
        if field in NUMBER_FIELDS:
            value = scanner._coerce_numeric(value)
        if value is not None:
            merged[field] = int(value) if field == "quantity" else value
    return merged


def check_lines(extracted: dict, images: list[tuple[bytes, str]]) -> dict:
    """Re-read each suspicious line once (at most OCR_MAX_LINE_REREADS per bill), keep a re-read only if it
    clears the problem, and set needs_confirm on the lines that are still wrong."""
    items = extracted.get("line_items", [])
    rereads = 0
    for index, item in enumerate(items):
        if not _blocking(item, index):
            continue
        page = _page_for(item, images)
        if page and rereads < config.OCR_MAX_LINE_REREADS:
            rereads += 1
            reread = scanner.reread_line(*page, item)
            candidate = _merge(item, reread) if reread else None
            if candidate and not _blocking(candidate, index):
                items[index] = candidate
                continue
    flagged = [(index, _blocking(item, index)[0]) for index, item in enumerate(items) if _blocking(item, index)]
    flagged.sort(key=lambda pair: ISSUE_PRIORITY[pair[1]["kind"]])
    for index, issue in flagged[: config.OCR_MAX_CONFIRM_LINES]:
        items[index].update(needs_confirm=True, issue_kind=issue["kind"], issue_field=issue["field"])
    return extracted
