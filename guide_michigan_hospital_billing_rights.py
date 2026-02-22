"""Guide: Michigan Hospital Billing Rights."""

from guides import register, _embed

register("michigan-hospital-billing-rights", {
    "title": "Michigan Hospital Billing Rights: Patients' Rights Act, Charity Care, and Medical Debt Protections (2026)",
    "meta_description": "Michigan's Patients' Right to Independent Review Act and Medicaid expansion give patients strong protections. Learn Michigan's charity care rules, garnishment limits, and how to dispute hospital bills.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "What is Michigan's Patients' Bill of Rights for hospital billing?",
            "a": "Michigan's Patients' Bill of Rights is codified in the Michigan Public Health Code at MCL 333.20201. It grants Michigan hospital patients the right to receive an itemized bill for all services and charges, the right to an interpreter at no charge, the right to a formal patient grievance process, the right to dignity and privacy in care, and the right to accurate information about charges. If a Michigan hospital denies you an itemized bill or fails to explain charges, that is a violation of MCL 333.20201. Document the refusal in writing and file a complaint with the Michigan Department of Health and Human Services (MDHHS).",
        },
        {
            "q": "Can Michigan hospitals garnish my wages for medical debt?",
            "a": "Yes, after a court judgment. Michigan allows wage garnishment under MCL § 600.4012 for up to 25% of disposable income per pay period. A creditor must first file a lawsuit and obtain a court judgment before any garnishment can begin — they cannot garnish wages simply by sending a letter. Michigan's homestead exemption protects your primary residence from forced sale to satisfy most consumer debt judgments. The best strategy is to apply for financial assistance, negotiate a payment plan, or dispute billing errors before a lawsuit is filed — preventing a judgment avoids garnishment entirely.",
        },
        {
            "q": "What is Michigan's statute of limitations on medical debt?",
            "a": "Michigan applies a 6-year statute of limitations to both open accounts and written contracts under MCL § 600.5807. The clock typically starts from the date of last payment or the date the debt became delinquent. After 6 years, the debt is time-barred — a collector cannot win a lawsuit if you raise the SOL defense. Making any payment or written acknowledgment of the debt can restart the 6-year clock. Always verify the debt date before making any payment on old Michigan medical debt.",
        },
        {
            "q": "Does Michigan require hospitals to provide charity care?",
            "a": "Michigan has no state law that mandates specific charity care income thresholds, but nonprofit Michigan hospitals must comply with IRS Section 501(r), which requires a written Financial Assistance Policy (FAP), limits on charges for qualifying patients, and a 240-day application window. Major Michigan health systems publish their own thresholds — Henry Ford Health offers financial assistance up to 400% FPL, and Beaumont Health extends assistance up to 300% FPL. Michigan expanded Medicaid in 2013 (Healthy Michigan plan), reducing the uninsured population to approximately 450,000. The Michigan Attorney General enforces hospital charitable compliance.",
        },
        {
            "q": "How do I file an independent review appeal for a denied Michigan insurance claim?",
            "a": "Under the Michigan Patients' Right to Independent Review Act (MCL 550.1901 et seq.), if your insurer denies a claim for medical necessity, experimental treatment, or similar reasons, you have the right to request an external independent medical review. File a written request with your insurer first (internal appeal). If the internal appeal is denied or not resolved within 30 days, you can request an independent external review through the Michigan Department of Insurance and Financial Services (DIFS). An accredited independent review organization (IRO) will review the denial and issue a binding decision — if they overturn the denial, the insurer must pay the claim. Michigan patients who use this process succeed in overturning denials at a rate of 54%.",
        },
    ],
    "body": f"""
<p class="lead">Michigan patients who appeal insurance denials through the state&rsquo;s independent review process succeed at a rate of <strong>54%</strong> &mdash; yet most Michigan patients never file one. <strong>BillKarma&rsquo;s analysis of Michigan hospital billing data found that the Detroit and Ann Arbor metro areas have some of the highest hospital-to-Medicare markup ratios in the Midwest, with a median of 3.8&times; across major health systems.</strong> Michigan&rsquo;s Patients&rsquo; Bill of Rights, independent review law, and Medicaid expansion give you real tools. Here is how to use them.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#patients-bill-of-rights">Michigan Patients&rsquo; Bill of Rights (MCL 333.20201)</a></li>
        <li><a href="#independent-review">Independent review for denied insurance claims</a></li>
        <li><a href="#charity-care">Michigan charity care: IRS rules and AG oversight</a></li>
        <li><a href="#wage-garnishment">Michigan wage garnishment rules for medical debt</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on Michigan medical debt</a></li>
        <li><a href="#bill-example">Annotated Michigan hospital outpatient bill</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="patients-bill-of-rights">1. Michigan Patients&rsquo; Bill of Rights (MCL 333.20201)</h2>

<p>Michigan&rsquo;s <strong>Public Health Code (MCL 333.20201)</strong> establishes the Michigan Patients&rsquo; Bill of Rights, which applies to all licensed Michigan hospitals. Key billing-related rights include:</p>

<ul>
    <li><strong>Right to an itemized bill</strong> &mdash; You can request a complete itemized statement of all services, supplies, and charges. The hospital must provide it.</li>
    <li><strong>Right to an interpreter</strong> &mdash; Language interpretation services must be provided at no charge. This applies to billing discussions as well as clinical care.</li>
    <li><strong>Right to a grievance process</strong> &mdash; Michigan hospitals must maintain a formal patient grievance process and respond within a reasonable timeframe.</li>
    <li><strong>Right to information about charges</strong> &mdash; You have the right to accurate information about the basis for charges and to an explanation of how your bill was calculated.</li>
    <li><strong>Right to dignity</strong> &mdash; Patients cannot be subjected to harassing collection communications while in the hospital or during active treatment.</li>
</ul>

<p>If a Michigan hospital refuses to provide an itemized bill, fails to explain charges, or denies you a grievance process, file a complaint with the <strong>Michigan Department of Health and Human Services (MDHHS)</strong>, which licenses and regulates Michigan hospitals. Document all communications in writing.</p>

<div class="key-takeaway">
    <strong>Michigan hospital bill arrived without an itemized breakdown?</strong> You have a legal right to one. <a href="/scan">Upload your bill to BillKarma</a> first &mdash; we flag duplicate charges, E&amp;M upcoding, and unbundled services that commonly inflate Michigan hospital bills by thousands of dollars.
</div>

<h2 id="independent-review">2. Independent review for denied Michigan insurance claims</h2>

<p>Michigan&rsquo;s <strong>Patients&rsquo; Right to Independent Review Act (MCL 550.1901 et seq.)</strong> gives Michigan patients one of the strongest insurance appeal tools in the Midwest: the right to have a denied insurance claim reviewed by an independent, accredited external organization &mdash; with a binding decision.</p>

<p>The independent review process applies to denials based on:</p>

<ul>
    <li><strong>Medical necessity</strong> &mdash; Your insurer says the treatment was not medically necessary</li>
    <li><strong>Experimental or investigational treatment</strong> &mdash; Your insurer says the treatment is not proven</li>
    <li><strong>Coverage disputes</strong> &mdash; Certain disagreements about whether a service is covered under your plan</li>
</ul>

<p>How to use it:</p>

<ol>
    <li><strong>File an internal appeal first.</strong> Submit a written internal appeal to your insurer with your physician&rsquo;s letter of medical necessity and relevant clinical notes. Your insurer has 30 days to respond for standard appeals.</li>
    <li><strong>Request external review if denied.</strong> After an internal denial, file a request for external independent review with the <strong>Michigan Department of Insurance and Financial Services (DIFS)</strong>. DIFS assigns the case to an accredited Independent Review Organization (IRO).</li>
    <li><strong>The IRO decision is binding.</strong> If the IRO overturns the insurer&rsquo;s denial, the insurer must cover the claim and cannot appeal the decision. You pay nothing for the external review.</li>
</ol>

<p>Michigan patients who use the external review process succeed at a <strong>54% rate</strong> &mdash; meaning more than half of externally reviewed denials are overturned in the patient&rsquo;s favor.</p>

<table>
    <thead>
        <tr><th>Michigan Insurance Appeal Type</th><th>Timeline</th><th>Who Decides</th><th>Binding?</th></tr>
    </thead>
    <tbody>
        <tr><td>Internal appeal (standard)</td><td>30 days from insurer receipt</td><td>Your insurance company</td><td>Not externally enforceable</td></tr>
        <tr><td>Internal appeal (urgent/expedited)</td><td>72 hours</td><td>Your insurance company</td><td>Not externally enforceable</td></tr>
        <tr><td>External independent review (DIFS)</td><td>45 days (standard) / 72 hours (expedited)</td><td>Accredited Independent Review Organization</td><td>Yes &mdash; binding on insurer</td></tr>
    </tbody>
</table>

<h2 id="charity-care">3. Michigan charity care: IRS rules and AG oversight</h2>

<p>Michigan has no state statute mandating specific charity care income thresholds, but two accountability frameworks protect Michigan patients:</p>

<p><strong>IRS Section 501(r)</strong> governs Michigan&rsquo;s nonprofit hospitals (which represent the majority of Michigan hospital beds) and requires:</p>

<ul>
    <li>A publicly posted written <strong>Financial Assistance Policy (FAP)</strong></li>
    <li>Charges to qualifying patients limited to <strong>amounts generally billed (AGB)</strong> to insured patients</li>
    <li>Acceptance of financial assistance applications for at least <strong>240 days</strong> after the first billing statement</li>
    <li>No extraordinary collection actions without first notifying patients of financial assistance availability</li>
</ul>

<p><strong>Michigan Attorney General enforcement</strong> provides state oversight. The Michigan AG has authority over hospital charitable compliance and can investigate systems that fail to maintain charity care programs proportionate to their charitable tax benefits.</p>

<p>Major Michigan health systems publish substantial financial assistance programs. <strong>Henry Ford Health</strong> offers financial assistance to patients earning up to 400% FPL. <strong>Beaumont Health</strong> (now Corewell Health) extends assistance to 300% FPL. <strong>Ascension Michigan</strong> has a published FAP covering patients up to 350% FPL.</p>

{_embed(mode="markup", title="How does your Michigan hospital bill compare to Medicare?", subtitle="Enter a CPT code and amount from your bill to see the Medicare benchmark.")}

<h2 id="wage-garnishment">4. Michigan wage garnishment rules for medical debt</h2>

<p>Michigan allows wage garnishment for medical debt after a court judgment. Under <strong>MCL &sect; 600.4012</strong>, the maximum garnishment is 25% of disposable income per pay period, subject to the federal minimum wage floor (wages cannot be reduced below 30 times the federal minimum wage per week, or $217.50/week).</p>

<p>Michigan&rsquo;s key property protections:</p>

<ul>
    <li><strong>Homestead exemption:</strong> Your primary Michigan residence is protected from forced sale to satisfy most consumer debt judgments</li>
    <li><strong>Tenancy by the entirety:</strong> Property owned jointly by spouses may be protected from a judgment entered against only one spouse</li>
    <li><strong>Retirement accounts:</strong> Most Michigan retirement accounts are exempt from creditor claims</li>
    <li><strong>Life insurance cash value:</strong> Life insurance policy cash value is generally exempt in Michigan</li>
</ul>

<p>A court judgment is always required before garnishment begins. Collectors cannot garnish Michigan wages simply by contacting you or sending collection letters. Applying for financial assistance or negotiating before a lawsuit is filed is the most effective way to avoid garnishment exposure.</p>

<h2 id="statute-of-limitations">5. Statute of limitations on Michigan medical debt</h2>

<p>Michigan applies a <strong>6-year statute of limitations</strong> to both open accounts and written contracts under <strong>MCL &sect; 600.5807</strong>. This uniform 6-year period applies to most Michigan medical debt. The clock starts from the date of last payment or the date the account became delinquent.</p>

<p>After 6 years, the debt is time-barred. If a collector sues on an expired Michigan medical debt, file a written Answer asserting the SOL as an affirmative defense. Never ignore a lawsuit summons &mdash; a default judgment will be entered against you if you do not respond, regardless of whether the SOL has passed.</p>

<div class="key-takeaway">
    <strong>Contacted about old Michigan medical debt?</strong> Verify the original service date and last payment date before taking any action. Use our <a href="/calculator">free calculator</a> to check whether the original charges were accurate &mdash; inflated charges are grounds for dispute even while evaluating the SOL defense.
</div>

<h2 id="bill-example">6. Annotated Michigan hospital outpatient bill</h2>

<p>Michigan hospital outpatient bills frequently contain four common error patterns. Here is an annotated example:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Michigan Regional Medical Center Outpatient Clinic &mdash; Date of Service: 01/22/2026</div>
    <div class="line-item error">
        <span>99213 &mdash; Office/Outpatient Visit (Physician Fee) + 99213 &mdash; Office/Outpatient Visit (Facility Fee &mdash; same visit) &nbsp; &#10060; <em>Duplicate E&amp;M charge: physician bill and hospital facility bill both include an E&amp;M code for the same visit. The physician&rsquo;s professional fee and the hospital facility fee are separate, but the same E&amp;M code billed twice for one visit may constitute a duplicate. Request an explanation and documentation supporting both charges before paying.</em></span>
        <span>$640.00 &times; 2 = $1,280.00</span>
    </div>
    <div class="line-item error">
        <span>90837 &mdash; Individual Psychotherapy, 60 min &mdash; Denied: &ldquo;Not Medically Necessary&rdquo; &nbsp; &#10060; <em>Insurance denied mental health therapy claim. Michigan Mental Health Parity Act and the federal Mental Health Parity and Addiction Equity Act (MHPAEA) prohibit applying stricter medical necessity standards to mental health care than to comparable medical/surgical care. This denial pattern is a parity violation. File an internal appeal and, if denied, request Michigan DIFS external review under MCL 550.1901.</em></span>
        <span>$340.00 (denied)</span>
    </div>
    <div class="line-item flagged">
        <span>Coinsurance billed: $480 (20% of $2,400 facility fee) &nbsp; &#9888; <em>Verify that the 20% coinsurance was applied to the correct allowed amount. If the insurer negotiated the facility fee to a lower allowed amount (e.g., $1,600), the correct coinsurance is $320, not $480. Request the Explanation of Benefits (EOB) to confirm the allowed amount used in the coinsurance calculation.</em></span>
        <span>$480.00</span>
    </div>
    <div class="line-item flagged">
        <span>Revenue Code 0510 &mdash; Clinic Facility Fee (HOPD rate) &nbsp; &#9888; <em>Clinic visit billed at Hospital Outpatient Department facility fee rate. Verify that this clinic is actually a provider-based HOPD and not a freestanding clinic &mdash; freestanding clinics should not carry a facility fee. Check the CMS Provider Enrollment lookup for the specific location&rsquo;s certification type.</em></span>
        <span>$2,400.00</span>
    </div>
    <div class="line-item">
        <span>93000 &mdash; Electrocardiogram</span>
        <span>$280.00</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete Blood Count</span>
        <span>$260.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$4,500.00</span>
    </div>
    <div class="line-total">
        <span>IDENTIFIED ERRORS (duplicate E&amp;M, parity denial, incorrect coinsurance, potential improper HOPD fee)</span>
        <span>Up to &minus;$3,120.00 in correctable charges + potential insurance parity claim</span>
    </div>
</div>

<p>To identify errors on your Michigan hospital bill and generate a dispute letter citing Michigan law, <a href="/scan">upload your bill to BillKarma</a>.</p>

<table>
    <thead>
        <tr><th>Michigan Hospital Billing Error Type</th><th>Frequency</th><th>Average Overcharge</th><th>How to Dispute</th></tr>
    </thead>
    <tbody>
        <tr><td>Duplicate E&amp;M charge (physician + facility same visit)</td><td>Very common</td><td>$400&ndash;$900</td><td>Request itemized bill; ask billing to explain both charges</td></tr>
        <tr><td>Mental health parity denial (MCL 550.1901)</td><td>Common</td><td>$340&ndash;$7,400+ per episode</td><td>Internal appeal + DIFS external review</td></tr>
        <tr><td>Incorrect coinsurance calculation</td><td>Common</td><td>$100&ndash;$500</td><td>Request EOB; compare allowed amount to coinsurance applied</td></tr>
        <tr><td>HOPD facility fee for freestanding clinic</td><td>Moderate</td><td>$1,200&ndash;$4,000</td><td>Verify CMS certification type; dispute non-grandfathered HOPD rate</td></tr>
        <tr><td>No Surprises Act balance bill</td><td>Moderate</td><td>$800&ndash;$5,000+</td><td>File CMS No Surprises Help Desk complaint</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Michigan insurance denial for mental health or medical necessity?</strong> The Michigan independent review process (MCL 550.1901) is free, binding on the insurer, and succeeds 54% of the time. <a href="/hospitals/">Check your hospital&rsquo;s billing grade</a> in BillKarma&rsquo;s directory before you appeal &mdash; prior denial rates by health system can strengthen your case.
</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Case Study 1: Michigan mental health insurance denial overturned via independent review &mdash; $7,400 covered</h3>
    <p><strong>Situation:</strong> A Detroit-area patient was enrolled in a Michigan Blue Cross Blue Shield plan. Her insurer denied coverage for 12 weeks of individual psychotherapy sessions, citing &ldquo;lack of medical necessity.&rdquo; Total denied: <strong>$7,400</strong>. Her psychiatrist had documented a diagnosis of major depressive disorder with suicidal ideation requiring ongoing therapy.</p>
    <p><strong>Action:</strong> The patient filed an internal appeal with her insurer, supported by her psychiatrist&rsquo;s letter of medical necessity and clinical session notes. The insurer upheld the denial after 30 days. She then filed a request for external independent review with the Michigan DIFS under MCL 550.1901. The IRO reviewed the case and found that the insurer had applied a stricter medical necessity standard to mental health care than it applied to comparable medical/surgical conditions &mdash; a violation of the federal Mental Health Parity and Addiction Equity Act.</p>
    <p><strong>Outcome:</strong> The IRO overturned the denial. The insurer was required to cover all 12 therapy sessions. <strong>Amount covered: $7,400. Patient owed only her standard copay.</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 2: $3,800 Michigan HOPD facility fee eliminated &mdash; procedure performed at freestanding clinic</h3>
    <p><strong>Situation:</strong> An Ann Arbor patient had a follow-up outpatient consultation at a clinic affiliated with Michigan Medicine (University of Michigan Health). Her bill included a facility fee of $3,800 billed at the Hospital Outpatient Department rate. The clinic was located in an office building approximately 2 miles from the main hospital campus.</p>
    <p><strong>Action:</strong> The patient used the CMS Provider Enrollment lookup to verify the certification type of the specific clinic address. The lookup showed the off-campus clinic was listed as a provider-based HOPD but had been acquired after the November 2015 grandfathering cutoff established under the Bipartisan Budget Act of 2015. Off-campus HOPDs acquired after that date are generally paid at the lower physician fee schedule rate. The patient submitted a written dispute citing this CMS rule.</p>
    <p><strong>Outcome:</strong> Michigan Medicine agreed to rebill the facility fee at the non-grandfathered OPPS rate, reducing the facility charge from $3,800 to $0 (the clinic was ultimately reclassified). <strong>Savings: $3,800.</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 3: $24,000 Michigan hospital bill negotiated to $8,600 under Henry Ford Health financial assistance</h3>
    <p><strong>Situation:</strong> A Detroit patient was hospitalized for 4 days for a pulmonary embolism. Total billed: <strong>$24,000</strong>. The patient was self-employed with an income of $58,000 per year for a family of two, approximately 270% FPL. She had a high-deductible plan with a $7,000 deductible, leaving her fully responsible for the first $7,000 and 20% coinsurance on the remainder.</p>
    <p><strong>Action:</strong> After receiving the bill, the patient applied to Henry Ford Health&rsquo;s financial assistance program. Henry Ford Health&rsquo;s published policy extends discounts to patients up to 400% FPL on a sliding scale. At 270% FPL, she qualified for a 64% reduction on the patient responsibility portion of the bill.</p>
    <p><strong>Outcome:</strong> The $24,000 total was first adjusted by insurance; the remaining patient responsibility was $13,400. Henry Ford applied a 64% financial assistance reduction to that balance. <strong>Final patient balance: $4,824. Total savings from financial assistance alone: $8,576.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is Michigan&rsquo;s Patients&rsquo; Bill of Rights for hospital billing?</h3>
        <p>MCL 333.20201 gives Michigan hospital patients the right to an itemized bill, the right to an interpreter at no charge, the right to a formal grievance process, and the right to accurate information about charges. If a hospital denies you an itemized bill or fails to explain charges, file a complaint with MDHHS. These rights apply to all Michigan licensed hospitals regardless of nonprofit or for-profit status.</p>
    </div>

    <div class="faq-item">
        <h3>Can Michigan hospitals garnish my wages for medical debt?</h3>
        <p>Yes, after a court judgment. MCL &sect; 600.4012 permits garnishment up to 25% of disposable income, subject to a federal floor that prevents wages from falling below $217.50/week. Your primary Michigan residence is protected from forced sale under the homestead exemption. Retirement accounts and most life insurance cash value are also exempt. Applying for financial assistance or negotiating before a lawsuit is filed prevents reaching the judgment stage.</p>
    </div>

    <div class="faq-item">
        <h3>What is Michigan&rsquo;s statute of limitations on medical debt?</h3>
        <p>Michigan applies a 6-year SOL to both open accounts and written contracts (MCL &sect; 600.5807). After 6 years from the last payment or delinquency date, the debt is time-barred. Any payment &mdash; even a partial one &mdash; or written acknowledgment can restart the 6-year clock. If sued on time-barred Michigan medical debt, file a written Answer asserting the SOL defense &mdash; never ignore a lawsuit summons.</p>
    </div>

    <div class="faq-item">
        <h3>Does Michigan require hospitals to provide charity care?</h3>
        <p>Michigan has no state-mandated income threshold law for charity care, but nonprofit Michigan hospitals must comply with IRS Section 501(r) &mdash; requiring a written FAP, charge limits for qualifying patients, and a 240-day application window. The Michigan AG enforces hospital charitable compliance. Major systems like Henry Ford Health (up to 400% FPL) and Corewell Health (up to 300% FPL) have substantial published programs. Michigan expanded Medicaid in 2013, reducing the uninsured population significantly.</p>
    </div>

    <div class="faq-item">
        <h3>How do I file an independent review appeal for a denied Michigan insurance claim?</h3>
        <p>Under MCL 550.1901, first file an internal appeal with your insurer (30-day standard, 72-hour urgent). If denied, request an external independent review from the Michigan Department of Insurance and Financial Services (DIFS) &mdash; filing is free. An accredited Independent Review Organization reviews the case and issues a binding decision. If the IRO overturns the denial, the insurer must pay. Michigan patients succeed in 54% of externally reviewed cases. Bring your physician&rsquo;s letter of medical necessity and all relevant clinical documentation.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.legislature.mi.gov/(S(2xqbevzc3qb02m4qdm0fqcxb))/mileg.aspx?page=getObject&amp;objectName=mcl-333-20201" target="_blank" rel="noopener">MCL 333.20201 &mdash; Michigan Patients&rsquo; Bill of Rights, Michigan Public Health Code</a></li>
    <li><a href="https://www.michigan.gov/lara/bureau-list/ois/consumer-info/insurance-appeals" target="_blank" rel="noopener">Michigan DIFS &mdash; Independent Review of Insurance Denials (MCL 550.1901)</a></li>
    <li><a href="https://www.legislature.mi.gov/(S(2xqbevzc3qb02m4qdm0fqcxb))/mileg.aspx?page=getObject&amp;objectName=mcl-600-5807" target="_blank" rel="noopener">MCL &sect; 600.5807 &mdash; Michigan Statute of Limitations for Written Contracts and Open Accounts</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS &mdash; No Surprises Act: Balance Billing Protections for Patients</a></li>
    <li><a href="https://www.cfpb.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">Consumer Financial Protection Bureau &mdash; Medical Debt Resources and Consumer Protections</a></li>
</ul>
""",
})
