"""B14.9: do a hospital's published insurer rates match what insurers actually paid, per users' statements?"""

import json

import config
from db import get_db


def _file_rate(db, facility_id: str, code: str, payer: str) -> float | None:
    row = db.execute("SELECT AVG(COALESCE(negotiated_rate, median_allowed)) AS rate FROM price_observations "
                     "WHERE source_type = 'mrf' AND facility_id = ? AND code = ? AND payer = ?", (facility_id, code, payer)).fetchone()
    return row["rate"]


def check() -> dict:
    """Per hospital with enough statement lines to judge: the share of lines within MRF_MATCH_TOLERANCE_PCT of the file rate.
    A hospital whose files mostly don't match is marked mrf_reliability = 'low'. The result is saved in data_quality_runs."""
    report = {}
    with get_db() as db:
        facilities = db.execute("SELECT facility_id FROM price_observations WHERE source_type = 'eob' GROUP BY facility_id").fetchall()
        for facility in facilities:
            facility_id = facility["facility_id"]
            lines = db.execute("SELECT code, payer, allowed_amount FROM price_observations WHERE source_type = 'eob' AND facility_id = ?",
                               (facility_id,)).fetchall()
            compared = matched = 0
            for line in lines:
                rate = _file_rate(db, facility_id, line["code"], line["payer"])
                if rate is None:
                    continue
                compared += 1
                matched += abs(line["allowed_amount"] - rate) <= rate * config.MRF_MATCH_TOLERANCE_PCT / 100
            if compared < config.OUTCOME_MIN_SAMPLE:
                continue
            share = round(matched / compared, 2)
            reliability = "ok" if share >= config.MRF_RELIABILITY_MIN_MATCH_SHARE else "low"
            db.execute("UPDATE hospitals SET mrf_reliability = ? WHERE facility_id = ?", (reliability, facility_id))
            report[facility_id] = {"compared": compared, "within_tolerance_share": share, "mrf_reliability": reliability}
        db.execute("INSERT INTO data_quality_runs (status, coverage_json, checks_json, notes) VALUES (?, '[]', ?, 'MRF vs EOB truth check')",
                   (config.MRF_TRUTH_RUN_STATUS, json.dumps(report)))
    return report
