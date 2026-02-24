from html import escape as _he
import json
import logging
import re
import urllib.error
import urllib.request

import config

log = logging.getLogger(__name__)

RESEND_URL = "https://api.resend.com/emails"


def send_email(to: str, subject: str, html_body: str, text_body: str = "") -> bool:
    """
    Send an email via Resend.
    Returns True on success, False if Resend is not configured.
    Raises RuntimeError if configured but delivery fails.
    """
    if not config.RESEND_API_KEY:
        log.warning("RESEND_API_KEY not set — email to %s not sent", to)
        return False

    payload = {
        "to": [to],
        "from": f"{config.EMAIL_FROM_NAME} <{config.EMAIL_FROM_ADDRESS}>",
        "subject": subject,
        "text": text_body or _strip_tags(html_body),
        "html": html_body,
    }

    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        RESEND_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {config.RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status in (200, 201, 202):
                return True
            raise RuntimeError(f"Resend returned unexpected status {resp.status}")
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        log.error("Resend HTTP error %s: %s", e.code, body)
        raise RuntimeError(f"Resend error {e.code}: {body}") from e
    except OSError as e:
        log.error("Resend network error: %s", e)
        raise RuntimeError(f"Email delivery failed: {e}") from e


def _strip_tags(html: str) -> str:
    """Minimal HTML tag stripper for plain-text fallback."""
    return re.sub(r"<[^>]+>", "", html).strip()


def send_dispute_to_hospital(
    to: str,
    subject: str,
    letter_text: str,
    patient_name: str,
) -> bool:
    """Send a dispute letter to the hospital billing department."""
    html = (
        f"<p>This is a formal billing dispute submitted on behalf of patient "
        f"<strong>{_he(patient_name)}</strong> by BillKarma Patient Advocacy.</p>"
        f"<pre style='font-family:monospace;white-space:pre-wrap;'>{_he(letter_text)}</pre>"
        f"<p style='color:#666;font-size:12px;'>Submitted via BillKarma.app — "
        f"AI-assisted medical bill dispute service.</p>"
    )
    return send_email(to=to, subject=subject, html_body=html, text_body=letter_text)


def send_dispute_confirmation(
    to: str,
    patient_name: str,
    case_id: int,
    hospital_name: str,
) -> bool:
    """Confirm to the patient that their dispute has been filed."""
    dashboard_url = f"{config.APP_URL}/dispute/dashboard?case={case_id}"
    subject = "Your dispute has been filed — BillKarma"
    html = f"""
    <div style="font-family:sans-serif;max-width:600px;margin:0 auto;">
        <h2 style="color:#00824F;">Your dispute is on its way.</h2>
        <p>Hi {_he(patient_name)},</p>
        <p>We've filed your formal billing dispute with <strong>{_he(hospital_name or 'the provider')}</strong>.
        Here's what happens next:</p>
        <ul>
            <li>We'll follow up automatically at day 7, 14, 30, and 45 if there's no response.</li>
            <li>If the hospital requires a phone call to resolve your dispute, you'll receive a full refund.</li>
            <li>If we haven't resolved it in 45 days, you'll receive a full refund.</li>
        </ul>
        <p><a href="{dashboard_url}" style="background:#00824F;color:#fff;padding:12px 24px;
        border-radius:999px;text-decoration:none;font-weight:bold;">Track Your Dispute →</a></p>
        <p style="color:#666;font-size:12px;margin-top:32px;">
            Questions? Reply to this email. Not legal advice.
        </p>
    </div>"""
    return send_email(to=to, subject=subject, html_body=html)


def send_followup_to_hospital(
    to: str,
    subject: str,
    patient_name: str,
    account_number: str,
    hospital_name: str,
    followup_number: int,
    case_id: int,
) -> bool:
    """Send a follow-up message to the hospital billing department."""
    body = (
        f"This is follow-up #{followup_number} regarding the formal billing dispute "
        f"submitted on behalf of patient {patient_name} (Account: {account_number}).\n\n"  # plain-text, not rendered as HTML
        f"We have not received a written response to our dispute letter sent on behalf of "
        f"our client. We respectfully request a written acknowledgment and resolution "
        f"within 7 business days.\n\n"
        f"Under CMS billing guidelines and applicable state law, patients have the right "
        f"to receive a written response to billing disputes. If we do not receive a response, "
        f"we will proceed with filing a complaint with the appropriate regulatory authorities.\n\n"
        f"Please respond in writing to disputes@billkarma.app, referencing case #{case_id}.\n\n"
        f"BillKarma Patient Advocacy\ndisputes@billkarma.app"
    )
    html = f"<pre style='font-family:monospace;white-space:pre-wrap;'>{_he(body)}</pre>"
    return send_email(to=to, subject=subject, html_body=html, text_body=body)


def send_refund_confirmation(
    to: str,
    patient_name: str,
    case_id: int,
    amount_cents: int,
) -> bool:
    """Confirm to the patient that a refund has been issued."""
    amount = f"${amount_cents / 100:.2f}"
    subject = f"Your refund of {amount} has been issued — BillKarma"
    html = f"""
    <div style="font-family:sans-serif;max-width:600px;margin:0 auto;">
        <h2 style="color:#00824F;">Your refund is on its way.</h2>
        <p>Hi {_he(patient_name)},</p>
        <p>We weren't able to resolve your dispute via written channels within our 45-day window,
        so we've issued a full refund of <strong>{_he(amount)}</strong> to your original payment method.</p>
        <p>Refunds typically appear within 5–10 business days.</p>
        <p>We're sorry we couldn't get this resolved for you. If you'd like to escalate further,
        consider filing a complaint with your state Attorney General or the CMS.</p>
        <p style="color:#666;font-size:12px;margin-top:32px;">Case #{case_id}</p>
    </div>"""
    return send_email(to=to, subject=subject, html_body=html)
