"""E-signature flow for HIPAA authorization, rep designation, and ToS."""

from __future__ import annotations

from db import get_db

ESIGN_VERSION = "1.0"

# Document types
HIPAA_AUTH = "hipaa_authorization"
REP_DESIGNATION = "representative_designation"
TERMS_OF_SERVICE = "terms_of_service"

ALL_DOCS = [HIPAA_AUTH, REP_DESIGNATION, TERMS_OF_SERVICE]


def get_or_create_session(bill_id: int, patient_name: str, patient_email: str) -> dict:
    """Get existing e-sign session for a bill or create a new one."""
    with get_db() as db:
        row = db.execute(
            "SELECT * FROM esign_records WHERE bill_id = ? ORDER BY created_at DESC LIMIT 1",
            (bill_id,),
        ).fetchone()
        if row:
            return dict(row)

        db.execute(
            """
            INSERT INTO esign_records (bill_id, patient_name, patient_email)
            VALUES (?, ?, ?)
            """,
            (bill_id, patient_name, patient_email),
        )
        row = db.execute(
            "SELECT * FROM esign_records WHERE bill_id = ? ORDER BY created_at DESC LIMIT 1",
            (bill_id,),
        ).fetchone()
        return dict(row)


def record_signature(
    bill_id: int,
    doc_type: str,
    ip_address: str,
    user_agent: str,
) -> None:
    """Record that a specific document was e-signed for a bill."""
    if doc_type not in ALL_DOCS:
        raise ValueError(f"Unknown doc_type: {doc_type}")

    col = {
        HIPAA_AUTH: "hipaa_signed_at",
        REP_DESIGNATION: "rep_signed_at",
        TERMS_OF_SERVICE: "tos_signed_at",
    }[doc_type]

    with get_db() as db:
        db.execute(
            f"""
            UPDATE esign_records
            SET {col} = CURRENT_TIMESTAMP, ip_address = ?, user_agent = ?
            WHERE bill_id = ?
            """,
            (ip_address, user_agent, bill_id),
        )


def get_status(bill_id: int) -> dict:
    """Return signing status for all three documents.

    Returns:
        dict with keys: session_id, patient_name, patient_email,
        hipaa_signed, rep_signed, tos_signed, all_signed
    """
    with get_db() as db:
        row = db.execute(
            "SELECT * FROM esign_records WHERE bill_id = ? ORDER BY created_at DESC LIMIT 1",
            (bill_id,),
        ).fetchone()

    if not row:
        return {
            "session_id": None,
            "patient_name": None,
            "patient_email": None,
            "hipaa_signed": False,
            "rep_signed": False,
            "tos_signed": False,
            "all_signed": False,
        }

    row = dict(row)
    hipaa = bool(row.get("hipaa_signed_at"))
    rep = bool(row.get("rep_signed_at"))
    tos = bool(row.get("tos_signed_at"))

    return {
        "session_id": row["id"],
        "patient_name": row["patient_name"],
        "patient_email": row["patient_email"],
        "hipaa_signed": hipaa,
        "rep_signed": rep,
        "tos_signed": tos,
        "all_signed": hipaa and rep and tos,
    }


def get_hipaa_text(patient_name: str, provider_name: str) -> str:
    """Return the HIPAA Authorization form text."""
    return f"""HIPAA AUTHORIZATION FOR RELEASE OF INFORMATION
AND AUTHORIZATION TO ACT AS AUTHORIZED REPRESENTATIVE

Patient Name: {patient_name}
Provider / Hospital: {provider_name}

1. AUTHORIZATION
I, {patient_name}, hereby authorize BillKarma, Inc. ("BillKarma") to:
   (a) Access and review my billing records, itemized statements, and Explanation of Benefits (EOB)
       related to the services described herein;
   (b) Communicate with {provider_name} and its billing department on my behalf;
   (c) Request, receive, and review any billing documentation necessary to dispute charges.

2. PURPOSE
The purpose of this authorization is to enable BillKarma to audit my medical bill for errors,
overcharges, and coding violations, and to submit a formal dispute on my behalf.

3. EXPIRATION
This authorization expires 12 months from the date of signing, or upon resolution of my dispute,
whichever occurs first.

4. RIGHT TO REVOKE
I understand that I may revoke this authorization at any time by contacting BillKarma in writing.
Revocation does not affect actions already taken in reliance on this authorization.

5. ACKNOWLEDGMENT
I understand that:
   - BillKarma is not a law firm and does not provide legal advice.
   - BillKarma is not a medical provider.
   - Outcomes of disputes are not guaranteed.
   - If BillKarma cannot resolve my dispute via written channels within 45 days, I am entitled
     to a full refund of my dispute fee.

Electronic signatures are valid under the Electronic Signatures in Global and National Commerce
Act (E-SIGN Act, 15 U.S.C. § 7001 et seq.)."""


def get_rep_designation_text(patient_name: str, provider_name: str) -> str:
    """Return the Authorized Representative Designation form text."""
    return f"""AUTHORIZED REPRESENTATIVE DESIGNATION

Patient Name: {patient_name}
Provider / Hospital: {provider_name}

I, {patient_name}, hereby designate BillKarma, Inc. as my Authorized Representative for purposes of:

   (a) Submitting formal billing disputes and requests for itemized statements;
   (b) Requesting billing corrections or adjustments;
   (c) Applying for financial assistance programs (including 501(r) charity care programs,
       if applicable);
   (d) Conducting all written correspondence with {provider_name} regarding my account.

This designation is limited to billing matters and does not grant authority to make medical
decisions on my behalf.

Hospitals and providers are required to work with authorized patient representatives under
45 C.F.R. § 164.524 and applicable state law."""


def get_tos_text() -> str:
    """Return the Terms of Service acceptance text."""
    return """BILLKARMA DISPUTE SERVICE — TERMS OF SERVICE

By signing below, you agree to the following:

1. SERVICE SCOPE
   BillKarma will audit your medical bill and submit a written dispute to your provider.
   We handle disputes via written channels (email/fax). We do not make phone calls on your behalf.

2. FEES
   You have paid a flat fee for this service. This fee covers the audit, dispute letter
   generation, initial submission, and up to 4 automated follow-ups over 45 days.

3. REFUND POLICY
   You are entitled to a full refund if:
   (a) BillKarma cannot resolve your dispute within 45 days of initial submission; OR
   (b) Your dispute cannot be handled via written channels (e.g., hospital requires a phone call).
   Refunds are not available if you received a billing correction, reduction, or adjustment.

4. NO GUARANTEES
   BillKarma does not guarantee that your bill will be reduced. Results depend on the
   hospital's response and the merits of your dispute.

5. NOT LEGAL ADVICE
   BillKarma provides an administrative dispute service, not legal advice. If you have
   legal questions, consult an attorney.

6. PRIVACY
   Your information is handled in accordance with BillKarma's Privacy Policy and our HIPAA
   obligations as a Business Associate."""
