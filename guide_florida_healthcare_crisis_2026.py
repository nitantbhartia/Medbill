"""Guide: Florida Healthcare Affordability Crisis 2026."""

from guides import register, _embed

register("florida-healthcare-affordability-2026", {
    "title": "Florida Healthcare Affordability Crisis 2026: Costs, Coverage Gaps, and Solutions",
    "meta_description": "Florida's 2.8M uninsured face rising costs, no Medicaid expansion, and expiring ACA subsidies. Learn about charity care, balance billing, and coverage options.",
    "published": "2026-03-04",
    "author": "BillKarma Team",
    "category": "Health Insurance",
    "faqs": [
        {
            "q": "Why is healthcare so expensive in Florida in 2026?",
            "a": "Florida faces a convergence of factors: it has not expanded Medicaid under the ACA, leaving 1.1 million adults in the coverage gap. Enhanced ACA subsidies expired in January 2026, and Florida saw a 31.5% base rate increase in marketplace premiums. The state has the highest Medicare Advantage penetration in the nation (56%), which drives up costs for remaining traditional Medicare patients. Florida also has limited balance billing protections and a high concentration of for-profit hospitals.",
        },
        {
            "q": "Does Florida have Medicaid expansion?",
            "a": "No. Florida is one of 10 states that has not expanded Medicaid under the ACA. This means adults without dependent children generally cannot qualify for Medicaid regardless of income, and parents qualify only at very low income levels (approximately 26% of the federal poverty level, or about $8,100 for a family of three). An estimated 1.1 million Floridians fall into the coverage gap, earning too much for traditional Medicaid but too little for ACA marketplace subsidies.",
        },
        {
            "q": "What are Florida's balance billing protections?",
            "a": "Florida has moderate balance billing protections under HB 221 (2016), which prohibits balance billing for emergency services at hospitals and freestanding emergency departments when the facility is in-network but the treating physician is out-of-network. However, this law has significant gaps: it does not cover ground ambulance, non-emergency services, or situations where both the facility and physician are out-of-network. The federal No Surprises Act provides additional protections for emergency services.",
        },
        {
            "q": "What charity care options exist in Florida?",
            "a": "Nonprofit hospitals in Florida must offer financial assistance under IRS Section 501(r). Florida also has a state-funded charity care program through the Safety Net Hospital Alliance of Florida, which distributes funding to hospitals serving high volumes of uninsured patients. Many large Florida hospital systems including AdventHealth, Baptist Health, and Orlando Health offer financial assistance for patients earning up to 200-400% of the federal poverty level. Apply before receiving non-emergency care.",
        },
        {
            "q": "How does hurricane season affect healthcare costs in Florida?",
            "a": "Hurricane season (June-November) creates healthcare cost spikes due to emergency room surges, pharmacy shortages, disrupted medical supply chains, and displacement of patients from their regular providers. After major hurricanes, FEMA provides Crisis Counseling Program grants and HHS may issue Section 1135 waivers that expand Medicaid and Medicare coverage temporarily. Floridians should maintain a 30-day medication supply and know their nearest FQHC locations as part of hurricane preparedness.",
        },
        {
            "q": "What is the Medicaid coverage gap in Florida?",
            "a": "The coverage gap affects adults who earn too much for Florida's traditional Medicaid (roughly above 26% FPL for parents, with no coverage for childless adults) but below 100% FPL ($15,060 individual / $31,200 family of four). These individuals do not qualify for ACA marketplace subsidies either, since subsidies start at 100% FPL in non-expansion states. An estimated 1.1 million Floridians are in this gap with no affordable coverage option.",
        },
    ],
    "body": f"""
<p class="lead">Florida has the <strong>third-largest uninsured population</strong> in the nation at 2.8 million residents, and 2026 is making things worse. ACA marketplace premiums jumped <strong>31.5%</strong> after enhanced subsidies expired. The state has not expanded Medicaid, leaving <strong>1.1 million adults in the coverage gap</strong> with no affordable insurance option. Florida has the <strong>highest Medicare Advantage penetration</strong> in the country at 56%, a large for-profit hospital sector, and limited balance billing protections. If you live in Florida, this guide covers your coverage options, financial assistance programs, and strategies for managing healthcare costs in 2026.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#coverage-crisis">Florida&rsquo;s coverage crisis: the numbers</a></li>
        <li><a href="#medicaid-gap">The Medicaid expansion gap</a></li>
        <li><a href="#aca-subsidy-impact">ACA subsidy expiration impact on Florida</a></li>
        <li><a href="#medicare-advantage">Medicare Advantage in Florida: highest penetration</a></li>
        <li><a href="#balance-billing">Balance billing protections (and gaps)</a></li>
        <li><a href="#charity-care">Charity care and financial assistance options</a></li>
        <li><a href="#hurricane-preparedness">Hurricane season medical preparedness</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="coverage-crisis">1. Florida&rsquo;s coverage crisis: the numbers</h2>

<p>Florida&rsquo;s healthcare affordability challenges are driven by a combination of policy decisions and market dynamics that together create one of the most difficult environments for patients in the country.</p>

<table>
    <thead>
        <tr><th>Metric</th><th>Florida</th><th>National Average</th></tr>
    </thead>
    <tbody>
        <tr><td>Uninsured rate (all ages)</td><td>13.2%</td><td>8.0%</td></tr>
        <tr><td>Uninsured population</td><td>2.8 million</td><td>&mdash;</td></tr>
        <tr><td>Adults in Medicaid coverage gap</td><td>1.1 million</td><td>1.5 million (all non-expansion states)</td></tr>
        <tr><td>ACA premium increase (2026)</td><td>31.5% (base rate)</td><td>22%</td></tr>
        <tr><td>Medicare Advantage penetration</td><td>56%</td><td>33%</td></tr>
        <tr><td>For-profit hospital share</td><td>~55%</td><td>~25%</td></tr>
        <tr><td>ER markup over Medicare (avg.)</td><td>5.3x</td><td>3.5x</td></tr>
    </tbody>
</table>

<p>Florida&rsquo;s for-profit hospital concentration is more than double the national average. For-profit hospitals are not required to offer charity care under IRS Section 501(r) (that applies only to nonprofits), which means a large share of Florida patients have no automatic access to financial assistance programs.</p>

<div class="key-takeaway">
    <strong>Florida&rsquo;s unique challenge:</strong> The combination of no Medicaid expansion, the highest Medicare Advantage penetration, a large for-profit hospital sector, and the 2026 ACA subsidy expiration creates a &ldquo;perfect storm&rdquo; for healthcare affordability. Floridians need to be especially proactive about knowing their rights and pursuing financial assistance.
</div>

<h2 id="medicaid-gap">2. The Medicaid expansion gap</h2>

<p>Florida is one of 10 states that has not expanded Medicaid under the Affordable Care Act. This creates a <strong>coverage gap</strong> that affects an estimated 1.1 million Floridians&mdash;more than any other non-expansion state.</p>

<p>Here is how the gap works:</p>

<ul>
    <li><strong>Traditional Medicaid in Florida</strong> covers parents and caretaker relatives only up to approximately <strong>26% of the federal poverty level</strong> ($8,100 for a family of three). Childless adults generally do not qualify at any income level.</li>
    <li><strong>ACA marketplace subsidies</strong> are available starting at <strong>100% FPL</strong> ($15,060 individual / $31,200 family of four).</li>
    <li><strong>The gap:</strong> Adults earning between 26% and 100% FPL (roughly $4,000&ndash;$15,060 for an individual) qualify for neither Medicaid nor marketplace subsidies. They have no affordable coverage option.</li>
</ul>

<table>
    <thead>
        <tr><th>Income Level</th><th>Coverage Available</th><th>Approximate Monthly Cost</th></tr>
    </thead>
    <tbody>
        <tr><td>Below 26% FPL (parents only)</td><td>Florida Medicaid</td><td>$0</td></tr>
        <tr><td>26%&ndash;100% FPL</td><td><strong>NONE (coverage gap)</strong></td><td>No affordable option</td></tr>
        <tr><td>100%&ndash;150% FPL</td><td>ACA marketplace with subsidies</td><td>$0&ndash;$50/mo (after subsidies)</td></tr>
        <tr><td>150%&ndash;400% FPL</td><td>ACA marketplace with reduced subsidies (2026)</td><td>$150&ndash;$600/mo</td></tr>
        <tr><td>Above 400% FPL</td><td>ACA marketplace, no subsidy (2026)</td><td>$600&ndash;$1,200+/mo</td></tr>
    </tbody>
</table>

<p>If you fall in the coverage gap, your best options are:</p>

<ul>
    <li><strong>Community health centers.</strong> Florida has 49 Federally Qualified Health Centers (FQHCs) with over 600 service sites. They serve patients regardless of insurance and charge on a sliding fee scale. Find one at <a href="https://findahealthcenter.hrsa.gov/" target="_blank" rel="noopener">FindAHealthCenter.hrsa.gov</a>.</li>
    <li><strong>Hospital charity care.</strong> Nonprofit hospitals (approximately 45% of Florida hospitals) must offer financial assistance. See Section 6 below.</li>
    <li><strong>Negotiated self-pay rates.</strong> Even for-profit hospitals often offer self-pay discounts of 20&ndash;50%. Always ask before receiving care.</li>
</ul>

<h2 id="aca-subsidy-impact">3. ACA subsidy expiration impact on Florida</h2>

<p>The expiration of enhanced ACA subsidies on January 1, 2026 hit Florida especially hard. Florida had the <strong>largest ACA marketplace enrollment</strong> of any state&mdash;over 3.6 million people&mdash;and its 31.5% base rate increase was the largest among big states.</p>

<div class="bill-example">
    <div class="bill-header">Florida ACA Premium Impact: Family of Four, $60,000 Income (192% FPL)</div>
    <div class="line-item">
        <span>2025 Silver plan premium (after enhanced subsidy)</span>
        <span>$558/mo</span>
    </div>
    <div class="line-item flagged">
        <span>2026 Silver plan premium (after reduced subsidy) &nbsp; &#9888; <em>$306/mo increase</em></span>
        <span>$864/mo</span>
    </div>
    <div class="line-total">
        <span>ANNUAL INCREASE</span>
        <span>$3,672/yr</span>
    </div>
</div>

<p>Aetna exited the Florida marketplace entirely for 2026, reducing competition in many counties. In some rural Florida counties, only one or two insurers remain. Early CMS data shows Florida marketplace enrollment declined by approximately 400,000 in the first two months of 2026.</p>

<p>If your Florida ACA premium has become unaffordable, see our <a href="/guides/aca-premium-increases-2026-by-state">state-by-state guide to ACA premium increases</a> for strategies to reduce costs, including switching to a Bronze plan and checking Medicaid eligibility.</p>

<div class="case-study">
    <h3>Case study: Jacksonville family navigates subsidy loss</h3>
    <p><strong>Situation:</strong> The Martinez family in Jacksonville&mdash;parents ages 38 and 36, two children&mdash;earned $65,000 (208% FPL). Their 2025 Silver plan cost $220/month after enhanced subsidies. In 2026, the same plan rose to $680/month.</p>
    <p><strong>What they did:</strong> They switched to a Bronze plan at $340/month with a $7,500 deductible. They confirmed eligibility for cost-sharing reductions was lost by moving off Silver. They used our <a href="/calculator">cost calculator</a> to compare total expected spending and <a href="/charity-care">checked charity care eligibility</a> at their local Baptist Health hospital, which covers families up to 300% FPL.</p>
    <p><strong>Result:</strong> Annual premium savings of $4,080 vs. the Silver plan. They also found that their local FQHC offered well-child visits and vaccinations on a sliding scale, reducing their out-of-pocket pediatric costs by approximately $600/year.</p>
</div>

<h2 id="medicare-advantage">4. Medicare Advantage in Florida: highest penetration</h2>

<p>Florida has the <strong>highest Medicare Advantage penetration rate</strong> of any state at 56%&mdash;compared to the national average of 33%. More than 2.5 million Florida Medicare beneficiaries are enrolled in MA plans rather than traditional Medicare.</p>

<p>This matters for several reasons:</p>

<ul>
    <li><strong>Prior authorization barriers.</strong> MA plans use prior authorization far more aggressively than traditional Medicare. The HHS OIG found that MA plans denied 13% of prior auth requests, with 75% of those denials overturned on appeal. In Florida, the high MA concentration means more patients face these barriers.</li>
    <li><strong>Network restrictions.</strong> MA plans limit which providers and hospitals you can use. In Florida, where hospital systems like HCA Healthcare dominate certain markets, being in or out of an MA plan&rsquo;s network can dramatically affect your costs.</li>
    <li><strong>Plan churn.</strong> Florida has aggressive MA plan marketing, and many seniors switch plans annually. Switching plans can disrupt provider relationships and trigger unexpected out-of-network bills.</li>
</ul>

<p>If you are on Medicare Advantage in Florida and facing claim denials, see our <a href="/guides/medicare-advantage-billing-explained">Medicare Advantage billing guide</a> and <a href="/guides/how-to-appeal-insurance-denial-and-win">insurance appeal guide</a>.</p>

<div class="key-takeaway">
    <strong>Florida Medicare Advantage tip:</strong> If your MA plan denies a service that would be covered under traditional Medicare, you have strong grounds for appeal. The 2024 CMS final rule requires MA plans to cover anything traditional Medicare covers. Reference this rule in your appeal letter. <a href="/scan">Scan your Medicare bill with BillKarma</a> to identify denied services and their Medicare coverage status.
</div>

<h2 id="balance-billing">5. Balance billing protections (and gaps)</h2>

<p>Florida has <strong>partial</strong> balance billing protections, but significant gaps remain.</p>

<h3>What IS protected</h3>

<p>Under Florida HB 221 (2016) and the federal No Surprises Act (2022):</p>

<ul>
    <li>Emergency services at hospitals and freestanding ERs cannot be balance billed beyond in-network cost-sharing</li>
    <li>Out-of-network providers at in-network facilities cannot balance bill for most non-emergency services (post-stabilization care, ancillary services)</li>
    <li>Air ambulance services (covered by the No Surprises Act)</li>
</ul>

<h3>What is NOT protected</h3>

<ul>
    <li><strong>Ground ambulance.</strong> Florida has no state law protecting patients from ground ambulance balance billing, and the No Surprises Act excludes ground ambulance. See our <a href="/guides/ground-ambulance-billing-costs">ground ambulance billing guide</a>.</li>
    <li><strong>Non-emergency out-of-network care.</strong> If you knowingly choose an out-of-network provider for non-emergency care, balance billing protections generally do not apply.</li>
    <li><strong>Self-funded employer plans.</strong> State balance billing laws do not apply to self-funded plans (which cover approximately 65% of employer-insured workers). Federal NSA protections still apply.</li>
</ul>

<p>If you receive a surprise balance bill in Florida, file a complaint with the <a href="https://www.floir.com/" target="_blank" rel="noopener">Florida Office of Insurance Regulation</a> or call the CMS No Surprises Help Desk at 1-800-985-3059. See our <a href="/guides/florida-hospital-billing-rights">Florida hospital billing rights guide</a> for complete details on wage garnishment exemptions and dispute procedures.</p>

<h2 id="charity-care">6. Charity care and financial assistance options</h2>

<p>Despite Florida&rsquo;s large for-profit hospital sector, meaningful financial assistance is available if you know where to look:</p>

<h3>Nonprofit hospital charity care</h3>

<p>Approximately 45% of Florida hospitals are nonprofit and must offer financial assistance under IRS Section 501(r). Major nonprofit systems include:</p>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Free Care Threshold</th><th>Discounted Care Threshold</th><th>Locations</th></tr>
    </thead>
    <tbody>
        <tr><td>AdventHealth</td><td>Up to 200% FPL</td><td>Up to 400% FPL</td><td>Central FL, Tampa, Daytona</td></tr>
        <tr><td>Baptist Health South Florida</td><td>Up to 200% FPL</td><td>Up to 300% FPL</td><td>Miami-Dade, Broward</td></tr>
        <tr><td>Orlando Health</td><td>Up to 200% FPL</td><td>Up to 300% FPL</td><td>Central FL</td></tr>
        <tr><td>Tampa General Hospital</td><td>Up to 200% FPL</td><td>Up to 400% FPL</td><td>Tampa Bay</td></tr>
        <tr><td>UF Health</td><td>Up to 200% FPL</td><td>Up to 400% FPL</td><td>Gainesville, Jacksonville</td></tr>
    </tbody>
</table>

<p><a href="/charity-care">Check your eligibility for hospital financial assistance</a> before receiving non-emergency care. Apply before you pay&mdash;most hospitals will not refund payments if you qualify retroactively.</p>

<h3>Safety Net Hospital Alliance</h3>

<p>Florida&rsquo;s Safety Net Hospital Alliance distributes state and federal funding to 14 safety net hospitals that serve disproportionately high volumes of uninsured and Medicaid patients. These hospitals, including Jackson Memorial (Miami), Tampa General, and UF Health Jacksonville, are required to provide care regardless of ability to pay and often have the most generous financial assistance programs.</p>

<h3>Community health centers</h3>

<p>Florida has 49 FQHCs with over 600 service sites statewide. They provide primary care, dental, behavioral health, and pharmacy services on a sliding fee scale. No one is turned away for inability to pay. Find your nearest center at <a href="https://findahealthcenter.hrsa.gov/" target="_blank" rel="noopener">FindAHealthCenter.hrsa.gov</a>.</p>

<h2 id="hurricane-preparedness">7. Hurricane season medical preparedness</h2>

<p>Florida&rsquo;s hurricane season (June through November) creates unique healthcare challenges. Major storms disrupt pharmacy access, close clinics, overwhelm emergency rooms, and displace patients from their regular providers. Being medically prepared is as important as boarding up windows.</p>

<h3>Before hurricane season</h3>

<ul>
    <li><strong>Maintain a 30-day medication supply.</strong> Most insurers will authorize an early refill of maintenance medications before a named storm approaches. Call your insurer or pharmacy to request an emergency supply override.</li>
    <li><strong>Download your medical records.</strong> Keep digital copies of your medication list, allergies, diagnoses, and recent test results. See our <a href="/guides/medical-records-rights-explained">medical records rights guide</a>.</li>
    <li><strong>Know your nearest FQHC and emergency facilities.</strong> After a storm, your regular provider may be closed. Identify backup locations now.</li>
    <li><strong>Review your insurance coverage.</strong> Confirm whether your plan covers emergency out-of-area care and whether your insurer has a disaster relief policy (many waive prior auth requirements during declared emergencies).</li>
</ul>

<h3>After a hurricane</h3>

<ul>
    <li><strong>HHS Section 1135 waivers.</strong> After a federally declared disaster, HHS can waive certain Medicare, Medicaid, and CHIP requirements. This may include expanded coverage for out-of-area providers, waived prior authorization, and extended prescription refill allowances.</li>
    <li><strong>FEMA disaster assistance.</strong> FEMA may cover medical and dental expenses not covered by insurance that resulted from the disaster. Apply at <a href="https://www.disasterassistance.gov/" target="_blank" rel="noopener">DisasterAssistance.gov</a>.</li>
    <li><strong>Watch for billing errors.</strong> Post-hurricane ER visits often generate inflated bills due to surge pricing, miscoded services, and overwhelmed billing departments. <a href="/scan">Scan any post-storm medical bills with BillKarma</a> to catch errors.</li>
</ul>

<div class="key-takeaway">
    <strong>Florida-specific action steps:</strong> <a href="/charity-care">Check your charity care eligibility</a> at your local hospital. <a href="/scan">Scan every medical bill</a> for errors and overcharges. If you are in the Medicaid coverage gap, use FQHCs for primary care and negotiate self-pay rates for hospital services using our <a href="/calculator">cost calculator</a> to reference Medicare rates.
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.kff.org/medicaid/issue-brief/status-of-state-medicaid-expansion-decisions/" target="_blank" rel="noopener">KFF: Status of State Medicaid Expansion Decisions</a></li>
    <li><a href="https://ahca.myflorida.com/" target="_blank" rel="noopener">Florida Agency for Health Care Administration (AHCA)</a></li>
    <li><a href="https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data" target="_blank" rel="noopener">CMS: Medicare Advantage Enrollment Data by State</a></li>
    <li><a href="https://www.floir.com/" target="_blank" rel="noopener">Florida Office of Insurance Regulation (OIR)</a></li>
    <li><a href="https://www.kff.org/health-reform/issue-brief/how-aca-marketplace-premiums-are-changing-by-state-in-2026/" target="_blank" rel="noopener">KFF: ACA Marketplace Premium Changes by State (2026)</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Consumer Protections</a></li>
    <li><a href="http://www.leg.state.fl.us/statutes/" target="_blank" rel="noopener">Florida Legislature: Online Sunshine (State Statutes)</a></li>
</ul>
""",
})
