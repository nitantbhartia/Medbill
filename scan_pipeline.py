"""Shared scan pipeline: OCR one or more bill pages, analyze, and save. Used by the web and mobile APIs."""

from __future__ import annotations

import logging

import analyzer
import scanner
from compliance import scrub_extracted_data

log = logging.getLogger(__name__)


class AnalysisFailed(Exception):
    """Raised when extraction worked but analyzing or saving the bill did not."""


def extract_pages(images: list[tuple[bytes, str]]) -> dict:
    """OCR one page, or several pages merged into one bill. Raises scanner errors as-is."""
    if len(images) == 1:
        return scanner.process_bill_with_verification(*images[0])
    return scanner.process_multi_page_bill(images)


def run_scan(
    images: list[tuple[bytes, str]],
    zip_code: str,
    user_id: int | None,
    referral_code: str | None,
    eob_images: list[tuple[bytes, str]] | None = None,
) -> tuple[int, dict, dict]:
    """OCR the pages, analyze, save. Returns (bill_id, extracted, analysis)."""
    extracted = extract_pages(images)
    try:
        extracted = scrub_extracted_data(extracted)
        if eob_images:
            eob_data = scrub_extracted_data(extract_pages(eob_images))
            extracted = analyzer.merge_eob_into_extracted(extracted, eob_data)
        analysis = analyzer.analyze_bill(extracted, zip_code)
        bill_id = analyzer.save_bill_and_findings(user_id, extracted, analysis, zip_code, referral_code)
    except Exception as exc:
        log.error("Analysis/save failed: %s", exc, exc_info=True)
        raise AnalysisFailed(str(exc)) from exc
    return bill_id, extracted, analysis
