"""Organization and team management for Advocacy Workspace."""

import logging

from fastapi import HTTPException, Request

from db import get_db
from auth import require_auth

log = logging.getLogger(__name__)

MAX_ORG_NAME_LEN = 200
MAX_EMAIL_LEN = 254


def create_org(request: Request, name: str, contact_email: str, org_type: str = "nonprofit") -> dict:
    """Create a new organization. The requesting user becomes admin."""
    user = require_auth(request)
    name = (name or "").strip()
    contact_email = (contact_email or "").strip().lower()

    if not name or len(name) > MAX_ORG_NAME_LEN:
        raise HTTPException(400, "Organization name required (max 200 chars)")
    if not contact_email or len(contact_email) > MAX_EMAIL_LEN:
        raise HTTPException(400, "Valid contact email required")
    if org_type not in ("nonprofit", "community", "other"):
        org_type = "nonprofit"

    with get_db() as db:
        cursor = db.execute(
            "INSERT INTO organizations (name, contact_email, org_type) VALUES (?, ?, ?)",
            (name, contact_email, org_type),
        )
        org_id = cursor.lastrowid
        db.execute(
            "INSERT INTO org_members (org_id, user_id, role, status) VALUES (?, ?, 'admin', 'active')",
            (org_id, user["id"]),
        )

    return {"id": org_id, "name": name, "contact_email": contact_email, "org_type": org_type}


def get_user_orgs(user_id: int) -> list[dict]:
    """Return all orgs the user belongs to."""
    with get_db() as db:
        rows = db.execute(
            """
            SELECT o.id, o.name, o.org_type, m.role
            FROM organizations o
            JOIN org_members m ON o.id = m.org_id
            WHERE m.user_id = ? AND m.status = 'active'
            """,
            (user_id,),
        ).fetchall()
    return [dict(r) for r in rows]


def get_org_members(org_id: int) -> list[dict]:
    """Return all members of an org."""
    with get_db() as db:
        rows = db.execute(
            """
            SELECT m.id, m.user_id, m.invite_email, m.role, m.status,
                   u.name, u.email
            FROM org_members m
            LEFT JOIN users u ON m.user_id = u.id
            WHERE m.org_id = ?
            ORDER BY m.created_at
            """,
            (org_id,),
        ).fetchall()
    return [dict(r) for r in rows]


def require_org_member(request: Request, org_id: int) -> dict:
    """Return user + membership info, or raise 403."""
    user = require_auth(request)
    with get_db() as db:
        row = db.execute(
            "SELECT role FROM org_members WHERE org_id = ? AND user_id = ? AND status = 'active'",
            (org_id, user["id"]),
        ).fetchone()
    if not row:
        raise HTTPException(403, "Not a member of this organization")
    return {**user, "org_role": row["role"]}


def require_org_writer(request: Request, org_id: int) -> dict:
    """Return user info if they have write access (admin or advocate). Viewers are rejected."""
    member = require_org_member(request, org_id)
    if member["org_role"] == "viewer":
        raise HTTPException(403, "Viewer role does not have write access")
    return member


def require_org_admin(request: Request, org_id: int) -> dict:
    """Return user info if they're an admin of the org, or raise 403."""
    member = require_org_member(request, org_id)
    if member["org_role"] != "admin":
        raise HTTPException(403, "Admin access required")
    return member


def invite_member(request: Request, org_id: int, email: str, role: str = "advocate") -> dict:
    """Invite a user to the org by email. If they already have an account, link them."""
    require_org_admin(request, org_id)
    email = (email or "").strip().lower()
    if not email:
        raise HTTPException(400, "Email required")
    if role not in ("admin", "advocate", "viewer"):
        role = "advocate"

    with get_db() as db:
        # Check if already a member
        existing = db.execute(
            """
            SELECT id FROM org_members
            WHERE org_id = ? AND (
                (user_id IS NOT NULL AND user_id = (SELECT id FROM users WHERE email = ?))
                OR invite_email = ?
            )
            """,
            (org_id, email, email),
        ).fetchone()
        if existing:
            raise HTTPException(409, "User already invited or is a member")

        # Check if user exists
        user_row = db.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()
        if user_row:
            db.execute(
                "INSERT INTO org_members (org_id, user_id, role, status) VALUES (?, ?, ?, 'active')",
                (org_id, user_row["id"], role),
            )
            return {"status": "active", "email": email, "role": role}

        # User doesn't exist yet — create invite
        db.execute(
            "INSERT INTO org_members (org_id, invite_email, role, status) VALUES (?, ?, ?, 'invited')",
            (org_id, email, role),
        )
        return {"status": "invited", "email": email, "role": role}


def remove_member(request: Request, org_id: int, member_id: int) -> None:
    """Remove a member from the org. Admins can't remove themselves if they're the last admin."""
    admin = require_org_admin(request, org_id)

    with get_db() as db:
        member = db.execute(
            "SELECT user_id, role FROM org_members WHERE id = ? AND org_id = ?",
            (member_id, org_id),
        ).fetchone()
        if not member:
            raise HTTPException(404, "Member not found")

        if member["user_id"] == admin["id"]:
            admin_count = db.execute(
                "SELECT COUNT(*) as cnt FROM org_members WHERE org_id = ? AND role = 'admin' AND status = 'active'",
                (org_id,),
            ).fetchone()["cnt"]
            if admin_count <= 1:
                raise HTTPException(400, "Cannot remove the last admin")

        db.execute("DELETE FROM org_members WHERE id = ? AND org_id = ?", (member_id, org_id))
