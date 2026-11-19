"""Shared scan pipeline: OCR one or more bill pages, analyze, and save. Used by the web and mobile APIs."""

from __future__ import annotations

import logging

import analyzer
import bill_contact
import extraction_selfcheck
import insurance_check
import scanner
from db import get_db
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
    eob_data = None
    try:
        extracted = scrub_extracted_data(extracted)
        extracted = extraction_selfcheck.check_lines(extracted, images)
        if eob_images:
            eob_data = scrub_extracted_data(extract_pages(eob_images))
            extracted = analyzer.merge_eob_into_extracted(extracted, eob_data)
        analysis = analyzer.analyze_bill(extracted, zip_code)
        bill_id = analyzer.save_bill_and_findings(user_id, extracted, analysis, zip_code, referral_code)
        bill_contact.store_from_extraction(bill_id, extracted)
        if eob_data:
            insurance_check.record(bill_id, eob_data, extracted.get("total_patient_owes"))
    except Exception as exc:
        log.error("Analysis/save failed: %s", exc, exc_info=True)
        raise AnalysisFailed(str(exc)) from exc
    return bill_id, extracted, analysis


class CannotRebuild(Exception):
    """The stored bill doesn't hold enough to merge a statement into."""


def rebuild_extracted(bill_id: int) -> tuple[dict, dict]:
    """The saved bill and its lines in the shape the analyzer takes."""
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        items = db.execute("SELECT * FROM line_items WHERE bill_id = ? ORDER BY id", (bill_id,)).fetchall()
    if not bill or not items:
        raise CannotRebuild("no stored line items")
    extracted = {key: bill[key] for key in ("provider_name", "provider_address", "bill_date",
                                            "total_charged", "total_patient_owes")}
    extracted["line_items"] = [dict(item) for item in items]
    return dict(bill), extracted


def add_eob(bill_id: int, eob_images: list[tuple[bytes, str]]) -> None:
    """Merge an insurance statement into a saved bill and redo its checks. The unlock is kept."""
    bill, extracted = rebuild_extracted(bill_id)
    eob_data = scrub_extracted_data(extract_pages(eob_images))
    try:
        merged = analyzer.merge_eob_into_extracted(extracted, eob_data)
        analysis = analyzer.analyze_bill(merged, bill["zip_code"] or "")
        analyzer.replace_findings_and_insurance_fields(bill_id, merged, analysis)
        insurance_check.record(bill_id, eob_data, bill["total_patient_owes"])
    except Exception as exc:
        log.error("Adding a statement failed: %s", exc, exc_info=True)
        raise AnalysisFailed(str(exc)) from exc
