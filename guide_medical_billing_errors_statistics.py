"""Guide: Medical Billing Errors: 2026 Statistics, Types, and What They Cost You."""

from guides import register, _embed

register("medical-billing-errors-statistics-2026", {
    "title": "Medical Billing Errors: How Common Are They in 2026?",
    "meta_description": "Up to 80% of medical bills contain errors. See the latest statistics, most common error types, and how to audit your own hospital bill.",
    "published": "2026-02-27",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What percentage of medical bills contain errors?",
            "a": "Multiple studies put the number between 26% and 80%, depending on the definition of error and the type of care. The HHS Office of Inspector General finds improper payment rates of 7-8% in Medicare Fee-for-Service claims. The Medical Billing Advocates of America estimates that roughly 80% of medical bills contain at least one mistake. BillKarma's own analysis flags potential billing issues in approximately 1 in 4 hospital bills reviewed.",
        },
        {
            "q": "How much do billing errors cost patients each year?",
            "a": "Billing errors are estimated to cost American patients approximately $210 billion per year, according to NHE and industry analyses. The average overcharge on a bill that contains errors is between $1,300 and $2,600, depending on the type of care. ER bills tend to have the highest error amounts, followed by surgical bills and inpatient stays.",
        },
        {
            "q": "What is the most common type of medical billing error?",
            "a": "Upcoding — billing for a higher-level service than was actually performed — is the single most common billing error by dollar impact. Duplicate charges are the most common by frequency. Other prevalent errors include unbundling, wrong patient information, incorrect quantities, and charges for services never rendered.",
        },
        {
            "q": "What happens if I dispute a billing error?",
            "a": "Patients who dispute billing errors succeed in getting adjustments roughly 60-70% of the time, according to medical billing advocate data. The average savings from a successful dispute is $800 to $3,000. Most disputes are resolved within 30 to 60 days. You do not need a professional advocate to dispute — a phone call with specific line items, CPT codes, and supporting documentation resolves many errors.",
        },
        {
            "q": "Do I need a professional billing advocate to dispute an error?",
            "a": "Not for most errors. Simple mistakes like duplicate charges, wrong patient information, and math errors can usually be resolved with a single phone call to the billing department. For complex disputes involving upcoding, unbundling, or large dollar amounts, a professional advocate can help — but tools like BillKarma can flag the same errors automatically so you know exactly what to dispute and why.",
        },
        {
            "q": "Which types of medical bills have the highest error rates?",
            "a": "Emergency room bills have the highest error rate at an estimated 40-50%, largely driven by ER visit level upcoding. Surgical bills follow at 30-40%, often due to unbundling and duplicate charges. Outpatient procedure bills, lab bills, and imaging bills have lower but still significant error rates of 15-25%.",
        },
    ],
    "body": f"""
<p class="lead">Studies show that <strong>26&ndash;49% of Medicare claims contain errors</strong>, and the Medical Billing Advocates of America estimates that <strong>80% of medical bills have at least one mistake</strong>. These errors cost American patients an estimated <strong>$210 billion per year</strong>. Despite these numbers, only about 20% of patients ever review their bills in detail. Here are the latest statistics on medical billing errors and what they mean for your bill.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#key-statistics">Key statistics at a glance</a></li>
        <li><a href="#common-errors">The 10 most common billing errors</a></li>
        <li><a href="#error-rates-by-care">Error rates by care type</a></li>
        <li><a href="#who-catches">Who catches billing errors</a></li>
        <li><a href="#financial-impact">The financial impact</a></li>
        <li><a href="#check-your-bill">How to check your bill for errors</a></li>
        <li><a href="#dispute-outcomes">What happens when you dispute</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="key-statistics">1. Key statistics at a glance</h2>

<p>The data on medical billing errors comes from federal audits, academic research, and industry analyses. Here are the numbers that matter most:</p>

<table>
    <thead>
        <tr>
            <th>Statistic</th>
            <th>Figure</th>
            <th>Source</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Share of medical bills with at least one error</td><td><strong>~80%</strong></td><td>Medical Billing Advocates of America</td></tr>
        <tr><td>Medicare claims with improper payments</td><td><strong>7.7%</strong> ($31.5B)</td><td>HHS OIG, FY 2025 audit</td></tr>
        <tr><td>Medicare claims containing coding errors</td><td><strong>26&ndash;49%</strong></td><td>OIG / JAMA Health Forum analysis</td></tr>
        <tr><td>Estimated annual cost of billing errors to patients</td><td><strong>$210 billion</strong></td><td>NHE / Access One industry estimate</td></tr>
        <tr><td>Average overcharge per bill with errors</td><td><strong>$1,300&ndash;$2,600</strong></td><td>Medical billing advocate industry data</td></tr>
        <tr><td>ER bills with visit-level upcoding</td><td><strong>~40&ndash;50%</strong></td><td>Health Affairs / AAPC analysis</td></tr>
        <tr><td>Patients who review their bills in detail</td><td><strong>~20%</strong></td><td>AARP / KFF consumer surveys</td></tr>
        <tr><td>Patients who find errors when they do review</td><td><strong>~50%</strong></td><td>AARP / medical billing advocate data</td></tr>
        <tr><td>Success rate of billing disputes</td><td><strong>60&ndash;70%</strong></td><td>Medical Billing Advocates of America</td></tr>
        <tr><td>Average savings per successful dispute</td><td><strong>$800&ndash;$3,000</strong></td><td>Medical billing advocate industry data</td></tr>
        <tr><td>Hospital bills flagged by BillKarma analysis</td><td><strong>~1 in 4</strong></td><td>BillKarma internal data</td></tr>
        <tr><td>NCCI code pairs that cannot be billed together</td><td><strong>200,000+</strong></td><td>CMS NCCI edit tables</td></tr>
    </tbody>
</table>

<p>The takeaway: billing errors are not rare exceptions. They are a structural feature of the American medical billing system &mdash; and they overwhelmingly favor the provider, not the patient.</p>

<div class="key-takeaway">
    <strong>Think your bill might be wrong?</strong> <a href="/scan">Upload your bill to BillKarma</a> and we&rsquo;ll automatically flag duplicate charges, upcoding, unbundling, and charges that exceed the Medicare rate &mdash; in minutes, not hours.
</div>

<h2 id="common-errors">2. The 10 most common billing errors</h2>

<p>Not all billing errors are created equal. Some appear frequently but cost relatively little per incident; others are less common but can add thousands of dollars to a single bill. Here are the 10 most common errors, ranked by overall impact (frequency multiplied by average dollar amount):</p>

<table>
    <thead>
        <tr>
            <th>Rank</th>
            <th>Error Type</th>
            <th>What It Means</th>
            <th>Estimated Frequency</th>
            <th>Avg. Dollar Impact</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td><strong>Upcoding</strong></td>
            <td>Billing a higher-level service code than the care actually warranted</td>
            <td>~25&ndash;35% of ER and office visit bills</td>
            <td>$500&ndash;$2,000+</td>
        </tr>
        <tr>
            <td>2</td>
            <td><strong>Duplicate charges</strong></td>
            <td>Same service or supply billed more than once</td>
            <td>~15&ndash;20% of multi-day inpatient bills</td>
            <td>$50&ndash;$1,500</td>
        </tr>
        <tr>
            <td>3</td>
            <td><strong>Unbundling</strong></td>
            <td>Billing component procedures separately instead of using the correct bundled code</td>
            <td>~10&ndash;15% of surgical and procedural bills</td>
            <td>$100&ndash;$800</td>
        </tr>
        <tr>
            <td>4</td>
            <td><strong>Wrong patient information</strong></td>
            <td>Incorrect name, DOB, insurance ID, or group number causing claim denials</td>
            <td>~10&ndash;12% of all claims</td>
            <td>Varies (can cause full-balance billing)</td>
        </tr>
        <tr>
            <td>5</td>
            <td><strong>Incorrect quantity</strong></td>
            <td>Billing for more units, doses, or supplies than were actually administered</td>
            <td>~8&ndash;12% of inpatient bills</td>
            <td>$50&ndash;$500</td>
        </tr>
        <tr>
            <td>6</td>
            <td><strong>Services not rendered</strong></td>
            <td>Charges for consultations, tests, or medications that never occurred</td>
            <td>~5&ndash;10% of hospital bills</td>
            <td>$100&ndash;$1,000</td>
        </tr>
        <tr>
            <td>7</td>
            <td><strong>Incorrect modifier usage</strong></td>
            <td>Wrong or missing CPT modifiers that change how a service is priced or processed</td>
            <td>~8&ndash;10% of surgical claims</td>
            <td>$200&ndash;$600</td>
        </tr>
        <tr>
            <td>8</td>
            <td><strong>Wrong date of service</strong></td>
            <td>Charges dated on a day the patient was not present or had been discharged</td>
            <td>~5&ndash;8% of multi-day stays</td>
            <td>$500&ndash;$3,000 (per extra day)</td>
        </tr>
        <tr>
            <td>9</td>
            <td><strong>Balance billing violations</strong></td>
            <td>Out-of-network providers billing beyond what the No Surprises Act or state law allows</td>
            <td>~3&ndash;5% of out-of-network claims</td>
            <td>$500&ndash;$5,000+</td>
        </tr>
        <tr>
            <td>10</td>
            <td><strong>Coordination of benefits errors</strong></td>
            <td>When a patient has two insurance plans and the billing order is wrong or one plan is not billed</td>
            <td>~5&ndash;7% of dual-coverage patients</td>
            <td>$200&ndash;$2,000</td>
        </tr>
    </tbody>
</table>

<h3>Error 1: Upcoding &mdash; the biggest dollar-impact error</h3>

<p>Upcoding is the single most costly billing error for patients. It means your visit or procedure was billed at a higher complexity level than the care you actually received. The most common example is ER visit level coding:</p>

<table>
    <thead>
        <tr>
            <th>ER Visit Level</th>
            <th>CPT Code</th>
            <th>Medicare Rate (2026)</th>
            <th>Typical Hospital Charge</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Level 3 (moderate)</td><td>99283</td><td>$106</td><td>$900&ndash;$1,800</td></tr>
        <tr><td>Level 4 (high severity)</td><td>99284</td><td>$176</td><td>$1,800&ndash;$3,200</td></tr>
        <tr><td>Level 5 (life-threatening)</td><td>99285</td><td>$227</td><td>$2,800&ndash;$5,000+</td></tr>
    </tbody>
</table>

<p>A Health Affairs analysis found that ER visit-level distributions have shifted dramatically upward over the past decade, with Level 4 and Level 5 visits now comprising the majority of ER claims &mdash; even as patient acuity has not changed proportionally. The result: patients are systematically billed at higher rates than their care warrants. If you visited the ER for a straightforward issue (sprained ankle, minor laceration, UTI) and were billed at Level 4 or 5, request a coding review.</p>

<h3>Error 2: Duplicate charges &mdash; the most frequent error</h3>

<p>Duplicate charges are the error type patients encounter most often, especially on multi-day inpatient stays. They happen when different hospital departments independently log the same service: the lab bills a CBC and the floor nurse&rsquo;s charting system also generates a CBC charge for the same day. IV medications, daily labs, and routine supplies are the most frequently duplicated items. Sorting your itemized bill by date and CPT code makes duplicates immediately visible.</p>

<h3>Error 3: Unbundling &mdash; hidden overcharges in procedure bills</h3>

<p>Unbundling inflates your bill by breaking a single procedure into its component parts and billing each one separately. CMS publishes over 200,000 NCCI code pairs specifically to prevent this. A common example: a colonoscopy with biopsy should be billed as CPT 45380 (Medicare rate: $198), but unbundling would bill the colonoscopy and biopsy as separate line items with separate charges totaling more than the bundled rate. BillKarma&rsquo;s analyzer checks every bill against the NCCI edit list automatically. Learn more about unbundling and other common hospital billing errors in our <a href="/guides/common-hospital-billing-errors">hospital billing errors guide</a>.</p>

<div class="key-takeaway">
    <strong>See exactly what Medicare pays for any procedure.</strong> Use our <a href="/calculator">Medicare rate calculator</a> to look up the benchmark rate for any CPT code on your bill &mdash; then compare it to what you were charged.
</div>

{_embed(mode="markup", title="Check if your charge looks right", subtitle="Enter a CPT code and the amount you were charged to compare against Medicare rates.", height="420")}

<h2 id="error-rates-by-care">3. Error rates by care type</h2>

<p>Billing error rates vary significantly depending on the type of care. More complex encounters generate more line items, more codes, and more opportunities for mistakes. Here is how error rates break down by care setting:</p>

<table>
    <thead>
        <tr>
            <th>Care Type</th>
            <th>Estimated Error Rate</th>
            <th>Most Common Error</th>
            <th>Average Overcharge</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><strong>Emergency room</strong></td><td>40&ndash;50%</td><td>Upcoding (visit level inflation)</td><td>$1,200&ndash;$2,600</td></tr>
        <tr><td><strong>Inpatient surgery</strong></td><td>30&ndash;40%</td><td>Unbundling and duplicate charges</td><td>$1,500&ndash;$4,000</td></tr>
        <tr><td><strong>Outpatient procedures</strong></td><td>20&ndash;30%</td><td>Incorrect modifiers and facility fees</td><td>$400&ndash;$1,200</td></tr>
        <tr><td><strong>Lab and pathology</strong></td><td>15&ndash;25%</td><td>Duplicate charges and incorrect quantities</td><td>$100&ndash;$500</td></tr>
        <tr><td><strong>Imaging (MRI, CT, X-ray)</strong></td><td>15&ndash;20%</td><td>Wrong imaging code (with vs. without contrast)</td><td>$200&ndash;$800</td></tr>
    </tbody>
</table>

<p>Emergency room bills have the highest error rate for two reasons. First, ER visits involve rapid, multi-provider care with documentation completed after the fact &mdash; which increases coding mistakes. Second, ER visit level coding (CPT 99281&ndash;99285) is subjective and hospitals have financial incentives to code at the highest defensible level. A JAMA study found that ER visit coding distributions have shifted significantly toward higher levels over the past decade, suggesting systematic upcoding rather than truly sicker patients.</p>

<p>Surgical bills carry the second-highest risk because of the sheer number of billable components: the surgeon&rsquo;s professional fee, the anesthesia fee, the facility fee, individual supply charges, recovery room charges, and post-operative care. Each component is an opportunity for an error &mdash; or an opportunity to unbundle what should be a single charge into several.</p>

<h2 id="who-catches">4. Who catches billing errors</h2>

<p>The short answer: almost no one. That&rsquo;s what makes billing errors so profitable for the system.</p>

<p>According to AARP and KFF consumer surveys, <strong>only about 20% of patients review their medical bills in detail</strong>. The other 80% either pay without reviewing, set up a payment plan without questioning the amount, or ignore the bill entirely. Of the patients who <em>do</em> review their bills:</p>

<ul>
    <li><strong>~50% find at least one questionable charge</strong> &mdash; a line item that doesn&rsquo;t match their recollection of care, a duplicate, or a charge they can&rsquo;t identify</li>
    <li><strong>~30% of those who find errors actually dispute them</strong> &mdash; the rest don&rsquo;t know how, don&rsquo;t have time, or assume the hospital is right</li>
    <li><strong>60&ndash;70% of disputes result in an adjustment</strong> &mdash; meaning the hospital agrees the charge was wrong or reduces it</li>
</ul>

<p>Putting those numbers together: out of 100 patients who receive a bill with an error, roughly 20 review it, 10 find something wrong, 3 dispute it, and 2 get an adjustment. The other 98 pay the incorrect amount. This math explains why the system persists &mdash; the expected revenue from billing errors far exceeds the cost of the occasional correction.</p>

<div class="key-takeaway">
    <strong>Don&rsquo;t be one of the 80% who never check.</strong> <a href="/scan">Upload your bill to BillKarma</a> for an automated review that takes minutes, not hours. We check every line against Medicare rates, flag duplicates, and identify unbundled codes.
</div>

<h2 id="financial-impact">5. The financial impact</h2>

<p>Billing errors are not just an inconvenience &mdash; they are a significant financial burden on American families. Here is what the data shows about real-dollar impact:</p>

<h3>The national picture</h3>

<p>National health expenditures in the United States exceeded <strong>$4.8 trillion in 2024</strong>, according to CMS. If even 5% of that spending represents billing errors and improper payments, the annual cost of mistakes is <strong>over $240 billion</strong>. The HHS OIG&rsquo;s own estimate of Medicare improper payments alone was $31.5 billion in fiscal year 2025 &mdash; and that covers only the federal Medicare program, not commercial insurance or Medicaid.</p>

<h3>Case study: ER visit for a child&rsquo;s broken arm</h3>

<div class="case-study">
    <h3>The Carter family &mdash; Austin, Texas</h3>
    <p>Their 8-year-old fell off a swing and broke her forearm. The ER visit included an X-ray (CPT 73060), a splint application (CPT 29125), and a prescription for ibuprofen. Time in the ER: 2 hours. Clinical complexity: straightforward, no surgery needed.</p>
    <p><strong>Billed:</strong> CPT 99285 (Level 5 ER visit) at $4,200, plus X-ray at $380 and splint at $520. <strong>Total: $5,100.</strong></p>
    <p><strong>What it should have been:</strong> A simple fracture with an X-ray and a splint is consistent with a Level 3 ER visit (CPT 99283). At the hospital&rsquo;s own pricing, Level 3 would have been $1,400 instead of $4,200.</p>
    <p><strong>After dispute:</strong> The family requested a coding review citing the clinical complexity criteria. The hospital downgraded to Level 4 (CPT 99284, $2,800). <strong>Savings: $1,400 on the ER visit charge alone.</strong> Their out-of-pocket share dropped from $1,530 to $1,110 after insurance adjustments.</p>
</div>

<h3>Case study: knee surgery with duplicate charges</h3>

<div class="case-study">
    <h3>Maria S. &mdash; Columbus, Ohio</h3>
    <p>Maria had an arthroscopic knee surgery (CPT 29881, Medicare rate: $458) at an in-network surgery center. The total bill was $18,400. When she requested an itemized statement, she found:</p>
    <ul>
        <li>The surgical procedure was billed twice on the same date &mdash; <strong>duplicate charge of $3,200</strong></li>
        <li>IV ketorolac was billed for 6 units when her medical record showed 2 were administered &mdash; <strong>overcharge of $340</strong></li>
        <li>A cardiology consultation appeared on the bill, but Maria has no cardiac history and no cardiologist visited her &mdash; <strong>phantom charge of $580</strong></li>
    </ul>
    <p><strong>Total errors: $4,120.</strong> Maria called the billing department with each item listed by date and CPT code. The duplicate and phantom charges were removed immediately. The medication quantity was corrected. Her out-of-pocket responsibility dropped from <strong>$4,600 to $2,980</strong>.</p>
</div>

<h3>Case study: lab bills after a routine physical</h3>

<div class="case-study">
    <h3>James T. &mdash; Denver, Colorado</h3>
    <p>James had an annual physical with routine bloodwork: a comprehensive metabolic panel (CPT 80053) and a lipid panel (CPT 80061). Both are standard preventive screenings covered at 100% under the ACA with no patient cost-sharing.</p>
    <p><strong>Billed:</strong> The lab coded the visit as a diagnostic visit (ICD-10 code R73.09, abnormal glucose) rather than a preventive visit (ICD-10 Z00.00, routine exam). This caused his insurance to apply the charges to his deductible instead of covering them at 100%. <strong>Result: a $480 bill for tests that should have cost $0.</strong></p>
    <p><strong>After dispute:</strong> James called the lab and asked for the diagnosis code to be corrected to the preventive code. The claim was reprocessed, and his bill was <strong>reduced to $0</strong>.</p>
</div>

<p>These cases illustrate a pattern: the errors are not random. They consistently result in higher charges, and they are consistently correctable when patients know what to look for. Use our <a href="/calculator">calculator</a> to check the Medicare rate for any CPT code on your bill.</p>

{_embed(mode="cost", title="Look up any procedure cost", subtitle="Enter a CPT code to see what Medicare pays in your area.", height="380")}

<h2 id="check-your-bill">6. How to check your bill for errors</h2>

<p>You do not need a professional medical billing advocate to catch most errors. Follow this five-step process:</p>

<h3>Step 1: Get your itemized bill</h3>

<p>Call the billing department and request an itemized bill with CPT codes. A summary showing only &ldquo;Lab Services: $1,200&rdquo; is not enough. You need every individual charge on its own line with the CPT or HCPCS code, date, description, quantity, and dollar amount.</p>

<div class="key-takeaway"><strong>Federal law gives you the right</strong> to an itemized statement. If the billing department resists, cite the No Surprises Act requirement for good-faith estimates and itemized billing. For a full walkthrough, see our guide on <a href="/guides/how-to-read-your-medical-bill">how to read your medical bill</a>.</div>

<h3>Step 2: Compare to your Explanation of Benefits</h3>

<p>Pull up the EOB from your insurance company for the same dates of service. The patient responsibility on the EOB should match what the provider is billing you. If the numbers differ, one of them is wrong. Common discrepancies include the provider not applying insurance adjustments or billing you the full charge before insurance has processed the claim.</p>

<h3>Step 3: Look for the obvious errors</h3>

<p>Scan the bill for the three easiest-to-spot error types:</p>
<ul>
    <li><strong>Duplicates:</strong> Same CPT code on the same date appearing twice</li>
    <li><strong>Wrong dates:</strong> Charges on a date you were not present or had been discharged</li>
    <li><strong>Services you don&rsquo;t recognize:</strong> Consultations, tests, or medications you have no recollection of receiving</li>
</ul>

<h3>Step 4: Check CPT codes against Medicare rates</h3>

<p>Look up the Medicare rate for the highest-dollar CPT codes on your bill. While hospitals charge more than Medicare pays, the ratio tells you whether the charge is in a reasonable range. A charge that is 10&ndash;15x the Medicare rate is almost always worth questioning. Use our <a href="/calculator">calculator</a> to look up any CPT code instantly.</p>

<h3>Step 5: Check for unbundling</h3>

<p>If you had a procedure, look for multiple CPT codes from the same clinical area on the same date. These may be component codes that should have been billed as a single bundled code. BillKarma&rsquo;s analyzer checks your bill against the CMS NCCI edit list automatically, or you can search the <a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits" target="_blank" rel="noopener">CMS NCCI tools page</a> directly.</p>

<div class="key-takeaway"><strong>Want to skip the manual work?</strong> <a href="/scan">Upload your bill to BillKarma</a> and our analyzer runs all five checks automatically. You&rsquo;ll get a flagged line-item report showing every potential error with the Medicare rate comparison for each code. For a more detailed walkthrough, see our <a href="/guides/medical-bill-audit-checklist">medical bill audit checklist</a>.</div>

<h2 id="dispute-outcomes">7. What happens when you dispute</h2>

<p>Many patients avoid disputing because they assume it won&rsquo;t work. The data says otherwise.</p>

<h3>Success rates</h3>

<p>Medical billing advocates report that <strong>60&ndash;70% of billing disputes result in an adjustment</strong> &mdash; either a correction of the error or a reduction in the charge. For specific error types, the success rates are even higher:</p>

<table>
    <thead>
        <tr>
            <th>Error Type</th>
            <th>Dispute Success Rate</th>
            <th>Average Adjustment</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Duplicate charges</td><td>~90%</td><td>Full removal of the duplicate</td></tr>
        <tr><td>Wrong patient/insurance information</td><td>~85%</td><td>Claim reprocessed; balance eliminated</td></tr>
        <tr><td>Incorrect quantities</td><td>~80%</td><td>Corrected to actual quantity administered</td></tr>
        <tr><td>Upcoding (visit level)</td><td>~55&ndash;65%</td><td>Downgrade of 1&ndash;2 levels; $500&ndash;$2,000 reduction</td></tr>
        <tr><td>Unbundling</td><td>~50&ndash;60%</td><td>Rebilled under correct bundled code</td></tr>
        <tr><td>Balance billing violations</td><td>~70&ndash;80%</td><td>Balance eliminated under No Surprises Act</td></tr>
    </tbody>
</table>

<p>Duplicate charges have the highest success rate because they are objectively verifiable &mdash; the same service on the same date billed twice is indefensible. Upcoding disputes are harder because visit level coding involves clinical judgment, but hospitals still agree to downgrades more than half the time when patients present specific documentation.</p>

<h3>Average savings</h3>

<p>Across all error types, the <strong>average savings from a successful billing dispute is $800 to $3,000</strong>, according to medical billing advocate data. For ER bills specifically, the average is higher &mdash; closer to $1,200 to $2,600 &mdash; because ER upcoding involves large per-incident dollar amounts.</p>

<h3>Timeline</h3>

<p>Most billing disputes follow this timeline:</p>
<ul>
    <li><strong>Day 1:</strong> Phone call to the billing department identifying specific errors by line item</li>
    <li><strong>Days 1&ndash;10:</strong> Simple errors (duplicates, data entry) often resolved on the first call or within 10 business days</li>
    <li><strong>Days 10&ndash;30:</strong> Coding reviews (upcoding, unbundling) typically take 2&ndash;4 weeks for the hospital to complete</li>
    <li><strong>Days 30&ndash;60:</strong> Written disputes and formal billing reviews, if the phone call did not resolve the issue</li>
    <li><strong>Days 60&ndash;90:</strong> Escalation to insurance company, state insurance commissioner, or Medicare Administrative Contractor if needed</li>
</ul>

<p>The key: <strong>do not pay the disputed amount while the dispute is open</strong>. Ask the billing department to place the disputed charges on hold. Most hospitals will not send an account to collections while a formal billing review is pending.</p>

<p>For a step-by-step guide to the dispute process with letter templates, see our <a href="/guides/how-to-dispute-a-medical-bill">complete guide to disputing a medical bill</a>.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What percentage of medical bills contain errors?</h3>
        <p>Multiple studies put the number between 26% and 80%, depending on the definition of &ldquo;error&rdquo; and the type of care. The HHS Office of Inspector General finds Medicare improper payment rates of 7&ndash;8% by dollar amount. The Medical Billing Advocates of America estimates 80% of bills contain at least one mistake. BillKarma&rsquo;s analysis flags potential issues in approximately <a href="/scan">1 in 4 hospital bills</a> reviewed.</p>
    </div>

    <div class="faq-item">
        <h3>How much do billing errors cost patients each year?</h3>
        <p>An estimated $210 billion per year across the U.S. healthcare system, based on NHE data and industry analyses. Individual overcharges average $1,300 to $2,600 per bill when errors are present. ER bills and surgical bills carry the highest per-incident impact.</p>
    </div>

    <div class="faq-item">
        <h3>What is the most common type of medical billing error?</h3>
        <p>By frequency, duplicate charges are the most common. By dollar impact, upcoding &mdash; billing for a higher-level service than was performed &mdash; is the costliest. Both are detectable with an itemized bill and basic knowledge of what to look for. Use our <a href="/calculator">calculator</a> to check if a CPT code charge looks reasonable.</p>
    </div>

    <div class="faq-item">
        <h3>What happens if I dispute a billing error?</h3>
        <p>Patients who dispute succeed roughly 60&ndash;70% of the time. For simple errors like duplicates, the success rate is over 90%. For upcoding disputes, it&rsquo;s 55&ndash;65%. The average savings from a successful dispute is $800 to $3,000. Most disputes are resolved within 30 to 60 days. See our <a href="/guides/how-to-dispute-a-medical-bill">dispute guide</a> for letter templates and step-by-step instructions.</p>
    </div>

    <div class="faq-item">
        <h3>Do I need a professional billing advocate?</h3>
        <p>Not for most errors. Duplicates, wrong information, and math errors can usually be resolved with a phone call. For complex disputes involving upcoding or unbundling, tools like <a href="/scan">BillKarma</a> flag the specific errors and provide the Medicare rate benchmarks you need to make your case. Professional advocates typically charge 25&ndash;35% of savings and are worth considering for bills over $10,000 with multiple complex issues.</p>
    </div>

    <div class="faq-item">
        <h3>Which types of bills have the highest error rates?</h3>
        <p>Emergency room bills lead at 40&ndash;50%, driven primarily by visit-level upcoding. Surgical bills follow at 30&ndash;40%, mainly from unbundling and duplicates. Outpatient, lab, and imaging bills have error rates of 15&ndash;25%. The more complex the care, the more opportunity for billing errors. For a complete checklist, see our <a href="/guides/medical-bill-audit-checklist">audit checklist guide</a>.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://oig.hhs.gov/reports-and-publications/medicare-and-medicaid-fraud-waste-and-abuse/" target="_blank" rel="noopener">HHS Office of Inspector General &mdash; Medicare Improper Payment Reporting and Annual Audit Results</a></li>
    <li><a href="https://www.cms.gov/priorities/key-initiatives/improper-payments" target="_blank" rel="noopener">CMS &mdash; Medicare Fee-for-Service Improper Payment Rate Data</a></li>
    <li><a href="https://jamanetwork.com/journals/jama-health-forum" target="_blank" rel="noopener">JAMA Health Forum &mdash; Studies on Medicare Claim Accuracy and Coding Error Prevalence</a></li>
    <li><a href="https://www.healthaffairs.org/topic/costs-spending" target="_blank" rel="noopener">Health Affairs &mdash; Research on Emergency Department Coding Trends and Upcoding</a></li>
    <li><a href="https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data" target="_blank" rel="noopener">CMS &mdash; National Health Expenditure (NHE) Data and Projections</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits" target="_blank" rel="noopener">CMS &mdash; National Correct Coding Initiative (NCCI) Edits and Code Pair Reference</a></li>
    <li><a href="https://www.aarp.org/money/personal-finance/info-2021/medical-billing-errors.html" target="_blank" rel="noopener">AARP &mdash; Medical Billing Errors: What Patients Need to Know</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/data-note-americans-challenges-with-health-care-costs/" target="_blank" rel="noopener">KFF &mdash; Americans&rsquo; Challenges with Health Care Costs and Medical Billing</a></li>
    <li><a href="https://www.aapc.com/resources/medical-coding-billing" target="_blank" rel="noopener">AAPC &mdash; Medical Coding and Billing Error Research and Industry Standards</a></li>
    <li><a href="https://www.medicalbillingadvocatesofamerica.com/" target="_blank" rel="noopener">Medical Billing Advocates of America &mdash; Billing Error Rates and Patient Dispute Outcomes</a></li>
</ul>
""",
})
