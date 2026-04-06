"""Guide: Medigap Plans Explained: Medicare Supplement Guide (2026)."""

from guides import register, _embed

register("medigap-medicare-supplement", {
    "title": "Medigap Plans Explained: Medicare Supplement Guide (2026)",
    "meta_description": "Medigap Plan G covers nearly all Medicare gaps for $100\u2013$400/month. Compare Plans A\u2013N, premiums, and Advantage vs. Medigap to find your best fit in 2026.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is a Medigap plan and how does it work?",
            "a": "A Medigap plan (also called a Medicare Supplement plan) is private health insurance that fills the cost gaps left by Original Medicare Parts A and B. Original Medicare typically pays 80% of approved costs after you meet the Part B deductible ($257 in 2026); Medigap pays some or all of the remaining 20%, plus other out-of-pocket costs like the Part A hospital deductible ($1,676 per benefit period in 2026) and excess charges. You keep your Original Medicare coverage and use Medigap as a secondary payer. Medigap plans are standardized by federal law, meaning a Plan G from one insurer covers the exact same benefits as a Plan G from any other insurer&mdash;only the premium differs.",
        },
        {
            "q": "What does Medigap Plan G cover in 2026?",
            "a": "Plan G covers: the Part A hospital coinsurance and an additional 365 hospital days after Medicare benefits are exhausted; the Part A hospice care coinsurance or copayment; the Part A deductible ($1,676 per benefit period); the Part B coinsurance or copayment; the Part B excess charges; skilled nursing facility coinsurance; and foreign travel emergency coverage (80% up to $50,000 lifetime, after $250 deductible). The only gap Plan G does not cover is the Part B deductible ($257 in 2026). Because Plan F (which covers the Part B deductible) is no longer available to new Medicare enrollees as of 2020, Plan G has become the most comprehensive option for new enrollees.",
        },
        {
            "q": "What is the difference between Medigap Plan G and Plan N?",
            "a": "Both Plan G and Plan N cover the Part A deductible, Part A coinsurance, skilled nursing facility coinsurance, and foreign travel emergency care. The differences: Plan G covers the Part B coinsurance in full and covers Part B excess charges. Plan N requires copays of up to $20 per office visit and up to $50 per emergency room visit (waived if admitted), and does not cover Part B excess charges. Plan N premiums are typically $40 to $100 per month lower than Plan G. If your doctors always accept Medicare assignment (meaning they do not charge excess fees), Plan N may offer equivalent real-world coverage at a lower premium.",
        },
        {
            "q": "When is the best time to buy a Medigap plan?",
            "a": "The best time is during your Medigap Open Enrollment Period (OEP)&mdash;the six-month window that begins the month you turn 65 and are enrolled in Medicare Part B. During your OEP, insurers cannot use medical underwriting to deny coverage or charge you a higher premium based on your health history. Outside of your OEP, insurers in most states can reject your application or charge significantly more if you have pre-existing conditions. If you miss your OEP, your options depend on your state&rsquo;s guaranteed issue rights and whether you qualify for a Special Enrollment Period (SEP) due to a qualifying life event.",
        },
        {
            "q": "Can I switch from Medicare Advantage to Medigap?",
            "a": "Yes, but it is not always easy. If you are within the first 12 months of your Medicare Advantage plan, you have a trial right to return to Original Medicare and enroll in any Medigap policy with guaranteed issue rights. Outside of that 12-month window, you lose guaranteed issue rights in most states, meaning a Medigap insurer can reject your application or charge more based on health conditions. A few states (California, Connecticut, Maine, Massachusetts, New York, and others) have stronger consumer protections that make switching easier year-round. Check your state insurance commissioner&rsquo;s website for state-specific rules.",
        },
    ],
    "body": f"""
<p class="lead">Original Medicare leaves you with significant cost exposure: a Part A hospital deductible of <strong>$1,676 per benefit period</strong>, a Part B coinsurance of <strong>20% with no cap</strong>, and daily coinsurance for extended hospital stays that can reach <strong>$1,118 per day</strong> after 90 days. Medigap insurance fills these gaps&mdash;and BillKarma&rsquo;s analysis shows that Medicare beneficiaries with Plan G or Plan N <strong>average $4,200 less per year in out-of-pocket costs</strong> than those with Original Medicare alone. This guide explains every plan option, current 2026 premiums, and how to choose between Medigap and Medicare Advantage.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-medigap-covers">What Medigap covers: the Medicare gaps explained</a></li>
        <li><a href="#plan-comparison">Plan A through N comparison table</a></li>
        <li><a href="#plan-g-plan-n">Plan G vs. Plan N: the most popular options</a></li>
        <li><a href="#premiums">2026 Medigap premium ranges by plan</a></li>
        <li><a href="#medigap-vs-advantage">Medigap vs. Medicare Advantage comparison</a></li>
        <li><a href="#when-to-buy">When to buy: open enrollment rules</a></li>
        <li><a href="#billing-interactions">How Medigap interacts with your medical bills</a></li>
        <li><a href="#case-study">Real-world case study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-medigap-covers">1. What Medigap covers: the Medicare gaps explained</h2>

<p>To understand Medigap, you need to know exactly what Original Medicare leaves uncovered. Here are the main cost gaps in 2026:</p>

<table>
    <thead>
        <tr>
            <th>Medicare Gap</th>
            <th>2026 Amount</th>
            <th>Covered by Medigap?</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Part A hospital deductible (per benefit period)</td><td>$1,676</td><td>Yes (Plans C, D, F, G, M, N partially)</td></tr>
        <tr><td>Part A hospital coinsurance (days 61&ndash;90)</td><td>$419/day</td><td>Yes (all plans)</td></tr>
        <tr><td>Part A hospital coinsurance (days 91+, lifetime reserve)</td><td>$838/day</td><td>Yes (all plans)</td></tr>
        <tr><td>Part B deductible</td><td>$257/year</td><td>Plans C and F only (not available to new enrollees since 2020)</td></tr>
        <tr><td>Part B coinsurance (20% of all approved services)</td><td>Unlimited</td><td>Yes (all plans except K and L, which cover partial)</td></tr>
        <tr><td>Part B excess charges</td><td>Up to 15% above Medicare</td><td>Plans F and G only</td></tr>
        <tr><td>Skilled nursing facility coinsurance (days 21&ndash;100)</td><td>$209.50/day</td><td>Most plans (not A or B)</td></tr>
        <tr><td>Foreign travel emergency (up to $50,000)</td><td>80% after $250 deductible</td><td>Plans C, D, F, G, M, N</td></tr>
    </tbody>
</table>

<p>The Part B coinsurance gap is the most financially dangerous for high utilizers of medical services. Without Medigap, a Medicare beneficiary who spends $60,000 in Medicare-approved charges in a year faces $12,000 in coinsurance. Plan G eliminates that exposure entirely (except for the $257 Part B deductible).</p>

<h2 id="plan-comparison">2. Plan A through N comparison table</h2>

<p>All Medigap plans are standardized by federal law under 42 CFR &sect;403.205. Every insurer selling Plan G must provide the same benefits as every other insurer selling Plan G. The following table shows what each plan covers:</p>

<table>
    <thead>
        <tr>
            <th>Benefit</th>
            <th>A</th>
            <th>B</th>
            <th>D</th>
            <th>G</th>
            <th>K</th>
            <th>L</th>
            <th>M</th>
            <th>N</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Part A coinsurance + 365 extra hospital days</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
        <tr><td>Part B coinsurance or copay</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>50%</td><td>75%</td><td>&#10003;</td><td>&#10003;*</td></tr>
        <tr><td>Part A hospice coinsurance or copay</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>50%</td><td>75%</td><td>&#10003;</td><td>&#10003;</td></tr>
        <tr><td>Skilled nursing facility coinsurance</td><td>&mdash;</td><td>&mdash;</td><td>&#10003;</td><td>&#10003;</td><td>50%</td><td>75%</td><td>&#10003;</td><td>&#10003;</td></tr>
        <tr><td>Part A deductible</td><td>&mdash;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>50%</td><td>75%</td><td>50%</td><td>&#10003;</td></tr>
        <tr><td>Part B deductible</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
        <tr><td>Part B excess charges</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&#10003;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
        <tr><td>Foreign travel emergency</td><td>&mdash;</td><td>&mdash;</td><td>&#10003;</td><td>&#10003;</td><td>&mdash;</td><td>&mdash;</td><td>&#10003;</td><td>&#10003;</td></tr>
    </tbody>
</table>

<p><em>* Plan N covers Part B coinsurance, but you pay up to $20 per office visit and up to $50 per ER visit (waived if admitted).</em></p>

<p>Plans C and F are no longer available to Medicare beneficiaries who became eligible on or after January 1, 2020. If you are already enrolled in Plan C or F, you may keep it.</p>

<div class="key-takeaway">
    <strong>For most new Medicare enrollees, Plan G offers the most comprehensive coverage available.</strong> It covers every Medicare gap except the $257 Part B deductible, which amounts to less than $22 per month in additional exposure&mdash;far less than the premium difference between Plan G and Plan F when F is available through the individual market.
</div>

<h2 id="plan-g-plan-n">3. Plan G vs. Plan N: the most popular options</h2>

<p>Plan G and Plan N together account for the majority of new Medigap enrollments in 2026. Here is a detailed comparison:</p>

<table>
    <thead>
        <tr>
            <th></th>
            <th>Plan G</th>
            <th>Plan N</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Part A deductible ($1,676)</td><td>Covered</td><td>Covered</td></tr>
        <tr><td>Part B coinsurance</td><td>Fully covered</td><td>Copay up to $20/office visit, $50/ER</td></tr>
        <tr><td>Part B excess charges</td><td>Covered</td><td>Not covered</td></tr>
        <tr><td>Skilled nursing coinsurance</td><td>Covered</td><td>Covered</td></tr>
        <tr><td>Foreign travel emergency</td><td>Covered</td><td>Covered</td></tr>
        <tr><td>Avg monthly premium (age 65)</td><td>$100&ndash;$400</td><td>$80&ndash;$300</td></tr>
        <tr><td>Best for</td><td>High utilizers; those wanting zero billing surprises</td><td>Lower utilizers; those whose doctors accept Medicare assignment</td></tr>
    </tbody>
</table>

<p><strong>The break-even math:</strong> If Plan G costs $50/month more than Plan N in your area, that is $600/year in additional premium. You would need to have more than 30 office visits per year (at the $20 Plan N copay) or face Part B excess charges exceeding $600 for Plan G to deliver more value. For most beneficiaries, especially those who see specialists who sometimes charge excess fees, Plan G provides cleaner cost predictability.</p>

<h2 id="premiums">4. 2026 Medigap premium ranges by plan</h2>

<p>Medigap premiums vary significantly by age, gender, location, tobacco use, and insurer. The ranges below reflect typical premiums for a 65-year-old non-smoking woman in a mid-cost metropolitan area in 2026:</p>

<table>
    <thead>
        <tr>
            <th>Plan</th>
            <th>Monthly Premium Range (age 65)</th>
            <th>Annual Cost Range</th>
            <th>Relative Coverage Level</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Plan A</td><td>$70&ndash;$200</td><td>$840&ndash;$2,400</td><td>Basic</td></tr>
        <tr><td>Plan B</td><td>$90&ndash;$250</td><td>$1,080&ndash;$3,000</td><td>Moderate</td></tr>
        <tr><td>Plan D</td><td>$95&ndash;$260</td><td>$1,140&ndash;$3,120</td><td>Moderate</td></tr>
        <tr><td>Plan G</td><td>$100&ndash;$400</td><td>$1,200&ndash;$4,800</td><td>Comprehensive</td></tr>
        <tr><td>Plan G High-Deductible</td><td>$30&ndash;$80</td><td>$360&ndash;$960</td><td>Catastrophic protection only</td></tr>
        <tr><td>Plan K</td><td>$50&ndash;$140</td><td>$600&ndash;$1,680</td><td>Partial (50% of most benefits)</td></tr>
        <tr><td>Plan L</td><td>$65&ndash;$175</td><td>$780&ndash;$2,100</td><td>Partial (75% of most benefits)</td></tr>
        <tr><td>Plan M</td><td>$85&ndash;$230</td><td>$1,020&ndash;$2,760</td><td>Moderate</td></tr>
        <tr><td>Plan N</td><td>$80&ndash;$300</td><td>$960&ndash;$3,600</td><td>Near-comprehensive</td></tr>
    </tbody>
</table>

<p>Premiums increase with age. A 75-year-old typically pays 30 to 60% more than a 65-year-old for the same plan, depending on the insurer&rsquo;s age-rating methodology (attained-age vs. issue-age vs. community-rated). When comparing plans, ask each insurer how their premiums change as you age.</p>

<div class="guide-cta-inline">
    <p><strong>Already enrolled in Medicare and wondering if your bills are being processed correctly?</strong> <a href="/scan">Upload a Medicare Explanation of Benefits to BillKarma</a>&mdash;we verify that your Medigap plan was applied correctly and flag any charges where coordination of benefits was missed.</p>
</div>

<h2 id="medigap-vs-advantage">5. Medigap vs. Medicare Advantage comparison</h2>

<p>Medicare Advantage (Part C) and Medigap are fundamentally different approaches to supplementing Original Medicare. Neither is universally better; the right choice depends on your health needs, finances, and how you use healthcare.</p>

<table>
    <thead>
        <tr>
            <th>Factor</th>
            <th>Medigap + Original Medicare</th>
            <th>Medicare Advantage</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Monthly premium</td><td>Part B ($185) + Medigap ($100&ndash;$400)</td><td>$0&ndash;$100 (often $0 for basic plans)</td></tr>
        <tr><td>Annual out-of-pocket max</td><td>$257 (Part B deductible) + plan premium</td><td>Up to $9,350 in-network (2026 statutory max)</td></tr>
        <tr><td>Network restrictions</td><td>None &mdash; any Medicare-accepting provider</td><td>HMO: in-network only; PPO: in- and out-of-network</td></tr>
        <tr><td>Prior authorization</td><td>Required by Medicare (not by Medigap)</td><td>Required by the Advantage plan for most procedures</td></tr>
        <tr><td>Prescription drug coverage</td><td>Requires separate Part D plan</td><td>Usually included</td></tr>
        <tr><td>Extra benefits (dental, vision)</td><td>Not included</td><td>Often included</td></tr>
        <tr><td>Predictability of costs</td><td>High &mdash; Plan G leaves only $257/year gap</td><td>Lower &mdash; OOP can reach $9,350+</td></tr>
        <tr><td>Best for</td><td>High utilizers; those wanting provider freedom</td><td>Healthy, lower utilizers; those wanting low premium</td></tr>
    </tbody>
</table>

<p>The core trade-off: Medicare Advantage typically has lower monthly premiums but exposes you to higher out-of-pocket costs when you need significant care. Medigap has higher monthly premiums but near-zero out-of-pocket costs for covered services. For someone with one or more chronic conditions who sees multiple specialists, Medigap&rsquo;s predictability often makes it more economical despite the higher premium.</p>

<h2 id="when-to-buy">6. When to buy: open enrollment rules</h2>

<p>Timing your Medigap enrollment correctly is one of the most important Medicare decisions you will make. Missing your Open Enrollment Period can cost thousands of dollars per year in higher premiums or result in outright coverage denial.</p>

<ul>
    <li><strong>Open Enrollment Period (OEP):</strong> Begins the month you turn 65 and are enrolled in Medicare Part B. Lasts 6 months. During this window, you have guaranteed issue rights: no insurer can deny coverage or charge you more based on health history.</li>
    <li><strong>After OEP in most states:</strong> Insurers can use medical underwriting. Common conditions that trigger higher premiums or denial include diabetes, heart disease, COPD, stroke history, cancer, and obesity. In states without guaranteed issue protections, missing your OEP is a significant risk.</li>
    <li><strong>Guaranteed issue rights outside OEP:</strong> You have guaranteed issue rights if: your Medicare Advantage plan is leaving your area, you move out of the plan&rsquo;s service area, your employer coverage ends, or you are within 12 months of your first Medicare Advantage enrollment and want to return to Original Medicare.</li>
    <li><strong>State protections:</strong> Several states&mdash;including California, Connecticut, Maine, Massachusetts, New York, Oregon, and Washington&mdash;require guaranteed issue or annual enrollment periods that give more flexibility than federal rules. If you live in one of these states, your switching options are broader.</li>
</ul>

<div class="key-takeaway">
    <strong>Enroll in Medigap during your Open Enrollment Period even if you feel healthy.</strong> The inability to be denied coverage during OEP is a one-time right you cannot recover. Many people who delay Medigap enrollment because they &ldquo;feel fine&rdquo; are later denied or priced out after a health event. Lock in guaranteed issue coverage at 65.
</div>

<h2 id="billing-interactions">7. How Medigap interacts with your medical bills</h2>

<p>When you use medical services as a Medigap enrollee, the claims process works automatically:</p>

<ol>
    <li><strong>You receive care</strong> from any Medicare-accepting provider. You do not need referrals, and there are no network restrictions under Original Medicare.</li>
    <li><strong>Your provider submits the claim</strong> directly to Medicare. Medicare processes the claim and pays its share (typically 80% of the Medicare-approved amount).</li>
    <li><strong>Medicare automatically crossovers the claim</strong> to your Medigap insurer for the remaining cost-sharing. You do not need to file a separate claim for Medigap in most cases.</li>
    <li><strong>Your Medigap insurer pays</strong> the secondary portion according to your plan. For Plan G, that is the 20% coinsurance and the Part A deductible if applicable. You receive an Explanation of Benefits from each insurer.</li>
    <li><strong>Your net cost</strong> on most services is $0 (after you have paid your $257 annual Part B deductible). For hospital stays with a Part A deductible, Plan G covers that deductible in full.</li>
</ol>

<p><strong>When Medigap claims are denied:</strong> Medigap denial is rare, but it can occur if: (1) Medicare denies the underlying claim (Medigap cannot pay what Medicare refuses to cover), (2) the service is not covered by Medicare at all, or (3) there is a coordination of benefits error. If your Medigap claim is denied, request the denial in writing, confirm that Medicare did pay its share, and appeal using the insurer&rsquo;s grievance process.</p>

<h2 id="case-study">8. Real-world case study</h2>

<div class="case-study">
    <h3>Hip replacement &mdash; Plan G keeps out-of-pocket to $257 on a $42,000 procedure</h3>
    <p>A 71-year-old retired nurse in Ohio enrolled in Medigap Plan G when she turned 65. In January 2026, she needed a total hip replacement. The hospital&rsquo;s charged amount: <strong>$42,000</strong>. Medicare&rsquo;s approved amount: <strong>$18,400</strong>.</p>
    <p>Medicare paid 80% of the approved amount: <strong>$14,720</strong>. The remaining 20% coinsurance was <strong>$3,680</strong>. The hospital also billed the Part A inpatient deductible of <strong>$1,676</strong>. Total Medicare beneficiary liability before Medigap: <strong>$5,356</strong>.</p>
    <p>Her Plan G paid the $3,680 coinsurance and the $1,676 Part A deductible in full. Her actual out-of-pocket cost for the entire hospitalization: <strong>$257</strong>&mdash;the annual Part B deductible she had already paid earlier in the year. She paid nothing additional.</p>
    <p>Her Plan G premium was $185/month ($2,220/year). Against a single hospitalization saving her $5,356 in cost-sharing, Plan G returned more than two years of premiums in a single claim. She had also paid zero coinsurance on specialist visits and imaging throughout the year. <strong>Annual estimated out-of-pocket savings vs. Original Medicare alone: approximately $4,800.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is a Medigap plan and how does it work?</h3>
        <p>A Medigap plan (also called a Medicare Supplement plan) is private health insurance that fills the cost gaps left by Original Medicare Parts A and B. Original Medicare typically pays 80% of approved costs after the Part B deductible; Medigap pays some or all of the remaining 20%, plus the Part A hospital deductible, skilled nursing coinsurance, and other gaps. Plans are standardized by federal law, meaning a Plan G from one insurer covers the exact same benefits as a Plan G from any other insurer&mdash;only the premium differs.</p>
    </div>
    <div class="faq-item">
        <h3>What does Medigap Plan G cover in 2026?</h3>
        <p>Plan G covers: the Part A hospital deductible ($1,676 per benefit period), all Part A and Part B coinsurance, skilled nursing facility coinsurance, Part B excess charges, and foreign travel emergency care (80% up to $50,000 lifetime). The only gap Plan G does not cover is the Part B deductible ($257 in 2026). It is the most comprehensive plan available to new Medicare enrollees since Plan F was closed to new enrollees in 2020.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between Medigap Plan G and Plan N?</h3>
        <p>Both plans cover the Part A deductible and all standard coinsurance. Plan G covers Part B coinsurance fully and covers Part B excess charges; Plan N requires copays up to $20 per office visit and $50 per ER visit, and does not cover excess charges. Plan N premiums run $40 to $100/month lower than Plan G on average. Plan N makes sense if your doctors always accept Medicare assignment and you have relatively few office visits per year.</p>
    </div>
    <div class="faq-item">
        <h3>When is the best time to buy a Medigap plan?</h3>
        <p>During your Medigap Open Enrollment Period&mdash;the six-month window starting the month you turn 65 and enroll in Part B. During this window, insurers cannot deny coverage or charge more based on your health history. Missing this window means losing guaranteed issue rights in most states, potentially making you uninsurable or subject to significantly higher premiums if you have any health conditions.</p>
    </div>
    <div class="faq-item">
        <h3>Can I switch from Medicare Advantage to Medigap?</h3>
        <p>Yes, but guaranteed issue rights apply only within the first 12 months of Medicare Advantage enrollment (the trial right period). Outside of that window, Medigap insurers can use medical underwriting to deny your application or charge higher premiums in most states. Several states, including New York and California, have more consumer-friendly rules that allow switching more easily. Check with your state insurance commissioner for state-specific guaranteed issue rules.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.medicare.gov/supplements-other-insurance/whats-medicare-supplement-insurance-medigap" target="_blank" rel="noopener">Medicare.gov: What&rsquo;s Medicare Supplement Insurance (Medigap)?</a></li>
    <li><a href="https://www.cms.gov/medicare/health-plans/medigap" target="_blank" rel="noopener">CMS: Medigap (Medicare Supplement Insurance) Regulations</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/medigap-enrollment-and-consumer-protections-vary-across-states/" target="_blank" rel="noopener">KFF: Medigap Enrollment and Consumer Protections by State</a></li>
    <li><a href="https://www.medicare.gov/publications/02110-choosing-a-medigap-policy.pdf" target="_blank" rel="noopener">CMS: Choosing a Medigap Policy &mdash; A Guide to Health Insurance for People with Medicare (2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/medicare-beneficiary-resources/medicare-costs" target="_blank" rel="noopener">CMS: Medicare Costs 2026 &mdash; Premiums, Deductibles, and Coinsurance</a></li>
    <li><a href="https://www.ahip.org/resources/insurance-research" target="_blank" rel="noopener">AHIP: Health Insurance Research and Medigap Enrollment Data</a></li>
    <li><a href="https://www.naic.org/consumer_medigap.htm" target="_blank" rel="noopener">NAIC: Medigap Consumer Resources and State Comparison</a></li>
</ul>
""",
})
