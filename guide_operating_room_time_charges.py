"""Guide: Operating Room Charges: How OR Time Is Billed."""

from guides import register

register("operating-room-time-charges", {
    "title": "Operating Room Charges: How OR Time Is Billed",
    "meta_description": "Operating room charges are usually priced by time units from the hospital’s chargemaster. Learn how to check the minutes against your surgery records.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "How do hospitals bill for operating room time?",
            "a": "Many hospitals price operating room use in time increments, such as a first block of minutes plus each additional block. The increments and prices are set by each hospital in its chargemaster, its master list of charges, so they differ from hospital to hospital. On an itemized bill, these lines usually appear under revenue code 036X (operating room services)."
        },
        {
            "q": "Where can I find how long my surgery actually took?",
            "a": "Look at the operative report and the anesthesia record from your surgery. The anesthesia record usually lists times such as when you entered and left the operating room and when anesthesia started and stopped. Under HIPAA you have a right to copies of your medical and billing records, and the provider must act on your request within 30 days, with one possible 30-day extension."
        },
        {
            "q": "Why do I have separate charges for the operating room, recovery room and anesthesia?",
            "a": "They are different services. The hospital bills for the operating room (revenue code 036X), anesthesia supplies and services (037X) and the recovery room (071X). The anesthesiologist or nurse anesthetist usually sends a separate professional bill based on anesthesia base units plus time units."
        },
        {
            "q": "How are anesthesia time units calculated?",
            "a": "Under Medicare rules, anesthesia time runs from when the anesthesia practitioner starts preparing you for anesthesia until you can safely be placed under postoperative care. The claim reports actual minutes, and Medicare divides those minutes by 15 and rounds to one decimal place. Payment is base units plus time units, multiplied by a conversion factor. Private insurers may use their own rules."
        },
        {
            "q": "Can I find out what the hospital charges per unit of operating room time?",
            "a": "Yes. Federal rules (45 CFR 180.50) require hospitals to post a free, machine-readable file of their standard charges, including gross charges from the chargemaster, without requiring an account or personal information. You can also ask the billing office in writing for the per-unit rate and the definition of the time unit used on your bill."
        },
        {
            "q": "Is an operating room billed the same way at a surgery center?",
            "a": "Not usually for Medicare. Medicare makes a single facility payment to an ambulatory surgical center for a covered procedure, with certain items packaged into it, rather than paying by the minute. A hospital outpatient department bills on a hospital claim that can show timed operating room lines. Your own bill may still list itemized charges, so read it line by line."
        },
    ],
    "body": f"""
<p class="lead">Operating room charges are usually billed in time units: the hospital counts the minutes your surgery used the room and multiplies by a per-unit price from its chargemaster, its master list of prices. You can check those minutes yourself by comparing the units on your itemized bill with the times written in your operative report and anesthesia record.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-or-is-billed">How operating room time is billed</a></li>
        <li><a href="#revenue-codes">The revenue codes on a surgery bill</a></li>
        <li><a href="#find-times">Where to find the real times</a></li>
        <li><a href="#anesthesia-units">Anesthesia time units on the anesthesia bill</a></li>
        <li><a href="#example">Example: checking the minutes</a></li>
        <li><a href="#steps">What to do: step by step</a></li>
        <li><a href="#chargemaster-rate">How to get the per-unit chargemaster rate</a></li>
        <li><a href="#asc-vs-hospital">Surgery center vs. hospital outpatient</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-or-is-billed">1. How operating room time is billed</h2>

<p>When you have surgery in a hospital, the hospital charges for the use of the operating room (OR): the room itself, the staff who run it and the equipment in it. Many hospitals price this by time. A common setup is a charge for a first block of time and then a charge for each additional block.</p>

<p>There is no single national time unit. Each hospital sets its own increments and prices in its chargemaster. Federal rules define the chargemaster as the list of all items and services a hospital keeps for which it has set a charge. Your own bill and your hospital&rsquo;s price file are the best guides to how your OR time was counted.</p>

<p>Hospitals can also define the start and end of &ldquo;OR time&rdquo; differently, so ask the billing office which start and stop times they used.</p>

<h2 id="revenue-codes">2. The revenue codes on a surgery bill</h2>

<p>A revenue code is a four-digit code on a hospital bill that tells you which department or type of service a charge belongs to. The &ldquo;X&rdquo; at the end means any last digit in that group. Medicare contractor Noridian lists these codes, which you will often see on a surgery bill:</p>

<table>
    <thead>
        <tr>
            <th>Revenue code</th>
            <th>What it covers</th>
            <th>Often priced by time?</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>036X (0360 general, 0361 minor surgery, 0362 and 0367 transplants, 0369 other)</td>
            <td>Operating room services</td>
            <td>Often, depending on the hospital&rsquo;s chargemaster</td>
        </tr>
        <tr>
            <td>037X (0370 general and others)</td>
            <td>Anesthesia supplies and services billed by the hospital</td>
            <td>Sometimes</td>
        </tr>
        <tr>
            <td>071X (0710 general)</td>
            <td>Recovery room</td>
            <td>Often, depending on the hospital&rsquo;s chargemaster</td>
        </tr>
    </tbody>
</table>

<p>Medicare&rsquo;s claims manual tells hospitals to group charges at the &ldquo;zero&rdquo; level (for example, 0360) where possible, so a summary bill may show one large OR line. An itemized bill breaks that line into units, which is what you need to check the minutes. For more on the codes, see our guide to <a href="/guides/hospital-revenue-codes-explained/">hospital revenue codes</a>.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>You can only check OR minutes if you can see the units. If your bill shows one total for surgery, ask for an itemized bill first. Our guide on <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a> walks you through the request.</p></div>

<h2 id="find-times">3. Where to find the real times</h2>

<p>The minutes on your bill should line up with times recorded in your medical records. Two records matter most:</p>

<ul>
    <li><strong>The anesthesia record.</strong> This is a minute-by-minute chart kept during surgery. It usually lists times such as &ldquo;in room&rdquo; and &ldquo;out of room,&rdquo; anesthesia start and stop, and often incision (first cut) and closure.</li>
    <li><strong>The operative report.</strong> The surgeon&rsquo;s write-up of the procedure. It may list the start and end of surgery and describes what was done.</li>
    <li><strong>Recovery room (PACU) notes.</strong> PACU means post-anesthesia care unit. Nursing notes there usually show when you arrived and when you were discharged or moved.</li>
</ul>

<p>You have a legal right to these papers. Under the HIPAA Privacy Rule, you can get a copy of your records in the provider&rsquo;s &ldquo;designated record set,&rdquo; which includes both medical records and billing records. The provider must act on your request within 30 days and can extend that once, by up to 30 more days, if it tells you why in writing. It may charge only a reasonable, cost-based fee. Our guide on <a href="/guides/how-to-request-medical-records/">how to request medical records</a> has a sample request.</p>

<h2 id="anesthesia-units">4. Anesthesia time units on the anesthesia bill</h2>

<p>The anesthesiologist or nurse anesthetist (CRNA) usually bills you separately from the hospital. This professional bill uses its own time math, and Medicare spells it out in its Claims Processing Manual, Chapter 12, Section 50:</p>

<ul>
    <li><strong>Base units.</strong> Each anesthesia procedure code has a fixed number of base units that reflects how complex it is. CMS publishes these values each year.</li>
    <li><strong>Time units.</strong> Anesthesia time starts when the anesthesia practitioner begins preparing you for anesthesia in the OR or a similar area. It ends when you can safely be placed under postoperative care. The claim reports actual minutes. Medicare divides the minutes by 15 and rounds to one decimal place.</li>
    <li><strong>Payment.</strong> Medicare pays base units plus time units, multiplied by a conversion factor for your area.</li>
</ul>

<p>These are Medicare rules; private insurers&rsquo; contracts can differ, so check your plan&rsquo;s explanation of benefits (EOB). Because anesthesia time can begin before you are wheeled in, anesthesia minutes and OR minutes may not match exactly. A gap of a few minutes can be normal; a large gap is worth asking about. Our guide to <a href="/guides/anesthesia-billing/">anesthesia billing</a> covers the professional bill in more depth.</p>

<h2 id="example">5. Example: checking the minutes</h2>

<p><strong>Example:</strong> This is an illustration with made-up prices, not real data from any hospital.</p>

<p>Suppose a hospital&rsquo;s chargemaster lists OR time as $3,000 for the first 30 minutes and $750 for each additional 15 minutes. Recovery room is $400 per 30 minutes.</p>

<table>
    <thead>
        <tr>
            <th>Item</th>
            <th>From the records</th>
            <th>Units supported</th>
            <th>Units billed</th>
            <th>Difference</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>OR time (0360)</td>
            <td>In room 7:55, out 10:25 = 150 minutes</td>
            <td>First 30 min + 8 extra units (120 &divide; 15) = $3,000 + $6,000 = $9,000</td>
            <td>First 30 min + 10 extra units = $3,000 + $7,500 = $10,500</td>
            <td>2 units, $1,500</td>
        </tr>
        <tr>
            <td>Recovery room (0710)</td>
            <td>Arrived 10:30, discharged 12:00 = 90 minutes</td>
            <td>3 units (90 &divide; 30) = $1,200</td>
            <td>3 units = $1,200</td>
            <td>None</td>
        </tr>
    </tbody>
</table>

<p>In this example the recovery room matches, but the OR line shows 150 minutes in the records and 180 minutes on the bill (30 + 10 &times; 15). That 30-minute gap is a question to raise with billing. There may be an explanation, such as a different start marker, so ask before assuming an error.</p>

<p>The same anesthesia record can check the professional bill. If anesthesia ran from 7:50 to 10:22, that is 152 minutes. Under Medicare&rsquo;s method, 152 &divide; 15 = 10.13, rounded to 10.1 time units. If the procedure code carried 5 base units (a made-up figure for this example), the total would be 15.1 units.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>Do the subtraction yourself: out-of-room time minus in-room time, then divide by the hospital&rsquo;s unit size. If the units on the bill are higher, you have a specific, polite question to ask. You can <a href="/scan">check your bill free</a> to flag lines worth a closer look.</p></div>

<h2 id="steps">6. What to do: step by step</h2>

<ol>
    <li><strong>Get the itemized bill.</strong> Ask for a bill that lists each line with its revenue code, CPT or HCPCS code (the standard codes for medical services and supplies), units and price.</li>
    <li><strong>Request your surgery records.</strong> Ask for the anesthesia record, operative report and recovery room notes for your date of surgery.</li>
    <li><strong>Find the OR and recovery lines.</strong> Look for revenue codes 036X and 071X and note the units and price on each.</li>
    <li><strong>Calculate the minutes.</strong> Subtract the start time from the end time in the records. Divide by the hospital&rsquo;s unit size to get the units you would expect.</li>
    <li><strong>Compare.</strong> Write down any line where billed units are higher than the records support, and the dollar difference.</li>
    <li><strong>Ask in writing.</strong> Send the billing office a short letter listing each line, the times from your records and your question. Ask them to explain or correct the units. Keep copies.</li>
    <li><strong>Check your EOB.</strong> If you have insurance, compare what the plan allowed. Tell your insurer about any corrected bill.</li>
    <li><strong>Escalate if needed.</strong> If you do not get a clear answer, follow up with the hospital&rsquo;s patient financial services manager. For serious disputes, consider talking to a consumer attorney or legal aid.</li>
</ol>

<h2 id="chargemaster-rate">7. How to get the per-unit chargemaster rate</h2>

<p>To check the dollars, not just the minutes, you need the price per unit. Under the federal hospital price transparency rule (45 CFR 180.50), hospitals must post a machine-readable file of their standard charges. That file must include gross charges (the chargemaster price before discounts), the discounted cash price, payer-specific negotiated charges and the minimum and maximum negotiated charges. The rule says the file must be free, must not require an account or password, must not require personal information and must be updated at least once a year.</p>

<p>CMS says enforcement of new and updated price transparency requirements from its 2026 rule began April 1, 2026. If you cannot find the file on a hospital&rsquo;s website, CMS accepts complaints through its price transparency page.</p>

<p>The files can be large. Search them for words like &ldquo;OR,&rdquo; &ldquo;operating room,&rdquo; &ldquo;surgery&rdquo; or &ldquo;recovery,&rdquo; or for the 0360 and 0710 codes. You can also ask the billing office directly: &ldquo;What is the chargemaster rate per unit for the OR and recovery room lines on my bill, and how long is each unit?&rdquo; Our guides to the <a href="/guides/hospital-chargemaster-explained/">hospital chargemaster</a> and <a href="/guides/hospital-price-transparency/">hospital price transparency</a> explain these files in more detail.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>Pair the per-unit price with the minutes from your records, then put your question in writing. Our <a href="/guides/medical-bill-dispute-letter/">medical bill dispute letter guide</a> has a template you can adapt for OR and recovery room units.</p></div>

<h2 id="asc-vs-hospital">8. Surgery center vs. hospital outpatient</h2>

<p>Where you had surgery changes how the facility fee is built:</p>

<ul>
    <li><strong>Hospital outpatient department.</strong> The hospital bills on a hospital claim form using revenue codes, so timed OR and recovery room lines like 0360 and 0710 can appear.</li>
    <li><strong>Ambulatory surgical center (ASC).</strong> An ASC is an outpatient facility that performs surgery, and most patients leave the same day. For Medicare, ASCs bill on a professional claim form, and Medicare makes a single payment for the ASC&rsquo;s facility services tied to a covered procedure, with certain items packaged into it. Medicare does not pay the ASC by the minute.</li>
</ul>

<p>An ASC bill may still show itemized charges, so check it the same way. Medicare&rsquo;s Procedure Price Lookup tool shows national average Medicare payments and copayments for procedures done in both settings. See our guide to <a href="/guides/surgery-center-vs-hospital-cost/">surgery center vs. hospital costs</a> for more.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How do hospitals bill for operating room time?</h3>
        <p>Many hospitals price operating room use in time increments, such as a first block of minutes plus each additional block. The increments and prices are set by each hospital in its chargemaster, its master list of charges, so they differ from hospital to hospital. On an itemized bill, these lines usually appear under revenue code 036X (operating room services).</p>
    </div>
    <div class="faq-item">
        <h3>Where can I find how long my surgery actually took?</h3>
        <p>Look at the operative report and the anesthesia record from your surgery. The anesthesia record usually lists times such as when you entered and left the operating room and when anesthesia started and stopped. Under HIPAA you have a right to copies of your medical and billing records, and the provider must act on your request within 30 days, with one possible 30-day extension.</p>
    </div>
    <div class="faq-item">
        <h3>Why do I have separate charges for the operating room, recovery room and anesthesia?</h3>
        <p>They are different services. The hospital bills for the operating room (revenue code 036X), anesthesia supplies and services (037X) and the recovery room (071X). The anesthesiologist or nurse anesthetist usually sends a separate professional bill based on anesthesia base units plus time units.</p>
    </div>
    <div class="faq-item">
        <h3>How are anesthesia time units calculated?</h3>
        <p>Under Medicare rules, anesthesia time runs from when the anesthesia practitioner starts preparing you for anesthesia until you can safely be placed under postoperative care. The claim reports actual minutes, and Medicare divides those minutes by 15 and rounds to one decimal place. Payment is base units plus time units, multiplied by a conversion factor. Private insurers may use their own rules.</p>
    </div>
    <div class="faq-item">
        <h3>Can I find out what the hospital charges per unit of operating room time?</h3>
        <p>Yes. Federal rules (45 CFR 180.50) require hospitals to post a free, machine-readable file of their standard charges, including gross charges from the chargemaster, without requiring an account or personal information. You can also ask the billing office in writing for the per-unit rate and the definition of the time unit used on your bill.</p>
    </div>
    <div class="faq-item">
        <h3>Is an operating room billed the same way at a surgery center?</h3>
        <p>Not usually for Medicare. Medicare makes a single facility payment to an ambulatory surgical center for a covered procedure, with certain items packaged into it, rather than paying by the minute. A hospital outpatient department bills on a hospital claim that can show timed operating room lines. Your own bill may still list itemized charges, so read it line by line.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c12.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 12, Section 50 (Payment for Anesthesiology Services)</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c25.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 25 (Form CMS-1450, FL 42 Revenue Code)</a></li>
    <li><a href="https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c14.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 14 (Ambulatory Surgical Centers)</a></li>
    <li><a href="https://med.noridianmedicare.com/web/jfa/topics/claim-submission/revenue-codes" target="_blank" rel="noopener">Noridian Medicare JF Part A &mdash; Revenue Codes</a></li>
    <li><a href="https://www.govinfo.gov/content/pkg/CFR-2024-title45-vol2/xml/CFR-2024-title45-vol2-sec180-50.xml" target="_blank" rel="noopener">GovInfo &mdash; 45 CFR 180.50, Requirements for making public hospital standard charges</a></li>
    <li><a href="https://www.govinfo.gov/content/pkg/CFR-2024-title45-vol2/xml/CFR-2024-title45-vol2-sec180-20.xml" target="_blank" rel="noopener">GovInfo &mdash; 45 CFR 180.20, Definitions (chargemaster, gross charge)</a></li>
    <li><a href="https://www.cms.gov/priorities/key-initiatives/hospital-price-transparency" target="_blank" rel="noopener">CMS &mdash; Hospital Price Transparency</a></li>
    <li><a href="https://www.govinfo.gov/content/pkg/CFR-2024-title45-vol2/xml/CFR-2024-title45-vol2-sec164-524.xml" target="_blank" rel="noopener">GovInfo &mdash; 45 CFR 164.524, Access of individuals to protected health information</a></li>
    <li><a href="https://www.govinfo.gov/content/pkg/CFR-2024-title45-vol2/xml/CFR-2024-title45-vol2-sec164-501.xml" target="_blank" rel="noopener">GovInfo &mdash; 45 CFR 164.501, Definitions (designated record set)</a></li>
    <li><a href="https://www.medicare.gov/coverage/ambulatory-surgical-centers" target="_blank" rel="noopener">Medicare.gov &mdash; Ambulatory surgical centers</a></li>
    <li><a href="https://www.medicare.gov/procedure-price-lookup" target="_blank" rel="noopener">Medicare.gov &mdash; Procedure Price Lookup for Outpatient Services</a></li>
    <li><a href="https://www.cms.gov/newsroom/press-releases/new-online-tool-displays-cost-differences-certain-surgical-procedures" target="_blank" rel="noopener">CMS &mdash; New online tool displays cost differences for certain surgical procedures</a></li>
</ul>
""",
})
