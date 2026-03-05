"""Guide: Outpatient Surgery Costs and Savings."""

from guides import register, _embed

register("outpatient-surgery-costs-how-to-save", {
    "title": "Outpatient Surgery Costs: How Ambulatory Surgery Centers Save You 40&ndash;60% Over Hospitals",
    "meta_description": "Ambulatory surgery centers cost 40-60% less than hospitals for the same procedures. Compare costs for colonoscopy, cataract, hernia, and more. Find an ASC near you.",
    "published": "2026-03-04",
    "author": "BillKarma Team",
    "category": "Medical Bills",
    "faqs": [
        {
            "q": "What is an ambulatory surgery center (ASC) and is it safe?",
            "a": "An ambulatory surgery center (ASC) is an outpatient facility where surgeries and procedures are performed that don't require an overnight hospital stay. ASCs are accredited by the same organizations as hospitals (AAAHC, Joint Commission, or state health departments), follow the same safety protocols, and are inspected regularly by CMS. Complication rates at ASCs are comparable to or lower than hospitals for eligible procedures. Over 28 million procedures are performed at ASCs annually in the US.",
        },
        {
            "q": "How much cheaper are ambulatory surgery centers vs hospitals?",
            "a": "ASCs cost 40-60% less than hospitals for the same procedure on average. A colonoscopy costs $1,200-$1,800 at an ASC vs $3,000-$6,000 at a hospital. Cataract surgery: $2,500-$3,500 at an ASC vs $5,000-$10,000 at a hospital. Hernia repair: $4,000-$6,000 at an ASC vs $10,000-$15,000 at a hospital. The savings come from lower facility fees, faster turnaround, and leaner operations. The surgeon and anesthesiologist are often the same people who operate at the hospital.",
        },
        {
            "q": "Does insurance cover procedures at ambulatory surgery centers?",
            "a": "Yes. All major insurance plans and Medicare cover procedures at ASCs. In fact, many insurers prefer ASCs because they cost less. Some plans have lower copays or coinsurance for ASC procedures vs hospital procedures. Medicare pays ASCs a separate fee schedule that is typically 58-60% of the hospital outpatient rate. Your insurance copay or coinsurance will almost always be lower at an ASC vs a hospital for the same procedure.",
        },
        {
            "q": "What procedures can be done at an ASC?",
            "a": "Over 3,500 procedure types can be performed at ASCs, including: colonoscopy and upper endoscopy, cataract surgery, orthopedic procedures (arthroscopy, rotator cuff repair), hernia repair, gallbladder removal, tonsillectomy, carpal tunnel release, knee and hip replacement (at some ASCs), spinal procedures, pain management injections, oral surgery, and many plastic surgery procedures. About 60% of all surgeries can be performed in an outpatient setting.",
        },
        {
            "q": "How do I find an ambulatory surgery center near me?",
            "a": "Search Medicare's Care Compare tool at medicare.gov/care-compare for ASCs in your area with quality ratings. Your insurer's provider directory lists in-network ASCs. Ask your surgeon: 'Do you operate at an ambulatory surgery center?' Many surgeons have privileges at both hospitals and ASCs and can schedule you at either. The ASC Quality Collaboration website also maintains a directory of accredited facilities.",
        },
    ],
    "body": f"""
<p class="lead">The same surgeon performs the same knee arthroscopy with the same anesthesiologist &mdash; but the bill is <strong>$4,500 at an ambulatory surgery center</strong> and <strong>$12,000 at a hospital</strong>. Why? Hospitals charge massive facility fees that ASCs don&rsquo;t. Over 28 million procedures are now done at ASCs annually, and choosing one over a hospital is the single easiest way to cut surgery costs by 40&ndash;60%. Here&rsquo;s everything you need to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-comparison">ASC vs. hospital cost comparison</a></li>
        <li><a href="#why-cheaper">Why ASCs cost so much less</a></li>
        <li><a href="#safety">Safety and quality: ASCs vs. hospitals</a></li>
        <li><a href="#what-procedures">What can be done at an ASC</a></li>
        <li><a href="#find-asc">How to find and choose an ASC</a></li>
        <li><a href="#negotiate">Negotiating surgery costs</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-comparison">1. ASC vs. hospital cost comparison</h2>

<table>
    <thead>
        <tr><th>Procedure</th><th>ASC average cost</th><th>Hospital average cost</th><th>Savings at ASC</th></tr>
    </thead>
    <tbody>
        <tr><td>Colonoscopy</td><td>$1,200&ndash;$1,800</td><td>$3,000&ndash;$6,000</td><td>50&ndash;70%</td></tr>
        <tr><td>Cataract surgery (one eye)</td><td>$2,500&ndash;$3,500</td><td>$5,000&ndash;$10,000</td><td>50&ndash;65%</td></tr>
        <tr><td>Hernia repair (inguinal)</td><td>$4,000&ndash;$6,000</td><td>$10,000&ndash;$15,000</td><td>55&ndash;60%</td></tr>
        <tr><td>Knee arthroscopy</td><td>$4,500&ndash;$7,000</td><td>$12,000&ndash;$18,000</td><td>55&ndash;65%</td></tr>
        <tr><td>Carpal tunnel release</td><td>$2,000&ndash;$3,500</td><td>$5,000&ndash;$8,000</td><td>55&ndash;60%</td></tr>
        <tr><td>Rotator cuff repair</td><td>$6,000&ndash;$10,000</td><td>$15,000&ndash;$25,000</td><td>55&ndash;60%</td></tr>
        <tr><td>Gallbladder removal</td><td>$5,000&ndash;$8,000</td><td>$12,000&ndash;$20,000</td><td>55&ndash;60%</td></tr>
        <tr><td>Total knee replacement</td><td>$15,000&ndash;$22,000</td><td>$35,000&ndash;$50,000</td><td>50&ndash;60%</td></tr>
    </tbody>
</table>

<div class="bill-example">
    <div class="bill-header">Same hernia repair, different settings</div>
    <div class="line-item">
        <span>Surgeon fee (both settings)</span>
        <span>$2,800</span>
    </div>
    <div class="line-item">
        <span>Anesthesia fee (both settings)</span>
        <span>$1,200</span>
    </div>
    <div class="line-item">
        <span>ASC facility fee</span>
        <span>$1,500</span>
    </div>
    <div class="line-item flagged">
        <span>Hospital facility fee</span>
        <span>$8,500</span>
    </div>
    <div class="line-total">
        <span>ASC total: $5,500 vs Hospital total: $12,500 (56% savings)</span>
        <span></span>
    </div>
</div>

<h2 id="why-cheaper">2. Why ASCs cost so much less</h2>

<ol>
    <li><strong>Lower facility fees.</strong> This is the #1 reason. Hospital facility fees are 2&ndash;5x higher than ASC facility fees because hospitals spread their massive overhead (ER, ICU, administration, 24/7 staffing) across all services.</li>
    <li><strong>Focused operations.</strong> ASCs specialize in specific procedure types. This focus drives efficiency &mdash; faster turnover between cases, specialized equipment, and optimized workflows.</li>
    <li><strong>Lower overhead.</strong> ASCs don&rsquo;t have ERs, ICUs, or the administrative burden of a full hospital. Staff-to-patient ratios are leaner.</li>
    <li><strong>Competitive market.</strong> ASCs compete on price and quality because patients can choose. Hospitals often have captive patients through physician employment and network restrictions.</li>
</ol>

<h2 id="safety">3. Safety and quality: ASCs vs. hospitals</h2>

<p>ASCs are held to the same safety standards as hospitals:</p>

<ul>
    <li><strong>Accreditation:</strong> ASCs must be accredited by AAAHC, Joint Commission, or state health departments</li>
    <li><strong>CMS certification:</strong> ASCs participating in Medicare must meet CMS Conditions for Coverage</li>
    <li><strong>Complication rates:</strong> Studies show complication rates at ASCs are comparable to or lower than hospitals for eligible procedures. A 2023 JAMA study found no significant difference in 30-day readmission rates.</li>
    <li><strong>Patient satisfaction:</strong> ASCs consistently score higher on patient satisfaction surveys than hospital outpatient departments.</li>
</ul>

<div class="key-takeaway">
    <strong>The surgeon matters more than the setting.</strong> For procedures eligible to be done at an ASC, your outcome depends primarily on your surgeon&rsquo;s skill and experience, not whether you&rsquo;re in a hospital or ASC. Many surgeons operate at both. Ask your surgeon: &ldquo;Do you perform this procedure at an ambulatory surgery center?&rdquo; If yes, you can get the same surgeon at a fraction of the cost.
</div>

<h2 id="what-procedures">4. What can be done at an ASC</h2>

<p><strong>Commonly done at ASCs:</strong></p>
<ul>
    <li>GI: Colonoscopy, upper endoscopy</li>
    <li>Ophthalmology: Cataract surgery, glaucoma procedures</li>
    <li>Orthopedics: Arthroscopy (knee, shoulder), rotator cuff, ACL, carpal tunnel, trigger finger</li>
    <li>General surgery: Hernia repair, gallbladder removal, breast biopsy</li>
    <li>ENT: Tonsillectomy, sinus surgery, ear tubes</li>
    <li>Pain management: Epidural injections, nerve blocks</li>
    <li>Spine: Discectomy, laminectomy (at specialized ASCs)</li>
    <li>Joint replacement: Total knee and hip (at high-acuity ASCs)</li>
</ul>

<p><strong>Requires a hospital:</strong></p>
<ul>
    <li>Open heart surgery</li>
    <li>Major organ transplants</li>
    <li>Procedures requiring overnight ICU monitoring</li>
    <li>Complex surgeries with high complication risk</li>
    <li>Patients with severe comorbidities requiring hospital-level monitoring</li>
</ul>

<h2 id="find-asc">5. How to find and choose an ASC</h2>

<ol>
    <li><strong>Ask your surgeon.</strong> &ldquo;Do you operate at an ambulatory surgery center? Can we schedule this there instead of the hospital?&rdquo; Many surgeons prefer ASCs for efficiency.</li>
    <li><strong>Search Medicare Care Compare.</strong> <a href="https://www.medicare.gov/care-compare/" target="_blank" rel="noopener">medicare.gov/care-compare</a> lists ASCs with quality ratings and inspection results.</li>
    <li><strong>Check your insurance network.</strong> Verify the ASC is in-network. Most insurers include ASCs and may offer lower cost-sharing.</li>
    <li><strong>Get a Good Faith Estimate.</strong> Request a written cost estimate from the ASC. Compare it to the hospital quote for the same procedure.</li>
    <li><strong>Verify accreditation.</strong> Ensure the ASC is accredited by AAAHC, Joint Commission, or your state health department.</li>
</ol>

<h2 id="negotiate">6. Negotiating surgery costs</h2>

<p>Whether at an ASC or hospital, you can negotiate surgery costs:</p>

<ol>
    <li><strong>Get multiple quotes.</strong> Get Good Faith Estimates from at least 2 ASCs and 1 hospital for comparison.</li>
    <li><strong>Ask for a bundled price.</strong> Request an all-inclusive price covering surgeon, anesthesiologist, facility, and any implants or supplies. Bundled pricing eliminates surprise bills from multiple providers.</li>
    <li><strong>Compare to Medicare rates.</strong> Use the <a href="/calculator">BillKarma calculator</a> to check what Medicare pays. A fair self-pay price is 150&ndash;250% of Medicare.</li>
    <li><strong>Ask about cash-pay discounts.</strong> ASCs frequently offer 10&ndash;20% cash-pay discounts since they avoid insurance billing costs.</li>
    <li><strong>Negotiate before surgery.</strong> Your leverage is strongest before the procedure. After surgery, you&rsquo;re negotiating from a weaker position. See our <a href="/guides/negotiate-medical-costs-before-procedure">pre-procedure negotiation guide</a>.</li>
</ol>

<div class="case-study">
    <h3>Case study: $18,000 saved on knee replacement</h3>
    <p><strong>Situation:</strong> Bill, 58, needed a total knee replacement. His orthopedic surgeon operated at both a hospital ($42,000 quote) and a new high-acuity ASC ($18,000 bundled quote). Same surgeon, same implant, same anesthesiologist.</p>
    <p><strong>What he did:</strong> Chose the ASC after verifying it was accredited and in-network. Requested a bundled all-inclusive price. Negotiated a 5% prompt-pay discount for paying within 30 days.</p>
    <p><strong>Result:</strong> Total cost: $17,100 at the ASC vs. $42,000 at the hospital. Same-day discharge. No complications. <strong>Savings: $24,900.</strong></p>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/health-safety-standards/asc" target="_blank" rel="noopener">CMS: Ambulatory Surgical Centers (ASC) Quality and Safety</a></li>
    <li><a href="https://www.ascassociation.org/advancingsurgicalcare/aboutascs/industryoverview" target="_blank" rel="noopener">ASC Association: Industry Overview and Statistics</a></li>
    <li><a href="https://www.medpac.gov/document/ambulatory-surgical-center-services/" target="_blank" rel="noopener">MedPAC: Ambulatory Surgical Center Services Payment Report</a></li>
    <li><a href="https://www.medicare.gov/care-compare/" target="_blank" rel="noopener">CMS Care Compare: Find and Compare ASCs</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/outpatient-facility-fees/" target="_blank" rel="noopener">KFF: Outpatient Facility Fees and Site-of-Service Pricing</a></li>
</ul>
""",
})
