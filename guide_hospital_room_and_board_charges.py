"""Guide: Hospital Room and Board Charges: How to Check Them."""

from guides import register

register("hospital-room-and-board-charges", {
    "title": "Hospital Room and Board Charges: How to Check Them",
    "meta_description": "Room and board is billed per day, and the discharge day is typically not counted. Learn to check the days, room type and ICU days on your hospital bill.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "Should I be charged room and board for the day I went home?",
            "a": "Typically not. Medicare's Claims Processing Manual says the day of discharge is not counted unless you were admitted and discharged the same day, and that there are no accommodation charges on the discharge day. Other payers can differ, so ask the billing office how they count.",
        },
        {
            "q": "How do I count how many room and board days I should have?",
            "a": "Count the midnights you spent as an admitted inpatient, which usually equals the discharge date minus the admission date. Admitted Tuesday and home Saturday is 4 days. A same-day stay counts as 1 day under Medicare rules.",
        },
        {
            "q": "What do revenue codes 0110, 0120 and 0200 mean on my bill?",
            "a": "They are room (accommodation) revenue codes. 011X is a private room, 012X semi-private, 013X a 3 to 4 bed room, 020X intensive care and 021X coronary care. The units next to each code are the days billed in that room type.",
        },
        {
            "q": "Can a hospital charge me extra for a private room?",
            "a": "Under Medicare rules, only if the private room was not medically needed and you or a family member asked for it after being told the price. If you needed isolation or no semi-private bed was open when you were admitted, Medicare covers it. Other insurers have their own rules.",
        },
        {
            "q": "Is observation billed as room and board?",
            "a": "No. Observation is an outpatient service billed by the hour under HCPCS code G0378 and revenue code 0762. If you were in observation before being admitted, your room days should start on your inpatient admission date.",
        },
        {
            "q": "Does Medicare pay hospitals by the day?",
            "a": "Not for most inpatient stays. Medicare pays a set amount per stay based on its diagnosis-related group (DRG), so extra room days usually do not change what Medicare pays. They matter most if you are uninsured or your plan pays a percentage of charges.",
        },
    ],
    "body": f"""
<p class="lead">Room and board is the daily charge for your hospital bed, and it is billed by the day, counted by midnights. The day you go home is typically not billed as a room day, so a 4-night stay should usually show 4 days, not 5. This guide shows how to read the room codes on your bill, check the number of days and the room type, and what to do if something does not match.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-it-covers">What room and board covers</a></li>
        <li><a href="#revenue-codes">The room codes on your bill</a></li>
        <li><a href="#counting-days">How days are counted</a></li>
        <li><a href="#example">Example: checking the day math</a></li>
        <li><a href="#room-type">Private rooms and ICU days</a></li>
        <li><a href="#observation">Observation is not room and board</a></li>
        <li><a href="#who-it-affects">When the daily lines matter most</a></li>
        <li><a href="#what-to-do">What to do, step by step</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-it-covers">1. What room and board covers</h2>

<p>&ldquo;Room and board&rdquo; is the everyday cost of being a hospital inpatient. Billing staff also call it an <strong>accommodation charge</strong> or a routine charge. Medicare describes inpatient hospital coverage as including a semi-private room, meals and general nursing. On a hospital bill, those everyday costs are generally rolled into one daily rate for the type of room you were in.</p>

<p>Lab tests, imaging, drugs, surgery and supplies are billed on their own lines as <strong>ancillary charges</strong>. Because the room rate is charged once per day, even one extra day can add a large amount.</p>

<h2 id="revenue-codes">2. The room codes on your bill</h2>

<p>Hospital bills use <strong>revenue codes</strong> (4-digit codes that group charges by type of service) on the standard hospital claim form, the UB-04. If you ask for an <a href="/guides/how-to-get-itemized-hospital-bill/">itemized bill</a>, you can usually see the revenue code next to each room line.</p>

<p>Here are the main room and board codes, as listed by Noridian, a Medicare contractor. The &ldquo;X&rdquo; is a last digit that narrows the type, such as 0 for general or 1 for medical/surgical.</p>

<table>
    <thead>
        <tr>
            <th>Revenue code</th>
            <th>Room type</th>
            <th>Examples of subcodes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>011X</td>
            <td>Private room (one bed)</td>
            <td>0110 General, 0111 Medical/Surgical/GYN, 0112 Obstetrics</td>
        </tr>
        <tr>
            <td>012X</td>
            <td>Semi-private room (two beds)</td>
            <td>0120 General, 0121 Medical/Surgical/GYN, 0122 OB</td>
        </tr>
        <tr>
            <td>013X</td>
            <td>Room with 3 or 4 beds</td>
            <td>0130 General, 0131 Medical/Surgical/GYN</td>
        </tr>
        <tr>
            <td>014X</td>
            <td>Deluxe private room</td>
            <td>0140 General</td>
        </tr>
        <tr>
            <td>020X</td>
            <td>Intensive care unit (ICU)</td>
            <td>0200 General, 0201 Surgical, 0202 Medical, 0206 Intermediate ICU</td>
        </tr>
        <tr>
            <td>021X</td>
            <td>Coronary care unit (CCU)</td>
            <td>0210 General, 0211 Myocardial Infarction, 0214 Intermediate CCU</td>
        </tr>
    </tbody>
</table>

<p>Two other columns matter. Medicare&rsquo;s claim form instructions say the <strong>units</strong> column shows the number of days in a particular type of room, and on inpatient bills the <strong>rate</strong> column shows the daily accommodation rate. So a line reading &ldquo;0120, 3 units&rdquo; means 3 days in a semi-private room. For a deeper look at all the codes, see our guide to <a href="/guides/hospital-revenue-codes-explained/">hospital revenue codes</a>.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Find every line on your bill with a revenue code from 0110 to 0219 and add up the units. That total is the number of room and board days you were charged. You can <a href="/scan">check your bill free at BillKarma</a> to see each line side by side with its code.</p>
</div>

<h2 id="counting-days">3. How days are counted</h2>

<p>Medicare&rsquo;s Claims Processing Manual (Chapter 3, Section 40.1) sets out the &ldquo;day count&rdquo; rules hospitals use on Medicare claims:</p>

<ul>
    <li><strong>The day you are admitted counts.</strong></li>
    <li><strong>The day you are discharged does not count</strong>, unless you were admitted and discharged on the same day. The same goes for the day of death or the start of a leave of absence.</li>
    <li><strong>Same-day stays count as 1 day.</strong> If you were admitted expecting to stay overnight but were discharged before midnight, that day still counts.</li>
</ul>

<p>The same chapter says there are no accommodation charges on the day of discharge, and it lists room and routine charges for the discharge day among the charges Medicare does not count, unless that day is also the admission day. Lab work or medicine you receive on your last morning can still be billed. It just should not come with another day of room charge.</p>

<p>A simple way to apply this: <strong>count the midnights</strong>. For most stays, the number of room days equals your discharge date minus your admission date. Use the inpatient admission date on the bill, not the time you arrived at the emergency room.</p>

<p>These are Medicare&rsquo;s rules. Many hospitals count the same way on every bill, but private insurance contracts and self-pay policies can differ, so ask the billing office how they counted if yours does not match.</p>

<h2 id="example">4. Example: checking the day math</h2>

<p><strong>Example:</strong> A patient is admitted as an inpatient on Tuesday, March 3 at 10 p.m. and goes straight to the ICU. On Thursday, March 5 at 2 p.m., she moves to a semi-private room. She goes home on Saturday, March 7 at 11 a.m. The rates below are made up for this example.</p>

<p>Midnights as an inpatient: March 3&ndash;4, 4&ndash;5, 5&ndash;6 and 6&ndash;7. That is <strong>4 days</strong> (March 7 minus March 3). Her records show she was in the ICU on the nights of March 3 and 4, and in the semi-private room on the nights of March 5 and 6.</p>

<table>
    <thead>
        <tr>
            <th>Line</th>
            <th>What the bill shows</th>
            <th>What the records support</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0200 ICU at $4,500/day</td>
            <td>3 days = $13,500</td>
            <td>2 days = $9,000</td>
        </tr>
        <tr>
            <td>0120 Semi-private at $2,200/day</td>
            <td>2 days = $4,400</td>
            <td>2 days = $4,400</td>
        </tr>
        <tr>
            <td><strong>Total room and board</strong></td>
            <td><strong>5 days = $17,900</strong></td>
            <td><strong>4 days = $13,400</strong></td>
        </tr>
    </tbody>
</table>

<p>The bill shows 5 room days for a stay with 4 midnights, and the extra day is billed at the ICU rate. The difference is $17,900 &minus; $13,400 = <strong>$4,500</strong>. That is a discrepancy worth asking about in writing. There may be an explanation, such as a transfer time recorded differently.</p>

<h2 id="room-type">5. Private rooms and ICU days</h2>

<h3>Private room charges</h3>

<p>Under Medicare regulations (42 CFR 409.11), Medicare Part A pays for a semi-private room (2 to 4 beds) or a ward. It also pays for a private room if any of these is true:</p>

<ul>
    <li>Your condition required you to be isolated.</li>
    <li>The hospital has no semi-private or ward rooms.</li>
    <li>The semi-private and ward rooms were all full when you were admitted for care you needed right away, and stayed full.</li>
</ul>

<p>In the isolation and full-hospital cases, Medicare pays for the private room until you no longer need isolation or a semi-private bed opens up. The hospital can charge you the difference between its private and semi-private rates only if none of those reasons applied <strong>and</strong> you or a family member asked for the private room after being told what it would cost. If you have Medicare and believe the private room was medically necessary, Medicare&rsquo;s manual says you have a right to a determination and can start a Part A appeal.</p>

<p>With other insurance or none, these exact rules may not apply, but the same questions are fair to ask.</p>

<h3>ICU and coronary care days</h3>

<p>ICU (020X) and coronary care (021X) days are often billed at a much higher daily rate than a regular room. Compare the number of ICU units on your bill with when you actually moved in and out of the unit. Your medical records, discharge summary or the nursing transfer notes usually show those times. If you moved from the ICU to a regular floor during the day, ask the billing office which room type they assigned to that day and why.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Check two things on every room line: the number of days (units) and the type of room (the revenue code). A private room you did not ask for, or one more ICU day than your records show, can add thousands. Our guide to <a href="/guides/common-hospital-billing-errors/">common hospital billing errors</a> covers other lines to check while you have the bill out.</p>
</div>

<h2 id="observation">6. Observation is not room and board</h2>

<p>If you spent time in the hospital under <strong>observation</strong> (care while doctors decide whether to admit you), that time is billed differently. Medicare&rsquo;s Claims Processing Manual (Chapter 4, Section 290) treats observation as an outpatient service. Hospitals report it under revenue code 0762 (observation room) with HCPCS code G0378, &ldquo;hospital observation service, per hour,&rdquo; rounded to the nearest hour. Time spent waiting for a ride home after treatment is finished should not be counted.</p>

<p>That means observation should appear as hours, not as room and board days. When you check your bill:</p>

<ul>
    <li>If you were in observation and never admitted, you should not see 011X to 021X room days for that visit.</li>
    <li>If you were in observation and then admitted, your room days should start on your inpatient admission date. The observation hours before that should appear as observation, not as an extra room day.</li>
</ul>

<p>Your status also affects what you owe under insurance. See our guide to <a href="/guides/hospital-observation-status/">hospital observation status</a> and <a href="/guides/inpatient-vs-outpatient-billing/">inpatient vs. outpatient billing</a>.</p>

<h2 id="who-it-affects">7. When the daily lines matter most</h2>

<p>Whether an extra room day changes what you pay depends on how your stay is paid.</p>

<ul>
    <li><strong>Medicare.</strong> Under Medicare&rsquo;s Inpatient Prospective Payment System, each stay is assigned a <strong>diagnosis-related group (DRG)</strong>, a category based on your diagnosis and treatment, and each DRG has its own payment weight. Because payment is set per stay, an extra room day on the bill usually does not change what Medicare pays the hospital. Your Medicare Summary Notice is the place to check your own share. See <a href="/guides/medicare-summary-notice-vs-hospital-bill/">Medicare Summary Notice vs. hospital bill</a>.</li>
    <li><strong>Uninsured or self-pay.</strong> You may be billed from the hospital&rsquo;s full price list (its chargemaster), so every extra day is added directly to your balance. See our guide for the <a href="/guides/uninsured-hospital-bill/">uninsured hospital bill</a>.</li>
    <li><strong>Plans that pay a percentage of charges, or per day.</strong> Some insurance contracts pay based on billed charges or a daily rate. Then an extra day can raise your coinsurance. Your Explanation of Benefits shows how your plan priced the stay.</li>
</ul>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>If you are uninsured or your plan pays by charges, room and board is often one of the largest lines on an inpatient bill, so the day count matters. <a href="/scan">Upload your bill to BillKarma</a> for a free line-by-line check before you pay.</p>
</div>

<h2 id="what-to-do">8. What to do, step by step</h2>

<ol>
    <li><strong>Get the itemized bill.</strong> A summary bill may show one total for &ldquo;room and board.&rdquo; Ask for a line-item bill with revenue codes, units and dates.</li>
    <li><strong>Write down your dates.</strong> Find your inpatient admission date and discharge date. They appear on the bill, the discharge papers and your patient portal.</li>
    <li><strong>Count the midnights.</strong> Subtract the admission date from the discharge date. For a same-day stay, the answer is 1.</li>
    <li><strong>Add up the room units.</strong> Total the units on every line from 0110 to 0219. Compare that total with your midnight count.</li>
    <li><strong>Check the room type.</strong> Make sure the revenue codes match where you stayed: private (011X), semi-private (012X), ICU (020X) or coronary care (021X). Compare ICU days with transfer times in your records.</li>
    <li><strong>Look for overlap with observation.</strong> Observation hours (0762 / G0378) should not also be billed as room days for the same time.</li>
    <li><strong>Ask in writing.</strong> Send the billing office a short letter or portal message listing the line, the date, what you were billed and what your records show. Ask them to correct it or explain it. Our <a href="/guides/medical-bill-dispute-letter/">medical bill dispute letter guide</a> has a template.</li>
    <li><strong>Ask about financial assistance at the same time.</strong> Many hospitals have assistance programs. See <a href="/guides/hospital-financial-assistance-charity-care/">hospital financial assistance</a>.</li>
</ol>

<p>Keep copies of everything you send and note the date. If the bill has gone to collections or you receive legal papers, consider talking to a consumer attorney or legal aid.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Should I be charged room and board for the day I went home?</h3>
        <p>Typically not. Medicare&rsquo;s Claims Processing Manual says the day of discharge is not counted unless you were admitted and discharged the same day, and that there are no accommodation charges on the discharge day. Other payers can differ, so ask the billing office how they count.</p>
    </div>
    <div class="faq-item">
        <h3>How do I count how many room and board days I should have?</h3>
        <p>Count the midnights you spent as an admitted inpatient, which usually equals the discharge date minus the admission date. Admitted Tuesday and home Saturday is 4 days. A same-day stay counts as 1 day under Medicare rules.</p>
    </div>
    <div class="faq-item">
        <h3>What do revenue codes 0110, 0120 and 0200 mean on my bill?</h3>
        <p>They are room (accommodation) revenue codes. 011X is a private room, 012X semi-private, 013X a 3 to 4 bed room, 020X intensive care and 021X coronary care. The units next to each code are the days billed in that room type.</p>
    </div>
    <div class="faq-item">
        <h3>Can a hospital charge me extra for a private room?</h3>
        <p>Under Medicare rules, only if the private room was not medically needed and you or a family member asked for it after being told the price. If you needed isolation or no semi-private bed was open when you were admitted, Medicare covers it. Other insurers have their own rules.</p>
    </div>
    <div class="faq-item">
        <h3>Is observation billed as room and board?</h3>
        <p>No. Observation is an outpatient service billed by the hour under HCPCS code G0378 and revenue code 0762. If you were in observation before being admitted, your room days should start on your inpatient admission date.</p>
    </div>
    <div class="faq-item">
        <h3>Does Medicare pay hospitals by the day?</h3>
        <p>Not for most inpatient stays. Medicare pays a set amount per stay based on its diagnosis-related group (DRG), so extra room days usually do not change what Medicare pays. They matter most if you are uninsured or your plan pays a percentage of charges.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c03.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 3: Inpatient Hospital Billing (Sections 40.1 and 40.2.2&ndash;40.2.3)</a></li>
    <li><a href="https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c04.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 4: Part B Hospital (Section 290, Observation Services)</a></li>
    <li><a href="https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c25.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 25: Completing and Processing the Form CMS-1450 (UB-04)</a></li>
    <li><a href="https://med.noridianmedicare.com/web/jea/topics/claim-submission/revenue-codes" target="_blank" rel="noopener">Noridian Medicare JE Part A &mdash; Revenue Codes</a></li>
    <li><a href="https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-409/subpart-B/section-409.11" target="_blank" rel="noopener">eCFR &mdash; 42 CFR 409.11, Bed and board</a></li>
    <li><a href="https://www.medicare.gov/coverage/inpatient-hospital-care" target="_blank" rel="noopener">Medicare.gov &mdash; Inpatient hospital care coverage</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/acute-inpatient-pps" target="_blank" rel="noopener">CMS &mdash; Acute Inpatient Prospective Payment System</a></li>
</ul>
""",
})
