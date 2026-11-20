# ClaimCoach Phase 1: backend design

Implements PRD sections **Appeal rules engine**, **AI pipeline**, **Data model and API**, **Compliance, privacy and claims language** and **Pricing** (unlock model only). Build plan: `docs/cc-build-prompt.md` §2 (in the claimcoach-ios repo).

Follow `CLAUDE.md`: flat modules, files under 300 lines, raw parameterized SQL, constants in `config.py`, `{"status": "ok", "data": ...}` responses (use `mobile_routes.ok`), no dead code. **No tests are written in this phase** (owner's decision); run the code you write.

## Where the plan and the real code differ, and what we do

| Plan says | Real code | Decision |
|---|---|---|
| Numbered SQL migration | Schema is inline in `db.py` (`SCHEMA` + `_run_migrations.ensure_columns`); `db.py` is 2,244 lines | New `cc_db.py` holds the ClaimCoach schema; `db.init_db()` calls `cc_db.init(db)` |
| Letter additions go in `appeal_letter.py` | 144 lines now; additions would pass 300 | New builders go in `appeal_kit.py`; `appeal_letter.py` gets two small changes only |
| Move case logic out of `appeals.py` | `record_sent`/`record_outcome`/`mail_by_lob` write the web table `appeal_cases` and send emails | Leave them. Only `deadlines()` changes (uses `appeal_rules`). ClaimCoach has its own `cc_cases.py`; shared pieces are `appeal_rules`, `appeal_letter`, `fax.send_fax`, `debt_fighter.send_certified_letter` |
| Images saved to `private_uploads`, deleted after extraction | — | Images are **never written to disk**: they are read in memory and dropped. Nothing to purge. (Send-for-me faxes text, not images.) |
| Self-check: claim number appears in the OCR text | There is no separate OCR text | Use `field_confidence` and format checks instead |
| `PLAN_TYPES` has all plan types | No `original_medicare` | Add it |
| Web send method `certified_mail` | — | ClaimCoach uses `mail` / `fax` / `self` in its own tables |

## Modules

### `config.py` (additions, next to the existing `APPEAL_*` block)
```python
APPEAL_FILING_DAYS = {"employer": 180, "individual": 180, "medicare_advantage": 65, "original_medicare": 120, "medicaid": 60}
# ClaimCoach
CC_SCAN_MAX_PAGES = 8
CC_SCAN_LIMIT_PER_HOUR = 10
CC_EXTRACT_SCHEMA_VERSION = "cc-1"
CC_CONFIRM_CONFIDENCE = 0.8          # fields read with less confidence are shown for the user to confirm
CC_DENIAL_REASON_MAX_CHARS = 300
CC_EXTRA_FACTS_MAX_CHARS = 1500
CC_FREE_CHECKLIST_ITEMS = 3
CC_APPEAL_KIT_PRODUCT_ID = os.getenv("CC_APPEAL_KIT_PRODUCT_ID", "cc_appeal_kit")
CC_PLUS_ENTITLEMENT = os.getenv("CC_PLUS_ENTITLEMENT", "cc_plus")
CC_SEND_FOR_ME_ENABLED = os.getenv("CC_SEND_FOR_ME_ENABLED", "") == "1"
CC_REMINDER_DAYS_BEFORE = (14, 3)
CC_RETENTION_DAYS = 365
CC_EVENT_NAMES = {...}               # the 16 names in the build plan §2.4
CC_EVENT_PROP_PATTERN = r"[a-z0-9_]{1,40}"
```

### `appeal_rules.py` (new, no AI, no DB)
`VERIFIED_ON = "2026-11-20"`. `RULES` is one dict keyed by plan type; each entry:
```python
{"level": "internal", "level_label": "Internal appeal", "file_within_days": 180,
 "decision_days": {"pre_service": 30, "post_service": 60, "urgent": 3},
 "next_level": "external", "next_level_label": "External review", "next_level_days": 120,
 "next_level_automatic": False, "next_level_goes_to": "...one sentence...",
 "source_url": "...", "verified_on": VERIFIED_ON}
```
Values, exactly:

| plan_type | level / label | file within | decision days (pre/post/urgent) | next level / label | next days | automatic |
|---|---|---|---|---|---|---|
| individual | internal / Internal appeal | 180 | 30 / 60 / 3 | external / External review | 120 | no |
| employer | internal / Internal appeal | 180 | 30 / 60 / 3 | external / External review | 120 | no |
| medicare_advantage | internal / Plan reconsideration | 65 | 30 / 60 / 3 | ire / Independent Review Entity (IRE) | None | yes |
| original_medicare | internal / Redetermination | 120 | 60 / 60 / 60 | qic / QIC reconsideration | 180 | no |
| medicaid | internal / Plan appeal | 60 | None (varies by state) | fair_hearing / State fair hearing | 120 | no |

`file_within_days` must be read from `config.APPEAL_FILING_DAYS[plan_type]` and employer/individual/MA decision days from `config.APPEAL_DECISION_DAYS` (no duplicated numbers). Source URLs are the ones in the build plan §2.5 table. `next_level_goes_to` wording:
- individual: "An independent reviewer outside your insurer decides. Your final denial letter says how to ask for it."
- employer: "An independent reviewer decides, through a federal or state process. Your final denial letter says which one and how to ask. Some employer plans have a second internal appeal first."
- medicare_advantage: "Your plan must send your case to Medicare's independent reviewer automatically. You don't need to file anything."
- original_medicare: "A Qualified Independent Contractor (QIC) reviews the decision. The redetermination notice explains how to ask."
- medicaid: "Your state holds a fair hearing. The plan's decision letter explains how to ask for one."

Functions:
```python
def route(plan_type, service_timing, notice_date: date | None, printed_deadline: date | None) -> dict
    # -> {level, level_label, file_by (date|None), deadline_source ("letter"|"default"|None),
    #     decision_window_days (int|None), next_level_label, next_level_days, source_url}
```
- `printed_deadline` wins: `file_by=printed_deadline`, `deadline_source="letter"`, for every plan type including unknown.
- Else known plan + `notice_date`: `file_by = notice_date + file_within_days`, `deadline_source="default"`.
- Else `file_by=None`, `deadline_source=None`.
- Unknown/"other" plan type: `level="internal"`, `level_label="Appeal"`, `decision_window_days=None`, next-level fields `None`.

```python
def decision_due(plan_type, service_timing, sent_on: date) -> date | None
def next_level(plan_type, decided_on: date) -> dict | None
    # -> {level, level_label, file_by (date|None), automatic (bool), goes_to, source_url}; None for unknown plan types
```
`appeals.deadlines()` is rewritten on top of `route`, `decision_due`, `next_level` and must return the same three keys with the same values as today for employer / individual / medicare_advantage, except: MA `external_review_by` becomes `None` (IRE is automatic), and the two new plan types now get dates.

### `cc_db.py` (new)
`SCHEMA` = the three tables from the build plan §2.3 (`cc_cases`, `cc_case_unlocks`, `cc_sends`) plus these extra `cc_cases` columns: `plain_reason TEXT`, `needs_confirmation TEXT` (JSON list), `letter_text TEXT`, `decided_at DATE`; and `CREATE INDEX IF NOT EXISTS idx_cc_unlocks_case ON cc_case_unlocks(case_id)`, `idx_cc_sends_case ON cc_sends(case_id)`.
`def init(db)`: `db.executescript(SCHEMA)` then add `mobile_devices.app TEXT NOT NULL DEFAULT 'billkarma'` if missing. `db.init_db()` calls it after `_run_migrations(db)`.

### `cc_extract.py` (new) — PRD AI pipeline steps 1–2
```python
def read_denial_letter(pages: list[tuple[bytes, str]], eob_pages: list[tuple[bytes, str]] | None = None) -> dict
def printed_deadline(extracted: dict) -> date | None
def needs_confirmation(extracted: dict) -> list[str]
```
- One Gemini call: every page as a `types.Part` (after `scanner._prepare_media_for_ocr`), then the prompt; `scanner._get_client()`, `config.GEMINI_MODEL`, JSON response, temperature 0, `scanner._parse_json_response`, one retry on broken JSON (as `scanner._run_vision_extraction` does). Raises `scanner.ScannerNotConfigured` / `ValueError` like the scanner.
- `EXTRACTION_PROMPT`: "You read health insurance denial letters. Extract ONLY what is printed. Never infer, guess or calculate. Use null when a field is not printed." then the `cc-1` field list from the build plan §2.6 with one line per field, dates as `YYYY-MM-DD`, amounts as numbers, `field_confidence` 0–1 per field. If EOB pages follow the letter, they may fill claim number, amounts, codes and `denial_codes` only.
- After parsing: keep only the known keys; coerce amounts with `scanner._coerce_numeric` (negative → None); invalid dates → None; truncate `denial_reason_text` to `CC_DENIAL_REASON_MAX_CHARS`; lists default to `[]`; set `schema_version`.
- `printed_deadline`: `printed_appeal_deadline` if it parses; otherwise parse `printed_appeal_window_text` in code (`(\d+)\s*(calendar\s+|business\s+)?(day|month)s?`; days → `notice_date + N days`, months → calendar months) when `notice_date` is known. A result on or before `notice_date` is discarded.
- `needs_confirmation`: field names among `insurer_name, claim_number, notice_date, printed_appeal_deadline, service_description, denial_reason` that are missing, or whose `field_confidence` is below `CC_CONFIRM_CONFIDENCE`, or (deadline) were discarded.

### `cc_classify.py` (new) — PRD AI pipeline steps 3 and 5
```python
def denial_reason(extracted: dict) -> str            # key in appeal_letter.DENIAL_REASONS
def plan_type(extracted: dict, user_answer: str | None) -> tuple[str, bool]   # (plan_type, needs_confirmation)
def service_timing(extracted: dict, user_answer: str | None) -> str
def plain_reason(extracted: dict, reason_key: str) -> str
```
- `denial_reason`: keyword map over lowercased `denial_reason_text` + `criteria_cited`, first match in this order: experimental ("experimental", "investigational", "unproven") → prior_authorization ("prior authorization", "preauthorization", "pre-certification", "precertification", "not authorized", "no authorization") → out_of_network ("out-of-network", "out of network", "non-participating", "nonparticipating") → medical_necessity ("medically necessary", "medical necessity") → not_covered ("not a covered", "not covered", "excluded", "exclusion", "benefit limit") → coding_error ("duplicate", "coding", "incorrect code", "missing information", "invalid code", "modifier"). No match and text present: one Gemini text call that must answer with exactly one of the 7 keys; anything else, or no key configured, → "other".
- `plan_type`: signal map (case-insensitive): "medicare advantage"/"ire"/"organization determination" → medicare_advantage; "medicare summary notice"/"redetermination" → original_medicare; "medicaid"/"fair hearing" → medicaid; "erisa" → employer; "marketplace"/"healthcare.gov"/"exchange" → individual. User answer valid and no signal → user answer, False. Signal and no valid answer (or answer "other") → signal, True. Both and they agree → False. Both and they disagree → **user answer, True** (never resolved silently). Neither → "other", True.
- `service_timing`: the user's answer if valid; else `pre_service` when `is_prior_auth`, else `post_service`. `urgent` only ever comes from the user.
- `plain_reason`: Gemini text call: "Rewrite this insurance denial reason in plain English for the patient, in at most 2 sentences. Use only what the text says. Do not add advice, deadlines, laws, or anything about whether the appeal will succeed." If it fails, is empty, or no key: template fallback `f"Your insurer says: {DENIAL_REASONS[reason_key].lower()}."`. Cut to 2 sentences in code.

### `appeal_letter.py` (two small changes)
- Add `"original_medicare": "Original Medicare (Part A or B)"` to `PLAN_TYPES` (before `medicaid`).
- `build_appeal_letter`: skip the "Amount denied" line when `amount_denied` is None; skip the email line when there is no email; the RE line uses `case.get("level_label")` when present ("Request for plan reconsideration") and is unchanged otherwise. An optional `case.get("case_paragraph")` is inserted right after the reason argument. Output for existing web cases must be byte-identical.

### `appeal_kit.py` (new) — the rest of the paid kit, all templates
```python
def evidence_checklist(denial_reason: str) -> list[str]
def build_doctor_request(case: dict) -> str
def phone_script(case: dict) -> list[dict]          # [{"heading": str, "say": str}]
def build_external_review_request(case: dict, next_level: dict) -> str
def case_paragraph(case: dict, extra_facts: str) -> str | None
def wants_billkarma(case: dict) -> bool             # out_of_network → True
```
`case` here is the letter case dict built by `cc_cases.letter_case` (keys below). Copy rules: never "guaranteed", "we'll get it paid", "win rate", "overturn your denial", "we'll win"; nothing about odds of success.
- `evidence_checklist`: 4–6 plain items per reason, most useful first. Every list starts with "A copy of the denial letter". medical_necessity/experimental include "A letter of medical necessity from your doctor" second. prior_authorization: proof the authorization was requested, or a note from the doctor on why it could not be. out_of_network: proof it was an emergency or that no in-network provider was available. not_covered: the page of your plan documents that describes this benefit. coding_error: the corrected claim or a note from the provider's billing office.
- `build_doctor_request`: short letter from the patient to the provider: names the service, the insurer, the denial reason label, the filing date if known, and asks for a letter of medical necessity and, where the plan offers it, a peer-to-peer review; lists what the letter should cover (diagnosis, why this treatment, what was tried first, what happens without it).
- `phone_script`: steps: who you are and the claim number; "I'm calling about a denied claim and I plan to appeal"; ask for the specific criteria or plan provision used; confirm the appeal deadline and the address or fax for appeals; if urgent, ask for an expedited appeal; ask for a reference number for the call.
- `build_external_review_request`: for `next_level["automatic"]` (Medicare Advantage) returns a short note explaining the plan forwards the case to the IRE and what to keep ready; otherwise a letter requesting the next level by its label, citing the final denial date and enclosing the denial letters.
- `case_paragraph`: one Gemini text call. Inputs: service, reason label, `extra_facts` (cut to `CC_EXTRA_FACTS_MAX_CHARS`). Prompt: one paragraph, first person, at most 90 words, only the facts given, no studies, guidelines, laws, statistics, or promises. Returns None when `extra_facts` is empty, the call fails, or the output contains a digit-year citation pattern, "study", "studies", "guideline", "U.S.C", "CFR", "Act" or "law".

### `cc_cases.py` (new) — storage and state
```python
def create_case(device_id, for_whom, extracted, plan_type, service_timing, reason_key, plain_reason, confirm: list[str]) -> int
def get_case(case_id) -> dict | None                 # row dict with "extracted" (parsed) and "needs_confirmation" (list)
def require_case(device_id, case_id) -> dict         # 404 unknown, 403 other device
def list_cases(device_id) -> list[dict]              # newest first
def update_confirmed(case: dict, fields: dict) -> None
def reroute(case_id) -> None                         # recompute file_by/deadline_source/level from appeal_rules.route and store
def record_sent(case: dict, channel: str, sent_on: date) -> None      # status 'sent', decision_due from appeal_rules.decision_due
def record_outcome(case: dict, outcome: str, amount_recovered: float | None) -> None   # status 'decided', decided_at today
def save_letter(case_id, letter_text) -> None
def letter_case(case: dict, name: str, member_id: str) -> dict        # dict in the shape build_appeal_letter expects
def delete_case(case_id) -> None                     # cc_sends, cc_case_unlocks, cc_cases
def delete_device_cases(device_id) -> None
def purge_old(days: int) -> int                      # cases created before the cutoff
```
- `update_confirmed` accepts only: `insurer_name, claim_number, service_description, notice_date, printed_appeal_deadline` (written into `extracted`) and `denial_reason, plan_type, service_timing` (columns, validated against `DENIAL_REASONS`, `PLAN_TYPES`, `SERVICE_TIMINGS`); bad values → `HTTPException(400)`. Confirmed fields are removed from `needs_confirmation`; status becomes `ready`; then `reroute`.
- `letter_case` maps: `patient_name=name`, `member_id` (argument, else extracted), `claim_number, provider_name, service_description, service_date, insurer_name` from extracted, `denial_date=notice_date` (or "[DATE OF DENIAL]"), `amount_denied`, `insurer_appeal_address=extracted.appeal_address`, `service_timing, denial_reason, plan_type`, `level_label`, `file_by`, `mailing_address=None, phone=None, email=None`.
- `compliance.purge_old_data` adds `cc_cases.purge_old(days)` to its count. `mobile_routes.delete_device` is not touched; ClaimCoach has its own `DELETE /api/cc/device`.

### `cc_purchases.py` (new)
```python
def is_unlocked(case_id) -> bool                     # a cc_case_unlocks row with status 'paid'
def unlock_with_purchase(device_id, case_id, transaction_id) -> None
def unlock_with_plus(device_id, case_id) -> bool
def handle_webhook_event(event: dict) -> None
```
- `unlock_with_purchase`: source `iap:<transaction_id>`. Same case → return. Other case → 409 "This purchase was already used for another appeal". Verify with `mobile_purchases._transaction_is_genuine(device_id, transaction_id, (config.CC_APPEAL_KIT_PRODUCT_ID,))`; not genuine → 402. `INSERT OR IGNORE`.
- Plus: active when `mobile_entitlements.plus_active` is set for the device (ClaimCoach devices are their own rows, so there is no clash with BillKarma Plus). When not active and not in mock mode, check `mobile_purchases._fetch_subscriber(device_id)["entitlements"]` for `config.CC_PLUS_ENTITLEMENT` and store it with `mobile_purchases._set_plus`. Source `plus:<device_id>:<case_id>`.
- `handle_webhook_event`: activating events / EXPIRATION carrying `CC_PLUS_ENTITLEMENT` → `_set_plus`; CANCELLATION of `CC_APPEAL_KIT_PRODUCT_ID` → `cc_case_unlocks.status='refunded'`. `mobile_purchase_routes.revenuecat_webhook` calls it right after the existing handler. The existing handler is unchanged.

### `cc_view.py` (new)
```python
def build_case_view(case_id: int) -> dict
def case_summary(case: dict) -> dict     # {case_id, insurer, service, reason_label, file_by, deadline_source, status, locked}
```
`build_case_view` returns exactly the `CaseView` shape in the build plan §2.8, plus `"status"`, `"for_whom"`, `"service_timing"`, `"outcome"`, `"next_level"` (from `appeal_rules.next_level` when outcome is `upheld`, else null), `"rule_source_url"`.
- Dates are ISO strings. `route.plan_label` = `PLAN_TYPES[plan_type]`. `send_to` = `{address, fax, phone}` from extracted.
- `evidence_checklist`: locked → first `CC_FREE_CHECKLIST_ITEMS` items; unlocked → all.
- `letter`: `None` when locked or when no letter has been built; otherwise `{"letter_text": ...}` only. **A locked view never contains letter text, the case paragraph, the doctor request or the phone script.**
- `timeline`: Denial notice (notice_date, done) → File by (file_by, done when sent) → Sent (sent_at date, when sent) → Decision due (decision_due, done when decided) → Decision (decided_at, when decided).
- `next_step.kind`: `confirm` (needs_confirmation not empty and status draft) → `file_appeal` (not sent; label "File your {level_label lower} by {date}" or "Check your letter for the deadline") → `wait_for_decision` → `next_level` (upheld) → `done`. For `service_timing == "urgent"` and not sent: kind `urgent`, label "Ask for an expedited appeal and call your doctor today".
- `crosspromo`: `"billkarma"` when `appeal_kit.wants_billkarma`, else null. `price`: `{"product_id": config.CC_APPEAL_KIT_PRODUCT_ID}`.

### `cc_send.py` (new, flag off)
`def send_for_me(case: dict, channel: str, approved_text_hash: str, mailing_address: str = "") -> dict` → `{send_id, status}`. 400 when the hash differs from `sha256(case["letter_text"])`, when the fax number / appeal address is missing, or (mail) when `mailing_address` is empty. Fax: `fax.send_fax`. Mail: `debt_fighter.send_certified_letter` with `config.LOB_API_KEY`. Inserts a `cc_sends` row and calls `cc_cases.record_sent`. Provider errors → 502.

### Routes — `cc_routes.py` and `cc_case_routes.py`, both `APIRouter(prefix="/api/cc")`, included in `main.py` after `mobile_account_router`
All routes except `POST /device` use `Depends(mobile_auth.device_from_request)`. Paths, requests and responses are the table in the build plan §2.8. Details:
- `cc_routes.py`: `POST /device` (rate limit key `cc-register:<ip>`, `MOBILE_REGISTER_LIMIT_PER_HOUR`; after `mobile_auth.register_device` set `app='claimcoach'`), `DELETE /device` (cases, `mobile_events`, `mobile_entitlements`, `mobile_devices` row; `log_audit("cc_delete_device", "device", device_id)`), `POST /events` (name in `CC_EVENT_NAMES`, props ≤ `MOBILE_EVENT_PROPS_MAX_BYTES`, every prop value a bool, an int, or a string fully matching `CC_EVENT_PROP_PATTERN`; anything else is dropped silently; stored in `mobile_events`). The RevenueCat webhook is the existing `/api/m/revenuecat/webhook`.
- `cc_case_routes.py`:
  - `POST /cases`: 1..`CC_SCAN_MAX_PAGES` pages (and at most that many `eob_pages`), same MIME and size checks as `mobile_bill_routes._read_pages` (import and reuse it); `for_whom` in {self, someone_else}; `plan_type`/`service_timing` optional; rate limit `cc-scan:<device>` at `CC_SCAN_LIMIT_PER_HOUR`. `ScannerNotConfigured` → 503 "Letter reading is unavailable right now. Please try again later."; `ValueError` → 400 "We couldn't read that letter. Try clearer photos." Then classify, create, reroute, `log_audit("cc_scan", "cc_case", id, metadata={"pages": n})` (no health content), return the view.
  - `PATCH /cases/{id}`, `GET /cases`, `GET /cases/{id}`, `DELETE /cases/{id}` (audit `cc_delete_case`).
  - `POST /cases/{id}/unlock`: `transaction_id` → purchase; empty → Plus, 402 "ClaimCoach Plus is not active on this device" when it isn't.
  - `POST /cases/{id}/letter`: 402 "Unlock this appeal to get the letter" while locked. Body `{name, member_id, extra_facts, next_level}`; `name` required (400). Builds `letter_case`, `case_paragraph`, then `build_appeal_letter` (or `build_external_review_request` when `next_level` is true and the outcome is upheld), saves it, and returns `{letter_text, case_paragraph_range: [start, end] | null, doctor_request, checklist, phone_script}`. `case_paragraph_range` is the character range of the paragraph inside `letter_text`.
  - `POST /cases/{id}/sent`: `{channel: "self", date}`; date optional (today), not in the future.
  - `POST /cases/{id}/send`: 404 unless `CC_SEND_FOR_ME_ENABLED`; requires unlocked; `channel` in {fax, mail}.
  - `POST /cases/{id}/outcome`: `outcome` in {overturned, partial, upheld}; `amount_recovered` optional number ≥ 0.

### Golden set and gate
- `test_assets/cc_golden/`: `README.md` (format), `generate.py` (draws 5 synthetic denial letters with Pillow, same approach as `test_assets/scan_baseline/scripts/generate_synthetic_baselines.py`), the 5 PNGs, and `expected.jsonl` (`file`, `claim_number`, `notice_date`, `printed_deadline`, `plan_type`, `reason_key`). Cases: employer medical necessity with a printed date; ACA out-of-network with "within 180 days"; Medicare Advantage with "within 65 days"; Medicaid with a printed date; employer prior-auth denial with no deadline printed.
- `cc_accuracy.py`: `def cc_gate() -> list[str]`: skips (returns `[]`) when the set has fewer than `CC_GOLDEN_MIN_CASES = 5` or `GEMINI_API_KEY` is unset; otherwise each of claim number, notice date and printed deadline must be ≥ `CC_GOLDEN_MIN_ACCURACY = 0.95` exact, and there must be zero cases where the computed `file_by` is later than the expected printed deadline. `accuracy_gate.run_gate` adds its failures when `suites is None`.

## Edge cases
- No notice date and no printed deadline → `file_by` null; UI says "check your letter".
- Printed deadline already past → still returned; the app words it.
- Unknown plan type → no default deadline, level label "Appeal".
- Medicaid decision window is null ("varies by state"): `decision_due` is null after sending.
- A refunded kit locks the case again; the stored letter is not returned while locked.
- Deleting a device deletes its cases even if unlocked.

## Coding tasks
- **A** — `config.py`, `appeal_rules.py`, `cc_db.py`, `db.py` hook, `appeals.deadlines()`.
- **B** — `cc_extract.py`, `cc_classify.py`, `appeal_kit.py`, `appeal_letter.py` changes.
- **C** (after A and B) — `cc_cases.py`, `cc_purchases.py`, `cc_view.py`, `cc_send.py`, `cc_routes.py`, `cc_case_routes.py`, `main.py`, `mobile_purchase_routes.py`, `compliance.py`.
- **D** (after C) — golden set, `cc_accuracy.py`, `accuracy_gate.py`.
