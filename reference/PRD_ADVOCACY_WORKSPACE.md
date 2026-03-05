# Advocacy Workspace: Engineering PRD v1

**Date:** 2026-03-05
**Status:** Draft for review
**Scope:** What to build, what to reuse, what to cut, and in what order.

---

## 1. Product Thesis

Advocacy groups (nonprofit patient advocates handling insurance denials and hospital billing disputes) spend 30-90 min/case on manual work: interpreting bills, deciding actions, drafting letters, tracking status. BillKarma already has the analysis engine + letter generators. The Advocacy Workspace wraps these in a multi-case management UI so advocates can process cases in minutes instead of hours.

**ICP for v1:** Nonprofit patient advocacy orgs handling insurance denials and hospital billing disputes. 20-200 cases/month. 1-5 advocates per org. Not billing companies, not law firms, not health systems.

---

## 2. Reuse Map: What Exists vs. What's New

### Already Built (Reuse directly)

| PRD Feature | Existing Code | Notes |
|---|---|---|
| OCR extraction (bills, EOBs) | `scanner.py` — Gemini 2.5 Flash extraction with preprocessing, ensemble mode, reconciliation | Handles PDF/JPG/PNG, extracts line items, CPT codes, amounts, provider info. Already supports EOB merge via `analyzer.merge_eob_into_extracted()` |
| Bill analysis (8 rule types) | `analyzer.py` + `validators/` — duplicates, pricing markup, NCCI unbundling, upcoding, NSA, EOB reconciliation, benchmarks, quantity flags | Each finding has type, severity, confidence, evidence_json, potential_savings. Already deterministic rules + structured output |
| Hospital dispute letter | `dispute_workflow.build_dispute_letter()` | Finding-type-specific paragraphs (duplicate, unbundling, upcoding, pricing). References Medicare rates, CMS guidelines |
| Insurance appeal letter | `dispute_workflow.build_appeal_letter()` | Lists disputed charges with amounts, references policy rights, requests re-review |
| Debt validation letter | `debt_fighter.py` — `LETTER_TYPES["debt_validation"]` | Full FDCPA-compliant letter with legal basis, timeline, educational content |
| Charity care letter | `debt_fighter.py` — charity care eligibility + letter generation | FPL calculations, nonprofit hospital detection via `hospital_financials` table, financial assistance URLs |
| Phone scripts | `dispute_workflow.build_phone_script()` | Structured call scripts with talking points per finding |
| Medicare rate lookups | `validators/pricing.py` — `get_medicare_rate()`, locality mapping | 2026 OPPS rates, locality-aware, facility vs non-facility |
| CPT enrichment | `enrichment.py` | Provider name normalization, facility matching |
| Compliance/audit | `compliance.py` — `record_consent()`, `log_audit()`, `export_bill_data()`, `delete_bill_data()` | GDPR-style consent, audit logging, data export/deletion already built |
| Dispute case management | `dispute_service.py` + `dispute_cases` table | Case creation, status tracking, followup scheduling. Currently tied to paid disputes |
| Evidence uploads | `evidence_uploads` table + upload handling in `api.py` | Multi-doc per bill, stores file data |
| Session access control | `access_control.py` | Cookie-based session binding to bills |

### Must Build New

| Feature | Effort | Why it can't be reused |
|---|---|---|
| **Auth system** (email+password or magic link) | Large | Current app has no login. Session cookies won't work for multi-user orgs |
| **Org + team model** (org creation, member invite, roles) | Medium | No concept of organizations exists |
| **Advocacy case wrapper** | Medium | Existing `dispute_cases` is payment-gated and consumer-only. Need a new `advocacy_cases` entity that wraps a bill + org ownership + status workflow without requiring payment |
| **Case dashboard UI** | Medium | No multi-case list view exists. Need table with filters, status, assignee |
| **Case detail page** | Medium | Existing results page is consumer-facing. Need advocate-oriented layout with docs, analysis, letters, notes sections |
| **Letter editor + PDF export** | Small-Medium | Existing letters are generated as plain text strings. Need an editable draft view + PDF render |
| **Advocate override fields** | Small | Need to store advocate-entered values separately from OCR extraction, with "prefer override > extracted" logic |
| **Consent attestation** | Small | Checkbox: "I have patient consent to upload these documents" |

### Cut from v1 (Do later)

| Feature | Why cut | When |
|---|---|---|
| Share links (FR-25) | Nice-to-have, not core workflow | v1.1 |
| Activity timeline auto-logging (FR-26/27) | Can add retroactively; advocates won't miss it in week 1 | v1.1 |
| Viewer role | Just Admin + Advocate for now; Viewer adds permission complexity | v1.1 |
| Letter version history | Just "last saved" for now | v1.1 |
| Bulk case operations | Single-case flow first; bulk is optimization | v1.1 |
| Tone options (neutral/firm) | One good default tone is fine | v1.1 |
| DOCX export | PDF + copy text covers 95% of use | v1.1 |
| Template library view | Advocates pick letter type in-context, not from a library | v1.1 |
| Dashboard filter persistence | Filters reset on page load is fine for MVP | v1.1 |
| Confidence badges on recommendations | Hard to calibrate without outcome data. Show evidence instead | v1.1 (after outcome data exists) |

---

## 3. ICP Narrowing

**v1 serves one persona:** Nonprofit patient advocates handling insurance denials and hospital billing disputes.

This means:
- Letter templates optimized for: insurance appeals, hospital disputes, charity care requests, debt validation
- UX language assumes advocate is acting on behalf of patient (not self-service)
- No billing company features (no batch import, no API access, no white-labeling)
- No law firm features (no attorney-client privilege handling, no litigation tracking)

Consumer flow continues unchanged. Advocacy Workspace is a separate mode behind the workspace switcher.

---

## 4. Data Model (Concrete Schema)

### New Tables

```sql
-- Organizations
CREATE TABLE IF NOT EXISTS organizations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_email TEXT NOT NULL,
    org_type TEXT NOT NULL DEFAULT 'nonprofit',  -- nonprofit, community, other
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Org membership
CREATE TABLE IF NOT EXISTS org_members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    org_id INTEGER NOT NULL REFERENCES organizations(id),
    user_id INTEGER NOT NULL REFERENCES users(id),
    role TEXT NOT NULL DEFAULT 'advocate',  -- admin, advocate
    invited_by INTEGER REFERENCES users(id),
    status TEXT NOT NULL DEFAULT 'active',  -- active, invited, deactivated
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(org_id, user_id)
);
CREATE INDEX IF NOT EXISTS idx_org_members_org ON org_members(org_id);
CREATE INDEX IF NOT EXISTS idx_org_members_user ON org_members(user_id);

-- Advocacy cases (wraps a bill with org context)
CREATE TABLE IF NOT EXISTS advocacy_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    org_id INTEGER NOT NULL REFERENCES organizations(id),
    bill_id INTEGER REFERENCES bills(id),
    patient_label TEXT NOT NULL,            -- alias, not necessarily legal name
    title TEXT,                             -- auto: "{patient_label} - {provider} - {DOS}"
    assigned_to INTEGER REFERENCES users(id),
    created_by INTEGER NOT NULL REFERENCES users(id),
    status TEXT NOT NULL DEFAULT 'new',     -- new, docs_uploaded, analyzed, letter_generated, sent, awaiting_response, resolved, closed
    hospital_name TEXT,
    insurance_carrier TEXT,
    date_of_service DATE,
    bill_amount REAL,
    notes TEXT,
    tags TEXT,                              -- comma-separated
    patient_consent INTEGER DEFAULT 0,      -- advocate attested consent
    outcome TEXT,                           -- resolved_reduced, resolved_forgiven, resolved_denied, unknown
    outcome_amount REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_advocacy_cases_org ON advocacy_cases(org_id);
CREATE INDEX IF NOT EXISTS idx_advocacy_cases_status ON advocacy_cases(status);
CREATE INDEX IF NOT EXISTS idx_advocacy_cases_assigned ON advocacy_cases(assigned_to);

-- Case documents (multiple per case, typed)
CREATE TABLE IF NOT EXISTS case_documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL REFERENCES advocacy_cases(id),
    doc_type TEXT NOT NULL DEFAULT 'other',  -- hospital_bill, eob, denial_letter, itemized_bill, other
    filename TEXT NOT NULL,
    file_data BLOB NOT NULL,
    mime_type TEXT,
    file_size_bytes INTEGER,
    extraction_status TEXT DEFAULT 'pending',  -- pending, extracted, failed
    extracted_json TEXT,                        -- raw extraction result
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_case_docs_case ON case_documents(case_id);

-- Advocate field overrides (prefer these over extracted values)
CREATE TABLE IF NOT EXISTS case_overrides (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL REFERENCES advocacy_cases(id),
    field_name TEXT NOT NULL,               -- total_charged, patient_responsibility, dos, claim_number, etc.
    field_value TEXT NOT NULL,
    set_by INTEGER NOT NULL REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(case_id, field_name)
);

-- Generated letters
CREATE TABLE IF NOT EXISTS case_letters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL REFERENCES advocacy_cases(id),
    letter_type TEXT NOT NULL,              -- insurance_appeal, hospital_dispute, charity_care, debt_validation
    input_fields TEXT,                      -- JSON of fields used to generate
    content TEXT NOT NULL,                  -- letter text (editable)
    generated_by INTEGER NOT NULL REFERENCES users(id),
    marked_sent INTEGER DEFAULT 0,
    sent_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_case_letters_case ON case_letters(case_id);

-- Case notes (manual, replaces full activity timeline in v1)
CREATE TABLE IF NOT EXISTS case_notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL REFERENCES advocacy_cases(id),
    author_id INTEGER NOT NULL REFERENCES users(id),
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_case_notes_case ON case_notes(case_id);
```

### Modified Tables

```sql
-- users: add password_hash and name for auth
ALTER TABLE users ADD COLUMN name TEXT;
ALTER TABLE users ADD COLUMN password_hash TEXT;
```

### Key Design Decisions

1. **One case = one bill for v1.** A case wraps a single `bills` record. Multiple docs can be uploaded to a case, but they all contribute to one bill extraction + analysis. If an advocate has multiple providers, they create multiple cases.

2. **Overrides stored separately.** `case_overrides` stores advocate corrections. Analysis logic checks overrides first, falls back to extracted values. This preserves the original extraction for audit.

3. **Letters are editable text.** Generated once, stored as text, editable in-place. No version history in v1 — just last saved content.

4. **No payment gate.** Unlike `dispute_cases` which requires Stripe payment, `advocacy_cases` are free to create. Monetization for advocacy orgs is per-seat or per-org (decided separately).

---

## 5. AI Output Quality Bar

Per reviewer feedback: every recommendation must be traceable to specific extracted fields/doc snippets, not pure LLM reasoning.

### Rules

1. **Recommendations are deterministic rules, not LLM output.** The existing `analyzer.py` already does this: 8 rule types with structured evidence. The recommendation engine maps finding types to letter types:
   - Duplicate/unbundling/upcoding/markup findings → "Generate hospital dispute letter"
   - Denial detected in EOB → "Generate insurance appeal letter"
   - Nonprofit hospital + high bill → "Generate charity care request"
   - Collection notice → "Generate debt validation letter"
   - No findings but high bill → "Request itemized bill"

2. **Every recommendation shows evidence.** For each recommended action, display:
   - Which document(s) the data came from
   - Which extracted fields triggered the recommendation
   - What the rule checked (e.g., "CPT 99285 charged $4,200 vs Medicare rate $512 = 8.2x markup")

3. **"Unknown" over guesses.** If a field can't be extracted, show "Not detected — enter manually" instead of guessing. Never fabricate claim numbers, policy numbers, or amounts.

4. **Extraction failure is visible.** If OCR fails or returns low-quality results, show a clear warning: "We couldn't reliably read this document. Please enter key fields manually or upload a clearer image."

5. **Discrepancy detection.** If bill and EOB show different amounts (already handled by `validators/eob.py`), surface this as a finding: "Bill total differs from EOB — recommend requesting corrected bill."

---

## 6. Status Workflow

### Auto-advance (system sets these)

- `new` → `docs_uploaded`: when first document is uploaded to case
- `docs_uploaded` → `analyzed`: when analysis completes successfully
- `analyzed` → `letter_generated`: when first letter is generated

### Manual-only (advocate sets these)

- `sent`: advocate marks letter as sent + enters date
- `awaiting_response`: advocate marks after sending
- `resolved`: advocate marks with outcome (reduced/forgiven/denied/unknown) + optional outcome amount
- `closed`: advocate marks when no further action needed

### Addition per reviewer: `human_reviewed` flag

Add a boolean `reviewed` flag on `case_letters` (not a case status). This lets teams track which letters have been QA'd before sending:

```sql
ALTER TABLE case_letters ADD COLUMN reviewed INTEGER DEFAULT 0;
ALTER TABLE case_letters ADD COLUMN reviewed_by INTEGER REFERENCES users(id);
```

---

## 7. Auth Approach

**Recommendation: Email + password for v1.** Simplest to build, no third-party dependency.

- `POST /api/auth/register` — email, password, name
- `POST /api/auth/login` — email, password → set session cookie
- `POST /api/auth/logout` — clear session
- Password hashed with `bcrypt` (or `argon2` if already in deps)
- Session stored in DB (replace current anonymous session with authenticated session)
- Existing consumer flow continues to work without login (session cookie as before)
- Advocacy workspace requires login

### Team Invites (v1 — simple)

- Admin enters email → system creates `org_members` row with status `invited`
- On registration, if email matches an invite, auto-join org
- No invite email in v1 (admin tells the person verbally/Slack). Add email invites in v1.1

---

## 8. Compliance Posture

Per reviewer feedback, define these explicitly:

1. **Consent attestation:** Every case creation requires checkbox: "I attest that I have the patient's consent to upload and analyze these documents on their behalf." Stored in `advocacy_cases.patient_consent` + `consent_logs` table.

2. **Data retention:** Cases and documents retained for 2 years after last activity, then auto-deleted. Configurable per org.

3. **Data export:** Advocates can export all case data (JSON) via existing `compliance.export_bill_data()` pattern. Extend to export full case with documents, analysis, letters.

4. **Data deletion:** Advocates can delete individual cases. Admins can request full org data deletion. Uses existing `compliance.delete_bill_data()` pattern.

5. **Audit access:** All case actions logged via existing `audit_logs` table. Admins can view audit trail per case.

6. **No HIPAA claim.** Product copy and terms state: "BillKarma implements security best practices but is not a HIPAA-covered entity or business associate." If orgs require a BAA, that's a separate enterprise conversation.

---

## 9. Reliability SLOs (MVP)

| Metric | Target | How measured |
|---|---|---|
| Extraction latency (upload → extracted) | < 15s p95 | Timer in `scanner.py` |
| Analysis latency (extracted → findings) | < 3s p95 | Timer in `analyzer.py` |
| Letter generation latency | < 2s p95 | Timer in letter gen functions |
| PDF export success rate | > 99% | Error rate on PDF render |
| Extraction success rate (non-blank result) | > 90% | % uploads with ≥1 extracted field |

---

## 10. Concurrent Edit Handling (v1 — Simple)

Per reviewer feedback on collision handling:

**v1 approach: Last write wins + optimistic locking on letters.**

- Case metadata edits: last write wins. Low collision risk (1-5 advocates per org, different cases).
- Letter edits: add `updated_at` timestamp. On save, check `updated_at` matches what was loaded. If not, show "This letter was edited by someone else. Reload to see changes." Reject the save.

This is sufficient for small teams. Proper collaborative editing is a v2 concern.

---

## 11. Success Metrics

### Primary

| Metric | Target (pilot) | How measured |
|---|---|---|
| Cases created per org per week | ≥ 10 | DB query |
| Median time: docs uploaded → letter generated | < 5 min | Timestamp diff |
| % cases with ≥1 letter generated | > 70% | DB query |

### Secondary (per reviewer additions)

| Metric | Target | How measured |
|---|---|---|
| Weekly active advocates per org | ≥ 2 | Login + action in 7 days |
| Retention: % orgs active in week 4 | > 60% | Activity tracking |
| Letter quality: thumbs up rate | > 80% | In-app feedback |
| % cases with outcome recorded | > 40% | DB query |
| Median cycle time to "sent" | < 24 hours | Status timestamps |
| % cases reaching "awaiting_response" | > 50% | Status tracking |
| Estimated dollar impact captured | Track total | Sum of `outcome_amount` where outcome = resolved_reduced |

---

## 12. Pilot Exit Criteria

### Gate: Pilot → Beta (after 4 weeks with 3-5 orgs)

**Must hit all:**
- ≥ 3 orgs with ≥ 5 cases created
- Median time-to-letter < 10 min (relaxed from 5 min target)
- ≥ 60% of cases have ≥1 letter generated
- No data loss incidents
- Extraction success rate > 85%
- NPS or satisfaction > 6/10 from advocate survey

**If not met:** Iterate for 2 more weeks, re-evaluate. If still not met after 6 weeks total, reconsider product scope.

### Gate: Beta → Public

- ≥ 10 orgs onboarded
- Week 4 retention > 50%
- Extraction + analysis latency within SLO
- Zero P0 bugs open
- Compliance checklist signed off (consent, retention, deletion working)

---

## 13. Build Plan (6-Week Execution)

### Week 1: Auth + Org Foundation

**Eng:**
- Add `password_hash`, `name` columns to `users` table
- Build auth endpoints: register, login, logout
- Build org creation + `org_members` table
- Add `require_auth` middleware for advocacy routes
- Workspace switcher: "Personal" (existing consumer) vs "{Org Name}"

**Design:**
- Login/register screens
- Workspace switcher component
- Case dashboard wireframe

**PM:**
- Finalize pilot org list (3-5 orgs)
- Draft consent attestation copy
- Draft "not legal advice" disclaimer copy

### Week 2: Case CRUD + Doc Upload

**Eng:**
- `advocacy_cases` + `case_documents` + `case_overrides` tables
- Case create/read/update API endpoints
- Doc upload endpoint (reuse existing upload handling, store in `case_documents`)
- Wire uploaded docs to `scanner.py` extraction pipeline
- Handle extraction failure: surface warning, allow manual field entry
- Store extraction results in `case_documents.extracted_json`
- Build `case_overrides` logic: prefer overrides > extracted values

**Design:**
- New Case flow (2-step: info → upload)
- Case detail page layout (sections: overview, documents, analysis, letters, notes)
- Extraction failure state

### Week 3: Analysis + Recommendations

**Eng:**
- Wire case documents to `analyzer.py` analysis pipeline
- Build recommendation engine (deterministic mapping: finding types → letter types)
- Render analysis results on case detail page with evidence tracing
- "Re-run analysis" button
- Auto-advance status: new → docs_uploaded → analyzed
- Build case dashboard: table view with status filter, search by patient label/hospital

**Design:**
- Analysis results card (findings + evidence)
- Recommendation cards with "Why we recommend this" + "Based on" sections
- Dashboard table design

### Week 4: Letter Generation + Editor

**Eng:**
- Adapt existing letter generators to work with advocacy case context:
  - `dispute_workflow.build_dispute_letter()` → hospital dispute
  - `dispute_workflow.build_appeal_letter()` → insurance appeal
  - `debt_fighter.py` charity care → charity care request
  - `debt_fighter.py` debt validation → debt validation letter
- Build letter editor: pre-filled fields form + editable text area
- PDF export (use existing PDF generation or add `weasyprint`/`reportlab`)
- Copy text button
- Store generated letters in `case_letters`
- "Reviewed" checkbox on letters
- Auto-advance: analyzed → letter_generated
- Manual status transitions: sent, awaiting_response, resolved, closed

**Design:**
- Letter type selection (cards)
- Letter editor with field form + draft area
- PDF preview
- Status transition UI

### Week 5: Polish + Integration Testing

**Eng:**
- Team invite flow (simple: admin adds email, user joins on registration)
- Role-based access control (admin vs advocate permissions)
- Case notes (manual notes on case detail page)
- Consent attestation on case creation
- Dashboard: sort by last updated, bill amount; filter by assignee
- Outcome recording on case resolution (outcome type + amount)
- Error handling: OCR failures, missing fields, edge cases
- Optimistic locking on letter edits

**Design:**
- Team management screen (admin only)
- Empty states for dashboard, case detail sections
- Error states and loading states

### Week 6: Testing + Pilot Launch

**Eng:**
- Write tests: case CRUD, doc upload + extraction, analysis, letter gen, auth, access control
- Test with realistic data (sample bills, EOBs, denial letters)
- Performance testing: extraction latency, analysis latency
- Security review: auth, session handling, org scoping, SQL injection
- Deploy behind feature flag
- Onboard first pilot org

**PM:**
- Pilot onboarding materials
- Feedback collection setup (weekly call + in-app thumbs up/down)
- Metrics dashboard setup

---

## 14. Open Decisions (Decide Before Week 1)

| # | Question | Recommendation | Impact if deferred |
|---|---|---|---|
| 1 | Auth method? | Email + password (simplest) | Blocks all advocacy features |
| 2 | One case = one bill? | Yes for v1 | Affects data model; hard to change later |
| 3 | Same analysis as consumer or different? | Same analysis engine, different UI rendering | Low risk either way |
| 4 | Pricing model for advocacy orgs? | Free during pilot, decide after | Need usage tracking from day 1 regardless |
| 5 | PDF library? | `weasyprint` (HTML → PDF) or `reportlab` | Affects letter export quality |
| 6 | Patient consent checkbox wording? | Legal review needed | Can ship with placeholder, update copy |

---

## 15. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Auth system takes longer than 1 week | Medium | Keep it minimal: email+password, no OAuth, no MFA in v1 |
| OCR quality insufficient for advocacy-grade letters | Low | Already tested extensively; ensemble mode available; manual override as fallback |
| Advocates want features we cut (share links, bulk ops) | Medium | Explicit phase communication; weekly feedback loop to prioritize v1.1 |
| Low adoption during pilot | Medium | Tight ICP; onboard orgs we have relationships with; weekly check-ins |
| AI confidence/trust issues | Medium | Deterministic rules, not LLM reasoning. Evidence tracing on every recommendation. "Unknown" defaults |
| Concurrent edit conflicts | Low | Small teams (1-5 people). Optimistic locking on letters. Last-write-wins on case fields |
