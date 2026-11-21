"""Guide: Anatomy of an ER Bill: Every Line on a Sample Statement."""

from guides import register

register("anatomy-of-an-er-bill", {
    "title": "Anatomy of an ER Bill: Every Line on a Sample Statement",
    "meta_description": "Walk through a sample ER bill line by line: revenue codes, the visit level, labs, X-ray, drugs, supplies, and why the ER doctor bills you separately.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "What do the 4-digit numbers on my ER bill mean?",
            "a": "They are revenue codes. Each one names the hospital department that charged you. CMS says hospitals enter a revenue code next to every charge, and the 045X family is the emergency room. 030X is the lab, 032X is diagnostic radiology (X-rays), 025X is the pharmacy, 026X is IV therapy and 027X is medical and surgical supplies.",
        },
        {
            "q": "Why do I have two bills for one ER visit?",
            "a": "The hospital bills for its staff, rooms, equipment, tests and supplies. The emergency doctor bills for their own work. CMS billing rules say the physician part is billed separately to Medicare Part B, and Medicare.gov says you pay for the hospital services and, separately, 20% of the approved amount for your doctor's services after the Part B deductible.",
        },
        {
            "q": "Is it a duplicate charge if 99284 appears on both bills?",
            "a": "Not by itself. The hospital uses the ER visit code to bill for its resources, and the doctor uses it to bill for their own care. CMS lets each hospital set its own internal guidelines for picking the facility level, while the doctor's level is based on medical decision making. A duplicate would be the same code twice on the same bill for the same visit.",
        },
        {
            "q": "What is revenue code 0001 on a hospital bill?",
            "a": "It is the total line. CMS says there is no fixed total line on the hospital claim form, so the hospital enters revenue code 0001 and puts the sum of all charges next to it.",
        },
    ],
    "body": f"""
<p class="lead">An ER bill is a list of departments, each with its own code and charge: the emergency room itself, the lab, X-ray, pharmacy, IV therapy and supplies. Below is a labeled <strong>sample</strong> hospital statement with every line explained, followed by a sample bill from the ER doctor, so you can read your own bill with confidence and spot what to question.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#sample-statement">The sample ER statement</a></li>
        <li><a href="#line-by-line">Line by line: what each charge means</a></li>
        <li><a href="#bottom-lines">The bottom lines: total, payments, balance</a></li>
        <li><a href="#doctor-bill">The second bill: the ER doctor</a></li>
        <li><a href="#what-to-do">What to do with your own ER bill</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="sample-statement">1. The sample ER statement</h2>

<p>This is a made-up, itemized hospital (facility) statement for one ER visit. The hospital, the patient and every dollar amount are sample data. The charges are not benchmarks or typical prices. They are here so the arithmetic is easy to follow.</p>

<p>Your real bill may look shorter, such as a summary with a few totals. If yours lists only a total, ask for an itemized bill (see our guide on <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a>).</p>

<table>
    <caption><strong>Sample</strong> &mdash; Itemized ER facility statement (not a real bill). Date of service: 11/02/2026.</caption>
    <thead>
        <tr>
            <th>#</th>
            <th>Rev. code</th>
            <th>Description</th>
            <th>CPT/HCPCS</th>
            <th>Units</th>
            <th>Charge</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>1</td><td>0250</td><td>Pharmacy &ndash; general</td><td>&mdash;</td><td>3</td><td>$54.00</td></tr>
        <tr><td>2</td><td>0260</td><td>IV therapy &ndash; general</td><td>96374</td><td>1</td><td>$386.00</td></tr>
        <tr><td>3</td><td>0270</td><td>Med/surg supplies &ndash; general</td><td>&mdash;</td><td>1</td><td>$139.00</td></tr>
        <tr><td>4</td><td>0300</td><td>Laboratory &ndash; general</td><td>80053</td><td>1</td><td>$248.00</td></tr>
        <tr><td>5</td><td>0300</td><td>Laboratory &ndash; general</td><td>85025</td><td>1</td><td>$96.00</td></tr>
        <tr><td>6</td><td>0320</td><td>Radiology diagnostic &ndash; general</td><td>71046</td><td>1</td><td>$412.00</td></tr>
        <tr><td>7</td><td>0450</td><td>Emergency room &ndash; general</td><td>99284</td><td>1</td><td>$2,140.00</td></tr>
        <tr><td>8</td><td>0636</td><td>Drugs requiring detailed coding</td><td>J3360</td><td>1</td><td>$68.00</td></tr>
        <tr><td></td><td>0001</td><td><strong>Total charges</strong></td><td></td><td></td><td><strong>$3,543.00</strong></td></tr>
        <tr><td></td><td></td><td>Insurance payment</td><td></td><td></td><td>&minus;$1,180.00</td></tr>
        <tr><td></td><td></td><td>Insurance contractual adjustment</td><td></td><td></td><td>&minus;$1,713.00</td></tr>
        <tr><td></td><td></td><td><strong>Patient balance</strong></td><td></td><td></td><td><strong>$650.00</strong></td></tr>
    </tbody>
</table>

<p>Check the math: $54 + $386 + $139 + $248 + $96 + $412 + $2,140 + $68 = $3,543. Then $3,543 &minus; $1,180 &minus; $1,713 = $650.</p>

<p>Two quick terms. A <strong>revenue code</strong> is a 4-digit number that names the hospital department behind a charge. A <strong>CPT or HCPCS code</strong> (the standard billing code for a medical service, drug or item) says exactly what was done. For a deeper look at the first one, see <a href="/guides/hospital-revenue-codes-explained/">hospital revenue codes explained</a>.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Every line on an ER bill should have a department (revenue code), and most should have a service code (CPT or HCPCS). Those codes are what let you, or a tool, check each charge. <a href="/scan">Check your ER bill free</a> to compare each code against what Medicare pays.</p>
</div>

<h2 id="line-by-line">2. Line by line: what each charge means</h2>

<p>Each callout matches the # column in the sample. CMS asks hospitals to list revenue codes in ascending order, which is why the ER visit, the biggest charge, sits near the bottom.</p>

<h3>Callout 1: Pharmacy, revenue code 0250</h3>
<p><strong>What it is:</strong> Drugs from the hospital pharmacy. Revenue code 025X is the pharmacy family.</p>
<p><strong>What&rsquo;s normal:</strong> A 0250 line often has no drug code next to it, so you can&rsquo;t tell what you got from the bill alone.</p>
<p><strong>What to question:</strong> Ask for the drug name, the dose and how many units. Our guide to <a href="/guides/hospital-drug-charges/">hospital drug charges</a> goes further.</p>

<h3>Callout 2: IV therapy, revenue code 0260 with CPT 96374</h3>
<p><strong>What it is:</strong> Giving a drug into a vein. CMS&rsquo;s coding manual groups 96374&ndash;96376 as &ldquo;IV push injection&rdquo; codes, and lists 96374 as an &ldquo;initial&rdquo; service code.</p>
<p><strong>What&rsquo;s normal:</strong> Under Medicare&rsquo;s outpatient billing rules, only one initial drug administration is reported per vascular access site per encounter. Putting in the IV line itself (for example, CPT 36000 or 36410) is not reported separately when it is used for an IV injection.</p>
<p><strong>What to question:</strong> Two &ldquo;initial&rdquo; IV codes when you had one IV line, or a separate charge for starting the IV. See <a href="/guides/upcoding-unbundling-hospital-bills/">upcoding and unbundling</a> for how bundled charges work, and <a href="/guides/iv-infusion-charges-er-bill/">IV infusion charges on an ER bill</a> for the time rules.</p>

<h3>Callout 3: Supplies, revenue code 0270</h3>
<p><strong>What it is:</strong> Medical and surgical supplies (027X).</p>
<p><strong>What&rsquo;s normal:</strong> Under Medicare&rsquo;s outpatient payment system, routine supplies are &ldquo;packaged.&rdquo; That means Medicare treats them as part of the main service and doesn&rsquo;t pay extra for them. The national correct coding rules (NCCI) also list surgical supplies as part of the procedure, except where CMS policy allows separate payment. A hospital may still list a supply charge on your statement.</p>
<p><strong>What to question:</strong> A large, vague supply line. Ask what the supplies were and why they aren&rsquo;t part of the visit or procedure.</p>

<h3>Callouts 4 and 5: Lab, revenue code 0300 with CPT 80053 and 85025</h3>
<p><strong>What it is:</strong> Blood tests. Revenue codes 0300&ndash;0319 are the lab. In CMS&rsquo;s list of shoppable services, 80053 is a &ldquo;comprehensive group of blood chemicals&rdquo; (a comprehensive metabolic panel) and 85025 is a complete blood count with an automated differential white cell count.</p>
<p><strong>What&rsquo;s normal:</strong> One unit each, as in the sample.</p>
<p><strong>What to question:</strong> The same test code twice on the same day without a reason, or separate lines for single tests that sound like they belong to the panel. Ask the billing office to explain any repeat. More in <a href="/guides/why-lab-test-bills-are-so-high/">why lab test bills are so high</a>.</p>

<h3>Callout 6: X-ray, revenue code 0320 with CPT 71046</h3>
<p><strong>What it is:</strong> Diagnostic radiology (032X). In Medicare&rsquo;s code list, 71046 is a chest X-ray with 2 views. Its siblings are 71045 (1 view), 71047 (3 views) and 71048 (4 or more views).</p>
<p><strong>What&rsquo;s normal:</strong> One chest X-ray code that matches the number of views taken.</p>
<p><strong>What to question:</strong> More views billed than you remember, or two chest X-ray codes for one session. Note the hospital bills the X-ray itself. A radiologist who read it may bill you separately.</p>


<h3>Callout 7: The ER visit, revenue code 0450 with CPT 99284</h3>
<p><strong>What it is:</strong> The hospital&rsquo;s charge for the ER visit itself. CMS says ER services are reported under the 045X revenue code. 99284 is level 4 of 5 ER visit levels (99281&ndash;99285).</p>
<p><strong>What&rsquo;s normal:</strong> For the hospital&rsquo;s charge, CMS tells hospitals to apply their own internal guidelines to choose the level. Those guidelines should &ldquo;reasonably relate the intensity of hospital resources&rdquo; to each level.</p>
<p><strong>What to question:</strong> Whether the level fits what happened. Ask the hospital what its guidelines say for the level billed. If your bill shows level 5, read <a href="/guides/er-level-5-charge-99285/">the ER level 5 charge (99285)</a>.</p>
<p>One more detail: CMS says the ER visit line carries the date you arrived, even if you stayed past midnight. Other services, like labs and imaging, carry the date they were done. So different dates on one ER bill can be normal.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>The most useful question on any line is &ldquo;how many, and was it really separate?&rdquo; Units, repeats and charges for things that are part of another service are worth checking. Our guide to <a href="/guides/duplicate-charges-hospital-bills/">duplicate charges on hospital bills</a> shows how to spot them.</p>
</div>

<h3>Callout 8: Drug with a code, revenue code 0636 with HCPCS J3360</h3>
<p><strong>What it is:</strong> 063X is an extension of the pharmacy codes, and 0636 means &ldquo;drugs requiring detailed coding.&rdquo; CMS uses J3360 as an example code: injection, diazepam, up to 5 mg.</p>
<p><strong>What&rsquo;s normal:</strong> CMS says drug units are billed in multiples of the dose in the code&rsquo;s description. For example, if the code is 50 mg and you got 200 mg, that&rsquo;s 4 units.</p>
<p><strong>What to question:</strong> Units that don&rsquo;t match the dose in your records. Ask for the dose given and do the division yourself.</p>

<h2 id="bottom-lines">3. The bottom lines: total, payments, balance</h2>

<p><strong>Revenue code 0001.</strong> CMS says there is no fixed &ldquo;total&rdquo; line on the hospital claim form. The hospital enters revenue code 0001 and puts the sum of all charges next to it. On the sample, that&rsquo;s $3,543.00.</p>

<p><strong>Insurance payment and adjustment.</strong> The payment is what the plan paid. The contractual adjustment is the amount written off under the hospital&rsquo;s contract with your plan.</p>

<p><strong>Patient balance.</strong> This is what the hospital says you owe. If you have insurance, compare it with your explanation of benefits (EOB). CMS says an EOB &ldquo;isn&rsquo;t a bill,&rdquo; and your bill should not be higher than the patient balance on the EOB. If it is, talk to the provider. Our <a href="/guides/explanation-of-benefits-eob/">EOB guide</a> shows where to look.</p>

<h2 id="doctor-bill">4. The second bill: the ER doctor</h2>

<p>You may get another bill for the same visit, often from a physician group rather than the hospital.</p>

<table>
    <caption><strong>Sample</strong> &mdash; ER physician bill (not a real bill). Date of service: 11/02/2026.</caption>
    <thead>
        <tr>
            <th>Description</th>
            <th>CPT</th>
            <th>Units</th>
            <th>Charge</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Emergency department visit, moderate medical decision making</td><td>99284</td><td>1</td><td>$615.00</td></tr>
        <tr><td>Insurance payment</td><td></td><td></td><td>&minus;$310.00</td></tr>
        <tr><td>Insurance contractual adjustment</td><td></td><td></td><td>&minus;$205.00</td></tr>
        <tr><td><strong>Patient balance</strong></td><td></td><td></td><td><strong>$100.00</strong></td></tr>
    </tbody>
</table>

<p>Check the math: $615 &minus; $310 &minus; $205 = $100.</p>

<p><strong>Why two bills?</strong> The hospital bills for its rooms, nurses, equipment, tests and supplies. The doctor bills for their own medical work. CMS&rsquo;s billing manual says the physician part must be billed to the Medicare Part B contractor, separate from the hospital&rsquo;s claim. Medicare.gov describes the same split for patients: you pay a copayment for the ER visit and for each hospital service, and, after the Part B deductible, 20% of the Medicare-approved amount for your doctor&rsquo;s services.</p>

<p><strong>Why 99284 shows up twice.</strong> It is not a duplicate. The same code describes two different things. On the hospital bill, the level comes from the hospital&rsquo;s internal guidelines. On the doctor&rsquo;s bill, the AMA&rsquo;s CPT rules (since 2023) base the ER level on medical decision making. For 99284, that&rsquo;s a &ldquo;moderate level&rdquo; of decision making. Time does not set the level for ER visits. Because the two use different yardsticks, the two levels can differ.</p>

<p><strong>Other bills.</strong> A radiologist or other specialist may bill separately too. See <a href="/guides/multiple-bills-one-hospital-visit/">multiple bills from one hospital visit</a> to match each bill to the visit. If any of them is out of network, CMS says the No Surprises Act protects you from unexpected bills in most emergency situations, and you only have to pay your copay or coinsurance and deductible. See <a href="/guides/out-of-network-emergency-room-bill/">out-of-network ER bills</a>.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Two bills for one ER visit is normal: one from the hospital, one from the doctor. Match each to its own EOB, and question only true repeats on the same bill. When the bills are in hand, <a href="/scan">upload them for a free line-by-line check</a>.</p>
</div>

<h2 id="what-to-do">5. What to do with your own ER bill</h2>

<ol>
    <li><strong>Get the itemized bill.</strong> CMS&rsquo;s checklist starts here: ask billing for a detailed bill.</li>
    <li><strong>Wait for your EOB if insured.</strong> Each bill should not be higher than its EOB&rsquo;s patient balance.</li>
    <li><strong>Label each line.</strong> Write the department next to each revenue code (0450 ER, 030X lab, 032X X-ray, 025X/063X pharmacy, 026X IV therapy, 027X supplies).</li>
    <li><strong>Ask for your medical records.</strong> CMS says you shouldn&rsquo;t get a bill for anything that isn&rsquo;t documented in your records. Compare the tests, drugs and doses.</li>
    <li><strong>Check counts and repeats.</strong> Drug units, extra initial IV codes, an IV-start charge, repeated tests.</li>
    <li><strong>Ask about the visit level.</strong> Ask the hospital what its internal guidelines require for the level it billed.</li>
    <li><strong>Put questions in writing.</strong> List each line and ask for a written answer. Our <a href="/guides/medical-bill-dispute-letter/">medical bill dispute letter</a> guide has a template.</li>
    <li><strong>Ask about financial assistance.</strong> Ask whether the hospital has a financial assistance (charity care) program and whether you qualify. See <a href="/guides/hospital-financial-assistance-charity-care/">hospital financial assistance</a>.</li>
    <li><strong>Get outside help if you&rsquo;re stuck.</strong> CMS points to state Consumer Assistance Programs and patient advocates. For surprise-billing problems, the No Surprises Help Desk is 1-800-985-3059. If a bill ends up in court, consider talking to a consumer attorney or legal aid.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What do the 4-digit numbers on my ER bill mean?</h3>
        <p>They are revenue codes. Each one names the hospital department that charged you. CMS says hospitals enter a revenue code next to every charge, and the 045X family is the emergency room. 030X is the lab, 032X is diagnostic radiology (X-rays), 025X is the pharmacy, 026X is IV therapy and 027X is medical and surgical supplies.</p>
    </div>
    <div class="faq-item">
        <h3>Why do I have two bills for one ER visit?</h3>
        <p>The hospital bills for its staff, rooms, equipment, tests and supplies. The emergency doctor bills for their own work. CMS billing rules say the physician part is billed separately to Medicare Part B, and Medicare.gov says you pay for the hospital services and, separately, 20% of the approved amount for your doctor&rsquo;s services after the Part B deductible.</p>
    </div>
    <div class="faq-item">
        <h3>Is it a duplicate charge if 99284 appears on both bills?</h3>
        <p>Not by itself. The hospital uses the ER visit code to bill for its resources, and the doctor uses it to bill for their own care. CMS lets each hospital set its own internal guidelines for picking the facility level, while the doctor&rsquo;s level is based on medical decision making. A duplicate would be the same code twice on the same bill for the same visit.</p>
    </div>
    <div class="faq-item">
        <h3>What is revenue code 0001 on a hospital bill?</h3>
        <p>It is the total line. CMS says there is no fixed total line on the hospital claim form, so the hospital enters revenue code 0001 and puts the sum of all charges next to it.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c25.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 25: Completing and Processing the Form CMS-1450 Data Set (FL 42&ndash;48)</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c04.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 4: Part B Hospital (OPPS), sections 10.4, 160, 180.6 and 230.2</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c17.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 17: Drugs and Biologicals</a></li>
    <li><a href="https://med.noridianmedicare.com/web/jea/topics/claim-submission/revenue-codes" target="_blank" rel="noopener">Noridian (Medicare Administrative Contractor) &mdash; Revenue Codes, JE Part A</a></li>
    <li><a href="https://www.cms.gov/files/document/01-chapter1-ncci-medicare-policy-manual-2026-final.pdf" target="_blank" rel="noopener">CMS &mdash; NCCI Policy Manual for Medicare Services, Chapter I: General Correct Coding Policies (rev. 1/1/2026)</a></li>
    <li><a href="https://www.cms.gov/files/document/11-chapter11a-ncci-medicare-policy-manual-2026-final.pdf" target="_blank" rel="noopener">CMS &mdash; NCCI Policy Manual for Medicare Services, Chapter XI: Medicine and E/M Services (rev. 1/1/2026)</a></li>
    <li><a href="https://www.ama-assn.org/system/files/2023-e-m-descriptors-guidelines.pdf" target="_blank" rel="noopener">American Medical Association &mdash; CPT Evaluation and Management (E/M) Code and Guideline Changes, 2023</a></li>
    <li><a href="https://www.cms.gov/files/document/steps-making-public-standard-charges-shoppable-services.pdf" target="_blank" rel="noopener">CMS &mdash; 10 Steps to Making Public Standard Charges for Shoppable Services</a></li>
    <li><a href="https://www.govinfo.gov/content/pkg/FR-2017-11-15/html/2017-23953.htm" target="_blank" rel="noopener">Federal Register &mdash; CY 2018 Medicare Physician Fee Schedule Final Rule (82 FR 52976), new chest X-ray codes 71045&ndash;71048</a></li>
    <li><a href="https://www.medicare.gov/coverage/emergency-department-services" target="_blank" rel="noopener">Medicare.gov &mdash; Emergency department services</a></li>
    <li><a href="https://www.cms.gov/medical-bill-rights/help/guides/explanation-of-benefits" target="_blank" rel="noopener">CMS &mdash; How to read a health insurance explanation of benefits</a></li>
    <li><a href="https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/medical-bill-guides-resources/check-your-medical-bill-errors" target="_blank" rel="noopener">CMS &mdash; Check your medical bill for errors</a></li>
    <li><a href="https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/find-action-plan-your-medical-bill/action-plan-surprise-bill-emergency-room-visit" target="_blank" rel="noopener">CMS &mdash; Action plan: Surprise bill for emergency room visit</a></li>
</ul>
""",
})
