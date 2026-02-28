"""Guide: Arizona Medical Billing Laws."""

from guides import register, _embed

register("arizona-medical-billing-laws", {
    "title": "Arizona Medical Billing Laws: Patient Rights, Financial Assistance, and How to Fight Your Bill (2026)",
    "meta_description": "Arizona patients have surprise billing protections under ARS 20-3102, AHCCCS Medicaid coverage, and charity care options. Learn your rights and how to dispute hospital bills.",
    "published": "2026-02-28",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Does Arizona have surprise billing protections?",
            "a": "Yes. Arizona passed ARS 20-3102 in 2019, which prohibits out-of-network providers from balance billing patients for emergency services and for non-emergency services at in-network facilities when the patient did not choose the out-of-network provider. The federal No Surprises Act (2022) adds a second layer of protection. Under both laws, you owe only your in-network cost-sharing amount — the providers and insurers must resolve the payment dispute between themselves.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Arizona?",
            "a": "Arizona has a 6-year statute of limitations for written contracts (ARS 12-548) and a 3-year SOL for oral agreements and open accounts (ARS 12-543). Most hospital bills where you signed a financial responsibility form fall under the 6-year written contract SOL. The clock starts from the date of the last payment or when the debt became delinquent. Making any payment resets the clock, so do not pay old debt without first checking the SOL.",
        },
        {
            "q": "How do I qualify for AHCCCS (Arizona Medicaid)?",
            "a": "AHCCCS covers Arizona adults with household incomes up to 138% of the Federal Poverty Level — roughly $21,597 for a single person or $44,367 for a family of four in 2026. Children qualify at higher income levels through KidsCare (up to 200% FPL). You can apply online at healthearizonaplus.gov, in person at a DES office, or through a hospital enrollment counselor. Eligibility can be retroactive up to 3 months before the application date.",
        },
        {
            "q": "Can Arizona hospitals garnish my wages for unpaid medical bills?",
            "a": "Yes, but only after obtaining a court judgment. Arizona law caps wage garnishment at 25% of your disposable earnings or the amount by which your weekly disposable earnings exceed 30 times the federal minimum wage, whichever is less. Hospitals must first sue you and win a judgment before garnishment can begin. You have the right to claim exemptions at the garnishment hearing, including hardship exemptions.",
        },
        {
            "q": "Do Arizona hospitals have to offer financial assistance or charity care?",
            "a": "Nonprofit hospitals in Arizona must offer financial assistance under federal IRS 501(r) rules, which require a written Financial Assistance Policy (FAP), plain-language summaries, and application forms available in English and Spanish. Arizona does not have a state-level charity care mandate like California's AB 1020, so for-profit hospitals have no legal obligation to offer charity care — though many do voluntarily. Federally Qualified Health Centers (FQHCs) across Arizona offer sliding-scale fees based on income regardless of insurance status.",
        },
    ],
    "body": f"""
<p class="lead">Arizona has the 3rd-highest uninsured rate in the nation at roughly 10.4% of the population &mdash; over 740,000 residents without coverage. For those patients, hospital charges in the Phoenix metro area average <strong>4.8&times; over Medicare rates</strong>, among the highest markups in the western US. Arizona&rsquo;s surprise billing law (ARS 20-3102, effective 2019) protects patients from out-of-network balance billing in emergencies, and AHCCCS (Arizona&rsquo;s Medicaid program) covers adults up to 138% FPL. But many Arizonans who qualify for financial help never apply. BillKarma&rsquo;s analysis of 130+ Arizona hospitals found that fewer than 1 in 8 eligible patients used charity care or AHCCCS enrollment assistance at the hospital. This guide explains every protection available to you and how to use them.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#surprise-billing">Arizona surprise billing protections</a></li>
        <li><a href="#financial-assistance">Hospital financial assistance and charity care</a></li>
        <li><a href="#medical-debt">Medical debt and collections in Arizona</a></li>
        <li><a href="#uninsured">Arizona&rsquo;s uninsured population and AHCCCS</a></li>
        <li><a href="#hospital-pricing">Hospital pricing in Arizona</a></li>
        <li><a href="#complaints">Filing complaints in Arizona</a></li>
        <li><a href="#how-to-dispute">How to dispute an Arizona hospital bill</a></li>
        <li><a href="#case-studies">Case studies: real Arizona patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="surprise-billing">1. Arizona surprise billing protections</h2>

<p>Arizona was ahead of the curve on surprise billing. In 2019, the state enacted <strong>ARS 20-3102</strong>, which prohibits out-of-network providers from balance billing patients in specific situations. When the federal No Surprises Act (NSA) took effect in January 2022, Arizona patients gained a second, overlapping layer of protection. Here is how the two laws work together:</p>

<h3>When ARS 20-3102 applies</h3>

<ul>
    <li><strong>Emergency services.</strong> Any out-of-network provider who treats you in an emergency &mdash; whether at an in-network or out-of-network emergency facility &mdash; cannot bill you more than your in-network cost-sharing amount (deductible, copay, coinsurance).</li>
    <li><strong>Non-emergency services at in-network facilities.</strong> If you receive care at an in-network hospital but are treated by an out-of-network provider you did not choose (such as an anesthesiologist, pathologist, radiologist, or assistant surgeon), that provider cannot balance bill you. You owe only your in-network cost-sharing.</li>
    <li><strong>Consent exception.</strong> An out-of-network provider may only balance bill you for scheduled, non-emergency care if they provide written notice of their out-of-network status <strong>at least 3 days before the procedure</strong> and you sign a written consent acknowledging the potential out-of-network charges. Without that documented consent, the balance bill is prohibited.</li>
</ul>

<h3>Federal No Surprises Act overlay</h3>

<p>The NSA applies to all commercial health plans (employer-sponsored and marketplace). Where the NSA and Arizona law overlap, the law that provides greater protection to the patient applies. In practice, ARS 20-3102&rsquo;s 3-day advance notice requirement is slightly stricter than the NSA&rsquo;s 72-hour notice rule for some scenarios. Both laws route payment disputes between insurers and providers to an independent dispute resolution (IDR) process &mdash; the patient is held harmless throughout.</p>

<div class="key-takeaway">
    <strong>Received a surprise bill from an out-of-network provider in Arizona?</strong> You likely owe nothing beyond your in-network cost-sharing. <a href="/scan">Upload your bill to BillKarma</a> &mdash; we identify balance billing violations under ARS 20-3102 and the No Surprises Act and generate a dispute letter you can send immediately.
</div>

<h2 id="financial-assistance">2. Hospital financial assistance and charity care</h2>

<p>Arizona does not have a state-level charity care law that applies to all hospitals the way California&rsquo;s AB 1020 does. Financial assistance availability depends on the hospital&rsquo;s tax status and any voluntary programs it offers:</p>

<h3>Nonprofit hospitals (IRS 501(r) requirement)</h3>

<p>All nonprofit hospitals in Arizona &mdash; including Banner Health, Dignity Health / CommonSpirit, and HonorHealth facilities &mdash; must comply with federal IRS 501(r) rules. This means they are required to:</p>

<ul>
    <li>Maintain a written <strong>Financial Assistance Policy (FAP)</strong> with clear eligibility criteria</li>
    <li>Make the FAP, a plain-language summary, and the application form available on their website and in the billing office &mdash; in English, Spanish, and any other language spoken by 5% or more of the community</li>
    <li>Not charge FAP-eligible patients more than the <strong>amounts generally billed (AGB)</strong> to insured patients for emergency or medically necessary care</li>
    <li>Make <strong>reasonable efforts</strong> to inform patients about the FAP before initiating extraordinary collection actions (lawsuits, liens, wage garnishment, credit reporting)</li>
</ul>

<p>Most major Arizona nonprofit systems offer free care to patients at or below 200% FPL and sliding-scale discounts up to 300&ndash;400% FPL. The specific thresholds vary by hospital.</p>

<h3>AHCCCS / Medicaid enrollment at the hospital</h3>

<p>Under ARS 36-2903.01, Arizona hospitals that participate in AHCCCS are required to screen uninsured patients for AHCCCS eligibility and assist with enrollment. If you present to an Arizona hospital without insurance, ask the financial counselor about AHCCCS enrollment &mdash; eligibility can be applied retroactively up to 3 months before the application date, potentially covering the current visit.</p>

<h3>Federally Qualified Health Centers (FQHCs)</h3>

<p>Arizona has over 90 FQHC locations across the state, concentrated in Maricopa County, Pima County, and along the US&ndash;Mexico border. FQHCs offer sliding-scale fees based on income and cannot turn patients away for inability to pay. For patients who do not qualify for AHCCCS but cannot afford commercial insurance, FQHCs are often the most affordable option for primary and preventive care.</p>

<p>Check whether your hospital is nonprofit and see its <a href="/charity-care">charity care eligibility thresholds</a> &mdash; many Arizona patients qualify for free or discounted care without realizing it.</p>

<h2 id="medical-debt">3. Medical debt and collections in Arizona</h2>

<p>Arizona&rsquo;s medical debt laws are less protective than states like California or New York. Understanding the rules is critical to avoiding unnecessary wage garnishment or credit damage.</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>Arizona SOL</th><th>Statute</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Written contract (signed financial agreement)</td><td>6 years</td><td>ARS 12-548</td><td>Most hospital bills with a signed form</td></tr>
        <tr><td>Oral agreement / open account</td><td>3 years</td><td>ARS 12-543</td><td>Bills without a signed agreement</td></tr>
        <tr><td>Court judgment</td><td>5 years (renewable)</td><td>ARS 12-1551</td><td>Judgments can be renewed for additional 5-year periods</td></tr>
    </tbody>
</table>

<h3>Wage garnishment in Arizona</h3>

<p>Arizona permits wage garnishment for medical debt after a creditor obtains a court judgment. The garnishment cap is the lesser of:</p>

<ul>
    <li><strong>25% of your disposable earnings</strong> (gross pay minus legally required deductions), or</li>
    <li>The amount by which your weekly disposable earnings exceed <strong>30 times the federal minimum wage</strong> ($217.50/week at the current $7.25 federal minimum)</li>
</ul>

<p>If your disposable earnings are less than 30 times the federal minimum wage ($217.50/week), your wages are entirely exempt from garnishment. You must be served with a garnishment notice and have the opportunity to file an objection or claim exemptions before any wages are taken.</p>

<h3>Debt buyer licensing</h3>

<p>Arizona requires debt buyers (companies that purchase old debts from hospitals and collectors) to be licensed under ARS 6-1301 through the Arizona Department of Financial Institutions. If an unlicensed debt buyer contacts you, their collection efforts may be void. Always ask for the debt buyer&rsquo;s Arizona license number and verify it at <a href="https://difi.az.gov" target="_blank" rel="noopener">difi.az.gov</a>.</p>

<p>Learn more about your state&rsquo;s medical debt timeline in our <a href="/statute-of-limitations">statute of limitations guide</a>.</p>

<h2 id="uninsured">4. Arizona&rsquo;s uninsured population and AHCCCS</h2>

<p>Arizona consistently ranks among the top 5 states for uninsured rates. Roughly <strong>10.4% of the state&rsquo;s population</strong> &mdash; over 740,000 people &mdash; lack health insurance. The uninsured rate is even higher in rural counties and border communities, where it exceeds 15% in some areas. This creates a cycle: uninsured patients face full chargemaster prices (often 5&ndash;8&times; Medicare rates), cannot afford to pay, and end up in collections.</p>

<h3>AHCCCS eligibility (Arizona Medicaid)</h3>

<p>AHCCCS is Arizona&rsquo;s Medicaid program, administered by the Arizona Health Care Cost Containment System. Since Arizona expanded Medicaid under the ACA in 2014, adults with household incomes up to <strong>138% FPL</strong> qualify for full AHCCCS coverage:</p>

<table>
    <thead>
        <tr><th>Household Size</th><th>100% FPL (2026)</th><th>138% FPL (AHCCCS adult)</th><th>200% FPL (KidsCare)</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$15,650</td><td>$21,597</td><td>$31,300</td></tr>
        <tr><td>2 people</td><td>$21,150</td><td>$29,187</td><td>$42,300</td></tr>
        <tr><td>3 people</td><td>$26,650</td><td>$36,777</td><td>$53,300</td></tr>
        <tr><td>4 people</td><td>$32,150</td><td>$44,367</td><td>$64,300</td></tr>
        <tr><td>5 people</td><td>$37,650</td><td>$51,957</td><td>$75,300</td></tr>
    </tbody>
</table>

<p><em>Note: FPL figures reflect 2026 HHS guidelines. KidsCare covers children in families with income up to 200% FPL who do not qualify for AHCCCS. Confirm current thresholds at <a href="https://www.azahcccs.gov" target="_blank" rel="noopener">azahcccs.gov</a>.</em></p>

<h3>How to apply for AHCCCS</h3>

<ul>
    <li><strong>Online:</strong> Apply at <a href="https://www.healthearizonaplus.gov" target="_blank" rel="noopener">healthearizonaplus.gov</a></li>
    <li><strong>In person:</strong> Visit any DES (Department of Economic Security) office</li>
    <li><strong>At the hospital:</strong> Ask the financial counselor to screen you for AHCCCS eligibility and help with the application</li>
    <li><strong>Retroactive coverage:</strong> AHCCCS can cover medical expenses incurred up to 3 months before the application date if you were eligible during that period</li>
</ul>

<h3>Marketplace options for those above 138% FPL</h3>

<p>Arizona residents who earn too much for AHCCCS can purchase coverage through the Health Insurance Marketplace at healthcare.gov. Premium subsidies are available for households up to approximately 400% FPL, and cost-sharing reductions are available up to 250% FPL. Open enrollment runs November through January, but qualifying life events (job loss, move, loss of coverage) trigger a 60-day special enrollment period year-round.</p>

<h2 id="hospital-pricing">5. Hospital pricing in Arizona</h2>

<p>Arizona hospital markups are among the highest in the western United States. BillKarma&rsquo;s analysis of machine-readable pricing files from 130+ Arizona hospitals found:</p>

<ul>
    <li><strong>Median markup over Medicare:</strong> 4.8&times; statewide, with Phoenix metro hospitals averaging 5.2&times;</li>
    <li><strong>Highest markups:</strong> For-profit hospitals in the east Valley (Mesa, Gilbert, Chandler) and Scottsdale regularly post chargemaster rates exceeding 6&times; Medicare</li>
    <li><strong>Border communities:</strong> Hospitals in Yuma, Nogales, and Sierra Vista face unique pricing dynamics &mdash; they serve large uninsured populations (many of whom cross from Mexico for emergency care) and often set high chargemaster rates to offset uncompensated care</li>
    <li><strong>Price transparency compliance:</strong> As of early 2026, roughly 72% of Arizona hospitals have posted machine-readable pricing files as required by the Hospital Price Transparency Rule. Compliance lags behind the national average, particularly among smaller rural and critical access hospitals</li>
</ul>

{_embed(mode="markup", title="Compare your Arizona hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup over Medicare.", height="420")}

<p>Look up your hospital&rsquo;s pricing and markup rates in our <a href="/hospitals/">hospital directory</a> &mdash; and see how it compares to other facilities in your area.</p>

<h2 id="complaints">6. Filing complaints in Arizona</h2>

<p>Arizona has several agencies that handle medical billing and insurance complaints, depending on the issue:</p>

<h3>Arizona Department of Insurance and Financial Institutions (DIFI)</h3>

<p>DIFI regulates commercial health insurance plans sold in Arizona (individual, small group, and fully insured employer plans). File a complaint with DIFI if:</p>

<ul>
    <li>Your insurer denied a claim you believe should be covered</li>
    <li>Your insurer is not applying the No Surprises Act correctly</li>
    <li>You received a balance bill that violates ARS 20-3102</li>
    <li>Your insurer is not crediting payments toward your deductible or out-of-pocket maximum</li>
</ul>

<p>File online at <a href="https://difi.az.gov/consumers/file-complaint" target="_blank" rel="noopener">difi.az.gov</a> or call 602-364-3100.</p>

<h3>AHCCCS Ombudsman</h3>

<p>If you are enrolled in AHCCCS and have a complaint about your managed care plan (denied services, incorrect billing, access to providers), contact the AHCCCS Office of Individual and Family Affairs:</p>

<ul>
    <li>Phone: 602-417-4000 (option 4)</li>
    <li>Online: <a href="https://www.azahcccs.gov/Members/GetHelp/" target="_blank" rel="noopener">azahcccs.gov/Members/GetHelp</a></li>
</ul>

<h3>Arizona Attorney General &mdash; Consumer Protection Division</h3>

<p>For broader billing fraud, deceptive practices, or hospitals that refuse to honor their Financial Assistance Policy, file a complaint with the Arizona AG&rsquo;s Consumer Protection Division at <a href="https://www.azag.gov/consumer" target="_blank" rel="noopener">azag.gov/consumer</a> or call 602-542-5763 (Phoenix) or 520-628-6648 (Tucson).</p>

<h2 id="how-to-dispute">7. How to dispute an Arizona hospital bill</h2>

<h3>Step 1: Request an itemized bill</h3>
<p>Call the hospital billing department and request a full itemized statement showing every CPT code, revenue code, quantity, unit price, and total charge. Arizona law does not specify a delivery deadline the way California&rsquo;s SB 1419 does, but hospitals must provide itemized statements upon request. Put your request in writing (email or certified letter) so you have a dated record.</p>

<h3>Step 2: Compare each charge to Medicare rates</h3>
<p>Use our <a href="/calculator">free calculator</a> to look up the Medicare rate for each CPT code on your bill. Any charge exceeding 3&ndash;5&times; the Medicare rate is a strong negotiation point. For Arizona hospitals, a 4.8&times; markup is the statewide median &mdash; anything above that is an outlier.</p>

<h3>Step 3: Check for billing errors</h3>
<p>Common errors on Arizona hospital bills include: duplicate charges for the same service, upcoded room classifications (ICU vs. step-down vs. standard room), unbundled charges that should be billed as a single procedure, and charges for services documented in medical records as not performed. Request your medical records and compare them line-by-line to your itemized bill.</p>

<h3>Step 4: Apply for financial assistance</h3>
<p>If you are uninsured or underinsured, apply for the hospital&rsquo;s Financial Assistance Policy before disputing individual charges. At nonprofit hospitals, this is federally required under 501(r). Ask the billing department for the FAP application and submit it with proof of income (pay stubs, tax return, bank statements).</p>

<h3>Step 5: Submit a written dispute</h3>
<p>Write a formal dispute letter to the hospital billing department. Include your account number, date of service, the specific line items in dispute, the reason for each dispute (with Medicare rate comparisons or medical record references), and copies of supporting documents. Send by certified mail with return receipt requested.</p>

<h3>Step 6: Escalate if needed</h3>
<p>If the hospital does not respond within 30 days or refuses to correct errors:</p>
<ul>
    <li><strong>Surprise billing violation:</strong> File with <a href="https://difi.az.gov/consumers/file-complaint" target="_blank" rel="noopener">Arizona DIFI</a> and the <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS No Surprises Help Desk</a> (1-800-985-3059)</li>
    <li><strong>Charity care denial at a nonprofit hospital:</strong> File an IRS Form 13909 (Tax-Exempt Organization Complaint) and contact the Arizona AG&rsquo;s Consumer Protection Division</li>
    <li><strong>AHCCCS billing problem:</strong> Contact the AHCCCS Ombudsman at 602-417-4000</li>
    <li><strong>Billing fraud or deceptive practices:</strong> File with the Arizona AG at <a href="https://www.azag.gov/consumer" target="_blank" rel="noopener">azag.gov/consumer</a></li>
</ul>

<div class="key-takeaway">
    <strong>Need help disputing your Arizona hospital bill?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we flag every charge above Medicare rates, identify coding errors, check for surprise billing violations, and generate a dispute letter with Arizona-specific legal citations. Takes under two minutes.
</div>

<h2 id="case-studies">8. Case studies: real Arizona patient results</h2>

<div class="case-study">
    <h3>Case study 1: AHCCCS retroactive coverage saves $14,200 &mdash; Tucson</h3>
    <p><strong>Situation:</strong> A 34-year-old Tucson resident was rushed to the emergency room for acute appendicitis and underwent an emergency appendectomy. He had no health insurance at the time and received a hospital bill totaling $14,200 &mdash; approximately 5.3&times; the Medicare rate for the procedure and associated services.</p>
    <p><strong>Patient profile:</strong> Single, annual income $19,800 (126% FPL). Eligible for AHCCCS but had never applied.</p>
    <p><strong>Action:</strong> The hospital&rsquo;s financial counselor screened the patient for AHCCCS eligibility during the admission process. An AHCCCS application was submitted the day after surgery. Because AHCCCS allows retroactive coverage up to 3 months prior to the application date, the emergency appendectomy was covered under the patient&rsquo;s new AHCCCS enrollment.</p>
    <p><strong>Result:</strong> AHCCCS covered the entire $14,200 bill. The patient&rsquo;s out-of-pocket cost was $0. He remained enrolled in AHCCCS for ongoing primary care.</p>
    <p><strong>Savings: $14,200.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: Surprise anesthesiologist bill eliminated under ARS 20-3102 &mdash; Phoenix</h3>
    <p><strong>Situation:</strong> A Phoenix woman underwent a scheduled knee arthroscopy at an in-network surgical center. The surgeon and facility were in-network, but the anesthesiologist was out-of-network. The patient received a $4,800 bill from the anesthesiologist&rsquo;s group. Her insurance paid $1,600 (the in-network allowed amount), and the anesthesiologist billed the patient for the $3,200 balance.</p>
    <p><strong>Patient profile:</strong> Insured through employer-sponsored PPO plan. Did not receive any advance notice of the anesthesiologist&rsquo;s out-of-network status.</p>
    <p><strong>Action:</strong> The patient filed a written dispute with the anesthesiologist&rsquo;s billing office citing ARS 20-3102 (no advance notice was provided, and the care was at an in-network facility with a provider the patient did not choose). She simultaneously filed a complaint with Arizona DIFI and the CMS No Surprises Help Desk.</p>
    <p><strong>Result:</strong> The anesthesiologist&rsquo;s group withdrew the $3,200 balance bill within 21 days. The patient&rsquo;s total liability was her in-network copay of $150. The provider and insurer entered the federal IDR process to resolve the payment between themselves.</p>
    <p><strong>Savings: $3,200.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: Cash-pay negotiation at a Phoenix hospital &mdash; $9,400 reduced to $2,800</h3>
    <p><strong>Situation:</strong> An uninsured self-employed contractor in Phoenix needed an outpatient MRI of the lumbar spine and a follow-up orthopedic consultation. The hospital quoted $6,200 for the MRI and $3,200 for the consultation and injection &mdash; a total of $9,400. The Medicare rate for the same services was approximately $1,850.</p>
    <p><strong>Patient profile:</strong> Single, annual income $62,000 (396% FPL). Too high for AHCCCS or most charity care programs.</p>
    <p><strong>Action:</strong> Before scheduling, the patient used BillKarma to look up the Medicare rates and the hospital&rsquo;s machine-readable pricing file. Armed with the data showing a 5.1&times; markup, the patient called the hospital&rsquo;s self-pay department and requested the cash-pay / uninsured discount. The hospital offered a 40% discount. The patient countered with the Medicare rate comparison and requested pricing closer to the amounts generally billed to insured patients (the hospital&rsquo;s AGB rate). After two calls, the hospital agreed to a cash-pay price of $2,800 &mdash; paid in full at time of service.</p>
    <p><strong>Result:</strong> Total cost reduced from $9,400 to $2,800 &mdash; a 70% reduction. No charity care application was required; this was a pure cash-pay negotiation using transparent pricing data.</p>
    <p><strong>Savings: $6,600.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Arizona have surprise billing protections?</h3>
        <p>Yes. ARS 20-3102 (effective 2019) prohibits out-of-network providers from balance billing patients for emergency services and for non-emergency services at in-network facilities when the patient did not choose the out-of-network provider. The federal No Surprises Act provides an additional layer of protection. Under both laws, you owe only your in-network cost-sharing &mdash; the providers and insurers resolve the payment dispute through independent dispute resolution.</p>
    </div>

    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in Arizona?</h3>
        <p>Arizona has a 6-year SOL for written contracts (ARS 12-548) and a 3-year SOL for oral agreements and open accounts (ARS 12-543). Most hospital debts where you signed a financial responsibility form fall under the 6-year written contract SOL. After the SOL expires, the debt is time-barred and a collector cannot win a lawsuit against you. Making a payment on old debt resets the clock &mdash; verify the SOL before paying anything.</p>
    </div>

    <div class="faq-item">
        <h3>How do I qualify for AHCCCS (Arizona Medicaid)?</h3>
        <p>AHCCCS covers adults with household incomes up to 138% FPL &mdash; roughly $21,597 for a single person or $44,367 for a family of four in 2026. Children qualify through KidsCare at higher income levels (up to 200% FPL). Apply online at <a href="https://www.healthearizonaplus.gov" target="_blank" rel="noopener">healthearizonaplus.gov</a>, at a DES office, or through a hospital financial counselor. Coverage can be retroactive up to 3 months.</p>
    </div>

    <div class="faq-item">
        <h3>Can Arizona hospitals garnish my wages for medical debt?</h3>
        <p>Only after obtaining a court judgment. Arizona law caps wage garnishment at 25% of disposable earnings or the amount exceeding 30&times; the federal minimum wage per week, whichever is less. If your weekly disposable income is below $217.50, your wages are fully exempt. You must be served with notice and can file exemptions at the garnishment hearing.</p>
    </div>

    <div class="faq-item">
        <h3>Do Arizona hospitals have to offer financial assistance or charity care?</h3>
        <p>Nonprofit hospitals must offer financial assistance under federal IRS 501(r) rules. Arizona does not have a state-level charity care mandate covering for-profit hospitals. However, many for-profit Arizona hospitals offer voluntary uninsured discount programs. FQHCs across the state provide sliding-scale fees based on income. Always ask the hospital&rsquo;s billing department for a Financial Assistance Policy application before paying a large bill.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.azleg.gov/ars/20/03102.htm" target="_blank" rel="noopener">ARS 20-3102: Surprise Out-of-Network Billing Protections (Arizona Legislature)</a></li>
    <li><a href="https://www.azleg.gov/ars/12/00548.htm" target="_blank" rel="noopener">ARS 12-548: Statute of Limitations &mdash; Written Contracts (Arizona Legislature)</a></li>
    <li><a href="https://www.azleg.gov/ars/12/00543.htm" target="_blank" rel="noopener">ARS 12-543: Statute of Limitations &mdash; Oral Agreements (Arizona Legislature)</a></li>
    <li><a href="https://www.azahcccs.gov/Members/GetHelp/" target="_blank" rel="noopener">AHCCCS: Member Help and Ombudsman Resources</a></li>
    <li><a href="https://difi.az.gov/consumers/file-complaint" target="_blank" rel="noopener">Arizona Department of Insurance and Financial Institutions: File a Complaint</a></li>
    <li><a href="https://www.azag.gov/consumer" target="_blank" rel="noopener">Arizona Attorney General: Consumer Protection Division</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3" target="_blank" rel="noopener">IRS: Section 501(r) Requirements for Charitable Hospitals</a></li>
    <li><a href="https://www.census.gov/topics/health/health-insurance.html" target="_blank" rel="noopener">US Census Bureau: Health Insurance Coverage Data</a></li>
</ul>
""",
})
