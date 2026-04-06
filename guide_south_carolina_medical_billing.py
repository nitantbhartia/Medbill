"""Guide: South Carolina Medical Billing Laws."""

from guides import register, _embed

register("south-carolina-medical-billing", {
    "title": "South Carolina Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "SC hospitals must provide charity care under SC Code § 44-7-3410. Learn surprise billing rights, the 3-year debt SOL, and how to cut your bill. Free analysis.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Are South Carolina hospitals required to offer charity care?",
            "a": "Yes. Under SC Code § 44-7-3410, every nonprofit hospital in South Carolina must maintain a written charity care policy and provide free or discounted care to qualifying low-income patients. The law requires hospitals to post charity care policies publicly and to screen all uninsured patients for eligibility. For-profit hospitals are not covered by this state mandate, but many voluntarily offer financial assistance. You can apply retroactively in most cases — ask the billing department for the financial assistance application immediately after receiving your first bill.",
        },
        {
            "q": "What is the statute of limitations on medical debt in South Carolina?",
            "a": "South Carolina has a 3-year statute of limitations on medical debt under SC Code § 15-3-530. The clock starts from the date of the last payment or the date the debt became due. Once the SOL expires, a collector cannot win a lawsuit against you — but making any payment or written acknowledgment of the debt can restart the clock. Always verify the SOL status before paying any old medical debt.",
        },
        {
            "q": "Does South Carolina protect patients from surprise medical bills?",
            "a": "South Carolina passed SB 1072 to address balance billing. For state-regulated health plans, the law limits patient cost-sharing for out-of-network emergency services to in-network levels. The federal No Surprises Act (effective January 1, 2022) provides broader protections for all plan types, including employer-sponsored self-funded plans. If you receive a surprise bill from an out-of-network provider at an in-network facility, you likely have the right to dispute it under the NSA.",
        },
        {
            "q": "What is the Medicaid income limit in South Carolina?",
            "a": "South Carolina expanded Medicaid under the ACA to 138% of the Federal Poverty Level — approximately $20,783 for a single person in 2026. If your income is at or below 138% FPL and you are a South Carolina resident, you likely qualify for Medicaid (SC Healthy Connections). Apply through scdhhs.gov. Medicaid eligibility is retroactive up to 3 months, which can cover recent medical bills.",
        },
        {
            "q": "Can a South Carolina hospital garnish my wages for medical debt?",
            "a": "Yes, but only after obtaining a court judgment. South Carolina follows federal garnishment limits: a creditor can garnish up to 25% of disposable earnings or the amount by which weekly earnings exceed 30 times the federal minimum wage, whichever is less. South Carolina does not have a state head-of-household garnishment exemption, so protections are limited to the federal floor. Never ignore a collections lawsuit — respond to the summons or you will receive a default judgment.",
        },
    ],
    "body": f"""
<p class="lead">South Carolina is home to <strong>over 130 licensed hospitals</strong>, and BillKarma&rsquo;s analysis of hospital charge data found that the median markup over Medicare rates across SC facilities is <strong>4.1&times;</strong> &mdash; meaning a procedure billed at $4,100 costs Medicare roughly $1,000. Despite SC Code &sect;&nbsp;44-7-3410 requiring nonprofit hospitals to maintain charity care programs, fewer than half of eligible patients ever apply. This guide explains every protection available to South Carolina patients, from charity care eligibility to the 3-year debt statute of limitations.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#charity-care">Charity care under SC Code &sect; 44-7-3410</a></li>
        <li><a href="#medicaid">South Carolina Medicaid (SC Healthy Connections)</a></li>
        <li><a href="#surprise-billing">Surprise billing protections (SB 1072 &amp; NSA)</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt</a></li>
        <li><a href="#debt-collection">Debt collection and wage garnishment rules</a></li>
        <li><a href="#how-to-dispute">How to dispute a South Carolina hospital bill</a></li>
        <li><a href="#bill-example">Annotated South Carolina hospital bill</a></li>
        <li><a href="#case-study">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="charity-care">1. Charity care under SC Code &sect; 44-7-3410</h2>

<p>South Carolina Code &sect;&nbsp;44-7-3410 requires every <strong>nonprofit hospital</strong> in the state to adopt and maintain a written charity care policy. The law is enforced by the South Carolina Department of Health and Environmental Control (SCDHEC), which licenses all hospitals in the state. Key requirements include:</p>

<ul>
    <li><strong>Written policy required.</strong> Every nonprofit hospital must have a formal, written charity care policy that defines eligibility thresholds, application procedures, and the types of assistance available (full write-off, discount, or payment plan).</li>
    <li><strong>Public posting.</strong> Hospitals must make their charity care policies available to patients on request and post them on their websites. If you cannot find a hospital&rsquo;s policy, call the billing department and ask for it in writing.</li>
    <li><strong>Uninsured patient screening.</strong> Hospitals are required to screen uninsured patients for charity care eligibility and to inform them of available financial assistance programs.</li>
    <li><strong>Application window.</strong> Most SC hospitals allow applications within 240 days of the first billing statement, though individual hospital policies vary. Apply as early as possible.</li>
</ul>

<p>Typical income thresholds at South Carolina nonprofit hospitals (thresholds vary by hospital — always check the specific hospital&rsquo;s policy):</p>

<table>
    <thead>
        <tr><th>Household Size</th><th>100% FPL (2026)</th><th>138% FPL (Medicaid)</th><th>200% FPL (common free care threshold)</th><th>300% FPL (common discount threshold)</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$15,650</td><td>$21,597</td><td>$31,300</td><td>$46,950</td></tr>
        <tr><td>2 people</td><td>$21,150</td><td>$29,187</td><td>$42,300</td><td>$63,450</td></tr>
        <tr><td>3 people</td><td>$26,650</td><td>$36,777</td><td>$53,300</td><td>$79,950</td></tr>
        <tr><td>4 people</td><td>$32,150</td><td>$44,367</td><td>$64,300</td><td>$96,450</td></tr>
        <tr><td>5 people</td><td>$37,650</td><td>$51,957</td><td>$75,300</td><td>$112,950</td></tr>
        <tr><td>6 people</td><td>$43,150</td><td>$59,547</td><td>$86,300</td><td>$129,450</td></tr>
    </tbody>
</table>

<p><em>FPL figures reflect 2026 HHS guidelines. Confirm current thresholds at <a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">aspe.hhs.gov</a>.</em></p>

<div class="key-takeaway">
    <strong>Always apply for charity care before paying.</strong> Under SC Code &sect;&nbsp;44-7-3410, every nonprofit hospital in South Carolina must have a financial assistance program. <a href="/charity-care">Use BillKarma&rsquo;s free eligibility tool</a> to see if you qualify and get a pre-filled application for your hospital.
</div>

<h2 id="medicaid">2. South Carolina Medicaid (SC Healthy Connections)</h2>

<p>South Carolina expanded Medicaid under the Affordable Care Act to cover adults earning up to <strong>138% of the Federal Poverty Level</strong> (approximately $20,783 for a single person in 2026). SC Healthy Connections is administered by the South Carolina Department of Health and Human Services (SCDHHS).</p>

<p>Key facts about SC Healthy Connections:</p>
<ul>
    <li><strong>Retroactive coverage.</strong> If approved, Medicaid can cover claims retroactively for up to 3 months before your application date. This means a recent hospital bill may be covered if you apply promptly.</li>
    <li><strong>Pregnant women.</strong> Pregnant South Carolina residents with income up to 194% FPL qualify for Medicaid coverage.</li>
    <li><strong>Children (CHIP).</strong> Children in households up to 208% FPL qualify for SC Healthy Connections for Children (CHIP).</li>
    <li><strong>Apply online.</strong> Applications can be submitted at <a href="https://www.scdhhs.gov" target="_blank" rel="noopener">scdhhs.gov</a> or at a local SCDHHS county office.</li>
</ul>

{_embed(mode="markup", title="Compare your South Carolina hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup over Medicare rates.", height="420")}

<h2 id="surprise-billing">3. Surprise billing protections (SB 1072 &amp; the No Surprises Act)</h2>

<p>South Carolina enacted SB 1072 to protect patients from unexpected out-of-network medical bills. Combined with the federal No Surprises Act (NSA), South Carolina patients have multiple layers of protection:</p>

<table>
    <thead>
        <tr><th>Protection</th><th>SC SB 1072</th><th>Federal No Surprises Act (2022)</th></tr>
    </thead>
    <tbody>
        <tr><td>Emergency services</td><td>Patient pays in-network cost-sharing only</td><td>Same; applies to all plan types including self-funded</td></tr>
        <tr><td>Non-emergency at in-network facility</td><td>Covered for state-regulated plans</td><td>Covered for all plan types; ancillary providers cannot balance bill</td></tr>
        <tr><td>Good faith cost estimate</td><td>Not required by state law</td><td>Providers must give uninsured patients a Good Faith Estimate before scheduled services</td></tr>
        <tr><td>Air ambulance</td><td>Not covered by state law</td><td>Covered; no balance billing for out-of-network air ambulance</td></tr>
        <tr><td>Dispute resolution</td><td>South Carolina DOI complaint process</td><td>Federal IDR process at CMS</td></tr>
    </tbody>
</table>

<p>If you receive a surprise bill from an out-of-network anesthesiologist, radiologist, or other ancillary provider at an in-network hospital, you likely have the right to dispute it under the NSA. <a href="/scan">Upload your bill to BillKarma</a> to check for NSA violations automatically.</p>

<div class="guide-cta-inline">
    <p><strong>Did you get a surprise bill in South Carolina?</strong> BillKarma identifies balance billing violations under SB 1072 and the federal No Surprises Act, then generates a ready-to-send dispute letter. <a href="/scan">Scan your bill free &mdash; takes under 2 minutes.</a></p>
</div>

<h2 id="statute-of-limitations">4. Statute of limitations on medical debt in South Carolina</h2>

<p>South Carolina Code &sect;&nbsp;15-3-530 sets a <strong>3-year statute of limitations</strong> on most medical debts. This is among the shortest SOL periods in the nation, giving patients significant protection against old debt lawsuits.</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>SC Statute of Limitations</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Medical bill (open account)</td><td>3 years</td><td>Applies to most hospital and physician bills without a signed contract</td></tr>
        <tr><td>Written contract (signed payment plan)</td><td>3 years</td><td>SC Code § 15-3-530 applies to both written and oral contracts</td></tr>
        <tr><td>Court judgment</td><td>10 years (renewable)</td><td>Responding to lawsuits is critical — never ignore a summons</td></tr>
    </tbody>
</table>

<p><strong>What resets the SOL in South Carolina:</strong></p>
<ul>
    <li>Any voluntary payment toward the debt — including a small partial payment — restarts the 3-year clock.</li>
    <li>A written acknowledgment of the debt can restart the clock.</li>
    <li>The SOL may be tolled (paused) if the debtor is absent from South Carolina for an extended period.</li>
</ul>

<p>Use our <a href="/statute-of-limitations">SOL lookup tool</a> to check your specific debt before making any payment or communicating with a collector about old medical bills.</p>

<h2 id="debt-collection">5. Debt collection and wage garnishment rules</h2>

<p>South Carolina patients facing medical debt collection have rights under both state and federal law:</p>

<h3>Wage garnishment limits</h3>
<p>South Carolina follows the federal Consumer Credit Protection Act garnishment limits:</p>
<ul>
    <li>A creditor may garnish up to <strong>25% of disposable earnings</strong> per week, or the amount by which disposable earnings exceed 30 times the federal minimum wage ($7.25/hour), whichever is <em>less</em>.</li>
    <li>A creditor must first sue you, win a judgment, and then petition the court for a garnishment order. No garnishment without a court judgment.</li>
    <li>South Carolina does <em>not</em> have a state head-of-household garnishment exemption beyond the federal floor.</li>
</ul>

<h3>Federal Fair Debt Collection Practices Act (FDCPA)</h3>
<p>The FDCPA prohibits third-party debt collectors from using abusive, deceptive, or unfair practices. Medical debt collectors cannot: call before 8 a.m. or after 9 p.m., use threatening or obscene language, falsely claim to be attorneys or government agencies, or threaten lawsuits they do not intend to file. File complaints with the <a href="https://www.consumerfinance.gov/complaint/" target="_blank" rel="noopener">CFPB</a> or the <a href="https://www.scag.gov/" target="_blank" rel="noopener">South Carolina Attorney General</a>.</p>

<h2 id="how-to-dispute">6. How to dispute a South Carolina hospital bill</h2>

<h3>Step 1: Request an itemized bill</h3>
<p>Call the hospital billing department and request a fully itemized statement listing every CPT code, revenue code, service description, quantity, and unit price. South Carolina patients have the right to an itemized bill on request. Put the request in writing by email or certified mail.</p>

<h3>Step 2: Check for billing errors</h3>
<p>Common errors include: duplicate charges, charges for services not rendered, upcoded procedure codes (billing a more complex procedure than was actually performed), and unbundling (breaking a single procedure into multiple smaller codes to inflate the total). Our <a href="/calculator">Medicare rate calculator</a> shows you the benchmark for every CPT code on your bill.</p>

<h3>Step 3: Apply for charity care if eligible</h3>
<p>If your income is at or below 200&ndash;300% FPL (thresholds vary by hospital), apply for financial assistance under the hospital&rsquo;s SC Code &sect;&nbsp;44-7-3410 charity care program. Ask the billing department for the application form &mdash; they are legally required to provide it.</p>

<h3>Step 4: Negotiate the balance</h3>
<p>If you do not qualify for full charity care, you can negotiate a reduced lump-sum settlement. Hospitals routinely accept 40&ndash;60 cents on the dollar for self-pay patients who can pay promptly. Always get any settlement agreement in writing before sending payment.</p>

<h3>Step 5: File a complaint if needed</h3>
<ul>
    <li><strong>Charity care denial:</strong> File a complaint with <a href="https://www.scdhec.gov/" target="_blank" rel="noopener">SCDHEC</a></li>
    <li><strong>Surprise billing:</strong> File with the <a href="https://doi.sc.gov/" target="_blank" rel="noopener">SC Department of Insurance</a></li>
    <li><strong>No Surprises Act violations:</strong> Contact the <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS No Surprises Help Desk</a> at 1-800-985-3059</li>
    <li><strong>Debt collection abuse:</strong> File with the <a href="https://www.consumerfinance.gov/complaint/" target="_blank" rel="noopener">CFPB</a> or <a href="https://www.scag.gov/" target="_blank" rel="noopener">SC Attorney General</a></li>
</ul>

<div class="key-takeaway">
    <strong>Always dispute in writing.</strong> Send dispute letters and charity care applications by certified mail with return receipt. Keep copies of everything. A paper trail is your strongest protection if the dispute escalates.
</div>

<h2 id="bill-example">7. Annotated South Carolina hospital bill</h2>

<p>The following example shows a common pattern in South Carolina hospital bills: an inflated ER charge, an ancillary provider surprise bill, and charges far above Medicare benchmarks.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Palmetto Regional Medical Center &mdash; Emergency Department &mdash; Date of Service: 03/14/2026</div>
    <div class="line-item error">
        <span>99285 &mdash; Emergency Department Visit, Level 5 &nbsp; &#10060; <em>Level 5 ED requires a high-severity presenting problem. If your visit involved a straightforward complaint (e.g., minor laceration, ear infection), a 99283 or 99284 is likely more appropriate. Request your visit notes and compare to AMA E&amp;M guidelines.</em></span>
        <span>$1,850.00</span>
    </div>
    <div class="line-item flagged">
        <span>71046 &mdash; Chest X-ray, 2 views &nbsp; &#9888; <em>Medicare pays approximately $41 for this code. At $380, this is a 9.3&times; markup over Medicare. While not automatically illegal, this supports a charity care or negotiation request.</em></span>
        <span>$380.00</span>
    </div>
    <div class="line-item">
        <span>93010 &mdash; Electrocardiogram (ECG), interpretation only</span>
        <span>$210.00</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete Blood Count (CBC) with differential</span>
        <span>$195.00</span>
    </div>
    <div class="line-item error">
        <span>Separate bill from Coastal Radiology Associates (out-of-network) &nbsp; &#10060; <em>If this radiologist interpreted your X-ray at an in-network ER, this is likely a surprise bill prohibited by the federal No Surprises Act. You should not owe more than your in-network cost-sharing.</em></span>
        <span>$640.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$3,275.00</span>
    </div>
</div>

<p><strong>How to address each issue:</strong></p>
<ul>
    <li><strong>Upcoded ER visit ($1,850):</strong> Request the medical chart notes from your visit. If the documentation doesn&rsquo;t support a Level 5 complexity, dispute the code and cite the AMA E&amp;M guidelines.</li>
    <li><strong>Chest X-ray at 9.3&times; Medicare ($380):</strong> Use this markup as leverage when negotiating a charity care application or lump-sum settlement.</li>
    <li><strong>Out-of-network radiology surprise bill ($640):</strong> Write a dispute letter citing the federal No Surprises Act. The radiologist interpreted images at an in-network facility — you owe only your in-network cost-sharing amount, not the balance.</li>
</ul>

<h2 id="case-study">8. Real patient results</h2>

<div class="case-study">
    <h3>Case study: $11,400 ER bill reduced to $0 through SC charity care &mdash; Columbia</h3>
    <p><strong>Situation:</strong> A 34-year-old uninsured construction worker in Columbia visited the ER after a workplace injury. He received X-rays, wound care, and pain management, resulting in an $11,400 bill from a Prisma Health nonprofit hospital.</p>
    <p><strong>Patient profile:</strong> Single, annual income $28,000 &mdash; approximately 179% FPL. Below the hospital&rsquo;s 200% FPL threshold for free care under SC Code &sect;&nbsp;44-7-3410.</p>
    <p><strong>Action:</strong> The patient did not know about charity care and began making $200/month payments. After two payments, he uploaded the bill to BillKarma. The system identified his likely charity care eligibility and flagged that his recent payments had reset the 3-year SOL clock. BillKarma generated a charity care application pre-filled with the hospital&rsquo;s specific income thresholds.</p>
    <p><strong>Result:</strong> The hospital approved the application, wrote off the remaining $11,000 balance, and refunded the two $200 payments already made. The patient&rsquo;s total liability was reduced to zero.</p>
    <p><strong>Savings: $11,400.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $2,800 surprise anesthesiology bill eliminated &mdash; Charleston</h3>
    <p><strong>Situation:</strong> A Charleston patient underwent outpatient gallbladder surgery at an in-network hospital. The surgeon and facility were in-network. Six weeks later, the patient received a $2,800 bill from an out-of-network anesthesiologist&rsquo;s group. Insurance paid $900 and the group balance-billed the patient $1,900.</p>
    <p><strong>Action:</strong> The patient disputed the balance bill under the federal No Surprises Act, noting that the anesthesiologist was an ancillary provider at an in-network facility with no advance consent obtained.</p>
    <p><strong>Result:</strong> The anesthesiology group withdrew the balance bill within 30 days. The patient owed only their in-network coinsurance of $150.</p>
    <p><strong>Savings: $1,900.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Know your 3-year clock.</strong> South Carolina&rsquo;s 3-year medical debt SOL is shorter than most states. If your bill is approaching 3 years old and you have not made any payments or acknowledged the debt in writing, a collector may not be able to win a lawsuit against you. Use our <a href="/statute-of-limitations">SOL lookup tool</a> to check your specific debt.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Are South Carolina hospitals required to offer charity care?</h3>
        <p>Yes &mdash; for nonprofit hospitals. SC Code &sect;&nbsp;44-7-3410 requires every nonprofit hospital to maintain a written charity care policy and screen uninsured patients for eligibility. For-profit hospitals are not covered by this mandate, though many voluntarily offer assistance. Always ask the billing department for a financial assistance application &mdash; you are entitled to one at any nonprofit hospital.</p>
    </div>
    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in South Carolina?</h3>
        <p>South Carolina has a 3-year SOL on most medical debts under SC Code &sect;&nbsp;15-3-530. The clock starts on the date of the last payment or the date the debt became due. Making any payment &mdash; even a small one &mdash; resets the clock. After 3 years without payment or written acknowledgment, a debt collector cannot win a lawsuit against you in South Carolina.</p>
    </div>
    <div class="faq-item">
        <h3>Does South Carolina protect patients from surprise medical bills?</h3>
        <p>Yes, through SB 1072 for state-regulated plans and the federal No Surprises Act for all plan types. If you received care at an in-network facility and got a separate bill from an out-of-network provider you didn&rsquo;t choose, that bill is likely prohibited. File a dispute with the provider and, if needed, with the <a href="https://doi.sc.gov/" target="_blank" rel="noopener">SC Department of Insurance</a> or CMS.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Medicaid income limit in South Carolina?</h3>
        <p>South Carolina&rsquo;s Medicaid expansion covers adults up to 138% FPL &mdash; about $20,783 for a single person or $35,277 for a family of three in 2026. Apply through <a href="https://www.scdhhs.gov" target="_blank" rel="noopener">scdhhs.gov</a>. Coverage can be retroactive for up to 3 months, potentially covering a recent hospital bill.</p>
    </div>
    <div class="faq-item">
        <h3>Can a South Carolina hospital sue me for an old medical bill?</h3>
        <p>Only if the debt is within the 3-year statute of limitations. After 3 years without payment or written acknowledgment, the debt is time-barred and a court cannot grant a judgment against you (if you raise the SOL as a defense). However, debt collectors may still contact you after the SOL expires. If sued on a time-barred debt, file an answer asserting the SOL as an affirmative defense — the court will not raise it on your behalf.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.scstatehouse.gov/code/t44c007.php" target="_blank" rel="noopener">SC Code &sect; 44-7-3410: Nonprofit Hospital Charity Care Requirements</a></li>
    <li><a href="https://www.scstatehouse.gov/code/t15c003.php" target="_blank" rel="noopener">SC Code &sect; 15-3-530: Statute of Limitations on Civil Actions</a></li>
    <li><a href="https://www.scdhhs.gov/apply-benefits" target="_blank" rel="noopener">SC DHHS: Apply for SC Healthy Connections Medicaid</a></li>
    <li><a href="https://doi.sc.gov/consumers/health-insurance" target="_blank" rel="noopener">SC Department of Insurance: Health Insurance Consumer Resources</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
    <li><a href="https://www.consumerfinance.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt Resources for Consumers</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
</ul>
""",
})
