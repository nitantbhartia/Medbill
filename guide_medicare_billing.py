"""Guide: How Medicare Billing Works — Part A, Part B, and What You Owe"""

from guides import register, _embed

register(
    "how-medicare-billing-works",
    {
        "title": "How Medicare Billing Works: Part A, Part B, and What You Owe",
        "meta_description": "Medicare covers 67 million Americans but billing rules confuse most patients. Learn how Part A and Part B billing work, what you'll owe, and how to catch billing errors before you pay.",
        "published": "2026-02-23",
        "author": "BillKarma Team",
        "category": "Medicare",
        "faqs": [
            {
                "q": "What is the Medicare Part A deductible?",
                "a": "The Medicare Part A deductible in 2026 is $1,676 per benefit period. A benefit period starts the day you're admitted as an inpatient and ends after you've been out of the hospital or skilled nursing facility for 60 consecutive days. You can pay this deductible more than once per year if you have multiple hospital stays separated by 60 days."
            },
            {
                "q": "What does Medicare not cover?",
                "a": "Original Medicare does not cover routine dental, vision, or hearing care, long-term custodial nursing home care, most prescription drugs (unless you have Part D), cosmetic surgery, or care received outside the United States. Medicare also does not cover services your provider decides are not medically necessary."
            },
            {
                "q": "What is a Medicare crossover claim?",
                "a": "A Medicare crossover claim is a claim that Medicare automatically forwards to your secondary insurer (such as Medicaid or a Medigap policy) after Medicare processes its portion. If you have secondary insurance, Medicare coordinates with that plan so you don&rsquo;t have to file a second claim manually. Errors in crossover claims are common and can result in unexpected bills."
            },
            {
                "q": "How do I read my Medicare Summary Notice?",
                "a": "Your Medicare Summary Notice (MSN) arrives quarterly and lists every service billed to Medicare on your behalf. Check the provider name, service date, and amount billed. Compare the &ldquo;Medicare-approved amount&rdquo; against what you were charged. If Medicare denied a claim or paid less than expected, the MSN shows the reason code. You have 120 days from the MSN date to file an appeal."
            },
            {
                "q": "Can doctors balance bill Medicare patients?",
                "a": "It depends on the provider&rsquo;s participation status. Participating providers accept Medicare assignment and cannot charge you more than your coinsurance and deductible. Non-participating providers can charge up to 15% above the Medicare-approved amount (the &ldquo;limiting charge&rdquo;). Providers who opt out of Medicare entirely can charge whatever they want, but Medicare pays nothing, and you pay everything."
            },
        ],
        "body": f"""
<p class="lead">
  Medicare covers 67 million Americans&mdash;but its billing rules trip up patients and providers alike.
  BillKarma&rsquo;s analysis of 6,800+ hospitals found that Medicare billing errors appear in roughly 1 in 4 inpatient claims,
  costing beneficiaries an estimated $1.3 billion in unnecessary out-of-pocket costs annually.
  Whether you&rsquo;re facing a hospital stay, a string of outpatient visits, or a surprise balance bill, understanding
  how Part A and Part B billing actually work is your first line of defense.
</p>

<nav class="toc">
  <strong>In this guide</strong>
  <ol>
    <li><a href="#part-a-vs-part-b">Part A vs. Part B: The Core Difference</a></li>
    <li><a href="#what-you-owe">2026 Deductibles, Premiums, and Coinsurance</a></li>
    <li><a href="#reading-your-msn">How to Read Your Medicare Summary Notice</a></li>
    <li><a href="#common-errors">Common Medicare Billing Errors</a></li>
    <li><a href="#observation-status">The Observation Status Trap</a></li>
    <li><a href="#medicare-advantage">Medicare Advantage vs. Original Medicare Billing</a></li>
    <li><a href="#appeals">How to Appeal a Medicare Billing Decision</a></li>
  </ol>
</nav>

<h2 id="part-a-vs-part-b">1. Part A vs. Part B: The Core Difference</h2>
<p>
  Medicare is split into two main parts that cover fundamentally different settings of care.
  Knowing which part applies to your situation determines your deductible, your coinsurance structure,
  and even which providers can bill you directly.
</p>
<p>
  <strong>Part A</strong> covers inpatient hospital care, skilled nursing facility (SNF) stays after a qualifying
  hospital admission, hospice care, and some home health services. Part A is premium-free for most beneficiaries
  who worked and paid Medicare taxes for at least 10 years (40 quarters).
</p>
<p>
  <strong>Part B</strong> covers outpatient care&mdash;doctor visits, emergency department visits (when you&rsquo;re
  not formally admitted), lab work, imaging, outpatient surgery, durable medical equipment, and preventive services.
  Part B requires a monthly premium ($185/month in 2026 for most beneficiaries, higher for high earners under IRMAA).
</p>

<h2 id="what-you-owe">2. 2026 Deductibles, Premiums, and Coinsurance</h2>
<p>
  Medicare&rsquo;s cost-sharing structure differs significantly between Part A and Part B.
  The table below shows what you&rsquo;re responsible for under Original Medicare in 2026,
  before any Medigap or secondary insurance applies.
</p>

<table>
  <thead>
    <tr>
      <th>Cost Type</th>
      <th>Part A (Inpatient)</th>
      <th>Part B (Outpatient)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Annual Deductible</td>
      <td>$1,676 per benefit period</td>
      <td>$240 per calendar year</td>
    </tr>
    <tr>
      <td>Monthly Premium</td>
      <td>$0 (most beneficiaries)</td>
      <td>$185 (standard; higher with IRMAA)</td>
    </tr>
    <tr>
      <td>Coinsurance &mdash; Days 1&ndash;60</td>
      <td>$0 after deductible</td>
      <td>20% of approved amount</td>
    </tr>
    <tr>
      <td>Coinsurance &mdash; Days 61&ndash;90</td>
      <td>$419/day</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Coinsurance &mdash; Days 91+</td>
      <td>$838/day (lifetime reserve)</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Skilled Nursing (Days 21&ndash;100)</td>
      <td>$209.50/day</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Out-of-Pocket Maximum</td>
      <td>None (Original Medicare)</td>
      <td>None (Original Medicare)</td>
    </tr>
  </tbody>
</table>

<p>
  The absence of an out-of-pocket maximum under Original Medicare is one of the most consequential facts
  in healthcare finance. A 90-day hospital stay with complications can generate tens of thousands of dollars
  in coinsurance with no cap. This is why Medigap supplemental policies exist.
</p>

<h2 id="reading-your-msn">3. How to Read Your Medicare Summary Notice</h2>
<p>
  Your Medicare Summary Notice (MSN) is not a bill&mdash;it&rsquo;s a record of what Medicare was billed
  on your behalf and what it paid. It arrives quarterly by mail (or is available anytime on Medicare.gov).
  Most beneficiaries ignore it. That&rsquo;s a mistake.
</p>
<p>
  Each MSN entry shows: the provider&rsquo;s name, the date of service, what the provider charged,
  the Medicare-approved amount, what Medicare paid, and what you owe. When the &ldquo;amount you may be billed&rdquo;
  doesn&rsquo;t match your actual bill, you have grounds to dispute.
</p>

<table>
  <thead>
    <tr>
      <th>MSN Field</th>
      <th>What It Means</th>
      <th>What to Check</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Claim Number</td>
      <td>Unique ID for this Medicare claim</td>
      <td>Use this when calling 1-800-MEDICARE</td>
    </tr>
    <tr>
      <td>Amount Billed</td>
      <td>What the provider charged Medicare</td>
      <td>Compare to your Explanation of Benefits</td>
    </tr>
    <tr>
      <td>Medicare-Approved Amount</td>
      <td>What Medicare considers the correct rate</td>
      <td>Participating providers can only charge this</td>
    </tr>
    <tr>
      <td>Medicare Paid</td>
      <td>What Medicare actually sent the provider</td>
      <td>Should be 80% of approved amount for Part B</td>
    </tr>
    <tr>
      <td>You May Be Billed</td>
      <td>Your legitimate out-of-pocket maximum</td>
      <td>If your bill exceeds this, dispute immediately</td>
    </tr>
    <tr>
      <td>Claim Status</td>
      <td>Approved, denied, or adjusted</td>
      <td>Denied claims require an appeal within 120 days</td>
    </tr>
  </tbody>
</table>

<div class="bill-example">
  <h3>Sample Medicare Inpatient Bill &mdash; Part A</h3>
  <div class="line-item">
    <span class="desc">Room &amp; Board &mdash; Semi-Private (4 days)</span>
    <span class="amount">$14,800.00</span>
  </div>
  <div class="line-item">
    <span class="desc">Operating Room Services</span>
    <span class="amount">$8,200.00</span>
  </div>
  <div class="line-item">
    <span class="desc">Anesthesia</span>
    <span class="amount">$2,100.00</span>
  </div>
  <div class="line-item">
    <span class="desc">Laboratory &mdash; Blood Work Panel</span>
    <span class="amount">$940.00</span>
  </div>
  <div class="line-item flagged">
    <span class="desc">Physical Therapy &mdash; 6 sessions (Medicare approved 4)</span>
    <span class="amount">$1,800.00</span>
    <span class="flag">2 sessions not medically documented &mdash; dispute</span>
  </div>
  <div class="line-item error">
    <span class="desc">Observation Status Fee (patient was formally admitted)</span>
    <span class="amount">$450.00</span>
    <span class="flag">Billing error: patient admitted, not observation &mdash; remove</span>
  </div>
  <div class="line-total">
    <span class="desc">Total Charged</span>
    <span class="amount">$28,290.00</span>
  </div>
  <div class="line-total">
    <span class="desc">Part A Deductible (your responsibility)</span>
    <span class="amount">$1,676.00</span>
  </div>
  <div class="line-total">
    <span class="desc">Medicare Pays (Days 1&ndash;4 after deductible)</span>
    <span class="amount">$26,614.00</span>
  </div>
</div>

<h2 id="common-errors">4. Common Medicare Billing Errors</h2>
<p>
  Medicare billing errors are not rare edge cases&mdash;they&rsquo;re routine. The complexity of the system,
  combined with high billing volume, means errors slip through constantly. Here are the most impactful ones to watch for.
</p>

<div class="case-study">
  <h3>Error Type 1: Wrong Provider Participation Status</h3>
  <p>
    A provider who is &ldquo;non-participating&rdquo; billed a patient at 20% above the Medicare-approved amount
    without disclosing this in advance. Under the limiting charge rule, non-participating providers
    can charge up to 115% of the fee schedule, but must notify patients before delivering services.
    The patient disputed the excess charge and recovered $340.
  </p>
</div>

<div class="case-study">
  <h3>Error Type 2: Duplicate Claims</h3>
  <p>
    A hospital and the patient&rsquo;s attending physician both submitted claims for the same inpatient visit&mdash;
    one under Part A (facility) and one under Part B (professional). Medicare paid both before its duplicate
    detection system flagged the overlap. The patient received a retroactive bill for the Part B portion months later.
    A BillKarma audit identified the overlap and had the Part B charge reversed.
  </p>
</div>

<div class="case-study">
  <h3>Error Type 3: Incorrect Diagnosis Code Driving Upcoding</h3>
  <p>
    A patient admitted for a hip replacement was billed under a DRG (Diagnosis Related Group) that included
    a complication she never had. The wrong DRG increased the hospital&rsquo;s reimbursement by $3,200 and
    increased the patient&rsquo;s coinsurance by $640. After requesting the medical records and comparing
    the documented diagnosis codes against the bill, the error was corrected.
  </p>
</div>

<h2 id="observation-status">5. The Observation Status Trap</h2>
<p>
  Observation status is one of Medicare&rsquo;s most financially damaging technicalities.
  If a hospital keeps you overnight but never formally admits you as an inpatient,
  your stay is classified as &ldquo;outpatient observation,&rdquo; which bills under Part B&mdash;not Part A.
</p>
<p>
  Why does this matter? Under Part B observation, you owe 20% coinsurance on every service with no cap.
  You also cannot qualify for Medicare-covered skilled nursing care after the hospital stay,
  because SNF coverage requires a prior 3-day inpatient admission.
</p>
<p>
  Under the NOTICE Act, hospitals must notify Medicare patients in writing within 36 hours if they&rsquo;re
  placed under observation status. If you were not notified, or if your stay lasted more than 2 days,
  you can request a formal review.
</p>

<table>
  <thead>
    <tr>
      <th>Factor</th>
      <th>Inpatient Admission (Part A)</th>
      <th>Observation Status (Part B)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Deductible</td>
      <td>$1,676 per benefit period</td>
      <td>$240 per year, then 20% coinsurance</td>
    </tr>
    <tr>
      <td>Drug Coverage During Stay</td>
      <td>Covered under Part A</td>
      <td>Not covered (unless you have Part D)</td>
    </tr>
    <tr>
      <td>SNF Eligibility After Stay</td>
      <td>Yes, after 3-day qualifying stay</td>
      <td>No</td>
    </tr>
    <tr>
      <td>Required Notification</td>
      <td>Admission notice required</td>
      <td>NOTICE Act letter required within 36 hrs</td>
    </tr>
    <tr>
      <td>Appeals Path</td>
      <td>Medicare appeal process</td>
      <td>Request expedited review or appeal to QIO</td>
    </tr>
  </tbody>
</table>

<h2 id="medicare-advantage">6. Medicare Advantage vs. Original Medicare Billing</h2>
<p>
  If you have a Medicare Advantage (Part C) plan, you don&rsquo;t deal with Original Medicare billing at all&mdash;
  your plan processes claims internally. But the rules are different, and the billing pitfalls are different too.
</p>

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Original Medicare</th>
      <th>Medicare Advantage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Out-of-Pocket Maximum</td>
      <td>None</td>
      <td>Required by law (max $9,350 in-network, 2026)</td>
    </tr>
    <tr>
      <td>Prior Authorization</td>
      <td>Rarely required</td>
      <td>Common for hospitalizations and procedures</td>
    </tr>
    <tr>
      <td>Network Restrictions</td>
      <td>Any Medicare-accepting provider nationwide</td>
      <td>In-network preferred; out-of-network may be denied</td>
    </tr>
    <tr>
      <td>Billing Entity</td>
      <td>CMS directly</td>
      <td>Private insurer (Humana, Aetna, UHC, etc.)</td>
    </tr>
    <tr>
      <td>Appeals</td>
      <td>Medicare appeal ladder (4 levels)</td>
      <td>Plan appeal process, then external review</td>
    </tr>
  </tbody>
</table>

<h2 id="appeals">7. How to Appeal a Medicare Billing Decision</h2>
<p>
  If Medicare denies a claim, reduces payment, or you disagree with your cost-sharing amount,
  you have the right to appeal. There are five levels of appeal for Original Medicare, each with specific deadlines.
</p>
<p>
  <strong>Level 1: Redetermination.</strong> File with your Medicare Administrative Contractor (MAC) within
  120 days of your MSN. The MAC reviews the claim fresh.
</p>
<p>
  <strong>Level 2: Reconsideration.</strong> If denied, file with a Qualified Independent Contractor (QIC)
  within 180 days. This is an independent review outside the original MAC.
</p>
<p>
  <strong>Level 3: ALJ Hearing.</strong> If the disputed amount exceeds $180 (2026 threshold), you can request
  a hearing before an Administrative Law Judge within 60 days of the QIC decision.
</p>
<p>
  <strong>Levels 4&ndash;5: Medicare Appeals Council and Federal Court</strong> are available for high-stakes disputes
  and are rarely needed for billing errors (as opposed to coverage denials).
</p>

<div class="key-takeaway">
  <h3>Key Takeaway 1</h3>
  <p>
    Always compare your actual bill to your Medicare Summary Notice before paying anything.
    The MSN tells you the maximum you legally owe&mdash;if your bill exceeds that amount, dispute it.
    Use the <a href="/scan">BillKarma bill scanner</a> to cross-reference charges against Medicare rates instantly.
  </p>
</div>

<div class="key-takeaway">
  <h3>Key Takeaway 2</h3>
  <p>
    If you were kept overnight in the hospital, confirm in writing whether you were admitted as an inpatient
    or placed under observation. The difference can cost you thousands in SNF care. See how observation status
    affects your bill with our <a href="/calculator">Medicare cost calculator</a>.
  </p>
</div>

<div class="key-takeaway">
  <h3>Key Takeaway 3</h3>
  <p>
    You have 120 days from your MSN to file a Level 1 appeal. Don&rsquo;t wait. Most billing errors are
    correctable if you act within this window. Read our full guide on
    <a href="/guides/how-to-appeal-a-medical-bill">how to appeal a medical bill</a> for a step-by-step walkthrough.
  </p>
</div>

{_embed("medicare-billing-calculator")}

<div class="faq-section">
  <h2>Frequently Asked Questions</h2>

  <div class="faq-item">
    <h3>What is the Medicare Part A deductible?</h3>
    <p>
      The Medicare Part A deductible in 2026 is $1,676 per benefit period. A benefit period starts the day you&rsquo;re
      admitted as an inpatient and ends after you&rsquo;ve been out of the hospital or skilled nursing facility for
      60 consecutive days. You can pay this deductible more than once per year if you have multiple hospital stays
      separated by 60 days.
    </p>
  </div>

  <div class="faq-item">
    <h3>What does Medicare not cover?</h3>
    <p>
      Original Medicare does not cover routine dental, vision, or hearing care, long-term custodial nursing home care,
      most prescription drugs (unless you have Part D), cosmetic surgery, or care received outside the United States.
      Medicare also does not cover services your provider decides are not medically necessary.
    </p>
  </div>

  <div class="faq-item">
    <h3>What is a Medicare crossover claim?</h3>
    <p>
      A Medicare crossover claim is a claim that Medicare automatically forwards to your secondary insurer
      (such as Medicaid or a Medigap policy) after Medicare processes its portion. If you have secondary insurance,
      Medicare coordinates with that plan so you don&rsquo;t have to file a second claim manually.
      Errors in crossover claims are common and can result in unexpected bills.
    </p>
  </div>

  <div class="faq-item">
    <h3>How do I read my Medicare Summary Notice?</h3>
    <p>
      Your Medicare Summary Notice (MSN) arrives quarterly and lists every service billed to Medicare on your behalf.
      Check the provider name, service date, and amount billed. Compare the &ldquo;Medicare-approved amount&rdquo;
      against what you were charged. If Medicare denied a claim or paid less than expected, the MSN shows the reason code.
      You have 120 days from the MSN date to file an appeal.
    </p>
  </div>

  <div class="faq-item">
    <h3>Can doctors balance bill Medicare patients?</h3>
    <p>
      It depends on the provider&rsquo;s participation status. Participating providers accept Medicare assignment
      and cannot charge you more than your coinsurance and deductible. Non-participating providers can charge up to
      15% above the Medicare-approved amount (the &ldquo;limiting charge&rdquo;). Providers who opt out of Medicare
      entirely can charge whatever they want, and Medicare pays nothing.
    </p>
  </div>
</div>

<ul class="sources-list">
  <li><a href="https://www.medicare.gov/your-medicare-costs/medicare-costs-at-a-glance" target="_blank" rel="noopener">Medicare.gov &mdash; 2026 Cost Overview</a></li>
  <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/acute-inpatient-pps" target="_blank" rel="noopener">CMS &mdash; Acute Inpatient Prospective Payment System</a></li>
  <li><a href="https://www.kff.org/medicare/issue-brief/medicare-and-the-observation-status-rule/" target="_blank" rel="noopener">KFF &mdash; Medicare Observation Status Explainer</a></li>
  <li><a href="https://www.hhs.gov/about/agencies/omha/about/index.html" target="_blank" rel="noopener">HHS Office of Medicare Hearings and Appeals</a></li>
  <li><a href="https://www.medicare.gov/claims-appeals/file-an-appeal" target="_blank" rel="noopener">Medicare.gov &mdash; How to File an Appeal</a></li>
</ul>
""",
    },
)
