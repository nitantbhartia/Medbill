"""Guide: Home Health Care Billing — What Medicare Pays & What You Owe."""

from guides import register, _embed

register("home-health-care-billing", {
    "title": "Home Health Care Billing: What Medicare Pays & What You Owe (2026)",
    "meta_description": "Medicare covers home health care at $0 cost-sharing — but only if you meet strict criteria. Learn the homebound requirement, the 60-day episode, and how to catch billing errors.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "Does Medicare cover home health care at no cost?",
            "a": "Yes, Medicare Part A and Part B cover home health care at $0 cost-sharing — no deductible, no copay — when four conditions are met: you are homebound, you need skilled care (skilled nursing, physical therapy, occupational therapy, or speech therapy), a physician has ordered the care, and the agency is Medicare-certified. If all four conditions are met and the claim is properly documented, you owe nothing. If you receive a bill for covered home health services, it may be a billing error.",
        },
        {
            "q": "What is the homebound requirement for Medicare home health?",
            "a": "Medicare defines 'homebound' as: leaving home requires considerable and taxing effort, and absences from home are infrequent, for short durations, or for medical appointments. You do not have to be bedridden. You can leave for medical appointments, religious services, or adult day programs and still qualify as homebound. Driving yourself, going to work, or regularly leaving for non-medical activities would disqualify homebound status. Documentation of homebound status is the most frequently cited basis for home health claim denials.",
        },
        {
            "q": "What is a 60-day home health episode under Medicare?",
            "a": "Medicare pays home health agencies in 60-day payment periods called episodes. The agency receives a fixed payment (adjusted by patient severity under PDGM) for all covered services provided during those 60 days. For you as a patient, this means one prior authorization period covers 60 days of care. If you still need care after 60 days, the agency must recertify your eligibility. There is no limit on the number of episodes you can have if you continue to meet eligibility criteria.",
        },
        {
            "q": "Does Medicare cover a home health aide to help me bathe and dress?",
            "a": "Only if you are also receiving skilled care. Medicare does not cover custodial home health aide services (help with bathing, dressing, meals, companionship) on a standalone basis. Home health aide visits are a covered benefit under Medicare only when skilled nursing or therapy services are also actively occurring. If your skilled care ends, Medicare stops covering the home health aide visits too, even if you still need the personal care assistance.",
        },
        {
            "q": "What does private-pay home health cost without insurance?",
            "a": "Home health aides typically charge $25–$45 per hour for custodial/personal care. Skilled nursing visits from a licensed nurse average $150–$250 per visit. Physical therapy visits run $100–$200 per visit. Home health agency costs vary significantly by region — metropolitan areas and coastal states tend to cost 20–40% more than rural or Midwest markets. Long-term care insurance, Medicaid waiver programs, and VA benefits may cover some of these costs depending on eligibility.",
        },
    ],
    "body": f"""
<p class="lead">Home health care is one of the most confusing areas of Medicare billing — and one where errors are common. BillKarma data shows <strong>home health billing errors affect 29% of claims</strong>, most stemming from incorrect homebound status documentation. When properly covered, Medicare pays for home health services at <strong>$0 cost to you</strong> — no deductible, no copay. But the distinction between covered skilled care and non-covered custodial care is the line that determines whether you owe nothing or thousands of dollars per month.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#skilled-vs-custodial">Skilled care vs. custodial care: the critical distinction</a></li>
        <li><a href="#medicare-coverage">What Medicare covers and what it doesn't</a></li>
        <li><a href="#eligibility">The four eligibility criteria for Medicare home health</a></li>
        <li><a href="#pdgm">How Medicare pays home health agencies (PDGM)</a></li>
        <li><a href="#other-coverage">Medicare Advantage, Medicaid, and private insurance</a></li>
        <li><a href="#private-pay">Private-pay and out-of-pocket costs</a></li>
        <li><a href="#billing-codes">HCPCS billing codes for home health</a></li>
        <li><a href="#billing-errors">Common billing errors to catch</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="skilled-vs-custodial">1. Skilled care vs. custodial care: the critical distinction</h2>

<p>The single most important distinction in home health billing is between <strong>skilled care</strong> and <strong>custodial care</strong>. Medicare covers the first. Medicare does not cover the second on its own.</p>

<table>
    <thead>
        <tr><th>Type</th><th>What it includes</th><th>Medicare covers?</th><th>Who provides it</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Skilled nursing care</strong></td><td>Wound care, injections, catheter care, IV therapy, complex medication management, patient education</td><td>Yes, at $0</td><td>RN or LPN</td></tr>
        <tr><td><strong>Physical therapy</strong></td><td>Mobility training, strengthening, fall prevention, post-surgical rehab</td><td>Yes, at $0</td><td>Licensed PT</td></tr>
        <tr><td><strong>Occupational therapy</strong></td><td>Activities of daily living, adaptive techniques, home safety modifications</td><td>Yes, at $0</td><td>Licensed OT</td></tr>
        <tr><td><strong>Speech-language pathology</strong></td><td>Swallowing disorders, speech and cognitive rehabilitation</td><td>Yes, at $0</td><td>SLP</td></tr>
        <tr><td><strong>Medical social work</strong></td><td>Care planning, community resource referrals (only alongside skilled care)</td><td>Yes, at $0</td><td>Licensed MSW</td></tr>
        <tr><td><strong>Home health aide</strong></td><td>Personal care: bathing, dressing, grooming (only alongside skilled care)</td><td>Yes, when skilled care also active</td><td>Home health aide</td></tr>
        <tr><td><strong>Custodial/personal care only</strong></td><td>Help with bathing, dressing, meals, companionship — no skilled component</td><td><strong>No</strong></td><td>Home care aide</td></tr>
    </tbody>
</table>

<p>This distinction is where most billing confusion originates. Many patients believe Medicare covers "home care" generally — it does not. A non-medical home care agency sending someone to help with bathing is providing custodial care, which Medicare does not cover unless skilled services are concurrently occurring.</p>

<div class="key-takeaway">
    <strong>Received a bill for home health that Medicare should have covered?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we check for homebound documentation errors, billing code mismatches, and custodial vs. skilled care classification issues.
</div>

<h2 id="medicare-coverage">2. What Medicare covers and what it doesn't</h2>

<p>When you qualify for Medicare home health coverage, the benefit is comprehensive and cost-sharing is zero:</p>

<ul>
    <li>Skilled nursing visits (as many as medically necessary)</li>
    <li>Physical, occupational, and speech therapy</li>
    <li>Home health aide visits (only when skilled care is also being provided)</li>
    <li>Medical social services</li>
    <li>Durable medical equipment (80% covered under Part B, 20% copay applies)</li>
    <li>Medical supplies used during home health visits</li>
</ul>

<p><strong>What Medicare does not cover under home health:</strong></p>

<ul>
    <li>24-hour-a-day home care</li>
    <li>Meals delivered to your home</li>
    <li>Homemaker services (cleaning, laundry) not related to patient care</li>
    <li>Personal care (bathing, dressing) when no skilled care is also occurring</li>
    <li>Custodial nursing home-type care at home</li>
</ul>

<h2 id="eligibility">3. The four eligibility criteria for Medicare home health</h2>

<p>All four of the following criteria must be met for Medicare to cover home health services. Missing any one of them results in denial.</p>

<ol>
    <li>
        <strong>You are homebound.</strong> Leaving home requires considerable and taxing effort. Brief, infrequent absences for medical care or other reasons (including adult day programs) do not disqualify homebound status. A physician must certify and document homebound status. This is the most frequently contested criterion — keep records of what assistance you need to leave home.
    </li>
    <li>
        <strong>You need skilled care.</strong> Your condition requires the skill of a licensed nurse, physical therapist, occupational therapist, or speech-language pathologist. The care must be medically necessary, not routine or maintenance-only. However, if skilled oversight is needed to ensure safe performance of a maintenance program (such as preventing decline), that can qualify as skilled.
    </li>
    <li>
        <strong>A physician has ordered the care.</strong> A licensed physician (or in some cases a nurse practitioner or physician assistant) must certify your eligibility and sign a plan of care. Re-certification is required every 60 days.
    </li>
    <li>
        <strong>The agency is Medicare-certified.</strong> The home health agency must be approved by Medicare. You can verify certification at Medicare.gov's Care Compare tool. Using a non-certified agency for services you expect Medicare to cover is a common and expensive mistake.
    </li>
</ol>

<p><strong>The 3-day hospital stay rule:</strong> Unlike skilled nursing facility benefits, Medicare home health does not require a prior 3-day inpatient hospital stay. This is a common misconception. You can qualify for Medicare home health directly, without a hospitalization, as long as the four criteria above are met.</p>

<h2 id="pdgm">4. How Medicare pays home health agencies (PDGM)</h2>

<p>Since 2020, Medicare has paid home health agencies under the <strong>Patient-Driven Groupings Model (PDGM)</strong>. Under PDGM, Medicare pays a fixed per-episode rate adjusted for your clinical characteristics. The agency receives one lump payment per 30-day period (two periods = one 60-day episode), rather than being paid per visit.</p>

<table>
    <thead>
        <tr><th>PDGM factor</th><th>What it affects</th></tr>
    </thead>
    <tbody>
        <tr><td>Admission source (community vs. institutional)</td><td>Higher payment for patients discharged from hospital or post-acute facility</td></tr>
        <tr><td>Clinical grouping (primary diagnosis)</td><td>Payment varies by condition type (e.g., musculoskeletal vs. behavioral health)</td></tr>
        <tr><td>Functional impairment level</td><td>Higher payment for patients with greater functional deficits (OASIS assessment)</td></tr>
        <tr><td>Comorbidity adjustment</td><td>Higher payment when qualifying secondary diagnoses are present</td></tr>
    </tbody>
</table>

<p>The typical Medicare payment per 60-day episode ranges from <strong>$1,800 to $5,000</strong> depending on these factors. For you as a patient, the key point is: <strong>your cost is $0 regardless of the episode payment amount</strong>. You are not responsible for any portion of the PDGM payment. If you are billed for covered services, that is a billing error.</p>

<h2 id="other-coverage">5. Medicare Advantage, Medicaid, and private insurance</h2>

<p><strong>Medicare Advantage (Part C):</strong> MA plans must cover the same home health services as traditional Medicare but may restrict you to in-network agencies. Always verify that your home health agency is in your MA plan's network before starting care. Out-of-network agencies may result in higher cost-sharing or denied claims.</p>

<p><strong>Medicaid:</strong> Traditional Medicare does not cover custodial home care, but Medicaid may — through Home and Community-Based Services (HCBS) waiver programs. These programs vary by state and often have waiting lists. Medicaid can cover personal care aides, homemaker services, and other supports that Medicare does not. Eligibility is income- and asset-based.</p>

<p><strong>Long-term care insurance:</strong> Private LTC insurance typically covers home health care, including custodial care, after an elimination period (typically 30–90 days). Review your policy's definition of "benefit trigger" — most require inability to perform 2 of 6 Activities of Daily Living (ADLs) or cognitive impairment.</p>

<p><strong>VA benefits:</strong> Veterans may be eligible for home-based primary care, skilled home health, and homemaker/home health aide services through the VA, independent of Medicare coverage.</p>

<h2 id="private-pay">6. Private-pay and out-of-pocket costs</h2>

<p>For services Medicare does not cover (custodial care, personal aides, etc.), costs are paid out of pocket unless covered by Medicaid, LTC insurance, or VA benefits.</p>

<table>
    <thead>
        <tr><th>Service</th><th>Typical cost</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Home health aide (custodial)</td><td>$25–$45/hour</td><td>Varies significantly by region</td></tr>
        <tr><td>Skilled nursing visit (private pay)</td><td>$150–$250/visit</td><td>Higher in metro areas</td></tr>
        <tr><td>Physical therapy visit</td><td>$100–$200/visit</td><td>Agency rate vs. independent PT</td></tr>
        <tr><td>Live-in home care aide</td><td>$200–$350/day</td><td>24-hour availability</td></tr>
        <tr><td>Adult day program</td><td>$75–$150/day</td><td>Medicaid often covers for eligible patients</td></tr>
    </tbody>
</table>

<h2 id="billing-codes">7. HCPCS billing codes for home health</h2>

<p>Home health services are billed primarily using HCPCS G-codes. Seeing these on your explanation of benefits (EOB) helps verify that the services billed match what was provided.</p>

<table>
    <thead>
        <tr><th>HCPCS code</th><th>Service</th></tr>
    </thead>
    <tbody>
        <tr><td>G0151</td><td>Physical therapy visit</td></tr>
        <tr><td>G0152</td><td>Occupational therapy visit</td></tr>
        <tr><td>G0153</td><td>Speech-language pathology visit</td></tr>
        <tr><td>G0154</td><td>Skilled nursing visit</td></tr>
        <tr><td>G0155</td><td>Medical social worker visit</td></tr>
        <tr><td>G0156</td><td>Home health aide visit</td></tr>
        <tr><td>G0157</td><td>Home health agency evaluation</td></tr>
    </tbody>
</table>

<p>The OASIS (Outcome and Assessment Information Set) assessment is required at the start of care, at recertification, and at discharge. It documents your clinical status and drives the PDGM payment calculation. The OASIS is not separately billed to you — it is part of the agency's documentation requirement.</p>

<h2 id="billing-errors">8. Common billing errors to catch</h2>

<p>BillKarma identifies home health billing errors in 29% of claims reviewed. The most common errors:</p>

<ul>
    <li><strong>Billing for visits not made:</strong> Agencies sometimes bill for a scheduled visit that was cancelled or not made. Cross-reference visit dates on your bill against your own records or a visit log.</li>
    <li><strong>Wrong number of visits:</strong> The bill shows 20 visits but only 15 were made. This can happen when billing is automated and schedule changes aren't communicated to billing staff.</li>
    <li><strong>Billing a skilled nursing code for custodial care:</strong> G0154 (skilled nursing) should only appear when an RN or LPN provided skilled care. If an aide helped you bathe and that visit was billed as G0154, that is upcoding.</li>
    <li><strong>Incorrect homebound status documentation:</strong> The agency may have documented homebound status incorrectly, causing the claim to be denied — but then billed to you instead of correcting the documentation and resubmitting.</li>
    <li><strong>Out-of-network MA billing:</strong> If you're on a Medicare Advantage plan and the agency is out-of-network, the claim may be denied and the balance billed to you. Verify network status before starting care.</li>
    <li><strong>Duplicate billing across episodes:</strong> The same service billed at the end of one episode and the beginning of the next.</li>
</ul>

<div class="key-takeaway">
    <strong>Verify your home health agency is Medicare-certified.</strong> Check at <a href="https://www.medicare.gov/care-compare/" target="_blank" rel="noopener">Medicare Care Compare</a> before starting care — and <a href="/fight-debt">contact BillKarma</a> if you receive a bill for services that should have been covered at $0.
</div>

{_embed(mode="cost", title="Look up Medicare rates for home health billing codes", subtitle="Enter a HCPCS code like G0154 to see the Medicare benchmark rate.")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Medicare cover home health care at no cost?</h3>
        <p>Yes — when all four eligibility criteria are met (homebound, skilled care needed, physician order, Medicare-certified agency), Medicare covers home health at $0 cost-sharing. No deductible, no copay. If you receive a bill for covered services, it is likely a billing error worth disputing.</p>
    </div>

    <div class="faq-item">
        <h3>What is the homebound requirement for Medicare home health?</h3>
        <p>Leaving home must require considerable and taxing effort. You do not have to be bedridden — brief absences for medical care, religious services, or adult day programs are allowed. Regularly driving yourself out for non-medical activities would disqualify homebound status. Proper documentation of homebound status is the most frequently disputed home health billing issue.</p>
    </div>

    <div class="faq-item">
        <h3>What is a 60-day home health episode under Medicare?</h3>
        <p>Medicare pays home health agencies in 60-day periods. The agency is recertified every 60 days if you still qualify. There is no limit on the number of episodes you can have. Your cost is $0 for each episode as long as you continue to meet eligibility criteria.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover a home health aide to help me bathe and dress?</h3>
        <p>Only if you are also receiving skilled nursing or therapy services. Medicare covers home health aide visits as part of a skilled care plan — not as a standalone benefit. When skilled services end, Medicare home health aide coverage ends too, even if you still need personal care assistance.</p>
    </div>

    <div class="faq-item">
        <h3>What does private-pay home health cost without insurance?</h3>
        <p>Home health aides charge $25–$45/hour for custodial care. Skilled nursing visits average $150–$250/visit. Costs vary significantly by region. Medicaid waiver programs, long-term care insurance, and VA benefits may cover custodial services that Medicare does not.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.medicare.gov/coverage/home-health-services" target="_blank" rel="noopener">Medicare.gov: Home Health Services Coverage</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/home-health-agency-pdgm" target="_blank" rel="noopener">CMS: Patient-Driven Groupings Model (PDGM)</a></li>
    <li><a href="https://www.cms.gov/files/document/pdgm-fact-sheet.pdf" target="_blank" rel="noopener">CMS: PDGM Fact Sheet</a></li>
    <li><a href="https://www.medicare.gov/care-compare/" target="_blank" rel="noopener">Medicare Care Compare: Find Medicare-Certified Home Health Agencies</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/home-health-care-and-medicares-oasis-assessment/" target="_blank" rel="noopener">KFF: Medicare Home Health Coverage and OASIS Assessment</a></li>
    <li><a href="https://www.genworth.com/aging-and-you/finances/cost-of-care.html" target="_blank" rel="noopener">Genworth Cost of Care Survey (2025)</a></li>
</ul>
""",
})
