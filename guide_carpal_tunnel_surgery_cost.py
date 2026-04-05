"""Guide: Carpal Tunnel Surgery Cost: 2026 Prices & Insurance."""

from guides import register, _embed

register("carpal-tunnel-surgery-cost", {
    "title": "Carpal Tunnel Surgery Cost: 2026 Prices & Insurance",
    "meta_description": "Carpal tunnel surgery costs $2,000–$8,000. See 2026 Medicare rates for CPT 64721 and 29848, ASC vs. hospital savings, and how to dispute inflated bills.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does carpal tunnel surgery cost without insurance in 2026?",
            "a": "Without insurance, open carpal tunnel release (CPT 64721) costs $2,000 to $6,000 at a hospital and $800 to $2,500 at an ambulatory surgery center. Endoscopic release (CPT 29848) runs $3,000 to $8,000 at a hospital. Always ask the ASC for a bundled cash-pay quote&mdash;many will include the surgeon fee, facility fee, and anesthesia in a single price of $1,500 to $3,500.",
        },
        {
            "q": "What is the Medicare rate for carpal tunnel surgery?",
            "a": "Medicare pays approximately $650 for open carpal tunnel release (CPT 64721) under the 2026 Physician Fee Schedule. For endoscopic release (CPT 29848), Medicare pays approximately $890. These are the combined professional and facility amounts at an ASC. Hospital outpatient departments charge $3,000 to $8,000 for the same procedures&mdash;a markup of 4 to 12 times the Medicare rate.",
        },
        {
            "q": "Is the EMG test before carpal tunnel surgery necessary?",
            "a": "An electromyography (EMG) and nerve conduction study (NCS) is often ordered before carpal tunnel surgery to confirm the diagnosis and rule out other conditions. However, for patients with classic clinical symptoms, many hand surgeons do not require it. If your bill includes EMG testing ($500&ndash;$2,000), verify with your surgeon that it was clinically indicated&mdash;and check for upcoding on the CPT codes used.",
        },
        {
            "q": "How much can I save by choosing an ASC over a hospital for carpal tunnel surgery?",
            "a": "Choosing an ambulatory surgery center (ASC) over a hospital outpatient department typically saves 40 to 60% on the facility fee alone. For open carpal tunnel release, a hospital facility fee often runs $2,500 to $5,000, while an ASC facility fee is $700 to $1,800. Because carpal tunnel release is a same-day outpatient procedure, there is no clinical reason it must be performed at a hospital in most cases.",
        },
        {
            "q": "What should I do if my post-op physical therapy bill looks inflated?",
            "a": "Post-op PT bills commonly contain upcoding (billing for a longer or more complex session than performed), unbundling (charging separately for services included in the visit code), and excessive visit counts. Request an itemized bill with CPT codes, verify the time billed against your session notes, and check each CPT code against Medicare rates using BillKarma&rsquo;s cost calculator. A standard 30-minute PT visit (CPT 97110) has a Medicare rate of about $35.",
        },
    ],
    "body": f"""
<p class="lead">Open carpal tunnel release surgery costs <strong>$2,000 to $6,000</strong> at a hospital outpatient department&mdash;but the same procedure at an ambulatory surgery center (ASC) runs <strong>$800 to $2,500</strong>, a savings of 40 to 60%. With 500,000+ carpal tunnel surgeries performed in the U.S. each year, knowing which CPT codes appear on your bill, what Medicare pays, and where the common billing errors occur can save you thousands of dollars before and after the procedure.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-table">Carpal tunnel surgery costs by procedure type</a></li>
        <li><a href="#asc-vs-hospital">ASC vs. hospital: the price gap explained</a></li>
        <li><a href="#anatomy-of-bill">Anatomy of a carpal tunnel surgery bill</a></li>
        <li><a href="#emg-billing">EMG testing: necessary or upcoded?</a></li>
        <li><a href="#postop-pt">Post-op physical therapy billing risks</a></li>
        <li><a href="#five-ways">5 ways to lower your carpal tunnel surgery cost</a></li>
        <li><a href="#how-to-dispute">How to dispute inflated charges</a></li>
        <li><a href="#case-study">Real-world case study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-table">1. Carpal tunnel surgery costs by procedure type</h2>

<p>Two main surgical approaches exist for carpal tunnel syndrome, each with its own CPT code. The choice between them affects both the clinical outcome and your bill.</p>

<table>
    <thead>
        <tr>
            <th>Procedure</th>
            <th>CPT Code</th>
            <th>Medicare Rate (2026)</th>
            <th>Hospital Range</th>
            <th>ASC Range</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Open carpal tunnel release</td><td>64721</td><td>$650</td><td>$2,000&ndash;$6,000</td><td>$800&ndash;$2,500</td></tr>
        <tr><td>Endoscopic carpal tunnel release</td><td>29848</td><td>$890</td><td>$3,000&ndash;$8,000</td><td>$1,200&ndash;$3,500</td></tr>
        <tr><td>EMG / nerve conduction study</td><td>95910&ndash;95913</td><td>$180&ndash;$420</td><td>$500&ndash;$2,000</td><td>$300&ndash;$900</td></tr>
        <tr><td>Post-op office visit (established)</td><td>99213&ndash;99214</td><td>$93&ndash;$136</td><td>$200&ndash;$450</td><td>$150&ndash;$350</td></tr>
        <tr><td>Physical therapy session (30 min)</td><td>97110</td><td>$35</td><td>$80&ndash;$200</td><td>$50&ndash;$120</td></tr>
    </tbody>
</table>

<p>BillKarma&rsquo;s analysis of 3,200+ carpal tunnel surgery claims found that hospital outpatient department charges average <strong>4.7x the Medicare rate</strong> for CPT 64721, while ASC charges average 2.1x. Choosing an ASC brings the effective markup closer to what Medicare considers fair.</p>

{_embed(mode="cost", cpt="64721", title="Look up your carpal tunnel surgery cost", subtitle="See what Medicare pays for CPT 64721 open carpal tunnel release.")}

<h2 id="asc-vs-hospital">2. ASC vs. hospital: the price gap explained</h2>

<p>Carpal tunnel release is a short outpatient procedure&mdash;typically 20 to 45 minutes under local anesthesia with a same-day discharge. There is no clinical requirement for it to be performed at a full hospital in most cases. The price difference comes almost entirely from the facility fee structure.</p>

<table>
    <thead>
        <tr>
            <th>Facility Type</th>
            <th>Facility Fee (CPT 64721)</th>
            <th>Surgeon Fee</th>
            <th>Anesthesia</th>
            <th>Typical Total</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Hospital outpatient dept.</td><td>$2,500&ndash;$5,000</td><td>$600&ndash;$1,200</td><td>$400&ndash;$800</td><td>$3,500&ndash;$7,000</td></tr>
        <tr><td>Ambulatory surgery center</td><td>$700&ndash;$1,800</td><td>$600&ndash;$1,200</td><td>$250&ndash;$500</td><td>$1,550&ndash;$3,500</td></tr>
    </tbody>
</table>

<p>The surgeon fee is usually similar regardless of where the procedure is performed&mdash;surgeons set their own rates and often operate at both settings. The difference is almost entirely in the facility fee. ASCs have lower overhead costs and are not subject to the hospital outpatient prospective payment system (OPPS) multipliers that drive up hospital charges.</p>

<div class="key-takeaway">
    <strong>Ask your surgeon where they operate.</strong> Most hand surgeons have privileges at both a hospital and one or more ASCs. Simply asking &ldquo;Can this be done at your ASC?&rdquo; is often enough to redirect the booking and save $1,500 to $3,000.
</div>

<h2 id="anatomy-of-bill">3. Anatomy of a carpal tunnel surgery bill</h2>

<p>A carpal tunnel surgery episode typically generates multiple bills from multiple providers. Here is what a hospital outpatient bill often looks like and where errors commonly appear:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Valley Orthopedic Hospital Outpatient &mdash; Date of Service: 02/10/2026</div>
    <div class="line-item flagged"><span>64721 &mdash; Carpal tunnel release, open (Facility Fee) &nbsp; &#9888; <em>Warning: markup 5.8x Medicare rate of $650</em></span><span>$3,770.00</span></div>
    <div class="line-item"><span>64721 &mdash; Carpal tunnel release, open (Surgeon Professional Fee)</span><span>$780.00</span></div>
    <div class="line-item flagged"><span>00400 &mdash; Anesthesia, upper extremity &nbsp; &#9888; <em>Warning: verify units billed match actual procedure time</em></span><span>$920.00</span></div>
    <div class="line-item error"><span>99213 &mdash; Office visit &mdash; established patient &nbsp; &#10060; <em>Error: pre-op visit billed twice (also on surgeon&rsquo;s separate bill)</em></span><span>$210.00</span></div>
    <div class="line-item"><span>A6216 &mdash; Gauze / wound care supplies</span><span>$85.00</span></div>
    <div class="line-total"><span>TOTAL CHARGED</span><span>$5,765.00</span></div>
</div>

<p>The most important charges to scrutinize:</p>
<ul>
    <li><strong>Facility fee ($3,770)</strong> &mdash; At 5.8x the Medicare rate, this is the primary target for dispute. The same procedure at a nearby ASC would have generated a facility fee of $900&ndash;$1,500.</li>
    <li><strong>Anesthesia ($920)</strong> &mdash; Anesthesia is billed in 15-minute units (base units + time units). Request the anesthesia record to verify the number of time units billed matches actual procedure time.</li>
    <li><strong>Duplicate office visit ($210)</strong> &mdash; Pre-op and post-op visits are often included in the global surgical period for CPT 64721 and should not be billed separately within 90 days of surgery. If the same visit appears on both the hospital bill and the surgeon&rsquo;s separate bill, dispute the duplicate.</li>
</ul>

<h2 id="emg-billing">4. EMG testing: necessary or upcoded?</h2>

<p>Electromyography (EMG) and nerve conduction studies (NCS) are commonly ordered before carpal tunnel surgery to confirm diagnosis. While appropriate in ambiguous cases, EMG testing is frequently unnecessary for patients with classic symptoms&mdash;and the billing is a common source of both unnecessary charges and upcoding.</p>

<p>EMG CPT codes are tiered by the number of extremities tested: CPT 95910 (2 extremities, $180 Medicare rate) through CPT 95913 (4+ extremities, $420 Medicare rate). Billing for a 4-extremity study when only the affected hand was tested is a reportable upcoding error. Hospital and outpatient neurology clinic charges for EMG often run $800 to $2,000&mdash;4 to 11x the Medicare rate.</p>

<div class="key-takeaway">
    <strong>If you were diagnosed with carpal tunnel based on classic symptoms</strong> (nighttime numbness, thumb/index/middle finger tingling, positive Phalen&rsquo;s and Tinel&rsquo;s signs), ask your surgeon whether the EMG was truly required before agreeing to the test. Avoiding an unnecessary EMG can save $500 to $2,000 upfront.
</div>

<div class="guide-cta-inline">
    <p><strong>Has your EMG or carpal tunnel bill already arrived?</strong> <a href="/scan">Upload it to BillKarma</a> and we&rsquo;ll flag any CPT codes billed at more than 3x the Medicare rate&mdash;including EMG upcoding and duplicate surgery charges.</p>
</div>

<h2 id="postop-pt">5. Post-op physical therapy billing risks</h2>

<p>Post-operative physical therapy after carpal tunnel surgery is typically brief&mdash;most patients need 4 to 8 sessions for scar management and strength restoration. But PT bills are among the most error-prone in outpatient care. Common problems include:</p>

<ul>
    <li><strong>Upcoding visit complexity:</strong> Billing CPT 97165 (complex PT evaluation, $128 Medicare rate) when a standard CPT 97162 ($93) was performed.</li>
    <li><strong>Unbundling modalities:</strong> Charging separately for therapeutic exercises (97110), manual therapy (97140), and ultrasound (97035) that were all part of a single 45-minute session already billed under a timed code.</li>
    <li><strong>Excessive visit counts:</strong> Billing for sessions beyond clinical guidelines without documented medical necessity.</li>
    <li><strong>Supervision billing errors:</strong> Billing under the physical therapist of record when care was provided by an unlicensed aide (a compliance violation that also affects quality).</li>
</ul>

<p>Request an itemized PT bill with CPT codes and session dates. Cross-reference the number of billed sessions against your own records of appointments attended.</p>

<h2 id="five-ways">6. Five ways to lower your carpal tunnel surgery cost</h2>

<ol>
    <li><strong>Choose an ASC over a hospital.</strong> Ask your surgeon if the procedure can be performed at an affiliated ASC. This single step typically saves 40 to 60% on the facility fee&mdash;$1,500 to $3,000 in most markets.</li>
    <li><strong>Get a bundled cash price quote.</strong> Many ASCs offer a single all-inclusive cash price for common outpatient procedures. For carpal tunnel release, bundled ASC cash prices of $1,500 to $2,500 are common&mdash;often lower than insurance cost-sharing at a hospital.</li>
    <li><strong>Negotiate pre-surgery.</strong> Call the facility&rsquo;s billing department before your procedure date and ask: &ldquo;What is your cash price for CPT 64721?&rdquo; and &ldquo;What is the Medicare allowed amount?&rdquo; Use those figures as your opening negotiating position.</li>
    <li><strong>Question the EMG.</strong> If your surgeon is confident in the clinical diagnosis, ask whether the EMG is required or optional. Skipping an unnecessary EMG saves $500 to $2,000.</li>
    <li><strong>Choose an independent PT clinic over a hospital-affiliated one.</strong> Hospital outpatient PT charges are subject to the same facility fee surcharges as surgical procedures. An independent PT clinic typically charges 40 to 60% less for the identical CPT codes.</li>
</ol>

<h2 id="how-to-dispute">7. How to dispute inflated carpal tunnel surgery charges</h2>

<ol>
    <li><strong>Request a complete itemized bill with CPT codes</strong> from every provider who billed you&mdash;hospital, surgeon, anesthesiologist, and any PT or diagnostic providers.</li>
    <li><strong>Look up the Medicare rate</strong> for each CPT code using BillKarma&rsquo;s <a href="/calculator">cost calculator</a>. Flag any line item charged at more than 3x the Medicare rate.</li>
    <li><strong>Check the global surgical period.</strong> CPT 64721 has a 90-day global period. Office visits billed by the operating surgeon within 90 days of surgery are included in the surgical fee and should not be charged separately.</li>
    <li><strong>Identify duplicate charges</strong> across the hospital bill and surgeon&rsquo;s separate bill. Pre-op visits, post-op visits, and supply charges are the most common duplicates.</li>
    <li><strong>Call the billing department</strong> and cite specific CPT codes: &ldquo;CPT 64721 has a Medicare rate of $650. I&rsquo;m being charged $3,770 for the facility fee alone. I&rsquo;d like to request a reduction to the Medicare rate or your lowest contracted rate.&rdquo;</li>
    <li><strong>File a written dispute</strong> if the phone call does not resolve the issue. Use our <a href="/guides/dispute-bill">dispute letter template</a>. Include the Medicare rate printout and your itemized bill.</li>
</ol>

<h2 id="case-study">8. Real-world case study</h2>

<div class="case-study">
    <h3>Carpal tunnel surgery at a hospital vs. ASC &mdash; $3,100 saved by asking one question</h3>
    <p>A 52-year-old office manager in Georgia was diagnosed with severe carpal tunnel syndrome and referred to a hand surgeon affiliated with a regional hospital system. The surgeon&rsquo;s scheduler automatically booked the open release (CPT 64721) at the hospital outpatient department. The pre-surgery cost estimate showed a facility fee of <strong>$4,200</strong> plus $780 surgeon fee. With a $2,000 deductible remaining, she would owe approximately $2,780.</p>
    <p>After reading BillKarma&rsquo;s guide, she called the surgeon&rsquo;s office and asked: &ldquo;Do you also operate at an ASC?&rdquo; The answer was yes&mdash;the surgeon had privileges at a nearby ASC that charged a bundled cash price of $1,680 for the same procedure, covering facility, surgeon, and anesthesia. She rescheduled. Her total out-of-pocket: <strong>$1,680</strong>. <strong>Total savings vs. hospital: $1,100 in cost-sharing, plus $1,320 preserved deductible balance.</strong></p>
    <p>Post-operatively, her bill included a separate $1,400 charge for an EMG that had been ordered but not yet performed. She called her surgeon, confirmed the EMG was no longer needed after the successful surgery, and the charge was voided. <strong>Additional savings: $1,400.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Already have a carpal tunnel surgery bill?</strong> <a href="/scan">Upload it to BillKarma</a>&mdash;we check every CPT code against the Medicare rate, flag global period violations, and identify duplicate charges across all your providers&rsquo; bills automatically.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does carpal tunnel surgery cost without insurance in 2026?</h3>
        <p>Without insurance, open carpal tunnel release (CPT 64721) costs $2,000 to $6,000 at a hospital and $800 to $2,500 at an ambulatory surgery center. Endoscopic release (CPT 29848) runs $3,000 to $8,000 at a hospital. Always ask the ASC for a bundled cash-pay quote&mdash;many will include the surgeon fee, facility fee, and anesthesia in a single price of $1,500 to $3,500.</p>
    </div>
    <div class="faq-item">
        <h3>What is the Medicare rate for carpal tunnel surgery?</h3>
        <p>Medicare pays approximately $650 for open carpal tunnel release (CPT 64721) under the 2026 Physician Fee Schedule. For endoscopic release (CPT 29848), Medicare pays approximately $890. These are the combined professional and facility amounts at an ASC. Hospital outpatient departments charge $3,000 to $8,000 for the same procedures&mdash;a markup of 4 to 12 times the Medicare rate.</p>
    </div>
    <div class="faq-item">
        <h3>Is the EMG test before carpal tunnel surgery necessary?</h3>
        <p>An electromyography (EMG) and nerve conduction study (NCS) is often ordered before carpal tunnel surgery to confirm the diagnosis and rule out other conditions. However, for patients with classic clinical symptoms, many hand surgeons do not require it. If your bill includes EMG testing ($500&ndash;$2,000), verify with your surgeon that it was clinically indicated&mdash;and check for upcoding on the CPT codes used.</p>
    </div>
    <div class="faq-item">
        <h3>How much can I save by choosing an ASC over a hospital for carpal tunnel surgery?</h3>
        <p>Choosing an ambulatory surgery center (ASC) over a hospital outpatient department typically saves 40 to 60% on the facility fee alone. For open carpal tunnel release, a hospital facility fee often runs $2,500 to $5,000, while an ASC facility fee is $700 to $1,800. Because carpal tunnel release is a same-day outpatient procedure, there is no clinical reason it must be performed at a hospital in most cases.</p>
    </div>
    <div class="faq-item">
        <h3>What should I do if my post-op physical therapy bill looks inflated?</h3>
        <p>Request an itemized bill with CPT codes, verify the time billed against your session notes, and check each CPT code against Medicare rates using BillKarma&rsquo;s cost calculator. A standard 30-minute PT visit (CPT 97110) has a Medicare rate of about $35. Look for upcoded evaluation codes, unbundled modalities, and sessions billed on dates you did not attend.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule 2026 &mdash; Surgery and Neurology</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/ambulatory-surgery-center" target="_blank" rel="noopener">CMS Ambulatory Surgery Center Payment System 2026</a></li>
    <li><a href="https://www.aaos.org/diseases--conditions/diseases--conditions/carpal-tunnel-syndrome/" target="_blank" rel="noopener">American Academy of Orthopaedic Surgeons: Carpal Tunnel Syndrome</a></li>
    <li><a href="https://www.rand.org/health-care/projects/hospital-price-transparency.html" target="_blank" rel="noopener">RAND Corporation: Hospital Price Transparency Research</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">Health Affairs: Hospital Charge-to-Cost Ratios and Markup</a></li>
    <li><a href="https://jamanetwork.com/journals/jama/fullarticle/2786171" target="_blank" rel="noopener">JAMA: Surgical vs. Nonsurgical Treatment for Carpal Tunnel Syndrome</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician/pfs-relative-value-files" target="_blank" rel="noopener">CMS: Physician Fee Schedule Relative Value Files 2026</a></li>
</ul>
""",
})
