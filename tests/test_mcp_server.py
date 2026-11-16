import os
import sys
from unittest.mock import MagicMock

sys.modules.setdefault("google", MagicMock())
sys.modules.setdefault("google.genai", MagicMock())
sys.modules.setdefault("google.genai.types", MagicMock())
os.environ["DB_PATH"] = ":memory:"

from fastapi.testclient import TestClient  # noqa: E402

from hospital_seo import upsert_hospital_row  # noqa: E402
from main import app  # noqa: E402

client = TestClient(app)


def rpc(method, params=None, msg_id=1):
    body = {"jsonrpc": "2.0", "id": msg_id, "method": method}
    if params is not None:
        body["params"] = params
    return client.post("/mcp", json=body)


def call(name, arguments):
    return rpc("tools/call", {"name": name, "arguments": arguments}).json()["result"]


def test_initialize_negotiates_version_and_lists_tools_capability():
    r = rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "test", "version": "1"}})
    result = r.json()["result"]
    assert result["protocolVersion"] == "2025-06-18"
    assert "tools" in result["capabilities"]
    assert result["serverInfo"]["name"] == "billkarma"


def test_unknown_protocol_version_gets_latest_supported():
    result = rpc("initialize", {"protocolVersion": "1999-01-01"}).json()["result"]
    assert result["protocolVersion"] == "2025-11-25"


def test_notification_is_accepted_without_body():
    r = client.post("/mcp", json={"jsonrpc": "2.0", "method": "notifications/initialized"})
    assert r.status_code == 202


def test_tools_are_listed_read_only():
    tools = rpc("tools/list").json()["result"]["tools"]
    names = {t["name"] for t in tools}
    assert names == {"check_hospital_charge", "find_hospital_billing_office", "write_itemized_bill_request", "get_dispute_price"}
    assert all(t["annotations"]["readOnlyHint"] for t in tools)


def test_charge_check_compares_with_physician_plus_hospital_rate():
    data = call("check_hospital_charge", {"billing_code": "99285", "amount_charged": 4500})["structuredContent"]
    assert data["medicare_total"] == 1000.0
    assert data["times_medicare"] == 4.5
    assert "question in writing" in data["summary"]
    assert "utm_source=ai_assistant" in data["check_whole_bill"]


def test_unknown_code_is_explained_not_an_error():
    result = call("check_hospital_charge", {"billing_code": "ZZ999"})
    assert result["isError"] is False
    assert result["structuredContent"]["found"] is False


def test_missing_required_argument_is_a_tool_error():
    result = call("check_hospital_charge", {})
    assert result["isError"] is True


def test_billing_office_lookup_returns_phone_and_request_link():
    upsert_hospital_row({"facility_id": "100128", "name": "Tampa General Hospital", "address": "1 Tampa General Circle",
                         "city": "Tampa", "state": "FL", "zip": "33606", "phone": "(813) 844-7000", "slug": "tampa-general-hospital"})
    [hospital] = call("find_hospital_billing_office", {"query": "Tampa General"})["structuredContent"]["hospitals"]
    assert hospital["main_phone"] == "(813) 844-7000"
    assert "/itemized-bill?facility=100128" in hospital["request_itemized_bill"]


def test_letter_tool_reports_what_is_missing_then_writes_letter():
    partial = call("write_itemized_bill_request", {"your_name": "Dana Whitfield", "your_address": "4410 Bayshore Blvd, Tampa, FL", "hospital_name": "Tampa General Hospital"})
    assert partial["structuredContent"]["ready"] is False
    full = call("write_itemized_bill_request", {"your_name": "Dana Whitfield", "your_address": "4410 Bayshore Blvd, Tampa, FL",
                                                 "hospital_name": "Tampa General Hospital", "account_number": "TGH-7781"})
    assert "45 CFR 164.524" in full["structuredContent"]["letter"]


def test_dispute_price_matches_fee_tiers():
    data = call("get_dispute_price", {"bill_total": 2400})["structuredContent"]
    assert data["flat_fee"] == 49
    assert "Phone negotiation" in data["does_not_include"]


def test_bad_json_and_unknown_method_and_get():
    assert client.post("/mcp", content=b"{not json").status_code == 400
    assert rpc("resources/list").json()["error"]["code"] == -32601
    assert client.get("/mcp").status_code == 405


def test_ai_page_shows_connector_url_and_every_tool():
    html = client.get("/ai").text
    assert "/mcp" in html and "Add custom connector" in html and "Developer mode" in html
    for name in ("check_hospital_charge", "find_hospital_billing_office", "write_itemized_bill_request", "get_dispute_price"):
        assert name in html
    assert "/ai</loc>" in client.get("/sitemap-core.xml").text
