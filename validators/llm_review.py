"""Optional second look (LLM_REVIEW_ENABLED): a model may keep or downgrade a finding. It cannot add, re-price or upgrade."""

import json
import logging

from google import genai
from google.genai import types

import config
from validators.innocent_explanations import SEVERITY_DOWN

log = logging.getLogger(__name__)

MAX_EXPLANATION_CHARS = 200


def apply_reviews(findings: list[dict], reviews: object) -> None:
    """Apply `[{"index": 0, "verdict": "keep"|"downgrade", "explanation": "..."}]`. Anything else is ignored."""
    if not isinstance(reviews, list):
        return
    for review in reviews:
        if not isinstance(review, dict) or review.get("verdict") != "downgrade":
            continue
        index = review.get("index")
        if not isinstance(index, int) or isinstance(index, bool) or not 0 <= index < len(findings):
            continue
        finding = findings[index]
        if finding.get("severity") not in SEVERITY_DOWN or finding.get("innocent_reason"):
            continue
        finding["severity"] = SEVERITY_DOWN[finding["severity"]]
        finding["llm_note"] = str(review.get("explanation") or "")[:MAX_EXPLANATION_CHARS]


def _ask_model(line_items: list[dict], findings: list[dict]) -> object:
    lines = [{k: item.get(k) for k in ("cpt_code", "description", "quantity", "charged_amount", "modifiers", "date_of_service")} for item in line_items]
    flagged = [{"index": i, "type": f.get("type"), "code": (f.get("line_item") or {}).get("cpt_code"), "severity": f.get("severity")} for i, f in enumerate(findings)]
    prompt = (
        "These are the line items of a hospital bill and the problems an automatic checker flagged. For each flagged problem, "
        "give the most plausible legitimate explanation on this bill. Answer only with a JSON list of "
        '{"index": number, "verdict": "keep" or "downgrade", "explanation": "one sentence"}.\n'
        f"Line items: {json.dumps(lines)}\nFlagged: {json.dumps(flagged)}"
    )
    client = genai.Client(api_key=config.GEMINI_API_KEY)
    response = client.models.generate_content(
        model=config.GEMINI_MODEL, contents=prompt,
        config=types.GenerateContentConfig(temperature=0, response_mime_type="application/json"),
    )
    return json.loads(response.text)


def review_findings(line_items: list[dict], findings: list[dict], ask=_ask_model) -> None:
    if not config.LLM_REVIEW_ENABLED or not config.GEMINI_API_KEY or not findings:
        return
    try:
        reviews = ask(line_items, findings)
    except (json.JSONDecodeError, TypeError, ValueError, OSError, genai.errors.APIError) as error:
        log.error("LLM review failed for %d findings, leaving them unchanged: %s", len(findings), error)
        return
    apply_reviews(findings, reviews)
