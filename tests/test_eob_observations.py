import json

import analyzer
import eob_observations
import mrf_truth
import payer_rates
from db import get_db
from validators.insurer_rate import check_peer_rate

FACILITY = "050625"
EOB = {"insurer_name": "Anthem BC", "plan_name": "PPO Select", "patient_name": "Dana Reyes", "line_items": [
    {"cpt_code": "99285", "description": "ER visit", "charged_amount": 4200.0, "allowed_amount": 900.0, "date_of_service": "2026-03-02", "patient_responsibility": 150.0},
    {"cpt_code": "71046", "description": "Chest X-ray", "charged_amount": 850.0, "allowed_amount": 120.0, "date_of_service": "2026-03-02", "patient_responsibility": 20.0},
    {"cpt_code": "85025", "description": "CBC", "charged_amount": 300.0, "allowed_amount": 40.0, "date_of_service": "2026-03-02", "patient_responsibility": 0.0},
]}


def _setup():
    payer_rates.seed_aliases()
    with get_db() as db:
        db.execute("INSERT OR IGNORE INTO hospitals (facility_id, name, city, state, zip, slug, state_slug, city_slug) "
                   "VALUES (?, 'Sharp Memorial Hospital', 'San Diego', 'CA', '92123', 'sharp', 'california', 'san-diego')", (FACILITY,))


def test_three_line_statement_makes_three_observations_with_no_identifiers():
    _setup()
    assert eob_observations.record(7, EOB, FACILITY) == 3
    with get_db() as db:
        rows = [dict(r) for r in db.execute("SELECT * FROM price_observations WHERE source_type = 'eob'")]
    assert {r["payer"] for r in rows} == {"Anthem Blue Cross"} and all(r["confidence"] == 0.8 for r in rows)
    text = json.dumps(rows)
    assert "Dana" not in text and "Reyes" not in text
    assert eob_observations.record(7, EOB, FACILITY) == 0  # the same statement twice adds nothing


def test_no_consent_no_observations(monkeypatch):
    _setup()
    with get_db() as db:
        db.execute("INSERT INTO mobile_devices (device_id, token_hash, data_improvement) VALUES ('d1', 'h', 0)")
    assert not eob_observations.consented("d1")
    with get_db() as db:
        db.execute("UPDATE mobile_devices SET data_improvement = 1 WHERE device_id = 'd1'")
    assert eob_observations.consented("d1")
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) AS n FROM price_observations WHERE source_type = 'eob'").fetchone()["n"] == 0


def _peers(count, allowed=900.0):
    for bill in range(count):
        eob_observations.record(100 + bill, {"insurer_name": "Anthem Blue Cross", "line_items": [{"cpt_code": "99285", "allowed_amount": allowed}]}, FACILITY)


def test_peer_rate_needs_enough_statements_and_is_only_worth_asking():
    _setup()
    item = {"cpt_code": "99285", "charged_amount": 4200.0, "patient_responsibility": 2500.0}
    _peers(9)
    assert check_peer_rate(item, FACILITY, "Anthem Blue Cross", "Sharp") is None  # under OUTCOME_MIN_SAMPLE: never shown
    _peers(12)
    finding = check_peer_rate(item, FACILITY, "Anthem Blue Cross", "Sharp")
    assert finding["severity"] == "low" and finding["potential_savings"] == 0 and finding["peer_median"] == 900.0
    from rule_sources import basis_for
    basis = basis_for(finding["rule_id"], finding)
    assert basis["kind"] == "check" and "median of $900" in basis["explanation"]


def test_truth_check_flags_a_hospital_whose_file_is_forty_percent_off():
    _setup()
    for index in range(10):
        code = f"9928{index}"
        eob_observations.record(200 + index, {"insurer_name": "Aetna", "line_items": [{"cpt_code": code, "allowed_amount": 1000.0}]}, FACILITY)
        with get_db() as db:
            db.execute("INSERT INTO price_observations (source_type, source_ref, code, facility_id, payer, negotiated_rate) VALUES ('mrf', ?, ?, ?, 'Aetna', 1667.0)",
                       (f"f{index}", code, FACILITY))
    report = mrf_truth.check()
    assert report[FACILITY]["mrf_reliability"] == "low" and report[FACILITY]["within_tolerance_share"] == 0.0
    with get_db() as db:
        assert db.execute("SELECT mrf_reliability FROM hospitals WHERE facility_id = ?", (FACILITY,)).fetchone()["mrf_reliability"] == "low"
        assert db.execute("SELECT COUNT(*) AS n FROM data_quality_runs WHERE status = 'mrf_truth_check'").fetchone()["n"] == 1


def test_truth_check_keeps_a_matching_hospital_reliable_and_ignores_small_samples():
    _setup()
    for index in range(10):
        code = f"9928{index}"
        eob_observations.record(300 + index, {"insurer_name": "Aetna", "line_items": [{"cpt_code": code, "allowed_amount": 1000.0}]}, FACILITY)
        with get_db() as db:
            db.execute("INSERT INTO price_observations (source_type, source_ref, code, facility_id, payer, negotiated_rate) VALUES ('mrf', ?, ?, ?, 'Aetna', 1050.0)",
                       (f"g{index}", code, FACILITY))
    assert mrf_truth.check()[FACILITY]["mrf_reliability"] == "ok"
    with get_db() as db:
        db.execute("DELETE FROM price_observations")
    eob_observations.record(1, EOB, FACILITY)
    assert mrf_truth.check() == {}


def test_unreliable_hospital_file_rate_is_only_supporting_evidence():
    _setup()
    with get_db() as db:
        db.execute("UPDATE hospitals SET mrf_reliability = 'low' WHERE facility_id = ?", (FACILITY,))
        db.execute("INSERT INTO price_observations (source_type, source_ref, code, facility_id, payer, negotiated_rate, file_updated) "
                   "VALUES ('mrf', 'x', '99285', ?, 'Anthem Blue Cross', 800.0, date('now'))", (FACILITY,))
    bill = {"provider_name": "Sharp Memorial Hospital", "insurer_name": "Anthem Blue Cross", "total_charged": 4200.0, "total_patient_owes": 4200.0, "line_items": [
        {"cpt_code": "99285", "description": "ER visit", "quantity": 1, "charged_amount": 4200.0, "date_of_service": "2026-03-02"}]}
    result = analyzer.analyze_bill(bill, "92123")
    rate = next(f for f in result["findings"] if f["type"] == "insurer_rate")
    assert rate["severity"] == "low"
    assert any(f["type"] in ("price_markup", "price_info") for f in result["findings"])  # the Medicare comparison still runs
