"""Guide: hospital revenue codes on an itemized bill."""

from guides import register, _embed

register("hospital-revenue-codes-explained", {
    "title": "Hospital Revenue Codes: How to Read Your Itemized Bill",
    "meta_description": "The 4-digit revenue code on a hospital bill names the department that charged you. What 0450, 0250, 0360 and 0636 mean and which lines to question.",
    "published": "2026-11-11",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What is a revenue code on a hospital bill?",
            "a": "A four-digit code that tells the payer which hospital department or type of service a charge belongs to, such as 0450 for the emergency room or 0250 for pharmacy. Hospitals report it on the UB-04 claim form.",
        },
        {
            "q": "What is the difference between a revenue code and a CPT code?",
            "a": "A revenue code says where in the hospital a charge came from. A CPT or HCPCS code says exactly what service or item it was. A line often has both, and the CPT or HCPCS code is what you compare against Medicare rates.",
        },
        {
            "q": "What does revenue code 0636 mean?",
            "a": "Drugs requiring detailed coding. These are drugs that must be reported with a specific HCPCS code and a number of units, so a 0636 line should show both.",
        },
        {
            "q": "Why do I see room and board charges on a short stay?",
            "a": "Room and board codes (the 011x and 012x families) bill by day. If the number of days doesn't match the nights you stayed, ask billing to explain, since observation and outpatient stays are billed differently.",
        },
        {
            "q": "Can a revenue code be wrong?",
            "a": "Yes. A charge can be assigned to the wrong department or described by a code that doesn't match the service. Ask billing to explain any line whose revenue code and description don't fit what you received.",
        },
    ],
    "body": f"""
<p class="lead">The four-digit number next to each charge on an itemized hospital bill is a <strong>revenue code</strong>. It tells the payer which department the charge came from. It doesn't say what the service was; the CPT or HCPCS code does that. Reading both on each line is the quickest way to find charges that don't match your care.</p>

<p>Hospitals report revenue codes in fields 42 to 49 of the UB-04, the standard claim form for hospitals (physician offices use a different form, the CMS-1500). The National Uniform Billing Committee maintains the code list, so the same code means the same department at every hospital.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#codes">The revenue codes you'll see most</a></li>
        <li><a href="#vs-cpt">Revenue code vs CPT code</a></li>
        <li><a href="#example">Reading a real-looking bill</a></li>
        <li><a href="#red-flags">What to question</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="codes">1. The revenue codes you'll see most</h2>

<table>
    <thead>
        <tr><th>Code</th><th>Department</th><th>What it usually covers</th></tr>
    </thead>
    <tbody>
        <tr><td class="bk-num">011x, 012x</td><td>Room and board</td><td>Daily charge for a hospital bed</td></tr>
        <tr><td class="bk-num">020x</td><td>Intensive care</td><td>ICU days</td></tr>
        <tr><td class="bk-num">0250</td><td>Pharmacy</td><td>Drugs and supplies given during the visit</td></tr>
        <tr><td class="bk-num">0260</td><td>IV therapy</td><td>IV solutions and administration</td></tr>
        <tr><td class="bk-num">0270</td><td>Medical and surgical supplies</td><td>Dressings, devices, kits</td></tr>
        <tr><td class="bk-num">0300</td><td>Laboratory</td><td>Blood and other lab tests</td></tr>
        <tr><td class="bk-num">0320</td><td>Radiology, diagnostic</td><td>X-rays</td></tr>
        <tr><td class="bk-num">0360</td><td>Operating room</td><td>Use of the operating room</td></tr>
        <tr><td class="bk-num">0370</td><td>Anesthesia</td><td>Anesthesia services and supplies</td></tr>
        <tr><td class="bk-num">0450</td><td>Emergency room</td><td>The facility charge for an ER visit</td></tr>
        <tr><td class="bk-num">0636</td><td>Drugs requiring detailed coding</td><td>Drugs billed with a specific HCPCS code and units</td></tr>
        <tr><td class="bk-num">0710</td><td>Recovery room</td><td>Time in recovery after a procedure</td></tr>
        <tr><td class="bk-num">0730</td><td>EKG</td><td>Heart tracing</td></tr>
    </tbody>
</table>

<p>Codes ending in <em>x</em> are families. For example, 0450 is the general emergency room code, 0451 covers the federally required emergency screening and 0456 is urgent care. Your hospital's bill may show the family code or a more specific one.</p>

<h2 id="vs-cpt">2. Revenue code vs CPT code</h2>

<p>The revenue code answers <em>where</em>. The CPT or HCPCS code answers <em>what</em>. A chest X-ray might appear as revenue code 0320 (radiology) with CPT 71046 (the X-ray itself). It's the CPT or HCPCS code you can look up and compare with what Medicare pays. A line with a revenue code and no CPT code can't be checked that way, which is why the bill should show both. If yours doesn't, ask for a version that does; see <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a>.</p>

{_embed(mode="markup", title="How far above Medicare is your charge?", subtitle="Enter a billing code and the amount charged.", height="420")}

<h2 id="example">3. Reading a real-looking bill</h2>

<p>This is an illustrative emergency bill. Amounts are made up to show the layout.</p>

<table>
    <thead>
        <tr><th>Rev code</th><th>Description</th><th>CPT/HCPCS</th><th>Units</th><th>Charged</th></tr>
    </thead>
    <tbody>
        <tr><td class="bk-num">0450</td><td>Emergency room</td><td class="bk-num">99284</td><td class="bk-num">1</td><td class="bk-num">$3,200</td></tr>
        <tr><td class="bk-num">0320</td><td>Radiology</td><td class="bk-num">71046</td><td class="bk-num">1</td><td class="bk-num">$850</td></tr>
        <tr><td class="bk-num">0300</td><td>Laboratory</td><td class="bk-num">80053</td><td class="bk-num">1</td><td class="bk-num">$350</td></tr>
        <tr><td class="bk-num">0250</td><td>Pharmacy</td><td></td><td class="bk-num">6</td><td class="bk-num">$310</td></tr>
        <tr><td class="bk-num">0636</td><td>Drugs, detailed coding</td><td class="bk-num">J1885</td><td class="bk-num">2</td><td class="bk-num">$164</td></tr>
    </tbody>
</table>

<p>Read each row left to right. The 0450 line is the ER facility charge at level 4. The 0320 and 0300 lines are an X-ray and a lab panel, each with a CPT code you can check. The 0250 pharmacy line has six units and no CPT code, so you can't tell what the six items were. The 0636 line has a HCPCS code and two units, which is the form that line should take.</p>

<div class="key-takeaway">
    <strong>Spot the lines you can't check.</strong> Upload your bill and <a href="/scan">BillKarma will compare every line that has a billing code</a> with Medicare's rate for it, and show you which lines have none.
</div>

<h2 id="red-flags">4. What to question</h2>

<ul>
    <li><strong>Pharmacy lines with no detail.</strong> A lump "pharmacy" or "supplies" charge with no code or unit breakdown. Ask for the drug-by-drug list.</li>
    <li><strong>Units that don't add up.</strong> Six units of a drug when you received one dose; ten days of room and board for a two-night stay.</li>
    <li><strong>Room and board on an outpatient visit.</strong> If you were in observation, you weren't admitted, and the bill should show observation charges, not a standard inpatient day. See <a href="/guides/observation-status-billing/">observation status billing</a>.</li>
    <li><strong>Two lines for one service.</strong> The same CPT code under two revenue codes, or a pair of codes that overlap. Our guide to <a href="/guides/upcoding-unbundling-hospital-bills/">upcoding and unbundling</a> covers the usual pairs.</li>
    <li><strong>A department you didn't visit.</strong> A recovery room charge after an exam, or an operating room charge for a bedside procedure.</li>
</ul>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is a revenue code on a hospital bill?</h3>
        <p>A four-digit code that tells the payer which hospital department or type of service a charge belongs to, such as 0450 for the emergency room or 0250 for pharmacy. Hospitals report it on the UB-04 claim form.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between a revenue code and a CPT code?</h3>
        <p>A revenue code says where in the hospital a charge came from. A CPT or HCPCS code says exactly what service or item it was. A line often has both, and the CPT or HCPCS code is what you compare against Medicare rates.</p>
    </div>
    <div class="faq-item">
        <h3>What does revenue code 0636 mean?</h3>
        <p>Drugs requiring detailed coding. These are drugs that must be reported with a specific HCPCS code and a number of units, so a 0636 line should show both.</p>
    </div>
    <div class="faq-item">
        <h3>Why do I see room and board charges on a short stay?</h3>
        <p>Room and board codes bill by day. If the number of days doesn't match the nights you stayed, ask billing to explain, since observation and outpatient stays are billed differently.</p>
    </div>
    <div class="faq-item">
        <h3>Can a revenue code be wrong?</h3>
        <p>Yes. A charge can be assigned to the wrong department or described by a code that doesn't match the service. Ask billing to explain any line whose revenue code and description don't fit what you received.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/Outreach-and-Education/MLN/WBT/MLN7388180-MLN-WBT-1450/1450/lesson05/13/index.html" target="_blank" rel="noopener">CMS Medicare Learning Network: Form CMS-1450 revenue codes (0450 emergency room, 0636 drugs requiring detailed coding)</a></li>
    <li><a href="https://www.findacode.com/ub04-revenue/ub04-revenue-cms-1450-codes-04-group.html" target="_blank" rel="noopener">FindACode: UB-04 revenue codes, 045x emergency room family</a></li>
    <li><a href="https://www.findacode.com/ub04-revenue/ub04-revenue-cms-1450-codes-06-group.html" target="_blank" rel="noopener">FindACode: UB-04 revenue codes, 063x pharmacy extension</a></li>
    <li><a href="https://etactics.com/blog/what-is-a-revenue-code" target="_blank" rel="noopener">Etactics: what a revenue code is; UB-04 fields 42&ndash;49</a></li>
    <li><a href="https://hcpf.colorado.gov/sites/hcpf/files/Billing%20101%20-%20Glossary%20of%20Billing%20Terms.pdf" target="_blank" rel="noopener">Colorado Health Care Policy and Financing: billing glossary, revenue codes</a></li>
</ul>
""",
})
