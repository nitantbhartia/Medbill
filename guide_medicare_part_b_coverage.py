"""Guide: Medicare Part B Coverage Explained"""

from guides import register, _embed

register("medicare-part-b-coverage-explained", {
    "title": "Medicare Part B Coverage Explained: What's Covered, What's Not, and the 20% Problem",
    "meta_description": "Medicare Part B covers doctor visits, outpatient care, and preventive services, but leaves you with 20% coinsurance forever. Learn costs, exclusions, and IRMAA surcharges for 2026.",
    "published": "2026-04-10",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is the Medicare Part B premium in 2026?",
            "a": "The standard Medicare Part B premium in 2026 is $185 per month. Higher-income beneficiaries pay more under the Income-Related Monthly Adjustment Amount (IRMAA). If your modified adjusted gross income in 2024 exceeded $106,000 (individual) or $212,000 (married filing jointly), you pay a surcharge on top of the standard premium.",
        },
        {
            "q": "Does Medicare Part B cover dental, vision, and hearing?",
            "a": "No. Original Medicare Part B does not cover routine dental care, eyeglasses, contact lenses, hearing aids, or routine hearing exams. These are among the most significant gaps in Medicare coverage. Medicare Advantage plans may offer limited dental, vision, and hearing benefits, but Original Medicare does not.",
        },
        {
            "q": "What is the Medicare Part B deductible in 2026?",
            "a": "The Medicare Part B annual deductible in 2026 is $257. Once you meet this deductible in a calendar year, Medicare pays 80% of the approved amount for covered services and you pay the remaining 20% coinsurance with no cap.",
        },
        {
            "q": "How do I avoid the Medicare Part B IRMAA surcharge?",
            "a": "IRMAA is based on your income from two years prior. If your income has dropped significantly since then (due to retirement, divorce, or other life-changing events), you can file form SSA-44 with the Social Security Administration to request a lower premium based on your current income. Act quickly&mdash;IRMAA surcharges apply from the date of enrollment.",
        },
        {
            "q": "Does Medicare Part B have an out-of-pocket maximum?",
            "a": "No. Original Medicare Part B has no out-of-pocket maximum. The 20% coinsurance applies indefinitely with no cap. A $200,000 outpatient cancer treatment could leave you owing $40,000 in coinsurance. This is why Medigap (Medicare Supplement) insurance exists&mdash;it fills the 20% gap.",
        },
    ],
    "body": f"""<article>
<div class="answer-box"><strong>Quick Answer:</strong> Medicare Part B covers most outpatient medical services including doctor visits, preventive care, and durable medical equipment. After a $257 annual deductible, you pay 20% of every covered service with no cap&mdash;forever, unless you have Medigap. It does not cover dental, vision, hearing, or long-term care.</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-part-b">What Is Medicare Part B?</a></li>
        <li><a href="#what-is-covered">What Part B Covers</a></li>
        <li><a href="#what-is-not-covered">What Part B Does Not Cover</a></li>
        <li><a href="#cost-sharing">2026 Costs: Premium, Deductible, and Coinsurance</a></li>
        <li><a href="#the-20-percent-problem">The 20% Coinsurance Problem</a></li>
        <li><a href="#dme">Durable Medical Equipment</a></li>
        <li><a href="#irmaa">How to Avoid IRMAA Premium Surcharges</a></li>
        <li><a href="#medigap">Closing the Gap with Medigap</a></li>
    </ol>
</nav>

<h2 id="what-is-part-b">What Is Medicare Part B?</h2>

<p>Medicare Part B is the outpatient component of Original Medicare. While Part A covers hospital stays and inpatient services, Part B covers the medical side: physician services, outpatient procedures, diagnostic tests, preventive care, mental health services, and durable medical equipment (DME).</p>

<p>Unlike Part A, Part B is not free. You pay a monthly premium that is deducted automatically from your Social Security benefit. Enrollment in Part B is optional, but most beneficiaries who skip it and enroll later pay a permanent late enrollment penalty of 10% per year they went without coverage.</p>

<h2 id="what-is-covered">What Part B Covers</h2>

<p>Part B is broader than most beneficiaries realize. It covers:</p>

<ul>
    <li><strong>Physician services:</strong> Office visits, specialist consultations, and services from any Medicare-participating doctor regardless of specialty</li>
    <li><strong>Outpatient hospital services:</strong> Outpatient surgery, emergency department visits (when not admitted), observation services</li>
    <li><strong>Preventive services:</strong> Annual Wellness Visit, cancer screenings, cardiovascular screenings, diabetes screening, flu shots, and other preventive services at no cost to you</li>
    <li><strong>Mental health care:</strong> Outpatient therapy, psychiatric evaluation, and partial hospitalization programs</li>
    <li><strong>Ambulance services:</strong> When medically necessary transportation to a hospital</li>
    <li><strong>Durable medical equipment (DME):</strong> Wheelchairs, walkers, CPAP machines, home oxygen, blood glucose monitors when prescribed by a doctor</li>
    <li><strong>Diagnostic tests:</strong> Lab work ordered by your doctor, X-rays, MRIs, CT scans, PET scans</li>
    <li><strong>Physical, occupational, and speech therapy:</strong> When medically necessary and prescribed by a physician</li>
    <li><strong>Second surgical opinions</strong></li>
    <li><strong>Diabetes supplies</strong> (when prescribed) and diabetes self-management training</li>
    <li><strong>Telehealth services</strong> (expanded permanently post-pandemic)</li>
</ul>

<h2 id="what-is-not-covered">What Part B Does Not Cover</h2>

<p>The exclusions in Part B represent major financial exposures for beneficiaries. Part B does <em>not</em> cover:</p>

<ul>
    <li><strong>Routine dental care:</strong> Cleanings, fillings, extractions, dentures, or dental X-rays. Medicare only covers dental services that are medically necessary as part of a covered procedure (e.g., jaw reconstruction after cancer surgery).</li>
    <li><strong>Routine vision care:</strong> Eye exams for glasses or contacts, eyeglasses, or contact lenses (except after cataract surgery)</li>
    <li><strong>Hearing aids and routine hearing exams</strong></li>
    <li><strong>Long-term custodial care:</strong> Help with bathing, dressing, and daily activities in a nursing home or at home. This is a critical gap&mdash;the average nursing home costs over $90,000/year and Medicare covers none of it once skilled care is no longer needed.</li>
    <li><strong>Most prescription drugs:</strong> Outpatient medications are covered by Part D, not Part B. Part B only covers drugs administered in a clinical setting (e.g., chemotherapy infusions, injections in the doctor's office).</li>
    <li><strong>Care outside the United States</strong> (with limited exceptions)</li>
    <li><strong>Cosmetic surgery</strong></li>
    <li><strong>Acupuncture</strong> (except for chronic low back pain, which Part B does cover)</li>
    <li><strong>Most foot care</strong> (routine nail trimming, callus removal)</li>
</ul>

<h2 id="cost-sharing">2026 Costs: Premium, Deductible, and Coinsurance</h2>

<table>
    <thead>
        <tr><th>Cost Component</th><th>2026 Amount</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Standard Monthly Premium</td><td>$185.00</td><td>Higher with IRMAA surcharge</td></tr>
        <tr><td>Annual Deductible</td><td>$257.00</td><td>Per calendar year (January–December)</td></tr>
        <tr><td>Coinsurance After Deductible</td><td>20%</td><td>No cap under Original Medicare</td></tr>
        <tr><td>Preventive Services</td><td>$0</td><td>No deductible or coinsurance applies</td></tr>
        <tr><td>Annual Wellness Visit</td><td>$0</td><td>Must be billed as preventive, not a regular visit</td></tr>
        <tr><td>Mental Health Services</td><td>20%</td><td>Same as other Part B services</td></tr>
        <tr><td>DME</td><td>20%</td><td>Must use Medicare-enrolled supplier</td></tr>
    </tbody>
</table>

<h2 id="the-20-percent-problem">The 20% Coinsurance Problem</h2>

<p>The most consequential feature of Medicare Part B is this: the 20% coinsurance never goes away. There is no out-of-pocket maximum under Original Medicare Part B. Every dollar Medicare approves generates a 20-cent obligation for you, indefinitely.</p>

<p>For most routine care, this is manageable. A $150 office visit leaves you owing $30. But for serious illness, the math gets frightening fast:</p>

<ul>
    <li>A $50,000 outpatient chemotherapy regimen: you owe $10,000</li>
    <li>A $30,000 outpatient surgery: you owe $6,000</li>
    <li>A $100,000 course of outpatient dialysis: you owe $20,000</li>
</ul>

<p>This is not a hypothetical. Beneficiaries facing cancer, kidney disease, or other serious conditions frequently accumulate five-figure Part B obligations in a single year with no ceiling.</p>

<div class="key-takeaway">
    <strong>The fix for the 20% gap is Medigap.</strong> A Medigap Plan G covers the 20% Part B coinsurance after you pay the $257 annual deductible. Monthly premiums range from $100 to $300 depending on your age and location. For anyone with ongoing medical care, Medigap typically saves money within months.
</div>

<h2 id="dme">Durable Medical Equipment</h2>

<p>Part B covers DME when your doctor prescribes it as medically necessary and you use a Medicare-enrolled DME supplier. The 20% coinsurance applies after the deductible. Important rules:</p>

<ul>
    <li>The supplier must be enrolled in Medicare and accept assignment, or you pay more than 20%</li>
    <li>Some DME is rented (e.g., oxygen equipment, CPAP machines for the first 13 months); others are purchased</li>
    <li>Prior authorization is required for certain high-cost DME items</li>
    <li>If your supplier is not Medicare-enrolled, Medicare pays nothing</li>
</ul>

<p>Always verify that your DME supplier participates in Medicare before accepting equipment. Non-participating suppliers commonly result in surprise bills.</p>

{_embed("cost", title="Estimate Your Medicare Part B Costs", subtitle="See what you'd owe for common outpatient services.")}

<h2 id="irmaa">How to Avoid IRMAA Premium Surcharges</h2>

<p>The Income-Related Monthly Adjustment Amount (IRMAA) increases your Part B premium if your income exceeds certain thresholds. Medicare uses your tax return from <strong>two years prior</strong> to set the premium.</p>

<table>
    <thead>
        <tr><th>2024 MAGI (Individual)</th><th>2024 MAGI (Married Filing Jointly)</th><th>2026 Monthly Premium</th></tr>
    </thead>
    <tbody>
        <tr><td>&le;$106,000</td><td>&le;$212,000</td><td>$185.00</td></tr>
        <tr><td>$106,001&ndash;$133,000</td><td>$212,001&ndash;$266,000</td><td>$259.00</td></tr>
        <tr><td>$133,001&ndash;$167,000</td><td>$266,001&ndash;$334,000</td><td>$370.00</td></tr>
        <tr><td>$167,001&ndash;$200,000</td><td>$334,001&ndash;$400,000</td><td>$480.90</td></tr>
        <tr><td>&gt;$500,000</td><td>&gt;$750,000</td><td>$591.90</td></tr>
    </tbody>
</table>

<p>If your income has dropped significantly&mdash;due to retirement, loss of a spouse, or other life event&mdash;you can appeal IRMAA using <strong>Form SSA-44</strong>. File it with your local Social Security office as soon as your income situation changes. The appeal can reduce your premium retroactively.</p>

<h2 id="medigap">Closing the Gap with Medigap</h2>

<p>The best time to enroll in a Medigap (Medicare Supplement) plan is during your six-month open enrollment window that starts the month you turn 65 and enroll in Part B. During this window, insurers cannot deny you coverage or charge you more due to pre-existing conditions.</p>

<p>Outside this window, you may face medical underwriting&mdash;meaning you can be denied or charged more based on your health history. The most popular Medigap plan is <strong>Plan G</strong>, which covers the Part B coinsurance, the Part A deductible, and skilled nursing coinsurance, leaving you responsible only for the $257 annual deductible.</p>

<ul class="sources-list">
    <li><a href="https://www.medicare.gov/your-medicare-costs/part-b-costs" target="_blank" rel="noopener">Medicare.gov &mdash; Part B Costs</a></li>
    <li><a href="https://www.cms.gov/medicare/enrollment-renewal/part-b" target="_blank" rel="noopener">CMS &mdash; Medicare Part B Enrollment</a></li>
    <li><a href="https://www.ssa.gov/forms/ssa-44.pdf" target="_blank" rel="noopener">SSA Form SSA-44 &mdash; IRMAA Life-Changing Event Request</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/an-overview-of-medicare/" target="_blank" rel="noopener">KFF &mdash; Overview of Medicare Coverage</a></li>
</ul>
</article>""",
})
