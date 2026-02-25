"""Tests for killer features: Bill Score, Savings Feed, Price Shopper, Bill Watch."""

from fastapi.testclient import TestClient

from main import app
from db import get_db

client = TestClient(app, raise_server_exceptions=False)


def _seed_bill_with_findings():
    """Insert a test bill with findings for score testing."""
    with get_db() as db:
        db.execute(
            "INSERT INTO bills (id, provider_name, provider_address, total_charged, total_patient_owes, "
            "total_findings, total_potential_savings, status, zip_code) "
            "VALUES (9999, 'Test Hospital', '123 Main St', 5000, 2000, 3, 800, 'analyzed', '10001')"
        )
        db.execute(
            "INSERT INTO line_items (bill_id, cpt_code, description, charged_amount, medicare_rate, markup_multiple) "
            "VALUES (9999, '99284', 'ER Visit Level 4', 3000, 600, 5.0)"
        )
        db.execute(
            "INSERT INTO line_items (bill_id, cpt_code, description, charged_amount, medicare_rate, markup_multiple) "
            "VALUES (9999, '71045', 'Chest X-Ray', 2000, 100, 20.0)"
        )
        db.execute(
            "INSERT INTO findings (bill_id, finding_type, severity, confidence, potential_savings, message, details) "
            "VALUES (9999, 'price_markup', 'high', 'high', 500, 'High markup', '{}')"
        )
        db.execute(
            "INSERT INTO findings (bill_id, finding_type, severity, confidence, potential_savings, message, details) "
            "VALUES (9999, 'duplicate_charge', 'high', 'high', 200, 'Duplicate', '{}')"
        )
        db.execute(
            "INSERT INTO findings (bill_id, finding_type, severity, confidence, potential_savings, message, details) "
            "VALUES (9999, 'unbundling', 'medium', 'medium', 100, 'Unbundling', '{}')"
        )
        db.execute(
            "INSERT OR IGNORE INTO bill_access_sessions (session_id, bill_id) VALUES ('test-session', 9999)"
        )


# --- Bill Health Score Tests ---


def test_compute_score_structure():
    _seed_bill_with_findings()
    from bill_score import compute_bill_score
    score = compute_bill_score(9999)
    assert score is not None
    assert 0 <= score["score"] <= 100
    assert score["grade"] in ("A", "B", "C", "D", "F")
    assert score["bill_id"] == 9999
    assert score["finding_count"] == 3
    assert score["potential_savings"] > 0
    assert len(score["share_token"]) == 12
    assert score["deductions"]


def test_score_decreases_with_findings():
    _seed_bill_with_findings()
    from bill_score import compute_bill_score
    score = compute_bill_score(9999)
    assert score["score"] < 100


def test_score_nonexistent_bill():
    from bill_score import compute_bill_score
    assert compute_bill_score(0) is None


def test_share_token_lookup():
    _seed_bill_with_findings()
    from bill_score import compute_bill_score, get_score_by_token
    score = compute_bill_score(9999)
    found = get_score_by_token(score["share_token"])
    assert found is not None
    assert found["bill_id"] == 9999
    assert found["score"] == score["score"]


def test_invalid_share_token():
    from bill_score import get_score_by_token
    assert get_score_by_token("nonexistent123") is None


def test_score_api_endpoint():
    _seed_bill_with_findings()
    resp = client.get("/api/score/9999", cookies={"bk_session": "test-session"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["data"]["score"] >= 0


def test_score_page_renders():
    _seed_bill_with_findings()
    resp = client.get("/score/9999", cookies={"bk_session": "test-session"})
    assert resp.status_code == 200
    assert "Bill Health Score" in resp.text


def test_public_share_page():
    _seed_bill_with_findings()
    from bill_score import compute_bill_score
    score = compute_bill_score(9999)
    resp = client.get(f"/score/share/{score['share_token']}")
    assert resp.status_code == 200
    assert "Bill Health Score" in resp.text


# --- Savings Feed Tests ---


def test_aggregate_stats():
    from savings_feed import get_aggregate_stats
    stats = get_aggregate_stats()
    assert "bills_analyzed" in stats
    assert "total_savings_found" in stats
    assert "total_issues_found" in stats
    assert "top_finding_types" in stats


def test_recent_savings():
    _seed_bill_with_findings()
    from savings_feed import get_recent_savings
    feed = get_recent_savings(10)
    assert isinstance(feed, list)
    if feed:
        item = feed[0]
        assert "finding_label" in item
        assert "savings" in item
        assert "provider_hint" in item


def test_savings_feed_page():
    resp = client.get("/savings")
    assert resp.status_code == 200
    assert "Community Savings" in resp.text


def test_savings_api_stats():
    resp = client.get("/api/savings/stats")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"


def test_savings_api_feed():
    resp = client.get("/api/savings/feed?limit=5")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert isinstance(data["data"], list)


# --- Price Shopper Tests ---


def test_shop_without_params_returns_empty():
    from price_shopper import shop_for_procedure
    result = shop_for_procedure("", "")
    assert result["providers"] == []


def test_shop_page_renders_empty():
    resp = client.get("/shop")
    assert resp.status_code == 200
    assert "Shop Before You Go" in resp.text


def test_shop_page_with_params():
    resp = client.get("/shop?cpt=99284&zip=10001")
    assert resp.status_code == 200


def test_shop_api_requires_zip():
    resp = client.get("/api/shop/99284")
    assert resp.status_code == 400


def test_shop_api_with_params():
    resp = client.get("/api/shop/99284?zip=10001")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"


# --- Bill Watch Tests ---


def test_create_watch():
    from bill_watch import add_watch
    result = add_watch("test@example.com", "provider", "Memorial Hospital")
    assert result["ok"] is True


def test_create_watch_invalid_email():
    from bill_watch import add_watch
    result = add_watch("not-an-email", "provider", "Memorial Hospital")
    assert result["ok"] is False


def test_create_watch_invalid_type():
    from bill_watch import add_watch
    result = add_watch("test@example.com", "invalid_type", "test")
    assert result["ok"] is False


def test_create_watch_empty_value():
    from bill_watch import add_watch
    result = add_watch("test@example.com", "provider", "")
    assert result["ok"] is False


def test_list_watches():
    from bill_watch import add_watch, get_watches_for_email
    add_watch("list@example.com", "procedure", "99284")
    watches = get_watches_for_email("list@example.com")
    assert isinstance(watches, list)
    assert len(watches) >= 1


def test_duplicate_watch_rejected():
    from bill_watch import add_watch
    add_watch("dup@example.com", "provider", "Same Hospital")
    result = add_watch("dup@example.com", "provider", "Same Hospital")
    assert result["ok"] is False


def test_remove_watch():
    from bill_watch import add_watch, get_watches_for_email, remove_watch
    add_watch("remove@example.com", "procedure", "99284")
    watches = get_watches_for_email("remove@example.com")
    assert len(watches) == 1
    result = remove_watch(watches[0]["id"], "remove@example.com")
    assert result["ok"] is True
    watches_after = get_watches_for_email("remove@example.com")
    assert len(watches_after) == 0


def test_max_watches_limit():
    from bill_watch import add_watch, MAX_WATCHES_PER_EMAIL
    for i in range(MAX_WATCHES_PER_EMAIL):
        add_watch("limit@example.com", "provider", f"Hospital {i}")
    result = add_watch("limit@example.com", "provider", "One Too Many")
    assert result["ok"] is False
    assert "Maximum" in result["error"]


def test_watch_page_renders():
    resp = client.get("/watch")
    assert resp.status_code == 200
    assert "Price Watch" in resp.text


def test_watch_api_create():
    resp = client.post("/api/watch", json={
        "email": "api@example.com",
        "watch_type": "provider",
        "watch_value": "API Hospital",
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"


def test_watch_api_list():
    client.post("/api/watch", json={
        "email": "api2@example.com",
        "watch_type": "provider",
        "watch_value": "API Hospital 2",
    })
    resp = client.get("/api/watches?email=api2@example.com")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert len(data["watches"]) >= 1


def test_watch_api_list_no_email():
    resp = client.get("/api/watches")
    assert resp.status_code == 400
