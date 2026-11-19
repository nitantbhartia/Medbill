import config
import inbound_bills
import ocr_quality
import reply_reader
import scan_pipeline
from db import get_db
from validators import text_layer

TEXT = """Memorial Regional Hospital
99285 Emergency visit level 5   $4,520.00
71046 Chest X-ray 2 views   $850.00
Total charges $5,370.00"""


def test_text_layer_number_wins_over_a_misread_image_number():
    extracted = {"line_items": [
        {"cpt_code": "99285", "description": "ER visit", "charged_amount": 4250.00},
        {"cpt_code": "71046", "description": "Chest X-ray", "charged_amount": 850.00}]}
    fixed = text_layer.reconcile(extracted, TEXT)
    assert fixed == 1 and extracted["line_items"][0]["charged_amount"] == 4520.00
    assert extracted["line_items"][1]["charged_amount"] == 850.00 and not extracted["line_items"][1].get("needs_confirm")


def test_amount_that_is_nowhere_near_the_text_layer_goes_to_confirm():
    extracted = {"line_items": [{"cpt_code": "99285", "description": "ER visit", "charged_amount": 12.50}]}
    assert text_layer.reconcile(extracted, TEXT) == 0
    item = extracted["line_items"][0]
    assert item["needs_confirm"] and item["issue_kind"] == "text_layer_mismatch" and item["charged_amount"] == 12.50


def test_text_layer_is_cleaned_and_capped():
    assert text_layer.clean("a\x00b\x07c") == "abc"
    assert len(text_layer.clean("x" * (config.MAX_TEXT_LAYER_CHARS + 500))) == config.MAX_TEXT_LAYER_CHARS


def test_scan_passes_the_text_layer_and_records_the_input_kind(monkeypatch):
    seen = {}

    def fake_extract(images, text=None):
        seen["text"] = text
        return {"provider_name": "Memorial Regional Hospital", "total_charged": 5370.0, "total_patient_owes": 5370.0, "line_items": [
            {"cpt_code": "99285", "description": "ER visit", "quantity": 1, "charged_amount": 4250.0, "date_of_service": "2026-03-02"}]}

    monkeypatch.setattr(scan_pipeline, "extract_pages", fake_extract)
    bill_id, extracted, _ = scan_pipeline.run_scan([(b"pdf", "application/pdf")], "33021", None, None, text_layer=TEXT, input_kind="pdf_text")
    assert seen["text"].startswith("Memorial Regional Hospital")
    assert extracted["line_items"][0]["charged_amount"] == 4520.0
    with get_db() as db:
        assert db.execute("SELECT input_kind FROM bills WHERE id = ?", (bill_id,)).fetchone()["input_kind"] == "pdf_text"


def _device(device_id="dev1", zip_code="33021"):
    with get_db() as db:
        db.execute("INSERT INTO mobile_devices (device_id, token_hash, zip_code) VALUES (?, ?, ?)", (device_id, f"h-{device_id}", zip_code))
    return inbound_bills.address_for(device_id)


def _stub_mail(monkeypatch):
    monkeypatch.setattr(reply_reader, "fetch_inbound_email", lambda email_id: {"sender": "x@y.z", "subject": "bill", "body": "",
                        "attachments": [{"id": "a1", "content_type": "application/pdf"}, {"id": "a2", "content_type": "text/html"}]})
    monkeypatch.setattr(reply_reader, "fetch_attachment", lambda email_id, attachment_id: b"%PDF-bill")
    monkeypatch.setattr(scan_pipeline, "extract_pages", lambda images, text=None: {
        "provider_name": "Memorial Regional Hospital", "total_charged": 850.0, "total_patient_owes": 850.0, "line_items": [
            {"cpt_code": "71046", "description": "Chest X-ray", "quantity": 1, "charged_amount": 850.0, "date_of_service": "2026-03-02"}]})


def test_email_to_a_valid_address_creates_a_bill_the_device_can_see(monkeypatch):
    _stub_mail(monkeypatch)
    address = _device()
    assert address.startswith("bills+") and address.endswith("@billkarma.app")
    assert inbound_bills.address_for("dev1") == address  # stable
    assert inbound_bills.process("em1", [f"BillKarma <{address}>"]) == "created"
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) AS n FROM bills WHERE input_kind = 'email'").fetchone()["n"] == 1
        assert db.execute("SELECT COUNT(*) AS n FROM bill_access_sessions WHERE session_id = 'dev1'").fetchone()["n"] == 1


def test_email_to_an_unknown_address_creates_nothing(monkeypatch):
    _stub_mail(monkeypatch)
    _device()
    assert inbound_bills.process("em2", ["bills+deadbeefcafe@billkarma.app"]) == "dropped"
    assert inbound_bills.process("em3", ["support@billkarma.app"]) == "dropped"
    with get_db() as db:
        assert db.execute("SELECT COUNT(*) AS n FROM bills").fetchone()["n"] == 0


def test_email_without_a_usable_attachment_and_over_the_daily_limit(monkeypatch):
    _stub_mail(monkeypatch)
    address = _device()
    monkeypatch.setattr(reply_reader, "fetch_inbound_email", lambda email_id: {"sender": "", "subject": "", "body": "", "attachments": []})
    assert inbound_bills.process("em4", [address]) == "no_attachment"
    monkeypatch.setattr(config, "INBOUND_MAX_PER_DAY", 2)
    assert inbound_bills.process("em5", [address]) == "no_attachment"
    assert inbound_bills.process("em6", [address]) == "rate_limited"


def test_quality_numbers_are_reported_per_input_kind(monkeypatch):
    _stub_mail(monkeypatch)
    inbound_bills.process("em7", [_device()])
    numbers = ocr_quality.weekly_numbers()["by_input_kind"]
    assert numbers["email"]["scans"] == 1 and numbers["photo"]["scans"] == 0


def test_webhook_routes_a_private_address_to_the_bill_maker_and_everything_else_to_replies(monkeypatch):
    from fastapi.testclient import TestClient
    from main import app
    client = TestClient(app)
    monkeypatch.setattr(config, "INBOUND_WEBHOOK_SECRET", "s3cret")
    _stub_mail(monkeypatch)
    address = _device()
    event = {"type": "email.received", "data": {"email_id": "em9", "to": [address]}}
    response = client.post("/api/webhooks/inbound-email?token=s3cret", json=event)
    assert response.status_code == 200 and response.json()["data"]["outcome"] == "created"
    monkeypatch.setattr(reply_reader, "process_reply", lambda email_id: "ignored")
    other = client.post("/api/webhooks/inbound-email?token=s3cret", json={"type": "email.received", "data": {"email_id": "em10", "to": ["disputes@billkarma.app"]}})
    assert other.json()["data"]["outcome"] == "ignored"
    assert client.post("/api/webhooks/inbound-email?token=wrong", json=event).status_code == 403


def test_mobile_scan_accepts_a_text_layer_and_settings_shows_the_address(monkeypatch):
    from fastapi.testclient import TestClient
    from main import app
    client = TestClient(app)
    seen = {}
    monkeypatch.setattr(scan_pipeline, "extract_pages", lambda images, text=None: seen.update(text=text) or {
        "provider_name": "Memorial Regional Hospital", "total_charged": 850.0, "total_patient_owes": 850.0, "line_items": [
            {"cpt_code": "71046", "description": "Chest X-ray", "quantity": 1, "charged_amount": 850.0, "date_of_service": "2026-03-02"}]})
    data = client.post("/api/m/device", json={"app_version": "1.0.0"}).json()["data"]
    headers = {"Authorization": f"Bearer {data['token']}"}
    response = client.post("/api/m/scan", files=[("pages", ("bill.pdf", b"%PDF", "application/pdf"))],
                           data={"zip_code": "33021", "text_layer": "71046 Chest X-ray $850.00"}, headers=headers)
    assert response.status_code == 200 and seen["text"] == "71046 Chest X-ray $850.00"
    with get_db() as db:
        assert db.execute("SELECT input_kind FROM bills ORDER BY id DESC LIMIT 1").fetchone()["input_kind"] == "pdf_text"
    address = client.get("/api/m/inbound-address", headers=headers).json()["data"]["address"]
    assert address.startswith("bills+") and client.get("/api/m/inbound-address", headers=headers).json()["data"]["address"] == address
