"""B16.7: how often each rule is right, from hospital outcomes. A rule that is mostly rejected is demoted to "worth asking",
and the demotion is lifted after a month back above the line. Every change is logged and emailed."""

import json
import logging
from html import escape

import config
import email_service
from db import get_db

log = logging.getLogger(__name__)

EVERYWHERE = ""


def rule_precision(facility_id: str = EVERYWHERE) -> dict:
    """{rule_id: (wins, total)}: a win is a verified saving, a loss is a rejection. Rules under OUTCOME_MIN_SAMPLE are left out."""
    where, args = ("AND facility_id = ?", (facility_id,)) if facility_id else ("", ())
    with get_db() as db:
        wins = db.execute(f"SELECT rule_ids FROM dispute_outcomes WHERE verified = 1 AND actual_savings > 0 {where}", args).fetchall()
        losses = db.execute(f"SELECT rejected_rule_ids FROM dispute_outcomes WHERE rejected_rule_ids IS NOT NULL {where}", args).fetchall()
    counts: dict[str, list[int]] = {}
    for rows, column, index in ((wins, "rule_ids", 0), (losses, "rejected_rule_ids", 1)):
        for row in rows:
            for rule_id in set(json.loads(row[column] or "[]")):
                counts.setdefault(rule_id, [0, 0])[index] += 1
    return {rule: (won, won + lost) for rule, (won, lost) in counts.items() if won + lost >= config.OUTCOME_MIN_SAMPLE}


def _scopes() -> list[str]:
    with get_db() as db:
        rows = db.execute("SELECT DISTINCT facility_id FROM dispute_outcomes WHERE facility_id IS NOT NULL").fetchall()
    return [EVERYWHERE] + [row["facility_id"] for row in rows]


def _update_scope(facility_id: str, changes: list[str]) -> None:
    where = "facility name " + facility_id if facility_id else "all hospitals"
    for rule_id, (won, total) in rule_precision(facility_id).items():
        precision = round(won / total, 2)
        with get_db() as db:
            active = db.execute("SELECT * FROM rule_demotions WHERE rule_id = ? AND facility_id = ? AND lifted_at IS NULL",
                                (rule_id, facility_id)).fetchone()
            if precision < config.RULE_DEMOTE_PRECISION and not active:
                db.execute("INSERT INTO rule_demotions (rule_id, facility_id, precision, sample) VALUES (?, ?, ?, ?)",
                           (rule_id, facility_id, precision, total))
                changes.append(f"Demoted {rule_id} for {where}: {won} of {total} outcomes held up ({precision:.0%}).")
            elif precision < config.RULE_DEMOTE_PRECISION and active:
                db.execute("UPDATE rule_demotions SET above_since = NULL WHERE id = ?", (active["id"],))
            elif active and not active["above_since"]:
                db.execute("UPDATE rule_demotions SET above_since = CURRENT_TIMESTAMP WHERE id = ?", (active["id"],))
            elif active and db.execute("SELECT ? <= datetime('now', ?) AS due", (active["above_since"], f"-{config.RULE_LIFT_DAYS} days")).fetchone()["due"]:
                db.execute("UPDATE rule_demotions SET lifted_at = CURRENT_TIMESTAMP WHERE id = ?", (active["id"],))
                changes.append(f"Lifted the demotion of {rule_id} for {where}: back at {precision:.0%} for {config.RULE_LIFT_DAYS} days.")


def nightly_update() -> list[str]:
    changes: list[str] = []
    for facility_id in _scopes():
        _update_scope(facility_id, changes)
    if not changes:
        return changes
    with get_db() as db:
        db.execute("INSERT INTO data_quality_runs (status, coverage_json, checks_json, notes) VALUES (?, '[]', ?, ?)",
                   (config.RULE_DEMOTION_RUN_STATUS, json.dumps(changes), f"{len(changes)} rule demotion changes"))
    if config.OPS_NOTIFY_EMAIL:
        body = "".join(f"<p>{escape(line)}</p>" for line in changes)
        try:
            email_service.send_email(config.OPS_NOTIFY_EMAIL, "[BillKarma] Rule demotions changed", body)
        except RuntimeError as error:
            log.error("Could not email the rule demotion summary: %s", error)
    return changes


def demoted_rules(facility_id: str | None) -> set[str]:
    """Rules to show only as "worth asking" for this hospital: demoted everywhere, or at this hospital."""
    with get_db() as db:
        rows = db.execute("SELECT rule_id FROM rule_demotions WHERE lifted_at IS NULL AND facility_id IN (?, ?)",
                          (EVERYWHERE, facility_id or EVERYWHERE)).fetchall()
    return {row["rule_id"] for row in rows}
