"""File a billing complaint with the state Attorney General by certified mail."""

import logging

import config
from debt_fighter import send_certified_letter

log = logging.getLogger(__name__)

# (office name, "street, city, ST zip"). Only states whose address has been checked are listed.
STATE_ATTORNEY_GENERAL = {
    "CA": ("Office of the Attorney General, Public Inquiry Unit", "P.O. Box 944255, Sacramento, CA 94244-2550"),
    "FL": ("Office of the Attorney General, Consumer Protection Division", "PL-01 The Capitol, Tallahassee, FL 32399-1050"),
    "IL": ("Office of the Attorney General, Consumer Fraud Bureau", "500 South Second Street, Springfield, IL 62701"),
    "MA": ("Office of the Attorney General, Consumer Advocacy and Response Division", "One Ashburton Place, Boston, MA 02108"),
    "MI": ("Office of the Attorney General, Consumer Protection Division", "P.O. Box 30213, Lansing, MI 48909"),
    "NJ": ("Division of Consumer Affairs, Consumer Services", "P.O. Box 45025, Newark, NJ 07101"),
    "NY": ("Office of the Attorney General, Health Care Bureau", "28 Liberty Street, New York, NY 10005"),
    "OH": ("Office of the Attorney General, Consumer Protection Section", "30 E. Broad Street, 14th Floor, Columbus, OH 43215"),
    "PA": ("Office of Attorney General, Bureau of Consumer Protection", "Strawberry Square, 15th Floor, Harrisburg, PA 17120"),
    "TX": ("Office of the Attorney General, Consumer Protection Division", "P.O. Box 12548, Austin, TX 78711-2548"),
    "WA": ("Office of the Attorney General, Consumer Protection Division", "800 Fifth Avenue, Suite 2000, Seattle, WA 98104"),
}


def build_complaint_letter(
    patient_name: str,
    patient_address: str,
    hospital_name: str,
    account_number: str,
    dispute_sent_on: str,
    followups_sent: int,
    dispute_letter: str,
) -> str:
    return f"""{patient_name}
{patient_address}

Re: Complaint about hospital billing practices — {hospital_name}, Account #{account_number or "N/A"}

To the Consumer Protection Division:

I am filing a complaint against {hospital_name} about charges on the account above. On {dispute_sent_on} a written dispute was sent to the hospital's billing office on my behalf by BillKarma, my authorized representative. The hospital has not resolved it despite {followups_sent} written follow-up request{"s" if followups_sent != 1 else ""}.

I ask your office to review the billing errors described in the enclosed dispute letter and to help me obtain a corrected bill.

Sincerely,
{patient_name}

Enclosure: copy of the dispute letter sent to {hospital_name}

----- ENCLOSED DISPUTE LETTER -----

{dispute_letter}"""


def file_attorney_general_complaint(
    state: str,
    patient_name: str,
    patient_address: str,
    letter_text: str,
    case_id: int,
) -> str:
    """Mail the complaint to the hospital's state AG. Returns the tracking number, or '' if not mailed
    (disabled, no Lob key, or no verified address for the state)."""
    if not (config.AUTO_FILE_COMPLAINTS and config.LOB_API_KEY):
        return ""
    office = STATE_ATTORNEY_GENERAL.get(state)
    if not office:
        log.warning("No Attorney General address for state %r; case %d complaint not filed", state, case_id)
        return ""
    try:
        result = send_certified_letter(
            description=f"AG complaint, case {case_id}",
            from_name=patient_name,
            from_address=patient_address,
            to_name=office[0],
            to_address=office[1],
            letter_text=letter_text,
            api_key=config.LOB_API_KEY,
        )
    except RuntimeError as exc:
        log.error("Attorney General complaint for case %d failed: %s", case_id, exc)
        return ""
    return result["tracking_number"]
