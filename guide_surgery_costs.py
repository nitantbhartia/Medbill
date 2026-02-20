"""Guide: How Much Does Surgery Cost?"""

from guides import register, _embed

register("how-much-does-surgery-cost", {
    "title": "How Much Does Surgery Cost? A Guide to Common Procedure Prices",
    "meta_description": "Surgery costs range from $3,500 to $100,000+ depending on procedure and location. Learn what drives costs, compare prices, and find ways to save thousands.",
    "published": "2026-02-20",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "Why is surgery so expensive?",
            "a": "Surgery bills include charges from multiple sources: the surgeon's fee, a facility fee (for using the operating room), anesthesia billed in 15-minute time units, lab work, imaging, and supplies or implants. The facility fee alone typically accounts for 50-60% of the total bill. Hospitals also apply chargemaster markups that can be 3-10x what Medicare pays for the same procedure. The combination of multiple billing sources and high markups is why surgery is the most expensive medical service most people encounter.",
        },
        {
            "q": "Can I negotiate surgery costs before the procedure?",
            "a": "Yes, and it is much easier to negotiate before surgery than after. Ask for a good faith estimate (required under the No Surprises Act for self-pay patients), then compare it to Medicare rates and ambulatory surgery center pricing. Many hospitals will offer a self-pay discount of 30-60% if you ask. You can also ask your surgeon if the procedure can be performed at a lower-cost ambulatory surgery center instead of a hospital.",
        },
        {
            "q": "What is a facility fee on a surgery bill?",
            "a": "A facility fee is what the hospital or surgery center charges for using the operating room, recovery area, nursing staff, and equipment. It is separate from the surgeon's fee and the anesthesia charge. Facility fees are typically the largest single item on a surgery bill, accounting for 50-60% of the total. Hospital facility fees are generally 2-4x higher than ambulatory surgery center facility fees for the same procedure.",
        },
        {
            "q": "Why does anesthesia cost so much?",
            "a": "Anesthesia is billed using a formula: base units (set by procedure complexity) plus time units (one unit per 15 minutes of anesthesia). Each unit is typically billed at $120-$200 at hospital rates. A 90-minute procedure might have 4 base units plus 6 time units, totaling 10 units at $150 each, or $1,500. Common billing errors include rounding up partial time units and billing for more time than the operative report shows.",
        },
        {
            "q": "What if I can't afford my surgery bill?",
            "a": "You have several options. First, ask for the self-pay or uninsured discount (30-60% off at most hospitals). Second, apply for financial assistance at nonprofit hospitals, which are required to have charity care programs. Third, negotiate a lump-sum settlement at 40-60% of the bill. Fourth, ask about a zero-interest payment plan. Finally, compare your charges to Medicare rates and dispute any items billed at more than 3x the Medicare rate.",
        },
        {
            "q": "What is the difference between a hospital and an ambulatory surgery center?",
            "a": "An ambulatory surgery center (ASC) is a facility designed specifically for outpatient surgeries. ASCs cost 40-60% less than hospitals for the same procedure because they have lower overhead, no emergency department to subsidize, and more efficient scheduling. Not all procedures can be done at an ASC (complex surgeries or patients with serious health conditions may require a hospital), but many common outpatient surgeries can be performed safely at either setting.",
        },
    ],
    "body": f"""
<p class="lead">The average outpatient surgery costs <strong>$15,000&ndash;$25,000</strong> before insurance. But the same knee arthroscopy that costs $8,500 at one hospital might cost $45,000 at the hospital across town. Surgery bills are the single largest medical expense most people face, and they&rsquo;re also the most negotiable. Here&rsquo;s what every surgery bill includes, what common procedures actually cost, and how to avoid overpaying.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#whats-on-a-surgery-bill">What&rsquo;s on a surgery bill (the 6 components)</a></li>
        <li><a href="#common-surgery-costs">Common outpatient surgery costs</a></li>
        <li><a href="#hospital-vs-asc">Hospital vs. ambulatory surgery center</a></li>
        <li><a href="#real-surgery-bill">A real surgery bill, annotated</a></li>
        <li><a href="#anesthesia-billing">Understanding anesthesia billing</a></li>
        <li><a href="#lower-your-cost">5 ways to lower your surgery cost</a></li>
        <li><a href="#case-studies">Real savings: 3 case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="whats-on-a-surgery-bill">1. What&rsquo;s on a surgery bill (the 6 components)</h2>

<p>A surgery bill isn&rsquo;t one charge&mdash;it&rsquo;s a collection of separate bills from different sources. Understanding the pieces is the first step to finding where you&rsquo;re overpaying.</p>

<table>
    <thead>
        <tr><th>Component</th><th>What It Covers</th><th>Typical % of Total Bill</th></tr>
    </thead>
    <tbody>
        <tr><td>Facility fee</td><td>Operating room time, recovery room, nursing staff, equipment</td><td>50&ndash;60%</td></tr>
        <tr><td>Surgeon&rsquo;s fee</td><td>The surgeon&rsquo;s professional services for performing the procedure</td><td>15&ndash;25%</td></tr>
        <tr><td>Anesthesia</td><td>Anesthesiologist or CRNA services, billed in 15-minute time units</td><td>10&ndash;15%</td></tr>
        <tr><td>Lab and pathology</td><td>Pre-operative blood work, tissue analysis if applicable</td><td>3&ndash;5%</td></tr>
        <tr><td>Imaging</td><td>Pre-operative imaging, intra-operative fluoroscopy or X-rays</td><td>3&ndash;5%</td></tr>
        <tr><td>Supplies, implants, and medications</td><td>Surgical supplies, any implanted hardware, anesthesia drugs, pain medication</td><td>5&ndash;10%</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The facility fee is the biggest target for savings.</strong> It makes up over half of most surgery bills and is where hospital-vs.-ASC pricing differences are the most dramatic. A facility fee of $12,000 at a hospital might be $4,000 at an ambulatory surgery center for the same procedure.
</div>

<p>Each component comes from a different billing source. The surgeon bills separately from the hospital. The anesthesiologist bills separately from both. This means you may receive three or more separate bills for a single surgery&mdash;make sure you <a href="/guides/how-to-read-your-medical-bill">review each one individually</a>.</p>

<h2 id="common-surgery-costs">2. Common outpatient surgery costs</h2>

<p>Here&rsquo;s what five of the most common outpatient surgeries cost, comparing the Medicare rate (what the federal government pays) to typical hospital and ambulatory surgery center (ASC) charges:</p>

<table>
    <thead>
        <tr><th>Procedure</th><th>CPT Code</th><th>Medicare Rate</th><th>Typical Hospital Charge</th><th>Typical ASC Charge</th></tr>
    </thead>
    <tbody>
        <tr><td>Knee arthroscopy (meniscectomy)</td><td>29881</td><td>~$3,800</td><td>$15,000&ndash;$45,000</td><td>$6,000&ndash;$15,000</td></tr>
        <tr><td>Gallbladder removal (laparoscopic)</td><td>47562</td><td>~$5,200</td><td>$18,000&ndash;$55,000</td><td>$8,000&ndash;$18,000</td></tr>
        <tr><td>Hernia repair (inguinal)</td><td>49505</td><td>~$4,100</td><td>$12,000&ndash;$35,000</td><td>$5,000&ndash;$12,000</td></tr>
        <tr><td>Cataract surgery (with lens implant)</td><td>66984</td><td>~$2,500</td><td>$6,000&ndash;$15,000</td><td>$3,000&ndash;$7,000</td></tr>
        <tr><td>Colonoscopy with biopsy</td><td>45380</td><td>~$1,200</td><td>$4,000&ndash;$12,000</td><td>$2,000&ndash;$5,000</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Wondering how your surgery charge compares to what Medicare pays?</strong> <a href="/calculator">Use BillKarma&rsquo;s cost calculator</a> &mdash; enter the CPT code from your bill and instantly see the Medicare rate so you know whether you&rsquo;re being charged a fair price.
</div>

<p>The Medicare rate includes both the physician fee and the facility fee. It represents what the federal government has determined the procedure is worth. When a hospital charges $45,000 for a knee arthroscopy that Medicare values at $3,800, that&rsquo;s a <strong>12x markup</strong>.</p>

<p>Look up the CPT code from your surgery bill to see what Medicare pays:</p>

{_embed(mode="cost", title="Look up your surgery cost", subtitle="Enter the CPT code from your surgery bill to see what Medicare pays.")}

<p>You can also <a href="/hospitals/">compare facility pricing</a> across hospitals in your area using our hospital directory.</p>

<h2 id="hospital-vs-asc">3. Hospital vs. ambulatory surgery center</h2>

<p>An ambulatory surgery center (ASC) is a facility built specifically for outpatient procedures. You go in, have the surgery, and go home the same day&mdash;no overnight stay. ASCs cost <strong>40&ndash;60% less</strong> than hospitals for the same procedure performed by the same surgeon.</p>

<p><strong>Why the price difference?</strong></p>

<ul>
    <li><strong>Lower overhead.</strong> ASCs don&rsquo;t maintain emergency departments, ICUs, or 24/7 staffing for every specialty. Their costs are lower, so their prices are lower.</li>
    <li><strong>No cross-subsidization.</strong> Hospitals use revenue from insured surgical patients to offset losses from uncompensated ER care and underpaid Medicaid patients. ASCs don&rsquo;t carry this burden.</li>
    <li><strong>More efficient scheduling.</strong> ASCs focus exclusively on surgery. There&rsquo;s no competition for OR time with emergency cases, and turnaround between procedures is faster.</li>
</ul>

<p><strong>When a hospital is the right choice:</strong></p>

<ul>
    <li>Complex procedures requiring overnight observation or ICU availability</li>
    <li>Patients with serious underlying health conditions (uncontrolled diabetes, heart disease, severe obesity)</li>
    <li>Procedures with a high risk of complications that may require immediate hospital-level intervention</li>
</ul>

<div class="key-takeaway">
    <strong>Always ask your surgeon: &ldquo;Can this be done at an ambulatory surgery center?&rdquo;</strong> Many surgeons operate at both hospitals and ASCs. If the procedure can safely be performed at an ASC, switching locations could save you $5,000&ndash;$25,000 with no difference in the quality of care.
</div>

<h2 id="real-surgery-bill">4. A real surgery bill, annotated</h2>

<p>Here&rsquo;s what an actual outpatient knee arthroscopy bill looks like at a hospital. This is a real bill structure with typical charges. We&rsquo;ve flagged the areas where costs are inflated.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Summit Medical Center &mdash; Date of Service: 01/10/2026 &mdash; Outpatient Knee Arthroscopy</div>
    <div class="line-item flagged">
        <span>29881 &mdash; Arthroscopy, knee, surgical; meniscectomy (facility fee) &nbsp; &#9888; <em>Facility fee is 3.5x Medicare&rsquo;s facility rate</em></span>
        <span>$12,800.00</span>
    </div>
    <div class="line-item">
        <span>29881 &mdash; Arthroscopy, knee, surgical; meniscectomy (surgeon fee)</span>
        <span>$3,200.00</span>
    </div>
    <div class="line-item flagged">
        <span>01382 &mdash; Anesthesia for knee arthroscopy (6 time units &times; $185/unit) &nbsp; &#9888; <em>6 units = 90 min of anesthesia for a 45-min procedure&mdash;check operative report</em></span>
        <span>$2,960.00</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete Blood Count (pre-op)</span>
        <span>$187.00</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive Metabolic Panel (pre-op)</span>
        <span>$246.00</span>
    </div>
    <div class="line-item">
        <span>73721 &mdash; MRI, knee (pre-operative imaging)</span>
        <span>$1,850.00</span>
    </div>
    <div class="line-item flagged">
        <span>99070 &mdash; Surgical supplies and materials &nbsp; &#9888; <em>Vague supply code with no itemization&mdash;request a detailed breakdown</em></span>
        <span>$780.00</span>
    </div>
    <div class="line-item">
        <span>J2704 &mdash; Propofol injection (anesthesia drug)</span>
        <span>$175.00</span>
    </div>
    <div class="line-item">
        <span>J3490 &mdash; Ketorolac 30mg IV (post-op pain medication)</span>
        <span>$205.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$22,403.00</span>
    </div>
</div>

<p>Let&rsquo;s break down the problems on this bill:</p>

<ul>
    <li><strong>Facility fee of $12,800 (57% of total bill).</strong> Medicare&rsquo;s facility rate for outpatient knee arthroscopy is approximately $3,600. This hospital is charging 3.5x the Medicare facility rate. At an ambulatory surgery center, this facility fee would typically be $3,500&ndash;$5,500.</li>
    <li><strong>Anesthesia billed at 90 minutes ($2,960).</strong> A straightforward knee arthroscopy typically takes 30&ndash;45 minutes of surgical time. Anesthesia time includes induction and recovery, but 90 minutes (6 time units) is high for this procedure. The operative report will show actual anesthesia start and stop times&mdash;always verify.</li>
    <li><strong>Surgical supplies at $780 with no itemization.</strong> The vague code 99070 (&ldquo;supplies and materials&rdquo;) is a red flag. You have the right to request an itemized breakdown of every supply charged. Without itemization, there&rsquo;s no way to verify you&rsquo;re not being overbilled.</li>
</ul>

<p><strong>The same surgery at an ASC would cost approximately $8,000&ndash;$10,000</strong>&mdash;primarily because the facility fee drops from $12,800 to $3,500&ndash;$5,500. That&rsquo;s a potential savings of $12,000&ndash;$14,000 for the exact same procedure.</p>

<p><a href="/scan">Upload your surgery bill to BillKarma</a> for a free audit that compares every line item to Medicare rates and flags overcharges automatically.</p>

<h2 id="anesthesia-billing">5. Understanding anesthesia billing</h2>

<p>Anesthesia has its own billing system, and it&rsquo;s one of the least understood parts of a surgery bill. Here&rsquo;s how it works.</p>

<p><strong>The formula:</strong> Total anesthesia charge = (base units + time units) &times; conversion factor (dollar amount per unit)</p>

<ul>
    <li><strong>Base units</strong> are set by the American Society of Anesthesiologists (ASA) based on procedure complexity. A knee arthroscopy has 3 base units. Open heart surgery has 15&ndash;20 base units.</li>
    <li><strong>Time units</strong> are measured in 15-minute blocks. Each 15 minutes of anesthesia adds one time unit. So 60 minutes of anesthesia = 4 time units.</li>
    <li><strong>Conversion factor</strong> is the dollar amount per unit. Medicare pays about $22&ndash;$24 per unit. Commercial insurance typically pays $80&ndash;$130 per unit. Hospitals charge $120&ndash;$200+ per unit to uninsured patients.</li>
</ul>

<p><strong>Common anesthesia billing error:</strong> billing for more time units than the actual anesthesia duration. Anesthesia time starts when the anesthesiologist begins preparing the patient and ends when the patient is transferred to recovery. This is documented in the operative report.</p>

<div class="case-study">
    <h3>Case study: Overbilled anesthesia time</h3>
    <p>A patient had outpatient knee arthroscopy and was billed for <strong>90 minutes of anesthesia</strong> (6 time units at $185 per unit = $1,110 in time charges). The surgical procedure lasted 45 minutes. The patient requested the operative report, which showed anesthesia start time of 10:15 AM and end time of 11:05 AM&mdash;<strong>50 minutes of actual anesthesia time</strong>, or 4 time units (rounding up the partial unit).</p>
    <p><strong>Billed:</strong> 6 time units &times; $185 = $1,110 in time charges</p>
    <p><strong>Correct:</strong> 4 time units &times; $185 = $740 in time charges</p>
    <p><strong>Overcharge: $370.</strong> Combined with the base unit charges, the patient was overbilled by approximately <strong>$450</strong> total on anesthesia alone.</p>
</div>

<p><strong>How to verify your anesthesia charges:</strong></p>

<ol>
    <li>Request a copy of the operative report from the hospital medical records department.</li>
    <li>Find the anesthesia start time and end time.</li>
    <li>Calculate the actual time in minutes and divide by 15 to get time units (round up partial units).</li>
    <li>Compare to the time units on your anesthesia bill. If the billed time units exceed the actual time, you have grounds for a dispute.</li>
</ol>

<h2 id="lower-your-cost">6. 5 ways to lower your surgery cost</h2>

<h3>a) Ask about the ambulatory surgery center option</h3>

<p>This is the single biggest lever for savings. ASCs charge 40&ndash;60% less than hospitals for the same procedure. Ask your surgeon: &ldquo;Can this procedure be done at an ASC?&rdquo; Many surgeons have privileges at both hospitals and ASCs. Switching the location&mdash;same surgeon, same procedure&mdash;can save <strong>$5,000&ndash;$25,000</strong>.</p>

<h3>b) Get a good faith estimate</h3>

<p>Under the <a href="/guides/no-surprises-act-explained">No Surprises Act</a>, if you&rsquo;re uninsured or self-pay, healthcare providers must give you a written good faith estimate of expected charges before any scheduled service. If the final bill exceeds the estimate by $400 or more, you can dispute the difference through the federal patient-provider dispute resolution process.</p>

<h3>c) Compare facility prices using price transparency data</h3>

<p>Hospitals are required to post their prices online, including negotiated rates with insurance companies. Check our <a href="/hospitals/">hospital pricing directory</a> to compare surgery costs across facilities in your area. Price differences of 3&ndash;5x for the same procedure at hospitals in the same city are common.</p>

<h3>d) Negotiate before the surgery</h3>

<p>It is always easier to <a href="/guides/how-to-negotiate-medical-bills">negotiate before the procedure</a> than after. Once you have a good faith estimate, compare each component to Medicare rates using our <a href="/calculator">cost calculator</a>. Then call the billing department and ask for a self-pay discount or negotiate based on Medicare rates. Get the agreed price in writing before your surgery date.</p>

<h3>e) Check if you qualify for financial assistance</h3>

<p>All nonprofit hospitals (roughly 60% of US hospitals) are required to have <a href="/guides/hospital-financial-assistance-charity-care">financial assistance programs</a>. If your income is below 200&ndash;400% of the federal poverty level, you may qualify for free or significantly reduced-cost care&mdash;even for elective surgery. Apply before the procedure if possible. Check your hospital&rsquo;s financial assistance policy in our <a href="/hospitals/">hospital directory</a>.</p>

{_embed(mode="cost", title="Compare your surgery cost to Medicare", subtitle="Enter the CPT code from your estimate or bill to see the Medicare rate.", height="380")}

<div class="key-takeaway">
    <strong>Already received your surgery bill?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we scan every line item against Medicare rates and identify specific charges you can dispute to reduce what you owe.
</div>

<h2 id="case-studies">7. Real savings: 3 case studies</h2>

<div class="key-takeaway">
    <strong>Think your surgery bill might have errors?</strong> <a href="/scan">Scan your itemized bill with BillKarma</a> &mdash; patients who find billing errors save an average of $1,200 per disputed surgery claim.
</div>

<div class="case-study">
    <h3>Case study 1: Gallbladder removal &mdash; hospital vs. ASC</h3>
    <p><strong>Situation:</strong> Patient needed a laparoscopic gallbladder removal (CPT 47562). The surgeon&rsquo;s hospital quoted <strong>$38,000</strong> for the procedure.</p>
    <p><strong>Action:</strong> The patient asked the surgeon if the procedure could be done at an ambulatory surgery center. The surgeon had privileges at an ASC 10 miles away.</p>
    <p><strong>Result:</strong> Same surgeon, same procedure, at an ASC: <strong>$12,500</strong>. The surgery went smoothly, and the patient went home the same day&mdash;exactly as they would have from the hospital.</p>
    <p><strong>Savings: $25,500.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: Hernia repair &mdash; billing errors found</h3>
    <p><strong>Situation:</strong> Patient received a bill for <strong>$28,000</strong> for an inguinal hernia repair (CPT 49505) at a hospital outpatient department.</p>
    <p><strong>Action:</strong> The patient <a href="/scan">uploaded the bill to BillKarma</a>. The analysis found two issues: the facility fee was <strong>8x the Medicare facility rate</strong>, and the anesthesia was billed for 30 minutes more than the operative report supported.</p>
    <p><strong>Result:</strong> The patient <a href="/guides/how-to-dispute-a-medical-bill">filed a dispute</a> citing the anesthesia time discrepancy and requested a reduction in the facility fee based on Medicare benchmarks. After two rounds of communication, the bill was reduced to <strong>$18,200</strong>.</p>
    <p><strong>Savings: $9,800.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: Colonoscopy &mdash; uninsured patient negotiation</h3>
    <p><strong>Situation:</strong> An uninsured patient was quoted <strong>$8,400</strong> for a colonoscopy with biopsy (CPT 45380) at a hospital outpatient department.</p>
    <p><strong>Action:</strong> The patient asked for the self-pay discount and received 40% off, bringing the price to $5,040. They then researched the Medicare rate ($1,200) and called back to negotiate further, using the Medicare rate as an anchor point.</p>
    <p><strong>Result:</strong> The hospital agreed to <strong>$3,200</strong>&mdash;approximately 2.7x the Medicare rate, which is within the range of what commercial insurance companies typically pay.</p>
    <p><strong>Savings: $5,200.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Why is surgery so expensive?</h3>
        <p>Surgery bills include charges from multiple sources: the surgeon&rsquo;s fee, a facility fee (for using the operating room), anesthesia billed in 15-minute time units, labs, imaging, and supplies. The facility fee alone is typically 50&ndash;60% of the total. On top of that, hospitals apply chargemaster markups that can be 3&ndash;10x what Medicare pays. The combination of multiple billing sources and high markups is why surgery is the most expensive medical service most people encounter.</p>
    </div>

    <div class="faq-item">
        <h3>Can I negotiate surgery costs before the procedure?</h3>
        <p>Yes, and it&rsquo;s much easier to negotiate before surgery than after. Ask for a good faith estimate (required under the <a href="/guides/no-surprises-act-explained">No Surprises Act</a> for self-pay patients), compare it to Medicare rates using our <a href="/calculator">calculator</a>, and ask for a self-pay discount or negotiate based on the Medicare benchmark. Many hospitals will offer 30&ndash;60% off the sticker price.</p>
    </div>

    <div class="faq-item">
        <h3>What is a facility fee?</h3>
        <p>A facility fee is what the hospital or surgery center charges for using the operating room, recovery area, nursing staff, and equipment&mdash;separate from the surgeon&rsquo;s fee and anesthesia. It&rsquo;s typically the largest single item on a surgery bill (50&ndash;60% of the total). Hospital facility fees are generally 2&ndash;4x higher than ASC facility fees for the same procedure.</p>
    </div>

    <div class="faq-item">
        <h3>Why does anesthesia cost so much?</h3>
        <p>Anesthesia is billed using base units (set by procedure complexity) plus time units (one unit per 15 minutes). Each unit costs $120&ndash;$200 at hospital rates. A 60-minute procedure might generate 7&ndash;8 total units at $150 each, or $1,050&ndash;$1,200. Common billing errors include rounding up time units and billing for more time than the operative report shows. Always verify the billed time against your operative report.</p>
    </div>

    <div class="faq-item">
        <h3>What if I can&rsquo;t afford my surgery bill?</h3>
        <p>Start by asking for the self-pay discount (30&ndash;60% off). Next, apply for <a href="/guides/hospital-financial-assistance-charity-care">financial assistance</a> at nonprofit hospitals. You can also negotiate a lump-sum settlement at 40&ndash;60% of the bill, or ask for a zero-interest payment plan. Finally, <a href="/scan">upload your bill to BillKarma</a> to identify billing errors and overcharges that can further reduce what you owe.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between a hospital and an ambulatory surgery center?</h3>
        <p>An ambulatory surgery center (ASC) is a facility designed specifically for outpatient surgeries. ASCs cost 40&ndash;60% less than hospitals for the same procedure because they have lower overhead and don&rsquo;t subsidize emergency departments. Many common surgeries (knee arthroscopy, gallbladder removal, hernia repair, cataract surgery) can safely be performed at an ASC. Ask your surgeon if this is an option for your procedure.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/hospital-outpatient" target="_blank" rel="noopener">CMS Hospital Outpatient Prospective Payment System (OPPS) &mdash; 2026 Final Rule</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/ambulatory-surgical-center-asc" target="_blank" rel="noopener">CMS Ambulatory Surgical Center (ASC) Payment System &mdash; 2026 Final Rule</a></li>
    <li><a href="https://hcup-us.ahrq.gov/" target="_blank" rel="noopener">AHRQ Healthcare Cost and Utilization Project (HCUP) &mdash; Surgery Cost Statistics</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">Health Affairs: Hospital Charge-to-Cost Ratios (2022)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.asahq.org/standards-and-practice-parameters/statement-on-anesthesia-care-team" target="_blank" rel="noopener">American Society of Anesthesiologists: Anesthesia Billing and Base Unit Values</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">No Surprises Act &mdash; CMS</a></li>
</ul>
""",
})
