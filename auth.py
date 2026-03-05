"""Authentication for BillKarma Advocacy Workspace.

Email + password auth with bcrypt hashing. Session-based (reuses existing cookie
infrastructure). Consumer flow continues to work without login.
"""

import re
import secrets
import logging

import bcrypt
from fastapi import HTTPException, Request

import config
from db import get_db
from access_control import SESSION_COOKIE_NAME

log = logging.getLogger(__name__)

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_SESSION_MAX_AGE = 60 * 60 * 24 * 45  # 45 days


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))


def validate_registration(email: str, password: str, name: str) -> None:
    """Raise HTTPException if inputs are invalid."""
    if not email or not _EMAIL_RE.fullmatch(email.strip()):
        raise HTTPException(400, "Valid email required")
    if not password or len(password) < 8:
        raise HTTPException(400, "Password must be at least 8 characters")
    if not name or not name.strip():
        raise HTTPException(400, "Name is required")
    if len(name.strip()) > 200:
        raise HTTPException(400, "Name too long")


def register_user(email: str, password: str, name: str) -> dict:
    """Create a new user account. Returns user dict with id, email, name."""
    email = email.strip().lower()
    name = name.strip()
    validate_registration(email, password, name)

    pw_hash = hash_password(password)
    with get_db() as db:
        existing = db.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()
        if existing:
            raise HTTPException(409, "Email already registered")

        cursor = db.execute(
            "INSERT INTO users (email, name, password_hash) VALUES (?, ?, ?)",
            (email, name, pw_hash),
        )
        user_id = cursor.lastrowid

        # Auto-join any pending org invites for this email
        db.execute(
            "UPDATE org_members SET user_id = ?, status = 'active' WHERE invite_email = ? AND status = 'invited'",
            (user_id, email),
        )

    return {"id": user_id, "email": email, "name": name}


def login_user(email: str, password: str) -> dict:
    """Verify credentials. Returns user dict or raises 401."""
    email = (email or "").strip().lower()
    if not email or not password:
        raise HTTPException(401, "Invalid email or password")

    with get_db() as db:
        row = db.execute(
            "SELECT id, email, name, password_hash FROM users WHERE email = ?",
            (email,),
        ).fetchone()

    if not row or not row["password_hash"]:
        raise HTTPException(401, "Invalid email or password")

    if not verify_password(password, row["password_hash"]):
        raise HTTPException(401, "Invalid email or password")

    return {"id": row["id"], "email": row["email"], "name": row["name"]}


def create_auth_session(user_id: int) -> str:
    """Create an authenticated session token and store it."""
    token = secrets.token_hex(32)
    with get_db() as db:
        db.execute(
            "INSERT INTO auth_sessions (token, user_id) VALUES (?, ?)",
            (token, user_id),
        )
    return token


def get_current_user(request: Request) -> dict | None:
    """Return the authenticated user from session cookie, or None."""
    token = request.cookies.get("bk_auth")
    if not token:
        return None

    with get_db() as db:
        row = db.execute(
            """
            SELECT u.id, u.email, u.name
            FROM auth_sessions s JOIN users u ON s.user_id = u.id
            WHERE s.token = ? AND s.expires_at > datetime('now')
            """,
            (token,),
        ).fetchone()

    if not row:
        return None
    return {"id": row["id"], "email": row["email"], "name": row["name"]}


def require_auth(request: Request) -> dict:
    """Return current user or raise 401."""
    user = get_current_user(request)
    if not user:
        raise HTTPException(401, "Authentication required")
    return user


def invalidate_session(token: str) -> None:
    """Delete an auth session."""
    with get_db() as db:
        db.execute("DELETE FROM auth_sessions WHERE token = ?", (token,))
