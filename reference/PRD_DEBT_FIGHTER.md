# PRD: BillKarma — Medical Debt Fighter Expansion

**Status:** Draft
**Date:** 2026-02-24
**Scope:** Reposition BillKarma from bill-error detection tool to full medical debt fighting platform. Add post-collections features. Keep all existing content and infrastructure.

---

## Problem

Most BillKarma-adjacent users are not upstream (reviewing a bill before paying). They are downstream — already in collections, already panicking, already on Reddit asking "what do I do." The current product has no entry point for them.

The upstream problem (billing errors) is real but quiet. The downstream problem (medical debt in collections) is a hair-on-fire emergency. We serve one, not the other.

---

## Goal

Expand BillKarma to serve users at every stage of the medical bill lifecycle:

| Stage | User state | What they need |
|---|---|---|
| 1. Bill just arrived | Confused, questioning | Bill scanner, error detection (current product) |
| 2. Can't afford to pay | Worried, overwhelmed | Charity care eligibility, payment plan guidance |
| 3. In collections | Panicking, desperate | FDCPA letter, SOL check, settlement guidance |

Single repositioned entry point: *"Got a medical bill or collection notice? We'll help you fight it."*

---

## What We Are NOT Building

Explicitly out of scope to stay legally safe:

- We do **not** negotiate with collectors on the user's behalf
- We do **not** contact hospitals or collectors directly as an agent
- We do **not** promise specific debt reduction outcomes
- We do **not** provide legal advice or act as a debt relief company
- We do **not** take contingency fees based on debt savings
- We do **not** require state debt settlement licensing because we are a self-help document generation tool — the user is always the actor

All generated letters are from the **user**, in the **user's name**, sent via a mailing API as a convenience service. We are the print shop, not the attorney.

---

## Feature 1: FDCPA Debt Validation Letter Generator

### What it does
When a medical debt goes to a collection agency, the consumer has 30 days from first contact to demand written validation of the debt. If the collector cannot produce documentation, they must cease collection and remove the debt from credit reports. Most people don't know this right exists or how to invoke it.

### User flow
1. User lands on `/fight-debt` or `/collection-notice`
2. Uploads photo or PDF of collection notice (or enters fields manually)
3. Gemini OCR extracts: collector name, address, account number, amount, date of first contact
4. User reviews extracted fields, corrects any errors
5. App generates a legally correct FDCPA debt validation letter:
   - Formally disputes the debt
   - Demands itemized documentation of the original charges
   - Invokes FDCPA § 809(b) right to validation
   - Does NOT acknowledge the debt as valid (critical — acknowledgment can reset SOL)
   - Does NOT include partial payment offer
6. User sees preview of the letter with their name and address as sender
7. User pays $19 → Lob API prints and mails via USPS certified mail from user's address
8. User receives USPS tracking number via email
9. App shows 30-day countdown timer and explains what to expect next

### Legal safeguards
- Letter templates reviewed and approved by a licensed consumer attorney before launch
- Clear disclosure on every screen: "This is a self-help document tool, not legal advice. BillKarma is not a law firm."
- If debt date of service is more than 4 years ago, show SOL warning before generating letter
- Letter language must never admit the debt is valid — templates locked, not LLM-generated freeform
- Add "consult an attorney for complex situations" CTA alongside the letter

### Integrations
- **Gemini Vision**: OCR the collection notice → extract fields
- **Lob API**: Print and certified-mail the letter from user's address
- **Stripe**: $19 payment before mailing

### Success metric
Letter sent within 10 minutes of first landing on the page.

---

## Feature 2: Charity Care Eligibility Checker

### What it does
Nonprofit hospitals (the majority of US hospitals) must offer Financial Assistance Programs (FAP) under IRS 501(r) or lose tax-exempt status. Income thresholds are generous — many people earning up to 300–400% of the federal poverty level qualify for full or partial debt forgiveness. Most patients never apply because they don't know it exists or can't find the form.

### User flow
1. User enters: hospital name, state, household size, approximate annual income
2. App checks hospital's nonprofit status (IRS 990 data, already partially in DB)
3. If nonprofit: looks up their published FAP income thresholds
4. Shows: "Based on your household size and income, you likely qualify for [X]% reduction or full forgiveness"
5. Generates a pre-filled charity care application:
   - Uses the hospital's own form where available (scraped/stored)
   - Falls back to a universal application format that hospitals are required to accept
   - Pre-fills name, hospital, account number, household income, size
   - Lists exactly which documents to attach (most recent tax return, 2–3 pay stubs)
6. User downloads the application packet as a PDF
7. App shows where to submit it (address, fax, email) and follow-up timeline

### Free vs. paid
- Checking eligibility: **free** (top of funnel, high discovery value)
- Generating the pre-filled application packet: **$9** or included in subscription

### Data requirements
- Hospital nonprofit status: IRS 990 data (public, updated annually)
- FAP income thresholds: scraped from hospital financial assistance policy pages, stored in DB
- This is the hardest part — start with top 500 hospitals by revenue, expand over time
- For hospitals not in DB: generate a universal application and tell user to call the billing office

### Legal safeguards
- "Eligibility estimate based on published hospital policy. Income thresholds may vary. Apply regardless of estimate — hospitals must review all applications."
- Never say "you will be approved" — say "you appear to qualify based on published guidelines"

---

## Feature 3: Statute of Limitations Calculator

### What it does
Every state has a SOL on medical debt (typically 3–6 years). After expiration, the debt is legally uncollectable via lawsuit. Collectors can still call but have no legal recourse. Many users are paying debts they no longer legally owe out of fear.

### User flow
1. User enters: state, date of last payment or date of service (whichever is later)
2. App looks up SOL for that state (static table, updated annually)
3. Shows: "In [State], the statute of limitations on medical debt is [X] years. Your debt's SOL expires on [date]."
4. If expired: "This debt may no longer be collectible by lawsuit. A collector can still contact you but likely cannot sue. Consider consulting an attorney before making any payment."
5. If active: Shows time remaining and explains what NOT to do (don't make partial payment — can reset SOL in some states)

### Free
No charge. This is top-of-funnel lead gen — every person who checks SOL is a candidate for the FDCPA letter.

### Legal safeguards
- "SOL laws vary and can be complex. This is an estimate based on published state law. Do not rely on this alone — consult an attorney before deciding not to pay a debt."
- Clear list of states where partial payment resets SOL (prominent warning)

---

## Feature 4: Settlement Offer Copilot

### What it does
Collection agencies buy medical debt for 3–7 cents on the dollar. A lump-sum settlement of 20–40% is commonly accepted. Most users don't know this, don't know how to start the conversation, and don't know how to protect themselves when making an offer.

### User flow
1. User enters: original debt amount, what collector is demanding, what they can afford as lump sum
2. App shows: "This debt likely sold for approximately $[X]. Collectors routinely accept 20–40% as a lump-sum settlement."
3. Generates a "Pay for Delete" settlement offer letter:
   - Offers specific lump-sum amount
   - Conditions payment on written confirmation that collector will delete the tradeline from all three credit bureaus
   - Does NOT acknowledge the debt as valid
   - Does NOT waive SOL rights
   - Instructs user to get agreement in writing before sending any payment
4. User downloads the letter to send themselves (email or certified mail)

### Paid
$9 to generate the letter. Free to read the guidance.

### Legal safeguards
- "Pay for Delete" is not guaranteed enforceable — letter templates reviewed by attorney
- "Send this letter yourself. Do not send payment until you have written confirmation."
- "BillKarma is not negotiating this debt. You are negotiating it yourself."
- Prominent warning: "Making any payment may reset the statute of limitations in your state. Check the SOL calculator first."

---

## UX / UI Changes

### Homepage (priority 1)
**Current hero:** "Upload your medical bill. We'll find what you were overcharged."
**New hero:** "Got a medical bill or collection notice you can't handle? We'll help you fight it."

Add three entry points above the fold:
- "I got a collection notice" → FDCPA letter flow
- "I can't afford my bill" → Charity care checker
- "I want to check my bill for errors" → existing bill scanner

Remove the single "upload your bill" CTA as the only option.

### Navigation
Add top-level nav item: **"Fight Debt"** (or "I'm in Collections")
Existing nav: Home, Hospital Directory, Guides, [new] Fight Debt

### `/fight-debt` landing page
Triage page. Three cards:
1. Got a collection notice → FDCPA letter generator
2. Can't afford your bill → Charity care eligibility
3. Want to check if the bill is right → Bill scanner

Each card shows: what it does, how long it takes, what it costs.

### New pages needed
- `/fight-debt` — triage landing page
- `/collection-notice` — FDCPA letter flow
- `/charity-care` — eligibility checker + application generator
- `/statute-of-limitations` — SOL calculator
- `/settle-debt` — settlement copilot

### Existing pages to update
- **Homepage**: New hero, three entry points, keep existing bill scanner below fold
- **`/scan`**: Add contextual link — "Already in collections? Check if the original bill had errors you can dispute"
- **Results page**: Add "This bill went to collections?" CTA if findings are significant

### Design principles for new flows
- **Progress indicator** on every multi-step flow (Step 1 of 3)
- **No dead ends** — every page where we can't help points to the next best option
- **Countdown timers** where legally relevant (30-day FDCPA window shown prominently)
- **Plain language** — every legal term defined inline on first use
- Consistent with existing design system (app.css, base.html)

---

## Legal Infrastructure (do before launch)

1. **Attorney review of all letter templates** — FDCPA letter, settlement offer letter. One-time cost, ~$500–1,500. Worth it.
2. **Updated Terms of Service** — explicitly state we are a document generation tool, not a law firm, not a debt relief company, not a credit repair organization (CROA has specific requirements)
3. **Disclosure on every new page** — "BillKarma is not a law firm. This is not legal advice. You are acting on your own behalf."
4. **No CROA compliance issues** — Credit Repair Organizations Act regulates companies that promise to improve credit. Do not promise credit score improvement. Frame as "collectors may be required to remove the debt from your credit report" not "we will fix your credit"
5. **State-specific SOL data verified** — have attorney verify the state SOL table before launch

---

## Integrations Summary

| Integration | Purpose | When needed |
|---|---|---|
| **Lob API** | Print + certified mail FDCPA letters from user's address | Feature 1 launch |
| **Stripe** | Payments ($19 letter mailing, $9 application generation) | Feature 1 launch |
| **Gemini Vision** | OCR collection notices to extract fields | Feature 1 launch |
| **IRS 990 data** | Hospital nonprofit status lookup | Feature 2 launch |
| **USPS Tracking API** | Email tracking number after Lob sends letter | Feature 1 launch |
| **SendGrid** | Confirmation emails, tracking updates | Feature 1 launch |

---

## What Stays Exactly the Same

- All 63 guides — unchanged, continue driving SEO traffic
- Hospital directory and grading system
- Bill scanner and analysis engine
- Existing dispute letter generator (for billing errors, not collections)
- Pricing benchmarks and Medicare rate lookups
- All existing API endpoints

The guides become the top-of-funnel for the new features. Medical debt guides (statute of limitations, collections, charity care, bankruptcy) now link directly to the relevant tool instead of generic advice.

---

## Build Order

**Week 1:** SOL calculator (static data, no integrations, free — drives immediate SEO and lead gen)
**Week 2:** FDCPA letter generator + Lob integration (core new feature, first revenue)
**Week 3:** Charity care checker (start with top 100 hospitals, eligibility only)
**Week 4:** Homepage reposition + navigation update
**Week 5:** Charity care application generation + settlement copilot
**Ongoing:** Expand hospital charity care database

---

## Updated PRODUCT_CONTEXT.md Language

Add to "What BillKarma Does":
- Generates FDCPA debt validation letters for users to send to collection agencies, mailed certified via USPS
- Checks eligibility for hospital financial assistance programs and generates pre-filled applications
- Calculates statute of limitations on medical debt by state
- Guides users through lump-sum settlement offers with legally protective language

Add to "What BillKarma Does NOT Do":
- BillKarma does **not** contact collection agencies or hospitals on the user's behalf
- BillKarma does **not** act as a debt settlement company or credit repair organization
- BillKarma does **not** guarantee debt reduction, deletion from credit reports, or legal outcomes
- BillKarma does **not** provide legal representation

Add to Approved Language:
- "You have the right to request validation of this debt"
- "Many patients qualify for full or partial forgiveness through hospital financial assistance"
- "This debt may be past the statute of limitations in your state"
- "Collectors often accept lump-sum settlements significantly below the full balance"

Add to Forbidden Language:
- "We will negotiate your debt" → "Here's how to negotiate your debt yourself"
- "Your debt will be removed from your credit" → "The collector may be required to remove it"
- "Guaranteed to work" → never use for any debt-fighting feature
- "Illegal" (about collector behavior) → "This may violate the FDCPA — consult an attorney"
