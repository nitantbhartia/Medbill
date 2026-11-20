# ClaimCoach — PRD & Technical Design

Nov 20, 2026 · @Nitant

## Summary

ClaimCoach is an iOS app that turns a health insurance denial letter into a ready-to-send appeal, with the deadline tracked, in about 10 minutes. It is BillKarma's sibling: the same scan → find → letter → follow-up loop, pointed at the insurer instead of the hospital.

**One-line pitch:** "Insurance said no? Scan the letter. We'll tell you why, what to send and by when."

**Key finding from the codebase review:** most of ClaimCoach already exists in pieces. Medbill has a full web appeal concierge (`appeals.py`, `appeal_letter.py`, `appeal_routes.py`: intake, plan types, denial reasons, deadlines, Lob mail, fax, outcomes), and the BillKarma iOS app has an `AppealView` behind the `denialAppeal` flag (off). v1 is mostly a new iOS shell plus a denial-letter reader, not a new product from scratch.

**v1 decision (recommended):**

- **New iOS repo** `claimcoach-ios`, forked from `billkarma-ios` (design system, networking, purchases, scan).
- **Same backend** (Medbill, same Railway service) with a new `/api/cc/*` router. The appeal logic, Lob, fax, Gemini extraction and device auth already live there. A second backend would duplicate all of it.
- **Same audience and social accounts** as BillKarma, as "from the makers of BillKarma".
- **Build gate:** start the build when 3–5 denial-themed BillKarma videos outperform the bill-error videos (see Metrics). Until then, run the research items in this doc.

**Not promised:** ClaimCoach never says it will get a claim paid. It writes a strong appeal and keeps you on time.

## Problem and market research

Denials are common, appeals are rare, and the people who do appeal often win. The gap is effort and know-how, not rights.

| Fact | Figure | Source |
| --- | --- | --- |
| In-network claims denied, HealthCare.gov insurers, 2023 | 19–20% (out-of-network: 36–37%) | [KFF, 2023 data](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans-in-2023/) |
| Denied claims that consumers appealed, 2024 | under 1% | [KFF, 2024 data](https://www.kff.org/private-insurance/issue-brief/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/) |
| Appeals where the insurer upheld its denial, 2024 | 66% | [KFF, 2024 data](https://www.kff.org/private-insurance/issue-brief/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/) |
| Insurer-level in-network denial rates, 2024 | 3% to 36% | [KFF, 2024 data](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/) |
| Insured adults who call denials and delays a "major problem" (Jan 2026 poll) | 66% | [KFF, 2024 data](https://www.kff.org/private-insurance/issue-brief/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/) |

The KFF figures cover HealthCare.gov plans only. Employer plans (most private coverage) and state marketplaces are not in the public data, so treat them as directional.

**Why people don't appeal** (working hypotheses to test in research interviews):

1. They don't know they can, or think the denial is final.
2. The letter is unreadable: codes, plan jargon, no clear next step.
3. They don't know which process applies (employer vs ACA vs Medicare vs Medicaid) or the deadline.
4. Writing a clinical argument feels impossible without a doctor's help.
5. They expect to lose (two-thirds of internal appeals are upheld), so the effort feels wasted. External review is the step most people never reach.

## Competitive landscape

The letter itself is already free elsewhere, so ClaimCoach cannot win on "AI writes your appeal". It wins on being a native phone app that handles the whole case: reading the letter, the right process and deadline, sending, follow-up and the next level. Plus distribution through BillKarma's audience.

| Product | What it does | Price | Gap ClaimCoach fills |
| --- | --- | --- | --- |
| [Counterforce Health](https://stateline.org/2025/11/20/patients-deploy-bots-to-battle-health-insurers-that-deny-care/) | Nonprofit; analyzes the denial letter, policy and medical research to draft an appeal | Free | Web-first; letter-focused. No phone-native case tracking or sending |
| [Fight Health Insurance](https://www.zenml.io/llmops-database/using-llms-to-combat-health-insurance-claim-denials) | Open-source; scan a denial, choose from several drafted letters | Free; fax for a small fee | Built for people who already know the process; consumer polish is thin |
| [Claimable](https://www.wabe.org/ai-powered-tool-claimable-helps-patients-fight-insurance-claim-denials/) | Appeals with clinical research and other patients' appeal history, focused on drugs and treatments | Not checked | Narrow (specialty drugs, chronic disease); not a general claims app |
| [Sheer Health](https://stateline.org/2025/11/20/patients-deploy-bots-to-battle-health-insurers-that-deny-care/) | Connect your insurance account, upload bills and claims, ask questions | Not checked | Broad navigation; appeals are one feature among many |

**How ClaimCoach is different:**

- **Phone-first:** scan the letter on the kitchen table, not a web upload flow.
- **The process, not just the letter:** it identifies the plan type, the appeal level and the deadline, and reminds you.
- **Sends it for you:** fax and certified mail already exist in Medbill.
- **Walks you to the next level:** internal appeal → external review, or MA reconsideration → the independent reviewer (IRE).
- **Pairs with BillKarma:** a denied claim often turns into a hospital bill, and the two apps hand off to each other.

**Risk to note:** a reporter or regulator may compare a paid app with free nonprofits. The free tier (understanding the denial and the deadline) has to be truly useful, so the paid part is clearly the convenience: sending, tracking and escalation.

## Users, jobs and v1 scope

v1 serves one person: someone holding a denial letter for care they already had, on an employer or ACA plan, who wants to fight it without a lawyer.

| User | Situation | Job to be done | v1? |
| --- | --- | --- | --- |
| Post-service denial, employer or ACA plan | Got the care; claim denied; now owes the bill | "Get the insurer to pay what it should" | Yes, the core |
| Prior-auth denial | Care not yet given; doctor's request denied | "Get approval so I can get the care" | Yes, but the letter leans on the doctor (peer-to-peer, letter of medical necessity) |
| Urgent | Waiting could seriously harm their health | "Get a decision in days, not weeks" | Yes, with an expedited path and a clear "call your doctor and the plan now" message |
| Medicare Advantage member | Plan issued an adverse organization determination | "Request a reconsideration on time" (65 days) | Yes |
| Original Medicare / Medicaid | MSN denial / managed-care ABD | Different forms and agencies | v1.1: routing and deadlines only; letter later |
| Caregiver for a parent or child | Handling someone else's denial | Same as above, for someone else | Yes: "Appealing for someone else" sets up an authorized-representative form |

**v1 scope (ship this):**

1. Onboarding (short): who is the appeal for, plan type, already had the care or not.
2. Scan the denial letter (and optionally the EOB) with the camera, photos or a PDF.
3. **Free:** "Your denial, explained": the reason in plain English, the plan type, the appeal level, the deadline (from the letter when printed; otherwise the usual window, clearly labelled), and what evidence helps.
4. **Paid:** the appeal letter for that denial reason, a doctor-request template (letter of medical necessity), a phone script and a checklist of what to attach.
5. Send: fax or certified mail through Medbill, or share the PDF yourself.
6. Case tracking: sent date, decision due date, reminders, and the outcome check-in.
7. If upheld: the external-review (or IRE) step with its own deadline and letter.
8. My appeals list, settings, delete my data.

**Not in v1:** connecting insurer accounts, Original Medicare redetermination forms, Medicaid fair-hearing filing, dental and vision, pharmacy (Part D) denials, Android, human advocates.

## Product experience

ClaimCoach uses BillKarma's design system unchanged, so the two apps read as one family. The one new idea is that **the deadline gets the highlighter.** In BillKarma the yellow mark sits on the money we found; in ClaimCoach it sits on the denial reason and the date you must file by.

**Brand, carried over from BillKarma (`Design/Theme.swift`, `Typography.swift`):**

- Colours: ink `#0E1726`, ground `#F4F5F7`, paper, mark `#FFE14D`, over (rust) for problems, good `#00824F` only for confirmations. Light and dark pairs as in BillKarma.
- Type: Inter Tight 800 for heroes and titles, Inter for body, IBM Plex Mono for evidence (claim numbers, codes, dates printed on the letter).
- Signature moves: the rotated highlighter block, ink hero cards for the moment of truth, mono for evidence.
- Tone: a friend who has fought insurers before. Calm, plain and specific. No "we'll win", no fear selling.
- App icon: same family as BillKarma (receipt + yellow highlight on green), but a letter with a highlighted line and a calendar or clock badge. Design it in the BillKarma icon canvas.

**Screens (v1):**

| # | Screen | Purpose | Reuses from BillKarma |
| --- | --- | --- | --- |
| 1 | Welcome | "Insurance said no? You can appeal." + Scan CTA | `WelcomeView`, `MarkedBill` (as a marked-up denial letter) |
| 2 | Who and what (3 quick questions) | For me or someone else; plan type; had the care yet? | `SingleChoiceStep`, `OnboardingModel` |
| 3 | Scan | Denial letter pages, optional EOB | `DocumentScanner`, `ScanSourceButtons`, `ImagePrep` |
| 4 | Reading your letter | Progress while extraction runs (20–60 s) | `ProcessingView` |
| 5 | Confirm details | Insurer, claim number, service, denial date, reason; user fixes anything wrong | `ConfirmLinesView` pattern |
| 6 | **Your denial, explained (free)** | Ink hero: reason highlighted + "File by {date}" highlighted; plain-English why; appeal level; what helps | `HeroResultCard`, `HighlightAmount` (as a date), `TipCard` |
| 7 | Paywall | Unlock the appeal kit; or the send-for-me bundle | `PaywallScreen`, `PlanCard`, `Timeline` |
| 8 | Your appeal | The letter, the doctor-request template, the attach-this checklist, the phone script | `LetterPreviewView`, `LetterPDF`, `PhoneScriptView` |
| 9 | Send it | Fax for me, certified mail for me, or share the PDF | `SendItView`, `ActivityView` |
| 10 | Case timeline | Sent → decision due → outcome; reminders | `Timeline`, `NotificationRouter` |
| 11 | Outcome check-in | Overturned / partly / upheld → next step | New, small |
| 12 | Next level | External review or IRE: deadline, letter, where to send | Reuses screens 8–9 |
| 13 | My appeals, Settings | List of cases; restore, delete my data | `BillsListView`, `SettingsView` |

Every screen gets a mockup in a ClaimCoach Design canvas before it is built, like `docs/mockups/` in BillKarma. Where the mockup and this doc disagree, the mockup wins.

## Appeal rules engine

The engine answers three questions for every case: which process applies, what the next step is, and the date it must be filed by. Getting the plan type wrong sends the appeal to the wrong place, so the app asks and confirms it rather than guessing.

**Rule 1: the date printed on the denial letter always wins.** The windows below are federal defaults used only when the letter shows none. The app labels them "usual deadline, check your letter". `AppealView.swift` already follows this rule.

| Plan type | Level 1 (file within) | Plan decides within | Level 2 (file within) | Source |
| --- | --- | --- | --- | --- |
| ACA individual / marketplace | Internal appeal: 180 days from the denial notice | 30 days pre-service · 60 days post-service · 72 hours urgent | External review: 4 months after the final denial; urgent cases can go straight to external review | [HealthCare.gov internal appeals](https://www.healthcare.gov/appeal-insurance-company-decision/internal-appeals), [external review](https://www.healthcare.gov/how-do-i-appeal-a-health-insurance-companys-decision/external-review/) |
| Employer plan (ERISA, non-grandfathered) | Internal appeal: 180 days (group plans may have 1 or 2 internal levels) | Same timing as above | External review (federal or state process) | [HHS appeals slides](https://www.hhs.gov/guidance/sites/default/files/hhs-guidance-documents/Internal-Appeals-External-Review-Slides-2022.pdf) |
| Medicare Advantage (Part C) | Plan reconsideration: 65 days from the notice | 30 days pre-service · 60 days payment · 72 hours expedited | The plan must send an upheld case to the IRE automatically | [Medicare.gov](https://www.medicare.gov/providers-services/claims-appeals-complaints/appeals/medicare-health-plans), [CMS IRE](https://www.cms.gov/medicare/appeals-grievances/managed-care/review-part-c-independent-entitiy) |
| Original Medicare | Redetermination: 120 days from the MSN | 60 days | QIC reconsideration: 180 days | [CMS appeals chart](https://cmsnationaltrainingprogram.cms.gov/sites/default/files/shared/Appeals%20Processes_Portrait_FINAL_508.pdf) |
| Medicaid managed care | Plan appeal: 60 days from the adverse benefit determination | Varies by state | State fair hearing: 120 days from the plan's decision | [42 CFR 438.402](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-438/subpart-F/section-438.402), [MACPAC](https://www.macpac.gov/wp-content/uploads/2018/07/Federal-Requirements-and-State-Options-Appeals.pdf) |

**What Medbill already encodes** (`config.py`): `APPEAL_FILING_DAYS = {employer: 180, individual: 180, medicare_advantage: 65}`, `APPEAL_DECISION_DAYS = {pre_service: 30, post_service: 60, urgent: 3}`, `APPEAL_EXTERNAL_REVIEW_DAYS = 120`, and `appeals.deadlines(case)`. ClaimCoach v1 reuses these and adds:

- `original_medicare: 120` and `medicaid: 60` filing windows, plus the second-level windows (QIC 180, fair hearing 120).
- `deadline_source`: `letter` (extracted) or `default` (table). The UI wording depends on it.
- Reminders at 14 days and 3 days before the filing deadline, and on the decision-due date.
- Urgent cases: never a reminder-only flow. The app shows "Ask for an expedited appeal and call your doctor today", and the letter is marked EXPEDITED (already in `appeal_letter.py`).

**Denial reasons** (already in `appeal_letter.DENIAL_REASONS`): medical necessity, prior authorization, out of network, experimental, not a covered benefit, coding error, other. Each has its own argument paragraph, evidence checklist and doctor-request template. Out-of-network emergency care also checks the No Surprises Act angle and can hand off to BillKarma.

**Rules live on the server** in one table (`appeal_rules.py`), each with a source URL and a `verified_on` date, so they can be fixed without an app release.

## Pricing and monetization

Understanding your denial and deadline is free. You pay for the work: the full appeal kit, and optionally for ClaimCoach to send it and run the case. This mirrors BillKarma (free teaser, paid report) and holds up next to free nonprofits.

| Tier | What's included | Starting price | How it's paid |
| --- | --- | --- | --- |
| Free | Denial explained, plan type and appeal level, deadline, evidence checklist, one reminder | $0 | — |
| Appeal kit (per case) | Appeal letter, doctor-request template, phone script, attach-this checklist, all reminders, outcome check-in, external-review letter if upheld | $19.99 | IAP, consumable `cc_appeal_kit` (same pattern as `bk_report_unlock`) |
| Send it for me (add-on) | Fax to the insurer's appeals line and/or certified mail with tracking, proof stored in the case | $9.99–$14.99 | **Open question:** fax and mail are services delivered outside the app, which App Review guideline 3.1.3(e) says must be paid outside IAP. Confirm before shipping (see Research) |
| ClaimCoach Plus (annual) | Unlimited cases for the household for a year | $59.99/yr | IAP auto-renewable, entitlement `plus` |

Prices are starting points, set in App Store Connect and tested later, as in BillKarma.

**Why not the web price?** Medbill's web concierge charges $149, or $299 for denials of $5,000+ (`APPEAL_PRICE_CENTS`). That is a human-reviewed, done-for-you service. The app is self-serve, so it starts at an impulse price. The web concierge can stay as an upsell for big denials, linked from the app once 3.1.3(e) is confirmed.

**One subscription across both apps:** App Store subscriptions belong to one app, so a shared "Karma Plus" for BillKarma and ClaimCoach needs a server-side entitlement tied to Sign in with Apple. Medbill already has `mobile_accounts.py` for this. It's a phase-2 experiment, not v1.

**Unit economics to confirm:** the Gemini cost per case (2–6 pages), the fax cost per page, and the Lob certified-letter cost. At $19.99 after Apple's 15–30% cut, the kit's margin should be fine. Send-it-for-me must be priced above its real mail and fax cost.

## Compliance, privacy and claims language

Denial letters carry diagnoses, treatments and member IDs, which is more sensitive than a hospital bill. ClaimCoach must be private by design and never overpromise.

**Health data rules that apply:**

- **Not HIPAA, but the FTC's Health Breach Notification Rule.** A consumer app is not a HIPAA covered entity. Since July 29, 2024, the [amended rule explicitly covers most health apps](https://www.ftc.gov/node/78112). An unauthorized disclosure, including sharing data with an analytics or ad SDK, counts as a breach that must be reported to users and the FTC.
  - Consequence: keep BillKarma's rule of **no third-party analytics or ad SDKs**. First-party events only, with no health content in event properties.
- **State health privacy laws** (e.g. Washington's My Health My Data Act, California's CMIA and CCPA): require consent before collecting health data and give users a deletion right. To confirm with a lawyer; see Research.
- **Apple:** `PrivacyInfo.xcprivacy` declares Health and Sensitive Info for App Functionality, no tracking. Apple's App Review health-data rules (5.1.3) bar using health data for ads or selling it.

**Data handling (same as BillKarma B8, tightened):**

- Images go only to the backend, are stored as private uploads (`private_uploads.py`), and are deleted after extraction unless the user opts to keep them in the case for sending.
- Retention: case data purged on a fixed window after the case closes (reuse `compliance.purge_old_data`); "Delete my data" removes everything server-side.
- Call notes and anything the user types about their health stay on the device unless it's needed in the letter.
- The Medbill repo is **public**. Before ClaimCoach code lands there, check that no secrets, sample patient data or private prompts are committed, or make it private (see Research).

**Claims language (copy rules):**

- Never: "We'll get your claim paid", "guaranteed", "win rate", "overturn your denial".
- Always: "ClaimCoach helps you write and send an appeal. Your insurer makes the decision."
- Not legal or medical advice; we don't speak to the insurer for you (except sending what you approved).
- Deadline copy: when the date is ours, say "usual deadline, check your letter". Never present a default as the user's real deadline.
- The user reads and approves every letter before it is sent (as `appeal_letter.py` already states).
- Free nonprofit help exists. Settings links to the state Consumer Assistance Program, which is honest and builds trust.

**Unauthorized practice of law:** letter generation that is self-help and user-approved is generally treated differently from representation. Confirm with a lawyer before offering send-it-for-me, and before acting as an authorized representative.

## Technical design

Two codebases, as with BillKarma: a new SwiftUI app in a new repo, and new routes in the existing Medbill backend. No new backend service, database or vendor.

| Part | Repo | Stack | What changes |
| --- | --- | --- | --- |
| A. Backend | `nitantbhartia/Medbill` (existing) | FastAPI, SQLite, Gemini 2.5 Flash, Lob, fax, Railway | New `cc_*` modules and a `/api/cc` router; new tables; reuse appeal, auth, purchase and upload code |
| B. iOS app | `claimcoach-ios` (new) | SwiftUI, iOS 17+, RevenueCat only | Fork of `billkarma-ios`: keep Design, Networking, Storage, Purchases, Scan; new Features |

**Why share the backend instead of a new project:** Medbill already holds the appeal engine, device tokens, RevenueCat webhooks, private uploads, Lob and fax, the Gemini extraction with self-checks, compliance purges and the accuracy gate. A second backend would copy all of that and drift. If you want a separate Railway project for billing or isolation, deploy the same repo twice with `APP_MODE=claimcoach` instead of forking it.

**Backend reuse map (Medbill):**

| Module | Reuse as is | Change for ClaimCoach |
| --- | --- | --- |
| `mobile_auth.py`, `mobile_accounts.py` | Device tokens, Sign in with Apple accounts | Add an `app` column (`billkarma`/`claimcoach`) on devices |
| `mobile_purchases.py`, `mobile_purchase_routes.py` | RevenueCat verify + webhook, idempotent unlocks | New product IDs; unlock a `case_id` instead of a `bill_id` |
| `appeal_letter.py` | Plan types, service timings, 7 denial reasons, argument paragraphs, expedited header | Add the Medicare/Medicaid wording, external-review letter, doctor-request template |
| `appeals.py` | Case states, `deadlines()`, `mail_by_lob`, `record_sent`, `record_outcome` | Split web-only parts (Stripe, email links) from case logic; add `deadline_source` |
| `fax.py`, `debt_fighter.send_certified_letter` | Fax and certified mail | Wrap in `cc_send.py`; store proof in the case |
| `scanner.py`, `extraction_selfcheck.py` | Gemini vision call, multi-page, self-check | New denial-letter schema and prompt (`cc_extract.py`) |
| `private_uploads.py`, `compliance.py` | Private image storage, purge, delete-my-data | Include `cc_cases` in purge and delete |
| `insurance_check.py`, `eob_observations.py` | EOB reading | Optional EOB on a case for the claim and amount details |
| `reply_reader.py` | Reads replies (built for hospital replies) | Later: read the insurer's decision letter to fill in the outcome |
| `guide_insurance_denial_appeal*.py`, `guide_prior_authorization.py`, `guide_appeal_denial.py` | Existing SEO guides | Add "Get the app" banners (smart app banner, as A7) |

**iOS reuse map (billkarma-ios):**

| Folder / file | Reuse | Change |
| --- | --- | --- |
| `Design/*` (Theme, Typography, Paper, Highlight, Buttons, Lists, Overlays, Haptics, Selection) | Whole folder | Nothing, except a `DeadlineBlock` variant of `Highlight` |
| `Networking/*`, `Storage/Keychain.swift`, `Purchases/PurchaseService.swift`, `Analytics/` | Whole | Base path `/api/cc`; product IDs; event names |
| `Features/Scan/*` (DocumentScanner, ImagePrep, ScanSourceButtons, ProcessingView) | Whole | Copy for denial letters; tips for finding the denial letter |
| `Features/Onboarding/*` | Components (SingleChoiceStep, MultiChoiceStep, TrustView, OnboardingPaper) | New 3-question flow and copy |
| `Features/Paywall/*` | PaywallScreen, ExitOfferSheet | New copy: personalized with the denial reason and deadline |
| `Features/Letter/*` (LetterPreview, LetterPDF, SendItView, ActivityView, HoldCallViews) | Whole | Recipient is the insurer's appeals address/fax |
| `Features/Results/AppealView.swift` | The `DenialReason` enum and on-device wording | Superseded by server-built letters; keep as offline fallback |
| `App/Features.swift` flags, `NotificationRouter` | Whole | Deadline and decision-due reminders |

```
ClaimCoach iOS (new repo claimcoach-ios) ──HTTPS /api/cc──►┐
BillKarma iOS ─────────────────────────────HTTPS /api/m──► │
                                                           ▼
            ┌──────────── Medbill backend (FastAPI) ────────────┐
            │ /api/cc router            NEW  → cases, unlock, send│
            │ Appeal engine             REUSE (appeals, appeal_letter) ──► Lob mail + fax → insurer
            │ Denial reader + rules     NEW  (cc_extract, appeal_rules) ──► Gemini 2.5 Flash
            │ Auth, purchases, uploads  REUSE (mobile_*, uploads) ──► RevenueCat
            │ SQLite                    NEW cc_cases + existing tables │
            └─────────────────────────────────────────────────────┘
```

ClaimCoach and BillKarma call the same Medbill service on different routers; only the router, the denial reader and the rules are new.

## AI pipeline

The AI only reads and classifies. Deadlines, routing and the letter's legal wording come from rules and templates on the server, so the model can't invent a deadline or a right.

1. **Extract** (`cc_extract.py`, Gemini 2.5 Flash vision, the same call as `scanner.py`): one JSON object per denial letter, extracting only what's printed.
   - `insurer_name`, `plan_name`, `member_id`, `claim_number`, `group_number`
   - `patient_name`, `provider_name`, `service_description`, `service_date`, `codes[]` (CPT/HCPCS/ICD-10 if printed)
   - `amount_billed`, `amount_denied`
   - `notice_date`, `printed_appeal_deadline` (date or "within N days" text), `appeal_address`, `appeal_fax`, `appeal_phone`
   - `denial_reason_text` (verbatim, under 300 characters), `denial_codes[]` (e.g. CARC/RARC on an EOB), `criteria_cited` (guideline named, if any)
   - `plan_type_signals`: words like "ERISA", "Medicare Advantage", "Medicaid", "Marketplace", "IRE", "fair hearing"
   - `urgent_signals`, `is_prior_auth` (pre-service wording)
   - `page_confidence` per field
2. **Self-check** (reuse `extraction_selfcheck.py`): dates parse, the deadline is after the notice date, the claim number appears in the image text. Low-confidence fields go to the confirm screen highlighted.
3. **Classify** (rules first, model second): map `denial_reason_text` to one of the 7 `DENIAL_REASONS`; map `plan_type_signals` plus the user's onboarding answer to a plan type. Disagreements are asked, not resolved silently.
4. **Route** (`appeal_rules.py`, no AI): plan type + timing → level, deadline (letter or default, with `deadline_source`), decision window, where to send.
5. **Explain** (template + short model rewrite): the free "your denial, explained" text. The model may only rephrase the denial reason in plain English (≤ 2 sentences); everything else is template.
6. **Write** (`appeal_letter.build_appeal_letter`): the existing templates, plus one optional model-written paragraph that ties the user's own facts to the denial reason. That paragraph:
   - may only use facts from the extraction and the user's answers;
   - can't cite studies, guidelines or laws (the templates do that, with sources);
   - is shown highlighted in the preview as "Written for your case, check it".
7. **Golden set and accuracy gate:** 30 real, redacted denial letters across the 5 plan types and 7 reasons (collect via research interviews and the BillKarma audience, with consent). Extraction must hit ≥ 95% on claim number, notice date and printed deadline before launch. Wire it into Medbill's existing `accuracy_gate.py`, which already runs on Railway pre-deploy.

**Model choice:** stay on Gemini 2.5 Flash for parity and cost. Swap only if the golden set fails. The prompt and schema version are stored on every case so changes can be audited.

## Data model and API

One new case table holds each appeal; everything else reuses BillKarma's mobile tables. Follow Medbill's `CLAUDE.md` exactly: raw parameterized SQL in a new numbered SQL file, files under 300 lines, constants in `config.py`, responses as `{"status": "ok", "data": ...}`.

```sql
ALTER TABLE mobile_devices ADD COLUMN app TEXT NOT NULL DEFAULT 'billkarma';

CREATE TABLE IF NOT EXISTS cc_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT NOT NULL,
    for_whom TEXT NOT NULL DEFAULT 'self',          -- self | someone_else
    plan_type TEXT,                                 -- employer | individual | medicare_advantage | original_medicare | medicaid | other
    service_timing TEXT,                            -- post_service | pre_service | urgent
    denial_reason TEXT,                             -- key in appeal_letter.DENIAL_REASONS
    level TEXT NOT NULL DEFAULT 'internal',         -- internal | external | ire | qic | fair_hearing
    extracted_json TEXT,                            -- cc_extract output (no images)
    schema_version TEXT,
    notice_date DATE,
    file_by DATE,
    deadline_source TEXT,                           -- letter | default
    status TEXT NOT NULL DEFAULT 'draft',           -- draft | ready | sent | decided | closed
    sent_at TIMESTAMP, sent_channel TEXT,           -- fax | mail | self
    decision_due DATE,
    outcome TEXT,                                   -- overturned | partial | upheld
    amount_denied REAL, amount_recovered REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_cc_cases_device ON cc_cases(device_id, created_at);

CREATE TABLE IF NOT EXISTS cc_case_unlocks (
    case_id INTEGER NOT NULL,
    source TEXT NOT NULL UNIQUE,                    -- iap:<transaction_id> | plus:<device_id>:<case_id>
    product_id TEXT, status TEXT NOT NULL DEFAULT 'paid',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cc_sends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL, channel TEXT NOT NULL,  -- fax | mail
    provider_ref TEXT, tracking_number TEXT, status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Routes** (`cc_routes.py`, `APIRouter(prefix="/api/cc")`; every route except `/device` needs `device_from_request`):

| Method & path | Request | Response `data` | Notes |
| --- | --- | --- | --- |
| `POST /device` | `{app_version}` | `{device_id, token}` | Reuses `mobile_auth.register_device`, sets `app='claimcoach'` |
| `POST /cases` | multipart `pages[]`, optional `eob_pages[]`, `for_whom`, `plan_type`, `service_timing` | `CaseView` | Extract → self-check → classify → route; rate-limited per device |
| `PATCH /cases/{id}` | Confirmed fields from the confirm screen | `CaseView` | Re-routes the deadline if dates or plan type change |
| `GET /cases`, `GET /cases/{id}` | — | `{cases: [CaseSummary]}` / `CaseView` | 403 if not the device's case |
| `POST /cases/{id}/unlock` | `{transaction_id}` or `{}` for Plus | `CaseView` | Same RevenueCat verification as A6; 409 on a reused transaction |
| `POST /cases/{id}/letter` | `{name, member_id, extra_facts}` | `{letter_text, doctor_request, checklist, phone_script}` | 402 while locked |
| `POST /cases/{id}/send` | `{channel, to, approved_text_hash}` | `{send_id, status}` | Only sends the exact text the user approved; see the 3.1.3(e) question |
| `POST /cases/{id}/sent` | `{channel: self, date}` | `CaseView` | When the user sent it themselves |
| `POST /cases/{id}/outcome` | `{outcome, amount_recovered}` | `CaseView` (with next level if upheld) | Starts the external-review / IRE step |
| `DELETE /cases/{id}`, `DELETE /device` | — | `{deleted: true}` | Removes cases, uploads, sends |
| `POST /events`, `POST /revenuecat/webhook` | as BillKarma |  | Reuse; new event-name set |

**`CaseView`** is the one model the app renders: `{case_id, locked, summary: {insurer, service, amount_denied, reason_label, plain_reason}, route: {plan_type, level, file_by, deadline_source, decision_window_days, send_to}, evidence_checklist[], letter: null|{...}, timeline: [...], next_step}`. Like BillKarma, a locked view never contains the letter text.

## Marketing and launch

ClaimCoach launches into BillKarma's audience, not a new one. Every channel BillKarma has gets a denial angle, and the two apps point to each other.

**Before building (validation, free):**

- Post 3–5 denial stories from the billkarmaapp accounts, in the same visual theme as the BillKarma videos. Hooks to test: "Your insurer denied it. Fewer than 1 in 100 people appeal." / "The deadline is on the letter. Most people never see it." / "Denied as 'not medically necessary'? Here's what that actually means."
- A waitlist page at claimcoach.app (already owned): "Scan your denial letter, get your deadline", with an email signup. Count signups per video.
- A Reddit pass on r/HealthInsurance and similar, answering denial questions the way the app would (no links until it's allowed).

**Launch:**

- **Cross-promotion:** BillKarma shows a "Was your claim denied?" row on Scan home (replacing the hidden `denialAppeal` flag) that opens ClaimCoach in the App Store. ClaimCoach does the same for "Got a bill you think is wrong?".
- **SEO:** Medbill already ranks guides on denials and prior authorization (`guide_insurance_denial_appeal.py`, `guide_insurance_claim_denied.py`, `guide_insurance_prior_auth_denied.py`, `guide_appeal_denial.py`). Add the smart app banner and an "Open in ClaimCoach" CTA, and point claimcoach.app's pages at the same guides.
- **App Store:** title "ClaimCoach: Appeal a Denial"; screenshots in BillKarma's style: "Scan the denial" / "See why, in plain English" / "Know your deadline" / "Send your appeal" / "Know what's next".
- **Share card:** after sending, "I appealed my denial. Check your deadline free: claimcoach.app" (no health details, ever).

**Content engine:** the BillKarma video playbook (one consistent theme, story-driven, voiceover, no face on camera) carries over unchanged. Denials add a recurring series: "Denial of the week", explaining one real (permissioned, anonymized) denial reason and the counter-argument.

## Metrics and success gates

Three gates decide whether to build, keep investing or fold it into BillKarma. The targets are starting guesses; replace them with BillKarma's real funnel numbers once those exist.

| Gate | When | Pass if | If it fails |
| --- | --- | --- | --- |
| 1. Build | After 3–5 denial videos | Denial videos beat the median BillKarma video on views or saves, **and** 50+ waitlist signups | Keep it as the BillKarma `denialAppeal` feature; don't build a second app |
| 2. Launch quality | Before submission | Golden set: ≥ 95% on claim number, notice date, printed deadline; 0 wrong-deadline cases | Fix extraction; don't ship |
| 3. Keep investing | 60 days after launch | Scan → explained ≥ 70%; explained → paid ≥ 8%; ≥ 20% of paid cases sent within 7 days | Rework the paywall and free tier, then re-test for 30 days |

**Events** (first-party only, no health content in properties): `onboarding_completed`, `case_scan_started`, `case_scan_succeeded {pages, deadline_source}`, `case_confirmed {fields_edited}`, `explained_viewed {plan_type, reason}`, `paywall_viewed`, `purchase_completed {product}`, `letter_viewed`, `letter_sent {channel}`, `reminder_scheduled`, `outcome_reported {outcome}`, `next_level_started`, `crosspromo_tapped {to}`.

**North star:** appeals sent on time per week. Outcome check-ins (overturned / partly / upheld) become ClaimCoach's data moat over time, by insurer and by reason, like BillKarma's verified outcomes.

## Research still needed

These are the open questions to settle before or during the build. The first four can block launch.

- [ ] **App Store payment for send-it-for-me.** Does fax or certified mail fall under guideline 3.1.3(e), so it must be paid outside IAP (Stripe/Apple Pay)? Read the current guideline text and ask App Review through a pre-submission question. Fallback: v1 ships with "share the PDF" only.
- [ ] **Legal review (1 hour with a health-law attorney).** Unauthorized practice of law for generated letters and for sending on the user's behalf; acting as an authorized representative; the FTC Health Breach Notification Rule duties; Washington MHMDA and California CMIA consent wording.
- [ ] **Medbill repo visibility.** The repo is public. Audit it for secrets, prompts and sample data, and decide whether to make it private before adding ClaimCoach code.
- [ ] **Golden set of 30 denial letters.** Source them (with consent, redacted) from BillKarma users, Reddit volunteers and public samples. Cover 5 plan types × the top reasons.
- [ ] **Employer-plan detail.** ERISA group plans can have two internal levels and different external-review routes (federal vs state). Confirm how to detect which applies from the letter, and the wording when it can't.
- [ ] **State external review.** Which states run their own process and what their forms are; start with CA (DMHC vs CDI), TX, FL and NY.
- [ ] **Medicare and Medicaid letters.** Whether to use the official CMS redetermination form and state fair-hearing forms instead of a letter (v1.1).
- [ ] **Competitors, hands-on.** Use Counterforce, Fight Health Insurance and Claimable with one sample denial. Note price, time to letter, and what happens after the letter.
- [ ] **User interviews (5–8).** People with a recent denial: what they did, why they stopped, what they'd pay for. Recruit from the BillKarma audience.
- [ ] **Unit costs.** Gemini cost per case; fax cost per page (current `fax.py` provider); Lob certified letter cost.
- [ ] **Cross-app subscription.** Whether a shared Plus via Sign in with Apple + server entitlements passes App Review, and how RevenueCat models two apps in one project.
- [ ] **Name and trademark.** A USPTO search for "ClaimCoach" in software / insurance classes, and App Store name availability.
- [ ] **CARC/RARC codes.** Whether to use the public denial-reason code lists on EOBs to classify reasons more reliably.

## Milestones and build plan

Phase 0 is research and runs now; the build itself is about four weeks of evenings at your BillKarma pace, and only starts once the build gate passes.

| Phase | Target | What |
| --- | --- | --- |
| 0. Validate | Weeks 1–3 | 3–5 denial videos, claimcoach.app waitlist, 5–8 interviews, legal and 3.1.3(e) questions, golden-set sourcing |
| ◆ Build gate | | Denial videos beat the BillKarma median and 50+ waitlist signups |
| 1. Backend (Medbill) | Week 4 | cc_extract schema, appeal_rules.py, cc_cases tables, /api/cc routes, unlocks, accuracy gate on 30 letters |
| 2. iOS core (claimcoach-ios) | Week 5 | Fork billkarma-ios; onboarding, scan, confirm, Your denial explained, paywall, letter and PDF |
| 3. Send and track | Week 6 | Share, fax and mail sends; case timeline; reminders; outcome check-in; external review / IRE step |
| ◆ Launch gate | | ≥ 95% on the golden set and zero wrong-deadline cases |
| 4. Launch | Week 7 | App Store assets, cross-promo row in BillKarma, smart app banners on denial guides, launch videos |
| ◆ 60-day gate | | Explained → paid ≥ 8% and 20%+ of paid cases sent within 7 days |

Weeks are targets, not commitments. As with BillKarma, write the build as a guide in the new repo (`docs/cc-guide.md`, from this doc) and run Claude Code phase by phase, with acceptance checks per phase:

1. **Backend:** "Read docs/cc-guide.md sections Appeal rules, AI pipeline and Data model. In Medbill, add `appeal_rules.py`, `cc_extract.py`, the `cc_*` tables and `cc_routes.py`, reusing `appeals.py`, `appeal_letter.py`, `mobile_auth.py` and `mobile_purchases.py`. Add tests and wire the golden set into `accuracy_gate.py`." ✅ Done when all tests pass, the golden set scores ≥ 95%, and a locked `CaseView` contains no letter text.
2. **iOS core:** "Fork billkarma-ios into claimcoach-ios. Keep Design, Networking, Storage, Purchases and Scan. Build screens 1–8 from the mockups." ✅ Done when a sample denial goes scan → explained → paywall (test store) → letter PDF.
3. **Send and track:** screens 9–12, reminders and outcomes. ✅ Done when sending moves the case to Sent, sets the decision-due reminder, and an upheld outcome opens the next level with its own deadline.
4. **Launch:** App Store assets, the cross-promo row in BillKarma, smart banners on the denial guides.
