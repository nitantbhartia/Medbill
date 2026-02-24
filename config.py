import os

# App
APP_NAME = "BillKarma"
APP_URL = os.getenv("APP_URL", "https://billkarma.app")
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
ENV = os.getenv("ENV", "development").lower()

# Database
DB_PATH = os.getenv("DB_PATH", "data/app.db")
AUTO_BOOTSTRAP_HOSPITAL_DATA = os.getenv("AUTO_BOOTSTRAP_HOSPITAL_DATA", "false").lower() == "true"

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

# Stripe
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_PRICE_REPORT = os.getenv("STRIPE_PRICE_REPORT", "")  # $19 report
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
DISPUTE_MAX_DAYS = 45

# Lob (for certified mail — debt validation letters)
LOB_API_KEY = os.getenv("LOB_API_KEY", "")
FDCPA_LETTER_PRICE_CENTS = 1900  # $19
CHARITY_CARE_APP_PRICE_CENTS = 900  # $9
SETTLEMENT_LETTER_PRICE_CENTS = 900  # $9

# Twilio (for fax sending — optional)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_FAX_FROM = os.getenv("TWILIO_FAX_FROM", "")

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

# Free geocoder backfill
GEOCODER_FALLBACK_ENABLED = os.getenv("GEOCODER_FALLBACK_ENABLED", "true").lower() == "true"
GEOCODER_REQUEST_DELAY_MS = int(os.getenv("GEOCODER_REQUEST_DELAY_MS", "1000"))
