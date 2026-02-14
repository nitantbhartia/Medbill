"""
Seed the SQLite database with common Medicare rates and NCCI edit pairs
for testing and initial functionality.
"""

import logging

from db import get_db

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Medicare physician fee schedule rates (national, 2026)
#
# Rates below reflect realistic 2026 CMS national Medicare Physician Fee
# Schedule (MPFS) allowable amounts.  "facility_rate" is the payment when
# the service is rendered inside a facility (hospital, ASC).
# "non_facility_rate" is the payment in a physician office setting.
# Locality "0000000" is the national (non-locality-adjusted) baseline.
# ---------------------------------------------------------------------------

MEDICARE_RATES = [
    # CPT      description                                     locality    state  non_fac   facility  year
    # --- Emergency department visits (99281-99285) ---
    ("99281",  "ED visit, level 1 (self-limited/minor)",       "0000000",  None,   27.00,    27.00,   2026),
    ("99282",  "ED visit, level 2 (low severity)",             "0000000",  None,   52.00,    52.00,   2026),
    ("99283",  "ED visit, level 3 (moderate severity)",        "0000000",  None,   98.00,    98.00,   2026),
    ("99284",  "ED visit, level 4 (high severity)",            "0000000",  None,  157.00,   157.00,   2026),
    ("99285",  "ED visit, level 5 (critical severity)",        "0000000",  None,  227.00,   227.00,   2026),

    # --- Office/outpatient visits (99213-99215) ---
    ("99213",  "Office visit, level 3 (low complexity)",       "0000000",  None,  110.00,    76.00,   2026),
    ("99214",  "Office visit, level 4 (moderate complexity)",  "0000000",  None,  161.00,   111.00,   2026),
    ("99215",  "Office visit, level 5 (high complexity)",      "0000000",  None,  218.00,   151.00,   2026),

    # --- Radiology ---
    ("71046",  "Chest X-ray, 2 views",                         "0000000",  None,   31.00,    13.00,   2026),
    ("71045",  "Chest X-ray, 1 view",                          "0000000",  None,   26.00,    10.00,   2026),
    ("72148",  "MRI lumbar spine without contrast",            "0000000",  None,  381.00,    97.00,   2026),
    ("70553",  "MRI brain with and without contrast",          "0000000",  None,  474.00,   123.00,   2026),
    ("74177",  "CT abdomen and pelvis with contrast",          "0000000",  None,  310.00,    88.00,   2026),

    # --- Cardiology / ECG ---
    ("93000",  "ECG, 12-lead, with interpretation and report", "0000000",  None,   28.00,    11.00,   2026),
    ("93005",  "ECG, tracing only",                            "0000000",  None,   14.00,     6.00,   2026),
    ("93010",  "ECG, interpretation and report only",          "0000000",  None,   14.00,    10.00,   2026),

    # --- Laboratory ---
    ("85025",  "CBC with automated differential",              "0000000",  None,   10.59,    10.59,   2026),
    ("85027",  "CBC without differential (automated)",         "0000000",  None,    8.02,     8.02,   2026),
    ("80053",  "Comprehensive metabolic panel (CMP)",          "0000000",  None,   14.49,    14.49,   2026),
    ("80048",  "Basic metabolic panel (BMP)",                  "0000000",  None,   11.21,    11.21,   2026),

    # --- Phlebotomy ---
    ("36415",  "Venipuncture (blood draw)",                    "0000000",  None,    3.00,     3.00,   2026),
    ("36416",  "Capillary blood draw (finger/heel stick)",     "0000000",  None,    3.00,     3.00,   2026),

    # --- Surgical ---
    ("27447",  "Total knee arthroplasty (replacement)",        "0000000",  None, 1576.00,  1576.00,   2026),
    ("27486",  "Revision of total knee replacement",           "0000000",  None, 2039.00,  2039.00,   2026),

    # --- Endoscopy ---
    ("43239",  "Upper GI endoscopy (EGD) with biopsy",        "0000000",  None,  340.00,   147.00,   2026),
    ("45380",  "Colonoscopy with biopsy",                      "0000000",  None,  455.00,   198.00,   2026),

    # --- Drugs / Injections ---
    ("J0170",  "Adrenalin (epinephrine) injection, up to 1 mL", "0000000", None,   None,     None,   2026),
]

# ---------------------------------------------------------------------------
# NCCI (National Correct Coding Initiative) edit pairs
#
# column_1_code is the comprehensive/primary code.
# column_2_code is the component code that should NOT be billed separately
# when column_1_code is also billed (unless a valid modifier applies).
# modifier_indicator "1" means a modifier is allowed to bypass the edit;
# "0" means never allowed.
# ---------------------------------------------------------------------------

NCCI_EDITS = [
    # col1     col2     effective    deletion  mod_ind
    ("80053",  "80048", "2010-01-01", None,    "0"),   # CMP includes BMP
    ("85025",  "85027", "2010-01-01", None,    "0"),   # CBC w/diff includes CBC w/o diff
    ("93000",  "93005", "2010-01-01", None,    "0"),   # Full ECG includes tracing only
    ("93000",  "93010", "2010-01-01", None,    "0"),   # Full ECG includes interp only
    ("36415",  "36416", "2010-01-01", None,    "0"),   # Venipuncture includes capillary draw
]


def seed_if_empty() -> None:
    """Check if the medicare_rates table is empty; if so, seed it with
    national baseline data and NCCI edit pairs."""

    with get_db() as db:
        # ---- Medicare rates ------------------------------------------------
        row = db.execute("SELECT COUNT(*) AS cnt FROM medicare_rates").fetchone()
        if row["cnt"] == 0:
            logger.info("medicare_rates table is empty -- seeding %d rates", len(MEDICARE_RATES))
            db.executemany(
                """
                INSERT INTO medicare_rates
                    (cpt_code, description, locality, state,
                     non_facility_rate, facility_rate, effective_year)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                MEDICARE_RATES,
            )
            logger.info("Medicare rate seed complete.")
        else:
            logger.debug("medicare_rates already contains %d rows -- skipping seed.", row["cnt"])

        # ---- NCCI edits ----------------------------------------------------
        row = db.execute("SELECT COUNT(*) AS cnt FROM ncci_edits").fetchone()
        if row["cnt"] == 0:
            logger.info("ncci_edits table is empty -- seeding %d edit pairs", len(NCCI_EDITS))
            db.executemany(
                """
                INSERT INTO ncci_edits
                    (column_1_code, column_2_code, effective_date,
                     deletion_date, modifier_indicator)
                VALUES (?, ?, ?, ?, ?)
                """,
                NCCI_EDITS,
            )
            logger.info("NCCI edit seed complete.")
        else:
            logger.debug("ncci_edits already contains %d rows -- skipping seed.", row["cnt"])
