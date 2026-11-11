# BillKarma Positioning

This file defines BillKarma's niche. Read it before writing any page, guide,
email or ad. `PRODUCT_CONTEXT.md` covers tone and language. This file covers
**what we sell, to whom, and what we deliberately don't do.**

---

## One line

**BillKarma checks your hospital bill against what Medicare pays, then sends
a written dispute to the billing office for you and follows up until they
answer.**

## Who it's for

People holding a **hospital or facility bill they think is wrong or too high**:

- Uninsured or self-pay patients billed at full "chargemaster" prices.
- Insured patients with a large balance after insurance (deductible,
  coinsurance, out-of-network or facility fees).
- Anyone whose hospital bill has gone, or is about to go, to collections.

Typical bill: a few hundred to a few thousand dollars, from an ER visit,
imaging, outpatient surgery, labs or a short stay.

## The job we do

In this order, and nothing else on the homepage:

| Step | What happens | Price |
| --- | --- | --- |
| 1. Check the bill | Upload or photograph it. Each line is compared to the Medicare rate for that code, and duplicates and unbundling are flagged. | Free |
| 2. Ask the hospital first | Itemized-bill request letter and a financial assistance (charity care) check against the hospital's own policy. | Free (we mail the application certified for $9) |
| 3. Dispute in writing | We write the dispute letter, send it to the hospital billing office, and follow up at 7, 14, 30 and 45 days. | Flat fee by bill size: $29 under $1k, $49 to $5k, $99 to $20k, $149 above |
| 4. If it's in collections | Debt validation letter to the collector, sent certified. | $19 |

Prices live in `config.py`. When they change, change this table.

## Why us (the edge)

1. **Hospital-specific data.** Billing contacts, financial assistance rules
   and a Medicare-markup grade for every U.S. hospital we cover. Competitors
   give generic advice; we name the office, the policy and the markup.
2. **Fully automated and flat-fee.** Human negotiators charge 10–35% of
   savings and often require bills over $5,000. We charge a flat fee and
   serve the smaller bills they turn away.
3. **Everything in writing.** A paper trail the patient owns, with dates.

## What we don't do

Say this plainly whenever it's relevant. It builds trust and keeps support
load at zero.

- **We don't negotiate by phone or guarantee a reduction.** We send written
  disputes and follow-ups. Outcomes are up to the hospital.
- **We don't fight insurance denials on the homepage.** That's a different
  job (against the insurer, not the hospital). The appeal flow at `/appeal`
  stays live but isn't promoted as a core offer.
- **We don't give legal advice or defend lawsuits.** For a lawsuit, wage
  garnishment or bankruptcy, point to a consumer attorney or legal aid.
- **We aren't a price-shopping tool.** Cost pages exist to help people judge
  a bill they already have, not to book care.
- **We don't handle doctor-only, dental or ambulance-only bills as a core
  case.** Guides may cover them; the paid dispute is for hospital and
  facility bills.

## Where to send people we can't help

| Situation | Send them to |
| --- | --- |
| Very large bill (roughly $20k+) and they want someone to negotiate by phone | A contingency-fee bill negotiator (referral partner, to be set up) |
| Low income, nonprofit hospital | The hospital's financial assistance program first (our free check), or Dollar For (free) |
| Insurance denied the claim | The insurer's internal appeal, then external review; `/appeal` if they want help |
| Sued, garnished, or considering bankruptcy | Local legal aid or a consumer attorney |

## Rules for content

- Every guide must connect back to the job above: understanding, checking
  or disputing a hospital bill. A topic that can't (e.g. choosing an
  insurance plan) is low priority and should not get new pages.
- One page per search intent. Before adding a guide, search `guides.py` for
  an existing page on the same question and improve it instead. Duplicates
  get a 301 in `GUIDE_REDIRECTS`.
- Calls to action point to step 1 (the free check) or the step that fits the
  page, never to products outside this table.
- Never claim to do something in "What we don't do".
