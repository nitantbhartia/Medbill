"""Dispute workflow — structured letter generation, phone script, and aggregate stats."""

from __future__ import annotations

import json
from datetime import date, datetime

from analyzer import get_bill_results
from charge_summary import group_findings_by_charge
import report_recheck
from rule_sources import basis_for, reply_for
from db import get_db



def _readable_date(value) -> str | None:
    """'2026-09-14' becomes 'September 14, 2026'. Anything else is returned as it came."""
    if not value:
        return None
    text = str(value)
    try:
        parsed = datetime.strptime(text[:10], "%Y-%m-%d")
    except ValueError:
        return text
    return f"{parsed.strftime('%B')} {parsed.day}, {parsed.year}"


def _proper(description: str) -> str:
    """Title-case a description word by word, leaving words that are already in capitals (CBC stays CBC, not Cbc)."""
    return " ".join(word if word.isupper() else word.title() for word in description.split(" "))


def build_dispute_letter(
    bill_id: int,
    finding_ids: list[int] | None = None,
    requestor_name: str = "[Your Name]",
    account_number: str = "[Account Number]",
) -> dict | None:
    """Build a formal dispute letter with finding-type-specific paragraphs.

    Returns a dict with keys: letter, provider, service_date, total_disputed, finding_count.
    Returns None if the bill does not exist or has no findings.
    """
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            return None
        if finding_ids:
            placeholders = ",".join(["?"] * len(finding_ids))
            rows = db.execute(
                f"SELECT * FROM findings WHERE bill_id = ? AND id IN ({placeholders}) ORDER BY id",
                [bill_id, *finding_ids],
            ).fetchall()
        else:
            rows = db.execute(
                "SELECT * FROM findings WHERE bill_id = ? ORDER BY id", (bill_id,)
            ).fetchall()

    rows = [row for row in rows if row["finding_type"] != "price_info"]
    if not rows:
        return None

    bill = dict(bill)
    provider = bill.get("provider_name") or "[Hospital/Provider Name]"
    service_date = _readable_date(bill.get("bill_date")) or "[Date of Service]"
    today = date.today().strftime("%B %d, %Y")

    rows = [row for row in rows if row["finding_type"] != "price_info"]  # information, never in a letter
    if not rows:
        return None
    paragraphs = []
    for row in rows:
        detail = json.loads(row["details"] or "{}")
        li = detail.get("line_item") or {}
        cpt = li.get("cpt_code") or "N/A"
        desc = li.get("description") or "this service"
        billed = float(li.get("charged_amount") or 0.0)
        medicare = float(detail.get("medicare_rate") or 0.0)
        finding_type = row["finding_type"] or "pricing"
        worth_asking = row["severity"] in ("low", "informational") or finding_type in ("quantity_question", "upcoding")
        if worth_asking and finding_type not in ("eob_mismatch", "upcoding"):
            paragraphs.append(_request_paragraph(finding_type, cpt, desc, billed, service_date))
        else:
            paragraphs.append(_finding_paragraph(finding_type, cpt, desc, billed, medicare, service_date, detail, bill))

    body = "\n\n".join(f"  {i+1}. {p}" for i, p in enumerate(paragraphs))
    sources = _source_footnotes(rows)

    letter = (
        f"{today}\n\n"
        f"{requestor_name}\n"
        f"[Your Address]\n"
        f"[Your Email / Phone]\n\n"
        f"Billing Department\n"
        f"{provider}\n"
        f"[Hospital Address]\n\n"
        f"Re: Formal Billing Dispute — Account: {account_number}\n"
        f"    Date of Service: {service_date}\n\n"
        f"Dear {provider} Billing Department,\n\n"
        f"I am writing to formally dispute the following charges on my account "
        f"({account_number}) for services received on {service_date}. "
        f"I have reviewed my itemized bill and compared each charge against the 2026 "
        f"Medicare Outpatient Prospective Payment System (OPPS) rates, which are the "
        f"nationally recognized benchmark for medically necessary services. "
        f"I am requesting a formal billing review and written response within 30 days.\n\n"
        f"DISPUTED CHARGES\n"
        f"{'─' * 60}\n\n"
        f"{body}\n\n"
        f"{'─' * 60}\n\n"
        f"REQUESTED ACTION\n\n"
        f"Please provide:\n"
        f"  1. Written acknowledgment that this dispute has been received and is under review.\n"
        f"  2. An itemized explanation of each disputed charge.\n"
        f"  3. A corrected statement if any charges are found to be in error, and an itemized bill with the documentation behind each charge.\n"
        f"  4. Confirmation that collection activity on the disputed amounts is on hold "
        f"pending resolution.\n\n"
        f"Please respond in writing to [Your Email / Mailing Address]. "
        f"If I do not receive a written response within 30 days, I reserve the right to "
        f"file a complaint with my state Attorney General's office and the Centers for "
        f"Medicare & Medicaid Services (CMS).\n\n"
        f"Thank you for your prompt attention to this matter.\n\n"
        f"Sincerely,\n\n"
        f"{requestor_name}\n"
        f"[Your Signature]\n\n"
        f"{sources}"
        f"Enclosures: Itemized bill, EOB (if applicable)"
    )

    return {
        "letter": letter,
        "provider": provider,
        "service_date": service_date,
        "account_number": account_number,
        **_disputed_totals(bill_id, [row["id"] for row in rows]),
    }


def _source_footnotes(rows) -> str:
    """The public sources behind the disputed charges, so the billing office can check them."""
    lines = []
    for row in rows:
        basis = basis_for(row["rule_id"], json.loads(row["details"] or "{}"))
        if not basis or basis["kind"] != "official":
            continue
        year = f", {basis['source_year']}" if basis.get("source_year") else ""
        line = f"  - {basis['source_name']}{year}: {basis['source_url']}"
        if line not in lines:
            lines.append(line)
    return "SOURCES\n" + "\n".join(lines) + "\n\n" if lines else ""


def _disputed_totals(bill_id: int, finding_ids: list[int]) -> dict:
    """Count and total the disputed charges the way the report does: each charge once, not each finding."""
    results = get_bill_results(bill_id)
    bill = results["bill"]
    owed = float(bill.get("total_patient_owes") or bill.get("total_charged") or 0) or None
    chosen = [f for f in results["findings"] if f["id"] in finding_ids]
    summary = group_findings_by_charge(chosen, owed)
    return {"total_disputed": summary["total_savings"], "finding_count": len(summary["charges"])}


def _finding_paragraph(
    finding_type: str,
    cpt: str,
    desc: str,
    billed: float,
    medicare: float,
    service_date: str,
    detail: dict,
    bill: dict | None = None,
) -> str:
    """Return a dispute paragraph tailored to the finding type."""
    billed_fmt = f"${billed:,.2f}" if billed else "[charge]"
    medicare_fmt = f"${medicare:,.2f}" if medicare else None
    markup = round(billed / medicare, 1) if medicare and billed else None

    if finding_type == "eob_mismatch":
        return _eob_paragraph(cpt, desc, billed_fmt, service_date, bill or {})

    if finding_type in ("duplicate", "duplicate_charge"):
        count = len(detail["duplicate_of"]) + 1 if detail.get("duplicate_of") else int(detail.get("duplicate_count") or 2)
        return (
            f"DUPLICATE BILLING — CPT {cpt} ({_proper(desc)})\n"
            f"     Date of Service: {service_date} | Charge: {billed_fmt}\n\n"
            f"     I was charged {count} times for {desc.lower()} (CPT {cpt}) on {service_date}. Please send the "
            f"documentation that supports more than one billing on that date. Please remove the duplicate if there "
            f"is none, keeping only the charges your records support."
        )

    if finding_type in ("unbundling", "ncci"):
        bundled = detail.get("bundled_code") or ""
        bundled_note = f" when CPT {bundled} applies" if bundled else ""
        return (
            f"POSSIBLE UNBUNDLING — CPT {cpt} ({_proper(desc)})\n"
            f"     Date of Service: {service_date} | Charge: {billed_fmt}\n\n"
            f"     CMS National Correct Coding Initiative (NCCI) edits indicate that CPT {cpt} "
            f"is not normally billed separately{bundled_note}. These codes are bundled under Medicare "
            f"billing rules and usually do not appear as separate line items. I am requesting "
            f"correction or removal of this charge in accordance with NCCI guidelines."
        )

    if finding_type == "upcoding":
        level = detail.get("billed_level") or {"99284": 4, "99285": 5}.get(cpt, "")
        return (
            f"ER VISIT LEVEL — CPT {cpt} ({_proper(desc)})\n"
            f"     Date of Service: {service_date} | Charge: {billed_fmt}\n\n"
            f"     Please send the documentation that supports a level {level} visit. I am asking for the "
            f"records that show why this level was assigned."
        )

    # Default: pricing markup
    medicare_line = (
        f"The current Medicare rate for this procedure is {medicare_fmt}"
        f"{f', representing a {markup}x markup' if markup else ''}. "
        if medicare_fmt
        else ""
    )
    return (
        f"CHARGE ABOVE MEDICARE BENCHMARK — CPT {cpt} ({_proper(desc)})\n"
        f"     Date of Service: {service_date} | Charge: {billed_fmt}\n\n"
        f"     {medicare_line}"
        f"I am requesting a review and adjustment of this charge to a rate consistent "
        f"with recognized Medicare reimbursement benchmarks."
    )


def _request_paragraph(finding_type: str, cpt: str, desc: str, billed: float, service_date: str) -> str:
    """A finding that is worth asking about is phrased as a request for an explanation, never as an accusation."""
    billed_fmt = f"${billed:,.2f}" if billed else "[charge]"
    head = f"REQUEST FOR EXPLANATION \u2014 CPT {cpt} ({_proper(desc)})\n     Date of Service: {service_date} | Charge: {billed_fmt}\n\n     "
    if finding_type in ("duplicate", "duplicate_charge"):
        return head + ("This service appears more than once on the same day. Please explain, or provide documentation that it was "
                       "repeated (a repeat test is normally shown with modifier 91). If it was billed in error, please remove the extra charge.")
    return head + "Please explain, or provide documentation for, this charge, and confirm that the code and quantity are correct."


def _eob_paragraph(cpt: str, desc: str, billed_fmt: str, service_date: str, bill: dict) -> str:
    owed, billed_owes = bill.get("eob_patient_owes"), bill.get("total_patient_owes")
    head = f"BALANCE DOES NOT MATCH MY INSURANCE STATEMENT \u2014 CPT {cpt} ({_proper(desc)})\n     Date of Service: {service_date} | Charge: {billed_fmt}\n\n     "
    if owed is None or billed_owes is None:
        return head + ("My Explanation of Benefits (EOB) does not agree with the amount on this bill. I am requesting "
                       "that the balance be corrected to match my insurer's determination.")
    dated = f" dated {bill['eob_date']}" if bill.get("eob_date") else ""
    return head + (f"My insurer's Explanation of Benefits (EOB){dated} shows that I owe ${owed:,.2f}. This bill asks me to "
                   f"pay ${billed_owes:,.2f}. I am requesting that the balance be corrected to match my insurer's "
                   f"determination, and that the difference of ${billed_owes - owed:,.2f} be removed from my account.")


def build_appeal_letter(
    bill_id: int,
    requestor_name: str = "[Your Name]",
    policy_number: str = "[Policy Number]",
) -> dict | None:
    """Build an insurance appeal letter for denied claims based on findings.

    Returns a dict with keys: letter, provider, finding_count.
    Returns None if the bill has no findings.
    """
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            return None
        rows = db.execute(
            "SELECT * FROM findings WHERE bill_id = ? ORDER BY id", (bill_id,)
        ).fetchall()

    if not rows:
        return None

    bill = dict(bill)
    provider = bill.get("provider_name") or "[Hospital/Provider Name]"
    service_date = _readable_date(bill.get("bill_date")) or "[Date of Service]"
    today = date.today().strftime("%B %d, %Y")

    issues = []
    total_disputed = 0.0
    for row in rows:
        detail = json.loads(row["details"] or "{}")
        li = detail.get("line_item") or {}
        cpt = li.get("cpt_code") or "N/A"
        desc = li.get("description") or "this service"
        billed = float(li.get("charged_amount") or 0.0)
        savings = float(row["potential_savings"] or 0.0)
        total_disputed += savings
        issues.append(f"CPT {cpt} ({_proper(desc)}) — billed ${billed:,.2f}, potential overcharge ${savings:,.2f}")

    issues_text = "\n".join(f"  {i+1}. {issue}" for i, issue in enumerate(issues))

    letter = (
        f"{today}\n\n"
        f"{requestor_name}\n"
        f"[Your Address]\n"
        f"[Your Phone / Email]\n\n"
        f"Insurance Appeals Department\n"
        f"[Insurance Company Name]\n"
        f"[Insurance Company Address]\n\n"
        f"Re: Appeal of Claim Denial\n"
        f"    Policy Number: {policy_number}\n"
        f"    Provider: {provider}\n"
        f"    Date of Service: {service_date}\n\n"
        f"Dear Appeals Department,\n\n"
        f"I am writing to formally appeal the denial of my claim for services received "
        f"at {provider} on {service_date}. After reviewing my Explanation of Benefits and "
        f"the itemized bill, I believe the following charges were improperly processed or denied:\n\n"
        f"{issues_text}\n\n"
        f"I am requesting that you:\n"
        f"  1. Re-review this claim with the supporting documentation enclosed.\n"
        f"  2. Provide a detailed written explanation if the denial is upheld.\n"
        f"  3. Process any eligible charges for reimbursement.\n\n"
        f"Under my policy and applicable state insurance regulations, I have the right to "
        f"appeal claim denials. If this internal appeal is denied, I reserve the right to "
        f"request an external review by an independent reviewer.\n\n"
        f"Enclosed: Itemized bill, Explanation of Benefits, and supporting documentation.\n\n"
        f"Please respond within 30 days as required.\n\n"
        f"Sincerely,\n\n"
        f"{requestor_name}\n"
    )

    return {
        "letter": letter,
        "provider": provider,
        "service_date": service_date,
        "total_disputed": round(total_disputed, 2),
        "finding_count": len(rows),
    }


def build_phone_script(bill_id: int) -> str | None:
    """Build a structured phone script for disputing flagged items."""
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            return None
        rows = db.execute(
            "SELECT * FROM findings WHERE bill_id = ? ORDER BY id", (bill_id,)
        ).fetchall()

    if not rows:
        return None

    bill = dict(bill)
    provider = bill.get("provider_name") or "the provider"
    service_date = _readable_date(bill.get("bill_date")) or "your date of service"

    finding_scripts = []
    for row in rows:
        detail = json.loads(row["details"] or "{}")
        li = detail.get("line_item") or {}
        cpt = li.get("cpt_code") or "N/A"
        desc = li.get("description") or "this service"
        billed = float(li.get("charged_amount") or 0.0)
        medicare = float(detail.get("medicare_rate") or 0.0)
        finding_type = row["finding_type"] or "pricing"
        if finding_type == "price_info":
            continue
        block = _phone_finding_block(finding_type, cpt, desc, billed, medicare, service_date)
        reply = reply_for(detail.get("innocent_reason"))
        if reply:
            block += f'\n\nThey may say: {reply["may_say"]}\nWhat to say back: "{reply["say_back"]}"'
        finding_scripts.append(block)

    findings_text = "\n\n".join(finding_scripts)

    withdrawn = report_recheck.withdrawn_items_for_sent_letter(bill_id)
    withdrawn_line = (f"WITHDRAW THESE ITEMS\n{'─' * 50}\nWe no longer think this charge was an error, and your letter named it: "
                      f"{', '.join(withdrawn)}. Tell them you withdraw that item.\n\n") if withdrawn else ""

    return (
        withdrawn_line +
        f"BEFORE YOU CALL\n"
        f"{'─' * 50}\n"
        f"Have ready: your account number, the date of service ({service_date}), and this script.\n"
        f"Ask to speak with: a billing specialist, not general customer service.\n\n"
        f"OPENING\n"
        f"{'─' * 50}\n"
        f'"Hi, my name is [your name] and I\'m calling about a bill from {provider} '
        f'for services on {service_date}. My account number is [your account number]. '
        f"I've reviewed my itemized bill and I'd like to request a formal billing review "
        f'for some specific charges."\n\n'
        f"FOR EACH DISPUTED CHARGE\n"
        f"{'─' * 50}\n"
        f"{findings_text}\n\n"
        f"IF THEY RESIST OR SAY THEY CAN'T HELP\n"
        f"{'─' * 50}\n"
        f'"I understand. Can I request a formal internal billing review in writing? '
        f"I'd like a written response, please. Can you give me the address or email to "
        f'send a formal dispute letter?"\n\n'
        f"IF THEY SAY THEY'LL CALL BACK\n"
        f"{'─' * 50}\n"
        f'"Can I get your name and direct number? And what\'s a reasonable timeframe — '
        f'should I follow up in 5 business days if I haven\'t heard back?"\n\n'
        f"TAKE NOTES\n"
        f"{'─' * 50}\n"
        f"Write down: representative's name, date and time of call, what was agreed to, "
        f"any reference number given."
    )


def _phone_finding_block(
    finding_type: str, cpt: str, desc: str, billed: float, medicare: float, service_date: str
) -> str:
    billed_fmt = f"${billed:,.2f}" if billed else "[charge amount]"
    medicare_fmt = f"${medicare:,.2f}" if medicare else None

    opening = (
        f'"On {service_date}, I was billed {billed_fmt} for CPT code {cpt} '
        f"({_proper(desc)}). "
    )

    if finding_type == "duplicate":
        detail = (
            f"This code appears more than once on the same date — I'd like to understand "
            f"the clinical justification for billing it multiple times. Can you review that?"
        )
    elif finding_type in ("unbundling", "ncci"):
        detail = (
            f"CMS coding guidelines indicate this code shouldn't be billed separately under "
            f"NCCI rules. Can you have your coding team check this?"
        )
    elif finding_type == "upcoding":
        detail = (
            f"Can you pull the clinical notes from that visit? I'd like to understand "
            f"what documentation supports the complexity level assigned to this code."
        )
    else:
        medicare_note = f"The Medicare rate for this procedure is {medicare_fmt}. " if medicare_fmt else ""
        detail = (
            medicare_note
            + "I'd like to request a review of this charge "
            + "and see if a more standard rate is available."
        )

    return opening + detail + '"'


def get_outcome_stats() -> dict:
    """Return aggregate dispute outcome stats. median_recovered is None if fewer than 50 outcomes."""
    with get_db() as db:
        total_row = db.execute("SELECT COUNT(*) AS n FROM dispute_outcomes").fetchone()
        savings_rows = db.execute(
            "SELECT actual_savings FROM dispute_outcomes "
            "WHERE outcome IN ('reduced', 'forgiven') AND actual_savings > 0 "
            "ORDER BY actual_savings"
        ).fetchall()

    total_count = total_row["n"] if total_row else 0
    savings = [r["actual_savings"] for r in savings_rows]
    recovery_count = len(savings)

    if recovery_count == 0:
        return {
            "total_disputes": total_count,
            "recovery_count": 0,
            "median_recovered": None,
            "avg_recovered": None,
            "show_stat": False,
        }

    mid = recovery_count // 2
    median = savings[mid] if recovery_count % 2 else (savings[mid - 1] + savings[mid]) / 2
    avg = sum(savings) / recovery_count

    return {
        "total_disputes": total_count,
        "recovery_count": recovery_count,
        "median_recovered": round(median, 2),
        "avg_recovered": round(avg, 2),
        "show_stat": total_count >= 50,
    }


def split_script_sections(script: str) -> list[dict]:
    """Split the phone script into [{"title", "body"}] at its UPPERCASE headings (each followed by a rule line)."""
    lines = script.split("\n")
    heading_at = [
        i for i in range(len(lines) - 1)
        if lines[i].strip() and lines[i] == lines[i].upper() and lines[i + 1].startswith("─")
    ]
    sections = []
    for position, start in enumerate(heading_at):
        end = heading_at[position + 1] if position + 1 < len(heading_at) else len(lines)
        body = "\n".join(lines[start + 2:end]).strip()
        sections.append({"title": lines[start].strip(), "body": body})
    return sections
