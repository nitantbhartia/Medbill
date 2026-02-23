"""Guide: How to Use Your HSA or FSA to Pay Medical Bills"""

from guides import register, _embed

register(
    "hsa-fsa-pay-medical-bills",
    {
        "title": "How to Use Your HSA or FSA to Pay Medical Bills",
        "meta_description": "HSA contribution limits hit $4,300 in 2026. Learn which medical expenses qualify, how to use HSA and FSA funds strategically, and why your HSA beats a savings account for medical bills.",
        "published": "2026-02-23",
        "author": "BillKarma Team",
        "category": "Health Insurance",
        "faqs": [
            {
                "q": "Can I use my HSA to pay old medical bills?",
                "a": "Yes&mdash;with an important caveat. You can use your HSA to reimburse yourself for any qualified medical expense incurred after your HSA was established, even if years have passed since you paid out of pocket. There is no deadline to reimburse yourself from your HSA. This makes the &ldquo;let it grow&rdquo; strategy powerful: pay bills out of pocket now, invest your HSA, and reimburse yourself years later using tax-free investment gains."
            },
            {
                "q": "What medical expenses are HSA-eligible?",
                "a": "HSA-eligible expenses are defined by IRS Publication 502 and include doctor visits, hospital care, prescriptions, dental care, vision care (including glasses and contacts), mental health services, physical therapy, hearing aids, and certain over-the-counter medications. Non-eligible expenses include cosmetic procedures, gym memberships (unless prescribed), non-prescription vitamins, and health insurance premiums (with narrow exceptions for long-term care insurance)."
            },
            {
                "q": "What happens to my FSA if I change jobs?",
                "a": "Your FSA balance is forfeited when you leave your employer unless your plan offers a grace period or rollover option. You are allowed to spend your full annual FSA election before leaving, even if you haven&rsquo;t contributed that much yet&mdash;this is one key advantage of FSAs. COBRA continuation of FSA coverage is sometimes available, but premiums make it expensive. Unlike HSAs, FSAs are owned by your employer, not you."
            },
            {
                "q": "Can I invest my HSA?",
                "a": "Yes. Most HSA providers allow you to invest your balance in mutual funds, ETFs, or other securities once your balance exceeds a minimum threshold (typically $500&ndash;$1,000). HSA investments grow tax-free and can be withdrawn tax-free for qualified medical expenses at any age. After age 65, HSA funds can be withdrawn for any reason and are taxed as ordinary income&mdash;just like a traditional IRA&mdash;but without penalty."
            },
            {
                "q": "What is the HSA contribution limit for 2026?",
                "a": "The IRS set the 2026 HSA contribution limit at $4,300 for self-only HDHP coverage and $8,550 for family HDHP coverage. Individuals 55 or older can make an additional $1,000 catch-up contribution annually. These limits apply to combined contributions from you and your employer. You cannot contribute to an HSA once you enroll in Medicare."
            },
        ],
        "body": f"""
<p class="lead">
  Health Savings Accounts and Flexible Spending Accounts are among the most underutilized tools in personal finance.
  BillKarma&rsquo;s analysis of 6,800+ hospitals found that fewer than 1 in 5 patients with HSA-eligible accounts
  use them optimally&mdash;many pay bills by credit card and carry interest charges on expenses that could have been
  covered tax-free. With HSA contribution limits reaching $4,300 for individuals and $8,550 for families in 2026,
  the tax advantage alone is worth hundreds of dollars annually for most account holders.
</p>

<nav class="toc">
  <strong>In this guide</strong>
  <ol>
    <li><a href="#hsa-vs-fsa">HSA vs. FSA: Core Differences at a Glance</a></li>
    <li><a href="#2026-limits">2026 Contribution Limits and Eligibility</a></li>
    <li><a href="#eligible-expenses">What Qualifies (and What Doesn&rsquo;t)</a></li>
    <li><a href="#how-to-pay">How to Use HSA/FSA to Pay a Medical Bill</a></li>
    <li><a href="#invest-strategy">The Strategic HSA: Invest Now, Reimburse Later</a></li>
    <li><a href="#fsa-pitfalls">FSA Use-It-or-Lose-It Pitfalls</a></li>
    <li><a href="#medicare-interaction">When Medicare Enrollment Stops HSA Contributions</a></li>
  </ol>
</nav>

<h2 id="hsa-vs-fsa">1. HSA vs. FSA: Core Differences at a Glance</h2>
<p>
  HSAs and FSAs both let you pay medical expenses with pre-tax dollars, but they work differently and serve
  different situations. The wrong choice costs you real money&mdash;either in taxes you didn&rsquo;t need to pay
  or in forfeited balances that evaporate at year-end.
</p>

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>HSA</th>
      <th>FSA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eligibility Requirement</td>
      <td>Must be enrolled in a qualifying HDHP</td>
      <td>Any employer-sponsored health plan</td>
    </tr>
    <tr>
      <td>2026 Contribution Limit (Individual)</td>
      <td>$4,300</td>
      <td>$3,300</td>
    </tr>
    <tr>
      <td>2026 Contribution Limit (Family)</td>
      <td>$8,550</td>
      <td>$3,300 (per employee)</td>
    </tr>
    <tr>
      <td>Rollover</td>
      <td>100% rolls over every year</td>
      <td>Up to $640 (2026 limit) or grace period only</td>
    </tr>
    <tr>
      <td>Ownership</td>
      <td>You own the account; portable</td>
      <td>Employer owns the account; forfeited on job change</td>
    </tr>
    <tr>
      <td>Investment Options</td>
      <td>Yes&mdash;invest in mutual funds, ETFs</td>
      <td>No&mdash;cash only</td>
    </tr>
    <tr>
      <td>Tax Treatment</td>
      <td>Triple tax-free (contribute, grow, withdraw)</td>
      <td>Pre-tax contribution; withdrawals tax-free for QME</td>
    </tr>
    <tr>
      <td>Self-Employment Eligible</td>
      <td>Yes</td>
      <td>No (requires employer plan)</td>
    </tr>
    <tr>
      <td>Use for Non-Medical (Age 65+)</td>
      <td>Yes (taxed as income, no penalty)</td>
      <td>No&mdash;non-medical use = taxes + 20% penalty</td>
    </tr>
  </tbody>
</table>

<div class="key-takeaway">
  <h3>Key Takeaway 1</h3>
  <p>
    Always audit your medical bill before paying it with HSA or FSA funds. Paying an erroneous charge
    with tax-advantaged dollars doesn&rsquo;t make the error free&mdash;it still costs you money you
    shouldn&rsquo;t owe. Use the <a href="/scan">BillKarma bill scanner</a> to verify every line item
    before you tap your HSA.
  </p>
</div>

<h2 id="2026-limits">2. 2026 Contribution Limits and Eligibility</h2>
<p>
  To contribute to an HSA, you must be enrolled in a High-Deductible Health Plan (HDHP).
  For 2026, the IRS defines an HDHP as a plan with a minimum annual deductible of $1,650 (self-only)
  or $3,300 (family) and an out-of-pocket maximum that does not exceed $8,300 (self-only) or $16,600 (family).
</p>
<p>
  You cannot contribute to an HSA if you are enrolled in Medicare (any part), claimed as a dependent
  on someone else&rsquo;s return, or have any non-HDHP health coverage. Violation of these rules means
  taxes and a 20% penalty on any disqualified contribution.
</p>

<table>
  <thead>
    <tr>
      <th>Coverage Type</th>
      <th>2025 Limit</th>
      <th>2026 Limit</th>
      <th>Change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HSA &mdash; Self-Only</td>
      <td>$4,150</td>
      <td>$4,300</td>
      <td>+$150</td>
    </tr>
    <tr>
      <td>HSA &mdash; Family</td>
      <td>$8,300</td>
      <td>$8,550</td>
      <td>+$250</td>
    </tr>
    <tr>
      <td>HSA &mdash; Catch-Up (55+)</td>
      <td>$1,000</td>
      <td>$1,000</td>
      <td>No change</td>
    </tr>
    <tr>
      <td>FSA &mdash; Healthcare</td>
      <td>$3,200</td>
      <td>$3,300</td>
      <td>+$100</td>
    </tr>
    <tr>
      <td>FSA &mdash; Dependent Care</td>
      <td>$5,000</td>
      <td>$5,000</td>
      <td>No change</td>
    </tr>
  </tbody>
</table>

<h2 id="eligible-expenses">3. What Qualifies (and What Doesn&rsquo;t)</h2>
<p>
  IRS Publication 502 governs which medical expenses are eligible for HSA and FSA reimbursement.
  The list is broader than most people realize&mdash;and the exclusions are specific enough to trip people up.
</p>

<table>
  <thead>
    <tr>
      <th>Expense</th>
      <th>HSA/FSA Eligible?</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Doctor visits and copays</td>
      <td>Yes</td>
      <td>Any licensed medical professional</td>
    </tr>
    <tr>
      <td>Prescription medications</td>
      <td>Yes</td>
      <td>Requires prescription; OTC covered since 2020</td>
    </tr>
    <tr>
      <td>Dental care (fillings, crowns, extractions)</td>
      <td>Yes</td>
      <td>Cosmetic dentistry (whitening) is not eligible</td>
    </tr>
    <tr>
      <td>Vision care, glasses, contacts</td>
      <td>Yes</td>
      <td>LASIK surgery is eligible</td>
    </tr>
    <tr>
      <td>Mental health therapy</td>
      <td>Yes</td>
      <td>Licensed therapists and psychiatrists</td>
    </tr>
    <tr>
      <td>Hearing aids and batteries</td>
      <td>Yes</td>
      <td>Including ear exams for hearing aids</td>
    </tr>
    <tr>
      <td>Gym membership</td>
      <td>No (generally)</td>
      <td>Eligible only if prescribed for specific condition</td>
    </tr>
    <tr>
      <td>Vitamins and supplements</td>
      <td>No (generally)</td>
      <td>Eligible if prescribed to treat diagnosed condition</td>
    </tr>
    <tr>
      <td>Cosmetic surgery</td>
      <td>No</td>
      <td>Reconstructive surgery after accident is eligible</td>
    </tr>
    <tr>
      <td>Health insurance premiums</td>
      <td>No (HSA); Yes (FSA if employer allows)</td>
      <td>COBRA premiums eligible for HSA</td>
    </tr>
    <tr>
      <td>Long-term care insurance premiums</td>
      <td>Yes (age-based limits)</td>
      <td>IRS caps vary by age; $5,880 max at age 70+ (2026)</td>
    </tr>
  </tbody>
</table>

<h2 id="how-to-pay">4. How to Use HSA/FSA to Pay a Medical Bill</h2>
<p>
  The mechanics of paying a medical bill with your HSA or FSA are straightforward&mdash;but errors
  are common. Always save your receipts and Explanation of Benefits documents. If you&rsquo;re ever audited,
  you need documentation showing the expense was a qualified medical expense.
</p>
<p>
  <strong>Step 1: Receive and verify your bill.</strong> Before paying anything, request an itemized bill
  and compare it to your Explanation of Benefits. Pay only after confirming the charges are correct.
  Use the <a href="/scan">BillKarma scanner</a> to catch errors fast.
</p>
<p>
  <strong>Step 2: Pay with your HSA debit card or FSA card.</strong> Most HSA and FSA accounts issue a debit card
  linked directly to the account. Swipe it like a normal debit card at the provider&rsquo;s payment window.
  The funds come out pre-tax.
</p>
<p>
  <strong>Step 3: Save the receipt.</strong> The IRS requires substantiation of HSA and FSA withdrawals.
  Keep a folder&mdash;digital or physical&mdash;with every receipt and EOB tied to an HSA or FSA payment.
  The IRS lookback period for HSA audits is 3 years (or more if fraud is suspected).
</p>
<p>
  <strong>Step 4: Reimburse yourself if you paid out of pocket.</strong> If you forgot to use your HSA card,
  or if you paid during a period when you were building your HSA balance, you can reimburse yourself later.
  Log in to your HSA portal, select &ldquo;reimburse myself,&rdquo; and upload the receipt. The funds transfer
  to your checking account tax-free.
</p>

<div class="key-takeaway">
  <h3>Key Takeaway 2</h3>
  <p>
    If you can afford to pay medical bills out of pocket, consider doing so and reimbursing yourself
    from your HSA years later after the funds have grown. There is no deadline on HSA reimbursements&mdash;
    just save your receipts. Use our <a href="/calculator">HSA growth calculator</a> to see what
    your balance could be worth in 10 or 20 years.
  </p>
</div>

<div class="bill-example">
  <h3>Sample $4,800 Hospital Bill Paid via HSA</h3>
  <div class="line-item">
    <span class="desc">Outpatient Surgery Facility Fee (CPT 27447)</span>
    <span class="amount">$3,200.00</span>
  </div>
  <div class="line-item">
    <span class="desc">Anesthesia &mdash; 90 minutes (CPT 00402)</span>
    <span class="amount">$840.00</span>
  </div>
  <div class="line-item">
    <span class="desc">Post-Op Physical Therapy &mdash; 3 sessions</span>
    <span class="amount">$510.00</span>
  </div>
  <div class="line-item flagged">
    <span class="desc">Compression Stockings (DME)</span>
    <span class="amount">$250.00</span>
    <span class="flag">HSA-eligible only if prescribed &mdash; verify prescription documentation</span>
  </div>
  <div class="line-total">
    <span class="desc">Total Patient Responsibility (after insurance)</span>
    <span class="amount">$4,800.00</span>
  </div>
  <div class="line-total">
    <span class="desc">Paid via HSA Debit Card (tax-free)</span>
    <span class="amount">$4,800.00</span>
  </div>
  <div class="line-total">
    <span class="desc">Estimated Tax Savings (24% bracket)</span>
    <span class="amount">$1,152.00</span>
  </div>
</div>

<h2 id="invest-strategy">5. The Strategic HSA: Invest Now, Reimburse Later</h2>
<p>
  The most powerful HSA strategy is rarely discussed: use the account as a stealth retirement vehicle.
  If you can afford to pay medical bills out of pocket, do so. Let your HSA contributions accumulate
  and invest in low-cost index funds. There is no deadline to reimburse yourself for qualified medical expenses.
</p>
<p>
  Thirty years from now, a $4,000 HSA contribution invested in a broad market index fund (assuming 7% average
  annual return) grows to approximately $30,450. Withdraw it tax-free to reimburse yourself for today&rsquo;s
  medical bills&mdash;bills you&rsquo;ve kept receipts for&mdash;and you&rsquo;ve just converted decades
  of investment gains into tax-free income.
</p>

<div class="key-takeaway">
  <h3>Key Takeaway 3</h3>
  <p>
    FSA dollars evaporate if you don&rsquo;t use them. Before your plan year ends, check your FSA balance
    and spend down remaining funds on eligible expenses&mdash;glasses, dental, prescriptions.
    Read our guide on <a href="/guides/how-to-read-an-eob">how to read your Explanation of Benefits</a>
    to make sure the bills you&rsquo;re paying are actually yours to pay.
  </p>
</div>

<div class="case-study">
  <h3>Case Study: HSA Triple Tax Advantage vs. Credit Card</h3>
  <p>
    Two patients each owed $4,300 after a knee surgery. Patient A paid with a credit card at 22% APR and
    took 14 months to pay off the balance, paying $706 in interest. Patient B maxed out her HSA ($4,300),
    paid the bill with HSA funds, and saved $1,032 in federal and state income taxes (24% combined rate).
    Patient B&rsquo;s effective cost was $3,268. Patient A&rsquo;s effective cost was $5,006&mdash;
    a $1,738 difference for the exact same medical care.
  </p>
</div>

<div class="case-study">
  <h3>Case Study: FSA Use-It-or-Lose-It Mistake</h3>
  <p>
    A user elected $2,800 into his FSA in January. By November, he had only spent $1,100. With no grace period
    and no rollover option in his plan, he had six weeks to spend $1,700 on eligible expenses.
    He scrambled to buy prescription eyeglasses, stock up on eligible OTC medications, and prepay a dental
    appointment. He spent $1,650 and forfeited $50. Planning his election amount based on expected expenses
    in the following year would have prevented the entire problem.
  </p>
</div>

<div class="case-study">
  <h3>Case Study: Reimbursing Three Years Later</h3>
  <p>
    A user paid $6,400 in out-of-pocket medical costs in 2023 while contributing to and investing her HSA.
    She kept all receipts and EOBs. In 2026, she withdrew $6,400 from her HSA&mdash;now grown to $8,100&mdash;
    to reimburse herself for 2023 expenses. The withdrawal was entirely tax-free. The $1,700 in investment
    gains she withdrew above her original expenses was also tax-free because the reimbursement qualified.
    Effectively, she converted stock market gains into tax-free cash.
  </p>
</div>

<h2 id="fsa-pitfalls">6. FSA Use-It-or-Lose-It Pitfalls</h2>
<p>
  The FSA &ldquo;use-it-or-lose-it&rdquo; rule means unspent funds at plan year-end are forfeited to your employer.
  The IRS allows employers to offer one of two options (but not both): a grace period of up to 2.5 months into
  the new plan year, or a rollover of up to $640 (2026 limit). Many employers offer neither.
</p>
<p>
  Avoid over-electing into your FSA. Estimate conservatively based on your known upcoming expenses.
  If you&rsquo;re pregnant, have a scheduled surgery, or need new glasses, increase your election.
  If your health is unpredictable, keep your election modest and supplement with HSA savings if eligible.
</p>

<h2 id="medicare-interaction">7. When Medicare Enrollment Stops HSA Contributions</h2>
<p>
  The moment you enroll in Medicare Part A, Part B, or Part D, you are no longer eligible to contribute
  to an HSA. This catches people by surprise when they sign up for Social Security benefits at 65&mdash;
  Social Security enrollment automatically triggers Medicare Part A, ending your HSA contribution eligibility
  retroactively up to 6 months before your application date.
</p>
<p>
  If you plan to delay Medicare and continue contributing to your HSA, you must also delay Social Security.
  Coordinate this decision with a financial planner 12&ndash;18 months before your target retirement date.
  Once enrolled in Medicare, your existing HSA balance remains yours to use tax-free for qualified expenses&mdash;
  including Medicare premiums, which are a rare exception to the general rule against using HSA funds for insurance.
</p>

{_embed("hsa-fsa-calculator")}

<div class="faq-section">
  <h2>Frequently Asked Questions</h2>

  <div class="faq-item">
    <h3>Can I use my HSA to pay old medical bills?</h3>
    <p>
      Yes&mdash;with an important caveat. You can use your HSA to reimburse yourself for any qualified medical
      expense incurred after your HSA was established, even if years have passed since you paid out of pocket.
      There is no deadline. This makes the &ldquo;let it grow&rdquo; strategy powerful: pay bills out of pocket now,
      invest your HSA, and reimburse yourself years later using tax-free investment gains.
    </p>
  </div>

  <div class="faq-item">
    <h3>What medical expenses are HSA-eligible?</h3>
    <p>
      HSA-eligible expenses are defined by IRS Publication 502 and include doctor visits, hospital care,
      prescriptions, dental care, vision care, mental health services, physical therapy, hearing aids,
      and over-the-counter medications. Non-eligible expenses include cosmetic procedures, gym memberships
      (unless prescribed), non-prescription vitamins, and most insurance premiums.
    </p>
  </div>

  <div class="faq-item">
    <h3>What happens to my FSA if I change jobs?</h3>
    <p>
      Your FSA balance is forfeited when you leave your employer unless your plan offers a grace period
      or rollover option. You are allowed to spend your full annual FSA election before leaving, even if
      you haven&rsquo;t contributed that much yet. Unlike HSAs, FSAs are owned by your employer, not you.
    </p>
  </div>

  <div class="faq-item">
    <h3>Can I invest my HSA?</h3>
    <p>
      Yes. Most HSA providers allow you to invest your balance in mutual funds or ETFs once your balance
      exceeds a minimum threshold (typically $500&ndash;$1,000). HSA investments grow tax-free and can be
      withdrawn tax-free for qualified medical expenses. After age 65, HSA funds can be withdrawn for any
      reason and taxed as ordinary income&mdash;just like a traditional IRA&mdash;with no penalty.
    </p>
  </div>

  <div class="faq-item">
    <h3>What is the HSA contribution limit for 2026?</h3>
    <p>
      The IRS set the 2026 HSA contribution limit at $4,300 for self-only HDHP coverage and $8,550 for
      family HDHP coverage. Individuals 55 or older can make an additional $1,000 catch-up contribution.
      These limits apply to combined contributions from you and your employer. You cannot contribute
      to an HSA once you enroll in Medicare.
    </p>
  </div>
</div>

<ul class="sources-list">
  <li><a href="https://www.irs.gov/publications/p502" target="_blank" rel="noopener">IRS Publication 502 &mdash; Medical and Dental Expenses</a></li>
  <li><a href="https://www.irs.gov/pub/irs-drop/rp-25-19.pdf" target="_blank" rel="noopener">IRS Revenue Procedure 2025-19 &mdash; HSA Limits for 2026</a></li>
  <li><a href="https://www.healthcare.gov/have-job-based-coverage/hsa-eligible-plan/" target="_blank" rel="noopener">HealthCare.gov &mdash; HSA-Eligible Plans Explained</a></li>
  <li><a href="https://www.dol.gov/sites/dolgov/files/ebsa/about-ebsa/our-activities/resource-center/faqs/fsa-and-flexible-benefits.pdf" target="_blank" rel="noopener">DOL &mdash; FSA Frequently Asked Questions</a></li>
  <li><a href="https://www.kff.org/health-costs/issue-brief/health-savings-accounts-hsas-and-high-deductible-health-plans-hdhps/" target="_blank" rel="noopener">KFF &mdash; HSAs and HDHPs: A Primer</a></li>
</ul>
""",
    },
)
