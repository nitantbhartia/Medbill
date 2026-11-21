"""Guide: Two Bills for One X-Ray or CT Scan? Here's Why."""

from guides import register

register("two-charges-one-xray-scan", {
    "title": "Two Bills for One X-Ray or CT Scan? Here’s Why",
    "meta_description": "Two bills for one X-ray, CT or MRI are usually the scan (technical part) and the radiologist’s read (modifier 26). Here’s how to spot a real duplicate.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "Why did I get two bills for one X-ray or CT scan?",
            "a": "Imaging is usually split into two parts. The technical component is the equipment, the room and the technologist who takes the images. The professional component is the radiologist’s reading of the images and written report. When you have the scan at a hospital, the hospital bills the technical part and the radiologist (or their group) bills the reading separately, often marked with modifier 26. Two bills for those two parts is normal.",
        },
        {
            "q": "What does modifier 26 mean on a radiology bill?",
            "a": "Modifier 26 is a two-character add-on to a CPT code that means the bill covers only the professional component, the doctor’s interpretation and report. Modifier TC means only the technical component. A code with no modifier, billed by one practice or imaging center that did both parts, is called a global charge and covers everything.",
        },
        {
            "q": "How can I tell if a radiology charge is a real duplicate?",
            "a": "Line up both bills by date of service and CPT code. Questions worth asking: the same technical charge appears twice on the hospital bill; one bill has a global charge (no modifier) while another bill also charges for the scan or the read; or the same reading is billed twice. Ask for itemized bills from both providers and ask the billing office to explain any line that overlaps.",
        },
        {
            "q": "Is the radiologist allowed to bill me out-of-network if the hospital was in-network?",
            "a": "If you have a private or job-based health plan, the No Surprises Act generally limits what an out-of-network radiologist can charge you for care related to a visit at an in-network hospital, hospital outpatient department or ambulatory surgical center: no more than your in-network cost sharing. Radiology is listed as an ancillary service, so the radiologist cannot ask you to sign away this protection. These rules do not cover people whose only coverage is Medicare, Medicaid, TRICARE, VA care or Indian Health Service, which have their own protections.",
        },
        {
            "q": "Who do I call if I think a radiology bill breaks the No Surprises Act?",
            "a": "Start with the radiology group’s billing office and your insurer. You can also call the federal No Surprises Help Desk at 1-800-985-3059 with questions or to submit a complaint. For legal questions, consider talking to a consumer attorney or legal aid.",
        },
    ],
    "body": f"""
<p class="lead">If you got one bill from the hospital and a second bill from a radiologist for the same X-ray, CT scan or MRI, that is usually not double billing. Imaging is split into two parts: the hospital bills for taking the images, and the radiologist bills for reading them. Here is how to tell a normal split from a real duplicate.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#two-parts">The two parts of every imaging test</a></li>
        <li><a href="#who-bills-what">Who bills what: a quick table</a></li>
        <li><a href="#read-the-bills">How to read each bill</a></li>
        <li><a href="#real-duplicates">When it really is a duplicate</a></li>
        <li><a href="#example">Example: comparing two bills line by line</a></li>
        <li><a href="#what-to-do">What to do, step by step</a></li>
        <li><a href="#no-surprises">Out-of-network radiologist? The No Surprises Act</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="two-parts">1. The two parts of every imaging test</h2>

<p>Many imaging tests have two pieces of work, each billable on its own:</p>

<ul>
    <li><strong>The technical component (TC).</strong> This is the scan itself: the machine, the room, the supplies and the technologist who positions you and takes the images.</li>
    <li><strong>The professional component (PC).</strong> This is the doctor&rsquo;s work: a radiologist looks at the images and writes a report for your medical record. Medicare&rsquo;s billing manual says the interpretation of a diagnostic test includes a written report.</li>
</ul>

<p>Billers mark which part they are charging for with a <strong>modifier</strong> (a two-character add-on to the CPT code, the standard billing code for a medical service):</p>

<ul>
    <li><strong>Modifier 26</strong> means &ldquo;professional component only&rdquo; &mdash; just the read and report.</li>
    <li><strong>Modifier TC</strong> means &ldquo;technical component only&rdquo; &mdash; just the scan.</li>
    <li><strong>No modifier</strong> on a code that can be split usually means a <strong>global</strong> charge &mdash; both parts in one line.</li>
</ul>

<p>Medicare&rsquo;s rules say a provider can bill globally only when the same physician or supplier entity furnishes both parts (and both are done in the same Medicare payment area). When different parties do the two parts, the reading doctor bills the interpretation separately with modifier 26. That is why you can end up with two bills for one test. More on codes: <a href="/guides/what-are-cpt-codes/">what CPT codes are</a>.</p>

<h2 id="who-bills-what">2. Who bills what: a quick table</h2>

<p>Where you had the scan decides how many bills you are likely to see.</p>

<table>
    <thead>
        <tr>
            <th>Where you had the scan</th>
            <th>Technical part (the scan)</th>
            <th>Professional part (the read)</th>
            <th>How many bills to expect</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Hospital outpatient department or ER</td>
            <td>Hospital, on its facility bill (UB-04 form) under an imaging revenue code</td>
            <td>Radiologist or radiology group, CPT code with modifier 26</td>
            <td>Usually two</td>
        </tr>
        <tr>
            <td>Hospital inpatient stay</td>
            <td>Hospital (for Medicare, included in the hospital&rsquo;s stay payment)</td>
            <td>Radiologist, modifier 26</td>
            <td>Usually two</td>
        </tr>
        <tr>
            <td>Freestanding imaging center or doctor&rsquo;s office that also reads the images</td>
            <td colspan="2">One global charge, CPT code with no modifier</td>
            <td>Usually one</td>
        </tr>
        <tr>
            <td>Freestanding center that sends images to an outside radiologist</td>
            <td>Imaging center, modifier TC</td>
            <td>Outside radiologist, modifier 26</td>
            <td>Usually two</td>
        </tr>
    </tbody>
</table>

<p>Medicare&rsquo;s manual uses this exact case as an example: an MRI at a hospital outpatient campus, with the hospital claiming the technical part and the physician billing the read. If you have more than two bills from one visit, our guide to <a href="/guides/multiple-bills-one-hospital-visit/">multiple bills from one hospital visit</a> explains who else may bill you.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>A hospital bill plus a radiologist bill for the same scan is usually the normal technical/professional split, not a duplicate. The thing to check is whether either part shows up twice. You can <a href="/scan">check your bill free</a> to flag repeated lines and compare each charge with what Medicare pays.</p>
</div>

<h2 id="read-the-bills">3. How to read each bill</h2>

<p>Ask both providers for an <strong>itemized bill</strong> (a line-by-line list of every charge with its code). A summary statement that only shows &ldquo;Radiology&rdquo; and a total is not enough to compare. Our guide on <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a> walks through the request.</p>

<h3>The hospital bill (technical part)</h3>

<p>Hospitals bill on a form called the UB-04 (CMS-1450). Each line has a <strong>revenue code</strong>, a four-digit code that says which hospital department the charge came from. Imaging usually shows up under these:</p>

<ul>
    <li><strong>032x</strong> &mdash; diagnostic radiology (for example, 0320 general, 0324 chest X-ray)</li>
    <li><strong>035x</strong> &mdash; CT scan (0350 general, 0351 head, 0352 body)</li>
    <li><strong>061x</strong> &mdash; MRI (0610 general, 0611 brain, 0612 spine)</li>
    <li><strong>040x</strong> &mdash; other imaging, such as ultrasound (0402) and diagnostic mammography (0401)</li>
</ul>

<p>Next to the revenue code you will often see a CPT code. The hospital line may not carry a TC modifier at all; the fact that it is on the hospital&rsquo;s facility bill is what tells you it is the technical part. For more on these codes, see <a href="/guides/hospital-revenue-codes-explained/">hospital revenue codes explained</a>.</p>

<h3>The radiologist bill (professional part)</h3>

<p>Radiologists bill on the physician claim form (CMS-1500). Look for the same CPT code with <strong>-26</strong> after it, such as 71046-26 for a chest X-ray read. The date of service should match the date of your scan, though the bill may arrive weeks later. The radiology group&rsquo;s name may be unfamiliar, since you likely did not meet the radiologist in person.</p>

<h2 id="real-duplicates">4. When it really is a duplicate</h2>

<p>Two bills for two parts is normal. These patterns are not, and are worth asking about:</p>

<ul>
    <li><strong>Two technical charges for one scan.</strong> The hospital bill lists the same CPT code under the same imaging revenue code twice on the same date, but you only had one scan. (A second line can be correct if you really had two studies, such as a repeat X-ray, so check your records first.)</li>
    <li><strong>A global charge plus a split charge.</strong> One bill shows the CPT code with no modifier (which already covers both parts), and a second bill also charges for the scan (TC) or the read (26) for the same test on the same date.</li>
    <li><strong>The same read billed twice.</strong> You see two modifier-26 charges for one scan, from the same group or from two different doctors. Medicare&rsquo;s manual says that for X-rays and EKGs given to ER patients, Medicare generally pays for only one interpretation, and pays for a second one only in unusual cases with documentation, such as a questionable finding that needs another doctor&rsquo;s expertise.</li>
    <li><strong>A read with no report.</strong> Medicare&rsquo;s manual says a quick &ldquo;review&rdquo; of an X-ray by the ER doctor, without a full written report, is not a separately payable interpretation; it is part of the ER visit charge.</li>
</ul>

<p>These are discrepancies to ask about, not proof of a mistake; the billing office should be able to explain each line. Our guide to <a href="/guides/duplicate-charges-hospital-bills/">duplicate charges on hospital bills</a> covers other repeat charges to look for.</p>

<h2 id="example">5. Example: comparing two bills line by line</h2>

<p><strong>Example:</strong> The following is made up to show the math. Names and amounts are not from a real bill.</p>

<p>You had one chest X-ray in a hospital outpatient department on March 12, 2026. You received two itemized bills.</p>

<table>
    <thead>
        <tr>
            <th>Bill</th>
            <th>Date</th>
            <th>Revenue code</th>
            <th>CPT code</th>
            <th>Charge</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Hospital</td>
            <td>03/12/2026</td>
            <td>0324 (chest X-ray)</td>
            <td>71046</td>
            <td>$310.00</td>
        </tr>
        <tr>
            <td>Hospital</td>
            <td>03/12/2026</td>
            <td>0324 (chest X-ray)</td>
            <td>71046</td>
            <td>$310.00</td>
        </tr>
        <tr>
            <td>Radiology group</td>
            <td>03/12/2026</td>
            <td>&mdash;</td>
            <td>71046-26</td>
            <td>$85.00</td>
        </tr>
    </tbody>
</table>

<p><strong>What is normal:</strong> one hospital line for the scan ($310.00) and one radiologist line for the read ($85.00). Together that is $310.00 + $85.00 = $395.00.</p>

<p><strong>What to question:</strong> the hospital billed the technical part twice. The billed total is $310.00 + $310.00 + $85.00 = $705.00. If the second $310.00 line turns out to be a duplicate, the total would drop to $705.00 &minus; $310.00 = $395.00.</p>

<p>You would ask the hospital, in writing, to explain or remove the second 71046 line. The radiologist&rsquo;s $85.00 read is the expected second bill.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Match the two bills by date of service and CPT code. One technical line plus one modifier-26 line is the normal pattern. If a part appears twice, put your question in writing. Our <a href="/guides/medical-bill-dispute-letter/">medical bill dispute letter guide</a> shows what to include.</p>
</div>

<h2 id="what-to-do">6. What to do, step by step</h2>

<ol>
    <li><strong>Gather everything:</strong> both bills and, if insured, your explanation of benefits (EOB) for each.</li>
    <li><strong>Ask for itemized bills</strong> from both the hospital and the radiology group if you only have summaries.</li>
    <li><strong>List each line</strong>: date, CPT code, modifier (26, TC or none) and amount.</li>
    <li><strong>Check each test.</strong> For each scan you had, you should usually see either one global line, or one technical line plus one modifier-26 line.</li>
    <li><strong>Mark anything that repeats</strong>: the same code on the same date twice, a global line plus a split line, or two reads.</li>
    <li><strong>Contact the billing office</strong> for the bill with the extra line and ask them to explain or correct it, in writing. Note dates and names.</li>
    <li><strong>Check the network status</strong> of the radiology group on your EOB. If it was out-of-network but the hospital was in-network, read the next section.</li>
    <li><strong>Hold off on paying the disputed line</strong> while you wait for an answer, and ask the billing office whether they will pause collection activity during the review.</li>
</ol>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>You do not have to sort this out from memory. Upload your itemized bill to <a href="/scan">check it free</a>: BillKarma flags repeated lines and shows how each charge compares with the Medicare rate for that code.</p>
</div>

<h2 id="no-surprises">7. Out-of-network radiologist? The No Surprises Act</h2>

<p>Sometimes the second bill is a surprise for another reason: the hospital was in-network, but the radiologist was not. The federal No Surprises Act, which took effect on January 1, 2022, addresses this.</p>

<p>Under the federal rule (45 CFR 149.420), an out-of-network provider who treats you as part of a visit to an in-network facility generally cannot bill you more than your in-network cost sharing (your normal copay, coinsurance and deductible). CMS lists the covered facilities as hospitals, hospital outpatient departments and ambulatory surgical centers.</p>

<p>Radiology gets extra protection. Some out-of-network providers can ask you to sign a notice and consent form giving up these protections, but the rule says that option does not apply to <strong>ancillary services</strong>, which include radiology and diagnostic services.</p>

<p>Limits to know, as of November 2026:</p>

<ul>
    <li>These protections apply to people with private health plans, such as job-based or marketplace coverage. They do not apply to people whose coverage is only Medicare, Medicaid, TRICARE, VA care or Indian Health Service, which CMS says already have their own protections against some out-of-network bills.</li>
    <li>They generally do not cover scans at a doctor&rsquo;s office or at an out-of-network facility.</li>
    <li>Short-term plans, fixed indemnity plans and health care sharing ministries are not covered.</li>
</ul>

<p>If you think a radiologist billed you more than your in-network share, ask your insurer to confirm how the claim was processed, and contact the radiology group&rsquo;s billing office. You can also call the federal No Surprises Help Desk at 1-800-985-3059 to ask questions or submit a complaint. For more detail, see our <a href="/guides/no-surprises-act-explained/">No Surprises Act guide</a>. For legal questions, consider talking to a consumer attorney or legal aid.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Why did I get two bills for one X-ray or CT scan?</h3>
        <p>Imaging is usually split into two parts. The technical component is the equipment, the room and the technologist who takes the images. The professional component is the radiologist&rsquo;s reading of the images and written report. When you have the scan at a hospital, the hospital bills the technical part and the radiologist (or their group) bills the reading separately, often marked with modifier 26. Two bills for those two parts is normal.</p>
    </div>
    <div class="faq-item">
        <h3>What does modifier 26 mean on a radiology bill?</h3>
        <p>Modifier 26 is a two-character add-on to a CPT code that means the bill covers only the professional component, the doctor&rsquo;s interpretation and report. Modifier TC means only the technical component. A code with no modifier, billed by one practice or imaging center that did both parts, is called a global charge and covers everything.</p>
    </div>
    <div class="faq-item">
        <h3>How can I tell if a radiology charge is a real duplicate?</h3>
        <p>Line up both bills by date of service and CPT code. Questions worth asking: the same technical charge appears twice on the hospital bill; one bill has a global charge (no modifier) while another bill also charges for the scan or the read; or the same reading is billed twice. Ask for itemized bills from both providers and ask the billing office to explain any line that overlaps.</p>
    </div>
    <div class="faq-item">
        <h3>Is the radiologist allowed to bill me out-of-network if the hospital was in-network?</h3>
        <p>If you have a private or job-based health plan, the No Surprises Act generally limits what an out-of-network radiologist can charge you for care related to a visit at an in-network hospital, hospital outpatient department or ambulatory surgical center: no more than your in-network cost sharing. Radiology is listed as an ancillary service, so the radiologist cannot ask you to sign away this protection. These rules do not cover people whose only coverage is Medicare, Medicaid, TRICARE, VA care or Indian Health Service, which have their own protections.</p>
    </div>
    <div class="faq-item">
        <h3>Who do I call if I think a radiology bill breaks the No Surprises Act?</h3>
        <p>Start with the radiology group&rsquo;s billing office and your insurer. You can also call the federal No Surprises Help Desk at 1-800-985-3059 with questions or to submit a complaint. For legal questions, consider talking to a consumer attorney or legal aid.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c13.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 13: Radiology Services and Other Diagnostic Procedures (sections 20, 100.1 and 150)</a></li>
    <li><a href="https://www.cms.gov/data-research/monitoring-programs/medicare-fee-service-compliance-programs/medicare-fee-service-recovery-audit-program/approved-rac-topics/0116-modifiers-tc-and-pc-incorrect-coding" target="_blank" rel="noopener">CMS &mdash; Recovery Audit Topic 0116: Modifiers TC and PC, Incorrect Coding</a></li>
    <li><a href="https://www.cms.gov/Research-Statistics-Data-and-Systems/Monitoring-Programs/Medicare-FFS-Compliance-Programs/Recovery-Audit-Program/Approved-RAC-Topics-Items/0136-Medical-Necessity-and-Coding-of-Chest-X-rays" target="_blank" rel="noopener">CMS &mdash; Recovery Audit Topic 0136: Radiologic Examination of the Chest (CPT 71045&ndash;71048)</a></li>
    <li><a href="https://bluebutton.cms.gov/resources/variables/rev_cntr" target="_blank" rel="noopener">CMS Blue Button &mdash; Revenue Center Code (REV_CNTR) values</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149/subpart-E/section-149.420" target="_blank" rel="noopener">eCFR &mdash; 45 CFR 149.420, Balance billing for non-emergency services by nonparticipating providers at participating facilities</a></li>
    <li><a href="https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/know-your-rights/insurance" target="_blank" rel="noopener">CMS &mdash; Know your medical bill rights when using insurance</a></li>
    <li><a href="https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/know-your-rights" target="_blank" rel="noopener">CMS &mdash; Know your medical bill rights (No Surprises Act effective date and Help Desk)</a></li>
</ul>
""",
})
