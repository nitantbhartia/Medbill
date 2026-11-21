"""Guide: Medical Supply Charges on a Hospital Bill (Revenue Code 0270)."""

from guides import register

register("hospital-supply-charges-0270", {
    "title": "Hospital Supply Charges (Revenue Code 0270) Explained",
    "meta_description": "Supply lines coded 0270, 0272 or 0278 on a hospital bill: what they mean, when Medicare counts them as part of the room or procedure, and what to check.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "What does revenue code 0270 mean on a hospital bill?",
            "a": "Revenue code 0270 is the general category for medical and surgical supplies. CMS lists 0270 as \"medical/surgical supplies, general classification.\" Related codes include 0271 (nonsterile supply), 0272 (sterile supply), 0273 (take-home supplies), 0274 (prosthetic or orthotic devices), 0275 (pacemaker), 0276 (intraocular lens), 0278 (other implants) and 0279 (other devices).",
        },
        {
            "q": "Should gloves and gauze be charged separately on a hospital bill?",
            "a": "Under Medicare's rules, minor medical and surgical supplies used during an inpatient stay are part of routine services, which are covered by the daily room and board charge. For outpatient procedures, Medicare packages routine supplies into the payment for the procedure. A supply line can still appear on your itemized bill, because hospitals are told to report charges for packaged items. Whether you should pay for it separately depends on how you are paying. Private insurance contracts vary, so ask your insurer how it treats supply lines.",
        },
        {
            "q": "Is revenue code 0278 an error?",
            "a": "Not by itself. CMS lists 0278 as \"other implants,\" and hospitals report implanted devices, such as screws, plates or mesh, under it. Check that the implant matches what your procedure records say was placed, that the quantity is right, and that it is not listed twice.",
        },
        {
            "q": "How do I find out what is inside a supply kit or tray charge?",
            "a": "Ask the hospital billing office in writing for a breakdown of the kit and the date and department for each supply line. If you have Medicare, federal law lets you ask in writing for an itemized statement of Medicare items and services, and the provider must send it within 30 days. Compare the kit contents with any separate supply lines on the same date.",
        },
        {
            "q": "Can I dispute supply charges if I have private insurance?",
            "a": "Yes, you can ask questions about any charge. Insurers' contracts with hospitals vary, so the insurer's explanation of benefits shows what was actually allowed and what you owe. Ask both the hospital and the insurer about lines that look duplicated or larger than what you received.",
        },
    ],
    "body": f"""
<p class="lead">Supply lines on a hospital bill are often legitimate, but many of them are not meant to be paid for one by one. Under Medicare&rsquo;s rules, minor supplies like gloves and gauze are part of the daily room charge during an inpatient stay, and routine supplies are packaged into the payment for an outpatient procedure, while implants such as screws, plates or a pacemaker are reported with their own codes. This guide explains what the 027x revenue codes mean, which supply lines deserve a closer look, and how to ask the hospital for a breakdown.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-027x-means">What 027x revenue codes mean</a></li>
        <li><a href="#routine-supplies">Routine supplies: what Medicare&rsquo;s rules say</a></li>
        <li><a href="#implants">When supplies and implants are their own line</a></li>
        <li><a href="#what-to-check">Five things to check on supply lines</a></li>
        <li><a href="#example">Example: reading a supply section</a></li>
        <li><a href="#what-to-do">What to do, step by step</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-027x-means">1. What 027x revenue codes mean</h2>

<p>A <strong>revenue code</strong> is a four-digit number that tells you which hospital department or cost center a charge came from. It is different from a CPT code (the billing code for a specific service). CMS describes the revenue center code as the code that identifies the cost center, such as radiology or the emergency room, for which a separate charge is billed. For a full tour of these codes, see our guide to <a href="/guides/hospital-revenue-codes-explained/">hospital revenue codes</a>.</p>

<p>Codes that start with 027 are the medical and surgical supplies and devices family. Here is how CMS describes each one:</p>

<table>
    <thead>
        <tr>
            <th>Code</th>
            <th>CMS description</th>
            <th>What you might see on the bill</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>0270</td><td>Medical/surgical supplies, general classification</td><td>&ldquo;Med/surg supply,&rdquo; &ldquo;supplies&rdquo;</td></tr>
        <tr><td>0271</td><td>Nonsterile supply</td><td>Exam gloves, tape, pads</td></tr>
        <tr><td>0272</td><td>Sterile supply</td><td>&ldquo;Sterile supply,&rdquo; trays, kits, sterile gauze</td></tr>
        <tr><td>0273</td><td>Take-home supplies</td><td>Dressings sent home with you</td></tr>
        <tr><td>0274</td><td>Prosthetic/orthotic devices</td><td>Braces, artificial limbs</td></tr>
        <tr><td>0275</td><td>Pacemaker</td><td>Pacemaker device</td></tr>
        <tr><td>0276</td><td>Intraocular lens</td><td>Lens implanted during cataract surgery</td></tr>
        <tr><td>0277</td><td>Oxygen, take-home</td><td>Oxygen sent home with you</td></tr>
        <tr><td>0278</td><td>Other implants</td><td>Screws, plates, mesh, stents</td></tr>
        <tr><td>0279</td><td>Other devices</td><td>Devices not listed above</td></tr>
    </tbody>
</table>

<p>Revenue codes describe the department, not the item. Two lines can share the code 0272 and be completely different things, so the item description, the date and the quantity matter more than the code.</p>

<h2 id="routine-supplies">2. Routine supplies: what Medicare&rsquo;s rules say</h2>

<p>Medicare splits hospital services into two groups. <strong>Routine services</strong> are what every patient on a unit gets as part of the daily room charge. <strong>Ancillary services</strong> are extras charged on top, such as lab tests, imaging, drugs and operating room time.</p>

<p><strong>Inpatient stays.</strong> The Medicare Provider Reimbursement Manual (section 2202.6) says routine services are generally those included in a daily service charge, &ldquo;sometimes referred to as the room and board charge.&rdquo; It lists the regular room, dietary and nursing services, <em>minor medical and surgical supplies</em>, and the use of equipment and facilities for which a separate charge is not customarily made. The Medicare Claims Processing Manual (chapter 4, section 240) repeats that list.</p>

<p>Section 2203 of the same manual adds two conditions. Medicare does not recognize a separate charge for an item when the common practice of hospitals in the same state is to include it in the room charge. And a separate charge counts only if the hospital charges it the same way to every patient, not just Medicare patients. The Claims Processing Manual says that if these instructions are not followed, a provider cannot bill these services as separate charges.</p>

<p><strong>Outpatient procedures and ER visits.</strong> Under Medicare&rsquo;s outpatient payment system, routine supplies are <em>packaged</em>, meaning their cost is built into the payment for the main procedure. The Claims Processing Manual (chapter 4, section 10.4) gives this example: routine supplies, anesthesia, recovery room use and most drugs are an integral part of a surgical procedure, so payment for them is packaged. The federal rule at 42 CFR 419.2(b)(4) lists medical and surgical supplies and surgical dressings among the costs included in that payment.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Under Medicare&rsquo;s rules, minor supplies are part of the room charge for an inpatient stay and are packaged into the procedure payment for outpatient care. If your bill lists many small supply lines, <a href="/scan">check your bill free</a> to see which lines are worth asking about.</p>
</div>

<p>One important detail: CMS also tells hospitals to report the charges for packaged items on the claim, because those charges feed into future payment rates. So a supply line on your itemized bill is not, by itself, a mistake. What it means for your balance depends on how you are paying:</p>

<ul>
    <li><strong>Medicare:</strong> your Medicare Summary Notice shows what Medicare allowed. Packaged supplies do not get a separate payment. Our guide to the <a href="/guides/medicare-summary-notice-vs-hospital-bill/">Medicare Summary Notice vs. the hospital bill</a> shows how to line the two up.</li>
    <li><strong>Private insurance:</strong> contracts between insurers and hospitals vary. Your explanation of benefits (EOB) shows what the plan allowed for each line and what you owe.</li>
    <li><strong>Self-pay or uninsured:</strong> you may be billed each line at the hospital&rsquo;s list price, so every supply line is worth reading closely.</li>
</ul>

<h2 id="implants">3. When supplies and implants are their own line</h2>

<p>Not every 027x line is a routine supply. Implants and devices are expensive, specific to you, and usually reported with their own revenue codes, often with a device code (a HCPCS code) next to them. A 2003 CMS program memo listed codes such as 0275, 0276 and 0278 (&ldquo;other implants&rdquo;) for reporting implantable devices.</p>

<p>Medicare&rsquo;s own claim edits show the difference. For one type of inpatient claim billed under Part B, the Claims Processing Manual (chapter 4, section 240.2) blocks codes 0270 through 0273, the general, nonsterile, sterile and take-home supply codes, while allowing 0274, 0275, 0276 and 0278, the device and implant codes.</p>

<p>Under the outpatient payment system, implantable devices are also part of the procedure payment (42 CFR 419.2(b)(11)). But they still appear on the itemized bill, and they are often among the largest supply charges. For an implant line, the question is not &ldquo;should this be here?&rdquo; but &ldquo;is this the right device, the right number, and listed only once?&rdquo;</p>

<h2 id="what-to-check">4. Five things to check on supply lines</h2>

<ol>
    <li><strong>Duplicates.</strong> The same item, same date, same quantity, listed twice. This happens when two departments both enter a charge. See our guide to <a href="/guides/duplicate-charges-hospital-bills/">duplicate charges</a>.</li>
    <li><strong>Quantity errors.</strong> A quantity of 20 where you would expect 2, or a line that keeps repeating across days after the item was no longer used. Multiply the unit price by the quantity and make sure it matches the line total.</li>
    <li><strong>Kits billed with their own parts.</strong> A &ldquo;laceration tray&rdquo; or &ldquo;IV start kit&rdquo; usually contains drapes, gauze, gloves or tubing. If the kit is billed and the same items are also billed alone on the same date, ask whether they were extra or already inside the kit. Charging for parts and the whole is a form of unbundling, covered in our guide to <a href="/guides/upcoding-unbundling-hospital-bills/">upcoding and unbundling</a>.</li>
    <li><strong>Routine items on an inpatient stay.</strong> Gloves, tape, basic dressings and similar items billed daily during a stay. Under Medicare&rsquo;s rules these are generally part of the room charge.</li>
    <li><strong>Vague lines.</strong> &ldquo;Supplies,&rdquo; &ldquo;sterile supply&rdquo; or &ldquo;misc&rdquo; with a large dollar amount and no item named. It is fair to ask what it was.</li>
</ol>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Ask about each supply line you question by name, date and amount. A clear list is easier for the billing office to answer. You can <a href="/scan">check your bill free</a> to flag duplicate and bundled lines.</p>
</div>

<h2 id="example">5. Example: reading a supply section</h2>

<p><strong>Example:</strong> a self-pay patient is treated in the ER for a cut that needs stitches. These are the supply lines on the itemized bill, all on the same date. The prices are made up for illustration.</p>

<table>
    <thead>
        <tr>
            <th>Rev. code</th>
            <th>Description</th>
            <th>Qty</th>
            <th>Unit price</th>
            <th>Line total</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>0272</td><td>Laceration repair tray</td><td>1</td><td>$210.00</td><td>$210.00</td></tr>
        <tr><td>0272</td><td>Sterile drape</td><td>1</td><td>$38.00</td><td>$38.00</td></tr>
        <tr><td>0271</td><td>Gloves, exam, pair</td><td>12</td><td>$6.50</td><td>$78.00</td></tr>
        <tr><td>0272</td><td>Gauze sponge 4x4, sterile</td><td>20</td><td>$4.25</td><td>$85.00</td></tr>
        <tr><td>0272</td><td>Gauze sponge 4x4, sterile</td><td>20</td><td>$4.25</td><td>$85.00</td></tr>
        <tr><td></td><td><strong>Supply total</strong></td><td></td><td></td><td><strong>$496.00</strong></td></tr>
    </tbody>
</table>

<p>Questions worth asking:</p>

<ul>
    <li><strong>The second gauze line ($85.00)</strong> matches the first exactly. Ask whether it is a duplicate.</li>
    <li><strong>The sterile drape ($38.00)</strong> may already be inside the laceration tray. Ask for the tray&rsquo;s contents.</li>
    <li><strong>Twelve pairs of exam gloves ($78.00)</strong> is a quantity to confirm. For an outpatient visit, Medicare would package routine supplies like these into the visit payment.</li>
</ul>

<p>Together these three lines come to $85.00 + $38.00 + $78.00 = $201.00. If all three were removed, the supply total would drop from $496.00 to $295.00. The hospital may explain some of them, so treat $201.00 as the amount to ask about, not an amount you are sure to save.</p>

<h2 id="what-to-do">6. What to do, step by step</h2>

<ol>
    <li><strong>Get the itemized bill.</strong> A summary bill that says &ldquo;supplies: $1,400&rdquo; does not tell you enough. Ask for an itemized bill with revenue codes, item descriptions, dates, quantities and unit prices. Our guide on <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a> walks through the request.</li>
    <li><strong>If you have Medicare, put it in writing.</strong> Federal law (42 U.S.C. 1395b-7) lets you send a written request for an itemized statement of Medicare items or services, and the provider must send it within 30 days. If the statement shows a billing problem, such as duplicate billing, you can ask Medicare to review it within 90 days of receiving it.</li>
    <li><strong>Sort the supply lines.</strong> Group the 027x lines by date. Mark duplicates, quantities that look high, kits with their parts billed alongside, and vague lines.</li>
    <li><strong>Match against your EOB or MSN.</strong> If you have insurance, check what the plan allowed. A supply line that the insurer bundled or denied may still show up on the hospital&rsquo;s statement.</li>
    <li><strong>Ask for a breakdown in writing.</strong> For each line you marked, ask what the item was, which department used it, why the quantity is what it is, and, for kits, what the kit contains. Ask the hospital to correct any line it cannot explain.</li>
    <li><strong>Ask for a hold.</strong> While the questions are open, ask the billing office to put the account on hold so it does not move toward collections.</li>
    <li><strong>Keep records.</strong> Save copies of every letter and note the date and name of anyone you speak with.</li>
</ol>

<p>If your bill is already in collections or you receive legal papers, consider talking to a consumer attorney or legal aid.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>A written question about specific supply lines leaves a paper trail you own. Our <a href="/guides/medical-bill-dispute-letter/">medical bill dispute letter guide</a> shows how to lay out each line and what to ask for.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What does revenue code 0270 mean on a hospital bill?</h3>
        <p>Revenue code 0270 is the general category for medical and surgical supplies. CMS lists 0270 as &ldquo;medical/surgical supplies, general classification.&rdquo; Related codes include 0271 (nonsterile supply), 0272 (sterile supply), 0273 (take-home supplies), 0274 (prosthetic or orthotic devices), 0275 (pacemaker), 0276 (intraocular lens), 0278 (other implants) and 0279 (other devices).</p>
    </div>
    <div class="faq-item">
        <h3>Should gloves and gauze be charged separately on a hospital bill?</h3>
        <p>Under Medicare&rsquo;s rules, minor medical and surgical supplies used during an inpatient stay are part of routine services, which are covered by the daily room and board charge. For outpatient procedures, Medicare packages routine supplies into the payment for the procedure. A supply line can still appear on your itemized bill, because hospitals are told to report charges for packaged items. Whether you should pay for it separately depends on how you are paying. Private insurance contracts vary, so ask your insurer how it treats supply lines.</p>
    </div>
    <div class="faq-item">
        <h3>Is revenue code 0278 an error?</h3>
        <p>Not by itself. CMS lists 0278 as &ldquo;other implants,&rdquo; and hospitals report implanted devices, such as screws, plates or mesh, under it. Check that the implant matches what your procedure records say was placed, that the quantity is right, and that it is not listed twice.</p>
    </div>
    <div class="faq-item">
        <h3>How do I find out what is inside a supply kit or tray charge?</h3>
        <p>Ask the hospital billing office in writing for a breakdown of the kit and the date and department for each supply line. If you have Medicare, federal law lets you ask in writing for an itemized statement of Medicare items and services, and the provider must send it within 30 days. Compare the kit contents with any separate supply lines on the same date.</p>
    </div>
    <div class="faq-item">
        <h3>Can I dispute supply charges if I have private insurance?</h3>
        <p>Yes, you can ask questions about any charge. Insurers&rsquo; contracts with hospitals vary, so the insurer&rsquo;s explanation of benefits shows what was actually allowed and what you owe. Ask both the hospital and the insurer about lines that look duplicated or larger than what you received.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://bluebutton.cms.gov/resources/variables/rev_cntr/" target="_blank" rel="noopener">CMS Blue Button &mdash; Variable: REV_CNTR (revenue center code descriptions, 0270&ndash;0279)</a></li>
    <li><a href="https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/P151_22.zip" target="_blank" rel="noopener">CMS &mdash; Provider Reimbursement Manual, Part 1, Chapter 22, sections 2202.6, 2202.8 and 2203</a></li>
    <li><a href="https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/Downloads/clm104c04.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 4 (sections 10.4, 20.1, 240 and 240.2)</a></li>
    <li><a href="https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-419/subpart-A/section-419.2" target="_blank" rel="noopener">eCFR &mdash; 42 CFR 419.2, Basis of payment (outpatient packaged costs)</a></li>
    <li><a href="https://cms.hhs.gov/regulations-and-guidance/guidance/transmittals/downloads/dwnlds/a03035pdf.pdf" target="_blank" rel="noopener">CMS &mdash; Program Memorandum A-03-035, Reporting of Revenue Codes Under the OPPS (2003)</a></li>
    <li><a href="https://www.law.cornell.edu/uscode/text/42/1395b-7" target="_blank" rel="noopener">Legal Information Institute &mdash; 42 U.S.C. 1395b-7 (itemized statements of Medicare items and services)</a></li>
</ul>
""",
})
