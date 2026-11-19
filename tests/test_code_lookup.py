import analyzer
import code_lookup
from db import get_db

def _hospital() -> dict:
    with get_db() as db:
        db.execute("INSERT OR IGNORE INTO hospitals (facility_id, name, city, state, zip, slug, state_slug, city_slug) "
                   "VALUES ('050625', 'Sharp Memorial Hospital', 'San Diego', 'CA', '92123', 'sharp-memorial', 'california', 'san-diego')")
    return {"facility_id": "050625", "name": "Sharp Memorial Hospital"}


def _bill(hospital: dict, description: str) -> dict:
    return {"provider_name": hospital["name"], "total_charged": 2400.0, "total_patient_owes": 2400.0, "line_items": [
        {"cpt_code": None, "description": description, "quantity": 1, "charged_amount": 2400.0, "date_of_service": "2026-03-02"}]}


def test_abbreviations_are_expanded_the_same_way_for_files_and_bills():
    assert code_lookup.normalize_description("CT Head W/O Contrast.") == "CT HEAD WITHOUT CONTRAST"
    assert code_lookup.normalize_description("ct head  without   contrast") == "CT HEAD WITHOUT CONTRAST"
    assert code_lookup.normalize_description("XR chest, 2 views") == "XRAY CHEST 2 VIEWS"


def test_exact_description_gets_the_hospitals_own_code():
    hospital = _hospital()
    code_lookup.record(hospital["facility_id"], "CT HEAD W/O CONTRAST", "70450", "mrf")
    code_lookup.record(hospital["facility_id"], "ER VISIT LEVEL 5", "99285", "mrf")
    ct = analyzer.analyze_bill(bill := _bill(hospital, "CT HEAD WITHOUT CONTRAST"), "92123")
    item = bill["line_items"][0]
    assert item["cpt_code"] == "70450" and item["code_source"] == "hospital_lookup" and not item.get("needs_confirm")
    visit = _bill(hospital, "ER Visit Level 5")
    visit["line_items"][0]["charged_amount"] = 9000.0
    result = analyzer.analyze_bill(visit, "92123")
    assert visit["line_items"][0]["cpt_code"] == "99285" and result["findings"], "a $9,000 ER visit should be flagged against Medicare"
    for finding in (f for f in result["findings"] if f.get("line_item")):
        assert finding["code_source_note"] == f"Code from {hospital['name']}'s own price list."


def test_close_match_goes_to_confirm_never_used_silently():
    hospital = _hospital()
    code_lookup.record(hospital["facility_id"], "CT HEAD WITHOUT CONTRAST ENHANCED", "70460", "mrf")
    bill = _bill(hospital, "CT HEAD WITHOUT CONTRAST ENHANCE")
    analyzer.analyze_bill(bill, "92123")
    item = bill["line_items"][0]
    assert item["cpt_code"] is None and item["needs_confirm"] and item["issue_kind"] == "code_lookup"
    assert "70460" in item["issue_choices"]


def test_ambiguous_description_offers_every_code():
    hospital = _hospital()
    for code in ("70450", "70460"):
        code_lookup.record(hospital["facility_id"], "CT HEAD", code, "mrf")
    found = code_lookup.lookup(hospital["facility_id"], "CT head")
    assert found["kind"] == "ambiguous" and {c["code"] for c in found["choices"]} == {"70450", "70460"}


def test_unknown_hospital_changes_nothing():
    bill = {"provider_name": "Nowhere Clinic Of Atlantis", "total_charged": 100.0, "line_items": [
        {"cpt_code": None, "description": "CT HEAD WITHOUT CONTRAST", "quantity": 1, "charged_amount": 100.0}]}
    analyzer.analyze_bill(bill, "")
    assert bill["line_items"][0]["cpt_code"] is None and not bill["line_items"][0].get("needs_confirm")


def test_invalid_codes_are_not_recorded():
    code_lookup.record("050625", "BED CHARGE", "0350", "mrf")
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) AS n FROM hospital_code_lookup").fetchone()["n"] == 0


def test_coverage_counts_lines_filled_from_the_list():
    hospital = _hospital()
    code_lookup.record(hospital["facility_id"], "CT HEAD W/O CONTRAST", "70450", "mrf")
    bill = _bill(hospital, "CT HEAD WITHOUT CONTRAST")
    result = analyzer.analyze_bill(bill, "92123")
    analyzer.save_bill_and_findings(None, bill, result, "92123")
    numbers = code_lookup.coverage()
    assert numbers["no_code_share_before"] == 1.0 and numbers["no_code_share_after"] == 0.0


def test_chargemaster_rows_load_for_known_hospitals_only():
    _hospital()
    result = code_lookup.load_chargemaster([
        {"facility_name": "Sharp Memorial Hospital", "description": "CT HEAD W/O CONTRAST", "code": "70450"},
        {"facility_name": "Nowhere Clinic Of Atlantis", "description": "CT HEAD W/O CONTRAST", "code": "70450"},
    ], "https://example.test/cm.csv")
    assert result == {"loaded": 1, "skipped_unknown_hospital": 1}
    assert code_lookup.lookup("050625", "ct head without contrast")["choices"][0]["code"] == "70450"


def test_confirm_sheet_asks_with_the_hospitals_choices_and_remembers_the_source():
    from line_confirmation import apply_confirmations
    from mobile_view import confirm_lines
    hospital = _hospital()
    code_lookup.record(hospital["facility_id"], "CT HEAD", "70450", "mrf")
    code_lookup.record(hospital["facility_id"], "CT HEAD", "70460", "mrf")
    bill = _bill(hospital, "CT head")
    result = analyzer.analyze_bill(bill, "92123")
    bill_id = analyzer.save_bill_and_findings(None, bill, result, "92123")
    line = confirm_lines(analyzer.get_bill_results(bill_id))[0]
    assert line["choices"] == ["70450", "70460"] and "more than one code" in line["message"]
    apply_confirmations(bill_id, [{"line_index": 0, "field": "cpt_code", "value": "70460"}])
    with get_db() as db:
        row = db.execute("SELECT cpt_code, code_source, needs_confirm FROM line_items WHERE bill_id = ?", (bill_id,)).fetchone()
    assert (row["cpt_code"], row["code_source"], row["needs_confirm"]) == ("70460", "hospital_lookup", 0)
