import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())
os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

import research_report  # noqa: E402
from db import get_db  # noqa: E402
from hospital_seo import upsert_hospital_row  # noqa: E402
from main import app  # noqa: E402

client = TestClient(app)

# Level 4 ER visit list prices for 24 hospitals: FL lower, NY higher
FL_PRICES = [1450, 1620, 1780, 1900, 2050, 2210, 2380, 2490, 2650, 2800, 2950, 3100]
NY_PRICES = [3300, 3520, 3700, 3890, 4100, 4350, 4600, 4880, 5150, 5400, 5900, 6600]


def _seed():
    rows = [("FL", p) for p in FL_PRICES] + [("NY", p) for p in NY_PRICES]
    for i, (state, price) in enumerate(rows):
        fid = f"{900100 + i}"
        upsert_hospital_row({"facility_id": fid, "name": f"{state} Regional Medical Center {i}", "city": "Tampa" if state == "FL" else "Albany",
                             "state": state, "zip": "33606" if state == "FL" else "12208", "slug": f"regional-{i}"})
        with get_db() as db:
            db.execute(
                "INSERT INTO hospital_prices (facility_id, cpt_code, description, gross_charge, data_year) VALUES (?, '99284', 'Emergency department visit, level 4', ?, 2026)",
                (fid, price),
            )


def test_spread_uses_percentiles_of_hospital_list_prices():
    _seed()
    [er] = research_report.procedure_spreads()
    assert er["code"] == "99284" and er["hospitals"] == 24
    assert er["median"] == 3200
    assert er["p10"] < er["median"] < er["p90"]
    assert er["spread"] == round(er["p90"] / er["p10"], 1)


def test_state_medians_rank_highest_first():
    _seed()
    states = research_report.state_medians()
    assert [s["state"] for s in states] == ["NY", "FL"]
    assert states[1]["median"] == 2295


def test_report_page_shows_only_computed_figures():
    _seed()
    html = client.get("/research/2026-medical-billing-report/").text
    for invented in ("47,000", "1 in 3", "76%", "34%", "$1,312"):
        assert invented not in html
    assert "24 hospitals" in html or "across 24" in html
    assert "New York" in html


def test_report_with_too_little_data_says_so():
    html = client.get("/research/2026-medical-billing-report/").text
    assert "being refreshed" in html


def test_press_stats_come_from_the_database():
    _seed()
    html = client.get("/press/").text
    assert "6,000" not in html and "4.2x" not in html
    assert "#1 cause" not in html


def test_procedure_pages_label_estimates_and_drop_markup_multiples():
    for path in ("/procedures/", "/procedures/knee-replacement/", "/costs/knee-replacement/florida/", "/costs/knee-replacement/new-york/"):
        html = client.get(path).text
        assert "Medicare surgeon fee" in html, path
        assert "15.9x" not in html and "4–18x" not in html, path
    assert "Hospitals must accept lower amounts" not in client.get("/costs/knee-replacement/new-york/").text


def test_procedure_cost_guides_are_not_shadowed():
    from main import app as main_app
    paths = [r.path for r in main_app.routes]
    assert paths.index("/procedures/{slug}-cost/") < paths.index("/procedures/{slug}/")
