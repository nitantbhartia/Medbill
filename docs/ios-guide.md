# BillKarma iOS — Technical Implementation Guide (v1)

Build guide for a native iOS app that lets a user photograph a medical bill, see how much may be wrong for free, and pay to unlock the full report, dispute letter and phone script. It reuses the existing BillKarma backend (`nitantbhartia/Medbill`: FastAPI + SQLite + Gemini vision OCR).

---

## 0. How to use this guide with Claude Code

There are two codebases:

| Part | Repo | What changes |
|---|---|---|
| **A. Backend** | existing `Medbill` repo | New mobile endpoints, device auth, in-app purchase unlocks, one security fix, universal links |
| **B. iOS app** | new repo `billkarma-ios` | New SwiftUI app |

Work **phase by phase** (section 7). For each phase, paste this whole guide into Claude Code once, then send the phase prompt from section 7. Don't ask for everything at once. Each phase has acceptance criteria. Don't move on until they pass.

The backend has a `CLAUDE.md` with strict style rules (simple functions, files under 300 lines, raw parameterized SQL, pinned dependencies, `{"status": "ok"|"error", "data": ...}` responses, constants in `config.py`). **Everything in Part A must follow it.** Part B follows the same spirit: no third-party code except RevenueCat.

---

## 1. Scope

### v1 (ship this)
1. Onboarding quiz (5 questions, includes attribution and ZIP code)
2. Scan a bill: document camera (multi-page), photo picker, or PDF import
3. Free result: provider, amount owed, **number of flagged charges, estimated savings**, and problem types (e.g. "2 × Possible duplicate"). The per-charge details stay blurred.
4. Paywall: **one-time report unlock** (consumable IAP) or **BillKarma Plus** (annual subscription: unlimited unlocks)
5. Full report: each flagged charge with code, charged amount, Medicare rate, markup, reasons, and savings
6. Dispute letter (fill in name and account number) → share as PDF or copy text
7. Phone script
8. "My Bills" list
9. Settings: restore purchases, delete my data, privacy policy, terms, support email

### Not in v1 (phase 2+)
- Paid done-for-you dispute service (Lob mailing, e-sign, follow-ups). It's a real-world service, so it may qualify for non-IAP payment under App Review Guideline 3.1.3(e), but **confirm before shipping**. Keeping it out of v1 avoids review risk.
- EOB upload, accounts and login, push notifications, widgets, Android.

### Free vs paid (mirrors the web's `SLIM_LAUNCH` model in `report.py`)
- A bill with **no flagged charges is never charged for**. `report.is_unlocked()` already returns `True` in that case, so the app shows the full (clean) result.
- A bill with flagged charges shows only `report.teaser()` until it's unlocked.

---

## 2. Architecture

```
┌──────────────────────── iOS app (SwiftUI, iOS 17+) ────────────────────────┐
│ Onboarding → Scan (VisionKit) → Processing → Teaser → Paywall → Report     │
│        │                                         │                         │
│   Keychain: device_token                RevenueCat SDK (appUserID =        │
│        │                                device_id from backend)            │
└────────┼─────────────────────────────────────────┼─────────────────────────┘
         │ HTTPS  Authorization: Bearer <token>    │ StoreKit purchase
         ▼                                         ▼
┌──────── BillKarma FastAPI (existing) ───────┐   ┌──── RevenueCat ────┐
│ /api/m/*  (new mobile_routes.py)            │◄──│ webhook → /api/m/  │
│   ├─ scanner.process_bill_with_verification │   │   revenuecat/hook  │
│   ├─ analyzer.analyze_bill / save_bill...   │──►│ REST: GET /v1/     │
│   ├─ report.teaser / is_unlocked            │   │   subscribers/{id} │
│   ├─ charge_summary.group_findings_by_charge│   └────────────────────┘
│   └─ dispute_workflow.build_dispute_letter  │
│ SQLite: bills, findings, report_unlocks,    │
│         bill_access_sessions, + mobile_*    │
└─────────────────────────────────────────────┘
```

Key design decisions:
- **No accounts in v1.** The app registers an anonymous device and gets a random token (stored in the Keychain). That token is used as the `session_id` in the existing `bill_access_sessions` table, so `grant_bill_access` and `has_bill_access` work unchanged.
- **RevenueCat's appUserID = the backend `device_id`**, so purchases and webhooks map straight to the device.
- **Paid unlocks reuse `report_unlocks`.** IAP rows use `stripe_session_id = "iap:<store_transaction_id>"`. The column is UNIQUE, which makes unlocks idempotent for free, and `report.is_paid()` / `is_unlocked()` keep working with no changes.
- **The server decides what's locked.** Mobile endpoints never return per-charge details for a locked bill.

---

## Part A — Backend changes (Medbill repo)

### A0. Security fix to make first (web, already live)
`POST /api/scan` in `api.py` returns the full `analysis` (every finding) in its response even when `SLIM_LAUNCH` is on and the bill isn't paid. Anyone can read the paid content from the network response.

**Fix:** after saving, if `not report_module.is_unlocked(bill_id)`, replace `analysis` in the response with `{"locked": True, **report_module.teaser(bill_id)}` and strip `findings`. Check `templates/` and `static/` JS for anything that reads `data.analysis.findings` right after a scan, and have it call `GET /api/results/{bill_id}` instead. Add a test: scan a bill with flagged charges → response contains no `findings`.

### A1. Database (new numbered SQL file, run once, in the same style as `db.py`)

```sql
CREATE TABLE IF NOT EXISTS mobile_devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT NOT NULL UNIQUE,          -- public id, also the RevenueCat appUserID
    token_hash TEXT NOT NULL UNIQUE,         -- sha256 of the bearer token; raw token never stored
    platform TEXT NOT NULL DEFAULT 'ios',
    app_version TEXT,
    attribution_source TEXT,                 -- "where did you hear about us"
    zip_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_seen_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS mobile_entitlements (
    device_id TEXT PRIMARY KEY,
    plus_active INTEGER NOT NULL DEFAULT 0,
    plus_expires_at TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS mobile_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT NOT NULL,
    name TEXT NOT NULL,
    props_json TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_mobile_events_name ON mobile_events(name, created_at);
```

### A2. `config.py` additions

```python
# Mobile app
MOBILE_TOKEN_BYTES = 32
MOBILE_SCAN_MAX_PAGES = 10
MOBILE_EVENT_NAMES = {
    "onboarding_completed", "scan_started", "scan_succeeded", "scan_failed",
    "teaser_viewed", "paywall_viewed", "purchase_completed", "letter_shared",
    "phone_script_viewed", "data_deleted",
}
REVENUECAT_SECRET_API_KEY = os.getenv("REVENUECAT_SECRET_API_KEY", "")   # sk_... (server only)
REVENUECAT_WEBHOOK_AUTH = os.getenv("REVENUECAT_WEBHOOK_AUTH", "")       # shared secret header value
REVENUECAT_REPORT_PRODUCT_ID = os.getenv("REVENUECAT_REPORT_PRODUCT_ID", "bk_report_unlock")
REVENUECAT_PLUS_ENTITLEMENT = os.getenv("REVENUECAT_PLUS_ENTITLEMENT", "plus")
IOS_APP_ID = os.getenv("IOS_APP_ID", "")                                 # e.g. TEAMID.app.billkarma.ios
APP_STORE_ID = os.getenv("APP_STORE_ID", "")                             # numeric, for the smart banner
```

### A3. Extract the scan pipeline (refactor, no behavior change)
`api.scan_bill` currently does validation, OCR, analysis and saving inline. Move the core into **`scan_pipeline.py`** so web and mobile share it:

```python
def run_scan(images: list[tuple[bytes, str]], zip_code: str, user_id: int | None,
             referral_code: str | None) -> tuple[int, dict, dict]:
    """OCR one or more pages, analyze, save. Returns (bill_id, extracted, analysis)."""
    if len(images) == 1:
        extracted = scanner.process_bill_with_verification(*images[0])
    else:
        extracted = scanner.process_multi_page_bill(images)
    extracted = scrub_extracted_data(extracted)
    analysis = analyzer.analyze_bill(extracted, zip_code)
    bill_id = analyzer.save_bill_and_findings(user_id, extracted, analysis, zip_code, referral_code)
    return bill_id, extracted, analysis
```

`api.scan_bill` then calls `run_scan` and keeps its EOB merge, evidence rows, audit log and error mapping (`ScannerNotConfigured` → 503, `ValueError` → 400). **All existing tests must still pass.**

### A4. `mobile_auth.py` (device tokens)

```python
def register_device(app_version: str) -> dict:
    """Create an anonymous device. Returns {"device_id", "token"}; the token is shown once."""

def device_from_request(request: Request) -> str:
    """FastAPI dependency: read 'Authorization: Bearer <token>', look up sha256(token),
    update last_seen_at, return device_id. Raise 401 if missing or unknown."""

def require_device_bill_access(device_id: str, bill_id: int) -> None:
    """Raise 403 unless has_bill_access(device_id, bill_id)."""
```

- Generate the token with `secrets.token_urlsafe(config.MOBILE_TOKEN_BYTES)` and the device_id with `secrets.token_hex(16)`.
- Store only `hashlib.sha256(token).hexdigest()`.
- Use **device_id as the `session_id`** when calling `grant_bill_access` / `has_bill_access`.

### A5. `mobile_routes.py` — `APIRouter(prefix="/api/m")`, included in `main.py`

All responses use `{"status": "ok", "data": {...}}`. Errors use `HTTPException` with the right code. Every route except `/device` and the webhook needs `device_id = Depends(device_from_request)`.

| Method & path | Request | Response `data` | Notes |
|---|---|---|---|
| `POST /device` | JSON `{"app_version": "1.0.0"}` | `{"device_id", "token"}` | Rate-limit by IP (reuse `_check_rate_limit` pattern) |
| `POST /profile` | JSON `{"zip_code", "attribution_source"}` | `{"saved": true}` | Validate 5-digit ZIP; attribution is one of a fixed list (see B4) |
| `POST /scan` | multipart: `pages[]` (jpeg/png/heic/pdf), `zip_code` | `BillView` (below) | ≤ `MOBILE_SCAN_MAX_PAGES`; size/MIME checks as in `api.scan_bill`; rate-limit per device; `grant_bill_access(device_id, bill_id)` |
| `GET /bills` | – | `{"bills": [BillSummary]}` | Bills this device can access, newest first |
| `GET /bills/{id}` | – | `BillView` | 403 if no access |
| `POST /bills/{id}/letter` | JSON `{"requestor_name", "account_number", "finding_ids": []}` | `build_dispute_letter(...)` result | 402 if locked; same length validation as `api.get_dispute_letter` |
| `GET /bills/{id}/phone-script` | – | `{"script": str}` | 402 if locked; `build_phone_script(bill_id)` |
| `POST /bills/{id}/unlock` | JSON `{"transaction_id": "..."}` or `{}` for Plus | `BillView` (unlocked) | See A6 |
| `DELETE /bills/{id}` | – | `{"deleted": true}` | User-initiated; `compliance.delete_bill_data` + remove access row; audit log |
| `DELETE /device` | – | `{"deleted": true}` | Deletes all this device's bills, events, entitlement, device row ("Delete my data") |
| `POST /events` | JSON `{"name", "props": {}}` | `{"ok": true}` | Drop names not in `MOBILE_EVENT_NAMES`; cap props at 2 KB |
| `POST /revenuecat/webhook` | RevenueCat event JSON | `{"ok": true}` | Check `Authorization` header == `REVENUECAT_WEBHOOK_AUTH` |

**`BillView` shape** (the one model the app renders):

```json
{
  "bill_id": 123,
  "locked": true,
  "bill": {
    "id": 123, "provider_name": "Scripps Mercy Hospital", "bill_date": "2026-09-14",
    "total_charged": 4210.0, "total_patient_owes": 1840.0
  },
  "teaser": {
    "charge_count": 3, "strong_count": 2, "total_savings": 912.4,
    "reason_counts": [{"label": "Possible duplicate", "count": 2}, {"label": "Priced far above Medicare", "count": 1}]
  },
  "report": null,
  "price": {"report_product_id": "bk_report_unlock"},
  "extraction_quality": 0.86
}
```

When unlocked (`report.is_unlocked(bill_id)` or the device has active Plus), `locked` is `false` and `report` is `charge_summary.group_findings_by_charge(findings, owed)`:

```json
"report": {
  "total_savings": 912.4, "strong_count": 2,
  "charges": [{
    "code": "99285", "description": "ER visit, high severity", "date": "2026-09-14",
    "charged": 3100.0, "medicare_rate": 412.18, "markup": 7.5, "savings": 610.0,
    "severity": "high", "strong": true, "finding_ids": [881, 882],
    "reasons": [{"type": "pricing_markup", "label": "Priced far above Medicare",
                 "message": "Charged 7.5x the Medicare rate for your area.", "severity": "high"}]
  }]
}
```

Build it with one helper, `build_bill_view(bill_id, device_id) -> dict`, so `/scan`, `/bills/{id}` and `/unlock` return the exact same shape. A locked view **must not** include `report` or any finding text.

### A6. In-app purchase unlocks

**Products (create in App Store Connect, then attach in RevenueCat):**

| Product ID | Type | Suggested price | RevenueCat |
|---|---|---|---|
| `bk_report_unlock` | Consumable | $19.99 | Non-subscription product in offering `default` |
| `bk_plus_annual` | Auto-renewable, 1 year | $59.99 | Grants entitlement `plus` |
| `bk_report_unlock_offer` | Consumable | $14.99 | Exit-offer experiment E4 only, offering `exit_offer`; the backend treats it like `bk_report_unlock` |

The prices are starting points. Change them in App Store Connect, not in code.

**`POST /api/m/bills/{id}/unlock` logic:**
1. `require_device_bill_access(device_id, bill_id)`.
2. If the body has `transaction_id`: call RevenueCat `GET https://api.revenuecat.com/v1/subscribers/{device_id}` with `Authorization: Bearer REVENUECAT_SECRET_API_KEY` (use `urllib.request`, matching how `payment._stripe_get` avoids extra dependencies). Confirm `subscriber.non_subscriptions[REVENUECAT_REPORT_PRODUCT_ID]` (or `bk_report_unlock_offer`) contains an entry whose `store_transaction_id` == `transaction_id`. If it does, insert into `report_unlocks` (`bill_id`, `stripe_session_id="iap:"+transaction_id`, `amount_cents=config.REPORT_PRICE_CENTS`, `status='paid'`, `paid_at=CURRENT_TIMESTAMP`) with `INSERT OR IGNORE`.
   - **Same transaction, different bill:** the UNIQUE constraint already blocks reusing one purchase for a second bill. Return 409 `"This purchase was already used for another bill"`.
3. If there's no `transaction_id`: check Plus (refresh from the RevenueCat REST API if the cached `mobile_entitlements` row is older than 10 minutes). Plus active → insert `report_unlocks` with `stripe_session_id = "plus:"+device_id+":"+bill_id`. That gives an audit trail, and the bill stays unlocked if Plus lapses later.
4. Return `build_bill_view(...)`.

**Webhook (`/api/m/revenuecat/webhook`):** upsert `mobile_entitlements` from the event's `app_user_id`, `entitlement_ids` and `expiration_at_ms`. Handle `INITIAL_PURCHASE`, `RENEWAL`, `PRODUCT_CHANGE`, `UNCANCELLATION` (active), and `EXPIRATION` (inactive). `CANCELLATION` only means auto-renew is off, so keep the row active until expiration. Log and return 200 for other event types. If RevenueCat reports a refund of `bk_report_unlock` (a `CANCELLATION` event for that product; check RevenueCat's current webhook docs for the exact fields), set the matching `iap:` row in `report_unlocks` to `status='refunded'`.

**Mock mode for development:** if `config.ENV != "production"` and `REVENUECAT_SECRET_API_KEY` is empty, accept `transaction_id` values starting with `"test_"` without calling RevenueCat. The simulator and pytest can then cover the full flow.

### A7. Universal links and web → app
- Serve `GET /.well-known/apple-app-site-association` (JSON, `content-type: application/json`, no redirect):
  ```json
  {"applinks": {"details": [{"appIDs": ["<IOS_APP_ID>"], "components": [{"/": "/scan*"}, {"/": "/app/*"}]}]}}
  ```
- Add `<meta name="apple-itunes-app" content="app-id={{APP_STORE_ID}}">` to the base template when `APP_STORE_ID` is set. This shows a Smart App Banner on every guide page, turning SEO traffic into app installs.
- Add an "Open in the app" button next to existing scan CTAs that links to `https://billkarma.app/app/scan`. With the app installed, iOS opens it; without, the page falls through to the normal web scan.

### A8. Backend tests (`tests/test_mobile_routes.py`)
Use the existing `conftest.py` fixtures and realistic data from `test_assets/scan_baseline/` and `data/ocr_benchmark/` (real-looking CPT codes and dollar amounts, per `CLAUDE.md`). Mock `scanner` calls the same way `test_api.py` does.
1. Register device → token works on `/bills`; bad token → 401.
2. Scan → `BillView` with `locked=true` and no `report` key content when charges are flagged.
3. Scan a clean bill (no findings) → `locked=false`.
4. Device B can't read device A's bill → 403.
5. Unlock with mock `test_tx1` → `locked=false`; reusing `test_tx1` on another bill → 409.
6. Letter and phone script → 402 while locked, 200 after unlock.
7. Webhook with wrong auth → 401. `EXPIRATION` → Plus inactive.
8. `DELETE /device` removes bills and access rows.
9. Web `/api/scan` no longer leaks `findings` for locked bills (A0).

---

## Part B — iOS app (new repo `billkarma-ios`)

### B1. Project setup
- Xcode 16+, Swift 5.10+ (Swift 6 language mode is fine), **iOS 17.0 minimum**, iPhone only, portrait.
- App name **BillKarma**, bundle ID `app.billkarma.ios`.
- Swift Package dependencies (only these):
  - `https://github.com/RevenueCat/purchases-ios-spm` → product `RevenueCat` (the paywall is custom SwiftUI, see B10.5, so `RevenueCatUI` isn't needed)
- Capabilities: **In-App Purchase**; **Associated Domains** → `applinks:billkarma.app`; **Sign in with Apple**; **Keychain Sharing** is not needed (synchronizable Keychain items work without it).
- Info.plist:
  - `NSCameraUsageDescription` = "BillKarma uses the camera to scan your medical bill."
  - `NSPhotoLibraryUsageDescription` isn't needed with `PhotosPicker` (it doesn't require permission).
- Build configurations: `Debug` → `API_BASE_URL = http://localhost:8000` (simulator) and the RevenueCat **test store** key. `Release` → `https://billkarma.app` and the production public key. Put these in `.xcconfig` files and read them via Info.plist keys. **No secret keys in the app**: the RevenueCat public SDK key only.
- `PrivacyInfo.xcprivacy`: no tracking; collected data types = Health (medical bill contents), Other User Content (images), Purchase History, Coarse Location (ZIP). All "App Functionality", none "Tracking". Required-reason API: `UserDefaults` (CA92.1).

### B2. Folder structure

```
BillKarma/
  App/            BillKarmaApp.swift, AppState.swift, Config.swift, DeepLinks.swift
  Networking/     APIClient.swift, APIError.swift, Endpoints.swift, Multipart.swift
  Models/         BillView.swift, BillSummary.swift, Letter.swift, Device.swift
  Storage/        Keychain.swift
  Purchases/      PurchaseService.swift
  Analytics/      Analytics.swift
  Features/
    Onboarding/   OnboardingFlow.swift (variant routing), OnboardingModel.swift (answers + rules from B10.4),
                  WelcomeView.swift, EducationSlidesView.swift, SingleChoiceStep.swift, MultiChoiceStep.swift,
                  ProviderSearchStep.swift, ZipStep.swift, TrustView.swift, BuildingCheckView.swift,
                  PlanView.swift, ScanTipsView.swift, OnboardingCopy.swift (all B10.3 strings in one place)
    Scan/         ScanHomeView.swift, DocumentScanner.swift, ImagePrep.swift, ProcessingView.swift
    Results/      TeaserView.swift, CleanResultView.swift, ReportView.swift, ChargeRow.swift, ShareCardView.swift
    Paywall/      PaywallScreen.swift, PlanCard.swift, PaywallTimeline.swift, ExitOfferSheet.swift
    Letter/       LetterFormView.swift, LetterPreviewView.swift, LetterPDF.swift
    PhoneScript/  PhoneScriptView.swift
    Bills/        BillsListView.swift
    Settings/     SettingsView.swift
    Engagement/   ReminderService.swift (local notifications), ReviewPromptPolicy.swift
  Design/         Theme.swift (tokens), Typography.swift, Components.swift (see B7 table), Haptics.swift
  Resources/Fonts/ InterTight-*.ttf, Inter-*.ttf, IBMPlexMono-*.ttf + OFL license files
  Resources/      Assets.xcassets, PrivacyInfo.xcprivacy
BillKarmaTests/   ModelDecodingTests.swift, ImagePrepTests.swift, Fixtures/*.json
```

Keep files short. Use `@Observable` view models, no extra architecture framework.

### B3. Networking core

```swift
struct Envelope<T: Decodable>: Decodable { let status: String; let data: T }

enum APIError: Error, LocalizedError {
    case unauthorized, forbidden, paymentRequired, conflict(String), rateLimited,
         unavailable, badRequest(String), server, offline
    var errorDescription: String? { /* human copy, see B9 */ }
}

final class APIClient {
    static let shared = APIClient()
    private let session: URLSession            // timeoutIntervalForRequest = 120 (OCR can take 20–60s)
    private let decoder: JSONDecoder = {
        let d = JSONDecoder(); d.keyDecodingStrategy = .convertFromSnakeCase; return d
    }()

    func send<T: Decodable>(_ endpoint: Endpoint) async throws -> T
    // Adds "Authorization: Bearer <token>" from Keychain.
    // Maps HTTP 401/402/403/409/429/503/400/5xx to APIError.
    // On 401: clear the token, re-register the device once, retry once.
}
```

- `Multipart.swift`: build `multipart/form-data` for `POST /api/m/scan` with fields `zip_code` and repeated `pages` parts (`image/jpeg` or `application/pdf`). Upload with `URLSession.upload(for:from:)`.
- `Keychain.swift`: store/read/delete `device_token` and `device_id` (`kSecClassGenericPassword`, `kSecAttrAccessibleAfterFirstUnlock`, **`kSecAttrSynchronizable = true`** so they move to a new iPhone via iCloud Keychain — B12.8).

**Models** (Codable, matching A5 exactly; amounts are `Double?` because the backend can return null):

```swift
struct BillView: Decodable, Identifiable {
    var id: Int { billId }
    let billId: Int
    let locked: Bool
    let bill: BillHeader
    let teaser: Teaser?
    let report: Report?
    let price: Price?
    let extractionQuality: Double?
}
struct BillHeader: Decodable { let id: Int; let providerName: String?; let billDate: String?
                               let totalCharged: Double?; let totalPatientOwes: Double? }
struct Teaser: Decodable { let chargeCount: Int; let strongCount: Int; let totalSavings: Double
                           let reasonCounts: [ReasonCount] }
struct ReasonCount: Decodable, Hashable { let label: String; let count: Int }
struct Report: Decodable { let totalSavings: Double; let strongCount: Int; let charges: [Charge] }
struct Charge: Decodable, Identifiable {
    var id: String { (code ?? "bill") + (date ?? "") + description }
    let code: String?; let description: String; let date: String?
    let charged: Double?; let medicareRate: Double?; let markup: Double?
    let savings: Double; let severity: String; let strong: Bool
    let findingIds: [Int]; let reasons: [Reason]
}
struct Reason: Decodable, Hashable { let type: String?; let label: String; let message: String; let severity: String }
struct Price: Decodable { let reportProductId: String }
```

Put real JSON fixtures from the backend (A8 test outputs) in `BillKarmaTests/Fixtures/` and test decoding locked, unlocked and clean bills.

### B4. Screens and flow

```
Launch ─► (first run) Onboarding ─► ScanHome ◄──────────── BillsList (tab)
                                       │                       Settings (tab)
                                       ▼
                         DocumentScanner / PhotosPicker / PDF
                                       ▼
                                 ProcessingView
                                       ▼
                     ┌──── locked ──► TeaserView ─► PaywallSheet ─► ReportView
                     └── unlocked/clean ───────────────────────────► ReportView
                                                                     ├─► LetterForm ─► LetterPreview (Share PDF / Copy)
                                                                     └─► PhoneScript
```

Use a `TabView` with **Scan** and **My Bills**, and Settings behind a gear icon. Navigation uses a `NavigationStack` with a typed path.

**1. Onboarding** — fully specified in **B10** (screens O1–O14, copy, logic, variants). Build it from B10, not from this summary.

**2. ScanHome** — layout and copy in **B11 (S)**.
Headline "Scan a medical bill" and three options: **Scan with camera** (primary), **Choose photos**, **Import PDF**. Below that, a tip: "Itemized bills work best. Ask the billing office for one if yours only shows totals."

**3. DocumentScanner.swift**
Wrap `VNDocumentCameraViewController` in `UIViewControllerRepresentable`. It returns `[UIImage]`, one per page. Hide the camera option if `VNDocumentCameraViewController.isSupported == false` (simulator). PhotosPicker: up to 10 images. PDF: `.fileImporter(allowedContentTypes: [.pdf])`, sent as-is.

**4. ImagePrep.swift**
Downscale so the longest side is at most 2200 px, encode JPEG quality 0.75, and target under 4 MB per page. Process pages off the main thread. Unit test: a 4000×3000 image comes out at most 2200 px on the long side.

**5. ProcessingView**
Upload, then show rotating steps tied to elapsed time ("Reading your bill…" → "Matching billing codes…" → "Comparing with Medicare rates in {ZIP}…" → "Checking for duplicates…"). If the request passes 60 s, show "Still working, big bills take longer." Cancel button. On success → route by `locked`. Events: `scan_started`, `scan_succeeded` (props: pages, locked, charge_count) / `scan_failed` (error type).

**6. TeaserView (locked) — the screen that sells**
- Top: provider name and "You owe {totalPatientOwes}"
- Hero: "**We found up to {totalSavings} in possible errors**" (big, animated count-up) and "{chargeCount} charges flagged · {strongCount} strong"
- Reason chips from `reasonCounts` ("2 × Possible duplicate")
- A blurred list of placeholder charge rows (`.redacted(reason: .placeholder)` plus a blur). **Never** render real line items while locked.
- Primary CTA: **See every flagged charge and get your dispute letter** → PaywallSheet
- Disclaimer (small): "Estimates based on Medicare rates and common billing errors. Not legal or medical advice."
- Event `teaser_viewed`.

**7. Clean result (no flagged charges, unlocked automatically)**
"No obvious errors on this bill." Then next steps: request an itemized bill, check financial assistance, and links to the matching billkarma.app guides. **No paywall.**

**8. Paywall** — fully specified in **B10.5** (custom SwiftUI screen using RevenueCat `Offerings`). The purchase → unlock rules below still apply:
- Consumable: read the transaction ID from the purchase result's `StoreTransaction` (`transactionIdentifier`) → `POST /api/m/bills/{id}/unlock {"transaction_id": ...}`
- Plus: → `POST /api/m/bills/{id}/unlock {}`
- Swap in the returned unlocked `BillView` and push `ReportView`.
- If the unlock call fails after a successful purchase, keep the transaction ID in `UserDefaults` (`pendingUnlocks[billId]`) and retry on next launch and on pull-to-refresh. **A user who paid must always end up unlocked.**

**9. ReportView (unlocked)**
- Header: total savings and the strong count
- A `ChargeRow` per charge: description, code, date, **Charged vs Medicare** (e.g. "$3,100 vs $412 · 7.5x"), savings, severity colour, and an expandable reasons list (label + message)
- Sticky bottom bar: **Get dispute letter** (primary), **Phone script** (secondary)

**10. LetterFormView → LetterPreviewView** — layout and copy in **B11 (L1, L2)**; behaviour below.
Fields: your name, account number (both optional; they map to `requestor_name` and `account_number`), and toggles for which charges to include (default: all `strong`; sends `finding_ids`). `POST /bills/{id}/letter` → preview the text. Actions: **Share PDF** (`LetterPDF.swift` uses `UIGraphicsPDFRenderer` for US Letter, 1" margins, 11 pt system font; `ShareLink` with the file URL) and **Copy text**. Event `letter_shared`. Show the backend's `finding_count` and `total_disputed` above the letter.

**11. PhoneScriptView** — layout, copy and the backend `sections` change in **B11 (PS)**.
`GET /bills/{id}/phone-script` → scrollable text with a Copy button. Event `phone_script_viewed`.

**12. BillsListView** — layout, badges and empty state in **B11 (MB)**.
`GET /bills` → rows: provider, date, amount owed, and a "Locked" / "{savings} found" badge. Swipe to delete (`DELETE /bills/{id}`, confirm first). Pull to refresh (also retries `pendingUnlocks`).

**13. SettingsView** — layout and copy in **B11 (SET)**.
Restore purchases (`Purchases.shared.restorePurchases()`, then refresh the bills list), Delete my data (confirm → `DELETE /device` → clear Keychain and UserDefaults → back to onboarding), Privacy policy and Terms (billkarma.app URLs), Contact support (`mailto:support@billkarma.app`), app version.

### B5. App start sequence (`AppState`)
1. Read the token from the Keychain. If there isn't one → `POST /api/m/device` → save `device_id` and `token`.
2. `Purchases.configure(withAPIKey: Config.revenueCatKey, appUserID: deviceId)`, so RevenueCat and the backend share one ID.
3. Retry any `pendingUnlocks`.
4. Route: onboarding if `!hasOnboarded`, otherwise the tabs.
5. Deep links: `.onOpenURL` → `/app/scan` opens ScanHome. Unknown paths open the default view.

### B6. Analytics
`Analytics.track(_ name: String, _ props: [String: String] = [:])` sends fire-and-forget `POST /api/m/events` on a background task, and **never** blocks the UI or throws. Use the event names from `config.MOBILE_EVENT_NAMES` only. The funnel from these events (onboarding → scan → teaser → paywall → purchase), split by `attribution_source`, is the scorecard for the 45-day test.

### B7. Design system — "the marked-up bill"

**Reference mockups:** https://claude.ai/artifact/XwBuaGNhYmXDoE1bMZh6ET: 16 screens (Welcome, quiz step, provider search, Your plan, Processing, Teaser, clean result, Paywall, Report, letter form, letter preview, phone script, share card, scan home, My bills, Settings) plus the tokens board. If this section and the mockups disagree, **the mockups win**. Match spacing, sizes and hierarchy closely. Use real SwiftUI controls, not web lookalikes.

**Direction in one line:** a friend who's good with money went through your bill with a highlighter. Confident, plain-spoken, warm. Not a hospital portal (no clinical blues, no stock photos of doctors) and not a fintech dashboard (no gradients, no charts for the sake of it). It shares billkarma.app's palette and fonts, so web and app read as one brand.

**Signature moves** (use all of them; they're what make it not look generic):
1. **The highlighter.** Every dollar amount we *found* sits on a yellow `mark` block, slightly rotated (−1° to −2°), like a highlighter swipe. Used only for "what we found", never for decoration.
2. **Ink hero cards.** The moment of truth (Your plan provider insight, Teaser result, Share card) is a dark `ink` card with white text. Everything else is light.
3. **Mono for evidence.** Billing codes, charged amounts and Medicare rates use IBM Plex Mono, so they read like the bill itself.
4. **Charged vs Medicare bar.** A rust-tinted bar for the charged amount, with a solid ink segment for the Medicare share. It makes markup visible in one glance.

#### Tokens (`Design/Theme.swift`)

```swift
import SwiftUI

enum BK {
    enum Color {
        // Light / dark pairs. Put these in Assets.xcassets as color sets with Any + Dark appearances,
        // then reference them here, so Dark Mode is automatic.
        static let ink      = SwiftUI.Color("ink")       // #0E1726 / #F4F5F7  primary text, primary button (light)
        static let muted    = SwiftUI.Color("muted")     // #5B6676 / #9AA5B4  secondary text
        static let ground   = SwiftUI.Color("ground")    // #F4F5F7 / #0B111C  screen background
        static let paper    = SwiftUI.Color("paper")     // #FFFFFF / #151E2C  cards, sheets
        static let rule     = SwiftUI.Color("rule")      // #E3E6EB / #26303F  borders, dividers
        static let ruleStrong = SwiftUI.Color("ruleStrong") // #C5CCD6 / #3B4658  unselected radio, inactive progress
        static let mark     = SwiftUI.Color("mark")      // #FFE14D / #FFE14D  "what we found" highlight (text on it is always #0E1726)
        static let markSoft = SwiftUI.Color("markSoft")  // #FFF7CC / #3A3415  selected option fill, tip cards
        static let over     = SwiftUI.Color("over")      // #A32E10 / #FF8F73  overcharge text and labels
        static let overSoft = SwiftUI.Color("overSoft")  // #FBECE7 / #3A1E18  overcharge chip background
        static let overBar  = SwiftUI.Color("overBar")   // #F6D6D3 / #4A2620  charged-amount bar
        static let good     = SwiftUI.Color("good")      // #00824F / #3DBB84  logo, checks, clean result
        static let codeBg   = SwiftUI.Color("codeBg")    // #EEF0F3 / #26303F  billing-code chip, locked badge
        static let goodSoft = SwiftUI.Color("goodSoft")  // #E6F4EE / #16352A  "No issues" badge
        static let heroBg   = SwiftUI.Color("heroBg")    // #0E1726 / #151E2C  ink hero cards (both modes stay dark)
        static let heroText = SwiftUI.Color("heroText")  // #FFFFFF / #F4F5F7
        static let heroMuted = SwiftUI.Color("heroMuted") // #C5CCD6 / #9AA5B4
    }
    enum Radius { static let chip: CGFloat = 4, tile: CGFloat = 10, control: CGFloat = 14, card: CGFloat = 16, hero: CGFloat = 20 }
    enum Space  { static let xs: CGFloat = 4, s: CGFloat = 8, m: CGFloat = 12, l: CGFloat = 16, xl: CGFloat = 20, xxl: CGFloat = 24, xxxl: CGFloat = 32
                  static let screen: CGFloat = 20 }       // horizontal screen margin
    enum Size   { static let buttonHeight: CGFloat = 56, optionMinHeight: CGFloat = 64, touch: CGFloat = 44, iconTile: CGFloat = 38 }
}
```

Primary button in **dark mode**: `mark` background with `#0E1726` text (an ink button would vanish on a dark ground).

#### Typography (`Design/Typography.swift`)
Bundle the fonts (all SIL Open Font License; include the license files): **Inter Tight** 700/800, **Inter** 400/500/600/700, **IBM Plex Mono** 500/600. Register them in Info.plist (`UIAppFonts`). Always use `Font.custom(_:size:relativeTo:)` so Dynamic Type scales them.

| Style | Font | Size / line height | Weight | Tracking | relativeTo | Used for |
|---|---|---|---|---|---|---|
| `moneyHero` | Inter Tight | 64 / 66 | 800 | −2 | .largeTitle | Teaser hero amount |
| `moneyLarge` | Inter Tight | 40 / 44 | 800 | −1 | .largeTitle | Report header amount |
| `display` | Inter Tight | 36 / 40 | 800 | −0.8 | .largeTitle | Welcome headline |
| `title` | Inter Tight | 30 / 34 | 800 | −0.6 | .title | Question and screen titles |
| `headline` | Inter | 17 / 24 | 600 | 0 | .headline | Option labels, card titles, buttons |
| `body` | Inter | 15–17 / 21–25 | 400 | 0 | .body | Body copy |
| `label` | Inter | 12 / 16 | 600, uppercase | +0.5 | .caption | Section labels ("WHAT WE'LL CHECK") |
| `caption` | Inter | 12–13 / 17–19 | 400 | 0 | .caption | Disclaimers, meta |
| `mono` | IBM Plex Mono | 12–17 | 500/600 | 0 | .body | Codes, charged and Medicare amounts |

Money formatting: whole dollars in heroes ("$912"), cents in line items ("$3,100.00" on the bill, "$3,100" in comparisons). Use `.currency(code: "USD")` with `precision(.fractionLength(0))` for heroes.

#### Components (`Design/Components.swift`, one small view each)

| Component | Spec (see mockups) |
|---|---|
| `PrimaryButton` | Full width, height 56, radius 14, ink fill, white `headline` 17/600; pressed = 0.9 opacity + scale 0.98; loading = `ProgressView` replacing the label; disabled = 40% opacity |
| `SecondaryButton` | Same size, paper fill, 1 pt `ruleStrong` border, ink text |
| `TextLinkButton` | 44 pt tall, muted or ink 15/500, underline only when it's an explanation link |
| `ProgressSegments` | N equal segments, 5 pt tall, radius 3, gap 4; done = ink, todo = ruleStrong; animates the newly filled segment over 0.25 s |
| `OptionCard` | Min height 64, radius 14, paper fill + 1 pt rule border; leading 38 pt icon tile (radius 10, ground fill, 20 pt stroke icon); label `headline`. **Selected:** 2 pt ink border, markSoft fill, icon tile turns mark, trailing filled ink check circle. Selection haptic `.selection` |
| `HeroResultCard` | heroBg, radius 20, padding 22/20; muted lead-in ("We found up to") → `HighlightAmount` → white line → divider (#2B3648) → summary row |
| `HighlightAmount` | The amount in `moneyHero` ink text on a mark block, horizontal padding 10, radius 6, rotated −1°. Counts up from 0 over 1.2 s (ease-out), with a `.success` haptic when it lands. Reduce Motion: no count-up, no rotation |
| `ReasonChip` | Capsule, overSoft fill, over text 13/600, padding 6×11. Format "2 × Billed more than once" |
| `CodeChip` | Mono 12/600 on codeBg, radius 4, padding 2×6 |
| `LockedRow` | Two placeholder bars (ruleStrong 12 pt, rule 10 pt) + a short overSoft bar, all blurred 3 pt, trailing lock icon (muted). **No real data inside**, ever |
| `ChargeCard` | Paper card, radius 16. Row 1: CodeChip + strength label ("STRONG" over 12/700, or "WORTH ASKING" muted) · description `headline` · date caption · trailing "Up to" + mono amount. Row 2: `ChargedVsMedicareBar`. Row 3 (divider above): reason title 14/600 + message 14/20 secondary. Weaker charges render collapsed (one line + chevron) |
| `ChargedVsMedicareBar` | 12 pt bar, radius 6, overBar fill; inner ink segment width = medicare / charged (min 4%); below: "Medicare $412" left, "Charged $3,100" + markup pill (overSoft, "7.5×") right. Hide the bar if either amount is missing |
| `PlanCard` | Radius 16, padding 16; radio (22 pt) · title 16/700 + subtitle 13 muted · trailing price in Inter Tight 20/800. Selected = 2 pt ink border + filled radio. Optional badge: mark capsule, 11/700, overlapping the top edge at the right |
| `Timeline` | Ground card; 12 pt dots (filled ink for today, outlined for the future date) joined by a 2 pt ruleStrong line; date 13/700 over description 14 |
| `ChecklistRow` | 18 pt good-coloured check, 15/20 text |
| `StatusChecklist` (Processing) | Done = filled good circle + white check, muted text; active = spinner ring + ink 600 text; pending = outlined circle, #8E99A8 text; 46 pt rows with rule dividers |
| `TipCard` | markSoft fill, radius 14, lightbulb stroke icon, 14/20 text |
| `ShareCard` | 1080×1920 render (design at 360×640, render at 3×): heroBg, logo, label, rotated HighlightAmount 84 pt, headline, footer "Check yours free / billkarma.app" in mono mark |

**Icons:** SF Symbols where they match the mockups (`chevron.left`, `xmark`, `checkmark`, `lock`, `lightbulb`, `calendar`, `doc.viewfinder`). Use stroke-style symbols with `.fontWeight(.semibold)`. Never emoji.

#### Screen layout rules
- Background `ground` on every screen except the Paywall (`paper`) and the Share card (`heroBg`).
- Screen margin 20 pt (24 on Welcome and Processing). Content starts below the safe area. **No fake status bars.**
- One primary action per screen, pinned to the bottom above the home indicator. Secondary actions go below it as text buttons.
- Section labels use the `label` style. Cards stack with 12–14 pt gaps.
- The Report has a sticky bottom bar (paper, top rule): Primary "Get dispute letter" (flex) + Secondary "Phone script" (fixed 132 pt).

#### Motion and haptics
| Moment | Motion | Haptic |
|---|---|---|
| Option tap | Border and fill cross-fade 0.15 s, then auto-advance after 0.25 s with a push transition | `.selection` |
| Progress bar | New segment fills left-to-right 0.25 s | – |
| Building your check (O12) | Ring 0→100% over 4 s; checklist rows tick every 0.8 s with a spring scale-in of the check | light `.impact` per tick |
| Processing | Ring advances with elapsed time (never claims a real %); active row spinner; rows tick as stages pass | – |
| Teaser | Hero card fades up 12 pt (0.35 s), then `HighlightAmount` counts up 1.2 s; chips stagger in 0.05 s apart | `.success` when the count lands |
| Purchase → Report | Locked rows un-blur (blur 3 → 0 over 0.5 s) as the real charge cards slide in | `.success` |
| Share | Card scales from 0.96 to 1 on appear | – |

All motion respects **Reduce Motion** (swap to cross-fades, no count-up, no rotation) and nothing loops forever except the active spinner.

#### States and accessibility
- **Loading:** skeleton cards (rule-coloured bars, shimmer off with Reduce Motion) on My Bills and Report. Never a bare spinner on an empty screen.
- **Empty My Bills:** illustration of the highlighted bill (as on Welcome) + "No bills yet" + PrimaryButton "Scan a bill".
- **Errors:** inline card at the top of the content (overSoft fill, over icon, message from B9, action button). No alert popups except destructive confirmations.
- **Dynamic Type:** test at XXXL. Option cards grow taller; hero amounts may wrap the label below. Nothing truncates money.
- **VoiceOver:** the hero reads as one element: "We found up to 912 dollars in possible billing errors. 3 charges flagged, 2 strong." Locked rows read "Locked charge". Selected option cards announce "selected".
- **Contrast:** every text pair above passes 4.5:1 (muted on ground included). Overcharge meaning is never colour-only: there's always a label ("Strong", "7.5×", "Billed more than once").

#### App Store screenshots
Use the same look: ground background, one big headline in Inter Tight 800 on top ("Snap your bill" / "See what's wrong" / "Know the fair price" / "Get your letter" / "Follow up on time"), and the matching mockup screen in a device frame below. The highlighter block on the money in screenshot 2 matches the app.

### B8. Privacy and data handling
- Bill images go only to the BillKarma backend. Nothing is stored on the device except the bill IDs you get back.
- No third-party analytics or ad SDKs. No App Tracking Transparency prompt.
- The "Delete my data" path is fully server-side (A5 `DELETE /device`).
- Backend retention: the existing `compliance.purge_old_data` covers mobile bills too. Make sure the privacy policy states the retention window.

### B9. Error copy (APIError → UI)

| Error | Message | Action |
|---|---|---|
| offline | "You're offline. Check your connection and try again." | Retry |
| badRequest (400) | Show the server's message (e.g. unreadable image) and suggest "Try better light, flat paper, all four corners in frame." | Rescan |
| paymentRequired (402) | Open the paywall | – |
| conflict (409) | "This purchase was already used for another bill. Contact support and we'll sort it out." | Mail support |
| rateLimited (429) | "Too many scans in a short time. Try again in a bit." | – |
| unavailable (503) | "Bill reading is down for a moment. Try again in a few minutes." | Retry |
| server (5xx) | "Something went wrong on our side. Your bill wasn't charged." | Retry |

### B10. Onboarding, paywall and growth loops — full spec

This section replaces the short onboarding description in B4. It adapts what the fastest-growing consumer apps of 2024–2026 do in onboarding and paywalls. Every screen has an ID, purpose, layout, **exact copy**, logic, saved data and analytics event. Claude Code should build the copy word for word. Change it later through A/B tests, not by improvising.

#### B10.0 Patterns borrowed (and what we don't copy)

| App | What they do | How BillKarma uses it |
|---|---|---|
| **Quittr** | Onboarding works like a sales call: quiz → symptom checklist → education slides → a personal date → paywall. "Where did you hear about us?" sits inside the quiz. | O2 education slides, O7 "What's going on with this bill?" checklist, O13 personal follow-up date, O10 attribution |
| **Cal AI** | Long quiz, a "thank you for trusting us" privacy screen, an animated "building your plan" screen with %, a "your plan is ready" screen, then a hard paywall | O11 trust screen, O12 "Building your bill check" animation, O13 plan screen. Our paywall comes **after** the scan, because the free result is the hook |
| **Ladder** | A 15-question quiz whose answers predict lifetime value and feed the ad platform | O3–O8 answers are saved per device and later tell you which users pay (B10.10). Once paid ads start, the high-value answers become conversion signals |
| **Bible Chat** | Trust-first paywall that explains what happens and when, plus a reminder promise | Paywall timeline (B10.5) and the honest "what happens next" copy |
| **Blinkist / Cal AI paywalls** | A "Today → Day 2 → Day 3" timeline on the paywall | Our timeline: "Today: see every charge → Today: send your letter → {date}: we remind you to follow up" |
| **Umax** | A score that turns the result into shareable content; referral to skip the fee | B10.6 shareable **Bill Score** card (the backend already has `bill_score.py` with share tokens). Referral unlock is a later experiment |
| **Tolan** | A playful result card users want to post | Bill Score card designed to be screenshotted |
| **Opal** | Tuned the free tier until free users recommended the app | Clean bills are always free, and the teaser always shows the real dollar figure. The free experience has to be worth recommending |
| **Stronger** | A hard paywall lifted conversions about 25% | Never show paid details before payment. The teaser shows the number, not the charges |

**Deliberately not copied** (each would hurt trust, break App Review rules, or risk FTC dark-pattern enforcement):
- Fake scarcity ("60% off, 9 spots remaining") and fake countdown timers
- Invented statistics ("80% of bills have errors"). Every number in the app must come from the user's own bill or from BillKarma's CMS-based data, with an as-of date
- Placeholder or invented testimonials. The testimonial slot (O11) stays hidden until there are real, permissioned reviews
- Asking for an App Store rating before the user has seen any value (Cal AI does this mid-onboarding). We ask after a win (B10.6)
- Hiding the price, or making a monthly-equivalent price look bigger than the billed amount (Guideline 3.1.2: the billed amount must be the most prominent price)

#### B10.1 Principles
1. **One question per screen, one tap.** Single-choice options auto-advance 250 ms after the tap, with a light haptic (`.sensoryFeedback(.selection)`). Multi-select screens have a Continue button.
2. **Under 60 seconds** to the camera for a user who taps straight through.
3. **Every answer changes something** the user sees later (B10.4). If an answer doesn't, delete the question.
4. **Show progress.** A segmented bar at the top, with a back chevron on every screen except O1.
5. **The scan result is the paywall moment.** Onboarding never shows a price.
6. **Honest personalization.** Personalized copy uses the user's answers and real hospital data only.
7. **Permissions only in context.** Camera when the user taps "Open camera", notifications after they get value, never at launch.

#### B10.2 Flow and variants

```
Variant A "Full" (default, 50%)
O1 Welcome → O2 Education (3 slides) → O3 Bill type → O4 Provider → O5 Amount → O6 Insurance
→ O7 What's going on → O8 Due date → O9 ZIP → O10 Attribution → O11 Trust
→ O12 Building your check → O13 Your plan → O14 Scan tips → Camera

Variant B "Fast" (50%)
O1 Welcome → O4 Provider → O9 ZIP → O10 Attribution → O12 → O13 → O14 → Camera
```

- Assign the variant on first launch at random, store it in `UserDefaults`, and send it with every onboarding event and in `POST /profile`.
- **Skip** (top right, from O2 onward) jumps to O9 ZIP, because the scan needs a ZIP, then to O14.
- Returning users (`hasOnboarded == true`) never see onboarding again. Settings → "Redo setup" resets it (useful for testing).

#### B10.3 Screen-by-screen spec

Layout conventions for every question screen: progress bar → headline (title2, bold, max 2 lines) → subhead (body, secondary colour, optional) → options as full-width rounded cards (min height 56 pt, SF Symbol on the left, label, checkmark when selected) → bottom-pinned primary button when needed. Background: system background. Accent: brand colour.

---

**O1 — Welcome**
- Purpose: state the promise and the price of entry (free, no account).
- Layout: a looping 3-second illustration of a bill with three lines highlighting one after another, built with plain SwiftUI animation over static assets (no Lottie: no extra dependencies), then the headline, subhead and button.
- Copy:
  - Headline: **"Is your medical bill right?"**
  - Subhead: "BillKarma checks every charge against Medicare rates and common billing mistakes. Free to check. No account needed."
  - Button: **"Check my bill"**
  - Footer (caption): "By continuing you agree to our Terms and Privacy Policy." (both linked)
- Event: `onboarding_step_viewed {step: "O1", variant}`

---

**O2 — Education (3 swipeable slides, Quittr-style)**
- Purpose: give the user the words for their problem before asking about it. Each slide is one big statement plus one supporting line. Page dots, with **Next** and on the last slide **Continue**.
- Slide 1:
  - Big: **"Medical bills are written in codes."**
  - Line: "Each line on an itemized bill has a billing code, like 99285 for an ER visit. The code decides the price."
- Slide 2:
  - Big: **"Mistakes happen."**
  - Line: "Charges can be billed twice, coded at a higher level than the care you got, or priced far above what Medicare pays for the same thing."
- Slide 3:
  - Big: **"You're allowed to question your bill."**
  - Line: "You can ask for an itemized bill, dispute charges in writing, and ask about financial assistance. BillKarma shows you exactly what to say."
- Event: `onboarding_step_viewed {step: "O2", slide}`

---

**O3 — Bill type** (single choice)
- Headline: **"What kind of bill is it?"**
- Options (value → label, SF Symbol):
  - `er` → "Emergency room visit" (`cross.case`)
  - `hospital_stay` → "Hospital stay" (`bed.double`)
  - `surgery` → "Surgery or procedure" (`scissors`)
  - `lab_imaging` → "Lab work, X-ray, MRI or CT" (`waveform.path.ecg`)
  - `doctor` → "Doctor or urgent care visit" (`stethoscope`)
  - `other` → "Something else" (`doc.text`)
- Saves `bill_type`.

---

**O4 — Provider** (search, Cal AI-style "input" screen)
- Headline: **"Who sent the bill?"**
- Subhead: "We'll compare your charges with what this provider usually bills."
- Search field (placeholder "Hospital or clinic name"), debounced 300 ms, calls `GET /api/m/hospitals/search?q=` (B10.9). Results show name, city and state.
- Below the field: secondary buttons **"It's a doctor's office or lab"** and **"Skip"**.
- Saves `hospital_facility_id` (or null).
- When a hospital is picked, prefetch `GET /api/m/hospital-insight?facility_id=` for O13.

---

**O5 — Amount** (single choice)
- Headline: **"About how much do you owe?"**
- Subhead: "Your share, after any insurance."
- Options: `under_500` "Under $500" · `500_2k` "$500 – $2,000" · `2k_10k` "$2,000 – $10,000" · `over_10k` "More than $10,000" · `unsure` "I'm not sure"
- Saves `amount_band`.

---

**O6 — Insurance** (single choice)
- Headline: **"Did insurance cover any of it?"**
- Options: `insured` "Yes, I have insurance" · `uninsured` "No, I'm paying myself" · `unsure` "I'm not sure"
- Saves `insurance_status`.

---

**O7 — What's going on** (multi-select, Quittr's "symptoms" screen)
- Headline: **"What's going on with this bill?"**
- Subhead: "Pick all that apply."
- Options:
  - `unexpected` "I didn't expect this bill"
  - `too_high` "The amount seems too high"
  - `confusing` "I don't understand the charges"
  - `out_of_network` "I was billed as out of network"
  - `collections` "It's been sent to collections"
  - `denied` "Insurance denied the claim"
  - `cant_afford` "I can't afford to pay it"
- Button: **"Continue"** (enabled after at least one pick)
- Saves `situations` (array).

---

**O8 — Due date** (single choice)
- Headline: **"When is it due?"**
- Options: `this_week` "This week" · `this_month` "This month" · `past_due` "It's already past due" · `unsure` "Not sure"
- Saves `due_band`. Drives the urgency line on O13 and the reminder date.

---

**O9 — ZIP code**
- Headline: **"What's your ZIP code?"**
- Subhead: "Medicare pays different rates in different areas. We use your ZIP to compare with the right ones."
- Single text field, number pad, 5 digits, auto-focused. **Continue** is enabled at 5 digits. Validate locally with `^\d{5}$`.
- Saves `zip_code`.

---

**O10 — Attribution** (single choice)
- Headline: **"Last one: how did you hear about BillKarma?"**
- Options: `tiktok` "TikTok" · `instagram` "Instagram" · `youtube` "YouTube" · `reddit` "Reddit" · `google` "Google search" · `article` "A BillKarma article" · `friend` "Friend or family" · `other` "Something else"
- Saves `attribution_source`. **This screen is required** in both variants. It's the only way to measure creator ROI without tracking SDKs.

---

**O11 — Trust (Cal AI's "thank you for trusting us")**
- Layout: a lock illustration, headline, three rows with icons, then a button.
- Headline: **"Your bill stays private."**
- Rows:
  - `lock.shield` "Your bill is only used to check your charges."
  - `person.crop.circle.badge.xmark` "No account, no ads, no selling your data."
  - `trash` "Delete everything anytime in Settings."
- Testimonial slot: **hidden in v1.** Show it only when `Config.realTestimonials` is non-empty (real, permissioned quotes with first name + city).
- Button: **"Continue"**

---

**O12 — Building your bill check** (Cal AI's "generating your plan")
- Purpose: a short moment where the app visibly uses the answers. It must finish in **4 seconds** and never fake a wait the user can't skip after it's done.
- Layout: a large circular progress ring counting 0 → 100%, and below it a checklist where each line ticks in turn (about 0.8 s apart):
  1. "Looking up Medicare rates for {ZIP}"
  2. "Loading {provider name}'s pricing data" (or "Loading pricing data for your area" if no provider)
  3. "Adding checks for {bill type label}"
  4. "Setting up your dispute templates"
- The prefetched hospital insight loads during this screen.
- Auto-advances to O13.

---

**O13 — Your plan** (the personal "diagnosis" + Quittr's date)
- Headline: **"Your bill check is ready."**
- Card 1, provider insight (only when the insight endpoint returned data):
  - "**{Hospital}**'s list prices average **{avg_markup:.1f}x** what Medicare pays, across {procedures_compared} procedures we compared."
  - Caption: "Billing grade {billing_grade} · CMS data as of {as_of}"
  - With no insight, show instead: "We'll compare each charge with Medicare rates for {ZIP}."
- Card 2, "What we'll check" — 3–4 rows chosen by `bill_type` (B10.4), each with a check icon. **Only list checks the analyzer actually runs** (the `REASON_LABELS` in `charge_summary.py`).
- Card 3, situation lines (B10.4). One line per selected situation, max 2.
- Card 4, the date:
  - "**Follow-up date: {date}**"
  - "We'll remind you to check whether {provider or 'the billing office'} replied."
  - `{date}` = today + 14 days, or today + 7 days when `due_band == "past_due"`. Format: "Tuesday, December 2". Save it in `UserDefaults` so the paywall and reminder use the same date.
- Footer line (always): "**If we find nothing wrong, you pay nothing.**"
- Button: **"Scan my bill"**

---

**O14 — Scan tips**
- Headline: **"Get the best result"**
- Three rows with small illustrations:
  - "Use the **itemized** bill — the one with codes like 99285 next to each charge."
  - "Lay it flat in good light with all four corners showing."
  - "Got several pages? Scan them all in one go."
- Primary: **"Open camera"** (VisionKit triggers the camera permission prompt the first time)
- Secondary: **"Choose photos"** · **"Import a PDF"**
- Tertiary link: "Only have a summary bill? **Get the itemized one first**" → a sheet with the itemized-bill request explanation and a link to the billkarma.app guide.
- If camera permission is denied: an inline banner "Camera is off for BillKarma. **Open Settings**" (`UIApplication.openSettingsURLString`), with photos and PDF still available.
- On finishing O14 (any path): `POST /api/m/profile` with every answer, set `hasOnboarded = true`, event `onboarding_completed {variant, bill_type, amount_band, insurance_status, situations, due_band, attribution_source, provider_selected}`.

---

**P — Processing screen** (replaces the B4 description)
- Ring animation plus a checklist that ticks on elapsed time: "Reading your bill" (0 s) → "Finding billing codes" (6 s) → "Comparing with Medicare rates in {ZIP}" (14 s) → "Checking for duplicates and coding problems" (22 s) → "Adding up what you may be owed" (30 s). The last item stays spinning until the response arrives.
- At 60 s: "Big bills take a little longer. Hang tight."
- Rotating tip under the ring every 6 s (real, helpful, no stats): "You can ask any hospital for an itemized bill." · "Disputes in writing create a paper trail." · "Nonprofit hospitals must have financial assistance policies." · "Ask whether a charge was billed under the right code."

---

**T — Teaser** (locked result; replaces B4 screen 6)
- Top: provider name · "You owe **{totalPatientOwes}**"
- Hero (count-up animation, 1.2 s, success haptic at the end):
  - "**We found up to {totalSavings}**"
  - "in possible billing errors"
- Row: "{chargeCount} charges flagged · {strongCount} strong"
- Reason chips from `reasonCounts`: "2 × Billed more than once"
- Blurred placeholder rows (3–5), each with a small lock.
- Primary CTA: **"Show me every flagged charge"** → paywall
- Secondary: "What does 'strong' mean?" → sheet: "Strong flags have clear evidence on your bill, like an exact duplicate or a price many times the Medicare rate. Weaker flags are worth asking about."
- Caption: "Estimates use CMS Medicare rates and common billing rules. Not legal or medical advice."

**C — Clean result** (no flagged charges): headline "**Good news: nothing obvious looks wrong.**" Sub: "We checked {n} charges against Medicare rates and common billing errors." Then next steps tailored by O6/O7: uninsured or `cant_afford` → "Ask about financial assistance"; summary-only bill → "Get the itemized bill"; `collections` → "Know your rights with collectors" (guide link). Free, no paywall.

#### B10.4 Personalization rules

**"What we'll check" by bill type** (pick rows from these labels only):

| bill_type | Rows shown on O13 |
|---|---|
| er | "ER visit level (codes 99281–99285) matches your care" · "Charges billed more than once" · "Prices far above what Medicare pays" · "No Surprises Act protections for out-of-network ER care" |
| hospital_stay | "Charges billed more than once" · "Quantities that look wrong (days, doses, supplies)" · "Prices far above what Medicare pays" · "Items billed separately that should be bundled" |
| surgery | "Items billed separately that should be bundled" · "Quantities that look wrong" · "Prices far above what Medicare pays" · "Surprise out-of-network bills (No Surprises Act)" |
| lab_imaging | "Tests billed more than once" · "Prices far above what Medicare pays" · "Charges above the typical price in your region" |
| doctor | "Visit level matches your care" · "Charges billed more than once" · "Prices far above what Medicare pays" |
| other | "Charges billed more than once" · "Prices far above what Medicare pays" · "Charges above the typical price in your region" |

**Situation lines** (O13 card 3, max 2, in this priority order):

| Situation | Line |
|---|---|
| collections | "Already in collections? You still have rights. We'll show you how to ask the collector to prove the debt." |
| cant_afford | "Can't afford it? Many hospitals offer financial assistance. We'll point you to how to apply." |
| out_of_network | "Billed out of network? The No Surprises Act may protect you. We'll check." |
| denied | "Claim denied? Your report includes what to ask your insurer." |
| uninsured (O6) | "Paying yourself? Ask for the self-pay or cash price. It's often lower than the list price." |
| too_high / confusing / unexpected | "We'll explain every flagged charge in plain English." |

**Due date:** `past_due` → follow-up date today + 7 and an extra line "Past due bills: send your dispute in writing as soon as you can." Everything else → today + 14.

**Amount:** `2k_10k` or `over_10k` → add "Bigger bills have more lines to check, so scan every page."

#### B10.5 Paywall spec

Build a **custom SwiftUI paywall** (`PaywallScreen.swift`) using RevenueCat `Offerings` for products and prices. A custom screen is needed because it personalizes with the bill's numbers, which RevenueCat's template paywalls can't do. Present it full screen. The close (X) button appears after 1.5 s, top left, low contrast but clearly visible.

**Layout and copy, top to bottom:**
1. Personalized header:
   - "**Up to {totalSavings} in possible errors**"
   - "on your {providerName} bill · {chargeCount} charges flagged"
2. "**Unlock your full bill check**" with checklist rows (checkmark icons):
   - "Every flagged charge, with the Medicare rate for your area"
   - "A dispute letter written for your bill, ready to send"
   - "A word-for-word phone script for the billing office"
   - "A reminder to follow up on {follow-up date}"
3. Timeline (vertical, three dots joined by a line, Blinkist / Cal AI style):
   - **Today** — "See every flagged charge and why"
   - **Today** — "Send your letter or call with the script"
   - **{date}** — "We remind you to follow up"
4. Plan cards (radio style; tap selects):
   - **This bill** — "$19.99" · "One-time payment. No subscription." — **selected by default** (variant B10.7 E3 tests Plus preselected)
   - **BillKarma Plus** — "$59.99 / year" (largest text on the card) · "Every bill for your household for a year" · small caption "That's $5 a month, billed yearly" · badge "Best for families"
   - Prices always come from `StoreProduct.localizedPriceString`, never hard-coded.
5. CTA button (full width, large):
   - "This bill" selected → "**Unlock for {price}**"
   - Plus selected → "**Start Plus for {price}/year**"
6. Under the button (caption):
   - "This bill" → "One-time purchase for this bill only."
   - Plus → "Renews yearly. Cancel anytime in Settings → Apple ID → Subscriptions."
7. Footer links: **Restore purchases** · **Terms** · **Privacy**

**Behaviour:**
- Purchase flow, unlock call and pending-unlock retry exactly as in B4 screen 8.
- Loading state on the CTA while purchasing. Disable double taps.
- User cancels the Apple sheet → stay on the paywall, no error.
- Events: `paywall_viewed {bill_id, total_savings_band, variant}`, `paywall_plan_selected {plan}`, `purchase_completed {plan}`, `paywall_closed {seconds_on_screen}`.

**Exit offer (experiment E4, off by default):** on the first close per bill, show a bottom sheet:
- "**Not ready for $19.99?**"
- "Get this bill's full check for **{offer price}**. One time, for this bill."
- Buttons: "Unlock for {offer price}" / "No thanks"
- Needs a second consumable product `bk_report_unlock_offer` (e.g. $14.99) in a separate RevenueCat offering `exit_offer`. The backend accepts either product ID in A6.

#### B10.6 After the purchase: retention and growth loops

**Follow-up reminder (notification permission in context).** After the user shares their letter or views the phone script for the first time, show a soft prompt sheet:
- "**Want a reminder to follow up?**"
- "We'll nudge you on {date} to check whether {provider} replied. Billing offices often need a second ask."
- Buttons: "Remind me" (→ system permission prompt → schedule a local `UNUserNotificationCenter` notification) / "Not now"
- Notification text: title "Did {provider} reply?", body "Open BillKarma to see your next step for your {amount} bill."
- Local notifications only, no push server in v1. Events: `notification_prompt_shown`, `notification_prompt_accepted`.

**App Store review prompt.** Call SwiftUI `requestReview` only when **all** are true: the user just shared a letter **or** saw a report with `totalSavings >= 100`; they haven't been asked in the last 120 days; it's not their first app session. Apple also caps the prompt at 3 times a year. Event `review_prompt_requested`.

**Shareable Bill Score card (Umax / Tolan loop).** On ReportView, a "Share my result" button renders a 1080×1920 image with:
- BillKarma logo, "My bill check"
- "**{totalSavings} in possible errors found**"
- "{chargeCount} charges flagged at {providerName}" (the provider name toggle defaults **off** for privacy)
- "Check yours free: billkarma.app"
- **Never** include the user's name, account number, codes, dates or line items.
- Share via `ShareLink` with the rendered image (`ImageRenderer`). Event `result_shared`.

**Comeback path.** The My Bills tab shows "Got another bill? Scan it" at the top. Plus users see "Plus · unlimited checks" in the header.

#### B10.7 Experiments backlog (run one at a time on enough traffic)

| ID | Test | Primary metric | Decide when |
|---|---|---|---|
| E1 | Onboarding A (full) vs B (fast) | onboarding → `scan_succeeded` rate; then purchase rate | ~500 completed onboardings per arm |
| E2 | Teaser CTA: "Show me every flagged charge" vs "Get my dispute letter" | teaser → purchase rate | ~300 teasers per arm |
| E3 | Default plan: This bill vs Plus | revenue per paywall view | ~300 paywall views per arm |
| E4 | Exit offer on vs off | revenue per paywall view (not just conversion) | ~300 per arm |
| E5 | Price of single unlock $14.99 / $19.99 / $24.99 | revenue per teaser view | after E2/E3 settle |
| E6 | Referral: "Share BillKarma with 3 friends to unlock this bill" (check App Review 3.1.1 and 3.2.2 before building) | new installs per sharer, revenue impact | phase 2 |

Use the variant field in `UserDefaults` and send it in events. Read results from `mobile_events` with SQL (B10.10). No experiment SDK needed.

#### B10.8 Analytics: event list (replace `MOBILE_EVENT_NAMES` in A2)

```python
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
    "eob_prompt_shown", "eob_added", "insurance_check", "send_screen_viewed", "letter_sent", "call_started", "call_notes_saved",
}
```

Every event includes `variant` and `app_version`. The backend also joins the event to `mobile_devices` for `attribution_source`.

#### B10.9 Backend additions for this section (add to A1/A5 in Phase 2)

1. `mobile_devices` new columns: `bill_type TEXT, amount_band TEXT, insurance_status TEXT, situations_json TEXT, due_band TEXT, hospital_facility_id TEXT, onboarding_variant TEXT`.
2. `POST /api/m/profile` accepts all O3–O10 answers plus `onboarding_variant`. Validate each against fixed allowed values in `config.py` (`MOBILE_BILL_TYPES`, `MOBILE_AMOUNT_BANDS`, and so on). Unknown values → 400.
3. `GET /api/m/hospitals/search?q=` (auth required, rate-limited): like `hospital_seo.find_hospitals`, but **also returns `facility_id`** (the existing function doesn't select it). Return `[{facility_id, name, city, state}]`, max 10, query at least 2 characters.
4. `GET /api/m/hospital-insight?facility_id=`: from `hospitals` JOIN `billing_metrics`, return `{name, city, state, avg_markup, billing_grade, procedures_compared, as_of}` **only when** `avg_markup_vs_medicare > 0` and `procedures_compared >= config.RANKING_MIN_PROCEDURES` (same rule as `hospital_rankings.py`). Otherwise `data: null`. **Never** fall back to a made-up national average (`savings_estimator._get_markup` defaults to 3.4, so don't reuse that).
5. Tests: profile validation (bad value → 400), search returns `facility_id`, insight returns null below the procedure threshold.

#### B10.10 Funnel queries (SQLite, run weekly)

```sql
-- Funnel by attribution source, last 30 days
WITH d AS (
  SELECT device_id, attribution_source, onboarding_variant FROM mobile_devices
  WHERE created_at >= datetime('now', '-30 days')
)
SELECT d.attribution_source, d.onboarding_variant,
  COUNT(DISTINCT d.device_id) AS installs,
  COUNT(DISTINCT CASE WHEN e.name = 'onboarding_completed' THEN e.device_id END) AS onboarded,
  COUNT(DISTINCT CASE WHEN e.name = 'scan_succeeded' THEN e.device_id END) AS scanned,
  COUNT(DISTINCT CASE WHEN e.name = 'paywall_viewed' THEN e.device_id END) AS saw_paywall,
  COUNT(DISTINCT CASE WHEN e.name = 'purchase_completed' THEN e.device_id END) AS paid
FROM d LEFT JOIN mobile_events e ON e.device_id = d.device_id
GROUP BY 1, 2 ORDER BY installs DESC;

-- Which onboarding answers predict paying (Ladder-style)
SELECT bill_type, amount_band, insurance_status,
  COUNT(*) AS devices,
  SUM(EXISTS(SELECT 1 FROM mobile_events e WHERE e.device_id = m.device_id AND e.name = 'purchase_completed')) AS paid
FROM mobile_devices m GROUP BY 1, 2, 3 HAVING devices >= 20 ORDER BY paid * 1.0 / devices DESC;
```

The second query tells you who to target. If, say, uninsured ER bills over $2k pay at 3x the average, that's the brief for your creators and, later, your ad conversion signal.

### B11. Remaining screens — exact copy and layout

Mockups for every screen here are in the same canvas, in the "Scan, letter, bills, settings" rows. Build from the mockup and this copy. Everything uses the B7 components.

**S — Scan home** (tab "Scan"; replaces B4 screen 2)
- Header: logo + "BillKarma" wordmark (left), gear → Settings (right).
- Title "**Scan a medical bill**" · sub "We'll read every charge and check it against Medicare rates for {ZIP}."
- Hero action (heroBg card, radius 20): mark-coloured 52 pt icon tile, "**Scan with camera**", "Best for paper bills. Scan every page in one go." Hidden when `VNDocumentCameraViewController.isSupported == false`.
- Paper list card, two rows with chevrons: "**Choose photos**" / "Photos or screenshots from your library" · "**Import a PDF**" / "From email, Files or a patient portal".
- Tip card (markSoft): "Itemized bills work best. If yours only shows totals, ask the billing office for one. **How to ask**" → itemized-bill sheet (B11 sheet below).
- Tab bar: **Scan** · **My bills** (84 pt tall, paper, top rule; active = ink + 700, inactive = #8E99A8).

**O4 — Provider search** (replaces the O4 layout in B10.3; copy unchanged)
- Search field: 54 pt, 2 pt ink border while focused, magnifier icon, label above "Hospital or clinic name".
- Results card: label "{n} matches", rows with a building icon tile, name 16/600, "City, ST" 13 muted. The tapped row shows markSoft for 0.25 s, then auto-advances.
- No results: "No matches for "{query}". Try a shorter name, or skip." (inside the results card).
- Bottom: Secondary "**It's a doctor's office or lab**" · text button "**I'm not sure, skip**".

**C — Clean result** (no flagged charges; free)
- Header: provider + "You owe {amount}", close (X).
- Good-green 64 pt check circle → title "**Good news: nothing obvious looks wrong.**" → "We checked {n} charges against Medicare rates and common billing errors."
- "YOU CAN STILL" card, 1–3 rows from these rules (each row opens the matching billkarma.app guide in an in-app Safari view):
  - uninsured or `cant_afford` → "**Ask for the self-pay price**" / "Paying yourself? Ask for the cash price. It's often lower than the list price." and "**Check for financial assistance**" / "Many hospitals reduce bills based on income. See how to apply."
  - summary-only bill (extraction found no line-item codes) → "**Get the itemized bill**" / "Your bill only shows totals. An itemized bill lets us check every charge."
  - `collections` → "**Know your rights with collectors**" / "You can ask a collector to prove the debt before you pay."
  - none of the above → "**Keep this for your records**" / "Save a copy in case anything changes later."
- Bottom: caption "Clean results are always free." · Primary "**Scan another bill**" · text button "**Done**" (→ My bills).

**L1 — Letter form** (replaces B4 screen 10's form)
- Header: back + provider name. Title "**Your dispute letter**". Sub "Disputing {k} charges · {amount}" (amount on a mark block; updates live as toggles change).
- Field "Your name, as it appears on the bill" (hint "Leave blank to fill it in by hand later.") → `requestor_name`.
- Field "Account number" (hint "Printed near the top of your bill.") → `account_number`. Pre-fill if the extraction found one.
- "CHARGES TO INCLUDE" card: one row per charge (CodeChip, strength label, "{description} · {savings}", trailing switch). Default on = `strong` charges. At least one must stay on; otherwise disable the button and show "Pick at least one charge."
- Primary "**Create my letter**" → `POST /bills/{id}/letter`. Caption "Your name and account number are only used to fill in the letter."

**L2 — Letter preview** (replaces B4 screen 10's preview)
- Header: back · "Letter ready".
- Paper sheet (radius 12, shadow-paper) showing the letter text from the backend, 13/19. Tap opens a full-screen scrollable reader. In the inline preview, the bottom fades out.
- Actions row: Primary "**Share as PDF**" (share icon) · Secondary "**Copy text**" (120 pt). Copy shows a 1.5 s toast "Copied".
- "HOW TO SEND IT" card: "Email it to the billing office, or mail it with tracking." · "Keep a copy and note the date you sent it."
- Reminder card (heroBg): "**Want a reminder to follow up?**" / "We'll nudge you on {follow-up date}." · mark button "**Remind me**". This *is* the B10.6 soft prompt. After it's accepted, the card becomes "Reminder set for {date}" with a check, and the review-prompt rule (B10.6) runs.

**PS — Phone script** (replaces B4 screen 11)
- Header: back · "Phone script" · text button "Copy" (copies the whole script).
- "BEFORE YOU CALL" card (markSoft): "Your bill and account number {acct}" · "Something to write down the rep's name and a reference number".
- Numbered steps, each a step badge + title + a speech-bubble card (radius 4/16/16/16) with the words to say. Render one step per section the backend returns (below).
- Bottom: Primary "**I've made the call**" (logs event `call_logged`, then shows the reminder card from L2 if none is set) · caption "Not legal advice. Stay polite, and get everything in writing."
- **Backend change (Phase 2):** `build_phone_script` returns one text block with UPPERCASE headings, each followed by a line of `─`. Add `sections: [{"title", "body"}]` to `GET /api/m/bills/{id}/phone-script` by splitting on those headings in a small helper `split_script_sections(text)`, with a test. Keep `script` too. Map titles to steps: OPENING → "Open the call", FOR EACH DISPUTED CHARGE → "Name the charge", IF THEY RESIST… → "If they say no", IF THEY SAY THEY'LL CALL BACK → "If they'll call back", TAKE NOTES → shown as the last tip line, BEFORE YOU CALL → the top card.

**MB — My bills** (tab; replaces B4 screen 12)
- Title "**My bills**" + gear.
- Banner (heroBg): "Got another bill?" · mark button "**Scan it**".
- List card, rows: provider 16/600 · "{date} · You owe {amount}" · trailing badge, then chevron. Badges:
  - unlocked with findings → mark block "{savings} found" (rotated −1°)
  - locked → lock + "Up to {savings}" on codeBg capsule
  - clean → "No issues" on goodSoft capsule (`#E6F4EE` / dark `#16352A`, text good)
- Caption "Swipe left on a bill to delete it." Swipe → destructive "Delete" → confirm dialog "Delete this bill? This removes the bill and its report from BillKarma." [Delete] [Cancel].
- **Empty state:** the highlighted-bill illustration from Welcome, "**No bills yet**", "Scan a bill and it'll show up here, with what we found.", Primary "**Scan a bill**".

**SET — Settings** (replaces B4 screen 13)
- Back + title "**Settings**".
- PURCHASES: "BillKarma Plus" → value "Active until {date}" or "Not active" (tap → paywall with Plus preselected when not active, or the App Store subscriptions page when active) · "Restore purchases" (spinner, then toast "Purchases restored" or "Nothing to restore").
- YOUR DATA: "Privacy policy" · "Terms of use" · "**Delete my data**" in over colour with sub "Removes every bill and report from our servers and this phone." → confirm dialog "Delete all your data? This can't be undone. Purchases stay with your Apple ID." [Delete everything] [Cancel].
- HELP: "Contact support" (value support@billkarma.app, opens Mail) · "Redo setup" (resets onboarding).
- Footer: "BillKarma {version} ({build})" · "Estimates only. Not legal or medical advice."

**Sheets (no separate mockups; use the B7 sheet style: paper, radius 20 top corners, grabber, 20 pt padding)**
- **Itemized bill:** title "Ask for your itemized bill" · body "Call or email the billing office and say: 'Please send me an itemized bill with the CPT or HCPCS code for every charge.' You're entitled to see what you're being charged for." · buttons "Copy that request" / "Read the full guide" (billkarma.app guide).
- **"What does strong mean?":** copy as in B10.3 (Teaser).
- **Exit offer:** copy as in B10.5.
- **Camera off banner** (inline on Scan home and O14): overSoft card, "Camera is off for BillKarma." + "**Open Settings**".

### B12. Conversion upgrades and accounts

These changes are on top of B10/B11. Each one is honest by design: it raises willingness to pay by making the value more **believable** and the price more **fair**, not by adding pressure.

> **v1 scope:** build only **B12.1** (free strongest charge) and **B12.8** (iCloud Keychain + optional Sign in with Apple). Everything else in B12 is the **post-launch roadmap**: don't build it in v1. Test each item after launch, one at a time, using real funnel data (B10.10).

| # | Upgrade | Why it lifts paying | When |
|---|---|---|---|
| 1 | Show the strongest charge free | Proof beats promises: the user sees one real error before paying | **v1** (Phases 2 + 5) |
| 2 | Priced by what we found | A $9.99 report on a $60 problem feels fair; $19.99 doesn't | Post-launch |
| 3 | Scan-first onboarding (variant C) | Answers the quiz during the 20–60 s scan wait, so time-to-wow drops | Post-launch |
| 4 | Paywall shows their actual letter | People pay for a concrete thing with their name on it, not a feature list | Post-launch |
| 5 | "How many bills this year?" → Plus | Offer Plus to the people it actually fits, and preselect it for them | Post-launch |
| 6 | Outcome loop | Turns results into real social proof, reviews and repeat use | Post-launch |
| 7 | Real social proof (when it exists) | Credible numbers from your own data, never invented | Post-launch (needs 50+ real outcomes) |
| 8 | Accounts: iCloud Keychain + optional Sign in with Apple | Paid reports never get lost; email for the report and follow-ups | **v1**: iCloud Keychain in Phase 4, Sign in with Apple in Phase 6 |

#### B12.1 Show the strongest charge free — **v1**

> This changes the Teaser mockup: insert the free charge card above the locked rows and use the CTA below. Everything else on the Teaser stays as mocked up.

- **Backend (`build_bill_view`):** a locked view may include **exactly one** `free_charge`: the highest-savings `strong` charge from `group_findings_by_charge`, as a full `Charge` object. Rules:
  - `charge_count >= 2` → include the full charge (code, description, charged vs Medicare, markup, first reason and message, savings).
  - `charge_count == 1` → include only `code`, `description` and the reason `label`. No Medicare comparison or message, so the paid report still has something to unlock.
  - Letter, phone script and every other charge stay locked.
- Update the A8 security test: locked views contain at most one charge, never `finding_ids`, and the letter/script endpoints still return 402.
- **Teaser (T):** the free charge appears as a normal `ChargeCard` with a small "FREE PREVIEW" label above it, then the locked rows below as "{n − 1} more flagged charges". The CTA becomes "**Show me the other {n − 1}**" (or "Get my dispute letter" when n = 1).

#### B12.2 Priced by what we found — post-launch

Your web dispute fees already scale with the bill (`DISPUTE_FEE_TIERS`). Do the same for the app's report unlock:

| Total savings found | Product | Suggested price |
|---|---|---|
| under $100 | `bk_report_small` | $9.99 |
| $100 – $999 | `bk_report_unlock` | $19.99 |
| $1,000 and up | `bk_report_large` | $29.99 |

- Thresholds go in `config.py` (`MOBILE_REPORT_TIERS`). `build_bill_view` sets `price.report_product_id` from the bill's `total_savings`, and the app shows whichever product it's given.
- `/unlock` accepts a transaction only when its product is the bill's product **or a pricier one** (so a stale paywall can't sell the $9.99 unlock for a $3,000 bill). Record the price actually paid for that product in `report_unlocks.amount_cents` (map product ID → cents in `config.py`).
- Paywall copy under the price: "**Priced by what we found.** Smaller problems cost less to fix." Plus stays $59.99/year.
- All three products are consumables in offering `default`. Add them in App Store Connect and RevenueCat (section 6).

#### B12.3 Scan-first onboarding (variant C, third arm of E1) — post-launch

```
O1 Welcome → O9 ZIP → O14 Scan tips → camera → Processing-with-questions → Teaser (personalized)
```

- During Processing, the checklist shrinks to a one-line status bar at the top ("Comparing with Medicare rates…" with the ring as a small 32 pt icon), and the quiz screens play **inside** it as cards: O3 bill type, O4 provider (prefilled from the scan if the extraction found a provider name), O6 insurance, O7 situation, B12.5's "bills this year", and O10 attribution. Same copy and components as B10.
- If the result arrives mid-quiz, a banner slides down: "**Your result is ready**" with a "See it now" button. The remaining questions are skipped and can be answered later from Settings → Redo setup.
- The situation lines and follow-up date from O13 appear on the Teaser, under the hero, instead of on a separate plan screen.
- Success metric for E1 now compares three arms: A full, B fast, C scan-first. Primary metric is install → purchase, not just onboarding completion.

#### B12.4 Paywall shows their letter — post-launch

Add a "**Your letter is ready**" card to the paywall (B10.5) between the checklist and the timeline:
- A paper sheet (radius 12, shadow-paper, 120 pt tall) with the first real lines, built from data the app already has: today's date, the provider name, "Re: Account {account number if extracted, else '[your account number]'} — request to review charges", then two lines of placeholder text bars that blur out.
- Caption: "Addressed to {provider}. Disputes {k} charges worth up to {total_savings}."
- No letter text from the backend is shown before payment. The preview uses only the header fields above.
- Add one value line under the price, only when `total_savings >= 3 × price`: "**Costs {price}. Could save up to {total_savings}.**"

#### B12.5 Bills this year → Plus — post-launch

- New onboarding question **O5b**, right after O5 (variants A and C; skipped in B):
  - Headline: **"How many medical bills have you had this year?"**
  - Options: `one` "Just this one" · `two_three` "2 or 3" · `four_plus` "4 or more" · `family` "I handle bills for my family"
  - Saves `bills_this_year`.
- Paywall default: `two_three`, `four_plus` or `family` → **Plus preselected** with a subline on its card: "You said you get several bills a year. Plus covers all of them." `one` → "This bill" preselected. This replaces experiment E3's random default with a rule. Keep E3 only within each group.
- Add `bills_this_year` to `mobile_devices`, `POST /profile`, allowed values and the B10.10 query.

#### B12.6 Outcome loop — post-launch

- The follow-up notification (B10.6) deep-links to a new **"What happened?"** screen for that bill:
  - Title: "**Did {provider} change your bill?**"
  - Options: "They lowered it" · "They removed charges entirely" · "No change yet" · "They said no" · "It went to collections"
  - "They lowered it" asks "What do you owe now?" (currency field), then shows the **win screen**: big highlight amount "**You saved {original − new}**", "Nice work. Billing offices count on people not asking." Buttons: "Share my win" (share card variant with "BillKarma helped me cut my bill by {amount}", no provider by default) and "Done". The App Store review prompt fires here (B10.6 rules).
  - "No change yet" schedules one more reminder 14 days later and points to the phone script.
  - "It went to collections" links to the collections guide on billkarma.app.
- **Backend:** `POST /api/m/bills/{id}/outcome` with `{outcome, final_patient_owes}`. Reuse the validation and storage in `api.record_dispute_outcome` (outcomes `reduced`, `forgiven`, `no_change`, `pending`, `sent_to_collections`). Move the shared logic into a helper so web and mobile write the same `dispute_outcomes` rows.
- Events: `outcome_reported {outcome, saved_band}`, `win_shared`.

#### B12.7 Real social proof (only once it's real) — post-launch

- `GET /api/m/stats` returns, from `dispute_outcomes`: number of reported outcomes, number with savings > 0, total realized savings, and `as_of`. Use **realized** savings from reported outcomes, not `savings_feed.get_aggregate_stats()`'s `total_savings_found` (that sums every finding, which double-counts charges with several findings and includes estimates).
- The app shows proof only when `successful_disputes >= config.MOBILE_PROOF_MIN_OUTCOMES` (start at 50):
  - Welcome (O1), under the subhead: "BillKarma users have reported **{total_realized_savings}** in lower bills." (caption: "Self-reported, as of {month year}")
  - Paywall, under the header: same line, smaller.
- Below the threshold, nothing is shown. **Never** seed, round up or fake these numbers.
- Real testimonials: the win screen's "Share my win" flow asks once "Can we quote you? (first name and city only)". Stored with consent, reviewed by you, then used in O11's testimonial slot.

#### B12.8 Accounts: iCloud Keychain + optional Sign in with Apple — **v1**

**iCloud Keychain (Phase 4, tiny change).** Store `device_token` and `device_id` with `kSecAttrSynchronizable = true` and `kSecAttrAccessibleAfterFirstUnlock`. When the user has iCloud Keychain on, a new iPhone gets the same token, so their bills and paid unlocks come with them, with no login.

**Sign in with Apple (Phase 6; optional for the user, never required).**
- Where it's offered (one button style: Apple's `SignInWithAppleButton`, black, 50 pt, radius 14):
  1. **Right after purchase**, top of the Report: card "**Save this report to your account**" / "So you don't lose it if you change phones." [Sign in with Apple] · "Not now"
  2. **My bills**, when signed out and there's at least one bill: banner "**Back up your bills**" / "Sign in to keep them safe across devices."
  3. **Letter preview**: secondary action "**Email me a copy**". If signed out, sign in first (that gives the email), then send.
  4. **Settings**: new row "Sign in with Apple" / "Signed in as {email or 'Apple ID'}".
- "Not now" hides the Report card for that bill. The My bills banner comes back at most once every 30 days.
- **Backend (new `mobile_accounts.py`):**
  - Table `mobile_accounts (id, apple_sub TEXT UNIQUE, email TEXT, email_is_relay INTEGER, created_at)` and a column `mobile_devices.account_id`.
  - `POST /api/m/auth/apple {identity_token, authorization_code}`: verify the identity token's signature against Apple's public keys (`https://appleid.apple.com/auth/keys`), plus `iss`, `aud` = your bundle ID and `exp`. Pin `PyJWT` and `cryptography` in `requirements.txt` (justified dependencies: don't hand-roll JWT crypto). Create or find the account, link this device, then copy `bill_access_sessions` rows so **every device on the account can open every bill on the account**. Save the refresh token from exchanging `authorization_code` (needed for deletion, below).
  - `POST /api/m/bills/{id}/email-letter`: signed-in only. Send the letter PDF through the existing `email_service.send_email`, rate-limited.
  - RevenueCat stays keyed on `device_id`. Paid report unlocks live on the bill server-side, so they follow the account automatically. Plus follows the Apple ID through Restore purchases.
- **Account deletion (required by App Review 5.1.1(v) once accounts exist):** Settings → "Delete my account and data" deletes the account, every linked device's bills, events and entitlements, and **revokes the Sign in with Apple token** through Apple's `/auth/revoke` endpoint (needs your Sign in with Apple key from the Apple Developer portal, stored as a backend secret).
- Events: `signin_prompt_shown {where}`, `signin_completed {where}`, `letter_emailed`.

#### B12.9 Later (needs more backend work)
- **Your own bill, marked up.** Show the user's photo on the Teaser with highlighter boxes over the flagged lines (numbers blurred until paid). This is the most compelling version of the teaser, but it needs the scanner to return line positions (Gemini can return bounding boxes, but `scanner.py` doesn't ask for them today). Prototype it after launch.
- **Done-for-you disputes in the app** ("We'll mail it and follow up for you", using your existing Lob and follow-up system) as a separate, higher-priced option once you've confirmed it qualifies as a real-world service under Guideline 3.1.3(e).

**What's deliberately not here:** fake urgency ("offer ends in 10:00"), invented user counts, guarantees you can't honour (Apple, not you, handles IAP refunds), and anything that scares people into paying. They'd lift conversion for a few weeks and cost you reviews, App Review trouble and the trust your whole brand runs on.

### B13. Proof, insurance check and one-tap sending (v1.1)

Three upgrades that raise perceived value without adding per-customer work. Mockups: the "Proof, insurance check, send it" row of the design canvas (WhyFlagged, InsuranceCheck, AddEOB, SendIt, CallMode). Build them in the order below; each one ships on its own.

**Facts from the current backend this section relies on (verify before building):**
- Every finding already has a `rule_id` (`RULE_MARKUP_VS_MEDICARE`, `RULE_NCCI_UNBUNDLING`, `RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT`, `RULE_ER_LEVEL_UPCODING_HEURISTIC`, `RULE_HIGH_QUANTITY_CHECK`, `RULE_REGIONAL_BENCHMARK_OUTLIER`, `RULE_EOB_RECONCILIATION`, `RULE_NO_SURPRISES_ACT_HEURISTIC`) set in `analyzer.RULE_ID_BY_TYPE`.
- `scan_pipeline.run_scan()` already accepts `eob_images` and the analyzer already produces `eob_mismatch` findings; the web scan endpoint sends them, `POST /api/m/scan` does not yet.
- `dispute_workflow` has no EOB-specific wording yet.
- The scanner does not extract a billing phone, email or address. The `hospitals` table has `phone` and `address` but no email.
- The raw extraction is not stored, but `line_items` and `bills` are.

#### B13.1 "Why we flagged this" on every charge

**Backend**
1. New `rule_sources.py` (one dict, under 150 lines) mapping each `rule_id` to:
   - `kind`: `official` (a public dataset or federal rule), `bill` (evidence printed on the user's own bill or EOB), or `check` (a BillKarma heuristic)
   - `explanation`: a one-sentence template filled from the finding, e.g. `"Medicare pays {medicare} for code {code} in {area}. This bill charges {charged}, which is {markup}× that."`
   - `source_name` and `source_url`, e.g. "CMS Medicare Physician Fee Schedule" / `https://www.cms.gov/medicare/payment/fee-schedules/physician`
   - `source_year`: read from config, never typed into the template

   | rule_id | kind | explanation gist | source |
   |---|---|---|---|
   | RULE_MARKUP_VS_MEDICARE | official | Medicare pays X for this code in your area; this bill charges Y (Z×) | CMS fee schedule for the data year actually loaded |
   | RULE_NCCI_UNBUNDLING | official | Medicare's coding edits pay these two codes as one; billing both separately is usually not allowed | CMS NCCI edits, version loaded |
   | RULE_NO_SURPRISES_ACT_HEURISTIC | official | Out-of-network emergency care is generally billed at in-network cost sharing under federal law | cms.gov/medical-bill-rights |
   | RULE_DUPLICATE_SAME_CODE_DATE_AMOUNT | bill | Same code, date and amount appear twice: page P, lines L1 and L2 | the user's bill |
   | RULE_EOB_RECONCILIATION | bill | Your insurer says you owe X; this bill asks for Y | the user's EOB, with its date |
   | RULE_ER_LEVEL_UPCODING_HEURISTIC | check | The highest ER level is for the most severe visits; ask for the records that support it | BillKarma check |
   | RULE_HIGH_QUANTITY_CHECK | check | Quantity N is unusually high for this code | BillKarma check |
   | RULE_REGIONAL_BENCHMARK_OUTLIER | check | Above the typical charge in your region | BillKarma check |

2. `config.py`: `MEDICARE_PFS_YEAR`, `MEDICARE_OPPS_YEAR`, `NCCI_EDITS_VERSION`. Set them from the dataset files the analyzer actually loads (find the loaders and read their years); if a year can't be determined, omit `source_year` rather than guess.
3. `charge_summary.group_findings_by_charge` adds `basis: {kind, rule_id, explanation, source_name, source_url, source_year}` to each reason. Page and line numbers for duplicates come from the extraction if available; otherwise leave them out.
4. Locked views: the free charge (B12.1) includes its `basis` (it's the proof); locked rows never do.
5. Tests: every `rule_id` in `RULE_ID_BY_TYPE` has an entry; no template renders with a missing value; `check` rules never return `kind: official`.

**App (mockup: WhyFlagged)**
- In each `ChargeCard`, below the comparison bar: a ground-coloured panel titled **"Why we flagged this"**, a kind badge, the explanation, and for `official` a source link that opens in an in-app Safari view.
- Badges: `official` → ink capsule "OFFICIAL DATA"; `bill` → mark capsule "FROM YOUR BILL"; `check` → codeBg capsule "BILLKARMA CHECK".
- Collapsed (weaker) charges show the badge + reason label only.
- Footnote under the list: "Official data and items from your bill are strong evidence. BillKarma checks are worth asking about."
- The PDF letter gets the same sources as footnotes.

#### B13.2 Insurance check (EOB)

**Backend**
1. `POST /api/m/scan` accepts an optional `eob_pages[]` (same limits as `pages`) and passes them to `run_scan(..., eob_images)`.
2. New `POST /api/m/bills/{id}/eob` (multipart `eob_pages[]`) for adding a statement after the scan: rebuild the extracted bill from `bills` + `line_items`, merge the EOB the same way `run_scan` does, re-run `analyze_bill`, replace that bill's findings, keep its `report_unlocks` row. If the rebuild isn't possible with stored data, return 409 with "Rescan the bill together with the statement" and the app falls back to a combined rescan.
3. `build_bill_view` adds `insurance_check`: `null` (no EOB), `{status: "match"}`, `{status: "mismatch", eob_owed, bill_owed, difference, eob_date}`, or `{status: "unreadable"}`. Available on locked bills too (it's a headline number, like the teaser total); the `eob_mismatch` finding itself follows the normal lock rules.
4. `dispute_workflow.build_dispute_letter` adds a paragraph when an `eob_mismatch` is included: the EOB date, the patient responsibility it shows, the amount billed, and a request to correct the balance to match the insurer's determination. Test it.

**App (mockups: AddEOB, InsuranceCheck)**
- **AddEOB** appears after the bill pages are captured, only when onboarding O6 = insured or unsure: title "Got your insurance statement too?", body "It's called an Explanation of Benefits (EOB). It shows what your insurer says you owe, the clearest way to catch a billing error.", tip "Find it in your insurer's app or website under Claims, or in the mail a few weeks after your visit.", Primary "Scan my insurance statement", Secondary "Choose photos or a PDF", Skip top right.
- The Report and Teaser show an "Add your insurance statement for a deeper check" card when insured and `insurance_check` is null (calls `/eob`).
- **InsuranceCheck card** (heroBg, top of the report) when there's a mismatch: label "INSURANCE CHECK", pill "Doesn't match", rows "Your insurer says you owe" / "This bill asks for" (mono), a highlight block "{difference} more" with "than your insurance statement says", and a badge "From your insurance statement (EOB) dated {date}". Below it a markSoft note: "If {provider} is in your insurer's network, it generally can't bill you more than your statement says you owe. Your letter asks them to correct it." Match → a small good-coloured "Matches your insurance statement" row instead. Unreadable → "We couldn't read the statement. Try a clearer photo of the page that says what you may owe."
- Events: `eob_prompt_shown`, `eob_added {when: scan|later}`, `insurance_check {status}`.

#### B13.3 One-tap sending

**Backend**
1. Extraction: add optional `billing_phone`, `billing_email`, `billing_address`, `account_number` to the scanner's extraction schema and store them on `bills` (new nullable columns). Extract only what's printed; never infer.
2. `GET /api/m/bills/{id}/contact` → `{provider_name, phone, email, address, source}` where each field comes from the bill first, then `find_hospital_match` → `hospitals.phone/address` (`source: "directory"`). Email only ever comes from the bill. Unlocked bills only.
3. `POST /api/m/bills/{id}/sent {channel}` records `sent_at` and channel (`email`, `call`, `mail`, `portal`); events `letter_sent {channel}`.

**App (mockups: SendIt, CallMode)**
- After the letter preview, **SendIt**: title "Send your letter", sub "To {provider} · Patient Billing", a "PICK ONE" list:
  - **Email it** — `MFMailComposeViewController` with the PDF attached, subject "Account {account} — request to review charges", To = bill email if known, otherwise empty with a hint "Find the billing email on your bill or the hospital's website." Hidden if Mail isn't set up (offer the share sheet instead).
  - **Call billing** — shows the phone number; tapping opens **CallMode**.
  - **Print and mail it** — `UIPrintInteractionController` for the PDF, the address with a Copy button, and "Send with tracking so you have proof."
  - **Patient portal message** — copies the letter text, toast "Copied. Paste it into your hospital's message center."
  - Caption: "Contact details come from your bill. Check them before you send." (or "…from BillKarma's hospital directory…" when `source` is directory).
  - Primary "I've sent it" → `POST /sent`, then the follow-up reminder is scheduled 14 days after the send date (replacing the date-of-purchase reminder), and the bill shows "Sent {date}" in My bills.
- **CallMode**: heroBg card with the number and a mark "Call now" button (`tel:`), the script with the current step highlighted (tap to advance), and "NOTES FROM THE CALL" (rep's name, reference number, what they said) saved **only on the device** (caption "Saved only on this phone"). When the app returns to the foreground after a call, CallMode is still open. Primary "Save notes" marks the bill sent via `call` if not already.
- Events: `send_screen_viewed`, `letter_sent {channel}`, `call_started`, `call_notes_saved`.

#### Phase 8 prompt (one session per sub-section)
> Read docs/ios-guide.md section B13 and the matching mockups. Implement B13.1 (backend `rule_sources.py`, config years, `basis` in charge summaries, tests; then the iOS "Why we flagged this" panel). Run all backend and iOS tests.

Then the same prompt for B13.2, then B13.3.

✅ Every flagged charge shows its basis and kind badge; official sources show a year read from config. A scan with an EOB produces an insurance check; adding one later re-runs the analysis without losing the unlock. "Email it" opens Mail with the PDF attached; "I've sent it" moves the reminder to 14 days after sending.

---

## 5. App Store submission checklist
- **Name (30 chars max):** `BillKarma - Medical Bill Scan` · **Subtitle:** `Find errors. Cut what you owe.`
- **Primary category: Finance** (where money-back apps like Collect, Settlemate and Ditch rank) · Secondary: Medical.
- Keywords (100 chars): `medical bill,hospital bill,bill dispute,overcharge,ER bill,itemized bill,EOB,medicare,negotiate,debt`
- Age rating: 17+ is not needed; answer the questionnaire honestly (no medical treatment info → likely 4+).
- **App Privacy labels** as in B1. Data not linked to identity (no accounts) and not used for tracking.
- In-app purchases submitted with the first build, with review screenshots of the paywall.
- **Review notes:** explain the app, say no login is required, and attach a sample itemized bill image (from `test_assets/scan_baseline/` or `data/ocr_benchmark/`) the reviewer can photograph or import. Mention: "Analysis compares charges with public CMS Medicare rates. It is informational, not legal or medical advice."
- Guideline 3.1.1: the report unlock and Plus are digital content → IAP (done). No links or buttons to web checkout inside the app.
- Guideline 5.1.1: data deletion available in-app (Settings → Delete my data).
- Screenshots (6.9" and 6.5"): 1) "Snap your bill" 2) "$912 in possible errors" 3) charge vs Medicare 4) dispute letter 5) phone script. Use realistic but fake data.
- TestFlight internal build first. Then run through the whole funnel with RevenueCat sandbox purchases.

---

## 6. Environment and secrets

| Where | Key | Value |
|---|---|---|
| Backend env | `REVENUECAT_SECRET_API_KEY` | RevenueCat secret key (`sk_...`) — server only |
| Backend env | `REVENUECAT_WEBHOOK_AUTH` | Random string; also set as the webhook Authorization header in RevenueCat |
| Backend env | `IOS_APP_ID` | `<TEAMID>.app.billkarma.ios` |
| Backend env | `APP_STORE_ID` | Numeric App Store ID (after the app record exists) |
| Backend env | `APPLE_SIGNIN_KEY_ID`, `APPLE_SIGNIN_TEAM_ID`, `APPLE_SIGNIN_PRIVATE_KEY` | Sign in with Apple key (for token exchange and revocation, B12.8) — server only |
| iOS xcconfig | `REVENUECAT_PUBLIC_KEY` | `appl_...` public SDK key (Release); test store key (Debug) |
| iOS xcconfig | `API_BASE_URL` | `http://localhost:8000` (Debug) / `https://billkarma.app` (Release) |

RevenueCat dashboard: create the project, add the App Store app with the App Store Connect API key, create entitlement `plus`, products `bk_report_unlock`, `bk_plus_annual` and (for experiment E4) `bk_report_unlock_offer`, offering `default` with the first two and offering `exit_offer` with the third, and the webhook URL `https://billkarma.app/api/m/revenuecat/webhook`.

---

## 7. Build phases (one Claude Code session each)

Paste this guide, then the phase prompt. Don't start the next phase until the acceptance criteria pass.

**Phase 1 — Backend security fix and refactor (Medbill)**
> Read CLAUDE.md and this guide. Do A0 (stop `/api/scan` leaking findings for locked bills, and update any front-end code that relied on it) and A3 (extract `scan_pipeline.run_scan` with no behavior change). Run the full test suite.

✅ All existing tests pass. New test proves a locked scan response has no findings. The web scan flow still works locally.

**Phase 2 — Mobile API (Medbill)**
> Implement A1, A2, A4, A5 (everything except `/unlock` and the webhook), the phone-script `sections` change from B11 (PS), B12.1 (free charge in locked views), B10.8 (event names) and B10.9 (profile fields, hospital search with facility_id, hospital insight), plus the tests from A8 items 1–4 and 8 and B10.9 item 5. Include `mobile_routes` in `main.py`.

✅ The `curl` flow works locally: register → profile → scan a sample bill from `data/ocr_benchmark/` → `/bills` → `/bills/{id}` returns the locked `BillView` shape exactly as in A5.

**Phase 3 — IAP unlock (Medbill)**
> Implement A6 (unlock with RevenueCat verification and dev mock mode, webhook, Plus caching) and tests A8 items 5–7. Then A7 (AASA, smart banner, app CTA).

✅ Mock unlock flips `locked` to false. Reusing a transaction returns 409. `/.well-known/apple-app-site-association` serves valid JSON.

**Phase 4 — iOS foundation (billkarma-ios)**
> Create the Xcode project per B1/B2. Implement B3 (APIClient, Keychain with iCloud sync per B12.8, Multipart, models with fixture decoding tests) and B5 steps 1 and 4. Add a debug screen that registers the device and lists bills.

✅ The simulator registers a device against the local backend. Decoding tests pass for locked, unlocked and clean fixtures.

**Phase 5 — Onboarding, scan, teaser (billkarma-ios)**
> First build the B7 design system (tokens as Any/Dark color sets, bundled fonts, every component in the B7 table with SwiftUI previews), matching the reference mockups. Then implement the onboarding exactly as specified in B10.1–B10.4 (screens O1–O14, both variants, all copy word for word), the free-charge teaser (B12.1), the Processing, Teaser and Clean result screens from B10.3, B4 screens 2–5 with Scan home and the clean result from B11, B6 analytics with the B10.8 events, plus ImagePrep tests.

✅ Both onboarding variants run start to finish in under 60 seconds of tapping; O13 shows real hospital insight for a hospital with data and the fallback line for one without. On a real iPhone: onboarding → scan a printed sample bill → ProcessingView → TeaserView shows the server's numbers with blurred rows. Events show up in `mobile_events`.

**Phase 6 — Purchases, report, letter (billkarma-ios)**
> Implement B5 step 2, the custom paywall in B10.5 (exit offer behind a flag, off), B4 screens 9–11 with the B11 letter form, letter preview and phone script layouts (unlock call, pending-unlock retry, ReportView, PDF share) B10.6 (follow-up reminder, review prompt rules, shareable result card) and B12.8 Sign in with Apple (backend `mobile_accounts.py` endpoints, the four sign-in prompts, email-a-copy, and account deletion with token revocation). Do not build the post-launch items in B12.

✅ Sign in with Apple links a second device and it sees the same bills; deleting the account revokes the Apple token and removes everything. The paywall shows the bill's real numbers and StoreKit prices for both plans. A sandbox purchase unlocks the bill. The share card contains no name, codes or line items. Killing the app mid-unlock and relaunching still unlocks it. The letter PDF shares to Files and Mail.

**Phase 7 — Bills list, settings, polish, submit (billkarma-ios)**
> Implement B4 screens 12–13 using the B11 My bills and Settings specs (and the B11 sheets), B5 step 5 (deep links), the B7 states/motion/accessibility rules across all screens, B8, B9 and the privacy manifest. Then prepare section 5.

✅ Delete my data wipes the server and the device and returns to onboarding. Restore purchases works. Dynamic Type at the largest size doesn't break layouts. TestFlight build uploaded.

---

## 8. Open decisions (defaults in brackets)

0. Post-launch roadmap: B12.2–B12.7. Pick the next one from the funnel data once you have ~500 installs.
1. Prices: report unlock [$19.99, matches the web $19] and Plus [$59.99/yr].
2. Should Plus also include the done-for-you dispute service later? [No for v1.]
3. Hard paywall before any scan, or free scan + teaser? [Free scan + teaser. The teaser number *is* the hook, and clean bills stay free.]
4. Long OCR times: if p95 scan time is over 45 s in TestFlight, switch `/scan` to an async job (`POST` returns `bill_id` + `status=processing`; the app polls `GET /bills/{id}`).
