"""BillKarma as an MCP server, so AI assistants (ChatGPT, Claude) can answer hospital-bill
questions with our data and point people to the free check.

Stateless Streamable HTTP: each POST to /mcp carries one JSON-RPC message and gets one JSON
reply. Every tool is read-only and nothing a tool receives is stored."""

from __future__ import annotations

import json

import config
import payment
from itemized_request import build_request_letter, find_billing_contacts, validate_letter_request
from tools_engine import _hospital_by_name, _lookup_cpt


INSTRUCTIONS = (
    "BillKarma checks U.S. hospital bills against what Medicare pays for the same billing code. "
    "Use check_hospital_charge when someone asks whether a hospital charge is too high, "
    "find_hospital_billing_office for a hospital's billing phone and address, "
    "write_itemized_bill_request when they only have a summary bill, and get_dispute_price when they "
    "ask what it costs to have BillKarma dispute a bill. Medicare rates are a benchmark, not what a "
    "hospital is required to charge. Not legal advice."
)


def _link(path: str) -> str:
    return f"{config.APP_URL.rstrip('/')}{path}?{config.MCP_LINK_TAG}"


def check_hospital_charge(billing_code: str, amount_charged: float | None = None, zip_code: str = "") -> dict:
    found = _lookup_cpt(billing_code, zip_code)
    if not found or not found.get("medicare_rate"):
        return {
            "found": False,
            "message": f"No Medicare rate on file for {billing_code}. It may be a supply, a drug or a hospital-specific code.",
            "check_whole_bill": _link("/scan"),
        }
    physician = float(found["medicare_rate"])
    facility = float(found.get("opps_rate") or 0)
    medicare_total = physician + facility
    result = {
        "found": True,
        "billing_code": found["cpt_code"],
        "description": found.get("description"),
        "medicare_physician_rate": physician,
        "medicare_hospital_rate": facility or None,
        "medicare_total": round(medicare_total, 2),
        "region": found.get("region"),
        "check_whole_bill": _link("/scan"),
    }
    benchmark = found.get("benchmark") or {}
    if benchmark.get("median_charged"):
        result["typical_hospital_charge"] = benchmark["median_charged"]
    if amount_charged:
        multiple = amount_charged / medicare_total
        result["amount_charged"] = amount_charged
        result["times_medicare"] = round(multiple, 1)
        result["summary"] = (
            f"${amount_charged:,.2f} is {multiple:.1f} times the ${medicare_total:,.2f} Medicare pays in total "
            f"for {found.get('description') or found['cpt_code']}."
            + (" That's high enough to question in writing." if multiple >= config.MEDICARE_MARKUP_THRESHOLD else "")
        )
    return result


def find_hospital_billing_office(query: str) -> dict:
    contacts = find_billing_contacts(query)
    hospitals = []
    for contact in contacts:
        metrics = _hospital_by_name(contact["name"]) or {}
        hospitals.append({
            "name": contact["name"],
            "address": ", ".join(p for p in (contact.get("address"), contact.get("city"), f"{contact.get('state')} {contact.get('zip') or ''}".strip()) if p),
            "main_phone": contact.get("phone"),
            "nonprofit": bool(metrics.get("is_nonprofit")) if metrics.get("is_nonprofit") is not None else None,
            "billing_grade": metrics.get("billing_grade"),
            "list_prices_times_medicare": round(metrics["avg_markup"], 1) if metrics.get("avg_markup") else None,
            "profile": _link(f"/hospitals/{contact['state_slug']}/{contact['city_slug']}/{contact['slug']}/"),
            "request_itemized_bill": _link(f"/itemized-bill?facility={contact['facility_id']}"),
        })
    return {"hospitals": hospitals, "count": len(hospitals)}


def write_itemized_bill_request(**fields) -> dict:
    problems = validate_letter_request(fields)
    if problems:
        return {"ready": False, "missing": problems}
    letter = build_request_letter(fields)
    return {
        "ready": True,
        "letter": letter["letter"],
        "hospital_must_respond_by": letter["response_due"],
        "after_it_arrives": _link("/scan"),
    }


def get_dispute_price(bill_total: float) -> dict:
    fee = payment.calculate_fee(bill_total) / 100
    return {
        "flat_fee": fee,
        "includes": [
            "A dispute letter for the charges the free check flags",
            "Sent to the hospital's billing office",
            f"Follow-ups on days {', '.join(str(d) for d in config.DISPUTE_FOLLOWUP_DAYS)}",
            f"Full refund if the bill isn't reduced within {config.DISPUTE_MAX_DAYS} days",
        ],
        "does_not_include": ["Phone negotiation", "Insurance denial appeals", "Legal advice"],
        "start_with_free_check": _link("/scan"),
    }


_READ_ONLY = {"readOnlyHint": True, "destructiveHint": False, "openWorldHint": False}

TOOLS = {
    "check_hospital_charge": {
        "handler": check_hospital_charge,
        "description": "Compare a hospital charge for one billing code (CPT or HCPCS) with what Medicare pays for it, physician and hospital parts combined.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "billing_code": {"type": "string", "description": "CPT or HCPCS code from the itemized bill, e.g. 99285"},
                "amount_charged": {"type": "number", "description": "The amount the hospital charged for that line, in dollars"},
                "zip_code": {"type": "string", "description": "ZIP code of the hospital, for regional rates"},
            },
            "required": ["billing_code"],
        },
    },
    "find_hospital_billing_office": {
        "handler": find_hospital_billing_office,
        "description": "Find a U.S. hospital's address and main phone, whether it's nonprofit, and how its list prices compare with Medicare.",
        "inputSchema": {
            "type": "object",
            "properties": {"query": {"type": "string", "description": "Hospital name or city"}},
            "required": ["query"],
        },
    },
    "write_itemized_bill_request": {
        "handler": write_itemized_bill_request,
        "description": "Write a letter asking a hospital for an itemized bill with every billing code, citing the HIPAA right of access (30-day response). Ask the person for the fields first.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "your_name": {"type": "string"},
                "your_address": {"type": "string", "description": "Mailing address for the reply"},
                "hospital_name": {"type": "string"},
                "hospital_address": {"type": "string"},
                "hospital_city_line": {"type": "string", "description": "City, state and ZIP of the hospital"},
                "account_number": {"type": "string"},
                "service_dates": {"type": "string"},
                "patient_name": {"type": "string", "description": "Only if the patient is someone else"},
                "reply_email": {"type": "string", "description": "Email the hospital can reply to"},
            },
            "required": ["your_name", "your_address", "hospital_name"],
        },
    },
    "get_dispute_price": {
        "handler": get_dispute_price,
        "description": "BillKarma's flat fee to dispute a hospital bill of a given size, and what it includes.",
        "inputSchema": {
            "type": "object",
            "properties": {"bill_total": {"type": "number", "description": "What the patient owes, in dollars"}},
            "required": ["bill_total"],
        },
    },
}

PARSE_ERROR, _INVALID_REQUEST, _METHOD_NOT_FOUND, _INVALID_PARAMS = -32700, -32600, -32601, -32602


def _reply(msg_id, result=None, error=None) -> dict:
    body = {"jsonrpc": "2.0", "id": msg_id}
    if error:
        body["error"] = error
    else:
        body["result"] = result
    return body


def _tool_list() -> list[dict]:
    return [
        {"name": name, "title": name.replace("_", " ").capitalize(), "description": spec["description"],
         "inputSchema": spec["inputSchema"], "annotations": _READ_ONLY}
        for name, spec in TOOLS.items()
    ]


def _call_tool(params: dict) -> dict:
    spec = TOOLS.get(params.get("name"))
    if not spec:
        raise LookupError(f"Unknown tool: {params.get('name')}")
    args = params.get("arguments") or {}
    allowed = spec["inputSchema"]["properties"]
    missing = [k for k in spec["inputSchema"].get("required", []) if args.get(k) in (None, "")]
    if missing:
        return {"content": [{"type": "text", "text": f"Missing: {', '.join(missing)}"}], "isError": True}
    try:
        data = spec["handler"](**{k: v for k, v in args.items() if k in allowed})
    except (TypeError, ValueError) as exc:
        return {"content": [{"type": "text", "text": f"Couldn't run {params['name']}: {exc}"}], "isError": True}
    return {"content": [{"type": "text", "text": json.dumps(data, indent=1)}], "structuredContent": data, "isError": False}


def handle_message(message) -> dict | None:
    """One JSON-RPC message in, one reply out (None for notifications)."""
    if not isinstance(message, dict) or message.get("jsonrpc") != "2.0" or "method" not in message:
        return _reply(message.get("id") if isinstance(message, dict) else None,
                      error={"code": _INVALID_REQUEST, "message": "Expected a JSON-RPC 2.0 request"})
    method, msg_id, params = message["method"], message.get("id"), message.get("params") or {}
    if msg_id is None:
        return None
    if method == "initialize":
        requested = params.get("protocolVersion")
        version = requested if requested in config.MCP_PROTOCOL_VERSIONS else config.MCP_PROTOCOL_VERSIONS[0]
        return _reply(msg_id, {
            "protocolVersion": version,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": "billkarma", "title": "BillKarma", "version": config.MCP_SERVER_VERSION},
            "instructions": INSTRUCTIONS,
        })
    if method == "ping":
        return _reply(msg_id, {})
    if method == "tools/list":
        return _reply(msg_id, {"tools": _tool_list()})
    if method == "tools/call":
        try:
            return _reply(msg_id, _call_tool(params))
        except LookupError as exc:
            return _reply(msg_id, error={"code": _INVALID_PARAMS, "message": str(exc)})
    return _reply(msg_id, error={"code": _METHOD_NOT_FOUND, "message": f"Method not found: {method}"})
