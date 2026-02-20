"""Guide: Paying Cash at a Hospital."""

from guides import register, _embed

register("hospital-cash-pay-self-pay-discount", {
    "title": "Paying Cash at a Hospital: When Skipping Insurance Actually Saves You Money",
    "meta_description": "Cash prices at hospitals average 52% below gross charges. With high-deductible plans, you may save more paying cash than running through insurance. Here's how to know.",
    "published": "2026-02-20",
    "author": "BillKarma Team",
    "category": "Negotiation",
    "faqs": [
        {
            "q": "Can I pay cash at a hospital even if I have insurance?",
            "a": "Yes. You can choose to pay cash for any service, even if you have active insurance coverage. The hospital cannot require you to bill your insurance. However, you should weigh this carefully: if you pay cash, that payment typically does not count toward your deductible or out-of-pocket maximum, so it may not help you reach the threshold where your insurance starts covering 100% of costs.",
        },
        {
            "q": "What is a discounted cash price at a hospital?",
            "a": "The discounted cash price is one of five price types CMS requires hospitals to post in their machine-readable price transparency files. It is the amount the hospital will accept from a patient who pays out of pocket without going through insurance. It is always lower than the gross charge (the chargemaster list price) and often lower than some negotiated insurance rates, particularly for patients with high-deductible plans.",
        },
        {
            "q": "How do I find a hospital's cash price before my procedure?",
            "a": "CMS requires all hospitals to post their discounted cash prices in a machine-readable file updated annually. BillKarma pulls these prices directly into each hospital's profile page — search our hospital directory by name or city, then look for the cash price column on any procedure. You can also call the hospital's billing department and ask specifically for the 'discounted cash price' or 'self-pay rate' for your CPT code.",
        },
        {
            "q": "Does paying cash affect my insurance deductible?",
            "a": "Generally no. Payments made directly to a provider without going through your insurance plan's claims process do not apply toward your deductible or out-of-pocket maximum. This is why cash payment makes more sense early in the plan year (before you've paid much toward your deductible) and less sense late in the plan year (when you're close to meeting it).",
        },
        {
            "q": "Can a hospital charge me more than my insurance's negotiated rate if I pay cash?",
            "a": "Under CMS price transparency rules, the discounted cash price must be clearly posted, but the rule does not explicitly require it to be lower than negotiated rates. In practice, some hospitals set cash prices higher than their in-network rates with certain insurers. This is a known gap in the transparency rules. BillKarma flags cases where the posted cash price exceeds the estimated insured rate — always compare both before deciding.",
        },
        {
            "q": "Can I negotiate the cash price further even after the hospital posts a discounted rate?",
            "a": "Yes. The posted discounted cash price is a starting point, not a floor. Many hospitals will reduce it further for patients who ask, offer to pay promptly, or demonstrate financial need. Using the Medicare rate as your anchor — typically 40-60% below even the discounted cash price — is the most effective negotiation strategy. A lump-sum payment offer often unlocks an additional 10-20% off the posted cash price.",
        },
    ],
    "body": f"""
<p class="lead">The average hospital&rsquo;s discounted cash price is <strong>52% below the gross charge</strong> for the same procedure, according to BillKarma&rsquo;s analysis of CMS price transparency files. And with more than 60% of Americans now enrolled in high-deductible health plans, millions of patients are effectively paying cash for much of their care anyway &mdash; just at the gross charge rate, without realizing a lower cash price exists. Here&rsquo;s how to find it, use it, and negotiate it further.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#when-cash-makes-sense">When paying cash at a hospital makes sense</a></li>
        <li><a href="#what-is-cash-price">What &ldquo;discounted cash price&rdquo; means and how to find it</a></li>
        <li><a href="#compare-cash-vs-insurance">How to compare cash vs. insurance for your situation</a></li>
        <li><a href="#negotiate-further">How to negotiate the cash price further</a></li>
        <li><a href="#traps">The traps: when cash pricing backfires</a></li>
        <li><a href="#step-by-step">Step-by-step: how to pay cash for a planned procedure</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="when-cash-makes-sense">1. When paying cash at a hospital makes sense</h2>

<p>Paying cash is not always the right move. It depends heavily on where you are in your deductible year and how aggressively your insurer has negotiated rates with your specific hospital. Here is a straightforward decision framework:</p>

<table>
    <thead>
        <tr>
            <th>Your situation</th>
            <th>Pay cash?</th>
            <th>Why</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>You haven&rsquo;t met your deductible and the procedure costs less than your remaining deductible</td><td><strong>Very likely yes</strong></td><td>You&rsquo;re paying out of pocket either way &mdash; the cash price is almost always lower than the insured gross charge you&rsquo;d owe</td></tr>
        <tr><td>You&rsquo;re uninsured</td><td><strong>Yes</strong></td><td>Always ask for the discounted cash price instead of paying the gross charge</td></tr>
        <tr><td>The procedure is elective and shoppable (imaging, colonoscopy, non-urgent surgery)</td><td><strong>Often yes</strong></td><td>You have time to compare cash prices across facilities and negotiate</td></tr>
        <tr><td>Your insurer&rsquo;s negotiated rate at this hospital is close to the cash price</td><td><strong>Depends</strong></td><td>If the negotiated rate is lower, use insurance so the payment counts toward your deductible</td></tr>
        <tr><td>You&rsquo;ve already met your deductible or out-of-pocket maximum</td><td><strong>No</strong></td><td>Your insurance now covers most costs &mdash; cash payment won&rsquo;t count toward your maximum</td></tr>
        <tr><td>The care is emergency, complex, or likely to be expensive</td><td><strong>No</strong></td><td>For high-cost care, hitting your out-of-pocket maximum protects you &mdash; cash leaves you exposed</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The high-deductible blind spot.</strong> If your deductible is $3,000 or more, you are effectively a cash payer for the first portion of every plan year. The difference is that going &ldquo;through insurance&rdquo; often means paying a higher insured rate that your plan applies to your deductible, rather than the lower cash price. Asking for the cash rate first can mean fewer dollars out of pocket for the same care.
</div>

<h2 id="what-is-cash-price">2. What &ldquo;discounted cash price&rdquo; means and how to find it</h2>

<p>Since January 2021, CMS has required all U.S. hospitals to post five specific price types in a machine-readable file, updated annually. The five required types are: gross charge, discounted cash price, payer-specific negotiated rate, de-identified minimum negotiated rate, and de-identified maximum negotiated rate.</p>

<p>The <strong>discounted cash price</strong> is the amount a hospital will accept from a patient paying without insurance. It is distinct from the gross charge (chargemaster list price) in an important way: it is the actual transactable price, not a fictional starting point.</p>

<p>BillKarma pulls cash prices from the <code>hospital_prices.cash_price</code> field in our database, sourced directly from each hospital&rsquo;s CMS transparency file. You can see it on every hospital profile page and in our procedure search.</p>

<p><strong>How to find the cash price for your procedure:</strong></p>
<ol>
    <li>Go to the <a href="/hospitals/">BillKarma hospital directory</a> and search for your facility.</li>
    <li>On the hospital profile, search by CPT code or procedure name. The cash price column shows the posted discounted cash price from that hospital&rsquo;s transparency file.</li>
    <li>Alternatively, call the billing department and ask: &ldquo;What is your discounted cash price for CPT [CODE]?&rdquo; &mdash; they are required to provide it.</li>
    <li>Use the Medicare rate as a cross-check. The cash price should be significantly above the Medicare rate (Medicare is the floor) but well below the gross charge.</li>
</ol>

<p>Here is how these price types typically stack up for common procedures:</p>

<table>
    <thead>
        <tr>
            <th>Procedure</th>
            <th>CPT</th>
            <th>Medicare rate (2026)</th>
            <th>Typical cash price</th>
            <th>Typical gross charge</th>
            <th>Cash savings vs. gross charge</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>MRI lumbar spine</td><td>72148</td><td>$97</td><td>$350&ndash;$700</td><td>$800&ndash;$2,200</td><td>40&ndash;65% off</td></tr>
        <tr><td>Colonoscopy (diagnostic)</td><td>45380</td><td>$198</td><td>$600&ndash;$1,200</td><td>$1,500&ndash;$4,000</td><td>45&ndash;70% off</td></tr>
        <tr><td>Chest X-ray (2 views)</td><td>71046</td><td>$13</td><td>$50&ndash;$150</td><td>$200&ndash;$600</td><td>50&ndash;75% off</td></tr>
        <tr><td>ER visit level 3</td><td>99283</td><td>$106</td><td>$300&ndash;$650</td><td>$900&ndash;$2,500</td><td>40&ndash;65% off</td></tr>
    </tbody>
</table>

<p>Medicare rates serve as a useful floor: a hospital&rsquo;s cash price should not exceed the gross charge, and the further it is above the Medicare rate, the more room there is to negotiate. Use our calculator to look up the Medicare rate for any CPT code on your bill:</p>

{_embed(mode="cost", title="Look up Medicare rates &mdash; your cash price floor", subtitle="Enter a CPT code to see the 2026 Medicare facility rate.", height="380")}

<h2 id="compare-cash-vs-insurance">3. How to compare cash vs. insurance for your specific situation</h2>

<p>The comparison requires knowing three numbers: the hospital&rsquo;s posted cash price, your insurer&rsquo;s negotiated rate at that hospital, and how much of your deductible you have left to meet.</p>

<p>Your insurer&rsquo;s negotiated rate is not always easy to find, but the Explanation of Benefits (EOB) from a previous claim at the same hospital will show what your plan&rsquo;s allowed amount was. Alternatively, your insurer&rsquo;s price transparency tool (required by CMS since 2022) must show procedure-level negotiated rates.</p>

<p><strong>The math you need to do:</strong></p>

<ol>
    <li><strong>Cash path:</strong> [Cash price] = your total out-of-pocket. This does not count toward your deductible.</li>
    <li><strong>Insurance path:</strong> If your deductible is not met, you pay [negotiated rate] until deductible is reached, then your coinsurance rate kicks in. If the negotiated rate is lower than the cash price, and you want the payment to apply toward your deductible, use insurance.</li>
    <li><strong>Break-even question:</strong> Is the cash price lower than what I would pay under insurance (applying the remainder of my deductible)? If yes, and if you don&rsquo;t expect to meet your deductible this year, cash wins.</li>
</ol>

<div class="bill-example">
    <div class="bill-header">Cash vs. Insurance: MRI Lumbar Spine (CPT 72148) &mdash; Example Comparison</div>
    <div class="line-item">
        <span>Hospital gross charge (list price)</span>
        <span>$1,400</span>
    </div>
    <div class="line-item">
        <span>Hospital discounted cash price</span>
        <span>$490</span>
    </div>
    <div class="line-item">
        <span>Insurer&rsquo;s negotiated rate (in-network)</span>
        <span>$420</span>
    </div>
    <div class="line-item">
        <span>Patient&rsquo;s remaining deductible</span>
        <span>$1,800</span>
    </div>
    <div class="line-item">
        <span>What patient pays through insurance (deductible not met)</span>
        <span>$420</span>
    </div>
    <div class="line-item flagged">
        <span>Cash price vs. insured rate difference &nbsp; &#9888; <em>Insurance wins here by $70</em></span>
        <span>$70 more by cash</span>
    </div>
    <div class="line-total">
        <span>Verdict: use insurance &mdash; but confirm deductible won&rsquo;t be met this year</span>
        <span>&nbsp;</span>
    </div>
</div>

<p>Notice that in this example the insurer&rsquo;s negotiated rate ($420) is actually lower than the hospital&rsquo;s cash price ($490). This is a common scenario at hospitals with aggressive commercial contracting. The cash price is not always the cheapest option &mdash; you must compare all three numbers.</p>

<p>However, if this patient&rsquo;s deductible were $800 (not $1,800), they might be close enough to meeting it that running the claim through insurance to hit the deductible threshold would be the smarter play for the rest of the plan year.</p>

<div class="key-takeaway">
    <strong>See your hospital&rsquo;s cash prices by procedure.</strong> The <a href="/hospitals/">BillKarma hospital directory</a> shows posted cash prices from CMS transparency files alongside the Medicare rate, so you can calculate your actual comparison before you schedule.
</div>

<h2 id="negotiate-further">4. How to negotiate the cash price further</h2>

<p>The posted discounted cash price is not the floor. Most hospitals will go lower for patients who ask, and especially for patients who can pay promptly. Here are the approaches that work:</p>

<h3>Anchor to the Medicare rate</h3>

<p>The Medicare rate is what the federal government pays for the same service based on a detailed cost analysis. If a hospital accepts Medicare patients &mdash; and virtually all do &mdash; they receive the Medicare rate and do not lose money on it. This makes it the most credible negotiation anchor available to patients.</p>

<div class="case-study">
    <h3>Phone script: negotiating below the posted cash price</h3>
    <p>&ldquo;I&rsquo;m planning to pay cash for [PROCEDURE], CPT [CODE]. I saw your posted discounted cash price is $[AMOUNT]. I&rsquo;ve also looked at the Medicare rate for this procedure, which is approximately $[MEDICARE RATE]. I&rsquo;d like to pay promptly by [date] and settle this in full. Would you be willing to accept $[1.5&ndash;2.5x Medicare] to resolve this today?&rdquo;</p>
    <p><em>Be specific. A concrete offer is harder to decline than a vague request for a discount.</em></p>
</div>

<h3>Offer prompt payment</h3>

<p>Hospitals collect a fraction of gross charges even from insured patients. Cash in hand today, with no claims processing, no denial risk, no appeals, and no collections process, is valuable to a billing department. A prompt-pay offer of 2&ndash;3x Medicare, paid within 10 business days, often beats the posted cash price by 15&ndash;30%.</p>

<h3>Ask about charity care at the same time</h3>

<p>If your income is below 400% of the Federal Poverty Level (approximately $62,400 for an individual in 2026), you may qualify for financial assistance on top of any cash discount. All nonprofit hospitals are required to have financial assistance programs under IRS Section 501(r). Ask both questions: &ldquo;What is your discounted cash rate, and what financial assistance programs do you offer?&rdquo; See our full guide to <a href="/guides/hospital-billing-grades-explained">hospital billing grades</a> for context on whether your hospital is likely to have generous financial assistance policies.</p>

<h2 id="traps">5. The traps: when cash pricing backfires</h2>

<p>Cash pricing has real downsides that catch patients off guard. Know these before you opt out of insurance:</p>

<h3>Trap 1: The cash price is higher than the insured rate</h3>

<p>Under the CMS price transparency rule, hospitals must post their discounted cash price, but the rule does not require it to be lower than all negotiated insurance rates. Some hospitals &mdash; particularly those with highly favorable commercial contracts &mdash; have negotiated rates from major insurers that are actually lower than the posted cash price.</p>

<p>According to a 2022 Health Affairs analysis, a meaningful percentage of uninsured patients at certain hospitals pay more than insured patients for the same services, because the hospital does not aggressively discount for self-pay patients. BillKarma flags this on hospital profiles when the posted cash price exceeds the estimated in-network rate range.</p>

<h3>Trap 2: Cash payments don&rsquo;t count toward your deductible</h3>

<p>If you pay cash for a $600 procedure, that $600 does not count toward your $3,000 deductible. If you were going to hit your deductible this year anyway, you essentially paid $600 out of pocket for nothing &mdash; and still have $3,000 left to pay before insurance kicks in.</p>

<h3>Trap 3: Surprise billing from affiliated providers</h3>

<p>If you negotiate a cash price with the hospital facility, be aware that other providers involved in your care &mdash; the anesthesiologist, the radiologist reading your scan, the pathologist reviewing a biopsy &mdash; may bill separately, and your cash deal with the facility does not cover them. Each provider must be negotiated with individually.</p>

<h3>Trap 4: Catastrophic cost exposure</h3>

<p>For complex, multi-day, or unpredictably expensive care, bypassing insurance removes your annual out-of-pocket maximum protection. A planned $2,000 procedure that turns into a $40,000 complication leaves you with no limit on what you owe if you&rsquo;re paying cash. Only use cash for shoppable, predictable procedures where the scope of care is well defined.</p>

<div class="key-takeaway">
    <strong>Before you decide, scan your bill or estimate first.</strong> <a href="/scan">Upload an existing bill to BillKarma</a> &mdash; we show you the cash price, the Medicare rate, and estimated insured rate for every procedure, so you can make the comparison with real numbers before your next visit.
</div>

<h2 id="step-by-step">6. Step-by-step: how to pay cash for a planned procedure</h2>

<p><strong>Step 1: Get your CPT codes in advance.</strong> Ask your doctor&rsquo;s office for the CPT codes they plan to use. For most scheduled procedures &mdash; imaging, colonoscopy, outpatient surgery &mdash; the codes are known before the appointment. Without CPT codes, you can&rsquo;t compare prices meaningfully.</p>

<p><strong>Step 2: Look up the hospital&rsquo;s posted cash price for each code.</strong> Use the <a href="/hospitals/">BillKarma hospital directory</a> or call the billing department. Get the price in writing (email is fine; ask for it to be confirmed by a supervisor or in a price quote letter).</p>

<p><strong>Step 3: Look up the Medicare rate for each code.</strong> Use our <a href="/calculator">calculator</a> to see the 2026 Medicare facility rate. This is your negotiation floor and your benchmark for whether the cash price is reasonable.</p>

<p><strong>Step 4: Compare the cash price to your insured rate.</strong> Check your insurer&rsquo;s price transparency tool or your EOB from a prior claim at the same facility to get the negotiated rate. If the insured rate is lower than the cash price, calculate whether hitting your deductible is worth more to you than the cash savings.</p>

<p><strong>Step 5: Negotiate if the cash price is more than 3x the Medicare rate.</strong> Call the billing department, reference the Medicare rate, and make a specific prompt-pay offer. A good target: 2.0&ndash;2.5x the Medicare rate, paid within 10 business days.</p>

<p><strong>Step 6: Get the agreed price confirmed in writing before your appointment.</strong> Ask for a price guarantee letter or a written quote on hospital letterhead. Verbal agreements with billing staff can be overridden by the facility&rsquo;s chargemaster system at check-in.</p>

<p><strong>Step 7: Pay after the procedure, once you confirm no unexpected services were added.</strong> If you pre-pay in full, it is harder to dispute add-on charges. Pay by credit card so you have dispute rights if the final bill differs from the agreed price.</p>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Case 1: Uninsured patient negotiates colonoscopy from $2,800 to $590</h3>
    <p>A 52-year-old self-employed patient in North Carolina needed a diagnostic colonoscopy (CPT 45380). Uninsured, she initially received a quote of $2,800 &mdash; the hospital&rsquo;s gross charge. She called BillKarma&rsquo;s hospital directory, found the facility&rsquo;s posted discounted cash price of $980, and looked up the Medicare rate of $198.</p>
    <p>She called the billing department and offered to pay $590 in full within five business days ($590 is approximately 3x the Medicare rate). The billing supervisor countered at $720. She accepted.</p>
    <p><strong>Gross charge: $2,800. Final cash price paid: $720. Savings: $2,080 (74% off gross charge).</strong></p>
    <p>She also asked about the pathology bill separately &mdash; the colonoscopy included biopsy specimens read by a separate pathology group. She negotiated that bill to $95 from a $380 gross charge, using the same Medicare-rate anchor approach.</p>
</div>

<div class="case-study">
    <h3>Case 2: HDHP patient saves $340 by paying cash before meeting deductible</h3>
    <p>A patient in Minnesota with a $4,000 deductible needed an MRI of the lumbar spine (CPT 72148) in January &mdash; early in the plan year, with $4,000 remaining on his deductible. His insurer&rsquo;s negotiated rate at the in-network hospital was $480. The hospital&rsquo;s posted discounted cash price was $310. Medicare&rsquo;s 2026 rate for 72148 is $97.</p>
    <p>Since his deductible was $4,000 and he was unlikely to hit it that year based on his expected care, the insured path meant paying $480 out of pocket with the payment counting toward the deductible he&rsquo;d never reach anyway. The cash path cost $310.</p>
    <p><strong>Insured out-of-pocket: $480. Cash out-of-pocket: $310. Savings: $170 on this one procedure.</strong></p>
    <p>He applied the same analysis to three other imaging studies that year and saved $340 total by choosing cash &mdash; while correctly running a $6,800 surgery through insurance in October, by which point his deductible was nearly met from a prior hospitalization.</p>
</div>

<div class="case-study">
    <h3>Case 3: Patient discovers cash price is higher than in-network rate &mdash; and uses insurance instead</h3>
    <p>A patient in Texas scheduled a chest X-ray (CPT 71046) and ER level 3 visit follow-up (CPT 99283) at a large regional hospital. The hospital&rsquo;s posted discounted cash price was $380 for the two services combined. Medicare&rsquo;s rates: $13 (71046) + $106 (99283) = $119 combined.</p>
    <p>Before paying cash, she checked her insurer&rsquo;s price transparency tool and found her plan&rsquo;s negotiated rate at that hospital was $210 for the same two codes. The cash price of $380 was <strong>81% higher</strong> than her insured rate.</p>
    <p>She ran the claim through insurance. Her out-of-pocket under the insured rate (applied to her remaining deductible) was $210 &mdash; $170 less than the cash price. The cash price was not a discount at all at this facility for these specific services.</p>
    <p><strong>Posted cash price: $380. Actual insured out-of-pocket: $210. Choosing insurance saved: $170.</strong></p>
    <p>This case illustrates why cash pricing is not automatically better &mdash; and why checking your insurer&rsquo;s negotiated rate for the same facility and codes is essential before opting out of insurance. BillKarma now flags hospitals where the posted cash price exceeds estimated in-network rates by more than 20%, based on transparency file data. Check your hospital&rsquo;s profile in our <a href="/hospitals/">directory</a> before your next procedure.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can I pay cash at a hospital even if I have insurance?</h3>
        <p>Yes. You can pay cash for any service regardless of whether you have insurance. The hospital cannot require you to bill your insurance. However, cash payments do not count toward your deductible or out-of-pocket maximum, so weigh whether you&rsquo;re likely to hit those thresholds during the plan year before opting out of insurance for a given procedure.</p>
    </div>
    <div class="faq-item">
        <h3>What is a discounted cash price at a hospital?</h3>
        <p>It is one of five price types CMS requires hospitals to post in their annual machine-readable price transparency files. It is the amount a hospital will accept from a patient paying without going through insurance &mdash; always lower than the gross charge (chargemaster price), and sometimes lower than some insurers&rsquo; negotiated rates. BillKarma pulls these prices from the <code>hospital_prices.cash_price</code> field for every hospital in our database.</p>
    </div>
    <div class="faq-item">
        <h3>How do I find a hospital&rsquo;s cash price before my procedure?</h3>
        <p>Use the <a href="/hospitals/">BillKarma hospital directory</a> to search your facility and look up cash prices by CPT code. You can also call the hospital&rsquo;s billing department and ask specifically for &ldquo;the discounted cash price for CPT [CODE].&rdquo; Under CMS transparency rules, they are required to provide this. Always get it in writing before your appointment.</p>
    </div>
    <div class="faq-item">
        <h3>Does paying cash affect my insurance deductible?</h3>
        <p>Generally no. Cash payments made directly to a provider without going through your plan&rsquo;s claims process do not apply toward your deductible or out-of-pocket maximum. This matters most if you expect to hit your deductible &mdash; in that case, use insurance so the payment counts. If you&rsquo;re unlikely to hit your deductible this plan year, cash may save you money upfront without any deductible benefit lost.</p>
    </div>
    <div class="faq-item">
        <h3>Can a hospital charge me more than my insurance&rsquo;s negotiated rate if I pay cash?</h3>
        <p>Yes, this happens. CMS transparency rules require cash prices to be posted, but do not require them to be lower than all negotiated insurance rates. At hospitals with strong commercial contracts, insured patients can sometimes pay less than the posted cash price. BillKarma flags this situation. Always compare both before deciding. See <a href="/guides/hospital-billing-grades-explained">our hospital billing grades guide</a> for context on which types of hospitals tend to price this way.</p>
    </div>
    <div class="faq-item">
        <h3>Can I negotiate the cash price below what the hospital posts?</h3>
        <p>Yes. The posted discounted cash price is not a floor. Hospitals routinely accept less for patients who can pay promptly and in full. Use the Medicare rate as your anchor &mdash; look it up with our <a href="/calculator">calculator</a> &mdash; and offer 2&ndash;2.5x Medicare as a prompt-pay lump sum. Many hospitals will accept this over the posted cash price for uncomplicated outpatient services.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency" target="_blank" rel="noopener">CMS: Hospital Price Transparency Rule &mdash; Requirements including discounted cash price (2021, updated 2026)</a></li>
    <li><a href="https://www.rand.org/pubs/research_reports/RRA1144-2.html" target="_blank" rel="noopener">RAND Corporation: Hospital Price Transparency Study &mdash; Cash Prices vs. Negotiated Rates (2023)</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2021.01420" target="_blank" rel="noopener">Health Affairs: Uninsured Patients and Hospital Pricing &mdash; When Self-Pay Costs More (2022)</a></li>
    <li><a href="https://www.kff.org/health-costs/report/2024-employer-health-benefits-survey/" target="_blank" rel="noopener">KFF: Employer Health Benefits Survey &mdash; High-Deductible Health Plan Enrollment Trends (2024)</a></li>
    <li><a href="https://www.hfma.org/topics/hfma-s-patient-friendly-billing-project/self-pay-discount-benchmarks.html" target="_blank" rel="noopener">HFMA: Hospital Charity Care and Self-Pay Discount Benchmarks</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/hospital-outpatient" target="_blank" rel="noopener">CMS: Outpatient Prospective Payment System (OPPS) &mdash; 2026 Final Rule</a></li>
</ul>
""",
})
