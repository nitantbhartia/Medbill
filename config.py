import os

# App
APP_NAME = "BillKarma"
APP_URL = os.getenv("APP_URL", "https://billkarma.app")
# Sitemap <lastmod> for every page. Bump it when a deploy changes pages site-wide,
# so Google recrawls them. 2026-11-11: relaunch, redesign and hospital regrade.
SITE_UPDATED = "2026-11-11"
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
ENV = os.getenv("ENV", "development").lower()

# Database
DB_PATH = os.getenv("DB_PATH", "data/app.db")
AUTO_BOOTSTRAP_HOSPITAL_DATA = os.getenv("AUTO_BOOTSTRAP_HOSPITAL_DATA", "false").lower() == "true"
CMS_HOSPITAL_GENERAL_CSV_URL = "https://data.cms.gov/provider-data/api/1/datastore/query/xubh-q36u/0/download?format=csv"
CMS_HOSPITAL_GENERAL_CSV_PATH = "data/cms/raw/hospital_general_information.csv"

# Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

# Analysis thresholds
MEDICARE_MARKUP_THRESHOLD = 3.0  # flag charges > 3x Medicare rate
HIGH_MARKUP_THRESHOLD = 5.0  # high severity if > 5x Medicare
HIGH_CHARGE_FLAG = 50000  # flag individual charges over $50k for review
HIGH_QUANTITY_FLAG = 3  # flag quantities > 3 for review

# Negotiation
NEGOTIATION_FEE_PERCENTAGE = 0.15
NEGOTIATION_FEE_CAP = 500.00
MAX_NEGOTIATION_ROUNDS = 5
DAYS_BETWEEN_FOLLOWUPS = 7
MAX_NEGOTIATION_DAYS = 45

# Email (for negotiation)
EMAIL_FROM_NAME = "BillKarma Patient Advocacy"
EMAIL_FROM_ADDRESS = os.getenv("EMAIL_FROM", "disputes@billkarma.app")
RESEND_API_KEY = os.getenv("RESEND_API_KEY", "")
INBOUND_WEBHOOK_SECRET = os.getenv("INBOUND_WEBHOOK_SECRET", "")

# Stripe
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_PRICE_REPORT = os.getenv("STRIPE_PRICE_REPORT", "")  # $19 report

# Slim launch: one paid product, the Bill Check Report. The scan and teaser are free; the
# per-charge findings, dispute letter and phone script unlock for REPORT_PRICE_CENTS.
# Set SLIM_LAUNCH=0 to make results free again and stop hiding the other product routes.
SLIM_LAUNCH = os.getenv("SLIM_LAUNCH", "1") == "1"
REPORT_PRICE_CENTS = int(os.getenv("REPORT_PRICE_CENTS", "1900"))
REPORT_PAYMENT_PURPOSE = "bill_report"
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")
STRIPE_SUCCESS_URL = os.getenv("STRIPE_SUCCESS_URL", f"{os.getenv('APP_URL', 'https://billkarma.app')}/dispute/payment-success?session_id={{CHECKOUT_SESSION_ID}}")
STRIPE_CANCEL_URL = os.getenv("STRIPE_CANCEL_URL", f"{os.getenv('APP_URL', 'https://billkarma.app')}/results/{{bill_id}}")

# Dispute flat-fee tiers (bill_total -> fee_cents)
# Under $1k: $29, $1k-$5k: $49, $5k-$20k: $99, Over $20k: $149
DISPUTE_FEE_TIERS = [
    (1000, 2900),
    (5000, 4900),
    (20000, 9900),
    (float("inf"), 14900),
]
DISPUTE_FOLLOWUP_DAYS = [7, 14, 30, 45]
# Certified mail costs several dollars a letter: send it with the initial letter and the final follow-up only.
CERTIFIED_MAIL_FOLLOWUP_NUMBERS = (len(DISPUTE_FOLLOWUP_DAYS),)
HOUSEHOLD_INCOME_MAX_USD = 5_000_000
HOUSEHOLD_SIZE_MAX = 20
DISPUTE_MAX_DAYS = 45
DAILY_JOBS_HOUR_UTC = 14  # follow-ups and reminders run once a day at this hour

# Concierge: denied-claim appeals (flat fee by amount denied)
APPEAL_PRICE_CENTS = 14900  # $149
APPEAL_PRICE_LARGE_CENTS = 29900  # $299
APPEAL_LARGE_CLAIM_THRESHOLD = 5000  # dollars denied at or above this pay the large price
# Days to file an internal appeal after the denial: 180 under ACA / ERISA rules (employer and
# individual plans), 65 for a Medicare Advantage reconsideration. Medicaid and other plans vary,
# so their deadline comes from the denial letter. Insurers decide in 30 days (pre-service),
# 60 days (post-service) or 72 hours (urgent); external review must be requested within
# 4 months of a final denial.
APPEAL_FILING_DAYS = {"employer": 180, "individual": 180, "medicare_advantage": 65}
APPEAL_DECISION_DAYS = {"pre_service": 30, "post_service": 60, "urgent": 3}
APPEAL_EXTERNAL_REVIEW_DAYS = 120
APPEAL_REMINDER_WINDOW_DAYS = 7

# Concierge: household bill plan (Stripe subscription)
HOUSEHOLD_PRICE_YEARLY_CENTS = 19900  # $199/year
HOUSEHOLD_PRICE_MONTHLY_CENTS = 2000  # $20/month
HOUSEHOLD_MATCH_TOLERANCE = 1.00  # dollars of rounding allowed between a bill and its EOB

# Concierge shared
OPS_NOTIFY_EMAIL = os.getenv("OPS_NOTIFY_EMAIL", "")
PRIVATE_UPLOAD_DIR = os.getenv("PRIVATE_UPLOAD_DIR", os.path.join(os.path.dirname(DB_PATH) or "data", "private_uploads"))

# Lob (for certified mail — debt validation letters)
LOB_API_KEY = os.getenv("LOB_API_KEY", "")
FDCPA_LETTER_PRICE_CENTS = 1900  # $19
CHARITY_CARE_APP_PRICE_CENTS = 900  # $9
SETTLEMENT_LETTER_PRICE_CENTS = 900  # $9

# Complaints to state Attorney Generals. Off until complaints.STATE_ATTORNEY_GENERAL addresses are verified.
AUTO_FILE_COMPLAINTS = os.getenv("AUTO_FILE_COMPLAINTS", "false").lower() == "true"
# Representative designations signed before this date don't authorize complaints.
COMPLAINT_AUTHORIZATION_START = "2026-11-16"

OPS_QUEUE_REPLY_LIMIT = 50

# Phaxio (fax sending). Twilio shut down its fax API in 2021.
PHAXIO_API_KEY = os.getenv("PHAXIO_API_KEY", "")
PHAXIO_API_SECRET = os.getenv("PHAXIO_API_SECRET", "")

# Directory monetization toggles
ENABLE_AFFILIATE_SLOTS = os.getenv("ENABLE_AFFILIATE_SLOTS", "false").lower() == "true"
ENABLE_HOSPITAL_CLAIM = os.getenv("ENABLE_HOSPITAL_CLAIM", "false").lower() == "true"
AFFILIATE_URL = os.getenv("AFFILIATE_URL", "")
CLAIM_HOSPITAL_URL = os.getenv("CLAIM_HOSPITAL_URL", "")
ENABLE_MARKUP_COMPARISONS = os.getenv("ENABLE_MARKUP_COMPARISONS", "true").lower() == "true"

# Stats cache TTL
STATS_CACHE_TTL_SECONDS = 60

# Rate limiting for /api/scan (per IP, in-memory)
RATE_LIMIT_REQUESTS = int(os.getenv("RATE_LIMIT_REQUESTS", "10"))
RATE_LIMIT_WINDOW_SECONDS = int(os.getenv("RATE_LIMIT_WINDOW_SECONDS", "3600"))
TOOLS_RATE_LIMIT_REQUESTS = int(os.getenv("TOOLS_RATE_LIMIT_REQUESTS", "60"))
TOOLS_RATE_LIMIT_WINDOW_SECONDS = int(os.getenv("TOOLS_RATE_LIMIT_WINDOW_SECONDS", "3600"))
DEBT_RATE_LIMIT_REQUESTS = int(os.getenv("DEBT_RATE_LIMIT_REQUESTS", "8"))
DEBT_RATE_LIMIT_WINDOW_SECONDS = int(os.getenv("DEBT_RATE_LIMIT_WINDOW_SECONDS", "600"))
DEBT_SEND_MAX_RETRIES = int(os.getenv("DEBT_SEND_MAX_RETRIES", "3"))
EMAIL_REPORT_RATE_LIMIT_REQUESTS = int(os.getenv("EMAIL_REPORT_RATE_LIMIT_REQUESTS", "3"))
EMAIL_REPORT_RATE_LIMIT_WINDOW_SECONDS = int(os.getenv("EMAIL_REPORT_RATE_LIMIT_WINDOW_SECONDS", "300"))
EMAIL_REPORT_BILL_DAILY_LIMIT = int(os.getenv("EMAIL_REPORT_BILL_DAILY_LIMIT", "20"))
EMAIL_REPORT_RECIPIENT_DAILY_LIMIT = int(os.getenv("EMAIL_REPORT_RECIPIENT_DAILY_LIMIT", "10"))
MAX_TOOL_PAYLOAD_BYTES = int(os.getenv("MAX_TOOL_PAYLOAD_BYTES", "32768"))
MAX_TOOL_CONTEXT_BYTES = int(os.getenv("MAX_TOOL_CONTEXT_BYTES", "8192"))

# Input length limits for user-supplied text fields
MAX_NAME_LEN = 200
MAX_ADDRESS_LEN = 300
MAX_ACCOUNT_NUMBER_LEN = 60
MAX_AMOUNT_LEN = 30
MAX_NOTE_LEN = 2000

# Admin API access for destructive/ops endpoints
ADMIN_API_TOKEN = os.getenv("ADMIN_API_TOKEN", "")

# IndexNow — instant URL submission to Bing, Yandex, etc.
# Generate once: python3 -c "import uuid; print(uuid.uuid4().hex)"
INDEXNOW_KEY = os.getenv("INDEXNOW_KEY", "b3e8f2a1c4d74e9f8a2b1c3d5e7f9a0b")

# Adaptive thresholds cache TTL (outcomes data changes slowly)
ADAPTIVE_THRESHOLDS_CACHE_TTL_SECONDS = 300

# Extraction validation
DOUBLE_EXTRACTION_THRESHOLD = 5000  # double-extract bills over $5k
MAX_REASONABLE_CHARGE = 500000
MAX_UPLOAD_SIZE_MB = int(os.getenv("MAX_UPLOAD_SIZE_MB", "20"))  # max per-file upload size

# OCR pipeline rollout
OCR_PREPROCESS_ENABLED = os.getenv("OCR_PREPROCESS_ENABLED", "true").lower() == "true"
OCR_ENSEMBLE_ENABLED = os.getenv("OCR_ENSEMBLE_ENABLED", "false").lower() == "true"
OCR_MAX_VARIANTS = int(os.getenv("OCR_MAX_VARIANTS", "3"))
OCR_RECONCILIATION_TOLERANCE_PCT = float(os.getenv("OCR_RECONCILIATION_TOLERANCE_PCT", "2.0"))

OCR_BENCHMARK_TRUTH_FILE = "test_assets/scan_baseline/synthetic_ground_truth.jsonl"
OCR_BENCHMARK_MIN_SCORE = 0.85

# Quality score weights for OCR extraction ranking
OCR_SCORE_PER_LINE_ITEM = 2.0
OCR_SCORE_PER_CPT = 2.5
OCR_SCORE_PER_AMOUNT = 2.0
OCR_SCORE_PER_DESCRIPTION = 1.0
OCR_SCORE_PROVIDER_NAME = 4.0
OCR_SCORE_TOTAL_CHARGED = 5.0
OCR_SCORE_TOTAL_PATIENT_OWES = 3.0
OCR_SCORE_RECON_PENALTY_MULTIPLIER = 1.5
OCR_SCORE_MAX_RECON_PENALTY = 25.0

# Free maps (Leaflet + OSM)
ENABLE_FREE_MAPS = os.getenv("ENABLE_FREE_MAPS", "true").lower() == "true"
MAP_TILE_URL = os.getenv("MAP_TILE_URL", "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png")
MAP_TILE_ATTRIBUTION = os.getenv(
    "MAP_TILE_ATTRIBUTION",
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
)
MAP_MAX_ZOOM = int(os.getenv("MAP_MAX_ZOOM", "18"))
GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY", "")

# Google Analytics
GA_MEASUREMENT_ID = os.getenv("GA_MEASUREMENT_ID", "G-QHRP0ZQD8K")

# Free geocoder backfill
GEOCODER_FALLBACK_ENABLED = os.getenv("GEOCODER_FALLBACK_ENABLED", "true").lower() == "true"
GEOCODER_REQUEST_DELAY_MS = int(os.getenv("GEOCODER_REQUEST_DELAY_MS", "1000"))

# Search snippet limits (characters) for page titles and meta descriptions
SEO_TITLE_MAX_CHARS = 60
SEO_META_MAX_CHARS = 155

# Google Search Console HTML-tag verification code (the content="..." value only)
GOOGLE_SITE_VERIFICATION = os.getenv("GOOGLE_SITE_VERIFICATION", "")

# State "most expensive hospitals" ranking pages
RANKING_MIN_PROCEDURES = 5   # a hospital needs this many priced procedures to be ranked
RANKING_MIN_HOSPITALS = 5    # a state needs this many ranked hospitals to get a page
RANKING_TOP_COUNT = 25       # hospitals shown in the most-expensive list
RANKING_BOTTOM_COUNT = 10    # hospitals shown in the least-expensive list

GRADED_LETTERS = ("A", "B", "C", "D", "F")  # billing grades; "N/A" means ungraded
CSV_MARKUP_DECIMALS = 2                     # markup precision in the grades CSV
BADGE_MARKUP_DECIMALS = 1                   # markup precision on the SVG badge, as shown on pages
BADGE_NAME_MAX_CHARS = 44                   # hospital name length on the badge before truncation
BADGE_CACHE_MAX_AGE_SECONDS = 86400         # badges change only when grades are recalculated
BADGE_WIDTH = 420
BADGE_HEIGHT = 72
BADGE_ACCENT_WIDTH = 6                      # colored bar on the badge's left edge
BADGE_TEXT_X = 20

# Guides shown first on /guides/ ("Start here"), in order
FEATURED_GUIDE_SLUGS = (
    ("how-to-get-itemized-hospital-bill", "Step 1"),
    ("common-hospital-billing-errors", "Step 2"),
    ("how-to-dispute-a-medical-bill", "Step 3"),
    ("hospital-financial-assistance-charity-care", "If you can't afford it"),
    ("medical-debt-collections-rights", "If it's in collections"),
    ("medical-bill-negotiation-service-cost", "If you're hiring help"),
)
# Guides shown per topic on /guides/ before "Show all"
GUIDES_PER_TOPIC = 6

# Press pitch drafts: how many states to write (highest median markup first)
PITCH_STATE_COUNT = 5
PITCH_OUTPUT_DIR = "seo/outreach"

# Appended to CSS/JS URLs so a deploy never serves stale styles from browser caches
ASSET_VERSION = (os.getenv("RAILWAY_GIT_COMMIT_SHA") or os.getenv("ASSET_VERSION") or "dev")[:8]

# Example itemized bill on the homepage (illustrative charges; Medicare rates are looked up live)
HOMEPAGE_EXAMPLE_BILL = (
    {"code": "99285", "desc": "Emergency visit, level 5", "amount": 4500.00, "flag": "Level 5 is for life-threatening problems. This visit ended with a splint.", "type": "upcoding", "tag": "Visit level"},
    {"code": "73610", "desc": "X-ray, ankle, 3 views", "amount": 610.00, "flag": ""},
    {"code": "80053", "desc": "Comprehensive metabolic panel", "amount": 198.00, "flag": ""},
    {"code": "80048", "desc": "Basic metabolic panel", "amount": 142.00, "flag": "Already included in the comprehensive panel.", "type": "unbundling", "bundled": "80053", "tag": "Overlap"},
    {"code": "36415", "desc": "Blood draw", "amount": 38.00, "flag": ""},
    {"code": "36415", "desc": "Blood draw", "amount": 38.00, "flag": "Billed twice for one draw.", "type": "duplicate", "tag": "Duplicate"},
)
HOMEPAGE_EXAMPLE_CLEAR_ERRORS = ("80048", "36415")
HOMEPAGE_EXAMPLE_SERVICE_DATE = "2026-03-03"

# Itemized-bill requests: HIPAA right of access gives the hospital 30 days (45 CFR 164.524(b)(2))
ITEMIZED_RESPONSE_DAYS = 30
ITEMIZED_LOOKUP_LIMIT = 8

# Good Faith Estimate vs bill check (patient-provider dispute resolution, PPDR).
# Source: https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/dispute-bill
# (page last modified 10/02/2026 per CMS; read 2026-11-16) and CMS's PPDR guidance PDF
# https://www.cms.gov/cciio/resources/regulations-and-guidance/downloads/good-faith-estimate-patient-provider-dispute-resolution-process-for-uninsured-or-self-pay-individuals.pdf
# Eligible: no insurance, or insurance not used and the provider was told so; care on or after 2022-01-01.
# The bill must be at least GFE_DISPUTE_THRESHOLD_USD above the estimate from the same provider or facility.
# Start within GFE_DISPUTE_DEADLINE_DAYS calendar days of the date on the initial bill.
# The fee is non-refundable and is deducted from what is owed if the dispute is decided for the patient.
# A reviewer can leave the bill as-is when the extra charges could not reasonably have been anticipated.
GFE_DISPUTE_THRESHOLD_USD = 400
GFE_DISPUTE_DEADLINE_DAYS = 120
GFE_DISPUTE_FEE_USD = 25
GFE_DISPUTE_INFO_URL = "https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/dispute-bill"
GFE_DISPUTE_FILING_URL = "https://nsa-idr.cms.gov/billdisputes/s/"
GFE_MAX_AMOUNT_USD = 10_000_000
GFE_FIELD_MAX_CHARS = 200

# MCP endpoint (/mcp) for AI assistants such as ChatGPT and Claude
MCP_PROTOCOL_VERSIONS = ("2025-11-25", "2025-06-18", "2025-03-26")
MCP_SERVER_VERSION = "1.0.0"
MCP_LINK_TAG = "utm_source=ai_assistant&utm_medium=mcp"

# Research report: procedures shown and the minimum hospitals behind any published figure
REPORT_CODES = ("99283", "99284", "99285", "71046", "74177", "70551", "73721", "77067", "80053", "85025", "45378", "93000")
REPORT_MIN_HOSPITALS = 20
REPORT_STATE_CODE = "99284"
REPORT_MIN_STATE_HOSPITALS = 5

# Billing contact discovery (scripts/discover_billing_contacts.py)
BILLING_CONTACT_USER_AGENT = "BillKarmaBot/1.0 (+https://billkarma.app/about/)"
BILLING_CONTACT_TIMEOUT_SECONDS = 10
BILLING_CONTACT_MIN_INTERVAL_SECONDS = 1.0
BILLING_CONTACT_MAX_PAGES = 6  # per hospital, homepage included
BILLING_CONTACT_MAX_NAV_LINKS = 2
BILLING_CONTACT_MAX_HOST_FAILURES = 3
BILLING_CONTACT_KEYWORD_WINDOW_CHARS = 200
BILLING_CONTACT_NAME_MIN_TOKEN_CHARS = 4
BILLING_CONTACT_CALL_CUE_CHARS = 40
BILLING_CONTACT_MAIL_CUE_CHARS = 80

# Spanish section (/es/). Machine-drafted: leave off until a native speaker has reviewed it.
ES_PAGES_ENABLED = os.getenv("ES_PAGES_ENABLED", "false").lower() == "true"

# Partner referral links (/scan?ref=partner-slug)
REFERRAL_COOKIE_NAME = "bk_ref"
REFERRAL_COOKIE_MAX_AGE_SECONDS = 60 * 60 * 24 * 30
REFERRAL_CODE_PATTERN = r"[a-z0-9-]{1,40}"
PARTNER_REPORT_DAYS = 90
PARTNER_CONTACT_EMAIL = os.getenv("PARTNER_CONTACT_EMAIL", "support@billkarma.app")

# Hospital x procedure pages
HOSPITAL_PROCEDURE_SITEMAP_MAX = 40000  # sitemap files allow 50,000 URLs
HOSPITAL_PROCEDURE_ALTERNATIVES = 5
HOSPITAL_PROCEDURE_MIN_HOSPITALS = 30  # codes priced by fewer hospitals are noindex and left out of the sitemap

# Mobile app
MOBILE_TOKEN_BYTES = 32
MOBILE_REGISTER_LIMIT_PER_HOUR = 60  # per IP; carrier and office networks share addresses
MOBILE_SCAN_MAX_PAGES = 10
MOBILE_EVENT_PROPS_MAX_BYTES = 2048
MOBILE_PLUS_CACHE_SECONDS = 600
MOBILE_HOSPITAL_SEARCH_LIMIT = 10
MOBILE_EVENT_NAMES = {
    "onboarding_step_viewed", "onboarding_completed", "onboarding_skipped",
    "hospital_insight_shown",
    "scan_started", "scan_succeeded", "scan_failed",
    "teaser_viewed", "clean_result_viewed",
    "paywall_viewed", "paywall_plan_selected", "paywall_closed", "exit_offer_viewed",
    "purchase_completed",
    "letter_shared", "phone_script_viewed", "call_logged", "result_shared",
    "notification_prompt_shown", "notification_prompt_accepted",
    "review_prompt_requested", "data_deleted",
    "outcome_reported", "win_shared", "signin_prompt_shown", "signin_completed", "letter_emailed",
}
MOBILE_BILL_TYPES = {"er", "hospital_stay", "surgery", "lab_imaging", "doctor", "other"}
MOBILE_AMOUNT_BANDS = {"under_500", "500_2k", "2k_10k", "over_10k", "unsure"}
MOBILE_INSURANCE_STATUSES = {"insured", "uninsured", "unsure"}
MOBILE_SITUATIONS = {"unexpected", "too_high", "confusing", "out_of_network", "collections", "denied", "cant_afford"}
MOBILE_DUE_BANDS = {"this_week", "this_month", "past_due", "unsure"}
MOBILE_ATTRIBUTION_SOURCES = {"tiktok", "instagram", "youtube", "reddit", "google", "article", "friend", "other"}
MOBILE_ONBOARDING_VARIANTS = {"A", "B"}
REVENUECAT_API_URL = "https://api.revenuecat.com/v1/subscribers"
REVENUECAT_SECRET_API_KEY = os.getenv("REVENUECAT_SECRET_API_KEY", "")
REVENUECAT_WEBHOOK_AUTH = os.getenv("REVENUECAT_WEBHOOK_AUTH", "")
REVENUECAT_REPORT_PRODUCT_ID = os.getenv("REVENUECAT_REPORT_PRODUCT_ID", "bk_report_unlock")
REVENUECAT_REPORT_OFFER_PRODUCT_ID = os.getenv("REVENUECAT_REPORT_OFFER_PRODUCT_ID", "bk_report_unlock_offer")
REVENUECAT_PLUS_ENTITLEMENT = os.getenv("REVENUECAT_PLUS_ENTITLEMENT", "plus")
IOS_APP_ID = os.getenv("IOS_APP_ID", "")
APP_STORE_ID = os.getenv("APP_STORE_ID", "")

# Sign in with Apple (optional accounts for the iOS app)
APPLE_BUNDLE_ID = os.getenv("APPLE_BUNDLE_ID", "app.billkarma.ios")
APPLE_ISSUER = "https://appleid.apple.com"
APPLE_KEYS_URL = "https://appleid.apple.com/auth/keys"
APPLE_TOKEN_URL = "https://appleid.apple.com/auth/token"
APPLE_REVOKE_URL = "https://appleid.apple.com/auth/revoke"
APPLE_SIGNIN_KEY_ID = os.getenv("APPLE_SIGNIN_KEY_ID", "")
APPLE_SIGNIN_TEAM_ID = os.getenv("APPLE_SIGNIN_TEAM_ID", "")
APPLE_SIGNIN_PRIVATE_KEY = os.getenv("APPLE_SIGNIN_PRIVATE_KEY", "").replace("\\n", "\n")
APPLE_CLIENT_SECRET_TTL_SECONDS = 300
APPLE_HTTP_TIMEOUT_SECONDS = 15

# Medicare rate coverage. A table smaller than this only holds the built-in samples, not the CMS fee schedule.
MIN_FULL_MEDICARE_RATE_COUNT = 1000
LAB_RATE_MARKER_CODE = "80053"  # a common blood test that only exists once the lab fee schedule is loaded

# A scan whose line items differ from the bill total by more than this is probably misread.
READ_CHECK_TOLERANCE = 0.10
READ_CHECK_MIN_GAP = 25.0
