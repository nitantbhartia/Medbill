"""Each hospital's own charity care rules, read from the policy it filed, with the exact sentence as proof.

California hospitals file their policies with HCAI, which posts them. The model reads the policy text, and nothing it
returns is kept unless its quoted sentence really appears in that text."""

from __future__ import annotations

import hashlib
import json
import re
from io import BytesIO
from urllib.request import Request, urlopen

import config
import scanner
from db import get_db
from google.genai import types

USER_AGENT = "Mozilla/5.0 (compatible; BillKarma policy research)"
TEXT_FIELDS = ("discount_rule", "asset_test", "application_deadline", "contact_phone")
LIST_FIELDS = ("presumptive_programs", "required_documents")
INCOME_FIELDS = ("free_care_max_fpl", "discount_max_fpl")

PROMPT = """You read a hospital's charity care and discount payment policy. Return JSON with exactly these keys.
Each key holds an object {{"value": ..., "quote": "..."}} or null. "quote" must be one sentence copied EXACTLY from the policy
that shows the value. If the policy does not say it, use null. Never guess or use outside knowledge.

free_care_max_fpl: whole number, the highest income as a percent of the federal poverty level that gets free care
discount_max_fpl: whole number, the highest income percent that gets a discount
discount_rule: text, how the discount is calculated (for example "capped at what Medicare pays")
asset_test: text, the rule on savings or assets, or null if the policy has none
presumptive_programs: list of programs that qualify a patient without an application (for example "Medi-Cal")
required_documents: list of documents the patient must send
application_deadline: text, the time limit to apply, or "no deadline" if the policy says there is none
contact_phone: text, the phone number for questions

POLICY TEXT:
{text}"""


def _get(url: str) -> bytes:
    with urlopen(Request(url, headers={"User-Agent": USER_AGENT}), timeout=60) as response:
        return response.read()


def pdf_text(pdf_bytes: bytes) -> str:
    from pypdf import PdfReader
    reader = PdfReader(BytesIO(pdf_bytes))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def fetch_policy(url: str) -> tuple[str, str]:
    """Download a policy PDF. Returns (sha256 of the file, its text). The text is empty for scanned images."""
    data = _get(url)
    if not data.startswith(b"%PDF"):
        raise ValueError("not a PDF")
    return hashlib.sha256(data).hexdigest(), pdf_text(data)


def _squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def _quote_is_real(quote, policy_text: str) -> bool:
    return isinstance(quote, str) and len(quote) > 8 and _squash(quote) in _squash(policy_text)


def _percent_in(quote: str, value) -> bool:
    return isinstance(value, int) and re.search(rf"\b{value}\s*(?:%|percent)", quote, re.I) is not None


def verify_terms(raw: dict, policy_text: str) -> tuple[dict, dict]:
    """Keep only fields whose quote is in the policy. An income limit must also appear in its quote."""
    terms, evidence = {}, {}
    for field in INCOME_FIELDS + TEXT_FIELDS + LIST_FIELDS:
        entry = raw.get(field)
        if not isinstance(entry, dict) or not _quote_is_real(entry.get("quote"), policy_text):
            continue
        value = entry.get("value")
        if field in INCOME_FIELDS and not _percent_in(entry["quote"], value):
            continue
        if field in LIST_FIELDS:
            value = [str(item).strip() for item in value if str(item).strip()] if isinstance(value, list) else None
        elif field in TEXT_FIELDS:
            value = str(value).strip() if value else None
        if value:
            terms[field], evidence[field] = value, entry["quote"]
    return terms, evidence


def apply_legal_floors(terms: dict, evidence: dict, state: str = "CA", rural: bool = False) -> dict:
    """California law: a non-rural hospital's discount limit can't be below 400% of the poverty level."""
    limit = terms.get("discount_max_fpl")
    if state == "CA" and not rural and limit is not None and limit < config.CA_CHARITY_CARE_FPL_FLOOR:
        evidence["discount_max_fpl_floor"] = (f"The policy says {limit}%; California law requires at least "
                                              f"{config.CA_CHARITY_CARE_FPL_FLOOR}% for non-rural hospitals.")
        terms["discount_max_fpl"] = config.CA_CHARITY_CARE_FPL_FLOOR
    return terms


def extract_policy_terms(text: str) -> tuple[dict, dict]:
    """Ask the model for the terms and quotes, then keep only what the policy text proves."""
    client = scanner._get_client()
    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=[PROMPT.format(text=text[: config.POLICY_MAX_TEXT_CHARS])],
        config=types.GenerateContentConfig(response_mime_type="application/json", temperature=0),
    )
    return verify_terms(scanner._parse_json_response(response.text), text)


def match_facility_id(name: str, zip_code: str | None) -> str | None:
    """Our CMS facility id for an HCAI hospital, by exact name or by name inside the same ZIP. None when unsure."""
    with get_db() as db:
        rows = db.execute("SELECT facility_id FROM hospitals WHERE lower(name) = lower(?)", (name,)).fetchall()
        if len(rows) != 1 and zip_code:
            rows = db.execute("SELECT facility_id FROM hospitals WHERE zip LIKE ? AND lower(name) LIKE ?",
                              (f"{zip_code[:5]}%", f"%{name.lower().split()[0]}%")).fetchall()
    return rows[0]["facility_id"] if len(rows) == 1 else None


def latest_hash(hcai_license: str) -> str | None:
    with get_db() as db:
        row = db.execute("SELECT document_sha256 FROM hospital_assistance_policies WHERE hcai_license = ? "
                         "AND review_status != 'rejected' ORDER BY id DESC LIMIT 1", (hcai_license,)).fetchone()
    return row["document_sha256"] if row else None


def save_policy(hospital: dict, source_url: str, sha256: str, effective_date: str | None, terms: dict, evidence: dict) -> int:
    with get_db() as db:
        cursor = db.execute(
            "INSERT INTO hospital_assistance_policies (facility_id, hospital_name, city, zip, hcai_license, source, source_url, "
            "document_sha256, effective_date, free_care_max_fpl, discount_max_fpl, discount_rule, asset_test, presumptive_programs, "
            "required_documents, application_deadline, application_form_url, contact_phone, evidence) "
            "VALUES (?, ?, ?, ?, ?, 'hcai', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (hospital.get("facility_id"), hospital["name"], hospital.get("city"), hospital.get("zip"), hospital.get("license"),
             source_url, sha256, effective_date, terms.get("free_care_max_fpl"), terms.get("discount_max_fpl"),
             terms.get("discount_rule"), terms.get("asset_test"), json.dumps(terms.get("presumptive_programs") or []),
             json.dumps(terms.get("required_documents") or []), terms.get("application_deadline"),
             hospital.get("application_form_url"), terms.get("contact_phone"), json.dumps(evidence)),
        )
        return cursor.lastrowid


def get_policy(facility_id: str) -> dict | None:
    """The newest policy for a hospital that hasn't been rejected, with each term next to its quote."""
    with get_db() as db:
        row = db.execute("SELECT * FROM hospital_assistance_policies WHERE facility_id = ? AND review_status != 'rejected' "
                         "ORDER BY id DESC LIMIT 1", (facility_id,)).fetchone()
    if not row:
        return None
    policy = dict(row)
    for field in LIST_FIELDS:
        policy[field] = json.loads(policy[field] or "[]")
    policy["evidence"] = json.loads(policy["evidence"] or "{}")
    return policy
