import os

# App
APP_NAME = "BillScan"
APP_URL = os.getenv("APP_URL", "http://localhost:8000")
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"

# Database
DB_PATH = os.getenv("DB_PATH", "data/app.db")

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
EMAIL_FROM_NAME = "BillScan Patient Advocacy"
EMAIL_FROM_ADDRESS = os.getenv("EMAIL_FROM", "disputes@billscan.app")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "")

# Stripe
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_PRICE_REPORT = os.getenv("STRIPE_PRICE_REPORT", "")  # $19 report

# Stats cache TTL
STATS_CACHE_TTL_SECONDS = 60

# Extraction validation
DOUBLE_EXTRACTION_THRESHOLD = 5000  # double-extract bills over $5k
MAX_REASONABLE_CHARGE = 500000
