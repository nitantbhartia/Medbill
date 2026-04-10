"""Guide: Dual Eligible Medicare and Medicaid Billing"""

from guides import register, _embed

register("dual-eligible-medicare-medicaid-billing", {
    "title": "Dual Eligible Billing: Medicare + Medicaid and Why You Should Never Owe Anything",
    "meta_description": "Dual eligible patients (Medicare + Medicaid) cannot be billed. Learn how Medicare pays first, Medicaid pays second, QMB/SLMB programs, D-SNPs, and what to do when billed incorrectly.",
    "published": "2026-04-10",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Who are dual eligible beneficiaries?",
            "a": "Dual eligible beneficiaries are individuals who qualify for both Medicare and Medicaid. There are approximately 12 million dual eligibles in the United States. They are typically low-income seniors or people with disabilities. Dual eligible patients receive the strongest billing protections of any patient population&mdash;providers cannot bill them for Medicare cost-sharing if they are in a qualifying category.",
        },
        {
            "q": "Can providers bill dual eligible patients?",
            "a": "In most cases, no. Providers who accept both Medicare and Medicaid cannot bill dual eligible patients for Medicare cost-sharing (deductibles, copays, and coinsurance) when Medicaid or a Medicare Savings Program covers those amounts. Billing a dual eligible patient for amounts that Medicaid is responsible for is a federal violation and can result in provider sanctions.",
        },
        {
            "q": "What is the QMB program?",
            "a": "The Qualified Medicare Beneficiary (QMB) program is a Medicare Savings Program that pays Medicare Part A and Part B premiums, deductibles, and coinsurance for qualifying low-income Medicare beneficiaries. QMB beneficiaries have the strongest billing protection: providers who accept Medicare cannot bill QMB patients for any Medicare cost-sharing, even if the provider does not accept Medicaid.",
        },
        {
            "q": "What is a D-SNP?",
            "a": "A Dual Eligible Special Needs Plan (D-SNP) is a Medicare Advantage plan specifically designed for people eligible for both Medicare and Medicaid. D-SNPs coordinate coverage between Medicare and Medicaid, often offering additional benefits like transportation, meal delivery, dental, and vision. Enrollment in a D-SNP is voluntary and separate from your Medicaid coverage.",
        },
        {
            "q": "What should I do if I am dual eligible and receive a bill?",
            "a": "Do not pay it. Show the provider your Medicaid ID card and Medicare card. Ask the provider to bill Medicaid as secondary payer after Medicare. If the provider insists on collecting, contact your state Medicaid agency and the CMS Regional Office. Keep the bill as documentation&mdash;it may constitute a billing violation.",
        },
    ],
    "body": f"""<article>
<div class="answer-box"><strong>Quick Answer:</strong> If you have both Medicare and Medicaid, Medicare pays first and Medicaid pays second as the "payer of last resort." Providers cannot bill you for the gap. QMB and other Medicare Savings Programs cover Medicare premiums and cost-sharing for low-income beneficiaries. Being billed as a dual eligible is a billing error&mdash;don't pay it, and report it.</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#who-is-dual-eligible">Who Is Dual Eligible?</a></li>
        <li><a href="#coordination">Medicare First, Medicaid Second</a></li>
        <li><a href="#billing-protection">Billing Protections: Why You Shouldn't Owe Anything</a></li>
        <li><a href="#msp-programs">Medicare Savings Programs (QMB, SLMB, QI)</a></li>
        <li><a href="#dsnp">D-SNP Plans</a></li>
        <li><a href="#common-errors">Common Billing Errors for Dual Eligibles</a></li>
        <li><a href="#what-to-do">What to Do When Billed Incorrectly</a></li>
        <li><a href="#state-programs">State Medicare Savings Programs</a></li>
    </ol>
</nav>

<h2 id="who-is-dual-eligible">Who Is Dual Eligible?</h2>

<p>Dual eligible beneficiaries hold both Medicare and Medicaid coverage simultaneously. There are approximately <strong>12 million dual eligibles</strong> in the United States, representing about 15% of all Medicare beneficiaries and 15% of all Medicaid enrollees.</p>

<p>Dual eligible status typically arises when a Medicare beneficiary has income and assets low enough to also qualify for Medicaid. Common pathways:</p>
<ul>
    <li>Older adults who spent down their savings and qualify for both age-based Medicare and income-based Medicaid</li>
    <li>People with disabilities who receive Medicare (after a 24-month Social Security Disability waiting period) and also qualify for Medicaid based on low income</li>
    <li>Low-income seniors (65+) who qualify for Medicare by age and Medicaid based on income/assets</li>
</ul>

<p>There are different subcategories of dual eligibility, which determine the scope of billing protections:</p>
<table>
    <thead>
        <tr><th>Category</th><th>Description</th><th>What Medicaid Covers</th></tr>
    </thead>
    <tbody>
        <tr><td>Full Dual Eligible</td><td>Eligible for full Medicaid benefits plus Medicare</td><td>Medicare cost-sharing plus Medicaid services</td></tr>
        <tr><td>Partial Dual Eligible (QMB)</td><td>Income too high for full Medicaid; qualifies for QMB</td><td>Medicare premiums, deductibles, and coinsurance</td></tr>
        <tr><td>Partial Dual Eligible (SLMB)</td><td>Slightly higher income; qualifies for SLMB</td><td>Medicare Part B premium only</td></tr>
        <tr><td>Partial Dual Eligible (QI)</td><td>Higher income; qualifies for QI program</td><td>Portion of Part B premium</td></tr>
    </tbody>
</table>

<h2 id="coordination">Medicare First, Medicaid Second</h2>

<p>When a dual eligible patient receives a covered service, the payment sequence is federally mandated:</p>

<ol>
    <li><strong>Medicare pays first</strong> (as the primary payer) for Medicare-covered services</li>
    <li><strong>Medicaid pays second</strong> (as the secondary payer) for any remaining cost-sharing that Medicare left behind&mdash;the deductible, copay, or coinsurance</li>
    <li><strong>The patient pays nothing</strong> (or pays only a nominal Medicaid copay in some situations)</li>
</ol>

<p>Medicaid is legally the "payer of last resort." Federal law prohibits Medicaid from paying claims before Medicare for Medicare-covered services. Providers must bill Medicare first, receive Medicare's payment, and then submit the remaining balance to Medicaid for secondary payment.</p>

<p>The provider's obligation: if a provider accepts Medicare assignment, they agree to accept Medicare's approved amount. They then must bill Medicaid for the cost-sharing portion. They cannot collect that cost-sharing from the patient.</p>

<h2 id="billing-protection">Billing Protections: Why You Shouldn't Owe Anything</h2>

<p>Dual eligible beneficiaries&mdash;particularly full duals and QMB enrollees&mdash;have the strongest patient billing protections under federal law:</p>

<ul>
    <li><strong>Prohibition on billing Medicare cost-sharing to QMB patients:</strong> Under 42 U.S.C. &sect;1396a(n), providers who accept Medicare cannot bill QMB beneficiaries for Medicare deductibles, copays, or coinsurance&mdash;even if the provider does not participate in Medicaid. This rule applies universally to QMB patients.</li>
    <li><strong>Medicaid acceptance by Medicare providers:</strong> In many states, providers enrolled in Medicare who also treat Medicaid-eligible patients must enroll in Medicaid or risk losing Medicare provider status.</li>
    <li><strong>No balance billing:</strong> Like all Medicaid beneficiaries, full dual eligibles are protected from balance billing.</li>
</ul>

<div class="key-takeaway">
    <strong>The QMB rule is frequently violated.</strong> CMS estimates that QMB beneficiaries are billed for Medicare cost-sharing millions of times per year, in violation of federal law. If you are a QMB patient and receive a bill for Medicare cost-sharing, you do not owe it. Show the provider your QMB card and cite 42 U.S.C. &sect;1396a(n). If they persist, report them.
</div>

<h2 id="msp-programs">Medicare Savings Programs (QMB, SLMB, QI)</h2>

<p>Medicare Savings Programs (MSPs) are state programs funded jointly by federal and state governments that help low-income Medicare beneficiaries pay their Medicare costs. They are distinct from full Medicaid but offer important billing protections:</p>

<h3>Qualified Medicare Beneficiary (QMB)</h3>
<ul>
    <li><strong>Covers:</strong> Medicare Part A and Part B premiums, deductibles, copays, and coinsurance</li>
    <li><strong>2026 income limits:</strong> Approximately $1,275/month (individual), $1,724/month (couple)</li>
    <li><strong>Billing protection:</strong> Providers cannot bill QMB patients for any Medicare cost-sharing</li>
    <li><strong>Automatic Extra Help:</strong> QMB enrollment automatically qualifies you for Part D Extra Help</li>
</ul>

<h3>Specified Low-Income Medicare Beneficiary (SLMB)</h3>
<ul>
    <li><strong>Covers:</strong> Medicare Part B premium ($185/month in 2026)</li>
    <li><strong>2026 income limits:</strong> Approximately $1,526/month (individual), $2,063/month (couple)</li>
    <li><strong>Annual savings:</strong> $2,220/year in Part B premiums</li>
    <li><strong>Automatic Extra Help:</strong> SLMB enrollment qualifies you for Part D Extra Help</li>
</ul>

<h3>Qualifying Individual (QI)</h3>
<ul>
    <li><strong>Covers:</strong> A portion of the Medicare Part B premium</li>
    <li><strong>2026 income limits:</strong> Approximately $1,715/month (individual), $2,319/month (couple)</li>
    <li><strong>Note:</strong> Funding is limited and enrollment is first-come, first-served. Apply early each year.</li>
</ul>

<p>To apply for any MSP, contact your state Medicaid agency. Applications can often be submitted at Social Security offices as well.</p>

{_embed("cost", title="Estimate Dual Eligible Savings", subtitle="See how Medicare Savings Programs could reduce your costs.")}

<h2 id="dsnp">D-SNP Plans for Dual Eligibles</h2>

<p>Dual Eligible Special Needs Plans (D-SNPs) are Medicare Advantage plans specifically designed for people who have both Medicare and Medicaid. D-SNPs are operated by private insurers and must:</p>
<ul>
    <li>Limit enrollment to dual eligible beneficiaries</li>
    <li>Coordinate Medicare and Medicaid benefits</li>
    <li>Have contracts with state Medicaid agencies</li>
    <li>Provide care coordination and case management</li>
</ul>

<p>D-SNPs often offer additional benefits beyond Original Medicare or Medicaid, including:</p>
<ul>
    <li>Dental, vision, and hearing coverage</li>
    <li>Transportation to medical appointments</li>
    <li>Meal delivery after hospitalizations</li>
    <li>Over-the-counter drug allowances</li>
    <li>Fitness program memberships</li>
</ul>

<p>Enrollment in a D-SNP is voluntary. You retain your Medicaid coverage regardless of whether you enroll in a D-SNP. Compare D-SNP options against Original Medicare plus Medigap using Medicare's Plan Finder tool.</p>

<h2 id="common-errors">Common Billing Errors for Dual Eligibles</h2>

<p>Dual eligible patients are frequently billed incorrectly. The most common errors:</p>

<ol>
    <li><strong>Billing for Medicare cost-sharing without billing Medicaid first:</strong> The provider bills you the deductible or coinsurance without submitting a claim to Medicaid as secondary payer. The correct process is Medicare first, then Medicaid, then you owe nothing (or nominal copay).</li>
    <li><strong>Failure to recognize QMB status:</strong> Provider staff don't check QMB enrollment and bill the standard Medicare cost-sharing. Show your Medicaid/QMB card at every visit.</li>
    <li><strong>Part D billing errors:</strong> Pharmacy charges you full drug costs without applying your Extra Help (LIS) status. Show your Extra Help card at the pharmacy and ask them to run your Medicare Part D claim with LIS applied.</li>
    <li><strong>SNF billing after observation status:</strong> As a dual eligible, Medicaid may cover some SNF costs that Medicare won't, but the process requires specific documentation and provider enrollment. Providers sometimes incorrectly calculate patient liability.</li>
    <li><strong>Private pay attempts:</strong> Provider attempts to bill you as a private-pay patient, bypassing Medicare and Medicaid entirely. This is illegal for enrolled providers treating dual eligible patients for covered services.</li>
</ol>

<h2 id="what-to-do">What to Do When Billed Incorrectly</h2>

<p>If you are a dual eligible patient and receive a bill you shouldn't owe:</p>

<ol>
    <li><strong>Don't pay it.</strong> Paying it may be interpreted as accepting responsibility and complicates the correction process.</li>
    <li><strong>Contact the provider's billing department.</strong> Provide your Medicare number and Medicaid/QMB ID number. Ask them to bill Medicaid as secondary payer (or confirm QMB status) and reprocess the claim.</li>
    <li><strong>Contact your state Medicaid agency.</strong> Explain that you are dual eligible (or QMB) and the provider is billing you for Medicare cost-sharing. Your state can contact the provider directly.</li>
    <li><strong>Call 1-800-MEDICARE.</strong> Report the billing violation. CMS can initiate a review of the provider's billing practices for dual eligible patients.</li>
    <li><strong>File a complaint with CMS.</strong> For systemic billing problems with a specific provider, file a formal complaint at cms.gov or through the CMS Regional Office.</li>
    <li><strong>Contact a Medicare/Medicaid counselor.</strong> Your State Health Insurance Assistance Program (SHIP) provides free counseling on dual eligible billing issues.</li>
</ol>

<h2 id="state-programs">State Medicare Savings Programs</h2>

<p>In addition to the federal QMB/SLMB/QI programs, many states offer additional Medicare cost assistance programs for low-income beneficiaries. Some states have higher income limits than the federal MSP thresholds. Contact your state Medicaid agency to ask about all available programs in your state.</p>

<p>To find free help applying for Medicare Savings Programs:</p>
<ul>
    <li><strong>SHIP (State Health Insurance Assistance Program):</strong> Free counseling at shiphelp.org or 1-877-839-2675</li>
    <li><strong>Benefits.gov:</strong> Federal benefits finder to identify all programs you may qualify for</li>
    <li><strong>Medicare.gov:</strong> Plan Finder and eligibility tools at medicare.gov/get-help</li>
    <li><strong>BenefitsCheckUp:</strong> ncoa.org/benefits-checkup for seniors</li>
</ul>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare-medicaid-coordination/medicare-and-medicaid-coordination/medicare-medicaid-coordination-office" target="_blank" rel="noopener">CMS &mdash; Medicare-Medicaid Coordination Office</a></li>
    <li><a href="https://www.medicare.gov/basics/costs/help/medicare-savings-programs" target="_blank" rel="noopener">Medicare.gov &mdash; Medicare Savings Programs</a></li>
    <li><a href="https://www.medicaid.gov/medicaid/dual-eligibles/index.html" target="_blank" rel="noopener">Medicaid.gov &mdash; Dual Eligible Individuals</a></li>
    <li><a href="https://www.kff.org/medicaid/issue-brief/10-things-to-know-about-medicare-and-medicaid/" target="_blank" rel="noopener">KFF &mdash; Medicare and Medicaid: Dual Eligibility</a></li>
    <li><a href="https://shiphelp.org" target="_blank" rel="noopener">SHIP &mdash; Free Medicare Counseling</a></li>
</ul>
</article>""",
})
