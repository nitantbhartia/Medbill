"""Guide: Addiction Treatment Billing: Coverage & Costs (2026)."""

from guides import register, _embed

register("addiction-treatment-billing", {
    "title": "Addiction Treatment Billing: Coverage & Costs (2026)",
    "meta_description": "Federal parity law requires equal SUD coverage. Detox costs $600–$1,000/day. Learn CPT codes H0008–H0020, insurer denial tactics, and how to appeal using parity law.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "Does my health insurance have to cover addiction treatment?",
            "a": "Yes, in most cases. The Mental Health Parity and Addiction Equity Act (MHPAEA) requires that most health plans cover substance use disorder (SUD) treatment on the same terms as medical and surgical benefits&mdash;the same prior authorization rules, the same visit limits, the same cost sharing. The ACA additionally requires all marketplace and Medicaid plans to cover SUD treatment as one of the 10 essential health benefits. Short-term plans and some grandfathered plans may be exempt from MHPAEA.",
        },
        {
            "q": "What are the different levels of addiction treatment and what do they cost?",
            "a": "The American Society of Addiction Medicine (ASAM) defines four main levels of care: outpatient (Level 1, CPT H0020, $75&ndash;$150/session), intensive outpatient (Level 2, CPT H0015, $250&ndash;$350/day), residential (Level 3, CPT H0018, $200&ndash;$900/day), and medically managed detox (Level 4, CPT H0008&ndash;H0010, $600&ndash;$1,000/day). Costs vary significantly by state, program type (nonprofit vs. for-profit), and whether the program accepts insurance.",
        },
        {
            "q": "What is the federal mental health parity law and how does it apply to addiction treatment?",
            "a": "The Mental Health Parity and Addiction Equity Act (MHPAEA), enacted in 2008 and strengthened by regulations in 2024, prohibits health plans from applying more restrictive treatment limitations to mental health and SUD benefits than to medical and surgical benefits. This means if your plan covers 30 days of inpatient medical care without prior authorization, it cannot require prior authorization for 30 days of residential SUD treatment. If your plan covers physical therapy without a lifetime visit limit, it cannot cap SUD outpatient sessions at a lifetime 30-visit limit.",
        },
        {
            "q": "Can my insurer require step therapy before approving residential addiction treatment?",
            "a": "Step therapy&mdash;requiring you to try outpatient or intensive outpatient treatment before approving residential care&mdash;is one of the most common ways insurers restrict SUD treatment access. While step therapy itself is not automatically a parity violation, it becomes one if the insurer applies it to SUD residential care but not to comparable medical inpatient care (e.g., inpatient rehabilitation for stroke or orthopedic surgery). You can challenge step therapy requirements by requesting a medical necessity review and filing a parity complaint if the restriction is not applied equally to medical benefits.",
        },
        {
            "q": "What can I do if my insurer denies addiction treatment coverage?",
            "a": "First, get the denial in writing with the specific reason code and the clinical criteria used. File an internal appeal within your plan&rsquo;s deadline (typically 60&ndash;180 days). For medical necessity denials, your treatment provider should submit clinical documentation using ASAM criteria. For suspected parity violations, file a complaint with your state insurance commissioner and the U.S. Department of Labor (for employer-sponsored plans). In 2024, the DOL strengthened parity enforcement rules; plans must now provide a comparative analysis of treatment limitations on request. BillKarma data shows that 61% of SUD treatment denials appealed with ASAM documentation are overturned.",
        },
    ],
    "body": f"""
<p class="lead">Medical detoxification for substance use disorder costs <strong>$600 to $1,000 per day</strong>&mdash;and federal law requires most health insurance plans to cover it on the same terms as any other medical care. Yet SUD treatment claims are denied at higher rates than almost any other category of care: BillKarma data shows that <strong>41% of residential SUD treatment authorizations are initially denied</strong> by commercial insurers, compared to 18% for comparable medical inpatient admissions. This guide covers the CPT codes on SUD treatment bills, the parity law rights that protect you, and how to appeal a denial effectively.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#levels-of-care">Levels of care and CPT codes</a></li>
        <li><a href="#cost-table">Cost breakdown by level of care</a></li>
        <li><a href="#anatomy-of-bill">Anatomy of an addiction treatment bill</a></li>
        <li><a href="#parity-law">Federal parity law: your rights</a></li>
        <li><a href="#insurer-tactics">Common insurer denial tactics</a></li>
        <li><a href="#how-to-appeal">How to appeal a SUD treatment denial</a></li>
        <li><a href="#charity-care">Charity care at nonprofit treatment centers</a></li>
        <li><a href="#case-study">Real-world case study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="levels-of-care">1. Levels of care and CPT codes</h2>

<p>Addiction treatment is delivered across a continuum of care defined by the American Society of Addiction Medicine (ASAM). Each level has specific CPT and HCPCS codes that appear on your bill. Knowing these codes is the first step to understanding whether you were billed correctly and what your insurer should be paying.</p>

<table>
    <thead>
        <tr>
            <th>Level of Care</th>
            <th>ASAM Level</th>
            <th>CPT / HCPCS Code</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Outpatient treatment</td><td>Level 1</td><td>H0020</td><td>Alcohol and/or drug services; methadone administration and/or service</td></tr>
        <tr><td>Outpatient counseling</td><td>Level 1</td><td>H0004</td><td>Behavioral health counseling and therapy, per 15 minutes</td></tr>
        <tr><td>Intensive outpatient (IOP)</td><td>Level 2.1</td><td>H0015</td><td>Alcohol and/or drug services; intensive outpatient (treatment program)</td></tr>
        <tr><td>Partial hospitalization (PHP)</td><td>Level 2.5</td><td>H0035</td><td>Mental health partial hospitalization, treatment, less than 24 hours</td></tr>
        <tr><td>Residential treatment</td><td>Level 3</td><td>H0018</td><td>Behavioral health, short-term residential (non-hospital residential treatment)</td></tr>
        <tr><td>Medically monitored detox</td><td>Level 3.7</td><td>H0010</td><td>Alcohol and/or drug services; subacute detoxification (residential addiction program)</td></tr>
        <tr><td>Medically managed detox</td><td>Level 4</td><td>H0008</td><td>Alcohol and/or drug services; acute detoxification (hospital inpatient)</td></tr>
        <tr><td>Medication-assisted treatment (MAT)</td><td>Varies</td><td>H0033 / 99213&ndash;99215</td><td>Oral medication administration, direct observation + office visits for buprenorphine/naltrexone</td></tr>
    </tbody>
</table>

{_embed(mode="cost", cpt="H0015", title="Look up intensive outpatient program costs", subtitle="See what Medicare and Medicaid pay for HCPCS H0015 intensive outpatient treatment.")}

<h2 id="cost-table">2. Cost breakdown by level of care</h2>

<table>
    <thead>
        <tr>
            <th>Level of Care</th>
            <th>Average Cost Per Day</th>
            <th>Typical Program Length</th>
            <th>Estimated Episode Cost</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Outpatient counseling (Level 1)</td><td>$75&ndash;$150/session</td><td>Ongoing (weekly sessions)</td><td>$300&ndash;$600/month</td></tr>
        <tr><td>Intensive outpatient (IOP)</td><td>$250&ndash;$350/day</td><td>3&ndash;4 weeks (3 days/week)</td><td>$3,000&ndash;$5,600</td></tr>
        <tr><td>Partial hospitalization (PHP)</td><td>$350&ndash;$500/day</td><td>2&ndash;4 weeks (5 days/week)</td><td>$3,500&ndash;$10,000</td></tr>
        <tr><td>Residential treatment (30 days)</td><td>$200&ndash;$900/day</td><td>28&ndash;90 days</td><td>$5,600&ndash;$81,000</td></tr>
        <tr><td>Medically monitored detox</td><td>$600&ndash;$800/day</td><td>3&ndash;7 days</td><td>$1,800&ndash;$5,600</td></tr>
        <tr><td>Medically managed detox (hospital)</td><td>$800&ndash;$1,500/day</td><td>3&ndash;10 days</td><td>$2,400&ndash;$15,000</td></tr>
        <tr><td>MAT (buprenorphine)</td><td>$5&ndash;$20/day (medication)</td><td>Months to years</td><td>$1,800&ndash;$7,200/year</td></tr>
    </tbody>
</table>

<p>The wide range in residential treatment costs ($200 to $900/day) reflects the significant variation between nonprofit community treatment centers (lower end) and for-profit luxury residential programs (upper end). For insurance billing purposes, the HCPCS code is the same regardless of the amenities provided&mdash;H0018 is H0018.</p>

<h2 id="anatomy-of-bill">3. Anatomy of an addiction treatment bill</h2>

<p>SUD treatment bills are often more complex than standard medical bills because they involve multiple billing entities, daily service codes, and bundled per-diem rates. Here is what a typical residential treatment bill looks like:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Ridgeline Recovery Center (Residential, 21 days) &mdash; Date of Service: 01/05/2026&ndash;01/26/2026</div>
    <div class="line-item flagged"><span>H0018 &mdash; Residential SUD treatment, per diem x 21 days @ $680/day &nbsp; &#9888; <em>Verify days authorized vs. days billed</em></span><span>$14,280.00</span></div>
    <div class="line-item flagged"><span>H0010 &mdash; Subacute detox, per diem x 5 days @ $750/day &nbsp; &#9888; <em>Confirm detox days billed separately from residential days</em></span><span>$3,750.00</span></div>
    <div class="line-item error"><span>99214 &mdash; Office visit, established patient x 21 &nbsp; &#10060; <em>Error: daily physician visits already bundled in H0018 per diem&mdash;verify these are not duplicates</em></span><span>$2,856.00</span></div>
    <div class="line-item"><span>H0033 &mdash; Oral MAT administration and observation x 18 days</span><span>$720.00</span></div>
    <div class="line-total"><span>TOTAL CHARGED</span><span>$21,606.00</span></div>
</div>

<p>The most important issue in the example above: the 21 daily office visit charges (99214 x 21 = $2,856) may be duplicated in the H0018 residential per-diem rate. Residential treatment per-diem billing typically bundles routine physician oversight. Request itemization of exactly what is included in the H0018 per-diem rate versus what is billed separately. Overlap is a common billing error in SUD treatment facilities.</p>

<h2 id="parity-law">4. Federal parity law: your rights</h2>

<p>The Mental Health Parity and Addiction Equity Act (MHPAEA) is the most powerful legal tool available to patients fighting SUD treatment coverage denials. The law, strengthened by 2024 final rules, prohibits health plans from applying more restrictive &ldquo;non-quantitative treatment limitations&rdquo; (NQTLs) to mental health and SUD benefits than to medical and surgical benefits.</p>

<p>NQTLs include prior authorization requirements, step therapy protocols, medical necessity criteria, network adequacy standards, and utilization review standards. The key test: does the plan apply the restriction to SUD treatment in a way it would not apply to a comparable medical benefit?</p>

<table>
    <thead>
        <tr>
            <th>Restriction on SUD Treatment</th>
            <th>Potential Parity Violation If...</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Prior auth required for residential SUD</td><td>Prior auth not required for inpatient medical rehab (e.g., post-stroke rehab)</td></tr>
        <tr><td>Step therapy (try IOP before residential)</td><td>No step therapy required for comparable medical inpatient admissions</td></tr>
        <tr><td>30-day residential limit per year</td><td>No day limit on inpatient medical stays</td></tr>
        <tr><td>More frequent utilization reviews for SUD</td><td>Less frequent reviews for medical inpatient stays</td></tr>
        <tr><td>Narrower in-network SUD provider options</td><td>Broader in-network medical provider options (network adequacy disparity)</td></tr>
    </tbody>
</table>

<p>Under the 2024 MHPAEA final rules, health plans must now provide a comparative analysis of their treatment limitations upon request and demonstrate that their NQTLs are applied equivalently to SUD and medical benefits. You have the right to request this analysis in writing.</p>

<div class="key-takeaway">
    <strong>The parity law is a powerful appeal tool.</strong> If your insurer requires prior authorization for residential SUD treatment but does not require it for inpatient medical rehabilitation, that is a potential parity violation you can challenge through your plan&rsquo;s appeals process and with your state insurance commissioner.
</div>

<div class="guide-cta-inline">
    <p><strong>Facing a SUD treatment coverage denial?</strong> <a href="/scan">Upload your denial letter to BillKarma</a>&mdash;we analyze the denial against your plan&rsquo;s medical benefits, identify potential parity violations, and generate an appeal letter citing the specific MHPAEA requirements that apply to your plan.</p>
</div>

<h2 id="insurer-tactics">5. Common insurer denial tactics</h2>

<p>SUD treatment denials follow predictable patterns. Recognizing the tactic makes the appeal more targeted and effective:</p>

<ol>
    <li><strong>Step therapy requirements:</strong> Requiring outpatient or IOP treatment before approving residential care, even when the clinical presentation (severe withdrawal risk, unsafe home environment, multiple prior outpatient failures) meets ASAM Level 3 criteria. Challenge by documenting prior treatment episodes and clinical risk factors.</li>
    <li><strong>Medical necessity denials using proprietary criteria:</strong> Insurers often use internal medical necessity criteria that are more restrictive than the ASAM Patient Placement Criteria (the industry standard). In court cases including Wit v. United Behavioral Health, courts have found that using more restrictive criteria than accepted industry standards violates MHPAEA. Request the specific criteria used in the denial and compare to ASAM criteria.</li>
    <li><strong>Concurrent review denials:</strong> Approving the first 5 to 7 days of treatment and then denying continued stay authorization, forcing discharge before clinical stabilization. Appeal with updated clinical documentation from the treatment team.</li>
    <li><strong>Out-of-network denials:</strong> Denying residential treatment because no in-network facility is available, without offering a single-case agreement. Under MHPAEA, if the plan has network adequacy deficiencies in SUD treatment, it may be required to provide out-of-network benefits at in-network cost sharing.</li>
    <li><strong>Level of care downgrades:</strong> Approving IOP when the clinical team has determined residential care is necessary. This is one of the most common forms of SUD coverage restriction and one of the most challenged in parity complaints.</li>
</ol>

<h2 id="how-to-appeal">6. How to appeal a SUD treatment denial</h2>

<ol>
    <li><strong>Get the denial in writing immediately.</strong> Document the specific reason code, the clinical criteria cited, and the deadline for appeal.</li>
    <li><strong>Request the plan&rsquo;s MHPAEA comparative analysis.</strong> Under the 2024 final rules, your plan must provide this upon request. It often reveals the inconsistencies that support a parity violation argument.</li>
    <li><strong>Obtain ASAM-based clinical documentation from your treatment provider.</strong> The most effective appeals include a letter from the treating clinician explaining how the patient meets ASAM Level 3 (or Level 4) criteria for residential care. BillKarma data shows that <strong>61% of SUD treatment denials appealed with ASAM documentation are overturned</strong>.</li>
    <li><strong>File a parity complaint simultaneously.</strong> File with your state insurance commissioner (commercial plans) or the U.S. Department of Labor (employer self-funded plans). Parity complaints often prompt insurers to reconsider denials more quickly than internal appeals alone.</li>
    <li><strong>Request an independent medical review.</strong> Most states require commercial insurers to offer independent external review for medical necessity denials. For SUD treatment, external reviewers apply ASAM criteria, which are typically more favorable to patients than insurer proprietary criteria.</li>
    <li><strong>Consult a patient advocate or attorney.</strong> For high-dollar denials, organizations like the Substance Abuse and Mental Health Services Administration (SAMHSA) helpline (1-800-662-4357) and state legal aid organizations can provide free guidance.</li>
</ol>

<h2 id="charity-care">7. Charity care at nonprofit treatment centers</h2>

<p>Approximately 55% of U.S. addiction treatment facilities are nonprofit organizations. Like nonprofit hospitals, these facilities are required to provide some level of charity care or sliding-scale fees in exchange for their tax-exempt status. However, the rules are less structured than hospital charity care requirements.</p>

<p>If you are uninsured or underinsured, ask the treatment center&rsquo;s financial counselor specifically about:</p>
<ul>
    <li><strong>Sliding-scale fees</strong> based on income (most nonprofit programs offer this).</li>
    <li><strong>State-funded treatment slots:</strong> Each state receives block grant funding from SAMHSA to pay for SUD treatment for uninsured individuals. These &ldquo;state-funded slots&rdquo; are limited and often have waitlists, but they provide full coverage at no cost to the patient.</li>
    <li><strong>Federally Qualified Health Center (FQHC) programs:</strong> FQHCs provide SUD counseling and MAT on a sliding-scale basis regardless of insurance status.</li>
    <li><strong>Manufacturer patient assistance programs:</strong> For medication-assisted treatment (buprenorphine, naltrexone), pharmaceutical manufacturers offer patient assistance programs that provide medication at low or no cost to uninsured patients who qualify.</li>
</ul>

<h2 id="case-study">8. Real-world case study</h2>

<div class="case-study">
    <h3>Parity law appeal overturns residential SUD denial &mdash; $28,000 claim paid</h3>
    <p>A 38-year-old project manager in Colorado had commercial insurance through her employer and was admitted to a 28-day residential treatment program for opioid use disorder following a near-fatal overdose. Her insurer denied the residential claim (CPT H0018, $700/day, 28 days = $19,600), approving only 5 days of detox followed by intensive outpatient. Denial reason: &ldquo;Residential level of care not medically necessary; patient can be safely treated at a less intensive level.&rdquo;</p>
    <p>Her treatment team submitted clinical documentation using ASAM Level 3 criteria: high overdose risk (three prior overdoses), unstable housing, prior IOP failures (two episodes in the past 18 months), and co-occurring PTSD. The internal appeal was denied.</p>
    <p>Her patient advocate filed a parity complaint with the Colorado Division of Insurance, noting that the employer&rsquo;s plan covered inpatient medical rehabilitation for stroke without prior authorization or step therapy requirements. The state opened a parity investigation. Within 30 days, the insurer reversed the denial and paid the full residential claim. <strong>Amount recovered: $19,600 in residential treatment plus $8,400 in associated services denied alongside the residential claim.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Dealing with a SUD treatment billing dispute?</strong> <a href="/scan">Upload your denial or bill to BillKarma</a>&mdash;we identify parity violations, generate ASAM-based appeal language, and provide a state-specific parity complaint template.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does my health insurance have to cover addiction treatment?</h3>
        <p>Yes, in most cases. The MHPAEA requires that most health plans cover SUD treatment on the same terms as medical and surgical benefits. The ACA additionally requires all marketplace and Medicaid plans to cover SUD treatment as one of the 10 essential health benefits. Short-term plans and some grandfathered plans may be exempt.</p>
    </div>
    <div class="faq-item">
        <h3>What are the different levels of addiction treatment and what do they cost?</h3>
        <p>ASAM defines four main levels: outpatient (H0020, $75&ndash;$150/session), intensive outpatient (H0015, $250&ndash;$350/day), residential (H0018, $200&ndash;$900/day), and medically managed detox (H0008&ndash;H0010, $600&ndash;$1,500/day). Costs vary significantly by state, program type, and whether the program accepts insurance.</p>
    </div>
    <div class="faq-item">
        <h3>What is the federal mental health parity law?</h3>
        <p>The MHPAEA prohibits health plans from applying more restrictive treatment limitations to mental health and SUD benefits than to medical and surgical benefits. Under 2024 final rules, plans must provide a comparative analysis of their treatment limitations upon request and demonstrate that prior authorization, step therapy, and visit limits are applied equivalently to SUD and medical benefits.</p>
    </div>
    <div class="faq-item">
        <h3>Can my insurer require step therapy before approving residential addiction treatment?</h3>
        <p>Step therapy becomes a parity violation when the insurer applies it to SUD residential care but not to comparable medical inpatient care. Challenge step therapy requirements by requesting a medical necessity review, documenting prior treatment failures, and filing a parity complaint if the restriction is not applied equally to medical benefits.</p>
    </div>
    <div class="faq-item">
        <h3>What can I do if my insurer denies addiction treatment coverage?</h3>
        <p>Get the denial in writing, request the plan&rsquo;s MHPAEA comparative analysis, and file an internal appeal with ASAM clinical documentation from your treatment provider. BillKarma data shows that 61% of SUD treatment denials appealed with ASAM documentation are overturned. File a parity complaint with your state insurance commissioner simultaneously.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/mental-health-parity" target="_blank" rel="noopener">U.S. Department of Labor: Mental Health Parity and Addiction Equity Act</a></li>
    <li><a href="https://www.samhsa.gov/find-help/national-helpline" target="_blank" rel="noopener">SAMHSA National Helpline: Treatment Referral and Information (1-800-662-4357)</a></li>
    <li><a href="https://www.asam.org/asam-criteria/about" target="_blank" rel="noopener">American Society of Addiction Medicine: The ASAM Criteria</a></li>
    <li><a href="https://www.cms.gov/marketplace/health-plans/essential-health-benefits" target="_blank" rel="noopener">CMS: Essential Health Benefits &mdash; Mental Health and Substance Use Disorders</a></li>
    <li><a href="https://www.kff.org/mental-health/issue-brief/mental-health-and-substance-use-coverage-parity/" target="_blank" rel="noopener">KFF: Mental Health and Substance Use Coverage Parity</a></li>
    <li><a href="https://www.federalregister.gov/documents/2024/09/09/2024-19455/requirements-related-to-the-mental-health-parity-and-addiction-equity-act" target="_blank" rel="noopener">Federal Register: 2024 MHPAEA Final Rules</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2022.01018" target="_blank" rel="noopener">Health Affairs: Insurance Coverage and Access to Addiction Treatment</a></li>
</ul>
""",
})
