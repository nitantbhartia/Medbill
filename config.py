import os

# App
APP_NAME = "BillKarma"
APP_URL = os.getenv("APP_URL", "https://billkarma.app")
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"

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
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "")

# Stripe
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_PRICE_REPORT = os.getenv("STRIPE_PRICE_REPORT", "")  # $19 report

# Directory monetization toggles
ENABLE_AFFILIATE_SLOTS = os.getenv("ENABLE_AFFILIATE_SLOTS", "false").lower() == "true"
ENABLE_HOSPITAL_CLAIM = os.getenv("ENABLE_HOSPITAL_CLAIM", "false").lower() == "true"
AFFILIATE_URL = os.getenv("AFFILIATE_URL", "")
CLAIM_HOSPITAL_URL = os.getenv("CLAIM_HOSPITAL_URL", "")
ENABLE_MARKUP_COMPARISONS = os.getenv("ENABLE_MARKUP_COMPARISONS", "false").lower() == "true"

# Stats cache TTL
STATS_CACHE_TTL_SECONDS = 60

# Rate limiting for /api/scan (per IP, in-memory)
RATE_LIMIT_REQUESTS = int(os.getenv("RATE_LIMIT_REQUESTS", "10"))
RATE_LIMIT_WINDOW_SECONDS = int(os.getenv("RATE_LIMIT_WINDOW_SECONDS", "3600"))

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
