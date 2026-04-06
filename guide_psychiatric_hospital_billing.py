"""Guide: Psychiatric Hospital Billing — What to Expect & Your Rights."""

from guides import register, _embed

register("psychiatric-hospital-billing", {
    "title": "Psychiatric Hospital Billing: What to Expect & Your Rights (2026)",
    "meta_description": "Psychiatric hospitalization can cost $10,000–$50,000. Learn how mental health parity law protects you, how prior auth works for psych admissions, and how to appeal a denial.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "Can a hospital bill me for a psychiatric hold I didn't consent to?",
            "a": "Yes. Involuntary psychiatric holds (such as a 5150 in California or equivalent in other states) are still billable medical events. The hospital provides care — evaluation, monitoring, medication — and is entitled to bill for it. However, you have the same rights as any other patient: to receive an itemized bill, to dispute errors, and to apply for financial assistance. Insurance must cover involuntary admissions under mental health parity law if you meet medical necessity criteria.",
        },
        {
            "q": "Does insurance have to cover psychiatric hospitalization?",
            "a": "Yes, under the Mental Health Parity and Addiction Equity Act (MHPAEA), insurers that cover mental health benefits cannot impose more restrictive limitations on psychiatric care than on comparable medical or surgical care. If your plan covers inpatient medical care, it must cover inpatient psychiatric care on the same terms. That said, prior authorization and medical necessity reviews still apply — and denials happen frequently. You have the right to appeal.",
        },
        {
            "q": "What is the difference between PHP and IOP billing?",
            "a": "Partial Hospitalization Programs (PHP) typically run 6 hours per day and bill around $600–$1,500 per day. Intensive Outpatient Programs (IOP) run 3 hours per day and bill around $400–$800 per day. Both are billed as outpatient services, meaning different cost-sharing applies than inpatient stays. PHP is usually billed under H0035 or per-diem facility codes; IOP under H0004 or similar. Always verify which level of care was actually provided matches what was billed.",
        },
        {
            "q": "What is retrospective authorization for a psychiatric emergency?",
            "a": "When someone is admitted to a psychiatric facility as an emergency — voluntarily or involuntarily — prior authorization cannot be required before admission. Insurers must process a retrospective (after-the-fact) authorization review instead. They must apply the same medical necessity criteria they would for a prospective review. If they deny the retrospective auth, you can appeal on the grounds that the admission was an emergency and delay would have endangered the patient.",
        },
        {
            "q": "What percentage of psychiatric prior auth denials get overturned on appeal?",
            "a": "BillKarma data shows that 58% of prior authorization denials for psychiatric care are overturned on external review. This is one of the highest overturn rates of any category. The key is submitting a complete appeal with clinical documentation: the admitting psychiatrist's assessment, specific DSM-5 criteria met, evidence of danger to self or others or inability to care for self, and a letter from the treating clinician. Do not accept a first denial as final.",
        },
    ],
    "body": f"""
<p class="lead">Psychiatric hospitalization is one of the most expensive and least understood areas of medical billing. Inpatient stays average <strong>$1,500–$3,000 per day</strong>, and a typical 3–7 day stay produces a bill of <strong>$10,000–$50,000</strong>. Insurance coverage is legally required to be equivalent to medical coverage — but denials are common. BillKarma data shows <strong>58% of prior authorization denials for psychiatric care are overturned on external review</strong>. Here is what you need to know to understand your bill and protect your rights.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#costs">What psychiatric hospitalization costs</a></li>
        <li><a href="#parity-law">Mental health parity: your insurance rights</a></li>
        <li><a href="#admission-types">Voluntary vs. involuntary admission and billing</a></li>
        <li><a href="#prior-auth">Prior authorization and emergency admissions</a></li>
        <li><a href="#levels-of-care">The level-of-care ladder: inpatient, PHP, IOP</a></li>
        <li><a href="#cpt-codes">CPT and HCPCS codes for psychiatric billing</a></li>
        <li><a href="#billing-errors">Common billing errors to catch</a></li>
        <li><a href="#appeals">How to appeal a psychiatric denial</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="costs">1. What psychiatric hospitalization costs</h2>

<p>Psychiatric facility costs vary significantly based on the level of care, the type of facility, and your insurance status. The table below covers typical ranges for each setting.</p>

<table>
    <thead>
        <tr><th>Level of care</th><th>Typical cost</th><th>Typical duration</th><th>Total range</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Inpatient psychiatric hospital</strong></td><td>$1,500–$3,000/day</td><td>3–7 days</td><td>$10,000–$50,000</td></tr>
        <tr><td><strong>Partial hospitalization (PHP)</strong></td><td>$600–$1,500/day</td><td>2–4 weeks</td><td>$8,000–$42,000</td></tr>
        <tr><td><strong>Intensive outpatient (IOP)</strong></td><td>$400–$800/day</td><td>4–8 weeks</td><td>$11,200–$44,800</td></tr>
        <tr><td><strong>Residential treatment center (RTC)</strong></td><td>$500–$1,200/day</td><td>30–90 days</td><td>$15,000–$108,000</td></tr>
        <tr><td><strong>Crisis stabilization unit</strong></td><td>$500–$1,500/day</td><td>1–3 days</td><td>$500–$4,500</td></tr>
    </tbody>
</table>

<p>With insurance, your out-of-pocket exposure is capped at your plan's annual out-of-pocket maximum — typically $3,000–$9,100 for individual plans in 2026. Without insurance or if your claim is denied, these full amounts can land on your bill.</p>

<div class="key-takeaway">
    <strong>Before paying anything, check your bill for errors.</strong> <a href="/scan">Upload your psychiatric hospital bill to BillKarma</a> &mdash; we check for wrong place-of-service codes, duplicate charges, and level-of-care mismatches that are common in psych billing.
</div>

<h2 id="parity-law">2. Mental health parity: your insurance rights</h2>

<p>The <strong>Mental Health Parity and Addiction Equity Act (MHPAEA)</strong> requires that insurers offering mental health and substance use disorder benefits cannot impose more restrictive limitations on those benefits than on comparable medical or surgical benefits. This means:</p>

<ul>
    <li>If your plan covers unlimited inpatient medical days, it cannot cap inpatient psychiatric days</li>
    <li>If your plan has a $500 inpatient medical deductible, it cannot impose a separate $2,000 psychiatric deductible</li>
    <li>Prior authorization and medical necessity criteria must be comparable — no stricter standards for psych than for medical</li>
    <li>The law applies to most employer-sponsored plans (via ERISA), marketplace plans, Medicaid managed care, and CHIP</li>
</ul>

<p>Parity violations are among the most common and actionable insurance issues BillKarma sees. If your plan approved an inpatient medical stay for a comparable condition but denied your psychiatric stay, that discrepancy is grounds for an appeal specifically citing MHPAEA.</p>

<h2 id="admission-types">3. Voluntary vs. involuntary admission and billing</h2>

<p>Both voluntary and involuntary psychiatric admissions generate bills in the same way — the hospital provides services and bills for them regardless of how the admission occurred.</p>

<p><strong>What triggers an inpatient psychiatric admission:</strong></p>
<ul>
    <li>Danger to self (active suicidal ideation with plan or intent)</li>
    <li>Danger to others (homicidal ideation or threatening behavior)</li>
    <li>Inability to care for self (severe psychosis, inability to meet basic needs)</li>
</ul>

<p><strong>Voluntary admission:</strong> The patient consents to hospitalization. Billing proceeds normally — insurance is billed, prior auth is typically requested (sometimes retrospectively if the admission happened quickly), and the patient is responsible for cost-sharing.</p>

<p><strong>Involuntary admission (psychiatric hold):</strong> The patient is detained by legal process (72-hour hold or equivalent). The patient still receives a bill. Insurance still must cover it under parity law if medical necessity criteria are met. The patient retains all rights to dispute billing errors and appeal denials.</p>

<p><strong>Important:</strong> Patients on involuntary holds retain their right to refuse certain treatments (not the hold itself in most states, but specific medications in many jurisdictions). This does not affect billing — the evaluation, monitoring, and facility costs are billed regardless.</p>

<h2 id="prior-auth">4. Prior authorization and emergency admissions</h2>

<p>Prior authorization is frequently required for psychiatric admissions — but there are important rules about when it can and cannot apply.</p>

<ol>
    <li><strong>Emergency admissions:</strong> Insurers cannot require prior authorization before an emergency psychiatric admission. If someone is admitted due to imminent danger, the insurer must process a retrospective authorization review after the fact.</li>
    <li><strong>Retrospective review:</strong> The insurer reviews whether the admission met medical necessity criteria. They must use the same criteria they would have applied prospectively. A denial of retrospective auth can be appealed.</li>
    <li><strong>Non-emergency admissions:</strong> Planned admissions (stepping up from outpatient care) require prior auth. Get authorization in writing before admission and document the reference number.</li>
    <li><strong>Concurrent review:</strong> Even with an authorized admission, insurers often require daily or every-other-day clinical updates to continue authorizing the stay. Missing a concurrent review deadline can result in a denial for additional days.</li>
    <li><strong>Discharge planning:</strong> Insurers often push for discharge before the clinical team is ready. You have the right to appeal a denial of continued inpatient care, and the hospital must give you notice of discharge in advance so you can file an expedited appeal.</li>
</ol>

<div class="key-takeaway">
    <strong>Know what your insurance actually paid.</strong> Use <a href="/calculator">BillKarma's cost calculator</a> to see Medicare benchmark rates for psychiatric CPT codes &mdash; this helps you verify whether your insurer's payment was reasonable before you pay the remaining balance.
</div>

<h2 id="levels-of-care">5. The level-of-care ladder: inpatient, PHP, IOP</h2>

<p>Psychiatric care exists on a continuum. Understanding each level matters because each is billed differently and has different insurance coverage rules.</p>

<table>
    <thead>
        <tr><th>Level</th><th>Hours/day</th><th>Setting</th><th>Typical billing</th><th>Cost range</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Inpatient</strong></td><td>24 hours</td><td>Locked psychiatric unit or hospital</td><td>Per diem + professional fees</td><td>$1,500–$3,000/day</td></tr>
        <tr><td><strong>Partial hospitalization (PHP)</strong></td><td>~6 hours</td><td>Outpatient psychiatric facility</td><td>Per diem (H0035) or CPT-based</td><td>$600–$1,500/day</td></tr>
        <tr><td><strong>Intensive outpatient (IOP)</strong></td><td>~3 hours</td><td>Outpatient clinic or group practice</td><td>Per service (H0004, CPT group codes)</td><td>$400–$800/day</td></tr>
        <tr><td><strong>Outpatient</strong></td><td>1 hour/week</td><td>Office or telehealth</td><td>Per visit (90834, 90837)</td><td>$150–$300/session</td></tr>
    </tbody>
</table>

<p><strong>Residential Treatment Centers (RTCs)</strong> occupy a separate category. They are not hospitals — they do not have a physician available 24/7 and provide a structured living environment with therapeutic programming. RTCs bill differently from hospitals: often as a per diem under H0018 (residential treatment, psychiatric). Insurance coverage for RTCs is more variable and frequently contested.</p>

<p><strong>Step-down billing issues:</strong> A common error occurs when a patient transitions from inpatient to PHP but the facility continues billing inpatient rates for several days. Always verify the dates of service against the level of care actually provided for each day.</p>

<h2 id="cpt-codes">6. CPT and HCPCS codes for psychiatric billing</h2>

<p>Knowing the codes on your bill helps you verify that what was billed matches what was provided. These are the most common codes you will see on a psychiatric facility bill.</p>

<table>
    <thead>
        <tr><th>Code</th><th>What it represents</th><th>Typical charge</th></tr>
    </thead>
    <tbody>
        <tr><td>99221–99223</td><td>Initial hospital care (low to high complexity)</td><td>$200–$600</td></tr>
        <tr><td>99231–99233</td><td>Subsequent hospital care (daily visits)</td><td>$100–$350/day</td></tr>
        <tr><td>99238</td><td>Hospital discharge day management</td><td>$150–$300</td></tr>
        <tr><td>90837</td><td>Individual psychotherapy, 60 minutes</td><td>$150–$300</td></tr>
        <tr><td>90853</td><td>Group psychotherapy</td><td>$50–$150/session</td></tr>
        <tr><td>H0018</td><td>Behavioral health, short-term residential</td><td>Per diem</td></tr>
        <tr><td>H0035</td><td>Partial hospitalization (PHP)</td><td>Per diem</td></tr>
        <tr><td>S0201</td><td>Psychiatric inpatient treatment program</td><td>Per diem</td></tr>
    </tbody>
</table>

<h2 id="billing-errors">7. Common billing errors to catch</h2>

<p>Psychiatric billing is among the most error-prone categories in medical billing. The most frequent errors BillKarma identifies include:</p>

<ul>
    <li><strong>Wrong place of service code:</strong> PHP services billed with inpatient place-of-service code (21) instead of outpatient (52 or 57). This results in incorrect cost-sharing for the patient.</li>
    <li><strong>Individual therapy billed when only group provided:</strong> CPT 90837 (individual, 60 min) billed instead of 90853 (group). Individual therapy reimburses 3–5× higher than group. This is one of the most audited billing errors in psychiatric settings.</li>
    <li><strong>Length-of-stay errors:</strong> Bill shows 7 days but the patient was discharged after 5 days. Always verify dates of service against your own records.</li>
    <li><strong>Duplicate professional and facility fees for the same service:</strong> The hospital and the attending psychiatrist both bill for the same evaluation — sometimes legitimately, sometimes in error. Verify that separate bills reflect genuinely separate services.</li>
    <li><strong>Level-of-care billing mismatch:</strong> Patient stepped down from inpatient to PHP on Day 4 but inpatient rate was billed for all 7 days.</li>
    <li><strong>Observation vs. inpatient status:</strong> A patient kept under psychiatric observation rather than formally admitted as inpatient will have different cost-sharing — observation is outpatient billing, which means Part B deductible applies under Medicare, not the inpatient deductible.</li>
</ul>

<h2 id="appeals">8. How to appeal a psychiatric denial</h2>

<p>BillKarma data shows 58% of prior authorization denials for psychiatric care are overturned on external review — the highest overturn rate of any category we track. The key is a complete, well-documented appeal.</p>

<ol>
    <li><strong>Get the denial letter and reason code.</strong> The insurer must provide a specific reason. Common reasons: "not medically necessary," "lower level of care appropriate," "criteria not met." Each requires a different response.</li>
    <li><strong>Request the clinical criteria used.</strong> Under MHPAEA and ERISA, you can demand the specific medical necessity criteria the insurer applied. Compare them to the criteria used for comparable medical admissions.</li>
    <li><strong>Gather clinical documentation.</strong> Get the admitting psychiatrist's assessment, DSM-5 diagnosis, specific criteria for admission level (danger to self/others, inability to care for self), medication records, and discharge summary.</li>
    <li><strong>Write the appeal letter.</strong> Cite MHPAEA if criteria were stricter than for medical admissions. Reference the specific clinical documentation. If denied for "lower level of care appropriate," get a letter from the treating clinician explaining why lower care was clinically inadequate.</li>
    <li><strong>File a Level 1 (internal) appeal first.</strong> You typically have 180 days from the denial. The insurer has 30–60 days to respond (15 days for urgent/concurrent appeals).</li>
    <li><strong>If Level 1 fails, request external review.</strong> An independent organization reviews the denial. External reviewers overturn psychiatric denials at notably high rates. This is free and available under ACA for most plans.</li>
    <li><strong>ERISA complaints:</strong> For employer-sponsored plans, you can file a complaint with the Department of Labor's Employee Benefits Security Administration (EBSA) if parity violations occurred.</li>
</ol>

<div class="key-takeaway">
    <strong>Psychiatric billing disputes are among the fastest-growing categories BillKarma handles.</strong> <a href="/fight-debt">Start a dispute with BillKarma</a> — our team reviews psych bills for billing errors and prepares documentation packages for insurance appeals.
</div>

{_embed(mode="cost", title="Look up Medicare rates for psychiatric CPT codes", subtitle="Enter a code like 99232 or 90837 to see the Medicare benchmark rate.")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can a hospital bill me for a psychiatric hold I didn't consent to?</h3>
        <p>Yes. Involuntary holds are billable medical events — the hospital provided care and can bill for it. You still have the right to an itemized bill, to dispute errors, and to apply for financial assistance. Insurance must cover it under mental health parity law if medical necessity criteria are met.</p>
    </div>

    <div class="faq-item">
        <h3>Does insurance have to cover psychiatric hospitalization?</h3>
        <p>Under the Mental Health Parity and Addiction Equity Act, yes. If your plan covers inpatient medical care, it must cover inpatient psychiatric care on equivalent terms. Denials still happen, but you have strong legal grounds for appeal when parity violations occur.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between PHP and IOP billing?</h3>
        <p>PHP (6 hours/day) bills at $600–$1,500/day, typically under H0035. IOP (3 hours/day) bills at $400–$800/day under H0004 or per-service CPT codes. Both are outpatient billing — different cost-sharing applies than for inpatient stays. Verify which level matches your actual schedule.</p>
    </div>

    <div class="faq-item">
        <h3>What is retrospective authorization for a psychiatric emergency?</h3>
        <p>When someone is admitted as a psychiatric emergency, the insurer cannot require prior authorization before admission. They must review the admission after the fact using the same criteria they would have applied prospectively. A retrospective denial can be appealed using the same process as any other denial.</p>
    </div>

    <div class="faq-item">
        <h3>What percentage of psychiatric prior auth denials get overturned on appeal?</h3>
        <p>BillKarma data shows 58% of prior authorization denials for psychiatric care are overturned on external review — one of the highest rates of any medical category. A complete appeal with clinical documentation significantly increases the chances of overturn. Do not accept a first denial as final.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/CCIIO/Programs-and-Initiatives/Other-Insurance-Protections/mhpaea_factsheet" target="_blank" rel="noopener">CMS: Mental Health Parity and Addiction Equity Act (MHPAEA) Overview</a></li>
    <li><a href="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/mental-health-parity" target="_blank" rel="noopener">Department of Labor: ERISA Mental Health Parity Enforcement</a></li>
    <li><a href="https://www.kff.org/mental-health/issue-brief/insurance-coverage-and-access-to-mental-health-care/" target="_blank" rel="noopener">KFF: Insurance Coverage and Access to Mental Health Care</a></li>
    <li><a href="https://www.samhsa.gov/data/" target="_blank" rel="noopener">SAMHSA: Behavioral Health Spending and Utilization Data</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.hhs.gov/about/news/2023/07/25/hhs-releases-report-mental-health-parity-protections.html" target="_blank" rel="noopener">HHS: Report on Mental Health Parity Protections (2023)</a></li>
</ul>
""",
})
