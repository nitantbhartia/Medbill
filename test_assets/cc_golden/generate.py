#!/usr/bin/env python3
"""Draw the 5 synthetic denial letters and write expected.jsonl. Deterministic: fixed dates, no randomness.

Run from the repo root:  .venv312/bin/python test_assets/cc_golden/generate.py
All names, numbers and addresses are invented.
"""

from __future__ import annotations

import json
import textwrap
from datetime import date, timedelta
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path(__file__).resolve().parent
PAGE = (1700, 2200)  # US Letter at 200 dpi
MARGIN = 150
BODY_SIZE = 31
LINE_GAP = 14
PARAGRAPH_GAP = 30
WRAP_CHARS = 68
FONT_PATHS = (
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
)


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    for path in FONT_PATHS[1::2] if bold else FONT_PATHS[0::2]:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def long_date(value: date) -> str:
    return f"{value.strftime('%B')} {value.day}, {value.year}"


# Each case: the letter content, plus the answers the reader should reach.
# window_days is set when the letter prints a window instead of a date.
CASES = [
    {
        "file": "employer_medical_necessity.png", "plan_type": "employer", "reason_key": "medical_necessity",
        "insurer": "Blue Harbor Health", "tagline": "Employer Group Health Plan",
        "title": "Adverse Benefit Determination",
        "notice": date(2026, 2, 12), "claim_number": "BH26-0412876", "printed_date": date(2026, 8, 11),
        "member": ["Member: Jordan A. Example", "Member ID: BHX 884 2201 07", "Group: Lakeside Manufacturing (G-55120)"],
        "claim_lines": ["Claim number: BH26-0412876", "Service: MRI lumbar spine without contrast (CPT 72148)",
                        "Provider: Lakeshore Imaging Center", "Date of service: January 29, 2026"],
        "body": [
            "Dear Member,",
            "We reviewed the claim above under your employer's group health plan, which is governed by the Employee "
            "Retirement Income Security Act of 1974 (ERISA). We have denied coverage for this service.",
            "Reason for denial: The requested MRI of the lumbar spine is not medically necessary. The records we "
            "received do not show at least six weeks of conservative treatment before imaging, as required by "
            "Clinical Policy 114, Imaging for Low Back Pain.",
            "You have the right to appeal this decision. To appeal, send a written request with any supporting "
            "records. You must file your appeal by August 11, 2026. Appeals received after that date will not be "
            "reviewed. You may ask for copies of the documents we used, free of charge.",
        ],
        "address": ["Blue Harbor Health, Appeals Department", "PO Box 48210, Dayton, OH 45401"],
        "fax": "Fax: 1-937-555-0142", "phone": "Member Services: 1-800-555-0177",
    },
    {
        "file": "aca_out_of_network.png", "plan_type": "individual", "reason_key": "out_of_network",
        "insurer": "Keystone Community Health Plan", "tagline": "Individual and Family Plans, Health Insurance Marketplace",
        "title": "Notice of Claim Denial",
        "notice": date(2026, 3, 9), "claim_number": "KCH-7731904-02", "window_days": 180,
        "member": ["Member: Riley T. Sample", "Member ID: KCH 77 31904", "Plan: Silver 4500 (Marketplace)"],
        "claim_lines": ["Claim number: KCH-7731904-02", "Service: Emergency department visit, level 4",
                        "Provider: Riverbend General Hospital (out of network)", "Date of service: February 17, 2026"],
        "body": [
            "Dear Member,",
            "We processed the claim above under your Marketplace plan and have denied payment.",
            "Reason for denial: The facility that treated you is out-of-network, and we did not approve care "
            "from a non-participating provider.",
            "If you disagree with this decision, you may file an internal appeal. Your appeal must be submitted "
            "within 180 days of the date of this notice. Include your member ID, the claim number and any "
            "records that support your request. After the appeal you may be able to ask for an external review.",
        ],
        "address": ["Keystone Community Health Plan, Member Appeals", "200 Market Street, Suite 900, Harrisburg, PA 17101"],
        "fax": "Fax: 1-717-555-0188", "phone": "Member Services: 1-866-555-0119",
    },
    {
        "file": "medicare_advantage_reconsideration.png", "plan_type": "medicare_advantage",
        "reason_key": "medical_necessity",
        "insurer": "Sunrise Medicare Advantage", "tagline": "A Medicare Advantage HMO plan",
        "title": "Notice of Denial of Medical Coverage",
        "notice": date(2026, 5, 4), "claim_number": "SMA2026-559318", "window_days": 65,
        "member": ["Member: Morgan L. Demo", "Member ID: 4XY7 TE5 MK19", "Plan: Sunrise Gold Plus (HMO)"],
        "claim_lines": ["Reference number: SMA2026-559318", "Service: Left total knee replacement",
                        "Provider: Pinecrest Orthopedics", "Requested date: April 20, 2026"],
        "body": [
            "Dear Morgan Demo,",
            "We have made an organization determination about the service listed above. We are denying coverage.",
            "Reason for denial: Based on the information we have, the surgery is not medically necessary at "
            "this time. Medicare coverage criteria for joint replacement are not met.",
            "You have the right to ask us for a reconsideration. You must ask within 65 days of the date of "
            "this notice. If we uphold our decision, we will send your case to the Independent Review Entity "
            "(IRE), an independent organization that works for Medicare. You do not need to file anything for "
            "that step.",
        ],
        "address": ["Sunrise Medicare Advantage, Appeals and Grievances", "7 Harbor Way, Tampa, FL 33602"],
        "fax": "Fax: 1-813-555-0136", "phone": "TTY 711. Member Services: 1-877-555-0150",
    },
    {
        "file": "medicaid_plan_appeal.png", "plan_type": "medicaid", "reason_key": "not_covered",
        "insurer": "Evergreen Medicaid Care", "tagline": "Medicaid Managed Care Organization",
        "title": "Notice of Adverse Benefit Determination",
        "notice": date(2026, 4, 14), "claim_number": "EMC-90455512", "printed_date": date(2026, 6, 13),
        "member": ["Member: Casey R. Placeholder", "Member ID: 100 482 9917", "Program: Medicaid Managed Care"],
        "claim_lines": ["Claim number: EMC-90455512", "Service: Outpatient physical therapy, 12 additional visits",
                        "Provider: Valley Rehab Associates", "Date of request: April 1, 2026"],
        "body": [
            "Dear Member,",
            "We have decided to deny the service listed above. This is called an adverse benefit determination.",
            "Reason for denial: The service is not a covered benefit because you have used all 20 physical "
            "therapy visits allowed in a calendar year under your plan.",
            "You may appeal this decision with the plan. Your appeal must be filed by June 13, 2026. You may "
            "also ask for a State fair hearing after you receive our appeal decision. Benefits may continue "
            "during an appeal only if you ask in time. Free help is available from your caseworker.",
        ],
        "address": ["Evergreen Medicaid Care, Appeals Unit", "1450 Capitol Avenue, Olympia, WA 98501"],
        "fax": "Fax: 1-360-555-0123", "phone": "Member Services: 1-855-555-0166",
    },
    {
        "file": "employer_prior_auth.png", "plan_type": "employer", "reason_key": "prior_authorization",
        "insurer": "Blue Harbor Health", "tagline": "Employer Group Health Plan",
        "title": "Prior Authorization Determination",
        "notice": date(2026, 6, 22), "claim_number": "PA-26-0093147",
        "member": ["Member: Avery K. Fictional", "Member ID: BHX 301 7745 12", "Group: Northwind Logistics (G-60288)"],
        "claim_lines": ["Reference number: PA-26-0093147", "Requested service: Outpatient sleep study (CPT 95810)",
                        "Requesting provider: Dr. P. Ortega, Sleep Medicine", "Request received: June 15, 2026"],
        "body": [
            "Dear Member,",
            "We reviewed your provider's prior authorization request for the service above under your "
            "employer's group health plan. We cannot approve it.",
            "Reason for denial: Prior authorization is denied. The information we received does not show that "
            "an in-lab sleep study is needed instead of a home sleep test.",
            "Because this service has not been performed yet, no claim has been paid or denied. You or your "
            "provider can ask us to review this decision again and send more information. Please call "
            "Member Services or write to us at the address below and tell us what you would like us to look at.",
        ],
        "address": ["Blue Harbor Health, Utilization Management Appeals", "PO Box 48210, Dayton, OH 45401"],
        "fax": "Fax: 1-937-555-0142", "phone": "Member Services: 1-800-555-0177",
    },
]


def expected_line(case: dict) -> dict:
    deadline = case.get("printed_date")
    if case.get("window_days"):
        deadline = case["notice"] + timedelta(days=case["window_days"])
    return {
        "file": case["file"], "claim_number": case["claim_number"], "notice_date": case["notice"].isoformat(),
        "printed_deadline": deadline.isoformat() if deadline else None,
        "plan_type": case["plan_type"], "reason_key": case["reason_key"],
    }


def draw_letter(case: dict) -> Image.Image:
    image = Image.new("RGB", PAGE, "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, PAGE[0], 190], fill=(24, 62, 110))
    draw.text((MARGIN, 45), case["insurer"], fill="white", font=font(58, bold=True))
    draw.text((MARGIN, 122), case["tagline"], fill=(210, 225, 245), font=font(28))
    body, bold = font(BODY_SIZE), font(BODY_SIZE, bold=True)
    y = 250
    draw.text((MARGIN, y), long_date(case["notice"]), fill="black", font=body)
    y += 80
    for line in case["member"]:
        draw.text((MARGIN, y), line, fill="black", font=body)
        y += BODY_SIZE + LINE_GAP
    y += 20
    draw.text((MARGIN, y), case["title"].upper(), fill=(24, 62, 110), font=font(38, bold=True))
    y += 80
    for line in case["claim_lines"]:
        draw.text((MARGIN, y), line, fill="black", font=body)
        y += BODY_SIZE + LINE_GAP
    y += 40
    for paragraph in case["body"]:
        for line in textwrap.wrap(paragraph, WRAP_CHARS):
            draw.text((MARGIN, y), line, fill="black", font=body)
            y += BODY_SIZE + LINE_GAP
        y += PARAGRAPH_GAP
    draw.text((MARGIN, y), "Where to send your appeal", fill="black", font=bold)
    y += BODY_SIZE + LINE_GAP + 6
    for line in case["address"] + [case["fax"], case["phone"]]:
        draw.text((MARGIN, y), line, fill="black", font=body)
        y += BODY_SIZE + LINE_GAP
    y += PARAGRAPH_GAP
    draw.text((MARGIN, y), "Sincerely,", fill="black", font=body)
    draw.text((MARGIN, y + 60), f"{case['insurer']} Appeals Team", fill="black", font=body)
    assert y + 140 < PAGE[1] - 80, f"{case['file']}: text runs off the page"
    return image


def main() -> None:
    for case in CASES:
        draw_letter(case).save(OUT_DIR / case["file"])
    lines = [json.dumps(expected_line(case)) for case in CASES]
    (OUT_DIR / "expected.jsonl").write_text("\n".join(lines) + "\n")
    print(f"wrote {len(CASES)} letters and expected.jsonl to {OUT_DIR}")


if __name__ == "__main__":
    main()
