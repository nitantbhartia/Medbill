"""Guide: Site-Neutral Payment 2026 - Stop Overpaying Facility Fees."""

from guides import register, _embed

_calc_embed = _embed(mode="cost", title="Look up Medicare rates for any procedure", subtitle="Compare what Medicare pays vs. what your hospital charges to find overpriced facility fees.", height="400")

register("site-neutral-payment-2026", {
    "title": "Site-Neutral Payment 2026: How New Rules Can Save You Hundreds on Hospital Facility Fees",
    "meta_description": "CMS expanded site-neutral payment in 2026, saving patients $70M in copays. Learn what facility fees are, how to avoid them, and how new rules protect you.",
    "published": "2026-03-02",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "What is site-neutral payment?",
            "a": "Site-neutral payment means paying the same rate for the same service regardless of where it is performed. Under current rules, a hospital outpatient department can charge a facility fee on top of the professional fee for the same service that an independent physician office performs for one flat rate. Site-neutral policies eliminate this pricing gap by paying hospital outpatient departments at the same rate as physician offices.",
        },
        {
            "q": "What changed about site-neutral payment in 2026?",
            "a": "CMS expanded site-neutral payment to cover drug administration services at off-campus hospital outpatient departments. These services, including chemotherapy infusions and injectable medications, are now paid at the Medicare Physician Fee Schedule rate instead of the higher hospital outpatient rate. CMS estimates this saves $290 million in 2026, including $70 million in reduced patient copayments.",
        },
        {
            "q": "What is a hospital facility fee?",
            "a": "A facility fee is an additional charge that hospital-owned outpatient departments add on top of the professional fee for a service. When a physician office is acquired by a hospital system, the same doctor in the same office performing the same service can suddenly cost 2-3x more because the hospital adds a facility fee. The Health Care Cost Institute found facility fees add roughly $100 to a primary care visit and $100 to a pediatric wellness visit.",
        },
        {
            "q": "How can I avoid paying facility fees?",
            "a": "Ask before scheduling whether the location is a hospital outpatient department or an independent office. Choose freestanding physician offices, ambulatory surgery centers, or independent imaging centers when possible. Check your insurer's cost estimator tool to compare prices at different locations. If you receive a bill with a facility fee, ask the billing department to explain the charge and whether a non-hospital alternative was available.",
        },
        {
            "q": "Do state laws protect me from facility fees?",
            "a": "As of 2026, 21 states have some level of protection against unjustified facility fees, up from 15 in 2024. Protections vary: some states require disclosure of facility fees before services are provided, others cap facility fees, and some ban facility fees at off-campus locations entirely. Check your state's specific protections.",
        },
        {
            "q": "Are rural hospitals affected by site-neutral payment?",
            "a": "Rural sole community hospitals are exempt from the 2026 site-neutral expansion. However, other rural hospital designations like Rural Emergency Hospitals and Medicare Dependent Hospitals are not exempt. The AHA estimates site-neutral policies could cut rural hospital Medicare payments by $26.3 billion over 10 years.",
        },
    ],
    "body": f"""
<p class="lead">When a doctor&rsquo;s office gets bought by a hospital, the price of an office visit can double overnight &mdash; even though the same doctor provides the same care in the same room. The culprit: <strong>hospital facility fees</strong>. In 2026, CMS expanded site-neutral payment rules that will save patients an estimated <strong>$70 million in copayments</strong> this year alone. Here&rsquo;s how facility fees work, how the new rules help, and how to avoid overpaying.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-facility-fees">What are hospital facility fees?</a></li>
        <li><a href="#how-much-more">How much more do facility fees cost you?</a></li>
        <li><a href="#2026-changes">What changed in 2026</a></li>
        <li><a href="#who-saves">Who saves money under the new rules</a></li>
        <li><a href="#avoid-fees">How to avoid facility fees</a></li>
        <li><a href="#state-protections">State-level protections</a></li>
        <li><a href="#check-your-bill">How to check your bill for facility fees</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-facility-fees">1. What are hospital facility fees?</h2>

<p>A facility fee is an extra charge hospitals add when they provide outpatient services. It is billed separately from the professional fee (what the doctor charges) and covers the hospital&rsquo;s overhead &mdash; building costs, equipment, nursing staff, and administrative expenses.</p>

<p>The problem: when hospitals acquire independent physician practices, those offices become "hospital outpatient departments" (HOPDs). The doctor, the office, and the service don&rsquo;t change. But the billing does. The hospital adds a facility fee on top of the professional fee, and the total cost to the patient jumps significantly.</p>

<p>A 2026 PIRG analysis found that hospital outpatient departments charge <strong>an average of 2.5x more</strong> than independent offices for the same services. For some procedures, the markup is even higher:</p>

<table>
    <thead>
        <tr><th>Service</th><th>Independent office cost</th><th>Hospital outpatient dept. cost</th><th>Difference</th></tr>
    </thead>
    <tbody>
        <tr><td>Primary care visit (new patient)</td><td>$115</td><td>$215</td><td>+$100 (87%)</td></tr>
        <tr><td>Pediatric wellness visit</td><td>$150</td><td>$250</td><td>+$100 (67%)</td></tr>
        <tr><td>Echocardiogram</td><td>$225</td><td>$550</td><td>+$325 (144%)</td></tr>
        <tr><td>Colonoscopy (diagnostic)</td><td>$620</td><td>$1,840</td><td>+$1,220 (197%)</td></tr>
        <tr><td>MRI (lumbar spine)</td><td>$510</td><td>$1,280</td><td>+$770 (151%)</td></tr>
        <tr><td>Drug infusion (first hour)</td><td>$180</td><td>$450</td><td>+$270 (150%)</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Why this matters for your wallet:</strong> If you haven&rsquo;t met your deductible, you pay the full facility fee out of pocket. Even after meeting your deductible, your coinsurance is calculated on the higher HOPD price &mdash; meaning your 20% copay is 20% of a much larger number.
</div>

<h2 id="how-much-more">2. How much more do facility fees cost you?</h2>

<p>The financial impact depends on your insurance plan and whether you&rsquo;ve met your deductible. Here is a concrete example:</p>

<div class="bill-example">
    <div class="bill-header">Same service, two locations: Echocardiogram (CPT 93306)</div>
    <div class="line-item">
        <span>Independent cardiology office &mdash; total charge</span>
        <span>$225</span>
    </div>
    <div class="line-item flagged">
        <span>Hospital outpatient department &mdash; professional fee</span>
        <span>$225</span>
    </div>
    <div class="line-item flagged">
        <span>Hospital outpatient department &mdash; facility fee</span>
        <span>$325</span>
    </div>
    <div class="line-total">
        <span>Hospital outpatient department &mdash; total charge</span>
        <span>$550</span>
    </div>
</div>

<table>
    <thead>
        <tr><th>Scenario</th><th>Independent office &mdash; you pay</th><th>Hospital OPD &mdash; you pay</th><th>Extra cost</th></tr>
    </thead>
    <tbody>
        <tr><td>Haven&rsquo;t met deductible</td><td>$225</td><td>$550</td><td><strong>+$325</strong></td></tr>
        <tr><td>Met deductible, 20% coinsurance</td><td>$45</td><td>$110</td><td><strong>+$65</strong></td></tr>
        <tr><td>Met deductible, $40 copay</td><td>$40</td><td>$40 + facility fee*</td><td><strong>varies</strong></td></tr>
    </tbody>
</table>

<p><em>*Some plans charge a separate copay for the facility fee, effectively doubling the copay.</em></p>

<p>Over a year, a patient with a chronic condition requiring monthly specialist visits and quarterly lab work at a hospital-owned practice could pay <strong>$1,500&ndash;$3,000 more</strong> in out-of-pocket costs than the same care at an independent office.</p>

<h2 id="2026-changes">3. What changed in 2026</h2>

<p>CMS finalized two major site-neutral payment expansions in the 2026 OPPS final rule:</p>

<p><strong>Drug administration services.</strong> Starting January 1, 2026, drug administration services (including chemotherapy infusions, biologic injections, and IV medications) at off-campus hospital outpatient departments are paid at the Medicare Physician Fee Schedule rate &mdash; approximately 40% of the previous OPPS rate. CMS estimates this saves <strong>$290 million in 2026</strong>: $220 million in Medicare savings and <strong>$70 million in reduced patient copays</strong>.</p>

<p><strong>Continued clinic visit site-neutrality.</strong> The 2019 site-neutral policy for clinic visits (evaluation and management codes) at off-campus HOPDs remains in effect. Hospitals fought this policy through the courts but lost, and it has been fully implemented since 2020.</p>

<p><strong>NPI billing transparency (2028).</strong> Starting in 2028, all off-campus HOPDs must bill under their own National Provider Identifier (NPI), making it easier to track facility fee billing patterns. This will expose which hospital systems charge the most in facility fees and support future site-neutral expansions.</p>

<div class="key-takeaway">
    <strong>What this means for you:</strong> If you receive chemotherapy, biologic infusions, or injectable medications at a hospital-owned clinic, your Medicare copay may decrease in 2026. Ask your provider if the site-neutral rate applies to your treatment. For privately insured patients, the impact depends on whether your insurer adopts Medicare&rsquo;s site-neutral approach in its own contracts.
</div>

<h2 id="who-saves">4. Who saves money under the new rules</h2>

<p><strong>Medicare patients receiving drug infusions.</strong> Patients getting chemotherapy, biologic medications (like infliximab for Crohn&rsquo;s disease or rituximab for rheumatoid arthritis), or other infused drugs at off-campus hospital clinics will see lower copays under the new rate. The average savings per infusion session ranges from $30&ndash;$150 depending on the drug and facility.</p>

<p><strong>Patients who comparison-shop.</strong> The growing availability of pricing data means patients who compare costs across facilities before scheduling care can save hundreds or thousands of dollars. Check the <a href="/hospitals/">BillKarma hospital directory</a> to compare procedure prices and identify which facilities charge the highest facility fees in your area.</p>

<p><strong>Self-pay and uninsured patients.</strong> If you are paying out of pocket, choosing a freestanding office or ambulatory surgery center over a hospital outpatient department is one of the single most effective ways to cut costs. The same procedure often costs 40&ndash;60% less at a freestanding facility.</p>

<h2 id="avoid-fees">5. How to avoid facility fees</h2>

<ol>
    <li><strong>Ask before you schedule: "Is this a hospital outpatient department?"</strong> If yes, ask whether the same service is available at a freestanding location within the same health system or nearby.</li>
    <li><strong>Choose ambulatory surgery centers (ASCs) over hospitals for outpatient procedures.</strong> ASCs typically charge 40&ndash;60% less than hospital outpatient departments for the same procedure.</li>
    <li><strong>Use independent imaging centers for MRIs, CT scans, and X-rays.</strong> Hospital-owned imaging is often 2&ndash;3x the price of independent centers for identical scans on identical equipment.</li>
    <li><strong>Check your insurer&rsquo;s cost estimator tool.</strong> Under the Transparency in Coverage Rule, your insurer must offer a price comparison tool that shows personalized cost estimates at different facilities.</li>
    <li><strong>Review your EOB for separate facility charges.</strong> If you see two charges for one visit (a professional fee and a facility fee), you may be paying a facility fee. <a href="/scan">Upload your bill to BillKarma</a> to identify facility fees and compare them to non-hospital rates.</li>
    <li><strong>Ask your doctor if they have a non-hospital office.</strong> Many physicians who were acquired by hospital systems still maintain some independent clinic locations.</li>
</ol>

{_calc_embed}

<div class="case-study">
    <h3>Case study: Patient saves $1,840 by switching from hospital to ASC for colonoscopy</h3>
    <p><strong>Situation:</strong> Robert, 55, was scheduled for a routine colonoscopy at a hospital-owned endoscopy center. He hadn&rsquo;t met his $3,000 deductible, so he would pay the full negotiated rate out of pocket.</p>
    <p><strong>What he found:</strong> The hospital&rsquo;s price transparency file showed a negotiated rate of $2,460 for CPT 45378 (diagnostic colonoscopy), including a $1,620 facility fee. He checked the <a href="/hospitals/">BillKarma hospital directory</a> and found an ambulatory surgery center 10 minutes away offering the same procedure at $620 &mdash; performed by the same gastroenterologist.</p>
    <p><strong>Result:</strong> By switching locations, Robert paid $620 instead of $2,460. <strong>Savings: $1,840</strong> &mdash; for the exact same procedure, same doctor, same outcome.</p>
</div>

<h2 id="state-protections">6. State-level protections</h2>

<p>As of 2026, <strong>21 states</strong> have some form of facility fee protection, up from 15 states in 2024. State laws vary significantly:</p>

<table>
    <thead>
        <tr><th>Protection type</th><th>States</th><th>What it does</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Facility fee disclosure required</strong></td><td>CT, CO, IN, ME, NY, OH, OR, TX, WA</td><td>Hospitals must inform patients about facility fees before services are provided</td></tr>
        <tr><td><strong>Facility fee banned at off-campus sites</strong></td><td>CT, CO, IN, OR</td><td>Off-campus hospital clinics cannot charge facility fees (strongest protection)</td></tr>
        <tr><td><strong>Facility fee caps</strong></td><td>ME, NY</td><td>Limits the amount hospitals can charge as a facility fee</td></tr>
        <tr><td><strong>Site-neutral payment in state employee plans</strong></td><td>CT, MT, NC, OR</td><td>State employee health plans pay the same rate regardless of care site</td></tr>
    </tbody>
</table>

<p>Check your state&rsquo;s specific protections. If your state requires facility fee disclosure and a hospital did not inform you before your visit, you may have grounds to dispute the fee.</p>

<h2 id="check-your-bill">7. How to check your bill for facility fees</h2>

<p>Facility fees often appear as separate line items on your EOB or hospital bill. Look for:</p>

<ul>
    <li><strong>Two charges for one visit:</strong> A professional/physician fee AND a facility/hospital fee for the same date of service</li>
    <li><strong>Revenue code 0510 or 0520:</strong> These codes indicate clinic or outpatient department charges (facility fees)</li>
    <li><strong>Charges labeled "hospital outpatient" or "facility":</strong> These are the facility fee component</li>
    <li><strong>Bills from two entities for one visit:</strong> A bill from the doctor AND a separate bill from the hospital for the same appointment</li>
</ul>

<p>If you identify a facility fee, <a href="/scan">upload your bill to BillKarma</a> to see how it compares to non-hospital rates for the same service. If the total is significantly higher than the Medicare rate or the going rate at independent offices, use that data to negotiate.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is site-neutral payment?</h3>
        <p>Site-neutral payment means paying the same amount for the same service regardless of where it is performed. Currently, hospital outpatient departments charge more than independent offices for identical services by adding a facility fee. Site-neutral policies eliminate this pricing gap. CMS has been expanding site-neutral policies since 2019, with the latest expansion covering drug administration services starting in 2026.</p>
    </div>
    <div class="faq-item">
        <h3>What is a hospital facility fee?</h3>
        <p>A facility fee is an additional charge that hospital-owned outpatient departments add on top of the doctor&rsquo;s professional fee. It covers hospital overhead costs. When a physician practice is acquired by a hospital, the same service at the same location can cost 2&ndash;3x more due to the added facility fee. The HCCI found that facility fees add roughly $100 to a primary care visit.</p>
    </div>
    <div class="faq-item">
        <h3>How can I avoid paying facility fees?</h3>
        <p>Ask before scheduling whether the location is a hospital outpatient department. Choose freestanding physician offices, ambulatory surgery centers, or independent imaging centers when possible. Use your insurer&rsquo;s cost estimator tool to compare prices. Check the <a href="/hospitals/">BillKarma hospital directory</a> to compare facility prices before you schedule.</p>
    </div>
    <div class="faq-item">
        <h3>Will the 2026 site-neutral changes lower my bill?</h3>
        <p>If you are a Medicare patient receiving drug infusions at an off-campus hospital clinic, your copay may decrease. CMS estimates $70 million in total patient copay savings. For privately insured patients, the impact depends on your insurer&rsquo;s contracts. However, choosing freestanding facilities over hospital outpatient departments remains the most reliable way to avoid facility fees regardless of insurance type.</p>
    </div>
    <div class="faq-item">
        <h3>Do state laws protect me from facility fees?</h3>
        <p>As of 2026, 21 states have some facility fee protections. The strongest protections (in CT, CO, IN, OR) ban facility fees at off-campus hospital locations. Other states require disclosure before services. Check your state&rsquo;s laws and ask hospitals about facility fees before scheduling care.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/cy-2026-medicare-hospital-outpatient-prospective-payment-system-and-ambulatory-surgical-center" target="_blank" rel="noopener">CMS: CY 2026 OPPS/ASC Final Rule Fact Sheet</a></li>
    <li><a href="https://pirg.org/resources/outpatient-outrage-2026-hospital-prices-for-care-outside-hospitals/" target="_blank" rel="noopener">PIRG: Outpatient Outrage 2026 &mdash; Hospital Prices for Care Outside Hospitals</a></li>
    <li><a href="https://www.claconnect.com/en/resources/blogs/health-care/payment-changes-in-2026-for-hospitals-ascs" target="_blank" rel="noopener">CLA: Payment Changes in 2026 for Hospitals and ASCs</a></li>
    <li><a href="https://nashp.org/new-site-neutral-payment-model-legislation-for-states/" target="_blank" rel="noopener">NASHP: New Site-Neutral Payment Model Legislation for States</a></li>
    <li><a href="https://www.aha.org/advocacy/site-neutral-payment" target="_blank" rel="noopener">AHA: Site-Neutral Payment Advocacy Position</a></li>
    <li><a href="https://www.healthcostinstitute.org/" target="_blank" rel="noopener">Health Care Cost Institute: Facility Fee Impact Analysis</a></li>
    <li><a href="https://www.milliman.com/en/insight/site-neutral-payment-5-considerations-hospitals" target="_blank" rel="noopener">Milliman: Site-Neutral Payment &mdash; 5 Considerations for Hospitals and Health Systems</a></li>
</ul>
""",
})
