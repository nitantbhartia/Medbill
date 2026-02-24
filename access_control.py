"""Session-scoped access control for bill/case resources.

This app has no login yet, so we bind bill access to a browser session cookie.
Only the browser that created/continued a case can read/mutate its bill/case data.
"""

from __future__ import annotations

import re
import secrets

from fastapi import HTTPException, Request
from fastapi.responses import Response

import config
from db import get_db

SESSION_COOKIE_NAME = "bk_sid"
_SESSION_RE = re.compile(r"^[0-9a-f]{32}$")
_SESSION_MAX_AGE_SECONDS = 60 * 60 * 24 * 45  # 45 days


def _client_ip(request: Request) -> str:
    return request.client.host if request.client else "unknown"


def is_admin_request(request: Request) -> bool:
    token = (config.ADMIN_API_TOKEN or "").strip()
    if token:
        presented = request.headers.get("x-admin-token", "")
        return bool(presented and secrets.compare_digest(presented, token))

    # Local fallback for non-production when no admin token is configured.
    if config.ENV != "production" and _client_ip(request) in {"127.0.0.1", "::1", "testclient"}:
        return True
    return False


def get_session_id(request: Request) -> str | None:
    sid = (request.cookies.get(SESSION_COOKIE_NAME) or "").strip()
    if not sid:
        return None
    if not _SESSION_RE.fullmatch(sid):
        return None
    return sid


def get_or_create_session_id(request: Request) -> tuple[str, bool]:
    existing = get_session_id(request)
    if existing:
        return existing, False
    return secrets.token_hex(16), True


def set_session_cookie(response: Response, session_id: str) -> None:
    response.set_cookie(
        SESSION_COOKIE_NAME,
        session_id,
        max_age=_SESSION_MAX_AGE_SECONDS,
        httponly=True,
        secure=not config.DEBUG,
        samesite="lax",
        path="/",
    )


def grant_bill_access(session_id: str, bill_id: int) -> None:
    with get_db() as db:
        db.execute(
            """
            INSERT OR IGNORE INTO bill_access_sessions (session_id, bill_id)
            VALUES (?, ?)
            """,
            (session_id, bill_id),
        )


def has_bill_access(session_id: str, bill_id: int) -> bool:
    with get_db() as db:
        row = db.execute(
            "SELECT 1 FROM bill_access_sessions WHERE session_id = ? AND bill_id = ? LIMIT 1",
            (session_id, bill_id),
        ).fetchone()
    return row is not None


def require_bill_access(request: Request, bill_id: int) -> None:
    if config.ENV != "production" and _client_ip(request) in {"127.0.0.1", "::1", "testclient"}:
        return
    if is_admin_request(request):
        return
    sid = get_session_id(request)
    if sid and has_bill_access(sid, bill_id):
        return
    raise HTTPException(403, "Access denied for this bill")


def require_case_access(request: Request, case_id: int) -> None:
    if is_admin_request(request):
        return
    with get_db() as db:
        row = db.execute(
            "SELECT bill_id FROM dispute_cases WHERE id = ?",
            (case_id,),
        ).fetchone()
    if not row:
        raise HTTPException(404, "Case not found")
    require_bill_access(request, int(row["bill_id"]))
