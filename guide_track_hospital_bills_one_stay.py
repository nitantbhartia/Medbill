"""Guide: Track Every Hospital Bill From One Stay (Free Template)."""

from guides import register

register("track-hospital-bills-one-stay", {
    "title": "Track Every Hospital Bill From One Stay (Free Template)",
    "meta_description": "One hospital stay can bring bills from the hospital, doctors, labs and ambulance. Use this free tracker to match each bill to its EOB and keep deadlines.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Taking Action",
    "faqs": [
        {
            "q": "Why did I get several bills for one hospital visit?",
            "a": "The hospital bills for the facility, and doctors, labs, imaging groups and ambulance services often bill separately. Your insurer can send a separate explanation of benefits (EOB) for each provider, each type of service and each day of treatment, according to CMS.",
        },
        {
            "q": "What should I do if my bill is higher than my EOB?",
            "a": "CMS says the amount you owe on the bill should match the What You Owe amount on your EOB, and you should not pay more than the EOB shows. If the bill is higher, contact the provider who sent it and ask them to correct it. If the EOB itself looks wrong, contact your insurer.",
        },
        {
            "q": "How long does a nonprofit hospital have to wait before sending my bill to collections?",
            "a": "Under IRS rules for tax-exempt hospitals (section 501(r)), the hospital must wait at least 120 days after the first post-discharge billing statement before starting extraordinary collection actions such as selling the debt, reporting it to credit bureaus or using a court process. You have at least 240 days from that first statement to apply for financial assistance.",
        },
        {
            "q": "Can I get my billing records from the hospital?",
            "a": "Yes. Under HIPAA (45 CFR 164.524) you have a right to a copy of your records in the designated record set, which includes billing records a provider keeps about you. The provider must act within 30 days, with one possible 30-day extension if it tells you why in writing. It can charge only a reasonable, cost-based fee for copies.",
        },
        {
            "q": "Should I call my insurer or the provider first?",
            "a": "Call the provider when the bill does not match the EOB, or when a date, service or code looks wrong. Call the insurer when the EOB itself looks wrong: a denied claim, a missing claim, or a provider treated as out of network that should not be. If you still disagree after the insurer answers, you can ask for an internal appeal and then an external review.",
        },
    ],
    "body": f"""
<p class="lead">To track bills from one hospital stay, give every bill its own row, match each one to the explanation of benefits (EOB) from your insurer, and pay only the amount the EOB says you owe. Copy the template below, fill in one row per bill, and check it once a week.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-several-bills">Why one stay creates several bills</a></li>
        <li><a href="#template">The tracker template (with sample rows)</a></li>
        <li><a href="#match-eob">How to match each bill to its EOB</a></li>
        <li><a href="#dates">Dates to write down: 501(r) for nonprofit hospitals</a></li>
        <li><a href="#records">Get your billing records under HIPAA</a></li>
        <li><a href="#who-to-call">Call the insurer or the provider?</a></li>
        <li><a href="#weekly-routine">Your 15-minute weekly routine</a></li>
        <li><a href="#red-flags">Red flags to act on</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="why-several-bills">1. Why one stay creates several bills</h2>

<p>A hospital stay is not one bill. It is a group of bills from the businesses that worked on your care:</p>

<ul>
    <li><strong>The hospital (facility).</strong> Room, nursing, supplies, drugs, the ER or operating room.</li>
    <li><strong>Physician groups.</strong> The ER doctor, surgeon or anesthesiologist may bill on their own.</li>
    <li><strong>Labs.</strong> Blood tests may be billed by the hospital or by an outside lab.</li>
    <li><strong>Imaging.</strong> The hospital may bill for the scan, and a radiology group may bill for reading it.</li>
    <li><strong>Ambulance.</strong> The ambulance company bills separately.</li>
</ul>

<p>Medicare shows this split plainly. For an ER visit, a person with Original Medicare pays a copayment to the hospital for each visit and each hospital service, and separately pays 20% of the Medicare-approved amount for the doctor&rsquo;s services after the Part B deductible. CMS notes you can get a separate EOB for each provider, each type of service and each day of treatment.</p>

<p>Bills also arrive weeks apart. For a deeper look at who sends what, see <a href="/guides/multiple-bills-one-hospital-visit/">why you get multiple bills for one hospital visit</a>.</p>

<h2 id="template">2. The tracker template (with sample rows)</h2>

<p>Select the table, copy it, and paste into cell A1 of Google Sheets, Excel or Numbers. One row per bill. When a provider sends an updated bill, update its row.</p>

<p><strong>Jargon, in plain words:</strong> a <em>CPT code</em> is a five-digit code for a medical service, maintained by the American Medical Association. A <em>revenue code</em> is a number on a hospital bill that tells which department or type of charge a line belongs to. An <em>adjustment</em> is the amount a provider takes off the charges, often because of its contract with your insurer.</p>

<table>
    <thead>
        <tr>
            <th>Date received</th>
            <th>Who billed</th>
            <th>Date of service</th>
            <th>CPT / revenue codes</th>
            <th>Billed</th>
            <th>Insurance paid</th>
            <th>Adjustment</th>
            <th>You owe per EOB</th>
            <th>You owe per bill</th>
            <th>Status</th>
            <th>Next action</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Sample: 10/06/2026</td>
            <td>Sample: Hospital (facility)</td>
            <td>09/03/2026</td>
            <td>Rev 0450 (ER)</td>
            <td>$4,850.00</td>
            <td>$2,120.00</td>
            <td>$2,230.00</td>
            <td>$500.00</td>
            <td>$500.00</td>
            <td>Matches EOB</td>
            <td>Ask about financial assistance before paying</td>
            <td>Itemized bill requested 10/07</td>
        </tr>
        <tr>
            <td>Sample: 10/14/2026</td>
            <td>Sample: ER physician group</td>
            <td>09/03/2026</td>
            <td>CPT 99284</td>
            <td>$1,200.00</td>
            <td>$310.00</td>
            <td>$640.00</td>
            <td>$250.00</td>
            <td>$890.00</td>
            <td>Bill $640 higher than EOB</td>
            <td>Call provider: adjustment not applied</td>
            <td>$1,200 &minus; $310 = $890, so the $640 adjustment is missing</td>
        </tr>
        <tr>
            <td>Sample: 10/20/2026</td>
            <td>Sample: Outside lab</td>
            <td>09/03/2026</td>
            <td>CPT 80053</td>
            <td>$380.00</td>
            <td>$0.00</td>
            <td>$0.00</td>
            <td>$380.00</td>
            <td>$380.00</td>
            <td>Claim denied on EOB</td>
            <td>Call insurer: ask the denial reason</td>
            <td>Remark code on EOB; consider appeal</td>
        </tr>
    </tbody>
</table>

<p>The sample rows are made up. In each row, Billed minus Insurance paid minus Adjustment should equal You owe per EOB. Row 1: $4,850 &minus; $2,120 &minus; $2,230 = $500. Row 2: $1,200 &minus; $310 &minus; $640 = $250. Row 3: $380 &minus; $0 &minus; $0 = $380.</p>

<p>Prefer plain text? Paste this header line into a sheet and use &ldquo;split text to columns&rdquo; on commas:</p>

<pre>Date received,Who billed,Date of service,CPT/revenue codes,Billed,Insurance paid,Adjustment,You owe per EOB,You owe per bill,Status,Next action,Notes</pre>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>The two columns that matter most are &ldquo;You owe per EOB&rdquo; and &ldquo;You owe per bill.&rdquo; When they differ, you have something to question. Want a line-by-line check of the hospital bill itself? <a href="/scan">Check your bill free</a> against Medicare rates.</p>
</div>

<h2 id="match-eob">3. How to match each bill to its EOB</h2>

<p>An EOB is a notice from your health plan, not a bill. It shows what the provider charged, what your plan allowed and paid, and what you owe.</p>

<ol>
    <li><strong>Match the provider name.</strong> The EOB lists who submitted the claim. Physician groups may use names you don&rsquo;t recognize.</li>
    <li><strong>Match the date of service.</strong> CMS suggests making sure you got services on the dates listed.</li>
    <li><strong>Match the billed amount.</strong> The &ldquo;provider charges&rdquo; on the EOB should match the total on the bill for that date.</li>
    <li><strong>Compare &ldquo;What You Owe.&rdquo;</strong> CMS says this amount should be the same as the amount on your bill, and that you should not pay more than the EOB shows.</li>
    <li><strong>Read the remark codes.</strong> These short codes explain denials and reductions. Their meanings are printed at the bottom of the EOB.</li>
    <li><strong>No EOB yet?</strong> Write &ldquo;waiting&rdquo; in the EOB column and hold off on paying. CMS advises keeping your EOBs and paying after you get a bill that matches them.</li>
</ol>

<p>More detail on each EOB field: <a href="/guides/explanation-of-benefits-eob/">how to read an explanation of benefits</a>.</p>

<h2 id="dates">4. Dates to write down: 501(r) for nonprofit hospitals</h2>

<p>If the hospital is a tax-exempt (nonprofit) hospital, federal tax rules in section 501(r) of the Internal Revenue Code set dates that protect you. Write the date of the <strong>first billing statement after you left the hospital</strong> in your Notes column. Every 501(r) date counts from it.</p>

<table>
    <thead>
        <tr>
            <th>Rule</th>
            <th>What it means for you</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>120-day notification period</td>
            <td>The hospital must wait at least 120 days after the first post-discharge statement before starting extraordinary collection actions.</td>
        </tr>
        <tr>
            <td>240-day application period</td>
            <td>You have at least 240 days from the first post-discharge statement to apply for the hospital&rsquo;s financial assistance.</td>
        </tr>
        <tr>
            <td>30-day notice</td>
            <td>Before those collection actions, the hospital must send a written notice with a deadline at least 30 days out, and make a reasonable effort to tell you about financial assistance by phone or in person.</td>
        </tr>
        <tr>
            <td>Applying pauses collections</td>
            <td>If you apply during the application period, the hospital must hold off on starting or continuing those actions while it decides.</td>
        </tr>
    </tbody>
</table>

<p><strong>Extraordinary collection actions</strong> include selling your debt, reporting it to credit bureaus, deferring or denying needed care because of an unpaid past bill, and actions that need a legal or court process, according to the IRS.</p>

<p><strong>Example:</strong> the first post-discharge statement is dated October 6, 2026. Day 120 is February 3, 2027. Day 240 is June 3, 2027.</p>

<p>Two limits: 501(r) applies to tax-exempt hospitals, and separate physician or ambulance companies may not be covered. See <a href="/guides/hospital-financial-assistance-charity-care/">how hospital financial assistance works</a> to apply.</p>

<h2 id="records">5. Get your billing records under HIPAA</h2>

<p>The HIPAA Privacy Rule gives you the right to see and get a copy of your records (45 CFR 164.524). Those records include the <em>designated record set</em>, which the rule defines to cover the medical records and billing records a provider keeps about you. For health plans, it covers enrollment, payment and claims records.</p>

<ul>
    <li><strong>Timing:</strong> the provider must act within 30 days of your request. It may take one extension of up to 30 more days if it gives you the reason and a new date in writing.</li>
    <li><strong>Written requests:</strong> it may require your request in writing, if it tells you so.</li>
    <li><strong>Fees:</strong> it may charge only a reasonable, cost-based fee for copies, covering labor, supplies and postage.</li>
    <li><strong>Format:</strong> you can ask for a specific format, such as electronic copies, if the provider can readily produce it.</li>
</ul>

<p>Log the request date so you know when day 30 lands. Step-by-step help: <a href="/guides/how-to-request-medical-records/">how to request your medical records</a>. For the line-by-line bill, also see <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a>.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Your tracker is your paper trail. Record every request, call and date. Once the itemized bill arrives, <a href="/scan">check it free</a> for duplicate lines and charges well above the Medicare benchmark.</p>
</div>

<h2 id="who-to-call">6. Call the insurer or the provider?</h2>

<p>Use this rule of thumb, based on CMS guidance:</p>

<table>
    <thead>
        <tr>
            <th>What you see</th>
            <th>Who to contact</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Bill is higher than the EOB&rsquo;s &ldquo;What You Owe&rdquo;</td>
            <td>Provider who sent the bill</td>
        </tr>
        <tr>
            <td>Wrong date, a service you didn&rsquo;t get, or a code you don&rsquo;t understand</td>
            <td>Provider</td>
        </tr>
        <tr>
            <td>Claim denied, or a covered service paid at $0</td>
            <td>Insurer (phone number is on the EOB)</td>
        </tr>
        <tr>
            <td>Bill arrived but no EOB after a few weeks</td>
            <td>Insurer, to confirm the claim was received</td>
        </tr>
        <tr>
            <td>EOB matches the bill, but you think the plan decided wrong</td>
            <td>Insurer: ask for an internal appeal, then external review</td>
        </tr>
        <tr>
            <td>Surprise out-of-network bill for ER care or from a doctor at an in-network hospital</td>
            <td>Provider and insurer; the No Surprises Help Desk is 1-800-985-3059</td>
        </tr>
    </tbody>
</table>

<p>CMS notes that ground ambulance services currently aren&rsquo;t covered by the No Surprises Act&rsquo;s billing protections, though state law may add limits. Air ambulance is covered. More on <a href="/guides/no-surprises-act-explained/">the No Surprises Act</a>.</p>

<p>After each call, note the date, name and reference number.</p>

<h2 id="weekly-routine">7. Your 15-minute weekly routine</h2>

<p>Pick one day a week:</p>

<ol>
    <li><strong>Open new mail and your insurer&rsquo;s portal.</strong> Add new bills; fill in EOB columns.</li>
    <li><strong>Do the math</strong> on each new row, as in the samples above.</li>
    <li><strong>Compare the two &ldquo;You owe&rdquo; columns.</strong> Mark any gap in Status.</li>
    <li><strong>Check your dates.</strong> Look at the 120-day and 240-day dates for any nonprofit hospital bill, and day 30 on any records request.</li>
    <li><strong>Make one call or send one letter</strong> on the row with the nearest deadline.</li>
    <li><strong>Update &ldquo;Next action&rdquo; for every open row.</strong> Close a row when the balance is $0 or confirmed paid.</li>
    <li><strong>File the paper.</strong> One folder per stay, each bill clipped to its EOB.</li>
</ol>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Pay rows that match their EOB once you have checked for financial assistance. Question rows that don&rsquo;t. For the hospital row, you can <a href="/scan">check your bill free</a> before you pay.</p>
</div>

<h2 id="red-flags">8. Red flags to act on</h2>

<ul>
    <li><strong>The bill is higher than the EOB.</strong> Ask the provider to apply the insurer&rsquo;s adjustment.</li>
    <li><strong>A bill with no EOB.</strong> Ask the provider whether it billed your plan.</li>
    <li><strong>A date of service you don&rsquo;t recognize.</strong> Ask the provider.</li>
    <li><strong>The same code twice on the same day.</strong> Ask whether it was given twice or is a duplicate.</li>
    <li><strong>A collection letter early.</strong> If a nonprofit hospital starts an extraordinary collection action before day 120 or without the 30-day notice, ask the hospital to explain, and ask for a financial assistance application.</li>
        <li><strong>No answer to a records request after 30 days</strong> and no written extension. Follow up in writing.</li>
    <li><strong>A court paper or wage garnishment notice.</strong> Consider talking to a consumer attorney or legal aid right away. See <a href="/guides/medical-debt-collections-rights/">your rights in medical debt collections</a>.</li>
</ul>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Why did I get several bills for one hospital visit?</h3>
        <p>The hospital bills for the facility, and doctors, labs, imaging groups and ambulance services often bill separately. Your insurer can send a separate explanation of benefits (EOB) for each provider, each type of service and each day of treatment, according to CMS.</p>
    </div>
    <div class="faq-item">
        <h3>What should I do if my bill is higher than my EOB?</h3>
        <p>CMS says the amount you owe on the bill should match the What You Owe amount on your EOB, and you should not pay more than the EOB shows. If the bill is higher, contact the provider who sent it and ask them to correct it. If the EOB itself looks wrong, contact your insurer.</p>
    </div>
    <div class="faq-item">
        <h3>How long does a nonprofit hospital have to wait before sending my bill to collections?</h3>
        <p>Under IRS rules for tax-exempt hospitals (section 501(r)), the hospital must wait at least 120 days after the first post-discharge billing statement before starting extraordinary collection actions such as selling the debt, reporting it to credit bureaus or using a court process. You have at least 240 days from that first statement to apply for financial assistance.</p>
    </div>
    <div class="faq-item">
        <h3>Can I get my billing records from the hospital?</h3>
        <p>Yes. Under HIPAA (45 CFR 164.524) you have a right to a copy of your records in the designated record set, which includes billing records a provider keeps about you. The provider must act within 30 days, with one possible 30-day extension if it tells you why in writing. It can charge only a reasonable, cost-based fee for copies.</p>
    </div>
    <div class="faq-item">
        <h3>Should I call my insurer or the provider first?</h3>
        <p>Call the provider when the bill does not match the EOB, or when a date, service or code looks wrong. Call the insurer when the EOB itself looks wrong: a denied claim, a missing claim, or a provider treated as out of network that should not be. If you still disagree after the insurer answers, you can ask for an internal appeal and then an external review.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.irs.gov/charities-non-profits/billing-and-collections-section-501r6" target="_blank" rel="noopener">IRS &mdash; Billing and Collections, Section 501(r)(6)</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/26/1.501(r)-6" target="_blank" rel="noopener">26 CFR 1.501(r)-6 &mdash; Billing and collection (via Cornell LII)</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/45/164.524" target="_blank" rel="noopener">45 CFR 164.524 &mdash; Access of individuals to protected health information (via Cornell LII)</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/45/164.501" target="_blank" rel="noopener">45 CFR 164.501 &mdash; Definitions, including designated record set (via Cornell LII)</a></li>
    <li><a href="https://cms.gov/medical-bill-rights/help/guides/explanation-of-benefits" target="_blank" rel="noopener">CMS &mdash; How to read an explanation of benefits (EOB)</a></li>
    <li><a href="https://www.cms.gov/medical-bill-rights/help/guides/how-to-read-bill" target="_blank" rel="noopener">CMS &mdash; How to read your medical bill</a></li>
    <li><a href="https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/find-action-plan-your-medical-bill/action-plan-bill-network-provider" target="_blank" rel="noopener">CMS &mdash; Action plan: Bill with an in-network provider</a></li>
    <li><a href="https://www.cms.gov/medical-bill-rights/know-your-rights/using-insurance" target="_blank" rel="noopener">CMS &mdash; Know your rights when using health insurance</a></li>
    <li><a href="https://www.cms.gov/nosurprises/consumers" target="_blank" rel="noopener">CMS &mdash; No Surprises Act: consumers</a></li>
    <li><a href="https://www.medicare.gov/coverage/emergency-department-services" target="_blank" rel="noopener">Medicare.gov &mdash; Emergency department services</a></li>
    <li><a href="https://www.ama-assn.org/practice-management/cpt/cpt-overview-and-code-approval" target="_blank" rel="noopener">American Medical Association &mdash; CPT overview and code approval</a></li>
    <li><a href="https://www.cms.gov/Outreach-and-Education/MLN/WBT/MLN7388180-MLN-WBT-1450/1450/lesson05/13/index.html" target="_blank" rel="noopener">CMS Medicare Learning Network &mdash; Revenue codes (CMS-1450)</a></li>
    <li><a href="https://resdac.org/articles/how-identify-hospital-claims-emergency-room-visits-medicare-claims-data" target="_blank" rel="noopener">ResDAC &mdash; How to identify hospital claims for emergency room visits (revenue codes 0450&ndash;0459)</a></li>
    <li><a href="https://hfs.illinois.gov/medicalproviders/notices/notice.prn120516a.html" target="_blank" rel="noopener">Illinois HFS &mdash; Provider notice on emergency department codes (including 99284)</a></li>
    <li><a href="https://cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r3619cp.pdf" target="_blank" rel="noopener">CMS &mdash; Transmittal R3619CP (CPT 80053, comprehensive metabolic panel)</a></li>
</ul>
""",
})
