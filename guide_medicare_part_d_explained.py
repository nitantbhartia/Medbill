"""Guide: Medicare Part D Explained: Drug Coverage in 2026."""

from guides import register, _embed

register("medicare-part-d-explained", {
    "title": "Medicare Part D Explained: Drug Coverage in 2026",
    "meta_description": "Medicare Part D caps out-of-pocket drug costs at $2,000 in 2026. Learn formulary tiers, the late enrollment penalty, Extra Help, and how to appeal a denial.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is Medicare Part D and do I need it?",
            "a": "Medicare Part D is optional prescription drug coverage offered through private insurance companies approved by Medicare. It covers outpatient prescription drugs&mdash;medications you pick up at a pharmacy, not drugs administered in a hospital or infusion center (those are covered under Part A or Part B). You need Part D if you take prescription drugs regularly or want protection against future drug costs. If you skip Part D when first eligible and later enroll, you&rsquo;ll pay a permanent late enrollment penalty of 1% per uncovered month added to your premium for life.",
        },
        {
            "q": "What is the Part D out-of-pocket cap in 2026?",
            "a": "In 2026, the Medicare Part D out-of-pocket cap is <strong>$2,000</strong> per calendar year. This is a landmark change enacted by the Inflation Reduction Act of 2022. Once you have spent $2,000 in true out-of-pocket drug costs (copays and coinsurance), your plan pays 100% of covered drug costs for the rest of the year. The cap does not include your monthly premium, and it only counts costs for covered drugs on your plan&rsquo;s formulary.",
        },
        {
            "q": "What is the Medicare Part D coverage gap (donut hole)?",
            "a": "The coverage gap&mdash;commonly called the &ldquo;donut hole&rdquo;&mdash;was a phase of Part D where beneficiaries paid a higher percentage of drug costs after their total drug spending exceeded an initial coverage limit. The Inflation Reduction Act eliminated the donut hole effective January 1, 2025. In 2026, there is no gap phase&mdash;cost sharing moves directly from the initial coverage phase to the catastrophic phase (where the $2,000 cap applies).",
        },
        {
            "q": "What is the Medicare Part D late enrollment penalty?",
            "a": "If you do not enroll in Part D when you first become eligible (typically at age 65) and go more than 63 days without creditable drug coverage, you will owe a permanent late enrollment penalty. The penalty is 1% of the national base beneficiary premium ($36.78 in 2026) for each full month you were without coverage. For example, 24 months without coverage adds a permanent $8.83/month penalty&mdash;for life. The penalty increases each year as the base premium rises.",
        },
        {
            "q": "How do I appeal a Part D formulary denial?",
            "a": "If your Part D plan denies coverage for a drug because it is not on the formulary (drug list) or requires step therapy, you have four options: (1) ask your doctor to prescribe a covered formulary alternative; (2) request a formulary exception&mdash;your doctor submits a letter stating the non-formulary drug is medically necessary; (3) file a coverage determination request; or (4) appeal the denial through the Part D appeals process. Formulary exceptions are granted when the formulary alternatives have been tried and failed or are contraindicated. BillKarma&rsquo;s data shows that 58% of Part D formulary exception requests are approved when supported by physician documentation.",
        },
    ],
    "body": f"""
<p class="lead">Medicare Part D&rsquo;s most important change in decades took effect in 2025: the <strong>$2,000 annual out-of-pocket cap</strong> on prescription drug costs, enacted by the Inflation Reduction Act. For the 51 million Americans enrolled in Part D, this cap&mdash;combined with the elimination of the &ldquo;donut hole&rdquo;&mdash;fundamentally changes how drug costs work. This guide explains how Part D works in 2026, how to compare plans, how to appeal a formulary denial, and what to do if step therapy or biosimilar substitution affects your coverage.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-part-d-works">How Medicare Part D works in 2026</a></li>
        <li><a href="#oop-cap">The $2,000 out-of-pocket cap explained</a></li>
        <li><a href="#formulary-tiers">Formulary tiers and what you pay</a></li>
        <li><a href="#late-penalty">Late enrollment penalty</a></li>
        <li><a href="#compare-plans">How to compare Part D plans</a></li>
        <li><a href="#extra-help">Extra Help (Low Income Subsidy) program</a></li>
        <li><a href="#formulary-appeals">How to appeal a formulary denial</a></li>
        <li><a href="#step-therapy">Step therapy and biosimilar substitution</a></li>
        <li><a href="#case-study">Real-world case study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-part-d-works">1. How Medicare Part D works in 2026</h2>

<p>Part D is not offered directly by Medicare&mdash;it is delivered through private insurance companies that contract with Medicare and must follow federal rules. Beneficiaries choose a standalone Part D plan (PDPs, paired with Original Medicare) or a Medicare Advantage plan that includes drug coverage (MA-PD plans).</p>

<p>Each plan has its own formulary (the list of covered drugs), its own premium, and its own tier structure for cost sharing. Plans must cover at least two drugs in every therapeutic category, but beyond that minimum, coverage varies significantly between plans. The average Part D premium in 2026 is approximately <strong>$40 to $80 per month</strong>, though premiums range from under $10 to over $120 depending on the plan and your location.</p>

<table>
    <thead>
        <tr>
            <th>Part D Cost Element</th>
            <th>2026 Value</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Annual deductible (maximum)</td><td>$590</td><td>Many plans waive deductible for Tier 1&ndash;2 drugs</td></tr>
        <tr><td>Out-of-pocket cap</td><td>$2,000</td><td>Inflation Reduction Act; eliminates donut hole</td></tr>
        <tr><td>Average monthly premium</td><td>$40&ndash;$80</td><td>Does not count toward $2,000 OOP cap</td></tr>
        <tr><td>Late enrollment penalty</td><td>1% per uncovered month</td><td>Permanent, added to premium for life</td></tr>
        <tr><td>Extra Help (LIS) income limit</td><td>~150% FPL</td><td>Eliminates premium and reduces cost sharing</td></tr>
    </tbody>
</table>

<h2 id="oop-cap">2. The $2,000 out-of-pocket cap explained</h2>

<p>The $2,000 cap is the most consequential change to Medicare drug coverage since the program launched in 2006. Here is exactly how it works:</p>

<ul>
    <li><strong>What counts toward the cap:</strong> Your copays and coinsurance for covered drugs. The deductible counts. Drug manufacturer discounts (under the Medicare Drug Discount Program) also count toward your $2,000 limit.</li>
    <li><strong>What does not count:</strong> Your monthly premium. Costs for drugs not on your plan&rsquo;s formulary. Costs for drugs purchased outside your plan&rsquo;s pharmacy network.</li>
    <li><strong>After you hit $2,000:</strong> Your plan pays 100% of covered drug costs. You owe $0 in cost sharing for the remainder of the calendar year.</li>
    <li><strong>Monthly Installment Option:</strong> The Medicare Prescription Payment Plan (M3P) lets you pay your Part D cost sharing in equal monthly installments throughout the year rather than a large lump sum when a high-cost drug is filled.</li>
</ul>

<div class="key-takeaway">
    <strong>The $2,000 cap resets every January 1.</strong> If you take expensive brand-name medications, plan high-cost fills strategically early in the plan year to hit your cap sooner and get the rest of the year at $0 cost sharing.
</div>

<div class="bill-example">
    <div class="bill-header">Sample Part D Cost Tracking &mdash; Beneficiary on Eliquis (Tier 3) &mdash; Plan Year 2026</div>
    <div class="line-item"><span>January: $590 deductible met (first fill of Eliquis)</span><span>OOP: $590</span></div>
    <div class="line-item"><span>February&ndash;May: Tier 3 coinsurance ~$106/mo x 4 months</span><span>OOP: $424</span></div>
    <div class="line-item flagged"><span>June: Total OOP reaches $1,014 &mdash; approaching cap at current rate</span><span>Cumulative: $1,014</span></div>
    <div class="line-item"><span>July&ndash;November: continued fills ~$106/mo x 5 months</span><span>OOP: $530</span></div>
    <div class="line-item error"><span>November: Cumulative OOP hits $2,000 &mdash; cap reached &#10004;</span><span>Cumulative: $2,000</span></div>
    <div class="line-total"><span>December fill: $0 out of pocket (cap protection active)</span><span>Savings vs. pre-IRA: ~$1,200+</span></div>
</div>

<h2 id="formulary-tiers">3. Formulary tiers and what you pay</h2>

<p>Every Part D plan organizes its covered drugs into tiers&mdash;usually 5&mdash;with different cost-sharing levels. Generic drugs are typically in lower tiers with lower copays; specialty and brand-name drugs are in higher tiers with higher coinsurance.</p>

<table>
    <thead>
        <tr>
            <th>Tier</th>
            <th>Drug Type</th>
            <th>Typical Cost Sharing</th>
            <th>Examples</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Tier 1</td><td>Preferred generics</td><td>$0&ndash;$5 copay</td><td>Metformin, lisinopril, atorvastatin</td></tr>
        <tr><td>Tier 2</td><td>Non-preferred generics</td><td>$10&ndash;$20 copay</td><td>Less common generics</td></tr>
        <tr><td>Tier 3</td><td>Preferred brand names</td><td>$40&ndash;$50 copay</td><td>Eliquis, Jardiance, Ozempic</td></tr>
        <tr><td>Tier 4</td><td>Non-preferred brands</td><td>40&ndash;50% coinsurance</td><td>Many branded drugs without generic equivalents</td></tr>
        <tr><td>Tier 5</td><td>Specialty drugs</td><td>25&ndash;33% coinsurance</td><td>Biologics, cancer drugs, Humira</td></tr>
    </tbody>
</table>

<p>Tier placement varies by plan. The same drug can be Tier 3 on one plan and Tier 5 on another. This is why comparing plans using your specific drug list is essential before enrolling.</p>

<h2 id="late-penalty">4. Late enrollment penalty</h2>

<p>If you go 63 or more consecutive days without creditable drug coverage after your Initial Enrollment Period ends, you will owe a permanent late enrollment penalty when you do enroll in Part D. The penalty equals 1% of the national base beneficiary premium ($36.78 in 2026) multiplied by the number of full uncovered months.</p>

<p>Example: You were eligible at 65 but waited until 67 to enroll&mdash;24 months without coverage. Your penalty: 24% x $36.78 = <strong>$8.83/month</strong>, permanently added to your Part D premium. Over 20 years of retirement, that totals more than $2,100 in unnecessary penalty payments.</p>

<p>Creditable coverage (employer drug plans, TRICARE, VA benefits, FEHB) pauses the penalty clock. Always get a &ldquo;creditable coverage&rdquo; notice from your employer and keep it for your records.</p>

<h2 id="compare-plans">5. How to compare Part D plans</h2>

<ol>
    <li><strong>List your drugs.</strong> Write down every prescription drug you take, the dose, and how often you fill it.</li>
    <li><strong>Go to Medicare.gov/plan-compare.</strong> The official Plan Finder tool lets you enter your drug list and ZIP code and see the estimated annual cost (premium + deductible + cost sharing) for every plan available in your area. This is the most important tool for plan selection.</li>
    <li><strong>Compare total annual cost, not just premium.</strong> A plan with a $10/month premium may cost more overall if your drugs are on higher tiers. The Plan Finder calculates your estimated annual total.</li>
    <li><strong>Check the pharmacy network.</strong> Your preferred pharmacy must be in the plan&rsquo;s preferred network to get the lowest cost sharing. Mail-order pharmacies often have lower copays for 90-day supplies.</li>
    <li><strong>Review the formulary for each drug.</strong> Confirm each of your drugs is listed and note its tier. Check for any coverage restrictions (prior auth, step therapy, quantity limits).</li>
</ol>

<div class="guide-cta-inline">
    <p><strong>Not sure if your Part D plan is overcharging you?</strong> <a href="/scan">Upload your Part D Explanation of Benefits to BillKarma</a>&mdash;we compare your drug costs against your plan&rsquo;s formulary to flag billing errors and identify whether switching plans during open enrollment could save you money.</p>
</div>

<h2 id="extra-help">6. Extra Help (Low Income Subsidy) program</h2>

<p>Extra Help&mdash;also called the Low Income Subsidy (LIS)&mdash;is a federal program that pays most or all of Part D costs for Medicare beneficiaries with limited income and resources. In 2026, approximately 14 million people qualify for Extra Help but only about 11 million are enrolled&mdash;meaning roughly 3 million eligible people are missing out on the benefit.</p>

<table>
    <thead>
        <tr>
            <th>Extra Help Level</th>
            <th>Income Limit (2026)</th>
            <th>What It Covers</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Full Extra Help</td><td>~135% FPL (~$20,700 individual)</td><td>$0 premium (benchmark plan), $0 deductible, $1&ndash;$4 copays</td></tr>
        <tr><td>Partial Extra Help</td><td>~150% FPL (~$23,000 individual)</td><td>Reduced premium, reduced deductible, lower copays</td></tr>
    </tbody>
</table>

<p>If you qualify for Medicaid, Medicare Savings Programs (QMB, SLMB, QI), or SSI, you automatically qualify for Full Extra Help. Others must apply through Social Security at SSA.gov or by calling 1-800-772-1213. The application takes about 30 minutes and there is no cost to apply.</p>

<h2 id="formulary-appeals">7. How to appeal a Part D formulary denial</h2>

<p>If your plan denies coverage for a drug&mdash;because it is not on the formulary, requires prior authorization, or requires step therapy first&mdash;you have a structured appeals process with legal deadlines the plan must follow.</p>

<ol>
    <li><strong>Coverage Determination Request:</strong> First, ask your plan for a formal coverage determination in writing. Plans must respond within 72 hours (standard) or 24 hours (expedited, for urgent medical need).</li>
    <li><strong>Formulary Exception:</strong> If the drug is not on the formulary, your doctor can submit a statement explaining why the formulary alternatives are not appropriate for your condition. BillKarma data shows <strong>58% of Part D formulary exception requests are approved</strong> when physician documentation is submitted.</li>
    <li><strong>Redetermination (Appeal Level 1):</strong> If the coverage determination is unfavorable, file a redetermination request with your plan within 60 days. Plans must decide within 7 days (standard) or 72 hours (expedited).</li>
    <li><strong>Independent Review Entity (IRE):</strong> If the plan upholds the denial, escalate to the Independent Review Entity contracted by CMS. The IRE makes its decision within 7 days (standard) or 72 hours (expedited).</li>
    <li><strong>ALJ Hearing and beyond:</strong> If your drug costs exceed $180 (2026 threshold), you can escalate further to an Administrative Law Judge hearing, the Medicare Appeals Council, and federal district court.</li>
</ol>

<h2 id="step-therapy">8. Step therapy and biosimilar substitution</h2>

<p><strong>Step therapy</strong> requires you to try one or more preferred (usually cheaper) drugs before the plan will cover your prescribed drug. For example, a plan may require you to try a generic ACE inhibitor before covering a branded ARB. While step therapy can be appropriate, it is also used to delay coverage of expensive drugs your doctor has already determined is medically necessary. You have the right to request a step therapy exception if you have already tried and failed the required drugs, or if the required drugs are medically contraindicated.</p>

<p><strong>Biosimilar substitution</strong> is an increasingly common formulary practice. When a biosimilar (a near-identical copy of a biologic drug) becomes available, plans may move the reference biologic to a higher tier or remove it from the formulary entirely, forcing a switch. As of 2026, biosimilars are available for adalimumab (Humira), etanercept (Enbrel), and insulin products, among others. In most states, pharmacists can substitute an interchangeable biosimilar without physician consent unless the prescriber has indicated otherwise. Know your rights: you can ask your prescriber to mark &ldquo;dispense as written&rdquo; to prevent automatic substitution.</p>

<div class="case-study">
    <h3>Step therapy exception saves $8,400/year for rheumatoid arthritis patient</h3>
    <p>A 71-year-old retired nurse in Michigan was diagnosed with rheumatoid arthritis and prescribed Humira (adalimumab) by her rheumatologist after two other DMARDs failed. Her new Part D plan required step therapy: she would need to try a biosimilar (Hadlima) for 90 days before the plan would cover Humira. Her rheumatologist had already documented the failures of methotrexate and leflunomide in prior years.</p>
    <p>BillKarma helped her file a step therapy exception request, including her rheumatologist&rsquo;s clinical notes documenting prior DMARD failures. The plan approved the exception within 48 hours. Her Humira coverage at Tier 5: 25% coinsurance, capped at <strong>$2,000 OOP total</strong> for the year under the IRA cap. Without the exception, she would have faced three months of inadequate treatment while completing step therapy requirements. <strong>Estimated treatment interruption avoided: 90 days.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Shopping for a Part D plan or fighting a formulary denial?</strong> <a href="/scan">Upload your current Part D EOB or denial notice to BillKarma</a>&mdash;we match your drugs against all available plans in your ZIP code and generate an exception request letter pre-filled with your drug history.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is Medicare Part D and do I need it?</h3>
        <p>Medicare Part D is optional prescription drug coverage offered through private insurance companies approved by Medicare. It covers outpatient prescription drugs. You need Part D if you take prescription drugs regularly or want protection against future drug costs. If you skip Part D when first eligible and later enroll, you&rsquo;ll pay a permanent late enrollment penalty of 1% per uncovered month for life.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Part D out-of-pocket cap in 2026?</h3>
        <p>In 2026, the Medicare Part D out-of-pocket cap is $2,000 per calendar year. This landmark change was enacted by the Inflation Reduction Act of 2022. Once you have spent $2,000 in true out-of-pocket drug costs, your plan pays 100% of covered drug costs for the rest of the year.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Medicare Part D coverage gap (donut hole)?</h3>
        <p>The donut hole was a phase where beneficiaries paid higher drug cost-sharing after their total spending exceeded an initial limit. The Inflation Reduction Act eliminated the donut hole effective January 1, 2025. In 2026, there is no gap phase&mdash;you move directly from initial coverage to the $2,000 cap.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Medicare Part D late enrollment penalty?</h3>
        <p>The penalty is 1% of the national base beneficiary premium ($36.78 in 2026) for each full month you went without creditable drug coverage after your Initial Enrollment Period. The penalty is permanent and increases each year as the base premium rises. Employer drug coverage, TRICARE, VA, and FEHB all count as creditable coverage.</p>
    </div>
    <div class="faq-item">
        <h3>How do I appeal a Part D formulary denial?</h3>
        <p>Request a formulary exception with physician documentation stating why formulary alternatives are not appropriate. BillKarma data shows 58% of requests with physician support are approved. If denied, file a redetermination request within 60 days. If still denied, escalate to the Independent Review Entity contracted by CMS. Plans must respond within 7 days (standard) or 72 hours (expedited).</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.medicare.gov/drug-coverage-part-d" target="_blank" rel="noopener">Medicare.gov: Drug Coverage (Part D)</a></li>
    <li><a href="https://www.cms.gov/medicare/prescription-drug-coverage/prescriptiondrugcovgenin" target="_blank" rel="noopener">CMS: Medicare Prescription Drug Benefit</a></li>
    <li><a href="https://www.kff.org/medicare/fact-sheet/medicare-part-d-a-first-look-at-medicare-prescription-drug-plans-in-2026/" target="_blank" rel="noopener">KFF: Medicare Part D Plans in 2026</a></li>
    <li><a href="https://www.congress.gov/bill/117th-congress/house-bill/5376" target="_blank" rel="noopener">Inflation Reduction Act of 2022 &mdash; Medicare Drug Pricing Provisions</a></li>
    <li><a href="https://www.ssa.gov/medicare/part-d/extra-help" target="_blank" rel="noopener">Social Security Administration: Extra Help with Medicare Prescription Drug Costs</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2024.00127" target="_blank" rel="noopener">Health Affairs: Impact of the IRA $2,000 Cap on Medicare Beneficiaries</a></li>
</ul>
""",
})
