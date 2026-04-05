"""Guide: How to Get an Itemized Hospital Bill."""

from guides import register, _embed

register("how-to-get-itemized-hospital-bill", {
    "title": "How to Get an Itemized Hospital Bill — And Why You Should",
    "meta_description": "Learn how to request an itemized hospital bill, read every charge, and spot overcharges. Hospitals must provide one by law. Here's exactly how to get yours.",
    "published": "2026-02-27",
    "author": "BillKarma Team",
    "category": "Taking Action",
    "faqs": [
        {
            "q": "Is a hospital legally required to give me an itemized bill?",
            "a": "Yes. Under HIPAA Section 164.524, you have the right to access your protected health information, which includes billing records. Additionally, the No Surprises Act reinforces your right to receive a detailed bill. Most state consumer protection laws also require hospitals to provide itemized statements upon request. If a hospital refuses, you can file a complaint with HHS Office for Civil Rights or your state attorney general.",
        },
        {
            "q": "How long does it take to get an itemized bill?",
            "a": "By law, hospitals must respond to your request within 30 days (with one possible 30-day extension if they notify you in writing). In practice, most hospitals provide an itemized bill within 5 to 15 business days. If you request it through the patient portal, it may arrive faster. If 30 days pass without a response, follow up in writing and reference your HIPAA right of access.",
        },
        {
            "q": "What is the difference between a summary bill and an itemized bill?",
            "a": "A summary bill groups charges into broad categories like Room and Board, Laboratory, and Pharmacy, showing only totals for each category. An itemized bill breaks down every individual charge with its CPT or HCPCS code, description, quantity, unit price, and total. The itemized version is the only one that lets you verify what you are actually being charged for and catch errors like duplicates, upcoding, and unbundling.",
        },
        {
            "q": "Does requesting an itemized bill cost anything?",
            "a": "Hospitals can charge a reasonable, cost-based fee for copies of medical records under HIPAA, but many hospitals provide itemized billing statements at no charge. If you are asked to pay, the fee should be minimal — typically under $25. Some states cap the amount hospitals can charge. If you are told the fee is excessive, reference your state's medical records fee schedule.",
        },
        {
            "q": "Can I get an itemized bill after I have already paid?",
            "a": "Yes. Your right to an itemized statement does not expire when you pay the bill. You can request one at any time. If you discover errors after paying, you can still dispute the charges and request a refund. There is no deadline for requesting an itemized bill, though disputing errors is easier the sooner you act.",
        },
        {
            "q": "What if my itemized bill does not include CPT codes?",
            "a": "Call the billing department back and specifically ask for a statement that includes CPT or HCPCS codes for every line item. Some hospitals initially send an itemized bill with descriptions but no codes. Without the CPT codes, you cannot look up Medicare rates or check for unbundling errors. You are entitled to the codes — they are part of your billing record.",
        },
    ],
    "body": f"""
<p class="lead">A summary bill just shows totals. An itemized bill shows every single charge&mdash;every IV bag, every pill, every minute of anesthesia. It&rsquo;s the only way to spot overcharges, and hospitals are legally required to provide one when you ask. Yet most patients never request one, and most hospitals don&rsquo;t send one automatically. This guide shows you exactly how to get yours, how to read it, and what to do when you find errors.</p>

<div class="answer-box"><strong>Quick answer</strong>Call the billing department and say "I am requesting an itemized bill showing each CPT code and charge." Hospitals are legally required to provide one. Allow 5–10 business days. If refused, file a complaint with your state health department.</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#summary-vs-itemized">Summary bill vs. itemized bill</a></li>
        <li><a href="#legal-right">Your legal right to an itemized bill</a></li>
        <li><a href="#how-to-request">How to request one</a></li>
        <li><a href="#how-to-read">How to read the itemized bill</a></li>
        <li><a href="#red-flags">5 red flags to look for</a></li>
        <li><a href="#found-errors">What to do when you find errors</a></li>
        <li><a href="#hospital-refuses">What if the hospital refuses or delays</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="summary-vs-itemized">1. Summary bill vs. itemized bill</h2>

<p>When you leave the hospital, the bill you receive in the mail is almost always a <strong>summary statement</strong>. It groups charges into broad categories and shows a single total. It tells you almost nothing about what you&rsquo;re actually paying for. Compare the same visit presented both ways:</p>

<div class="bill-example">
    <div class="bill-header">Summary Statement &mdash; Riverside General Hospital &mdash; Date of Service: 02/10/2026</div>
    <div class="line-item">
        <span>Room &amp; Board</span>
        <span>$3,200.00</span>
    </div>
    <div class="line-item">
        <span>Laboratory Services</span>
        <span>$1,840.00</span>
    </div>
    <div class="line-item">
        <span>Pharmacy</span>
        <span>$3,360.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$8,400.00</span>
    </div>
</div>

<p>That&rsquo;s it. Three lines. No way to tell what you actually received, what each item cost, or whether any charge is wrong. Now look at the same visit itemized:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Riverside General Hospital &mdash; Date of Service: 02/10/2026</div>
    <div class="line-item">
        <span>99284 &mdash; ER Visit Level 4</span>
        <span>$2,890.00</span>
    </div>
    <div class="line-item">
        <span>71046 &mdash; Chest X-ray, 2 views</span>
        <span>$940.00</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive Metabolic Panel</span>
        <span>$487.00</span>
    </div>
    <div class="line-item flagged">
        <span>80048 &mdash; Basic Metabolic Panel &nbsp; &#9888; <em>Bundled into 80053 above</em></span>
        <span>$294.00</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete Blood Count (CBC)</span>
        <span>$182.00</span>
    </div>
    <div class="line-item flagged">
        <span>85025 &mdash; Complete Blood Count (CBC) &nbsp; &#9888; <em>Duplicate charge</em></span>
        <span>$182.00</span>
    </div>
    <div class="line-item">
        <span>96374 &mdash; IV Push, single substance</span>
        <span>$348.00</span>
    </div>
    <div class="line-item">
        <span>96360 &mdash; IV Infusion, first hour</span>
        <span>$412.00</span>
    </div>
    <div class="line-item">
        <span>J2405 &mdash; Ondansetron (Zofran) 4mg injection</span>
        <span>$85.00</span>
    </div>
    <div class="line-item flagged">
        <span>J2405 &mdash; Ondansetron (Zofran) 4mg injection &nbsp; &#9888; <em>Billed x3, patient received x1</em></span>
        <span>$170.00</span>
    </div>
    <div class="line-item">
        <span>J0170 &mdash; Epinephrine injection</span>
        <span>$62.00</span>
    </div>
    <div class="line-item">
        <span>Room &amp; Board &mdash; Med/Surg (02/10)</span>
        <span>$1,840.00</span>
    </div>
    <div class="line-item">
        <span>36000 &mdash; IV Access, peripheral</span>
        <span>$189.00</span>
    </div>
    <div class="line-item">
        <span>99285 &mdash; ER Visit Level 5</span>
        <span>$0.00</span>
    </div>
    <div class="line-item">
        <span>A0427 &mdash; Ambulance, ALS emergency</span>
        <span>$319.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$8,400.00</span>
    </div>
    <div class="line-total">
        <span>Flagged charges</span>
        <span>$646.00</span>
    </div>
</div>

<p>Same $8,400 bill. But the itemized version reveals <strong>$646 in questionable charges</strong> that are invisible on the summary: a duplicate CBC, an unbundled lab panel, and inflated medication quantities. Without the itemized bill, you&rsquo;d never know.</p>

<div class="key-takeaway">
    <strong>The rule is simple:</strong> Never pay a hospital bill based only on a summary statement. Always request the itemized version with CPT codes before you pay anything.
</div>

<h2 id="legal-right">2. Your legal right to an itemized bill</h2>

<p>You are not asking for a favor. You have a legal right to your itemized billing records under multiple federal and state laws.</p>

<p><strong>HIPAA Section 164.524 &mdash; Right of Access.</strong> Under the HIPAA Privacy Rule, you have the right to inspect and obtain a copy of your protected health information (PHI), which includes billing records and claims data. Hospitals must respond to your request within 30 days. They may take one 30-day extension if they notify you in writing, but 60 days is the absolute maximum.</p>

<p><strong>The No Surprises Act (2022).</strong> This federal law strengthened patient billing transparency requirements. Providers must give you a good-faith estimate before scheduled services and provide detailed billing information after treatment. The law reinforces your right to understand every charge on your bill.</p>

<p><strong>State laws.</strong> Most states have additional consumer protection statutes that require hospitals to provide itemized billing upon request. Many states go further than HIPAA:</p>

<ul>
    <li><strong>California</strong> &mdash; Health &amp; Safety Code &sect;1339.56 requires hospitals to provide an itemized statement automatically for bills over $25.</li>
    <li><strong>Texas</strong> &mdash; Health &amp; Safety Code &sect;311.002 requires hospitals to provide itemized bills within a reasonable time after a request.</li>
    <li><strong>New York</strong> &mdash; Public Health Law &sect;2803-j requires hospitals to provide itemized bills to patients and establishes a billing complaint process.</li>
    <li><strong>Florida</strong> &mdash; Florida Statutes &sect;395.301 requires hospitals to provide itemized bills within 7 days of a patient&rsquo;s request.</li>
    <li><strong>Illinois</strong> &mdash; Hospital Uninsured Patient Discount Act requires itemized statements for uninsured patients.</li>
</ul>

<div class="key-takeaway">
    <strong>Bottom line:</strong> If a hospital tells you they &ldquo;can&rsquo;t&rdquo; or &ldquo;don&rsquo;t&rdquo; provide itemized bills, they are wrong. Federal law requires it. State law often adds additional requirements. You have every right to see exactly what you are being charged for.
</div>

<h2 id="how-to-request">3. How to request an itemized bill</h2>

<p>There are three ways to request your itemized bill. Use whichever is most convenient, but always follow up in writing so you have a record.</p>

<h3>Option A: Call Patient Financial Services</h3>

<p><strong>Do not call the general billing number.</strong> Ask the hospital operator to transfer you to <em>Patient Financial Services</em> or the <em>Health Information Management (HIM) department</em>. These departments handle detailed billing records. The general billing line often only deals with payment processing and may not know how to generate a full itemized statement.</p>

<p>Here&rsquo;s the exact script to use:</p>

<div class="case-study">
    <h3>Phone script for requesting an itemized bill</h3>
    <p>&ldquo;Hi, I&rsquo;m calling to request an itemized bill for my recent visit. My name is [NAME] and my account number is [NUMBER]. The date of service was [DATE].</p>
    <p>I need a line-by-line itemized statement that includes the CPT or HCPCS code, description, quantity, and unit price for every charge. A summary statement with category totals is not sufficient&mdash;I need every individual line item.</p>
    <p>Can you tell me how long this will take to prepare, and whether it will be mailed or available through the patient portal?&rdquo;</p>
</div>

<p><strong>Key details to note during the call:</strong> Write down the name of the person you spoke with, the date, and any case or reference number they give you. If they say the request will take more than 10 business days, ask why and reference your right to access under HIPAA.</p>

<h3>Option B: Send a written request via email or patient portal</h3>

<p>A written request creates a timestamped paper trail, which matters if you need to escalate later.</p>

<div class="case-study">
    <h3>Email template for requesting an itemized bill</h3>
    <p><em>Subject: Request for Itemized Bill &mdash; Account #[NUMBER]</em></p>
    <p>Dear Patient Financial Services,</p>
    <p>I am writing to request a complete itemized billing statement for the following visit:</p>
    <p><strong>Patient name:</strong> [NAME]<br>
    <strong>Date of birth:</strong> [DOB]<br>
    <strong>Account number:</strong> [NUMBER]<br>
    <strong>Date of service:</strong> [DATE]</p>
    <p>I am requesting a line-by-line itemized statement that includes:</p>
    <ul>
        <li>CPT or HCPCS code for each charge</li>
        <li>Revenue code</li>
        <li>Description of each service, medication, or supply</li>
        <li>Quantity and unit price</li>
        <li>Date each service was provided</li>
    </ul>
    <p>A summary statement showing only category totals is not sufficient for my review.</p>
    <p>This request is made pursuant to my right of access under HIPAA (45 CFR &sect;164.524). I understand the response is due within 30 days.</p>
    <p>Please send the itemized statement to [YOUR EMAIL/ADDRESS]. Thank you.</p>
    <p><em>Sincerely,<br>[Your Name]<br>[Phone Number]</em></p>
</div>

<h3>Option C: Request through the patient portal</h3>

<p>Many hospital patient portals have a &ldquo;billing&rdquo; or &ldquo;statements&rdquo; section. Check there first&mdash;some hospitals automatically post itemized bills to the portal. If only a summary is available, use the portal&rsquo;s messaging feature to send your written request. Portal messages are timestamped and stored, making them ideal for documentation.</p>

<div class="key-takeaway">
    <strong>Timeline:</strong> Hospitals must respond within 30 days under HIPAA. Most respond in 5&ndash;15 business days. If you haven&rsquo;t received your itemized bill within 15 business days, call to follow up and reference your original request date.
</div>

<h2 id="how-to-read">4. How to read the itemized bill</h2>

<p>Once you have your itemized bill, here&rsquo;s how to decode each column. Every hospital formats their statement slightly differently, but the core information is the same.</p>

<div class="bill-example">
    <div class="bill-header">How to read each column on an itemized bill</div>
    <div class="line-item">
        <span><strong>Date</strong> &mdash; When the service was performed. Check that all dates fall within your actual stay.</span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>Revenue Code</strong> &mdash; A 3&ndash;4 digit code that groups the charge into a billing category (e.g., 0250 = Pharmacy, 0300 = Laboratory, 0120 = Room &amp; Board semi-private).</span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>CPT/HCPCS Code</strong> &mdash; The 5-digit procedure code. This is the most important column. It tells you exactly what service was billed and lets you look up the Medicare rate.</span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>Description</strong> &mdash; A text description of the service. Descriptions can be vague (&ldquo;Lab Services&rdquo;) so always rely on the CPT code for specifics.</span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>Quantity</strong> &mdash; How many units were billed. Verify that the quantity matches what you actually received. Medication quantities are a common source of overcharges.</span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>Unit Price / Total Charge</strong> &mdash; The hospital&rsquo;s chargemaster price for this item. This is <em>not</em> the Medicare rate or the insurance-negotiated rate&mdash;it&rsquo;s the hospital&rsquo;s list price.</span>
        <span></span>
    </div>
</div>

<p>Use the calculator below to look up the Medicare rate for any CPT code on your itemized bill:</p>

{_embed(mode="cost", title="Look up any CPT code from your bill", subtitle="See what Medicare pays for this service in your area.")}

<p>For a deeper dive into reading every section of a medical bill, including insurance adjustments and EOB comparisons, see our <a href="/guides/how-to-read-your-medical-bill">complete guide to reading your medical bill</a>.</p>

<h2 id="red-flags">5. Five red flags to look for on an itemized bill</h2>

<p>Once you have your itemized bill with CPT codes, these are the five most common errors to check for. Each one can add hundreds or thousands of dollars to your bill. For a comprehensive breakdown of all seven major error types, see our <a href="/guides/common-hospital-billing-errors">guide to common hospital billing errors</a>.</p>

<h3>Red flag 1: Duplicate charges</h3>

<p><strong>What to look for:</strong> The same CPT code appearing twice (or more) on the same date of service. This is the easiest error to spot and the most common. Sort your bill by date and CPT code&mdash;duplicates jump out immediately.</p>

<div class="case-study">
    <h3>Case study: Duplicate CBC on an ER bill</h3>
    <p>A patient in Ohio went to the ER for chest pain. Her itemized bill showed CPT 85025 (Complete Blood Count) billed twice on the same date&mdash;once at $182 and once at $178. She confirmed with the ER records that blood was drawn only once. She called billing, identified the duplicate by CPT code and date, and the second charge was removed. <strong>Savings: $178.</strong></p>
</div>

<h3>Red flag 2: Charges for services you didn&rsquo;t receive</h3>

<p><strong>What to look for:</strong> Line items for specialist consultations you don&rsquo;t remember, medications you weren&rsquo;t given, or supplies that don&rsquo;t match your treatment. These &ldquo;phantom charges&rdquo; are especially common on multi-day stays where billing systems accumulate charges automatically.</p>

<div class="case-study">
    <h3>Case study: Billed for a specialist who never showed</h3>
    <p>A patient hospitalized for pneumonia in Texas found a $580 cardiology consultation charge on his itemized bill. He had never seen a cardiologist during his stay. He requested the nursing notes and confirmed no cardiology visit was documented. The billing department removed the charge after a single phone call. <strong>Savings: $580.</strong></p>
</div>

<h3>Red flag 3: Inflated supply and medication costs</h3>

<p><strong>What to look for:</strong> Common over-the-counter medications billed at extreme markups. The most notorious examples: ibuprofen tablets billed at $30&ndash;$40 each, acetaminophen (Tylenol) at $25 per tablet, saline IV bags at $300&ndash;$800, and adhesive bandages at $50+. While some facility markup is expected, charges that exceed 10x the retail cost of common items are worth challenging.</p>

<div class="case-study">
    <h3>Case study: $40 ibuprofen and $600 saline bag</h3>
    <p>A patient in Georgia had a 2-day hospital stay for a minor procedure. Her itemized bill included 6 doses of ibuprofen 200mg at $38 each ($228 total) and 3 saline IV bags at $589 each ($1,767 total). A bottle of 200 ibuprofen tablets costs about $8 at a pharmacy. A saline IV bag costs a hospital approximately $1. She submitted a written dispute citing the retail prices and the hospital reduced the medication charges by 60%. <strong>Savings: $1,197.</strong></p>
</div>

<h3>Red flag 4: Operating room time billed in excess</h3>

<p><strong>What to look for:</strong> Operating room or anesthesia time that exceeds the actual duration of your procedure. OR time is billed in 15-minute increments, and each increment can cost $150&ndash;$400+. If your surgery took 45 minutes but the bill shows 90 minutes of OR time, you&rsquo;re paying double.</p>

<div class="case-study">
    <h3>Case study: 90 minutes billed for a 40-minute procedure</h3>
    <p>A patient had a laparoscopic appendectomy that, per the operative report, lasted 42 minutes. The itemized bill showed 6 units of OR time (90 minutes) at $320 per unit ($1,920 total). The actual time supported only 3 units ($960). The patient requested the operative report, compared the documented time to the billed time, and disputed the excess 3 units. The hospital corrected the bill. <strong>Savings: $960.</strong></p>
</div>

<p>Look up what Medicare pays for anesthesia and OR time for your procedure:</p>

{_embed(mode="cost", title="Check OR and anesthesia rates", subtitle="Enter the anesthesia CPT code from your bill.", height="380")}

<h3>Red flag 5: Upcoded evaluation codes</h3>

<p><strong>What to look for:</strong> ER visit levels or evaluation and management (E&amp;M) codes that seem too high for the care you received. ER visits are coded from Level 1 (CPT 99281, minor problem) through Level 5 (CPT 99285, life-threatening emergency). The cost difference between Level 3 and Level 5 can be <strong>$1,500&ndash;$3,000+</strong> at hospital chargemaster rates.</p>

<div class="case-study">
    <h3>Case study: Sprained ankle billed as Level 5 emergency</h3>
    <p>A patient in Florida went to the ER after twisting her ankle playing tennis. She received an X-ray (no fracture), an ice pack, an ACE bandage, and a prescription for ibuprofen. Total time in the ER: 2 hours. Her bill showed CPT 99285 (Level 5 ER visit) at $4,120. Level 5 is reserved for life-threatening emergencies requiring immediate intervention. She requested a coding review, citing that her visit involved low-complexity decision-making and no urgent interventions. The hospital downgraded to CPT 99283 (Level 3) and reduced the facility charge by $2,340. <strong>Savings: $2,340.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Want to check all five of these automatically?</strong> <a href="/scan">Upload your itemized bill to BillKarma</a> and we&rsquo;ll scan every line item for duplicates, phantom charges, inflated pricing, unbundling errors, and upcoding&mdash;then generate a dispute-ready report you can send to the hospital.
</div>

<h2 id="found-errors">6. What to do when you find errors</h2>

<p>Finding the error is half the battle. Here&rsquo;s the dispute process, step by step:</p>

<ol>
    <li><strong>Document every error.</strong> For each flagged line item, write down the CPT code, date of service, charged amount, and the specific reason it&rsquo;s wrong (duplicate, phantom, upcoded, inflated, etc.). Use the <a href="/calculator">BillKarma calculator</a> to look up the Medicare rate for each disputed code so you have a benchmark.</li>
    <li><strong>Call Patient Financial Services.</strong> Reference each error by CPT code and date. Be specific: &ldquo;CPT 85025 appears twice on 02/10/2026. I received one blood draw, not two. Please remove the duplicate.&rdquo; Simple errors like duplicates are often corrected on the spot.</li>
    <li><strong>Follow up in writing.</strong> Even if the phone call seems to resolve things, send a written dispute letter listing every error. This creates a paper trail. Send via the patient portal (timestamped) or certified mail.</li>
    <li><strong>Request a formal billing review.</strong> For complex errors like upcoding or inflated OR time, ask the hospital to conduct a formal coding review. Say: &ldquo;I am requesting a formal billing review of these specific charges.&rdquo; This triggers an internal audit process.</li>
    <li><strong>Do not pay the disputed amount.</strong> Pay the undisputed portion of your bill to show good faith, but request in writing that the disputed charges be placed on hold during the review. Most hospitals will not send disputed items to collections while a review is pending.</li>
    <li><strong>Follow up in 30 days.</strong> If you haven&rsquo;t received a corrected statement, call again and reference your original dispute date and any case numbers.</li>
</ol>

<p>For detailed dispute letter templates and phone scripts, see our <a href="/guides/how-to-dispute-a-medical-bill">complete guide to disputing a medical bill</a>.</p>

<p><strong>Already have your itemized bill?</strong> <a href="/scan">Upload it to BillKarma</a> for a free analysis. We&rsquo;ll compare every charge to Medicare rates, flag potential errors, and generate a personalized dispute letter automatically.</p>

<h2 id="hospital-refuses">7. What if the hospital refuses or delays</h2>

<p>Most hospitals comply with itemized bill requests without issue. But if yours doesn&rsquo;t, here is the escalation path, in order:</p>

<ol>
    <li><strong>Billing manager.</strong> If the front-line billing staff cannot or will not process your request, ask to speak with the billing department manager or supervisor. Reference your original request date and HIPAA right of access. Many requests stall simply because they were not routed to the right person.</li>
    <li><strong>Patient advocate or ombudsman.</strong> Every hospital has a patient advocate (sometimes called a patient representative or ombudsman). Their job is to resolve patient complaints. Ask the hospital operator to transfer you. Explain that you have requested an itemized bill, provide the dates of your requests, and ask them to expedite it.</li>
    <li><strong>HIPAA complaint with HHS Office for Civil Rights (OCR).</strong> If the hospital has not responded within 30 days (or 60 days with a written extension), they are in violation of HIPAA. File a complaint at <em>hhs.gov/ocr/complaints</em>. Hospitals take OCR complaints seriously because they carry financial penalties. In many cases, simply telling the hospital you intend to file an OCR complaint is enough to get a response.</li>
    <li><strong>State attorney general&rsquo;s consumer protection division.</strong> Your state AG&rsquo;s office handles complaints about unfair business practices, including hospitals that withhold billing records. File a complaint online through your state AG&rsquo;s website. AG complaints often trigger a response within 2&ndash;4 weeks.</li>
    <li><strong>CMS complaint.</strong> For hospitals that participate in Medicare (which is virtually all of them), you can file a complaint with the Centers for Medicare &amp; Medicaid Services. CMS can investigate billing practices and impose conditions on hospitals that fail to comply with federal transparency requirements.</li>
</ol>

<div class="key-takeaway">
    <strong>In practice, most patients never need to go past step 2.</strong> A polite but firm request that references HIPAA and includes specific dates of prior requests is usually sufficient. Hospitals know the rules&mdash;they just need to know that you do too.
</div>

<p>Once you finally have your itemized bill in hand, <a href="/scan">run it through BillKarma&rsquo;s scanner</a> to instantly identify every overcharge, duplicate, and coding error&mdash;and get a dispute letter you can send the same day.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Is a hospital legally required to give me an itemized bill?</h3>
        <p>Yes. Under HIPAA Section 164.524, you have the right to access your protected health information, which includes billing records. The No Surprises Act reinforces your right to detailed billing information. Most state consumer protection laws also require hospitals to provide itemized statements upon request. If a hospital refuses, you can file a complaint with the HHS Office for Civil Rights or your state attorney general.</p>
    </div>

    <div class="faq-item">
        <h3>How long does it take to get an itemized bill?</h3>
        <p>By law, hospitals must respond within 30 days (with one possible 30-day extension if they notify you in writing). In practice, most hospitals provide an itemized bill within 5&ndash;15 business days. If you request it through the patient portal, it may arrive faster. If 30 days pass without a response, follow up in writing and reference your HIPAA right of access.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between a summary bill and an itemized bill?</h3>
        <p>A summary bill groups charges into broad categories like Room and Board, Laboratory, and Pharmacy, showing only totals for each category. An itemized bill breaks down every individual charge with its CPT or HCPCS code, description, quantity, unit price, and total. The itemized version is the only one that lets you verify what you are actually being charged for and catch errors like duplicates, upcoding, and unbundling.</p>
    </div>

    <div class="faq-item">
        <h3>Does requesting an itemized bill cost anything?</h3>
        <p>Hospitals can charge a reasonable, cost-based fee for copies of medical records under HIPAA, but many hospitals provide itemized billing statements at no charge. If you are asked to pay, the fee should be minimal&mdash;typically under $25. Some states cap the amount hospitals can charge for medical records.</p>
    </div>

    <div class="faq-item">
        <h3>Can I get an itemized bill after I have already paid?</h3>
        <p>Yes. Your right to an itemized statement does not expire when you pay the bill. You can request one at any time. If you discover errors after paying, you can still dispute the charges and request a refund. There is no deadline for requesting an itemized bill, though disputing errors is easier the sooner you act.</p>
    </div>

    <div class="faq-item">
        <h3>What if my itemized bill does not include CPT codes?</h3>
        <p>Call the billing department and specifically ask for a statement that includes CPT or HCPCS codes for every line item. Without the codes, you cannot look up Medicare rates or check for unbundling errors. You are entitled to the codes&mdash;they are part of your billing record under HIPAA.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/access/index.html" target="_blank" rel="noopener">HHS: HIPAA Right of Access (45 CFR &sect;164.524)</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Patient Billing Protections</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS: Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.hhs.gov/ocr/complaints/index.html" target="_blank" rel="noopener">HHS Office for Civil Rights: Filing a HIPAA Complaint</a></li>
    <li><a href="https://www.consumerfinance.gov/ask-cfpb/can-i-dispute-a-medical-bill-en-2125/" target="_blank" rel="noopener">CFPB: Disputing Medical Bills &mdash; Consumer Rights</a></li>
    <li><a href="https://www.naag.org/find-my-ag/" target="_blank" rel="noopener">National Association of Attorneys General: Find Your State AG</a></li>
</ul>
""",
})
