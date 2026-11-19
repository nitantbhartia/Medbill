"""Insurer-specific prices: payer rows kept apart, insurer names made comparable, the finding and its fallback."""

import copy

import analyzer
import payer_rates
from db import get_db
from hospital_etl import normalize_price_rows, summarize_by_code
from tests.conftest import SAMPLE_BILL

TALL = [
    {"code": "99285", "description": "ER visit", "payer_name": "Anthem Blue Cross", "plan_name": "PPO", "negotiated_rate": "800",
     "median_amount": "790", "10th_percentile": "600", "90th_percentile": "950"},
    {"code": "99285", "description": "ER visit", "payer_name": "Aetna", "plan_name": "HMO", "negotiated_rate": "1000"},
]
WIDE = [{"code": "71046", "description": "Chest X-ray", "standard_charge|Blue Shield of California|PPO|negotiated_dollar": "120",
         "standard_charge|Health Net|HMO|negotiated_dollar": "100", "standard_charge|Oscar|EPO|negotiated_dollar": ""}]


def test_rows_stay_one_per_payer_and_plan_with_allowed_amounts():
    rows = normalize_price_rows(TALL)
    assert [(r["payer"], r["plan_name"], r["avg_negotiated_rate"]) for r in rows] == [("Anthem Blue Cross", "PPO", 800.0), ("Aetna", "HMO", 1000.0)]
    assert (rows[0]["median_allowed"], rows[0]["p10_allowed"], rows[0]["p90_allowed"]) == (790.0, 600.0, 950.0)


def test_wide_files_expand_to_one_row_per_payer_column_that_has_a_rate():
    rows = normalize_price_rows(WIDE)
    assert [(r["payer"], r["avg_negotiated_rate"]) for r in rows] == [("Blue Shield of California", 120.0), ("Health Net", 100.0)]


def test_seo_summary_still_has_avg_min_max_across_payers():
    summary = summarize_by_code(normalize_price_rows(TALL))[0]
    assert (summary["avg_negotiated_rate"], summary["min_negotiated_rate"], summary["max_negotiated_rate"]) == (900.0, 800.0, 1000.0)


def test_insurer_names_on_files_and_statements_become_one_name():
    payer_rates.seed_aliases()
    assert payer_rates.canonical_payer("Anthem BC Life & Health") == "Anthem Blue Cross"
    assert payer_rates.canonical_payer("BCBS?") is None
    assert payer_rates.canonical_payer("Blue Shield of CA PPO Plan") == "Blue Shield of California"


def seed_rate(file_updated="2026-09-01", parsed="2026-09-02T00:00:00"):
    with get_db() as db:
        db.execute("DELETE FROM price_observations WHERE facility_id = 'F1'")
        db.execute("DELETE FROM hospitals WHERE facility_id = 'F1'")
        db.execute("INSERT INTO hospitals (facility_id, name, city, state, zip, slug, state_slug, city_slug) VALUES ('F1', 'Memorial Regional Hospital', 'Hollywood', 'FL', '33021', 'memorial-regional-hospital', 'florida', 'hollywood')")
    payer_rates.seed_aliases()
    payer_rates.save_payer_rates("F1", [{"cpt_code": "71046", "payer": "Anthem Blue Cross", "plan_name": "PPO", "avg_negotiated_rate": 120.0}],
                                 "https://hospital.example/prices.csv", file_updated, 2026)
    with get_db() as db:
        db.execute("UPDATE price_observations SET parsed_at = ? WHERE facility_id = 'F1'", (parsed,))


def analyzed(insurer):
    bill = copy.deepcopy(SAMPLE_BILL)
    bill["insurer_name"] = insurer
    for item in bill["line_items"]:
        item.update(insurance_paid=None, insurance_adjustment=None, patient_responsibility=None)
    return analyzer.analyze_bill(bill, "33021")


def types_for(analysis, code):
    return {f["type"] for f in analysis["findings"] if (f.get("line_item") or {}).get("cpt_code") == code}


def test_a_named_insurer_with_a_file_rate_replaces_the_medicare_finding():
    seed_rate()
    finding = next(f for f in analyzed("Anthem Blue Cross")["findings"] if f["type"] == "insurer_rate")
    assert finding["contracted_rate"] == 120.0 and finding["rule_id"] == "RULE_INSURER_CONTRACTED_RATE"
    assert "insurer_rate" in types_for(analyzed("Anthem BC Life & Health"), "71046")
    assert "price_markup" not in types_for(analyzed("Anthem Blue Cross"), "71046")


def test_without_an_insurer_or_rate_the_medicare_finding_is_the_fallback():
    seed_rate()
    assert "insurer_rate" not in types_for(analyzed(None), "71046")
    assert "insurer_rate" not in types_for(analyzed("Aetna"), "71046")


def test_files_older_than_the_limit_are_not_used():
    seed_rate(file_updated="2020-01-01", parsed="2020-01-02T00:00:00")
    assert payer_rates.find_contracted_rate("F1", "71046", "Anthem Blue Cross") is None
