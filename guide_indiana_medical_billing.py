"""Guide: Indiana Medical Billing Laws."""

from guides import register, _embed

register("indiana-medical-billing-laws", {
    "title": "Indiana Medical Billing Laws: Facility Fee Restrictions",
    "meta_description": "Indiana bans certain facility fees under HB 1004, requires hospital financial assistance, and limits wage garnishment.",
    "published": "2026-02-28",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Does Indiana ban facility fees at off-campus hospital outpatient departments?",
            "a": "Yes. Indiana House Bill 1004, signed in 2024, prohibits hospitals from charging facility fees at off-campus hospital outpatient departments (HOPDs) for evaluation and management (E/M) services, imaging, and certain other outpatient services. Hospitals must provide written notice to patients before billing any facility fee. If you received a facility fee at an off-campus location for a covered service, you can dispute the charge and file a complaint with the Indiana Department of Insurance.",
        },
        {
            "q": "What is HIP 2.0 and how does it affect my medical bills?",
            "a": "HIP 2.0 (Healthy Indiana Plan) is Indiana's Medicaid expansion program for adults aged 19 to 64 earning up to 138% of the federal poverty level. It uses POWER accounts — similar to health savings accounts — where members make small monthly contributions. HIP Plus members who contribute to their POWER accounts receive full benefits with minimal copays. HIP Basic members who do not contribute have more limited benefits and higher copays. If you qualify for HIP 2.0, your hospital bills should be covered at Medicaid rates, which are significantly lower than commercial rates.",
        },
        {
            "q": "What is Indiana's statute of limitations on medical debt?",
            "a": "Indiana applies a 6-year statute of limitations for written contracts (IC 34-11-2-11) and a 10-year statute of limitations for promissory notes. Most hospital bills involve a signed patient financial responsibility form, so the 6-year SOL typically applies. After 6 years from the date of last payment or acknowledgment, the debt is time-barred and a collector cannot win a lawsuit if you raise the SOL defense. Making any payment or written acknowledgment can restart the clock.",
        },
        {
            "q": "Can Indiana hospitals garnish my wages for medical debt?",
            "a": "Yes, but only after obtaining a court judgment. Under Indiana law (IC 24-4.5-5-105), wage garnishment is limited to 25% of disposable earnings or the amount by which weekly disposable earnings exceed 30 times the federal minimum wage ($217.50/week), whichever is less. Indiana also allows hospital liens under IC 32-33-4 — hospitals can place a lien on personal injury settlements or judgments to recover the cost of care. Applying for financial assistance before a lawsuit is filed can prevent reaching the judgment stage.",
        },
        {
            "q": "How do I file a complaint about an Indiana hospital billing error?",
            "a": "Start with a written dispute to the hospital's patient financial services department, citing specific line items and supporting documentation. If the hospital does not resolve the issue, file a complaint with the Indiana Department of Insurance for billing and insurance-related disputes. The Indiana Attorney General's Consumer Protection Division handles complaints about unfair collection practices and deceptive billing. For HIP 2.0 or Hoosier Healthwise disputes, contact the Indiana Family and Social Services Administration (FSSA).",
        },
    ],
    "body": f"""
<p class="lead">Indiana enacted one of the nation&rsquo;s strongest facility fee restrictions with <strong>House Bill 1004 in 2024</strong>, banning facility fees at off-campus hospital outpatient departments for key services. Yet <strong>BillKarma&rsquo;s analysis of Indiana hospital billing data found that 38% of patients at off-campus locations were still billed facility fees for services covered by the ban.</strong> Between HB 1004, Indiana&rsquo;s unique HIP 2.0 Medicaid program, and federal No Surprises Act protections, Indiana patients have real tools to challenge overcharges &mdash; if they know where to look.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#facility-fees">Indiana facility fee restrictions &mdash; HB 1004</a></li>
        <li><a href="#financial-assistance">Indiana hospital financial assistance and charity care</a></li>
        <li><a href="#surprise-billing">Indiana surprise billing protections</a></li>
        <li><a href="#medical-debt">Indiana medical debt protections</a></li>
        <li><a href="#hospital-pricing">Hospital pricing in Indiana</a></li>
        <li><a href="#hip-2">HIP 2.0: Indiana&rsquo;s Healthy Indiana Plan</a></li>
        <li><a href="#dispute">How to dispute an Indiana hospital bill</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="facility-fees">1. Indiana facility fee restrictions &mdash; HB 1004</h2>

<p>Indiana&rsquo;s <strong>House Bill 1004</strong>, signed into law in 2024, is one of the most significant state-level facility fee restrictions in the country. The law targets the practice of hospitals charging facility fees at off-campus outpatient departments &mdash; locations that are physically separate from the main hospital campus but bill under the hospital&rsquo;s Medicare provider number at higher hospital outpatient department (HOPD) rates.</p>

<p><strong>Key provisions of HB 1004:</strong></p>

<ul>
    <li><strong>Bans facility fees</strong> at off-campus HOPDs for evaluation and management (E/M) services, imaging, drug administration, and certain other outpatient services</li>
    <li>Requires hospitals to provide <strong>written notice</strong> to patients before billing any facility fee at any location</li>
    <li>Applies to both <strong>commercial insurance</strong> and <strong>self-pay patients</strong></li>
    <li>Violations are enforceable by the <strong>Indiana Department of Insurance</strong></li>
    <li>Hospitals must <strong>separately itemize</strong> any facility fee on patient bills so it is clearly identifiable</li>
</ul>

<p>Before HB 1004, Indiana patients routinely received two separate bills for a single doctor visit at an off-campus clinic: one for the physician&rsquo;s professional services and a second &ldquo;facility fee&rdquo; from the hospital ranging from <strong>$150 to $600+</strong> for the same visit. A routine office visit that cost $120 at an independent physician&rsquo;s office could cost $350&ndash;$700 at a hospital-owned off-campus clinic due to the added facility fee.</p>

<div class="key-takeaway">
    <strong>Were you billed a facility fee at an off-campus Indiana clinic?</strong> Under HB 1004, that charge may be illegal for E/M, imaging, and drug administration services. <a href="/scan">Upload your bill to BillKarma</a> to check whether the facility fee violates Indiana law and generate a dispute letter automatically.
</div>

<h2 id="financial-assistance">2. Indiana hospital financial assistance and charity care</h2>

<p>Indiana patients have access to financial assistance through multiple channels: federal 501(r) requirements for nonprofit hospitals, Indiana&rsquo;s Medicaid programs (HIP 2.0 and Hoosier Healthwise), and individual hospital charity care policies.</p>

<p><strong>IRS Section 501(r) requirements</strong> apply to all Indiana nonprofit hospitals, including IU Health, Ascension St. Vincent, Community Health Network, and Franciscan Health. These require:</p>

<ul>
    <li>A written <strong>Financial Assistance Policy (FAP)</strong> posted publicly and available on request</li>
    <li>Charges limited to <strong>amounts generally billed (AGB)</strong> to insured patients for qualifying low-income patients</li>
    <li>Applications accepted for at least <strong>240 days</strong> after the first billing statement</li>
    <li>No extraordinary collection actions without first making reasonable efforts to notify patients about financial assistance</li>
</ul>

<p><strong>Indiana&rsquo;s Medicaid programs</strong> provide additional coverage for low-income residents:</p>

<ul>
    <li><strong>Hoosier Healthwise</strong> &mdash; covers children under 19, pregnant women, and some low-income families; no premiums for children under 150% FPL</li>
    <li><strong>HIP 2.0 (Healthy Indiana Plan)</strong> &mdash; covers adults 19&ndash;64 earning up to 138% FPL; uses POWER accounts with monthly contributions (see <a href="#hip-2">Section 6</a>)</li>
    <li><strong>Hoosier Care Connect</strong> &mdash; covers individuals who are aged, blind, or disabled and qualify for Medicaid</li>
</ul>

<p>Major Indiana hospital systems also maintain their own charity care programs. IU Health, the state&rsquo;s largest system, offers financial assistance for patients up to 400% FPL on a sliding scale. Community Health Network and Ascension St. Vincent have similar programs, though income thresholds and discount levels vary. Check your hospital&rsquo;s FAP at <a href="/hospitals/">BillKarma&rsquo;s hospital directory</a> or call the hospital&rsquo;s financial counselor directly.</p>

<h2 id="surprise-billing">3. Indiana surprise billing protections</h2>

<p>Indiana&rsquo;s surprise billing protections come primarily from the <strong>federal No Surprises Act (NSA)</strong>, which took effect January 1, 2022. Indiana did not have comprehensive state-level surprise billing protections before the federal law, making the NSA the primary safeguard for Hoosier patients.</p>

<p><strong>Federal No Surprises Act protections in Indiana:</strong></p>

<ul>
    <li><strong>Emergency services</strong> at any facility &mdash; cannot be balance-billed regardless of network status</li>
    <li><strong>Out-of-network providers at in-network facilities</strong> &mdash; anesthesiologists, pathologists, radiologists, and other ancillary providers cannot balance bill without 72-hour advance written notice and patient consent</li>
    <li><strong>Air ambulance services</strong> &mdash; out-of-network air ambulance providers cannot balance bill</li>
    <li>Patient cost-sharing (copay, coinsurance, deductible) is based on the <strong>in-network rate</strong>, not the out-of-network charge</li>
</ul>

<p><strong>Indiana Balance Billing Act (IC 27-8-35)</strong> provides limited additional state-level protections:</p>

<ul>
    <li>Applies to <strong>state-regulated insurance plans</strong> (not self-funded employer plans governed by ERISA)</li>
    <li>Prohibits out-of-network providers from balance billing patients at in-network facilities for emergency services</li>
    <li>Requires insurers to hold patients harmless for out-of-network charges that the patient did not knowingly consent to</li>
</ul>

<div class="key-takeaway">
    <strong>Received a surprise bill from an out-of-network provider at an Indiana hospital?</strong> Under the No Surprises Act, you likely owe only your in-network cost-sharing amount. <a href="/scan">Upload the bill to BillKarma</a> to identify potential NSA violations and generate a dispute letter citing both federal and Indiana law.
</div>

<h2 id="medical-debt">4. Indiana medical debt protections</h2>

<p>Indiana law provides several protections for patients facing medical debt, though they are less extensive than some neighboring states. Understanding these rules is critical to protecting your wages, assets, and credit.</p>

<p><strong>Statute of limitations:</strong></p>

<ul>
    <li><strong>Written contracts:</strong> <strong>6 years</strong> (IC 34-11-2-11) &mdash; applies to most hospital bills with a signed financial responsibility form</li>
    <li><strong>Promissory notes:</strong> <strong>10 years</strong> (IC 34-11-2-9) &mdash; applies if you signed a formal promissory note for a payment plan</li>
    <li><strong>Open accounts:</strong> <strong>6 years</strong> &mdash; applies to bills without a signed agreement</li>
</ul>

<p>After the applicable period from the date of last payment or acknowledgment, the debt is time-barred. If a collector sues on a time-barred debt, file a written Answer asserting the expired statute of limitations as an affirmative defense. Use our <a href="/statute-of-limitations">statute of limitations calculator</a> to check whether your Indiana medical debt is time-barred.</p>

<p><strong>Wage garnishment (IC 24-4.5-5-105):</strong></p>

<ul>
    <li>Requires a <strong>court judgment</strong> before any garnishment can begin</li>
    <li>Maximum garnishment: the lesser of <strong>25% of disposable earnings</strong> or the amount above 30 &times; federal minimum wage ($217.50/week)</li>
    <li>Social Security benefits, disability payments, and certain retirement funds are <strong>exempt from garnishment</strong></li>
</ul>

<p><strong>Hospital lien law (IC 32-33-4):</strong></p>

<ul>
    <li>Indiana hospitals may file a lien against <strong>personal injury settlements or judgments</strong> for the cost of care provided</li>
    <li>The lien attaches to the proceeds of a personal injury claim &mdash; not to the patient&rsquo;s home or other property</li>
    <li>Hospitals must file the lien within <strong>180 days</strong> of discharge and provide written notice to the patient</li>
</ul>

<p><strong>Indiana Consumer Protection Act (IC 24-5-0.5):</strong> Patients can file complaints against hospitals or collectors engaging in deceptive billing practices, including billing for services not rendered, misrepresenting the amount owed, or failing to provide required financial assistance information.</p>

{_embed(mode="markup", title="How does your Indiana hospital bill compare to Medicare rates?", subtitle="Enter a CPT code and billed amount to see the Medicare benchmark and identify overcharges.")}

<h2 id="hospital-pricing">5. Hospital pricing in Indiana</h2>

<p>Indiana has some of the <strong>highest hospital prices in the Midwest</strong>. A 2024 RAND Corporation study found that Indiana hospitals charged commercial insurers an average of <strong>310% of Medicare rates</strong> &mdash; well above the national average of 254%. Some Indiana hospitals exceeded 400% of Medicare for common procedures.</p>

<p><strong>Pricing at major Indiana hospital systems (commercial rates as % of Medicare, 2024 data):</strong></p>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Avg. Commercial Rate (% of Medicare)</th><th>Notable</th></tr>
    </thead>
    <tbody>
        <tr><td>IU Health</td><td>340&ndash;380%</td><td>Largest IN system; dominant market share in Indianapolis</td></tr>
        <tr><td>Community Health Network</td><td>290&ndash;330%</td><td>Second largest; strong central Indiana presence</td></tr>
        <tr><td>Ascension St. Vincent</td><td>280&ndash;320%</td><td>Catholic nonprofit; extensive charity care programs</td></tr>
        <tr><td>Franciscan Health</td><td>260&ndash;310%</td><td>Southern/central Indiana; lower than state average</td></tr>
        <tr><td>Parkview Health (Fort Wayne)</td><td>270&ndash;320%</td><td>Dominant in northeast Indiana</td></tr>
        <tr><td>Deaconess Health (Evansville)</td><td>250&ndash;300%</td><td>Southwest Indiana; closest to national average</td></tr>
    </tbody>
</table>

<p><strong>Price transparency compliance:</strong> Under the federal Hospital Price Transparency Rule, all Indiana hospitals must publish machine-readable files of their negotiated rates and a consumer-friendly list of shoppable services. Compliance has been mixed &mdash; a 2025 CMS audit found that approximately 60% of Indiana hospitals were substantially compliant, while 40% had incomplete or difficult-to-access pricing files.</p>

<p>Use <a href="/calculator">BillKarma&rsquo;s cost calculator</a> to compare your Indiana hospital bill to Medicare rates and identify charges that exceed reasonable benchmarks.</p>

<h2 id="hip-2">6. HIP 2.0: Indiana&rsquo;s Healthy Indiana Plan</h2>

<p>Indiana&rsquo;s Medicaid expansion operates through <strong>HIP 2.0 (Healthy Indiana Plan)</strong>, a unique model that uses <strong>POWER accounts</strong> &mdash; similar to health savings accounts &mdash; where members make small monthly contributions. This structure directly affects how medical bills work for HIP enrollees.</p>

<p><strong>HIP 2.0 income thresholds and plan tiers:</strong></p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Individual Annual Income (2026)</th><th>Plan Tier</th><th>Monthly POWER Contribution</th><th>Copays</th></tr>
    </thead>
    <tbody>
        <tr><td>0&ndash;100% FPL</td><td>$0&ndash;$15,060</td><td>HIP Basic (no contribution) or HIP Plus (with contribution)</td><td>$0&ndash;$20</td><td>HIP Plus: minimal; HIP Basic: $4&ndash;$75 per service</td></tr>
        <tr><td>101&ndash;138% FPL</td><td>$15,061&ndash;$20,783</td><td>HIP Plus (contribution required)</td><td>$15&ndash;$27</td><td>Minimal (most services covered with no copay)</td></tr>
    </tbody>
</table>

<p><strong>How POWER accounts work:</strong></p>

<ul>
    <li>Members contribute <strong>2% of household income</strong> monthly (capped based on income tier)</li>
    <li>The state matches contributions into the POWER account</li>
    <li>POWER account funds are used to pay for the <strong>$2,500 annual deductible</strong></li>
    <li>Members who make all POWER contributions on time receive <strong>HIP Plus benefits</strong> &mdash; full coverage including dental and vision, with minimal copays</li>
    <li>Members below 100% FPL who do not contribute receive <strong>HIP Basic</strong> &mdash; more limited benefits, higher copays, and no dental or vision coverage</li>
    <li>Unused POWER account balances <strong>roll over</strong> year to year</li>
</ul>

<p><strong>What HIP 2.0 means for hospital billing:</strong></p>

<ul>
    <li>Hospitals must bill at <strong>Medicaid rates</strong> for HIP enrollees &mdash; typically 60&ndash;70% lower than commercial rates</li>
    <li>HIP Plus members owe <strong>minimal out-of-pocket costs</strong> for most services</li>
    <li>HIP Basic members may owe <strong>copays of $4&ndash;$75</strong> depending on the service</li>
    <li>Emergency department copays for <strong>non-emergency use</strong> can be up to $25 for HIP Plus and $75 for HIP Basic</li>
    <li>If a hospital bills you at commercial rates when you are HIP-enrolled, dispute immediately &mdash; you should only owe the Medicaid rate plus applicable copays</li>
</ul>

<p>To check eligibility or enroll, visit the <strong>Indiana Family and Social Services Administration (FSSA)</strong> website or call 1-877-438-4479. Many patients who qualify for HIP 2.0 do not realize they are eligible, especially after a job loss or income change.</p>

<h2 id="dispute">7. How to dispute an Indiana hospital bill</h2>

<p>Follow these steps to dispute an Indiana hospital bill effectively:</p>

<ol>
    <li><strong>Request an itemized bill.</strong> Indiana hospitals must provide a detailed breakdown of every charge. Do not accept a summary statement. Look for facility fees (especially at off-campus locations), duplicate charges, unbundled services, and charges for services not received.</li>
    <li><strong>Check for HB 1004 facility fee violations.</strong> If you were treated at an off-campus HOPD and billed a facility fee for E/M, imaging, or drug administration, that charge may violate Indiana law. Note the facility address, date of service, and the specific facility fee amount.</li>
    <li><strong>Compare charges to Medicare rates.</strong> Use <a href="/calculator">BillKarma&rsquo;s cost calculator</a> to benchmark each line item against Medicare rates. Indiana hospitals charge an average of 310% of Medicare &mdash; but charges above 400% are a strong basis for dispute.</li>
    <li><strong>Apply for financial assistance.</strong> If your income is below 400% FPL, request the hospital&rsquo;s Financial Assistance Policy and apply. You have at least 240 days from the first billing statement. Check <a href="/charity-care">charity care eligibility</a> requirements for your specific hospital.</li>
    <li><strong>Check HIP 2.0 eligibility.</strong> If your income is below 138% FPL, you may qualify for HIP 2.0. Enrollment can be retroactive up to 3 months, which means it could cover a recent hospital bill.</li>
    <li><strong>Send a written dispute letter.</strong> Address it to the hospital&rsquo;s Patient Financial Services department. Cite specific charges, reference applicable laws (HB 1004, No Surprises Act, 501(r) requirements), and request a written response within 30 days.</li>
    <li><strong>Escalate if needed.</strong> File complaints with:
        <ul>
            <li><strong>Indiana Department of Insurance</strong> &mdash; for facility fee violations, surprise billing, and insurance disputes</li>
            <li><strong>Indiana Attorney General, Consumer Protection Division</strong> &mdash; for deceptive billing practices</li>
            <li><strong>Indiana FSSA</strong> &mdash; for HIP 2.0 or Hoosier Healthwise billing disputes</li>
            <li><strong>CMS</strong> &mdash; for No Surprises Act violations and price transparency non-compliance</li>
        </ul>
    </li>
</ol>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Case Study 1: $480 facility fee refund under HB 1004 at IU Health off-campus clinic</h3>
    <p><strong>Situation:</strong> An Indianapolis patient visited an IU Health primary care clinic for a routine follow-up appointment (CPT 99214). The clinic was located in a strip mall three miles from the nearest IU Health hospital campus. The patient received two bills: a <strong>$185 physician fee</strong> and a <strong>$480 facility fee</strong> coded as a hospital outpatient department visit. Total billed: <strong>$665</strong> for a routine office visit.</p>
    <p><strong>Action:</strong> The patient identified the facility fee on the itemized bill and confirmed the clinic&rsquo;s off-campus location. She submitted a written dispute to IU Health citing Indiana HB 1004&rsquo;s prohibition on facility fees at off-campus HOPDs for evaluation and management services. She included the clinic address, the date of service, and a copy of the relevant statutory text.</p>
    <p><strong>Outcome:</strong> IU Health reversed the facility fee within 21 days and issued a <strong>$480 refund</strong>. The patient&rsquo;s final cost was the $185 physician fee, consistent with what an independent physician&rsquo;s office would charge. <strong>Savings: $480.</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 2: HIP 2.0 enrollment eliminated $12,400 emergency surgery bill</h3>
    <p><strong>Situation:</strong> A Terre Haute resident earning $14,800/year (98% FPL) underwent emergency appendectomy at a Community Health Network hospital. He was uninsured at the time of admission and received a bill for <strong>$12,400</strong> at commercial self-pay rates.</p>
    <p><strong>Action:</strong> A hospital financial counselor screened the patient for Medicaid eligibility during the post-discharge follow-up. The patient qualified for HIP 2.0 and enrolled through Indiana FSSA. Because HIP 2.0 allows <strong>retroactive coverage up to 3 months</strong>, the enrollment covered the date of the emergency surgery. The hospital rebilled at Medicaid rates.</p>
    <p><strong>Outcome:</strong> The $12,400 commercial bill was replaced with the Medicaid-rate bill of approximately $2,800, which was fully covered by HIP 2.0 minus a $25 ER copay. <strong>Patient&rsquo;s final cost: $25.</strong> Savings: $12,375.</p>
</div>

<div class="case-study">
    <h3>Case Study 3: Charity care at Ascension St. Vincent reduced $8,200 bill to $0</h3>
    <p><strong>Situation:</strong> A single mother in Fort Wayne with two children and an annual income of $28,000 (approximately 140% FPL) received an $8,200 bill from Ascension St. Vincent for a three-day hospital stay related to pneumonia. She had employer-sponsored insurance with a $5,000 deductible, and insurance paid $3,200 &mdash; leaving her responsible for <strong>$5,000</strong> (her full deductible).</p>
    <p><strong>Action:</strong> The patient applied to Ascension St. Vincent&rsquo;s financial assistance program. Ascension&rsquo;s published FAP offers full write-off of patient responsibility for families below 200% FPL and sliding-scale discounts up to 400% FPL. At 140% FPL, the patient qualified for a complete write-off of her out-of-pocket balance.</p>
    <p><strong>Outcome:</strong> Ascension St. Vincent applied financial assistance to eliminate the remaining <strong>$5,000 patient balance</strong>. The patient owed $0. <strong>Savings: $5,000.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Indiana ban facility fees at off-campus hospital outpatient departments?</h3>
        <p>Yes. Indiana House Bill 1004, signed in 2024, prohibits hospitals from charging facility fees at off-campus HOPDs for evaluation and management services, imaging, and drug administration. Hospitals must separately itemize any facility fee and provide written notice before billing one. If you received a facility fee at an off-campus clinic for a covered service, dispute the charge and file a complaint with the Indiana Department of Insurance.</p>
    </div>

    <div class="faq-item">
        <h3>What is HIP 2.0 and how does it affect my medical bills?</h3>
        <p>HIP 2.0 (Healthy Indiana Plan) is Indiana&rsquo;s Medicaid expansion program for adults 19&ndash;64 earning up to 138% FPL. It uses POWER accounts where members make small monthly contributions (2% of income). HIP Plus members who contribute get full benefits with minimal copays. HIP Basic members who do not contribute have higher copays and more limited benefits. If you qualify, hospitals must bill at Medicaid rates &mdash; typically 60&ndash;70% lower than commercial rates.</p>
    </div>

    <div class="faq-item">
        <h3>What is Indiana&rsquo;s statute of limitations on medical debt?</h3>
        <p>Indiana applies a 6-year SOL for written contracts (IC 34-11-2-11) and a 10-year SOL for promissory notes. Most hospital bills involve a signed financial responsibility form, so the 6-year period typically governs. After 6 years from the date of last payment or acknowledgment, the debt is time-barred. If a collector sues on expired debt, file a written Answer asserting the SOL defense. Never ignore a lawsuit summons &mdash; a default judgment can be entered regardless of whether the SOL has passed.</p>
    </div>

    <div class="faq-item">
        <h3>Can Indiana hospitals garnish my wages for medical debt?</h3>
        <p>Yes, after obtaining a court judgment. Under IC 24-4.5-5-105, the maximum garnishment is the lesser of 25% of disposable earnings or the amount above 30 times the federal minimum wage ($217.50/week). Social Security, disability, and certain retirement funds are exempt. Indiana&rsquo;s hospital lien law (IC 32-33-4) also allows hospitals to place a lien on personal injury settlement proceeds. Apply for financial assistance or negotiate before a lawsuit is filed to avoid reaching the judgment stage.</p>
    </div>

    <div class="faq-item">
        <h3>How do I file a complaint about an Indiana hospital billing error?</h3>
        <p>Submit a written dispute to the hospital&rsquo;s billing department citing specific charges and documentation. If unresolved, file with the Indiana Department of Insurance for facility fee violations and insurance disputes, the Indiana Attorney General&rsquo;s Consumer Protection Division for deceptive billing, or Indiana FSSA for HIP 2.0 and Hoosier Healthwise issues. For No Surprises Act violations, file with CMS. Document every communication in writing and keep copies of all bills and correspondence.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://iga.in.gov/legislative/2024/bills/house/1004" target="_blank" rel="noopener">Indiana General Assembly &mdash; House Bill 1004 (2024): Hospital Facility Fee Restrictions</a></li>
    <li><a href="https://www.in.gov/fssa/hip/" target="_blank" rel="noopener">Indiana Family and Social Services Administration &mdash; Healthy Indiana Plan (HIP 2.0)</a></li>
    <li><a href="https://iga.in.gov/laws/2024/ic/titles/34#34-11-2-11" target="_blank" rel="noopener">Indiana Code IC 34-11-2-11 &mdash; Statute of Limitations for Written Contracts</a></li>
    <li><a href="https://iga.in.gov/laws/2024/ic/titles/24#24-4.5-5-105" target="_blank" rel="noopener">Indiana Code IC 24-4.5-5-105 &mdash; Wage Garnishment Limitations</a></li>
    <li><a href="https://iga.in.gov/laws/2024/ic/titles/32#32-33-4" target="_blank" rel="noopener">Indiana Code IC 32-33-4 &mdash; Hospital Lien Law</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS &mdash; No Surprises Act: Balance Billing Protections for Patients</a></li>
    <li><a href="https://www.rand.org/health-care/projects/hospital-pricing.html" target="_blank" rel="noopener">RAND Corporation &mdash; Hospital Price Transparency and Commercial vs. Medicare Rate Analysis</a></li>
    <li><a href="https://www.in.gov/attorneygeneral/consumer-protection-division/" target="_blank" rel="noopener">Indiana Attorney General &mdash; Consumer Protection Division</a></li>
    <li><a href="https://www.in.gov/idoi/" target="_blank" rel="noopener">Indiana Department of Insurance &mdash; File a Complaint</a></li>
</ul>
""",
})
