"""B14.9: what an insurer allowed a hospital for a code, from a user's insurance statement. Stored only with the user's
data-improvement consent, with no name, member ID or claim number, and used when no hospital file has the rate."""

import hashlib
import statistics

import config
from code_lookup import BILLING_CODE
from db import get_db
from payer_rates import canonical_payer


def consented(device_id: str) -> bool:
    with get_db() as db:
        row = db.execute("SELECT data_improvement FROM mobile_devices WHERE device_id = ?", (device_id,)).fetchone()
    return bool(row and row["data_improvement"])


def record(bill_id: int, eob_data: dict, facility_id: str | None, confidence: float = config.EOB_OBSERVATION_CONFIDENCE_PHOTO) -> int:
    """One observation per statement line that has a code and an allowed amount. Returns how many were stored."""
    payer = canonical_payer(eob_data.get("insurer_name")) or eob_data.get("insurer_name")
    if not facility_id or not payer:
        return 0
    stored = 0
    with get_db() as db:
        for index, line in enumerate(eob_data.get("line_items") or []):
            code, allowed = str(line.get("cpt_code") or "").strip().upper(), line.get("allowed_amount")
            if not BILLING_CODE.fullmatch(code) or not isinstance(allowed, (int, float)) or allowed <= 0:
                continue
            source_ref = hashlib.sha256(f"{bill_id}:{index}".encode()).hexdigest()
            stored += db.execute(
                "INSERT OR IGNORE INTO price_observations (source_type, source_ref, code, facility_id, payer, plan_name, "
                "billed_amount, allowed_amount, event_date, confidence) VALUES ('eob', ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (source_ref, code, facility_id, payer, eob_data.get("plan_name"), line.get("charged_amount"), allowed,
                 line.get("date_of_service"), confidence),
            ).rowcount
    return stored


def peer_median(facility_id: str, code: str, insurer: str | None) -> dict | None:
    """The median allowed amount other users' statements show, or None under OUTCOME_MIN_SAMPLE observations."""
    payer = canonical_payer(insurer)
    if not payer:
        return None
    with get_db() as db:
        rows = db.execute("SELECT allowed_amount FROM price_observations WHERE source_type = 'eob' AND facility_id = ? "
                          "AND code = ? AND payer = ?", (facility_id, code, payer)).fetchall()
    if len(rows) < config.OUTCOME_MIN_SAMPLE:
        return None
    return {"payer": payer, "median": round(statistics.median(row["allowed_amount"] for row in rows), 2), "sample": len(rows)}
