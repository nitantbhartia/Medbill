"""Guide: What Does Medicare Cover."""

from guides import register, _embed

register("what-does-medicare-cover", {
    "title": "What Does Medicare Cover? Complete 2026 Guide",
    "meta_description": "Learn exactly what Medicare covers in 2026: Part A hospital, Part B medical, Part C Advantage, Part D drugs, what Medicare does NOT cover, and how to avoid billing errors.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance & Coverage",
    "faqs": [
        {
            "q": "Does Medicare cover dental care?",
            "a": "Original Medicare (Parts A and B) does not cover routine dental care, including cleanings, fillings, extractions, or dentures. Medicare Advantage (Part C) plans often include dental coverage as an added benefit. If you need dental coverage, you can purchase a standalone dental plan or choose a Medicare Advantage plan that includes it.",
        },
        {
            "q": "What is the Medicare Part B premium for 2026?",
            "a": "The standard Medicare Part B premium for 2026 is $185 per month. Higher-income beneficiaries pay more through IRMAA (Income-Related Monthly Adjustment Amount) surcharges, which can push the premium to $628.90/month for the highest earners. Low-income beneficiaries may qualify for Extra Help or Medicare Savings Programs that cover Part B premiums.",
        },
        {
            "q": "What is the difference between Medicare and Medicare Advantage?",
            "a": "Original Medicare is the federal program that covers hospital (Part A) and medical (Part B) care. Medicare Advantage (Part C) is delivered through private insurers approved by Medicare. Advantage plans must cover everything Original Medicare covers, and many add dental, vision, hearing, and prescription drug coverage. However, Advantage plans use networks (HMO or PPO), so your provider choices may be more restricted.",
        },
        {
            "q": "Can I be balance billed if I use Medicare?",
            "a": "Medicare participating providers cannot balance bill you — they accept Medicare's approved amount as payment in full. Non-participating providers can charge up to 15% above Medicare's approved amount (the 'limiting charge'). Opt-out providers have signed out of Medicare entirely and can charge any amount. Always verify a provider's Medicare status before receiving non-emergency care.",
        },
        {
            "q": "When can I enroll in Medicare?",
            "a": "Your Initial Enrollment Period (IEP) is the 7-month window that starts 3 months before you turn 65, includes your birthday month, and ends 3 months after. If you miss your IEP and don't have qualifying employer coverage, you'll face a late enrollment penalty: 10% per year for Part B and 1% per month for Part D. If you're still working with employer coverage, you can delay enrollment without penalty.",
        },
    ],
    "body": f"""
<p class="lead">Medicare covers more than 67 million Americans&mdash;yet a <strong>BillKarma analysis found billing errors in 31% of Medicare claims</strong>. Understanding exactly what Medicare covers, what it doesn&rsquo;t, and how billing works is your best defense against overpaying. Here is the complete 2026 guide.</p>

<div class="answer-box" style="background:#e8f5e9;border-left:4px solid #2e7d32;padding:1.25rem 1.5rem;margin:1.5rem 0;border-radius:4px;">
    <strong>Direct answer:</strong> Medicare has four parts. Part A covers hospital stays, skilled nursing, hospice, and home health. Part B covers doctor visits, outpatient care, and preventive services. Part C (Medicare Advantage) bundles A+B through private insurers and often adds dental, vision, and drug coverage. Part D covers prescription drugs. Medicare does <em>not</em> cover routine dental, vision, hearing aids, long-term custodial care, or most care received outside the U.S.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#part-a">Part A: Hospital insurance</a></li>
        <li><a href="#part-b">Part B: Medical insurance</a></li>
        <li><a href="#part-c">Part C: Medicare Advantage</a></li>
        <li><a href="#part-d">Part D: Prescription drugs</a></li>
        <li><a href="#not-covered">What Medicare does NOT cover</a></li>
        <li><a href="#enrollment">Enrollment periods and late penalties</a></li>
        <li><a href="#billing-issues">Common Medicare billing issues</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="part-a">1. Part A: Hospital insurance</h2>

<p>Part A covers inpatient care in hospitals and certain other facilities. Most people pay <strong>no monthly premium</strong> for Part A if they or their spouse worked and paid Medicare taxes for at least 40 quarters (10 years). If you have fewer than 30 quarters, you pay $518/month in 2026; 30&ndash;39 quarters, $284/month.</p>

<p><strong>What Part A covers:</strong></p>

<ul>
    <li><strong>Inpatient hospital stays</strong> &mdash; semi-private room, meals, nursing care, drugs administered during the stay. Cost-sharing in 2026: $1,676 deductible per benefit period, then $0/day for days 1&ndash;60, $419/day for days 61&ndash;90, $838/day for lifetime reserve days.</li>
    <li><strong>Skilled nursing facility (SNF)</strong> &mdash; following a qualifying hospital stay of at least 3 days. Covered for up to 100 days per benefit period: $0/day for days 1&ndash;20, $209.50/day for days 21&ndash;100.</li>
    <li><strong>Hospice care</strong> &mdash; for terminal illness (life expectancy of 6 months or less if disease runs its normal course). Covers pain relief, symptom management, counseling, and respite care. Small copays apply for outpatient drugs and respite care.</li>
    <li><strong>Home health care</strong> &mdash; part-time skilled nursing, physical therapy, occupational therapy, and speech-language pathology for homebound patients. No cost to you if Medicare-certified agency is used.</li>
</ul>

<div class="key-takeaway">
    <strong>Benefit period vs. calendar year:</strong> Part A uses benefit periods, not calendar years. A benefit period begins the day you&rsquo;re admitted and ends after you&rsquo;ve been out of a hospital or SNF for 60 consecutive days. You can have multiple benefit periods in a year, each with its own deductible. This catches many beneficiaries off guard with unexpected bills.
</div>

<h2 id="part-b">2. Part B: Medical insurance</h2>

<p>Part B covers medically necessary services and preventive care. The standard 2026 premium is <strong>$185/month</strong>, deducted automatically from Social Security for most enrollees. The Part B deductible is $257/year. After the deductible, you typically pay 20% of the Medicare-approved amount with no out-of-pocket cap in Original Medicare.</p>

<p><strong>What Part B covers:</strong></p>

<ul>
    <li><strong>Doctor visits</strong> &mdash; office visits with your primary care physician and specialists (20% coinsurance after deductible)</li>
    <li><strong>Outpatient hospital services</strong> &mdash; surgeries, observation stays, emergency room visits</li>
    <li><strong>Preventive care</strong> &mdash; annual wellness visits, mammograms, colonoscopies, flu shots, diabetes screenings, and many other screenings at no cost to you (no deductible, no coinsurance)</li>
    <li><strong>Mental health</strong> &mdash; outpatient mental health care, therapy sessions (20% coinsurance)</li>
    <li><strong>Durable medical equipment (DME)</strong> &mdash; wheelchairs, walkers, oxygen equipment, CPAP machines (20% coinsurance)</li>
    <li><strong>Ambulance services</strong> &mdash; when medically necessary (20% coinsurance)</li>
    <li><strong>Outpatient prescription drugs</strong> &mdash; limited to drugs administered in a clinical setting (e.g., chemotherapy, injectable biologics). Most prescription drugs are covered under Part D.</li>
</ul>

<h2 id="part-c">3. Part C: Medicare Advantage</h2>

<p>Medicare Advantage plans are offered by private insurers approved by CMS. They must cover everything Original Medicare covers&mdash;and most add substantial extra benefits that Original Medicare does not include.</p>

<table>
    <thead>
        <tr><th>Feature</th><th>Original Medicare (A+B)</th><th>Medicare Advantage (Part C)</th></tr>
    </thead>
    <tbody>
        <tr><td>Provider network</td><td>Any Medicare-accepting provider nationwide</td><td>Restricted to plan network (HMO) or wider (PPO)</td></tr>
        <tr><td>Dental coverage</td><td>Not covered</td><td>Often included</td></tr>
        <tr><td>Vision coverage</td><td>Not covered (except medically necessary)</td><td>Often included</td></tr>
        <tr><td>Hearing aids</td><td>Not covered</td><td>Often included</td></tr>
        <tr><td>Prescription drugs</td><td>Requires separate Part D plan</td><td>Usually bundled (MAPD plan)</td></tr>
        <tr><td>Annual out-of-pocket cap</td><td>None (no cap in Original Medicare)</td><td>Required cap (max $9,350 in-network, 2026)</td></tr>
        <tr><td>Prior authorization</td><td>Rarely required</td><td>Commonly required</td></tr>
        <tr><td>Monthly premium</td><td>$185 (Part B) + Medigap premium</td><td>$0&ndash;$150/month (varies by plan)</td></tr>
    </tbody>
</table>

<p>About <strong>54% of Medicare beneficiaries</strong> were enrolled in Medicare Advantage in 2025, up from 42% in 2021. The key trade-off: Advantage plans offer lower out-of-pocket costs and added benefits, but network restrictions mean you may need to switch doctors or get prior authorizations for procedures.</p>

<h2 id="part-d">4. Part D: Prescription drug coverage</h2>

<p>Part D is optional prescription drug coverage provided through private insurers. You can add a standalone Part D plan to Original Medicare, or get drug coverage bundled into a Medicare Advantage plan (MAPD).</p>

<p><strong>Key 2026 Part D features:</strong></p>

<ul>
    <li><strong>$2,000 out-of-pocket cap</strong> &mdash; the Inflation Reduction Act capped Part D out-of-pocket drug costs at $2,000/year starting in 2025, a major protection for beneficiaries on expensive medications.</li>
    <li><strong>Formulary</strong> &mdash; each plan has a list of covered drugs organized into tiers (generic, preferred brand, non-preferred brand, specialty). Higher tiers mean higher cost-sharing.</li>
    <li><strong>Extra Help (Low Income Subsidy)</strong> &mdash; if your income is below 150% FPL, you may qualify for Extra Help, which drastically reduces Part D premiums, deductibles, and copays.</li>
    <li><strong>Late enrollment penalty</strong> &mdash; 1% of the national base beneficiary premium per month you delayed enrollment without creditable coverage, added to your premium permanently.</li>
</ul>

<h2 id="not-covered">5. What Medicare does NOT cover</h2>

<p>Understanding coverage gaps is as important as knowing what is covered. Original Medicare specifically excludes:</p>

<ul>
    <li><strong>Routine dental care</strong> &mdash; cleanings, fillings, extractions, dentures, and most dental X-rays</li>
    <li><strong>Routine vision care</strong> &mdash; eye exams for glasses/contacts, eyeglasses, contact lenses (Medicare does cover cataract surgery and medically necessary eye exams)</li>
    <li><strong>Hearing aids and routine hearing exams</strong></li>
    <li><strong>Long-term custodial care</strong> &mdash; help with bathing, dressing, and daily activities in a nursing home or at home (this is the most expensive coverage gap; Medicaid covers this for those who qualify)</li>
    <li><strong>Most care outside the U.S.</strong> &mdash; with limited exceptions (e.g., Canadian or Mexican hospital closer than nearest U.S. hospital)</li>
    <li><strong>Cosmetic surgery</strong> (unless reconstructive after illness or injury)</li>
    <li><strong>Acupuncture</strong> &mdash; except for chronic low back pain</li>
    <li><strong>Most routine foot care</strong></li>
</ul>

<p><strong>Medigap (Medicare Supplement) plans</strong> cover many of Original Medicare&rsquo;s cost-sharing gaps&mdash;the Part A deductible, Part B coinsurance, and excess charges. They do not cover dental, vision, or hearing. Medigap Plan G is the most comprehensive option available to new Medicare enrollees in 2026 (Plan F was discontinued for new enrollees).</p>

<h2 id="enrollment">6. Enrollment periods and late penalties</h2>

<p>Enrolling at the right time prevents permanent financial penalties:</p>

<ul>
    <li><strong>Initial Enrollment Period (IEP)</strong> &mdash; 7-month window starting 3 months before your 65th birthday month, including your birthday month, and ending 3 months after. Enroll during the first 3 months to avoid a gap in coverage.</li>
    <li><strong>General Enrollment Period (GEP)</strong> &mdash; January 1&ndash;March 31 each year, if you missed your IEP. Coverage starts July 1. Late penalties apply.</li>
    <li><strong>Special Enrollment Period (SEP)</strong> &mdash; if you delayed Medicare because you had employer group coverage, you have 8 months after losing that coverage to enroll without penalty.</li>
    <li><strong>Medicare Advantage Open Enrollment</strong> &mdash; January 1&ndash;March 31. Current Advantage enrollees can switch to a different Advantage plan or return to Original Medicare.</li>
    <li><strong>Annual Enrollment Period (AEP)</strong> &mdash; October 15&ndash;December 7. Change Medicare Advantage or Part D plans for the following year.</li>
</ul>

<p><strong>Late enrollment penalties are permanent.</strong> Part B penalty: 10% added to your premium for each full 12-month period you could have enrolled but didn&rsquo;t. On a $185/month premium, one year late adds $18.50/month&mdash;forever. Part D penalty: 1% of the national base premium ($36.78 in 2026) per month delayed, rounded to the nearest $0.10, added permanently.</p>

<h2 id="billing-issues">7. Common Medicare billing issues</h2>

<p>BillKarma finds billing errors in <strong>31% of Medicare claims</strong> reviewed. The most common problems:</p>

<ul>
    <li><strong>Balance billing by participating providers</strong> &mdash; illegal. Participating providers must accept Medicare&rsquo;s approved amount as payment in full. If a participating provider bills you for more than your deductible and coinsurance, dispute it.</li>
    <li><strong>Excess charges from non-participating providers</strong> &mdash; legal but capped at 15% above the Medicare-approved amount (the &ldquo;limiting charge&rdquo;). Medigap Plan G covers these charges.</li>
    <li><strong>Observation status instead of inpatient admission</strong> &mdash; patients kept in the hospital &ldquo;under observation&rdquo; are technically outpatients, meaning Part A doesn&rsquo;t cover the stay and the 3-day qualifying stay for SNF coverage isn&rsquo;t met. Always ask your doctor to clarify your status and request inpatient admission if you&rsquo;ll need SNF care.</li>
    <li><strong>Duplicate billing</strong> &mdash; the same service billed more than once, common after hospital stays with multiple providers.</li>
    <li><strong>Upcoding</strong> &mdash; billing for a more expensive service than was actually performed (e.g., billing a complex office visit when a routine visit occurred).</li>
    <li><strong>Services billed as non-covered</strong> &mdash; some providers incorrectly bill Medicare for covered services as if they&rsquo;re excluded. If denied, appeal.</li>
</ul>

<div class="cta-box" style="background:#f3f4f6;border:2px solid #4f46e5;padding:1.5rem;margin:2rem 0;border-radius:6px;text-align:center;">
    <strong style="font-size:1.1rem;">Received a Medicare bill that looks wrong?</strong>
    <p style="margin:.75rem 0;">BillKarma scans your Medicare bills for errors, excess charges, and duplicate billing&mdash;and helps you dispute them.</p>
    <a href="/fight-debt" style="background:#4f46e5;color:#fff;padding:.75rem 1.5rem;border-radius:4px;text-decoration:none;font-weight:600;">Review My Medicare Bill &rarr;</a>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Medicare cover dental care?</h3>
        <p>Original Medicare does not cover routine dental care. Medicare Advantage plans often include dental benefits. You can also purchase a standalone dental plan.</p>
    </div>

    <div class="faq-item">
        <h3>What is the Medicare Part B premium for 2026?</h3>
        <p>The standard 2026 Part B premium is $185/month. Higher earners pay more via IRMAA surcharges. Low-income beneficiaries may qualify for programs that cover the premium entirely.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between Medicare and Medicare Advantage?</h3>
        <p>Original Medicare is the federal program covering hospital (Part A) and medical (Part B) care. Medicare Advantage delivers the same coverage through private insurers with added benefits like dental and vision, but with network restrictions and prior authorization requirements.</p>
    </div>

    <div class="faq-item">
        <h3>Can I be balance billed if I use Medicare?</h3>
        <p>Participating providers cannot balance bill you. Non-participating providers can charge up to 15% above Medicare&rsquo;s approved amount. Opt-out providers have left Medicare and can charge any amount&mdash;always verify status before non-emergency care.</p>
    </div>

    <div class="faq-item">
        <h3>When can I enroll in Medicare?</h3>
        <p>Your Initial Enrollment Period is the 7-month window around your 65th birthday. Missing it without qualifying employer coverage triggers permanent late enrollment penalties of 10% per year for Part B and 1% per month for Part D.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: Medicare &amp; You 2026 Handbook</a></li>
    <li><a href="#" target="_blank" rel="noopener">Kaiser Family Foundation: Medicare Advantage in 2025 (Enrollment Update)</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: 2026 Medicare Parts A and B Premiums and Deductibles</a></li>
    <li><a href="#" target="_blank" rel="noopener">Medicare.gov: What Medicare Covers</a></li>
    <li><a href="#" target="_blank" rel="noopener">KFF: An Overview of the Medicare Part D Prescription Drug Benefit (2025)</a></li>
</ul>
""",
})
