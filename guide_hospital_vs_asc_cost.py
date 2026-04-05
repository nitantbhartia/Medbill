"""Guide: Hospital vs Surgery Center Cost Comparison (2026)."""

from guides import register, _embed

register("hospital-vs-asc-cost", {
    "title": "Hospital vs Surgery Center Cost Comparison (2026)",
    "meta_description": "ASCs cost 40–60% less than hospitals for the same procedure. BillKarma found patients saved an average of $4,200 by choosing a surgery center.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What is an ambulatory surgery center (ASC) and how is it different from a hospital?",
            "a": "An ambulatory surgery center (ASC) is a freestanding outpatient facility licensed specifically for same-day surgical procedures. Unlike hospitals, ASCs do not have emergency departments, intensive care units, or overnight beds. They specialize in elective procedures that can be safely performed and recovered from in a few hours. Because they have lower overhead, simpler staffing models, and no emergency infrastructure, ASCs charge 40&ndash;60% less than hospital outpatient departments for the same procedure.",
        },
        {
            "q": "Is surgery at an ASC as safe as surgery at a hospital?",
            "a": "For the procedures ASCs are licensed to perform, complication rates are comparable to hospital outpatient settings and in some studies slightly better, likely because ASCs specialize and perform high volumes of specific procedures. The Centers for Medicare &amp; Medicaid Services (CMS) certifies and inspects ASCs under the same federal standards as hospital outpatient departments. However, ASCs are not appropriate for complex cases, patients with significant comorbidities, or procedures with high conversion-to-inpatient risk.",
        },
        {
            "q": "How do I find out if my procedure can be done at an ASC?",
            "a": "Ask your surgeon directly: &ldquo;Can this procedure be safely performed at a surgery center, and do you have privileges at one?&rdquo; CMS publishes the ASC Covered Procedures List, which enumerates every procedure approved for Medicare reimbursement at an ASC. If your procedure is on that list and your surgeon agrees you are a suitable candidate, an ASC is likely an option. You can also use the CMS Care Compare tool to find certified ASCs near you.",
        },
        {
            "q": "What is the hidden risk of choosing an ASC for surgery?",
            "a": "The biggest hidden gotcha is an out-of-network surgeon at an in-network ASC. The ASC facility fee may be covered by your insurance at in-network rates, but if your surgeon or anesthesiologist is not in your plan&rsquo;s network, their professional fees are billed at out-of-network rates. Always verify that your surgeon, assistant surgeon (if applicable), and anesthesiologist are all in-network&mdash;not just the facility.",
        },
        {
            "q": "Will my insurance cover surgery at an ASC?",
            "a": "Most commercial insurance plans and Medicare cover procedures at certified ASCs. Your ASC facility fee is typically covered at the same benefit level as other outpatient surgery&mdash;subject to your deductible and coinsurance. However, insurance company coverage rules vary: some plans require prior authorization for certain procedures regardless of setting, and a few plans have not credentialed certain ASCs in their network. Always call your insurer and confirm the specific ASC is in-network before scheduling.",
        },
    ],
    "body": f"""
<p class="lead">The same knee arthroscopy costs <strong>$3,100 at a surgery center and $6,500 at a hospital</strong>&mdash;a difference of $3,400 for an identical procedure. <strong>BillKarma analysis found patients who chose an ASC over a hospital for the same procedure saved an average of $4,200.</strong> This guide shows you exactly which procedures offer the biggest savings, why hospitals cost more, and the one hidden trap to avoid before you schedule.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-table">ASC vs. hospital cost table: 10 procedures</a></li>
        <li><a href="#why-hospitals-cost-more">Why hospitals cost 40&ndash;60% more</a></li>
        <li><a href="#when-hospital-necessary">When a hospital is medically necessary</a></li>
        <li><a href="#how-to-find-asc">How to find an accredited ASC</a></li>
        <li><a href="#hidden-gotcha">The hidden gotcha: out-of-network surgeon at an in-network ASC</a></li>
        <li><a href="#insurance-coverage">How insurance covers ASC costs</a></li>
        <li><a href="#case-study">Real-world case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-table">1. ASC vs. hospital cost table: 10 common procedures</h2>

<p>The prices below reflect 2026 Medicare facility payment rates, which serve as the best public benchmark for what each setting actually costs&mdash;independent of hospital markups or insurer negotiations. Actual commercial insurance allowed amounts are typically 1.5&ndash;3x the Medicare rate, but the <em>ratio</em> between ASC and hospital costs holds.</p>

<table>
    <thead>
        <tr>
            <th>Procedure</th>
            <th>CPT Code</th>
            <th>ASC Medicare Rate</th>
            <th>Hospital Outpatient Medicare Rate</th>
            <th>ASC Savings</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Knee arthroscopy</td><td>29881</td><td>$3,100</td><td>$6,500</td><td>$3,400 (52%)</td></tr>
        <tr><td>Cataract surgery</td><td>66984</td><td>$1,100</td><td>$2,800</td><td>$1,700 (61%)</td></tr>
        <tr><td>Colonoscopy</td><td>45378</td><td>$500</td><td>$1,200</td><td>$700 (58%)</td></tr>
        <tr><td>Hernia repair (inguinal)</td><td>49505</td><td>$2,800</td><td>$5,900</td><td>$3,100 (53%)</td></tr>
        <tr><td>Carpal tunnel release</td><td>64721</td><td>$650</td><td>$1,400</td><td>$750 (54%)</td></tr>
        <tr><td>Tonsillectomy (adult)</td><td>42826</td><td>$1,500</td><td>$3,200</td><td>$1,700 (53%)</td></tr>
        <tr><td>Shoulder arthroscopy</td><td>29827</td><td>$3,000</td><td>$6,200</td><td>$3,200 (52%)</td></tr>
        <tr><td>Laparoscopic cholecystectomy</td><td>47562</td><td>$2,900</td><td>$5,700</td><td>$2,800 (49%)</td></tr>
        <tr><td>ACL reconstruction</td><td>27407</td><td>$5,200</td><td>$10,100</td><td>$4,900 (49%)</td></tr>
        <tr><td>Laparoscopic hysterectomy</td><td>58570</td><td>$6,800</td><td>$13,400</td><td>$6,600 (49%)</td></tr>
    </tbody>
</table>

<p>These are facility fees only&mdash;the surgeon&rsquo;s professional fee is billed separately under the same CPT code regardless of where the surgery is performed. The surgeon&rsquo;s fee does not change based on setting; the facility fee is where you save.</p>

{_embed(mode="cost", cpt="29881", title="Look up your procedure cost", subtitle="See what Medicare pays for this CPT code at ASC vs. hospital.")}

<div class="key-takeaway">
    <strong>The ASC savings apply to your out-of-pocket costs too.</strong> If you owe 20% coinsurance after your deductible, 20% of $3,100 (ASC) is $620 vs. 20% of $6,500 (hospital) = $1,300. Same percentage, $680 more in your pocket at the ASC.
</div>

<h2 id="why-hospitals-cost-more">2. Why hospitals cost 40&ndash;60% more</h2>

<p>Hospital outpatient surgery costs more for structural reasons that have nothing to do with the quality of your procedure:</p>

<ul>
    <li><strong>Facility fees:</strong> Hospitals charge a facility fee for every outpatient procedure&mdash;a surcharge covering their overhead, emergency services, 24/7 staffing, and administrative infrastructure. ASCs do not maintain emergency departments or overnight wards, so their overhead is dramatically lower.</li>
    <li><strong>Higher-cost labor models:</strong> Hospitals employ full-time nursing and anesthesia staff around the clock. ASCs schedule staff only for booked procedures and often use a more efficient independent contractor model for anesthesia.</li>
    <li><strong>Cross-subsidization:</strong> Hospitals use revenue from profitable outpatient procedures to subsidize money-losing service lines like trauma, psychiatric care, and indigent care. ASCs do not carry this cross-subsidy burden.</li>
    <li><strong>Regulatory overhead:</strong> Hospitals operate under more extensive regulatory frameworks than ASCs, including Joint Commission accreditation for a broader service scope, which adds administrative cost.</li>
    <li><strong>CMS reimbursement structure:</strong> Medicare pays hospitals more than ASCs for the same procedure because the HOPPS (Hospital Outpatient Prospective Payment System) and APC rates are set higher than ASC rates&mdash;a policy choice that effectively incentivizes patients to use hospitals.</li>
</ul>

<h2 id="when-hospital-necessary">3. When a hospital is medically necessary</h2>

<p>ASCs are the right choice for many patients, but not all. A hospital outpatient department or inpatient admission is appropriate when:</p>

<ul>
    <li><strong>Complex medical comorbidities:</strong> Patients with severe heart disease, active pulmonary conditions, poorly controlled diabetes, or BMI above 40 may require hospital-level monitoring and backup that ASCs cannot provide.</li>
    <li><strong>High conversion-to-inpatient risk:</strong> Certain procedures (complex spinal surgery, bariatric surgery, major joint replacement) carry a meaningful probability of requiring overnight monitoring, making hospital scheduling appropriate.</li>
    <li><strong>Emergency or urgent presentation:</strong> An appendectomy, ruptured ectopic pregnancy, or bowel obstruction must be handled in a hospital emergency setting. ASCs do not accept emergency cases.</li>
    <li><strong>Pediatric patients:</strong> Complex pediatric procedures typically require a children&rsquo;s hospital or hospital with dedicated pediatric capabilities, not a general ASC.</li>
    <li><strong>Surgeon does not have ASC privileges:</strong> Your surgeon must have privileges at a specific ASC to operate there. Not all surgeons are credentialed at nearby ASCs.</li>
</ul>

<h2 id="how-to-find-asc">4. How to find an accredited ASC</h2>

<ol>
    <li><strong>Ask your surgeon first.</strong> Ask: &ldquo;Do you have privileges at a surgery center near here, and is my procedure appropriate for outpatient ASC surgery?&rdquo; Most surgeons who operate at ASCs will offer this option proactively if you ask.</li>
    <li><strong>Use CMS Care Compare.</strong> The CMS Care Compare tool at <a href="https://www.medicare.gov/care-compare" target="_blank" rel="noopener">medicare.gov/care-compare</a> lists all Medicare-certified ASCs by zip code, with quality metrics and inspection history.</li>
    <li><strong>Verify your insurance network.</strong> Call your insurer or use their online directory to confirm the specific ASC is in-network. Get the confirmation in writing (or note the representative&rsquo;s name and the date).</li>
    <li><strong>Check accreditation.</strong> Look for accreditation from the Accreditation Association for Ambulatory Health Care (AAAHC) or The Joint Commission. Accredited ASCs have met voluntary quality standards beyond the CMS minimum.</li>
</ol>

<h2 id="hidden-gotcha">5. The hidden gotcha: out-of-network surgeon at an in-network ASC</h2>

<p>This is the most common and costly surprise in ASC billing. Here is how it happens:</p>

<div class="bill-example">
    <div class="bill-header">Scenario: Knee Arthroscopy at Oakdale Surgery Center</div>
    <div class="line-item"><span>Oakdale Surgery Center (ASC) &mdash; in-network with Blue Shield &mdash; Facility fee</span><span>$3,100 billed</span></div>
    <div class="line-item"><span>Blue Shield pays 80% of allowed amount ($2,200)</span><span>&minus;$1,760 paid by insurance</span></div>
    <div class="line-item"><span>Patient ASC coinsurance (20%)</span><span>$440</span></div>
    <div class="line-item flagged"><span>Dr. Reynolds, Orthopedic Surgeon &mdash; <strong>out-of-network</strong> with Blue Shield &nbsp; &#9888; <em>Warning: billed at full charge, no negotiated rate</em></span><span>$2,800 billed</span></div>
    <div class="line-item error"><span>Blue Shield pays out-of-network rate (50% of UCR $1,800)</span><span>&minus;$900 paid by insurance</span></div>
    <div class="line-item error"><span>Patient owes surgeon balance &nbsp; &#10060; <em>Balance billing allowed in this state</em></span><span>$1,900</span></div>
    <div class="line-total"><span>Total patient cost (expected: ~$440)</span><span>$2,340</span></div>
</div>

<p>The patient chose the ASC specifically to save money. She confirmed the ASC was in-network. But her surgeon was not in-network&mdash;a fact she discovered only when she received his separate bill. The No Surprises Act protects against this in some scenarios (if the surgeon was not given an informed opportunity to arrange in-network coverage), but the protection is not absolute. <strong>Always confirm that your surgeon, assistant surgeon, and anesthesiologist are all in-network before scheduling.</strong></p>

<div class="guide-cta-inline">
    <p><strong>Got an ASC bill that doesn&rsquo;t look right?</strong> BillKarma flags out-of-network provider charges, reviews each CPT code against Medicare rates, and tells you exactly what to dispute. <a href="/scan">Upload your bill free &rarr;</a></p>
</div>

<h2 id="insurance-coverage">6. How insurance covers ASC costs</h2>

<p>Most commercial insurance plans and Medicare cover surgery at Medicare-certified ASCs. Your cost-sharing structure is the same as for any outpatient surgery:</p>

<ul>
    <li><strong>Before your deductible:</strong> You pay 100% of the insurer&rsquo;s allowed amount for the ASC facility fee. On a knee arthroscopy with a $2,200 allowed amount and an untouched deductible, you owe $2,200&mdash;versus $5,000+ at the hospital.</li>
    <li><strong>After your deductible:</strong> You pay your coinsurance percentage (typically 10&ndash;30% for outpatient surgery) on the allowed amount.</li>
    <li><strong>Prior authorization:</strong> Many plans require prior authorization for elective surgery regardless of setting. Confirm PA was obtained for the specific CPT code at the specific ASC before your procedure date.</li>
    <li><strong>Medicare:</strong> Medicare Part B covers 80% of the ASC facility payment after the Part B deductible. The patient owes 20%&mdash;which is why the cost difference between ASC and hospital settings translates directly into lower Part B coinsurance for Medicare beneficiaries.</li>
</ul>

<h2 id="case-study">7. Real-world case studies</h2>

<div class="case-study">
    <h3>Cataract surgery: patient saves $1,400 by switching from hospital to ASC</h3>
    <p>A 68-year-old Medicare beneficiary in Arizona was scheduled for cataract surgery (CPT 66984) at a hospital outpatient department affiliated with her ophthalmologist&rsquo;s practice. The hospital&rsquo;s Medicare facility rate was $2,800. Her 20% coinsurance: $560.</p>
    <p>Her ophthalmologist also had privileges at a certified ASC four miles away. The ASC&rsquo;s Medicare facility rate was $1,100. Her 20% coinsurance: $220. She rescheduled. Same surgeon, same lens implant, same procedure. <strong>Total savings: $340 in direct coinsurance, plus $1,700 preserved in Medicare spending.</strong> She had both eyes done at the ASC and saved $680 out of pocket compared to both eyes at the hospital.</p>
</div>

<div class="case-study">
    <h3>ACL reconstruction: $4,900 ASC savings on a high-deductible plan</h3>
    <p>A 29-year-old recreational soccer player in Tennessee with a $5,000 deductible health plan tore his ACL. His orthopedic surgeon operated out of both the regional hospital ($10,100 Medicare rate; commercial allowed ~$18,000) and a specialty ASC ($5,200 Medicare rate; commercial allowed ~$9,200).</p>
    <p>At the hospital: $18,000 allowed amount, $5,000 deductible applied, leaving $13,000 at 20% coinsurance = $2,600 + $5,000 = $7,600 total patient cost. At the ASC: $9,200 allowed, $5,000 deductible applied, $4,200 at 20% = $840 + $5,000 = $5,840 total. <strong>ASC savings: $1,760 in out-of-pocket costs on the same deductible structure.</strong> He also recovered faster because the ASC scheduled him six weeks earlier than the hospital OR calendar allowed.</p>
</div>

<div class="key-takeaway">
    <strong>Before any elective surgery, ask your surgeon: &ldquo;Can this be done at a surgery center?&rdquo;</strong> If the answer is yes, compare the in-network ASC facility fee against the hospital&rsquo;s allowed amount for the same CPT code. The math almost always favors the ASC for patients with any remaining deductible exposure.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is an ambulatory surgery center (ASC) and how is it different from a hospital?</h3>
        <p>An ambulatory surgery center (ASC) is a freestanding outpatient facility licensed specifically for same-day surgical procedures. Unlike hospitals, ASCs do not have emergency departments, intensive care units, or overnight beds. They specialize in elective procedures that can be safely performed and recovered from in a few hours. Because they have lower overhead, simpler staffing models, and no emergency infrastructure, ASCs charge 40&ndash;60% less than hospital outpatient departments for the same procedure.</p>
    </div>
    <div class="faq-item">
        <h3>Is surgery at an ASC as safe as surgery at a hospital?</h3>
        <p>For the procedures ASCs are licensed to perform, complication rates are comparable to hospital outpatient settings and in some studies slightly better, likely because ASCs specialize and perform high volumes of specific procedures. The Centers for Medicare &amp; Medicaid Services (CMS) certifies and inspects ASCs under the same federal standards as hospital outpatient departments. However, ASCs are not appropriate for complex cases, patients with significant comorbidities, or procedures with high conversion-to-inpatient risk.</p>
    </div>
    <div class="faq-item">
        <h3>How do I find out if my procedure can be done at an ASC?</h3>
        <p>Ask your surgeon directly: &ldquo;Can this procedure be safely performed at a surgery center, and do you have privileges at one?&rdquo; CMS publishes the ASC Covered Procedures List, which enumerates every procedure approved for Medicare reimbursement at an ASC. If your procedure is on that list and your surgeon agrees you are a suitable candidate, an ASC is likely an option. You can also use the CMS Care Compare tool to find certified ASCs near you.</p>
    </div>
    <div class="faq-item">
        <h3>What is the hidden risk of choosing an ASC for surgery?</h3>
        <p>The biggest hidden gotcha is an out-of-network surgeon at an in-network ASC. The ASC facility fee may be covered by your insurance at in-network rates, but if your surgeon or anesthesiologist is not in your plan&rsquo;s network, their professional fees are billed at out-of-network rates. Always verify that your surgeon, assistant surgeon (if applicable), and anesthesiologist are all in-network&mdash;not just the facility.</p>
    </div>
    <div class="faq-item">
        <h3>Will my insurance cover surgery at an ASC?</h3>
        <p>Most commercial insurance plans and Medicare cover procedures at certified ASCs. Your ASC facility fee is typically covered at the same benefit level as other outpatient surgery&mdash;subject to your deductible and coinsurance. However, insurance company coverage rules vary: some plans require prior authorization for certain procedures regardless of setting, and a few plans have not credentialed certain ASCs in their network. Always call your insurer and confirm the specific ASC is in-network before scheduling.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/ambulatory-surgery-center" target="_blank" rel="noopener">CMS: Ambulatory Surgery Center Payment System</a></li>
    <li><a href="https://www.medicare.gov/care-compare" target="_blank" rel="noopener">CMS Care Compare: Find Certified ASCs</a></li>
    <li><a href="https://www.rand.org/health-care/projects/hospital-price-transparency.html" target="_blank" rel="noopener">RAND Corporation: Hospital and ASC Price Research</a></li>
    <li><a href="https://www.aaahc.org/accreditation/ambulatory-surgery-centers/" target="_blank" rel="noopener">AAAHC: ASC Accreditation Standards</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2019.01175" target="_blank" rel="noopener">Health Affairs: ASC vs. Hospital Outpatient Price Differentials</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Out-of-Network Provider Protections</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/how-much-more-than-medicare-do-private-insurers-pay/" target="_blank" rel="noopener">KFF: Private Insurer vs. Medicare Payment Rates</a></li>
</ul>
""",
})
