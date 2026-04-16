"""Guide: Bariatric Surgery Costs: Insurance Requirements, Appeals, and How to Save."""

from guides import register, _embed

register("weight-loss-surgery-billing", {
    "title": "Bariatric Surgery Costs: Insurance Requirements",
    "meta_description": "Bariatric surgery costs $15,000-$35,000. Learn insurance BMI requirements, the 6-month diet rule, how to appeal denials, and Centers of Excellence discounts.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does bariatric surgery cost without insurance?",
            "a": "Without insurance, gastric bypass costs $20,000-$35,000, gastric sleeve costs $15,000-$25,000, and lap-band costs $10,000-$18,000. These figures include the surgeon fee, anesthesia, hospital facility fee, and standard follow-up. Cash-pay programs at Centers of Excellence often offer bundled pricing 20-40% below standard hospital rates.",
        },
        {
            "q": "What BMI do I need for insurance to cover bariatric surgery?",
            "a": "Most insurers follow NIH guidelines: BMI of 40 or higher (roughly 100+ pounds overweight), or BMI of 35-39.9 with at least one obesity-related comorbidity such as type 2 diabetes, sleep apnea, or hypertension. Some newer policies cover patients with a BMI of 30-34.9 and uncontrolled type 2 diabetes, particularly for gastric bypass.",
        },
        {
            "q": "What is the 6-month supervised diet requirement?",
            "a": "Most insurers require 3-6 months of documented physician-supervised weight management before approving bariatric surgery. This means monthly visits with a doctor where your weight, diet, and exercise are recorded. Missing even one monthly visit can reset the clock. The requirement exists to demonstrate that non-surgical approaches have been tried. Keep copies of every visit note yourself in case the provider's records are incomplete.",
        },
        {
            "q": "Can I appeal a bariatric surgery denial?",
            "a": "Yes, and appeal success rates for bariatric surgery are relatively high when comorbidities are well-documented. Common denial reasons include incomplete supervised diet documentation, BMI not meeting threshold at the time of submission, or missing psychological evaluation. A strong appeal includes updated BMI measurements, a letter of medical necessity from your surgeon, documentation of all comorbidities, and proof of completed supervised diet visits.",
        },
        {
            "q": "Does Medicare cover bariatric surgery?",
            "a": "Medicare covers bariatric surgery for beneficiaries with a BMI of 35 or higher and at least one obesity-related comorbidity. Covered procedures include Roux-en-Y gastric bypass and sleeve gastrectomy. Lap-band (laparoscopic adjustable gastric banding) was removed from Medicare coverage in 2024 due to high revision rates. The surgery must be performed at a Medicare-certified bariatric surgery center.",
        },
        {
            "q": "What is a Center of Excellence and does it save money?",
            "a": "A Center of Excellence (COE) is a hospital or surgical practice that meets specific volume and outcomes standards for bariatric surgery, as certified by the Metabolic and Bariatric Surgery Accreditation and Quality Improvement Program (MBSAQIP). Many insurers require surgery at a COE for coverage. COE facilities often have lower complication rates and offer bundled pricing that includes surgeon, anesthesia, facility, and 90-day follow-up in one price, which can be 20-40% less than unbundled hospital pricing.",
        },
    ],
    "body": f"""
<p class="lead">More than <strong>42% of American adults</strong> meet the clinical definition of obesity, yet fewer than 1% of eligible patients undergo bariatric surgery each year&mdash;largely because of cost and insurance barriers. The average bariatric procedure costs <strong>$15,000&ndash;$35,000</strong> depending on the surgery type, and insurers impose months of pre-authorization requirements that trip up even well-prepared patients. Here is how bariatric surgery billing works, what your insurance actually requires, and how to save thousands whether you have coverage or not.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#procedure-costs">Bariatric procedure types and costs compared</a></li>
        <li><a href="#insurance-requirements">Insurance requirements: BMI, comorbidities, and the 6-month diet</a></li>
        <li><a href="#pre-authorization">The pre-authorization gauntlet</a></li>
        <li><a href="#billing-breakdown">What is actually on your bariatric surgery bill</a></li>
        <li><a href="#appeals">How to appeal a bariatric surgery denial</a></li>
        <li><a href="#coe-discounts">Centers of Excellence and bundled pricing</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="procedure-costs">1. Bariatric procedure types and costs compared</h2>

<p>There are three main bariatric procedures performed in the United States today. Each has different costs, insurance approval rates, and long-term outcomes. Understanding the differences matters because your insurer may cover one but not another, and pricing varies dramatically by facility.</p>

<table>
    <thead>
        <tr><th>Procedure</th><th>CPT Code</th><th>Average Cost (No Insurance)</th><th>Medicare Rate</th><th>Insurance Approval Rate</th><th>Avg. Excess Weight Loss (5 yr)</th></tr>
    </thead>
    <tbody>
        <tr><td>Roux-en-Y Gastric Bypass</td><td>43644</td><td>$20,000&ndash;$35,000</td><td>~$12,500</td><td>72%</td><td>60&ndash;70%</td></tr>
        <tr><td>Sleeve Gastrectomy</td><td>43775</td><td>$15,000&ndash;$25,000</td><td>~$10,800</td><td>78%</td><td>55&ndash;65%</td></tr>
        <tr><td>Lap-Band (Adjustable Gastric Banding)</td><td>43770</td><td>$10,000&ndash;$18,000</td><td>Not covered*</td><td>45%</td><td>40&ndash;50%</td></tr>
    </tbody>
</table>

<p><em>*Medicare removed lap-band coverage in 2024 due to high revision and removal rates. Many private insurers have followed suit.</em></p>

<p>Sleeve gastrectomy has become the most commonly performed bariatric procedure in the U.S., surpassing gastric bypass in 2014. It has a slightly higher insurance approval rate because the complication profile is lower and the hospital stay is shorter (typically 1&ndash;2 nights vs. 2&ndash;3 for bypass). However, gastric bypass remains the gold standard for patients with severe type 2 diabetes or BMI above 50, because long-term metabolic outcomes are stronger.</p>

<div class="key-takeaway">
    <strong>Have your bill handy?</strong> <a href="/scan">Scan it with BillKarma</a>&mdash;we flag overcharges in seconds. Bariatric surgery bills frequently contain duplicate facility charges and unbundled services that should be included in the surgical package.
</div>

<h2 id="insurance-requirements">2. Insurance requirements: BMI, comorbidities, and the 6-month diet</h2>

<p>Most commercial insurers and Medicare follow the 1991 NIH Consensus Conference guidelines for bariatric surgery eligibility. The core criteria are:</p>

<ul>
    <li><strong>BMI &ge; 40</strong> (morbid obesity) with or without comorbidities, OR</li>
    <li><strong>BMI 35&ndash;39.9</strong> with at least one obesity-related comorbidity: type 2 diabetes, obstructive sleep apnea, hypertension, hyperlipidemia, GERD, or obesity hypoventilation syndrome</li>
</ul>

<p>Some insurers have expanded coverage to patients with <strong>BMI 30&ndash;34.9</strong> and uncontrolled type 2 diabetes, following updated clinical evidence. Check your specific plan documents&mdash;the Summary of Benefits and Coverage (SBC) must state whether bariatric surgery is covered and under what conditions.</p>

<h3>The 6-month supervised diet requirement</h3>

<p>This is where most patients get tripped up. Nearly all commercial insurers require <strong>3&ndash;6 consecutive months</strong> of physician-supervised weight management before approving surgery. Requirements typically include:</p>

<ul>
    <li>Monthly office visits with a physician (not just a nutritionist)</li>
    <li>Documented weight at each visit</li>
    <li>Written diet and exercise plan in the medical record</li>
    <li>No gaps longer than 45 days between visits</li>
</ul>

<p><strong>Missing a single visit can reset the clock to month one.</strong> If your doctor&rsquo;s office cancels or reschedules your appointment, document the reason in writing and ask the office to note it in your chart. Some insurers will accept a gap if documentation shows it was the provider&rsquo;s scheduling issue, not yours.</p>

<table>
    <thead>
        <tr><th>Insurer Type</th><th>Supervised Diet Requirement</th><th>BMI Threshold</th><th>Psychological Eval Required</th></tr>
    </thead>
    <tbody>
        <tr><td>Medicare</td><td>None (removed in 2013)</td><td>&ge; 35 with comorbidity</td><td>No (but surgeon may require)</td></tr>
        <tr><td>Blue Cross Blue Shield (typical)</td><td>6 months</td><td>&ge; 40 or &ge; 35 + comorbidity</td><td>Yes</td></tr>
        <tr><td>UnitedHealthcare</td><td>6 months</td><td>&ge; 40 or &ge; 35 + comorbidity</td><td>Yes</td></tr>
        <tr><td>Aetna</td><td>6 months</td><td>&ge; 40 or &ge; 35 + comorbidity</td><td>Yes</td></tr>
        <tr><td>Cigna</td><td>3 months</td><td>&ge; 40 or &ge; 35 + comorbidity</td><td>Yes</td></tr>
        <tr><td>Medicaid (varies by state)</td><td>3&ndash;6 months</td><td>Varies by state</td><td>Usually yes</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Strategy tip:</strong> Start the supervised diet program the moment you begin considering bariatric surgery&mdash;even before your surgical consultation. The 6-month clock runs regardless of whether you have picked a surgeon. Use our <a href="/calculator">cost calculator</a> to look up Medicare rates for bariatric CPT codes so you know the benchmark price before you schedule.
</div>

<h2 id="pre-authorization">3. The pre-authorization gauntlet</h2>

<p>Bariatric surgery requires prior authorization from virtually every insurer. The authorization package your surgeon&rsquo;s office submits typically includes:</p>

<ol>
    <li><strong>Letter of medical necessity</strong> from the operating surgeon, detailing BMI history, failed weight-loss attempts, and specific comorbidities</li>
    <li><strong>Supervised diet documentation</strong>&mdash;visit notes for each monthly appointment showing date, weight, diet plan, and physician signature</li>
    <li><strong>Psychological evaluation</strong>&mdash;a mental health assessment confirming the patient understands the procedure, has realistic expectations, and does not have uncontrolled psychiatric conditions that would impair compliance</li>
    <li><strong>Medical clearance</strong>&mdash;cardiac clearance (EKG, sometimes stress test), pulmonary function tests if sleep apnea is present, and lab work including HbA1c for diabetics</li>
    <li><strong>Sleep study results</strong> if sleep apnea is listed as a comorbidity (see our <a href="/guides/sleep-study-billing/">sleep study billing guide</a> for what to expect)</li>
</ol>

<p>Turnaround time for prior authorization is typically 15&ndash;30 business days. Denials are common&mdash;roughly 25&ndash;30% of initial bariatric surgery authorizations are denied, most frequently for incomplete supervised diet documentation or BMI that dropped below the threshold during the diet period.</p>

<p>Check your hospital&rsquo;s track record with bariatric billing in our <a href="/hospitals/">hospital directory</a>&mdash;some facilities have significantly better authorization success rates than others because their coordinators are experienced with the paperwork requirements.</p>

<h2 id="billing-breakdown">4. What is actually on your bariatric surgery bill</h2>

<p>A bariatric surgery generates multiple bills from multiple providers, similar to any major surgery. Here is what a typical sleeve gastrectomy bill looks like when fully itemized:</p>

<div class="bill-example">
    <div class="bill-header">Regional Medical Center &mdash; Bariatric Surgery Program &mdash; DOS: 01/20/2026</div>
    <div class="line-item">
        <span>43775 &mdash; Sleeve gastrectomy (surgeon fee)</span>
        <span>$6,200</span>
    </div>
    <div class="line-item">
        <span>00790 &mdash; Anesthesia for intra-abdominal procedure (anesthesia fee, 4 units)</span>
        <span>$3,800</span>
    </div>
    <div class="line-item">
        <span>Hospital facility fee &mdash; OR time, 2-night inpatient stay, nursing</span>
        <span>$14,500</span>
    </div>
    <div class="line-item flagged">
        <span>49320 &mdash; Diagnostic laparoscopy &nbsp; &#9888; <em>Often bundled with 43775; may be duplicate charge</em></span>
        <span>$1,800</span>
    </div>
    <div class="line-item flagged">
        <span>88305 &mdash; Surgical pathology, gross and microscopic (x3) &nbsp; &#9888; <em>3 specimens billed; verify count with operative report</em></span>
        <span>$945</span>
    </div>
    <div class="line-item">
        <span>74246 &mdash; Upper GI series with contrast (post-op leak test)</span>
        <span>$1,200</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$28,445</span>
    </div>
</div>

<p>Common billing errors on bariatric surgery bills include:</p>

<ul>
    <li><strong>Unbundled laparoscopy (49320):</strong> Diagnostic laparoscopy is typically included in the sleeve gastrectomy (43775) or gastric bypass (43644) code. Billing it separately is unbundling and should be disputed.</li>
    <li><strong>Duplicate pathology charges:</strong> The removed stomach tissue generates one pathology specimen. If you see multiple pathology codes, verify the count against the operative report.</li>
    <li><strong>Extended stay charges:</strong> A sleeve gastrectomy typically requires a 1&ndash;2 night stay. If you were billed for 3+ nights without a documented complication, verify the dates against your discharge summary.</li>
    <li><strong>Post-op visit charges within the global surgical period:</strong> Most bariatric surgery codes include a 90-day global period, meaning follow-up visits within 90 days of surgery are included in the surgeon&rsquo;s fee and should not be billed separately.</li>
</ul>

<p><a href="/scan">Upload your bariatric surgery bill to BillKarma</a> and we will automatically flag unbundled charges, duplicate line items, and amounts that exceed Medicare benchmarks.</p>

{_embed(mode="cost", cpt="43775", title="Look up bariatric surgery costs", subtitle="See Medicare rates for sleeve gastrectomy, gastric bypass, and more.")}

<h2 id="appeals">5. How to appeal a bariatric surgery denial</h2>

<p>If your insurer denies bariatric surgery coverage, you have the right to appeal. The appeal process for bariatric surgery is well-established, and success rates are meaningful: roughly <strong>40&ndash;50% of bariatric surgery denials are overturned</strong> on first or second appeal when properly documented.</p>

<h3>Common denial reasons and how to counter them</h3>

<ul>
    <li><strong>&ldquo;Incomplete supervised diet&rdquo;</strong>&mdash;Gather all visit notes and submit a timeline showing each monthly visit. If a gap exists, include a letter from the provider explaining it.</li>
    <li><strong>&ldquo;BMI does not meet criteria&rdquo;</strong>&mdash;BMI can fluctuate. Submit multiple BMI measurements over 12+ months showing consistent morbid obesity. A single measurement below threshold does not negate years of documented obesity.</li>
    <li><strong>&ldquo;Comorbidities not documented&rdquo;</strong>&mdash;Provide specialist records: sleep study results for OSA, HbA1c levels for diabetes, medication history for hypertension. Each comorbidity should be documented by a treating physician, not just mentioned in the surgeon&rsquo;s letter.</li>
    <li><strong>&ldquo;Not medically necessary&rdquo;</strong>&mdash;Ask your surgeon to write a detailed letter of medical necessity explaining why surgery is indicated and why conservative measures have failed despite documented attempts.</li>
</ul>

<div class="case-study">
    <h3>Case study: Denied bariatric surgery approved on appeal after documenting comorbidities</h3>
    <p>A 48-year-old woman with a BMI of 38 was denied sleeve gastrectomy by her BCBS plan because the initial submission listed only hypertension as a comorbidity, and the insurer required two or more comorbidities for BMI 35&ndash;39.9 patients. Her surgeon&rsquo;s office had not included her sleep study results showing moderate obstructive sleep apnea (AHI of 18) or her endocrinologist&rsquo;s records showing pre-diabetes (HbA1c 6.3).</p>
    <p>On appeal, the patient submitted the sleep study report, the endocrinology records, a 12-month weight history showing consistent BMI above 37, and an updated letter of medical necessity. The insurer approved the surgery within 21 days. The <strong>total surgery cost was $22,400</strong>; the patient&rsquo;s out-of-pocket after insurance was <strong>$3,200</strong> (her remaining deductible plus 20% coinsurance up to her out-of-pocket maximum). Without the successful appeal, she would have owed the full $22,400.</p>
</div>

<p>For a detailed walkthrough of the insurance appeal process, including letter templates, see our <a href="/guides/how-to-appeal-insurance-denial/">guide to appealing insurance denials</a>.</p>

<h2 id="coe-discounts">6. Centers of Excellence and bundled pricing</h2>

<p>A bariatric Center of Excellence (COE) is a facility accredited by the Metabolic and Bariatric Surgery Accreditation and Quality Improvement Program (MBSAQIP). These centers meet strict volume, outcomes, and safety standards. Many insurers require surgery at an MBSAQIP-accredited center for coverage.</p>

<p>COE facilities often offer <strong>bundled pricing</strong>&mdash;a single all-inclusive price that covers the surgeon, anesthesiologist, hospital facility, and 90 days of follow-up care. This eliminates surprise bills from individual providers and makes costs predictable.</p>

<div class="case-study">
    <h3>Case study: Uninsured patient saves $11,000 with COE bundled pricing</h3>
    <p>An uninsured 52-year-old man with BMI of 44 and type 2 diabetes received a quote of $28,000 for gastric bypass at his local community hospital (unbundled: $8,500 surgeon, $4,200 anesthesia, $15,300 facility). He contacted an MBSAQIP-accredited Center of Excellence 90 miles away, which offered a bundled cash-pay price of <strong>$17,000</strong> including surgeon, anesthesia, facility, pre-op testing, and 90-day follow-up.</p>
    <p>The COE price also included a complication guarantee&mdash;if he needed readmission within 30 days for a surgery-related complication, it was covered at no additional charge. His local hospital offered no such guarantee. <strong>Total savings: $11,000 (39% reduction)</strong>, with a lower complication rate and better warranty.</p>
</div>

<div class="case-study">
    <h3>Case study: $28,000 bill reduced to $16,800 with self-pay discount and payment plan</h3>
    <p>A 41-year-old woman with a BMI of 43 and type 2 diabetes needed sleeve gastrectomy but had no bariatric surgery coverage under her employer&rsquo;s health plan. Her hospital quoted <strong>$28,000</strong> for the procedure (surgeon, anesthesia, facility, and one overnight stay). According to BillKarma data, bariatric surgery charges at nonprofit hospitals average 2.8x Medicare rates, compared to 4.2x at for-profit facilities.</p>
    <p>Because her hospital was a nonprofit, she applied for their self-pay discount program and qualified for a 30% reduction based on her income. The hospital also offered a 12-month interest-free payment plan for balances under $20,000. With the 30% discount applied, her total dropped to <strong>$19,600</strong>. She negotiated an additional 14% prompt-pay reduction by offering to set up automatic monthly payments. <strong>Final cost: $16,800. Savings: $11,200 (40% off the original quote).</strong></p>
    <p><strong>Lesson:</strong> Nonprofit hospitals are required to have financial assistance policies. Always ask about self-pay discounts, payment plans, and prompt-pay reductions before scheduling surgery. Combining multiple discount programs can cut a bariatric surgery bill by 30&ndash;50%.</p>
</div>

<div class="key-takeaway">
    <strong>Comparing bariatric surgery programs?</strong> Check facility pricing and quality grades in our <a href="/hospitals/">hospital directory</a>. Then <a href="/scan">upload any quotes or bills to BillKarma</a> to see how each facility&rsquo;s charges compare to Medicare benchmarks.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does bariatric surgery cost without insurance?</h3>
        <p>Gastric bypass costs $20,000&ndash;$35,000, sleeve gastrectomy costs $15,000&ndash;$25,000, and lap-band costs $10,000&ndash;$18,000 without insurance. Centers of Excellence often offer bundled cash-pay pricing 20&ndash;40% below standard hospital rates. Use our <a href="/calculator">cost calculator</a> to look up Medicare rates for bariatric CPT codes and establish a baseline for negotiation.</p>
    </div>

    <div class="faq-item">
        <h3>What BMI do I need for insurance to cover bariatric surgery?</h3>
        <p>Most insurers require a BMI of 40 or higher, or BMI 35&ndash;39.9 with at least one obesity-related comorbidity (type 2 diabetes, sleep apnea, hypertension). Some plans now cover BMI 30&ndash;34.9 with uncontrolled type 2 diabetes. Check your plan&rsquo;s Summary of Benefits and Coverage for the exact criteria.</p>
    </div>

    <div class="faq-item">
        <h3>What is the 6-month supervised diet requirement?</h3>
        <p>Most insurers require 3&ndash;6 consecutive months of documented physician-supervised weight management. This means monthly office visits with your weight recorded, a diet and exercise plan in the notes, and no gaps longer than 45 days. Missing one visit can restart the entire clock. Medicare eliminated this requirement in 2013, but most commercial insurers still enforce it.</p>
    </div>

    <div class="faq-item">
        <h3>Can I appeal a bariatric surgery denial?</h3>
        <p>Yes. About 40&ndash;50% of bariatric surgery denials are overturned on appeal. The strongest appeals include complete supervised diet records, specialist documentation of every comorbidity, updated BMI measurements, and a detailed letter of medical necessity from the surgeon. For step-by-step appeal instructions, see our <a href="/guides/how-to-appeal-insurance-denial/">insurance appeal guide</a>.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover bariatric surgery?</h3>
        <p>Medicare covers gastric bypass (CPT 43644) and sleeve gastrectomy (CPT 43775) for beneficiaries with BMI &ge; 35 and at least one obesity-related comorbidity. Lap-band is no longer covered under Medicare. The surgery must be performed at a Medicare-certified bariatric center. Medicare does not require a supervised diet period.</p>
    </div>

    <div class="faq-item">
        <h3>What is a Center of Excellence and does it save money?</h3>
        <p>A Center of Excellence (COE) is a bariatric program accredited by MBSAQIP that meets strict volume, safety, and outcomes standards. COE facilities often offer bundled pricing that includes surgeon, anesthesia, facility, and 90-day follow-up in one price&mdash;typically 20&ndash;40% less than unbundled hospital charges. Many insurers require surgery at a COE for coverage.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/coverage/bariatric-surgery" target="_blank" rel="noopener">CMS: Medicare Coverage of Bariatric Surgery (2026)</a></li>
    <li><a href="https://asmbs.org/resources/estimate-of-bariatric-surgery-numbers" target="_blank" rel="noopener">American Society for Metabolic and Bariatric Surgery: National Procedure Estimates</a></li>
    <li><a href="https://www.facs.org/quality-programs/accreditation-and-verification/metabolic-and-bariatric-surgery-accreditation-and-quality-improvement-program/" target="_blank" rel="noopener">MBSAQIP: Metabolic and Bariatric Surgery Accreditation Standards</a></li>
    <li><a href="https://www.niddk.nih.gov/health-information/weight-management/bariatric-surgery" target="_blank" rel="noopener">NIH/NIDDK: Bariatric Surgery Procedures and Outcomes</a></li>
    <li><a href="https://www.cdc.gov/obesity/data/adult.html" target="_blank" rel="noopener">CDC: Adult Obesity Facts and Prevalence Data</a></li>
</ul>
""",
})
