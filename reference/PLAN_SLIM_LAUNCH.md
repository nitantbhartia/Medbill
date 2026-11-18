# Slim Launch Plan: one paid thing

Reviewed with /plan-ceo-review, SCOPE REDUCTION mode, 2026-11-16.
Review only. No code has been changed.

## Problem

BillKarma has about 430 Python files, about 400 guides and 8+ paid products.
The main product, the $29-149 dispute, refunds the customer if the hospital
does not reduce the bill within 45 days. So revenue depends on what the hospital
does, which we cannot control.

## Decision D1 (approved by user): sell the Bill Check Report, $19 one-time

Every deliverable is output we control. The hospital's reaction never affects revenue.

| Step | What happens | Price |
| --- | --- | --- |
| Scan | Upload bill, extract lines, compare to Medicare, flag duplicates/unbundling | Free |
| Teaser | Show number of flagged lines and total potential savings. Hide the per-line detail and letters | Free |
| Unlock | Per-line findings, itemized-bill request letter, dispute letter, phone script. The patient sends them | $19 one-time |

Refund policy: refund in full if the scan finds no flagged lines. No outcome refund.

## What we reuse (already built)

scanner.py, analyzer.py, validators/, bill_score.py, results page, itemized_request.py,
dispute_packet.py / appeal_letter.py (letter text), advisor.py phone script,
payment.py one-time checkout, Stripe webhook.

## New work (the only new code)

1. One `report_unlocks` table (bill_id, stripe_session_id, status), as a numbered SQL file.
2. Gate the per-line detail, letters and script on `results/{bill_id}` behind an unlock check.
3. Checkout route for $19 (reuse the one-time session helper) and success redirect.
4. Webhook marks the unlock paid. Refund path for zero-finding bills.
5. One config constant: `REPORT_PRICE_CENTS = 1900`.

## Cut from the launch surface (hide behind flags or remove links; do not delete yet)

- Dispute mailing, follow-ups, 45-day outcome refund (dispute_service, daily_jobs follow-up job)
- Insurance appeals ($149/$299), household plan ($199/yr), debt fighter, FDCPA / settlement /
  charity-care mail-in letters, GFE dispute, AG complaints, esign, fax, 15% negotiation fee,
  advocacy workspace, org management, referrals, MCP server
- Homepage and guide CTAs that point to any product other than the free scan

## Kept as free top-of-funnel (no new work)

Existing guides and hospital/procedure pages. Freeze: no new guides. Point every CTA at the free scan.

## NOT in scope

- Mailing letters for the patient. Needs Lob, follow-up jobs and reply parsing, and creates the outcome expectation.
- Subscriptions. No recurring revenue until one-time purchase is proven.
- Deleting code. Hiding costs less and is reversible. Delete after 60 days if still unused.
- Charity-care check as a separate product. Add back to the report later if buyers ask.
- New guides, new states, Spanish expansion.

## Risks

1. Teaser gives away too much and nobody pays. Mitigation: show count and dollar total only.
2. False positives erode trust, since we cannot control hospital response either.
   Mitigation: "potential" language per PRODUCT_CONTEXT.md and the zero-finding refund.
3. $19 is untested. No evidence of willingness to pay exists in the repo.

## Success and kill criteria

Run 30 days after launch, with 200 scans minimum.
- Ship signal: 10% or more of completed scans unlock (20 of 200).
- Kill or reprice: under 3% unlock.
- Before launch: run 3 real bills end to end and read every flagged line by hand.

## Failure modes

| Failure | Handled? | User sees | Test |
| --- | --- | --- | --- |
| Webhook delayed, user paid but still locked | Must handle: poll the session on success page | "Confirming payment" then unlock | Yes, needed |
| Double click on Pay | Stripe session reuse per bill | Same checkout | Yes, needed |
| Zero flagged lines | Skip the paywall, offer the free letters | No charge | Yes, needed |
| OCR fails or bill unreadable | Existing scanner error path | Retry message | Exists |
| Refund request after unlock | Manual, within 7 days if scan was wrong | Email | Manual |

## Implementation tasks

1. Add `report_unlocks` SQL migration.
2. Add `REPORT_PRICE_CENTS` to config.py.
3. Add unlock check helper in payment.py (one function).
4. Gate results page and letter routes on the unlock check.
5. Add `/report/checkout` route and success handler.
6. Webhook branch for report unlocks.
7. Flag-off the cut products and remove their homepage and guide CTAs.
8. Tests: unlocked vs locked results, webhook marks paid, zero-finding bill not gated.

## GSTACK REVIEW REPORT

| Review | Runs | Status | Findings |
| --- | --- | --- | --- |
| CEO Review (scope reduction) | 1 | Condensed run | 1 decision settled (D1), 5 failure modes mapped |

VERDICT: Review was condensed to the scope question the user raised. Sections 1-10 were not each run to full depth, and no outside voice or spec-review subagent was used. Treat as a scope decision, not a full engineering review.

**UNRESOLVED DECISIONS:**
- Whether to hide or delete the cut products (plan assumes hide, revisit at 60 days)

## Implementation status (2026-11-17, branch slim-launch-report-paywall)

Built and tested locally, not deployed. 898 tests pass; the 2 failures in tests/test_dispute_delivery.py
(date-dependent refund-date text) fail identically on the untouched code.

What changed
- `report.py` (new): teaser, unlock check, pending/paid records. `report_unlocks` table in db.py SCHEMA.
- `slim_launch.py` (new): pages that redirect to /scan, API routes that answer 404 while SLIM_LAUNCH=1.
- `payment.create_report_checkout`, `POST /report/checkout` (form post, 303 to Stripe), `GET /report/success`
  (confirms with Stripe, then opens the report), webhook branch for payment_purpose=bill_report.
- Paywalled: /api/results (teaser only), dispute-letter, dispute-phone-script, dispute-packet, score, email-report.
  A bill with nothing flagged is never charged. Double-charge guard checks pending sessions with Stripe first.
- Copy rewritten around one offer (free check, $19 unlock): landing, scan, results, terms, about, footer, nav.
- Tests: tests/test_slim_launch.py (59). conftest defaults SLIM_LAUNCH=0 so product tests still run.

Config: SLIM_LAUNCH (default on), REPORT_PRICE_CENTS (default 1900). SLIM_LAUNCH=0 makes results free and
unhides routes, but landing/results templates stay on the new copy (revert the commit for the old pages).

Go-live checklist
1. Stripe: STRIPE_SECRET_KEY set; webhook endpoint /api/stripe/webhook subscribed to checkout.session.completed
   with STRIPE_WEBHOOK_SECRET set. Try one purchase with test keys first.
2. Decide the refund policy and add it to templates/terms.html (none is promised on the site now).
3. Have counsel read the new terms text. The old e-sign dispute terms are only shown when SLIM_LAUNCH=0.
4. Merging to the deploy branch turns the slim launch ON immediately (it is the default).

Known gaps
- Buyers re-open the report with the same browser session cookie. If the cookie is lost they cannot get back in;
  emailing a access link after purchase would fix that.
- Spanish pages (/es/...) and guide article text still talk about the dispute service; links to hidden pages
  redirect to /scan.
- Success text promises no receipt, because Stripe receipts depend on dashboard settings.
