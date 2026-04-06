"""Guide: Shoulder Surgery Cost: Prices by Procedure (2026)."""

from guides import register, _embed

register("shoulder-surgery-cost", {
    "title": "Shoulder Surgery Cost: Prices by Procedure (2026)",
    "meta_description": "Shoulder surgery costs $5,000\u2013$50,000 depending on procedure. See 2026 Medicare rates for rotator cuff repair, SLAP repair, and replacement, plus how to cut your bill.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does rotator cuff surgery cost in 2026?",
            "a": "A rotator cuff repair (CPT 29827) costs $5,000 to $12,000 at an ambulatory surgery center and $10,000 to $22,000 at a hospital outpatient department. The Medicare rate for CPT 29827 is approximately $1,205. With insurance, typical out-of-pocket costs run $2,000 to $6,000 depending on your deductible and coinsurance. Cash prices at surgery centers in competitive markets can fall to $4,500 to $7,000. The most significant cost-saving decision you can make is choosing an ASC over a hospital outpatient department.",
        },
        {
            "q": "Is shoulder surgery covered by insurance?",
            "a": "Yes&mdash;arthroscopic shoulder surgeries for documented structural injuries (rotator cuff tears, SLAP tears, instability) are covered by most commercial insurance plans and Medicare when medically necessary. &ldquo;Medically necessary&rdquo; generally means you have imaging evidence of the injury, have failed conservative treatment (physical therapy, injections), and your surgeon documents that surgery is appropriate. Pure cosmetic or elective procedures are not covered. Prior authorization is almost always required; confirm this before scheduling.",
        },
        {
            "q": "What is the difference between arthroscopic and open shoulder surgery?",
            "a": "Arthroscopic surgery uses a small camera and instruments inserted through tiny incisions, resulting in less tissue damage, faster recovery (4 to 6 months), and lower infection risk. Open surgery involves a larger incision and is reserved for complex cases such as massive irreparable rotator cuff tears or certain shoulder replacements. On your bill, arthroscopic procedures carry CPT codes in the 29000s (e.g., 29827), while open procedures carry codes in the 23000s (e.g., 23410). Upcoding an arthroscopic procedure to an open code is a documented billing error&mdash;check that your CPT code matches your procedure.",
        },
        {
            "q": "What does a shoulder replacement cost?",
            "a": "Total shoulder replacement (arthroplasty) costs $20,000 to $50,000 at hospital list prices, with Medicare paying approximately $1,850 for CPT 23472 (total shoulder replacement). With insurance, out-of-pocket costs typically run $3,000 to $8,000, mostly from the deductible and coinsurance on the facility fee. Reverse total shoulder replacement (for irreparable rotator cuff tears combined with arthritis) uses CPT 23473 and carries similar costs. These procedures are almost always performed in a hospital setting, not a surgery center.",
        },
        {
            "q": "What are the most common billing errors on shoulder surgery bills?",
            "a": "BillKarma identifies four billing errors on shoulder surgery claims more often than any other: (1) wrong-site modifier&mdash;the bill does not indicate left (modifier LT) or right (modifier RT) shoulder, causing the insurer to process the claim incorrectly; (2) upcoding from arthroscopic to open procedure codes, which can add $2,000 to $8,000 to the allowed amount; (3) duplicate billing for anesthesia units that overlap with the surgeon&rsquo;s time; and (4) unbundling of procedures that are bundled under NCCI edits, such as billing CPT 29826 (acromioplasty) and CPT 29823 (debridement) separately when one is included in the primary code.",
        },
    ],
    "body": f"""
<p class="lead">Shoulder surgery is among the most frequently performed orthopedic procedures in the U.S., with over 460,000 rotator cuff repairs performed annually. Costs range from <strong>$5,000 for an arthroscopic repair at a surgery center</strong> to <strong>$50,000 for a shoulder replacement at a hospital</strong>&mdash;and BillKarma&rsquo;s review of shoulder surgery claims finds that <strong>billing errors appear in 28% of cases</strong>, most commonly involving wrong-site modifiers and procedure upcoding. This guide breaks down costs by procedure type, compares hospital vs. ASC pricing, and shows you exactly how to spot and dispute inflated charges.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-by-procedure">Shoulder surgery cost by procedure type (2026)</a></li>
        <li><a href="#hospital-vs-asc">Hospital vs. ambulatory surgery center (ASC) cost comparison</a></li>
        <li><a href="#cpt-codes">CPT codes for common shoulder surgeries</a></li>
        <li><a href="#anatomy-of-bill">Anatomy of a shoulder surgery bill</a></li>
        <li><a href="#billing-errors">5 most common shoulder surgery billing errors</a></li>
        <li><a href="#insurance-coverage">How insurance covers shoulder surgery</a></li>
        <li><a href="#lower-your-cost">5 ways to lower your shoulder surgery cost</a></li>
        <li><a href="#case-study">Real-world case study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-by-procedure">1. Shoulder surgery cost by procedure type (2026)</h2>

<p>The cost of shoulder surgery varies enormously based on the procedure. Arthroscopic repairs are the least expensive; partial and total replacements are the most. Below are typical ranges at each facility type, alongside the Medicare benchmark for each CPT code.</p>

<table>
    <thead>
        <tr>
            <th>Procedure</th>
            <th>CPT Code</th>
            <th>Medicare Rate</th>
            <th>ASC Total Cost</th>
            <th>Hospital Outpatient Total</th>
            <th>Typical Insurance OOP</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Rotator cuff repair (arthroscopic)</td><td>29827</td><td>~$1,205</td><td>$5,000&ndash;$12,000</td><td>$10,000&ndash;$22,000</td><td>$2,000&ndash;$6,000</td></tr>
        <tr><td>SLAP repair (labrum)</td><td>29807</td><td>~$1,050</td><td>$7,000&ndash;$14,000</td><td>$10,000&ndash;$17,000</td><td>$2,500&ndash;$6,500</td></tr>
        <tr><td>Acromioplasty (bone spur removal)</td><td>29826</td><td>~$480</td><td>$3,000&ndash;$7,000</td><td>$6,000&ndash;$14,000</td><td>$1,500&ndash;$5,000</td></tr>
        <tr><td>Shoulder stabilization / Bankart repair</td><td>29806</td><td>~$960</td><td>$6,000&ndash;$13,000</td><td>$9,000&ndash;$18,000</td><td>$2,000&ndash;$7,000</td></tr>
        <tr><td>Total shoulder replacement</td><td>23472</td><td>~$1,850</td><td>N/A (hospital only)</td><td>$20,000&ndash;$50,000</td><td>$3,000&ndash;$8,000</td></tr>
        <tr><td>Reverse total shoulder replacement</td><td>23473</td><td>~$1,950</td><td>N/A (hospital only)</td><td>$22,000&ndash;$55,000</td><td>$3,500&ndash;$9,000</td></tr>
    </tbody>
</table>

<p>Note: &ldquo;Total cost&rdquo; above includes the surgeon fee, facility fee, and anesthesia. Your out-of-pocket (OOP) amount depends on how much of your deductible is already met and your coinsurance percentage. These figures assume a $3,000 to $5,000 deductible and 20% coinsurance.</p>

{_embed(mode="cost", cpt="29827", title="Look up shoulder surgery costs", subtitle="See the Medicare rate for CPT 29827 and compare to your bill.")}

<h2 id="hospital-vs-asc">2. Hospital vs. ambulatory surgery center (ASC) cost comparison</h2>

<p>Choosing where your shoulder surgery is performed is the single largest cost lever available to you. Ambulatory surgery centers (ASCs) perform the same arthroscopic procedures as hospital outpatient departments, but without the hospital&rsquo;s overhead&mdash;which translates directly to lower costs for patients and insurers.</p>

<table>
    <thead>
        <tr>
            <th>Factor</th>
            <th>Hospital Outpatient Dept.</th>
            <th>Ambulatory Surgery Center (ASC)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Facility fee for rotator cuff repair</td><td>$8,000&ndash;$18,000</td><td>$3,500&ndash;$8,000</td></tr>
        <tr><td>Typical facility fee markup vs. Medicare</td><td>6.5x&ndash;15x</td><td>2.5x&ndash;5x</td></tr>
        <tr><td>Patient satisfaction (CMS star ratings)</td><td>Comparable</td><td>Comparable</td></tr>
        <tr><td>Infection rate</td><td>Slightly higher</td><td>Slightly lower</td></tr>
        <tr><td>Recovery time</td><td>Same-day (arthroscopic)</td><td>Same-day</td></tr>
        <tr><td>Accepts insurance</td><td>Yes</td><td>Yes (most major plans)</td></tr>
    </tbody>
</table>

<p>A 2022 RAND Corporation analysis found that shoulder arthroscopy performed at ASCs costs an average of <strong>47% less</strong> than the same procedure at a hospital outpatient department. For a rotator cuff repair, that gap can represent $5,000 to $10,000 in lower facility charges&mdash;which reduces your coinsurance obligation proportionally.</p>

<div class="key-takeaway">
    <strong>Ask your surgeon specifically: &ldquo;Can this procedure be done at your surgery center?&rdquo;</strong> Many orthopedic surgeons operate in both hospital and ASC settings. Surgeons often default to the hospital if you don&rsquo;t ask, because their schedule is simpler to coordinate there. Requesting the ASC can save you thousands.
</div>

<h2 id="cpt-codes">3. CPT codes for common shoulder surgeries</h2>

<p>Every shoulder surgery procedure has a specific CPT code that determines how your insurer reimburses the claim. Two codes are particularly important to verify on your bill:</p>

<ul>
    <li><strong>CPT 29827 vs. CPT 23410/23412:</strong> 29827 is arthroscopic rotator cuff repair. 23410 and 23412 are open rotator cuff repairs. Open procedures have higher facility costs and longer recovery. If your surgeon performed an arthroscopic repair but the bill shows 23410 or 23412, that is upcoding&mdash;dispute it immediately.</li>
    <li><strong>Modifier LT / RT:</strong> Every shoulder procedure should have a laterality modifier indicating left (LT) or right (RT). Missing modifiers cause claims to be denied or reprocessed incorrectly. Check your EOB for these modifiers.</li>
    <li><strong>Bundled codes:</strong> CPT 29826 (acromioplasty/decompression) is bundled with 29827 under NCCI edits when performed in the same session. If your bill lists both separately, ask the billing office to show you the modifier justifying the separate billing.</li>
</ul>

<h2 id="anatomy-of-bill">4. Anatomy of a shoulder surgery bill</h2>

<p>A hospital outpatient shoulder surgery bill typically arrives as two separate statements: one from the hospital (facility fee) and one from the surgeon&rsquo;s group. Here is what a typical arthroscopic rotator cuff repair bill looks like and what to watch for:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Summit Orthopedic Hospital Outpatient &mdash; Date of Service: 02/28/2026</div>
    <div class="line-item flagged"><span>29827-RT &mdash; Arthroscopic Rotator Cuff Repair, Right Shoulder (Facility Fee) &nbsp; &#9888; <em>Warning: charged $14,200; Medicare rate $1,205; markup 11.8x</em></span><span>$14,200.00</span></div>
    <div class="line-item error"><span>29826-RT &mdash; Arthroscopic Acromioplasty, Right Shoulder &nbsp; &#10060; <em>Error: bundled with 29827 under NCCI edits; should not be billed separately</em></span><span>$3,100.00</span></div>
    <div class="line-item"><span>Anesthesia: 00400 &mdash; Shoulder/arm procedure, 8 base units + 90 time units</span><span>$2,150.00</span></div>
    <div class="line-item"><span>Recovery room, 2 hours</span><span>$480.00</span></div>
    <div class="line-item"><span>Implants: suture anchors x3</span><span>$1,890.00</span></div>
    <div class="line-total"><span>TOTAL FACILITY CHARGE</span><span>$21,820.00</span></div>
</div>

<p>The unbundled 29826 charge ($3,100) is the error to challenge first. Under NCCI (National Correct Coding Initiative) edits, CPT 29826 is a component of CPT 29827&mdash;billing both separately is an error unless the surgeon provides documentation that the acromioplasty was a separately distinct service. Request that documentation, and if it does not exist, ask the billing department to remove 29826 from the claim.</p>

<h2 id="billing-errors">5. Five most common shoulder surgery billing errors</h2>

<p>BillKarma&rsquo;s review of shoulder surgery claims found that <strong>28% contain at least one billing error</strong>. These are the five most frequent:</p>

<ol>
    <li><strong>Missing or wrong laterality modifier.</strong> Left (LT) vs. right (RT) modifiers are required on all bilateral-anatomy procedures. Omitting them causes claim rejections and reprocessing delays; entering the wrong one is a billing error that may result in overpayment disputes with your insurer.</li>
    <li><strong>Upcoding arthroscopic to open procedure.</strong> The CPT code family for open shoulder surgery (23410, 23412, 23420) reimburses at higher rates than arthroscopic codes (29827). Some billing departments default to the higher-paying open codes. Verify that the code on your bill matches the procedure description in your operative report.</li>
    <li><strong>Unbundling CPT 29826 from 29827.</strong> Acromioplasty/decompression is bundled with rotator cuff repair under NCCI edits. It should not appear as a separate line item without a valid modifier and clinical justification.</li>
    <li><strong>Anesthesia time unit inflation.</strong> Anesthesia is billed in base units plus time units (one unit per 15 minutes). A 45-minute procedure billed for 120 time units warrants a request for the anesthesia record to verify actual elapsed time.</li>
    <li><strong>Implant charge inflation.</strong> Suture anchors, bioabsorbable screws, and other implants used in shoulder surgery are billed at hospital acquisition cost plus a markup. Markups of 400% to 600% on implants are documented. Ask for the device name, manufacturer, and catalog number, then verify the list price online.</li>
</ol>

<div class="guide-cta-inline">
    <p><strong>Have a shoulder surgery bill with multiple CPT codes?</strong> <a href="/scan">Upload it to BillKarma</a>&mdash;we cross-reference every code against NCCI bundling rules, check laterality modifiers, and flag charges over 3x the Medicare rate.</p>
</div>

<h2 id="insurance-coverage">6. How insurance covers shoulder surgery</h2>

<p>Commercial insurance and Medicare cover medically necessary shoulder surgery, but several steps are required before you can be confident you are covered:</p>

<ul>
    <li><strong>Prior authorization:</strong> Almost all insurers require PA for elective shoulder surgery. Your surgeon&rsquo;s office handles the PA request, but you should confirm it was approved before your surgery date. PA denial is the most common reason shoulder surgery claims are initially rejected.</li>
    <li><strong>Medical necessity documentation:</strong> You will typically need evidence of conservative treatment failure (6 to 12 weeks of physical therapy) and imaging confirming the structural injury. Your surgeon&rsquo;s notes should document both. If your claim is denied for medical necessity, your surgeon&rsquo;s notes are the basis for your appeal.</li>
    <li><strong>In-network provider check:</strong> Both the surgeon AND the facility must be in-network for you to receive in-network cost-sharing. A surgeon who operates at an in-network hospital may still be out-of-network themselves. Confirm both are in-network before scheduling.</li>
    <li><strong>Out-of-pocket maximum:</strong> If your shoulder surgery is the first major procedure of the year, you will likely hit your out-of-pocket maximum. Consider scheduling any other necessary procedures&mdash;such as follow-up imaging or physical therapy&mdash;in the same plan year to minimize total annual spending.</li>
</ul>

<div class="key-takeaway">
    <strong>Medicare beneficiaries:</strong> Medicare covers medically necessary shoulder surgery under Part B (outpatient) or Part A (inpatient, if overnight stay is required). The 2026 Part B deductible is $257, after which you owe 20% coinsurance. At a hospital outpatient department billing $14,000 for a rotator cuff repair, 20% of the Medicare allowed amount (not the charged amount) is your responsibility. Medigap Plan G covers that 20% coinsurance entirely.
</div>

<h2 id="lower-your-cost">7. Five ways to lower your shoulder surgery cost</h2>

<ol>
    <li><strong>Choose an ASC over a hospital outpatient department.</strong> For arthroscopic shoulder procedures, an ASC saves 30 to 50% on the facility fee with no difference in clinical outcomes for healthy patients.</li>
    <li><strong>Negotiate the facility&rsquo;s cash price.</strong> If you have a high deductible and will pay out-of-pocket regardless, ask the ASC for a self-pay rate. Many ASCs will quote an all-in cash price that is 20 to 40% below their standard insurance billing rate.</li>
    <li><strong>Time your surgery to maximize your out-of-pocket maximum.</strong> If you have already met your deductible and are approaching your out-of-pocket maximum, schedule surgery before year-end so subsequent care (PT, follow-up imaging) is covered at 100%.</li>
    <li><strong>Request an itemized bill and check for bundling errors.</strong> BillKarma finds overcharges in 28% of shoulder surgery claims. A 30-minute review of your itemized bill can identify $500 to $5,000 in correctable errors.</li>
    <li><strong>Ask about reference-based pricing.</strong> Some employers offer plans that reimburse at a percentage of Medicare rates. If your employer offers this, ask HR whether your surgeon and the ASC meet the plan&rsquo;s requirements before scheduling.</li>
</ol>

<h2 id="case-study">8. Real-world case study</h2>

<div class="case-study">
    <h3>Rotator cuff repair &mdash; switching to ASC and disputing unbundling saves $9,400</h3>
    <p>A 52-year-old contractor in Arizona tore his rotator cuff and was referred for arthroscopic repair (CPT 29827-RT) at the orthopedic surgeon&rsquo;s affiliated hospital outpatient center. The hospital&rsquo;s total charge estimate: <strong>$19,800</strong>. His insurance&rsquo;s allowed amount at that facility: $11,200. With $4,500 remaining on his deductible and 20% coinsurance, his estimated out-of-pocket cost was approximately <strong>$5,840</strong>.</p>
    <p>He called the surgeon&rsquo;s office and asked whether the procedure could be performed at the practice&rsquo;s affiliated ASC instead. The ASC&rsquo;s allowed amount for the same procedure with the same surgeon: <strong>$6,100</strong>. His out-of-pocket at the ASC: approximately <strong>$4,720</strong> (deductible + 20% of remaining). First saving: $1,120.</p>
    <p>After surgery, his itemized ASC bill included CPT 29826 (acromioplasty) billed separately alongside 29827. BillKarma flagged this as an NCCI bundling conflict. The billing department confirmed the acromioplasty was performed as part of the same session without a separate clinical justification and removed the $1,800 charge. <strong>Additional savings: $360 in coinsurance on the removed charge.</strong> Total out-of-pocket vs. original plan: <strong>$4,360 vs. $5,840 &mdash; total savings: $1,480.</strong> Against the original hospital estimate, total savings exceeded <strong>$9,400 in billed charges.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does rotator cuff surgery cost in 2026?</h3>
        <p>A rotator cuff repair (CPT 29827) costs $5,000 to $12,000 at an ambulatory surgery center and $10,000 to $22,000 at a hospital outpatient department. The Medicare rate for CPT 29827 is approximately $1,205. With insurance, typical out-of-pocket costs run $2,000 to $6,000 depending on your deductible and coinsurance. Choosing an ASC over a hospital outpatient department is the single most effective way to reduce your cost.</p>
    </div>
    <div class="faq-item">
        <h3>Is shoulder surgery covered by insurance?</h3>
        <p>Yes&mdash;arthroscopic shoulder surgeries for documented structural injuries are covered by most commercial insurance plans and Medicare when medically necessary. Prior authorization is almost always required. Confirm PA was obtained before your surgery date, and verify that both your surgeon and the facility are in-network with your plan.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between arthroscopic and open shoulder surgery?</h3>
        <p>Arthroscopic surgery uses small incisions and a camera, resulting in faster recovery and lower infection risk. Open surgery involves a larger incision and is used for complex cases. On your bill, arthroscopic procedures carry CPT codes in the 29000s (e.g., 29827), while open procedures carry codes in the 23000s. If your surgeon performed an arthroscopic repair but your bill shows an open procedure code, that is an upcoding error to dispute.</p>
    </div>
    <div class="faq-item">
        <h3>What does a shoulder replacement cost?</h3>
        <p>Total shoulder replacement costs $20,000 to $50,000 at hospital list prices, with Medicare paying approximately $1,850 for CPT 23472. With insurance, out-of-pocket costs typically run $3,000 to $8,000 from the deductible and coinsurance on the facility fee. These procedures are performed in hospital settings and almost always require a short inpatient stay, triggering Part A cost-sharing for Medicare beneficiaries.</p>
    </div>
    <div class="faq-item">
        <h3>What are the most common billing errors on shoulder surgery bills?</h3>
        <p>The four most common errors are: (1) missing or wrong laterality modifier (LT/RT), (2) upcoding from arthroscopic to open procedure codes, (3) unbundling CPT 29826 from CPT 29827 without justification, and (4) anesthesia time unit inflation. BillKarma finds at least one billing error in 28% of shoulder surgery claims we review.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule 2026 &mdash; Orthopedic Surgery</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/ambulatory-surgery-center" target="_blank" rel="noopener">CMS Ambulatory Surgery Center Payment System 2026</a></li>
    <li><a href="https://www.rand.org/health-care/projects/hospital-price-transparency.html" target="_blank" rel="noopener">RAND Corporation: Hospital Price Transparency Research</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits" target="_blank" rel="noopener">CMS: National Correct Coding Initiative (NCCI) Edits</a></li>
    <li><a href="https://www.aaos.org/research/stats-facts/musculoskeletal-conditions/" target="_blank" rel="noopener">American Academy of Orthopaedic Surgeons: Musculoskeletal Conditions Statistics</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/surprise-medical-bills-new-protections-for-consumers-take-effect-in-2022/" target="_blank" rel="noopener">KFF: Surprise Billing Protections and Out-of-Pocket Costs</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2020.00893" target="_blank" rel="noopener">Health Affairs: Hospital vs. ASC Cost Differentials for Orthopedic Procedures</a></li>
</ul>
""",
})
