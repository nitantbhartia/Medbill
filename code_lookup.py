"""B14.7: a bill line with a description but no billing code gets its code from the hospital's own price list."""

from __future__ import annotations

import json
import re
from difflib import get_close_matches

import config
from db import get_db

BILLING_CODE = re.compile(r"[0-9]{4}[0-9A-Z]|[A-Z][0-9]{4}")
CODE_SOURCE = "hospital_lookup"


def normalize_description(text: str | None) -> str:
    """Uppercase, expand the abbreviations in config, drop punctuation and extra spaces. Used for price files and bills alike."""
    words = re.sub(r"[^A-Z0-9/\- ]", " ", (text or "").upper()).split()
    expanded = " ".join(config.DESCRIPTION_ABBREVIATIONS.get(word, word) for word in words)
    return re.sub(r"\s+", " ", re.sub(r"[^A-Z0-9 ]", " ", expanded)).strip()


def record(facility_id: str, description: str | None, cpt_code: str | None, source: str, source_url: str | None = None) -> None:
    code = (cpt_code or "").strip().upper()
    norm = normalize_description(description)
    if not facility_id or not norm or not BILLING_CODE.fullmatch(code):
        return
    with get_db() as db:
        db.execute(
            "INSERT INTO hospital_code_lookup (facility_id, description_norm, cpt_code, source, source_url) VALUES (?, ?, ?, ?, ?) "
            "ON CONFLICT(facility_id, description_norm, cpt_code) DO UPDATE SET seen_count = seen_count + 1, updated_at = CURRENT_TIMESTAMP",
            (facility_id, norm, code, source, source_url),
        )


def _codes_for(facility_id: str, description_norm: str) -> list[dict]:
    with get_db() as db:
        rows = db.execute("SELECT cpt_code FROM hospital_code_lookup WHERE facility_id = ? AND description_norm = ? ORDER BY seen_count DESC, cpt_code",
                          (facility_id, description_norm)).fetchall()
    return [{"code": row["cpt_code"], "description": description_norm.title()} for row in rows]


def lookup(facility_id: str, description: str) -> dict | None:
    """{"kind": "exact"|"close"|"ambiguous", "choices": [{code, description}]}, or None when the hospital's list has nothing."""
    norm = normalize_description(description)
    if not norm:
        return None
    exact = _codes_for(facility_id, norm)
    if len(exact) == 1:
        return {"kind": "exact", "choices": exact}
    if exact:
        return {"kind": "ambiguous", "choices": exact}
    with get_db() as db:
        known = [row["description_norm"] for row in db.execute("SELECT DISTINCT description_norm FROM hospital_code_lookup WHERE facility_id = ?", (facility_id,))]
    close = get_close_matches(norm, known, n=1, cutoff=config.CODE_LOOKUP_MIN_SIMILARITY)
    if not close:
        return None
    return {"kind": "close", "choices": _codes_for(facility_id, close[0])}


def fill_codes(extracted: dict, hospital: dict | None) -> None:
    """Fill codes on lines that have a description and no valid code. Only an exact single match is used silently;
    anything else is sent to the confirm sheet with the choices."""
    if not hospital:
        return
    for item in extracted.get("line_items") or []:
        if item.get("cpt_code") or not item.get("description") or item.get("needs_confirm"):
            continue
        found = lookup(hospital["facility_id"], item["description"])
        if not found:
            continue
        if found["kind"] == "exact":
            item["cpt_code"], item["code_source"] = found["choices"][0]["code"], CODE_SOURCE
            continue
        item.update(needs_confirm=True, issue_kind="code_lookup", issue_field="cpt_code",
                    issue_choices=json.dumps({"hospital": hospital["name"], "choices": found["choices"]}))


def coverage() -> dict:
    """Lines with no code before the lookup (no code now, or filled from the hospital's list) and after."""
    with get_db() as db:
        row = db.execute("SELECT COUNT(*) AS lines, SUM(cpt_code IS NULL OR cpt_code = '') AS none_after, "
                         "SUM(code_source = ?) AS filled FROM line_items", (CODE_SOURCE,)).fetchone()
    lines, none_after, filled = row["lines"] or 0, row["none_after"] or 0, row["filled"] or 0
    return {"lines": lines,
            "no_code_share_before": round((none_after + filled) / lines, 4) if lines else None,
            "no_code_share_after": round(none_after / lines, 4) if lines else None}


def load_chargemaster(rows, source_url: str | None = None) -> dict:
    """Rows of {"facility_name", "description", "code"} from a hospital's filed chargemaster. A row is used only when
    its hospital matches one we know with enough confidence; the others are counted, never guessed."""
    from analyzer import find_hospital_match

    loaded = skipped = 0
    facility_by_name: dict[str, str | None] = {}
    for row in rows:
        name = row["facility_name"]
        if name not in facility_by_name:
            match = find_hospital_match(name, None)
            facility_by_name[name] = match["facility_id"] if match and match["match_confidence"] >= config.HCAI_NAME_MATCH_MIN else None
        if not facility_by_name[name]:
            skipped += 1
            continue
        record(facility_by_name[name], row["description"], row["code"], "chargemaster", source_url)
        loaded += 1
    return {"loaded": loaded, "skipped_unknown_hospital": skipped}
