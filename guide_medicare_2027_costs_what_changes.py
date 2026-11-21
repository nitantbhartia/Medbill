"""Guide: Medicare 2027 Costs: Deductibles, Drug Cap, New Prices."""

from guides import register

register("medicare-2027-costs-what-changes", {
    "title": "Medicare 2027 Costs: Deductibles, Drug Cap, New Prices",
    "meta_description": "Medicare 2027 costs: Part B is $209.40 a month, the Part A deductible is $1,776, and the Part D drug cap rises to $2,400. What to check by Dec. 7.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is the Medicare Part B premium and deductible for 2027?",
            "a": "CMS announced on November 17, 2026 that the standard Part B premium will be $209.40 a month in 2027, up from $202.90 in 2026. The yearly Part B deductible will be $292, up from $283.",
        },
        {
            "q": "What is the Medicare Part A hospital deductible for 2027?",
            "a": "The Part A inpatient hospital deductible is $1,776 for each benefit period in 2027, up from $1,736 in 2026. A benefit period starts when you are admitted as an inpatient and ends after you have gone 60 days in a row without inpatient hospital or skilled nursing facility care.",
        },
        {
            "q": "What is the Medicare Part D out-of-pocket cap for 2027?",
            "a": "For 2027, the Part D out-of-pocket threshold is $2,400, up from $2,100 in 2026. The highest deductible a Part D plan can charge rises to $700, up from $615. Once your out-of-pocket spending on covered drugs reaches the threshold, you pay nothing more for covered Part D drugs for the rest of the year.",
        },
        {
            "q": "Will I pay less for Ozempic or Wegovy in 2027 because of Medicare negotiation?",
            "a": "Maybe. CMS negotiated a price of $274 for a 30-day supply of Ozempic, Rybelsus and Wegovy, starting January 1, 2027. That is the price Medicare plans pay. What you pay depends on your plan: if you pay coinsurance (a percentage), a lower price can lower your share; if you pay a flat copay, your cost may not change. Your plan must also cover the drug for your condition, so check its formulary.",
        },
        {
            "q": "Does the Medicare Prescription Payment Plan lower my drug costs?",
            "a": "No. Medicare.gov says the payment plan does not save you money or lower your drug costs. It spreads what you owe for covered drugs into monthly bills from your plan across the calendar year.",
        },
        {
            "q": "When is Medicare open enrollment for 2027 coverage?",
            "a": "Open enrollment runs from October 15 to December 7, 2026. Your plan must get your request by December 7, and changes generally start January 1, 2027. If you are in a Medicare Advantage plan, you get one more chance to switch from January 1 to March 31.",
        },
    ],
    "body": f"""
<p class="lead">In November 2026, CMS announced what Medicare Parts A and B will cost in 2027, adding to April&rsquo;s news that the Part D drug cap rises to $2,400 and lower negotiated prices for 15 drugs, including Ozempic and Wegovy, start January 1, 2027. In short: your Part B premium goes to $209.40 a month, a hospital stay starts with a $1,776 deductible, and you have until December 7, 2026 to pick the plan that fits those costs best.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#numbers">2026 vs 2027: the numbers</a></li>
        <li><a href="#your-bill">What this means for your bill</a></li>
        <li><a href="#hospital">Hospital costs: deductibles, observation status and your MSN</a></li>
        <li><a href="#part-d">Part D in 2027: the $700 deductible and $2,400 cap</a></li>
        <li><a href="#negotiated-drugs">The 15 negotiated drugs and what &ldquo;Maximum Fair Price&rdquo; means</a></li>
        <li><a href="#payment-plan">Spreading drug costs: the Medicare Prescription Payment Plan</a></li>
        <li><a href="#before-dec-7">What to check before December 7</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="numbers">1. 2026 vs 2027: the numbers</h2>

<p>CMS (the Centers for Medicare &amp; Medicaid Services, the agency that runs Medicare) released the 2027 Part A and Part B amounts on November 17, 2026. It set the 2027 Part D amounts in its rate announcement on April 6, 2026. CMS says the higher Part B premium and deductible are &ldquo;mainly due to projected increases in healthcare spending.&rdquo;</p>

<table>
    <thead>
        <tr><th>Cost</th><th>2026</th><th>2027</th><th>Source</th></tr>
    </thead>
    <tbody>
        <tr><td>Part B standard monthly premium</td><td>$202.90</td><td>$209.40</td><td>CMS, Nov. 2026</td></tr>
        <tr><td>Part B yearly deductible</td><td>$283</td><td>$292</td><td>CMS, Nov. 2026</td></tr>
        <tr><td>Part A hospital deductible (per benefit period)</td><td>$1,736</td><td>$1,776</td><td>CMS, Nov. 2026</td></tr>
        <tr><td>Part A coinsurance, hospital days 61&ndash;90</td><td>$434 a day</td><td>$444 a day</td><td>CMS, Nov. 2026</td></tr>
        <tr><td>Part A coinsurance, lifetime reserve days</td><td>$868 a day</td><td>$888 a day</td><td>CMS, Nov. 2026</td></tr>
        <tr><td>Skilled nursing facility, days 21&ndash;100</td><td>$217 a day</td><td>$222 a day</td><td>CMS, Nov. 2026</td></tr>
        <tr><td>Part D maximum deductible</td><td>$615</td><td>$700</td><td>CMS, Apr. 2026</td></tr>
        <tr><td>Part D out-of-pocket cap</td><td>$2,100</td><td>$2,400</td><td>CMS, Apr. 2026</td></tr>
    </tbody>
</table>

<p>About 99% of people with Medicare pay no Part A premium, according to CMS. People with higher incomes pay more than the standard Part B premium.</p>

<h2 id="your-bill">2. What this means for your bill</h2>

<ul>
    <li><strong>Your monthly cost rises a little.</strong> The standard Part B premium goes up $6.50 a month.</li>
    <li><strong>A hospital stay costs more up front.</strong> In Original Medicare, the first inpatient stay in a benefit period now starts with a $1,776 deductible, unless a Medigap (supplement) policy or other coverage pays it.</li>
    <li><strong>Your drug spending has a higher ceiling.</strong> The most you pay out of pocket for covered Part D drugs in 2027 is $2,400, up $300.</li>
    <li><strong>Some drug prices drop.</strong> Medicare plans will pay lower negotiated prices for 15 drugs. Whether your copay drops depends on how your plan sets cost sharing.</li>
    <li><strong>Your plan can change too.</strong> Premiums, networks and drug lists can change on January 1, so comparing plans now can help you avoid surprises.</li>
</ul>

<div class="key-takeaway"><h3>Key takeaway</h3><p>Higher deductibles mean more of your first hospital bill of 2027 may land on you. Before you pay a hospital bill, compare it with your Medicare Summary Notice using our guide to <a href="/guides/medicare-summary-notice-vs-hospital-bill/">reading an MSN next to a hospital bill</a>, or <a href="/scan">check your bill free</a>.</p></div>

<h2 id="hospital">3. Hospital costs: deductibles, observation status and your MSN</h2>

<h3>The Part A deductible is per benefit period, not per year</h3>

<p>Under Original Medicare, the Part A deductible applies to each <strong>benefit period</strong>. A benefit period starts the day you are admitted as an inpatient. It ends once you have gone 60 days in a row without inpatient care in a hospital or skilled nursing facility. Medicare.gov notes there is no limit on how many benefit periods you can have in a year.</p>

<p>After the deductible, you pay $0 a day for days 1&ndash;60 of a benefit period. In 2027 you pay $444 a day for days 61&ndash;90 and $888 a day for any lifetime reserve days.</p>

<p><em>Example:</em> In 2027 you are admitted in March, go home, and are admitted again in July, more than 60 days later. That is two benefit periods, so under Original Medicare with no supplement you could owe two deductibles: $1,776 &times; 2 = $3,552.</p>

<h3>Observation status changes what you pay</h3>

<p>You can spend the night in a hospital bed and still be an <strong>outpatient</strong> under &ldquo;observation status.&rdquo; Your hospital care is then covered under Part B, not Part A. Instead of one Part A deductible, you generally pay the Part B deductible and a copayment for each outpatient service. Medicare.gov notes that no single outpatient service&rsquo;s copayment can be more than the inpatient deductible, but your total for all services can be. Observation also matters for nursing home care: Medicare covers skilled nursing facility care only after an inpatient stay of at least 3 days in a row, and Medicare.gov says observation time does not count toward those 3 days.</p>

<p>If you are under observation for more than 24 hours, the hospital must give you a Medicare Outpatient Observation Notice (MOON) no later than 36 hours after observation starts, or sooner if you leave. The notice explains that you are an outpatient and what that means for your costs and skilled nursing coverage. Our guide to <a href="/guides/medicare-observation-status-billing/">observation status billing</a> covers what to ask.</p>

<h3>Your Medicare Summary Notice is your check</h3>

<p>If you have Original Medicare, the Medicare Summary Notice (MSN) lists the Part A and Part B services billed to Medicare, what Medicare paid, and the most you may owe the provider. It is not a bill. Medicare.gov suggests comparing it with your bills, and electronic MSNs let you see processed claims sooner. If a hospital bill asks for more than the MSN says you may owe, ask the billing office why before you pay.</p>

<h2 id="part-d">4. Part D in 2027: the $700 deductible and $2,400 cap</h2>

<p>Part D is Medicare&rsquo;s prescription drug coverage, offered through standalone drug plans or Medicare Advantage plans. In CMS&rsquo;s standard Part D design for 2027:</p>

<ul>
    <li><strong>Deductible phase:</strong> you pay the full cost of covered drugs until you reach the deductible. The maximum a plan can charge is $700 in 2027; a plan can set a lower deductible.</li>
    <li><strong>Initial coverage phase:</strong> you pay 25% of the cost of covered drugs in the standard design. Your plan may use copays or coinsurance by tier instead.</li>
    <li><strong>Catastrophic phase:</strong> once your out-of-pocket spending reaches $2,400, you pay nothing for covered Part D drugs for the rest of 2027.</li>
</ul>

<p>The cap covers only drugs on your plan&rsquo;s formulary (its list of covered drugs). It does not include your monthly premium. A drug your plan does not cover does not count toward the cap. For a refresher on the phases, see <a href="/guides/medicare-part-d-explained/">Medicare Part D explained</a>.</p>

<h2 id="negotiated-drugs">5. The 15 negotiated drugs and what &ldquo;Maximum Fair Price&rdquo; means</h2>

<p>Under the Medicare Drug Price Negotiation Program, CMS negotiated prices for 15 Part D drugs that take effect January 1, 2027. The law calls these negotiated prices <strong>Maximum Fair Prices</strong>. The 15 drugs are: Austedo/Austedo XR, Breo Ellipta, Calquence, Ibrance, Janumet/Janumet XR, Linzess, Ofev, Otezla/Otezla XR, Ozempic/Rybelsus/Wegovy, Pomalyst, Tradjenta, Trelegy Ellipta, Vraylar, Xifaxan and Xtandi.</p>

<table>
    <thead>
        <tr><th>Drug (examples)</th><th>Common uses</th><th>2024 list price, 30 days</th><th>2027 negotiated price, 30 days</th></tr>
    </thead>
    <tbody>
        <tr><td>Ozempic; Rybelsus; Wegovy</td><td>Type 2 diabetes; heart disease; obesity/overweight</td><td>$959</td><td>$274</td></tr>
        <tr><td>Trelegy Ellipta</td><td>Asthma; COPD</td><td>$654</td><td>$175</td></tr>
        <tr><td>Linzess</td><td>Constipation; IBS with constipation</td><td>$539</td><td>$136</td></tr>
        <tr><td>Xtandi</td><td>Prostate cancer</td><td>$13,480</td><td>$7,004</td></tr>
        <tr><td>Ibrance</td><td>Breast cancer</td><td>$15,741</td><td>$7,871</td></tr>
    </tbody>
</table>

<p>Source: CMS fact sheet on negotiated prices for 2027. CMS estimates people with Part D coverage would save about $685 million in out-of-pocket costs under the standard benefit once these prices take effect.</p>

<h3>What the negotiated price means for what you pay</h3>

<p>The Maximum Fair Price is the price Medicare drug plans pay for the drug. It is not a promise about your copay. As KFF explains, your savings depend on whether your plan charges coinsurance or a flat copay:</p>

<ul>
    <li><strong>Coinsurance (a percentage):</strong> a lower price lowers your share. <em>Example:</em> 25% of a $274 negotiated price is $68.50 a month.</li>
    <li><strong>Flat copay:</strong> your copay may stay the same even though the plan pays less.</li>
    <li><strong>Deductible phase:</strong> if you pay full price until you meet the deductible, a lower price means you pay less during that phase.</li>
</ul>

<p>Your plan also has to cover the drug for your condition. Check each plan&rsquo;s formulary for your exact drug and use. See our <a href="/guides/glp1-drug-coverage/">GLP-1 drug coverage</a> guide.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>A lower negotiated price helps most when you pay coinsurance or are still in your deductible. Learn how tiers set your share in <a href="/guides/how-drug-formulary-tiers-work/">how drug formulary tiers work</a> before you pick a 2027 plan.</p></div>

<h2 id="payment-plan">6. Spreading drug costs: the Medicare Prescription Payment Plan</h2>

<p>If expensive prescriptions mean you could reach the $2,400 cap early in the year, the Medicare Prescription Payment Plan can help with cash flow. Instead of paying the pharmacy for covered drugs, you get a monthly bill from your drug plan that spreads those costs across the calendar year.</p>

<ul>
    <li>All Medicare drug plans and Medicare Advantage plans with drug coverage offer it, and joining is voluntary.</li>
    <li>Medicare.gov says there is no cost to participate.</li>
    <li>It <strong>does not lower</strong> your drug costs. It changes when you pay, not how much.</li>
    <li>Starting in 2026, CMS rules renew your participation for the next year unless you opt out. If you switch plans, contact your new plan to ask how to sign up.</li>
</ul>

<p>You still pay your monthly premium as usual. To sign up, contact your plan.</p>

<h2 id="before-dec-7">7. What to check before December 7</h2>

<p>During open enrollment (October 15 to December 7, 2026), you can switch between Original Medicare and Medicare Advantage, change Medicare Advantage plans, or join, drop or switch a drug plan. Your plan must get your request by December 7, and coverage generally starts January 1, 2027.</p>

<ol>
    <li><strong>Make a list of every drug you take,</strong> with the dose and how often. Medicare.gov advises adding all the drugs you take regularly so cost estimates are accurate.</li>
    <li><strong>Use the Medicare Plan Finder</strong> at Medicare.gov/plan-compare. Compare monthly premiums, deductibles and estimated yearly drug costs, not just the premium.</li>
    <li><strong>Check each plan&rsquo;s formulary</strong> for your drugs, their tier, and any prior authorization or quantity limits.</li>
    <li><strong>Check networks.</strong> If you are looking at Medicare Advantage, confirm your doctors, your hospital and your pharmacy are in network for 2027.</li>
    <li><strong>Look at hospital costs.</strong> For Medicare Advantage, find the inpatient copay and the plan&rsquo;s yearly out-of-pocket limit. For Original Medicare, think about how you would cover the $1,776 deductible; see our <a href="/guides/medigap-medicare-supplement-guide/">Medigap guide</a>.</li>
    <li><strong>Keep your paperwork,</strong> including plan confirmations and, in 2027, your MSNs or plan Explanation of Benefits.</li>
</ol>

<div class="key-takeaway"><h3>Key takeaway</h3><p>Spreading costs helps your budget but does not shrink what you owe, so it still pays to make sure each charge is right. If a hospital or pharmacy bill looks off, <a href="/scan">check your bill free</a> or read <a href="/guides/prescription-drug-billing-errors/">common prescription billing errors</a>.</p></div>

<p>If you are in a Medicare Advantage plan and change your mind, the Medicare Advantage Open Enrollment Period from January 1 to March 31, 2027 lets you switch to another Medicare Advantage plan or return to Original Medicare and join a drug plan. For questions, you can call 1-800-MEDICARE.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the Medicare Part B premium and deductible for 2027?</h3>
        <p>CMS announced on November 17, 2026 that the standard Part B premium will be $209.40 a month in 2027, up from $202.90 in 2026. The yearly Part B deductible will be $292, up from $283.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Medicare Part A hospital deductible for 2027?</h3>
        <p>The Part A inpatient hospital deductible is $1,776 for each benefit period in 2027, up from $1,736 in 2026. A benefit period starts when you are admitted as an inpatient and ends after you have gone 60 days in a row without inpatient hospital or skilled nursing facility care.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Medicare Part D out-of-pocket cap for 2027?</h3>
        <p>For 2027, the Part D out-of-pocket threshold is $2,400, up from $2,100 in 2026. The highest deductible a Part D plan can charge rises to $700, up from $615. Once your out-of-pocket spending on covered drugs reaches the threshold, you pay nothing more for covered Part D drugs for the rest of the year.</p>
    </div>
    <div class="faq-item">
        <h3>Will I pay less for Ozempic or Wegovy in 2027 because of Medicare negotiation?</h3>
        <p>Maybe. CMS negotiated a price of $274 for a 30-day supply of Ozempic, Rybelsus and Wegovy, starting January 1, 2027. That is the price Medicare plans pay. What you pay depends on your plan: if you pay coinsurance (a percentage), a lower price can lower your share; if you pay a flat copay, your cost may not change. Your plan must also cover the drug for your condition, so check its formulary.</p>
    </div>
    <div class="faq-item">
        <h3>Does the Medicare Prescription Payment Plan lower my drug costs?</h3>
        <p>No. Medicare.gov says the payment plan does not save you money or lower your drug costs. It spreads what you owe for covered drugs into monthly bills from your plan across the calendar year.</p>
    </div>
    <div class="faq-item">
        <h3>When is Medicare open enrollment for 2027 coverage?</h3>
        <p>Open enrollment runs from October 15 to December 7, 2026. Your plan must get your request by December 7, and changes generally start January 1, 2027. If you are in a Medicare Advantage plan, you get one more chance to switch from January 1 to March 31.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/2027-medicare-parts-b-premiums-deductibles" target="_blank" rel="noopener">CMS &mdash; 2027 Medicare Parts A &amp; B Premiums and Deductibles (November 17, 2026)</a></li>
    <li><a href="https://www.cms.gov/files/document/2027-announcement.pdf" target="_blank" rel="noopener">CMS &mdash; Announcement of CY 2027 MA Capitation Rates and Part C and Part D Payment Policies (April 6, 2026), Tables V-2 and V-6</a></li>
    <li><a href="https://www.cms.gov/files/document/fact-sheet-negotiated-prices-ipay-2027.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Drug Price Negotiation Program: Negotiated Prices for Initial Price Applicability Year 2027</a></li>
    <li><a href="https://www.cms.gov/priorities/medicare-prescription-drug-affordability/overview/medicare-drug-price-negotiation-program/selected-drugs-and-negotiated-prices" target="_blank" rel="noopener">CMS &mdash; Selected Drugs and Negotiated Prices</a></li>
    <li><a href="https://www.kff.org/medicare/key-facts-about-medicare-drug-price-negotiation/" target="_blank" rel="noopener">KFF &mdash; Key Facts About Medicare Drug Price Negotiation</a></li>
    <li><a href="https://www.medicare.gov/basics/costs/medicare-costs" target="_blank" rel="noopener">Medicare.gov &mdash; Medicare costs</a></li>
    <li><a href="https://www.medicare.gov/coverage/inpatient-hospital-care" target="_blank" rel="noopener">Medicare.gov &mdash; Inpatient hospital care</a></li>
    <li><a href="https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-409/subpart-F/section-409.60" target="_blank" rel="noopener">eCFR &mdash; 42 CFR 409.60, Benefit periods</a></li>
    <li><a href="https://www.medicare.gov/coverage/skilled-nursing-facility-snf-care" target="_blank" rel="noopener">Medicare.gov &mdash; Skilled nursing facility care</a></li>
    <li><a href="https://medicare.gov/coverage/inpatient-hospital-care/inpatient-outpatient-status" target="_blank" rel="noopener">Medicare.gov &mdash; Inpatient or outpatient hospital status affects your costs</a></li>
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/medicare-outpatient-observation-notice-moon" target="_blank" rel="noopener">CMS &mdash; Medicare Outpatient Observation Notice (MOON) fact sheet</a></li>
    <li><a href="https://medicare.gov/basics/forms-publications-mailings/mailings/costs-and-coverage/medicare-summary-notice" target="_blank" rel="noopener">Medicare.gov &mdash; Medicare Summary Notice</a></li>
    <li><a href="https://www.medicare.gov/prescription-payment-plan" target="_blank" rel="noopener">Medicare.gov &mdash; Medicare Prescription Payment Plan</a></li>
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/contract-year-2026-policy-and-technical-changes-medicare-advantage-program-medicare-prescription-final" target="_blank" rel="noopener">CMS &mdash; Contract Year 2026 Medicare Advantage and Part D final rule fact sheet (payment plan automatic renewal)</a></li>
    <li><a href="https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan" target="_blank" rel="noopener">Medicare.gov &mdash; Joining a plan (enrollment periods)</a></li>
</ul>
""",
})
