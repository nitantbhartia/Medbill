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
# Hospital Outpatient Prospective Payment System (OPPS) rates
#
# These are the facility-side payments Medicare makes for outpatient hospital
# services, separate from physician fees (PFS). When a patient gets an ER
# visit at a hospital, the hospital bills an OPPS rate on top of the
# physician's PFS rate.  APC = Ambulatory Payment Classification.
# ---------------------------------------------------------------------------

OPPS_RATES = [
    # CPT      APC     description                                      payment    year
    ("99281",  "5021", "ED visit, level 1",                               68.00,   2026),
    ("99282",  "5022", "ED visit, level 2",                              155.00,   2026),
    ("99283",  "5023", "ED visit, level 3",                              297.00,   2026),
    ("99284",  "5024", "ED visit, level 4",                              504.00,   2026),
    ("99285",  "5025", "ED visit, level 5",                              773.00,   2026),
    ("71046",  "5522", "Chest X-ray, 2 views",                           72.00,   2026),
    ("71045",  "5521", "Chest X-ray, 1 view",                            58.00,   2026),
    ("72148",  "5572", "MRI lumbar spine without contrast",              305.00,   2026),
    ("70553",  "5573", "MRI brain with and without contrast",            474.00,   2026),
    ("74177",  "5572", "CT abdomen and pelvis with contrast",            264.00,   2026),
    ("93000",  "5073", "ECG, 12-lead, with interpretation",               38.00,   2026),
    ("85025",  "5004", "CBC with automated differential",                 11.00,   2026),
    ("80053",  "5008", "Comprehensive metabolic panel (CMP)",             15.00,   2026),
    ("36415",  "5012", "Venipuncture (blood draw)",                        4.00,   2026),
    ("27447",  "5115", "Total knee arthroplasty (replacement)",        12998.00,   2026),
    ("43239",  "5301", "Upper GI endoscopy (EGD) with biopsy",         1075.00,   2026),
    ("45380",  "5302", "Colonoscopy with biopsy",                      1250.00,   2026),
]

# ---------------------------------------------------------------------------
# Regional procedure benchmarks
#
# Realistic price distribution data for common procedures.
# avg/median/p25/p75/min/max represent what hospitals actually charge
# (not what Medicare pays). Region "national" is a baseline;
# specific regions reflect geographic variation.
# ---------------------------------------------------------------------------

PROCEDURE_BENCHMARKS = [
    # CPT      region       sample  avg       median    p25       p75       min      max       medicare
    ("99283",  "national",  5200,   920.00,   850.00,   480.00,  1200.00,   195.00,  3800.00,   98.00),
    ("99284",  "national",  4100,  1650.00,  1500.00,   850.00,  2100.00,   350.00,  6500.00,  157.00),
    ("99285",  "national",  3800,  2800.00,  2500.00,  1400.00,  3600.00,   550.00, 12000.00,  227.00),
    ("71046",  "national",  6100,   450.00,   380.00,   180.00,   620.00,    45.00,  2200.00,   13.00),
    ("72148",  "national",  2900,  2800.00,  2400.00,  1200.00,  3800.00,   400.00,  8500.00,   97.00),
    ("70553",  "national",  2200,  3200.00,  2800.00,  1500.00,  4200.00,   500.00,  9800.00,  123.00),
    ("74177",  "national",  3400,  2200.00,  1900.00,   950.00,  2900.00,   300.00,  7200.00,   88.00),
    ("80053",  "national",  8500,   185.00,   150.00,    65.00,   250.00,    20.00,   900.00,   14.49),
    ("85025",  "national",  7800,   110.00,    85.00,    35.00,   150.00,    12.00,   550.00,   10.59),
    ("93000",  "national",  5600,   320.00,   270.00,   120.00,   450.00,    30.00,  1500.00,   11.00),
    ("27447",  "national",  1800, 48000.00, 42000.00, 28000.00, 62000.00, 15000.00,125000.00, 1576.00),
    ("43239",  "national",  2100,  3200.00,  2700.00,  1400.00,  4200.00,   500.00, 12000.00,  147.00),
    ("45380",  "national",  2400,  4100.00,  3500.00,  1800.00,  5400.00,   600.00, 15000.00,  198.00),
    ("36415",  "national",  9200,    45.00,    35.00,    15.00,    60.00,     5.00,   250.00,    3.00),
    # Southeast region (FL, GA, etc.)
    ("99285",  "southeast", 1200,  3100.00,  2800.00,  1600.00,  4000.00,   600.00, 13000.00,  227.00),
    ("71046",  "southeast", 1800,   500.00,   420.00,   200.00,   680.00,    50.00,  2400.00,   13.00),
    ("80053",  "southeast", 2500,   200.00,   165.00,    70.00,   275.00,    22.00,   950.00,   14.49),
    # Northeast region
    ("99285",  "northeast", 1000,  3500.00,  3100.00,  1800.00,  4500.00,   700.00, 14000.00,  227.00),
    ("71046",  "northeast", 1500,   550.00,   460.00,   220.00,   750.00,    55.00,  2600.00,   13.00),
    # Midwest region
    ("99285",  "midwest",    900,  2400.00,  2100.00,  1200.00,  3100.00,   450.00, 10000.00,  227.00),
    ("71046",  "midwest",   1400,   380.00,   320.00,   150.00,   520.00,    40.00,  1800.00,   13.00),
    # West region
    ("99285",  "west",      1100,  3300.00,  2900.00,  1700.00,  4200.00,   650.00, 13500.00,  227.00),
    ("71046",  "west",      1600,   480.00,   400.00,   190.00,   650.00,    48.00,  2300.00,   13.00),
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

# ---------------------------------------------------------------------------
# ZIP to locality/region map
#
# Prefix rows allow progressively-specific matching:
# - 5-digit exact ZIP when available
# - 3-digit ZIP prefix for metro/locality grouping
# - 1-digit fallback for broad region
# ---------------------------------------------------------------------------

ZIP_LOCALITY_MAP = [
    # Exact ZIPs used in tests and sample data
    ("33021", "0000000", "FL", "southeast"),
    ("33101", "0000000", "FL", "southeast"),
    ("90210", "0000000", "CA", "west"),
    ("10001", "0000000", "NY", "northeast"),
    ("60601", "0000000", "IL", "midwest"),
    # Common 3-digit prefixes
    ("330", "0000000", "FL", "southeast"),
    ("331", "0000000", "FL", "southeast"),
    ("902", "0000000", "CA", "west"),
    ("100", "0000000", "NY", "northeast"),
    ("606", "0000000", "IL", "midwest"),
    # Broad 1-digit fallback coverage
    ("0", "0000000", None, "northeast"),
    ("1", "0000000", None, "northeast"),
    ("2", "0000000", None, "southeast"),
    ("3", "0000000", None, "southeast"),
    ("4", "0000000", None, "midwest"),
    ("5", "0000000", None, "midwest"),
    ("6", "0000000", None, "midwest"),
    ("7", "0000000", None, "southeast"),
    ("8", "0000000", None, "west"),
    ("9", "0000000", None, "west"),
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

        # ---- OPPS rates ------------------------------------------------------
        row = db.execute("SELECT COUNT(*) AS cnt FROM hospital_opps_rates").fetchone()
        if row["cnt"] == 0:
            logger.info("hospital_opps_rates table is empty -- seeding %d rates", len(OPPS_RATES))
            db.executemany(
                """
                INSERT INTO hospital_opps_rates
                    (cpt_code, apc, description, national_payment_rate, effective_year)
                VALUES (?, ?, ?, ?, ?)
                """,
                OPPS_RATES,
            )
            logger.info("OPPS rate seed complete.")
        else:
            logger.debug("hospital_opps_rates already contains %d rows -- skipping seed.", row["cnt"])

        # ---- Procedure benchmarks ---------------------------------------------
        row = db.execute("SELECT COUNT(*) AS cnt FROM procedure_benchmarks").fetchone()
        if row["cnt"] == 0:
            logger.info("procedure_benchmarks table is empty -- seeding %d rows", len(PROCEDURE_BENCHMARKS))
            db.executemany(
                """
                INSERT INTO procedure_benchmarks
                    (cpt_code, region, sample_size, avg_charged, median_charged,
                     p25_charged, p75_charged, min_charged, max_charged, medicare_rate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                PROCEDURE_BENCHMARKS,
            )
            logger.info("Procedure benchmark seed complete.")
        else:
            logger.debug("procedure_benchmarks already contains %d rows -- skipping seed.", row["cnt"])

        # ---- ZIP locality map --------------------------------------------------
        row = db.execute("SELECT COUNT(*) AS cnt FROM zip_locality_map").fetchone()
        if row["cnt"] == 0:
            logger.info("zip_locality_map table is empty -- seeding %d rows", len(ZIP_LOCALITY_MAP))
            db.executemany(
                """
                INSERT INTO zip_locality_map
                    (zip_prefix, locality, state, region)
                VALUES (?, ?, ?, ?)
                """,
                ZIP_LOCALITY_MAP,
            )
            logger.info("ZIP locality map seed complete.")
        else:
            logger.debug("zip_locality_map already contains %d rows -- skipping seed.", row["cnt"])
