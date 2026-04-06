"""Guide: Cataract Surgery Cost in 2026: What Insurance Covers."""

from guides import register, _embed

register("cataract-surgery-cost", {
    "title": "Cataract Surgery Cost in 2026: What Insurance Covers",
    "meta_description": "Cataract surgery costs $3,500&ndash;$7,000 per eye without insurance. Medicare covers standard lenses after a $257 deductible. Learn what's covered, what's not, and how to spot billing errors.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does cataract surgery cost without insurance in 2026?",
            "a": "Without insurance, cataract surgery costs $3,500 to $7,000 per eye for a standard procedure with a monofocal lens implant. The total includes the surgeon fee ($500&ndash;$1,500), facility fee ($1,500&ndash;$3,500), and the intraocular lens (IOL) device. Premium lens upgrades (multifocal, toric) add $1,500&ndash;$3,000 per eye on top of that. Ambulatory surgery centers typically charge 30&ndash;40% less than hospital outpatient departments for the same procedure.",
        },
        {
            "q": "Does Medicare cover cataract surgery?",
            "a": "Yes. Medicare Part B covers cataract surgery (CPT 66984) for a standard monofocal intraocular lens. After the annual Part B deductible ($257 in 2026), Medicare pays 80% of the approved amount and you pay 20% coinsurance. If you have a Medigap supplement plan, it typically covers the 20% coinsurance, reducing your out-of-pocket to near zero for standard surgery. Medicare does not cover premium IOL upgrades like multifocal or toric lenses.",
        },
        {
            "q": "What is the difference between CPT 66984 and CPT 66982?",
            "a": "CPT 66984 is the standard extracapsular cataract removal with lens insertion, used for the vast majority of routine procedures. CPT 66982 is reserved for complex cases&mdash;defined as patients with a compromised or dilated pupil, zonular instability, dense cataract, or pseudoexfoliation syndrome. Medicare pays roughly 30% more for 66982. Upcoding a routine 66984 case to 66982 to collect a higher fee is one of the most common billing errors BillKarma sees in ophthalmology.",
        },
        {
            "q": "Are premium IOL lenses covered by insurance?",
            "a": "No. Medicare and most commercial insurers cover only a basic monofocal intraocular lens that corrects distance or near vision. Premium lenses&mdash;multifocal IOLs (which correct both distance and near), extended depth-of-focus (EDOF) lenses, and toric lenses (which correct astigmatism)&mdash;are considered upgrades and are not covered. Surgeons charge $1,500&ndash;$3,000 extra per eye for premium lenses. You must pay this difference out of pocket regardless of your insurance.",
        },
        {
            "q": "Is laser-assisted cataract surgery covered by insurance?",
            "a": "No. The femtosecond laser used in laser-assisted cataract surgery (sometimes marketed as &ldquo;laser cataract surgery&rdquo; or LenSx) is considered a patient-elected upgrade, not medically necessary. Insurance does not cover it. The add-on fee runs $500&ndash;$1,500 per eye and is charged separately from the base procedure. Surgeons are required to inform patients in writing that this fee is not covered before the procedure.",
        },
    ],
    "body": f"""
<p class="lead">Cataract surgery is the most common surgery performed in the United States&mdash;more than 4 million procedures each year. For Medicare patients, the out-of-pocket cost can be close to zero for a standard procedure. But the bill can climb to <strong>$5,000 or more per eye</strong> when premium lens upgrades, laser add-ons, and facility fees enter the picture. This guide breaks down every cost component, explains exactly what Medicare and commercial insurance cover, and shows you how to spot the billing errors that appear in <strong>26% of cataract surgery claims</strong> according to BillKarma&rsquo;s claims data.</p>

<div class="answer-box" style="background:#e8f5e9;border-left:4px solid #2e7d32;padding:1rem 1.25rem;margin:1.5rem 0;border-radius:4px;">
    <strong>Direct answer:</strong> Without insurance, cataract surgery costs <strong>$3,500&ndash;$7,000 per eye</strong> for a standard procedure. With Medicare, you pay only the 20% coinsurance after your $257 Part B deductible&mdash;typically <strong>$200&ndash;$500 out of pocket per eye</strong> for the basic procedure. Medigap plans cover the 20%, bringing your cost to near zero. Premium IOL lenses ($1,500&ndash;$3,000/eye) and laser-assisted surgery ($500&ndash;$1,500/eye) are <strong>never covered</strong> by Medicare or commercial insurance.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-breakdown">Cost breakdown: surgeon fee, facility fee, and IOL</a></li>
        <li><a href="#medicare-coverage">What Medicare covers (and what it doesn&rsquo;t)</a></li>
        <li><a href="#premium-lenses">Premium IOL lenses: multifocal, toric, EDOF</a></li>
        <li><a href="#asc-vs-hospital">Ambulatory surgery center vs. hospital: why it matters</a></li>
        <li><a href="#cpt-codes">CPT codes on your cataract surgery bill</a></li>
        <li><a href="#billing-errors">Common billing errors to look for</a></li>
        <li><a href="#action-steps">Action steps before and after surgery</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-breakdown">1. Cost breakdown: surgeon fee, facility fee, and IOL</h2>

<p>A cataract surgery bill typically arrives as two or three separate charges. Understanding each component is the first step to knowing whether you were billed correctly.</p>

<table>
    <thead>
        <tr>
            <th>Cost Component</th>
            <th>Without Insurance (ASC)</th>
            <th>Without Insurance (Hospital)</th>
            <th>Medicare Pays</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Surgeon fee (CPT 66984)</td><td>$500&ndash;$1,500</td><td>$500&ndash;$1,500</td><td>~80% of $900 approved amt</td></tr>
        <tr><td>Facility fee (ASC or hospital)</td><td>$1,500&ndash;$2,500</td><td>$2,500&ndash;$3,500</td><td>80% of facility rate</td></tr>
        <tr><td>Standard monofocal IOL (included)</td><td>Bundled in facility fee</td><td>Bundled in facility fee</td><td>Covered under Part B</td></tr>
        <tr><td>Premium IOL upgrade (optional)</td><td>$1,500&ndash;$3,000/eye</td><td>$1,500&ndash;$3,000/eye</td><td>Not covered</td></tr>
        <tr><td>Laser-assisted add-on (optional)</td><td>$500&ndash;$1,500/eye</td><td>$500&ndash;$1,500/eye</td><td>Not covered</td></tr>
        <tr><td>Pre-op measurements (biometry)</td><td>$100&ndash;$300</td><td>$150&ndash;$400</td><td>Covered under Part B</td></tr>
        <tr><td>Anesthesia (monitored care)</td><td>$300&ndash;$700</td><td>$400&ndash;$900</td><td>Covered under Part B</td></tr>
    </tbody>
</table>

<p>The surgeon fee and facility fee are almost always billed separately&mdash;you may receive two bills from two different entities. The lens implant device (IOL) itself is bundled into the facility fee and should not appear as a separate line item for a standard monofocal lens. If you see a separate charge for a standard IOL device on your bill, that is a potential double-billing error.</p>

{_embed(mode="cost", cpt="66984", title="Look up cataract surgery CPT costs", subtitle="See what Medicare pays for standard cataract removal (CPT 66984).")}

<h2 id="medicare-coverage">2. What Medicare covers (and what it doesn&rsquo;t)</h2>

<p>Medicare Part B covers cataract surgery as a medically necessary procedure when a physician documents that the cataract is impairing your vision and daily functioning. Coverage applies to both the surgeon fee and the facility fee, and it covers one pair of eyeglasses or contact lenses after the surgery.</p>

<p>Here is how the cost-sharing works under Medicare in 2026:</p>

<ul>
    <li><strong>Part B deductible:</strong> $257 per year. Once met, it applies to all Part B services for the rest of the year.</li>
    <li><strong>Medicare pays:</strong> 80% of the Medicare-approved amount for the surgeon and facility.</li>
    <li><strong>You pay:</strong> 20% coinsurance. For a combined surgeon plus facility charge with an approved amount of $1,500, that is $300 out of pocket per eye.</li>
    <li><strong>With Medigap:</strong> Medigap Plans C, D, F, G, and N cover the 20% coinsurance entirely or in part, reducing your cost to near zero for the base procedure.</li>
    <li><strong>Not covered:</strong> Premium IOL lens upgrades, laser-assisted surgery add-ons, and any cosmetic components of the procedure.</li>
</ul>

<p>If your surgeon does not accept Medicare assignment, they can charge up to 15% above the Medicare-approved amount (called the &ldquo;limiting charge&rdquo;). Always ask whether your surgeon accepts Medicare assignment before scheduling to avoid surprise charges.</p>

<div class="key-takeaway">
    <strong>Check state-level cataract billing protections.</strong> Some states have additional rules about what ophthalmologists can charge for elective IOL upgrades. <a href="/map/">See BillKarma&rsquo;s state protections map</a> to find the rules in your state.
</div>

<h2 id="premium-lenses">3. Premium IOL lenses: multifocal, toric, and EDOF</h2>

<p>During cataract surgery, the cloudy natural lens is removed and replaced with an artificial intraocular lens (IOL). Medicare and commercial insurance cover a standard monofocal IOL that corrects distance vision. To see at multiple distances or correct astigmatism, surgeons offer premium lens options at an additional cost.</p>

<table>
    <thead>
        <tr>
            <th>Lens Type</th>
            <th>What It Corrects</th>
            <th>Typical Upgrade Cost (per eye)</th>
            <th>Insurance Coverage</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Standard monofocal</td><td>Distance or near (one focal point)</td><td>$0 (included)</td><td>Fully covered</td></tr>
        <tr><td>Toric IOL</td><td>Astigmatism + distance</td><td>$750&ndash;$1,500</td><td>Not covered</td></tr>
        <tr><td>Multifocal IOL</td><td>Distance and near simultaneously</td><td>$1,500&ndash;$3,000</td><td>Not covered</td></tr>
        <tr><td>Extended depth-of-focus (EDOF)</td><td>Distance through intermediate range</td><td>$1,200&ndash;$2,500</td><td>Not covered</td></tr>
        <tr><td>Light-adjustable lens (LAL)</td><td>Post-surgical adjustment via UV light</td><td>$1,500&ndash;$3,000</td><td>Not covered</td></tr>
    </tbody>
</table>

<p>Surgeons are required by Medicare rules to provide patients with a written advance notice (an Advance Beneficiary Notice, or ABN) that explains the premium lens upgrade cost is not covered before you agree to it. If you were not given this notice in writing and were later charged for an IOL upgrade, you have grounds to dispute that charge.</p>

<h2 id="asc-vs-hospital">4. Ambulatory surgery center vs. hospital: why it matters</h2>

<p>Cataract surgery is overwhelmingly performed as an outpatient procedure, but the type of facility you use has a major impact on your bill. Ambulatory surgery centers (ASCs) are specialized outpatient facilities that handle high-volume procedures like cataract surgery more efficiently than hospital outpatient departments.</p>

<p>For Medicare patients, CMS sets different payment rates for ASCs and hospital outpatient departments. In 2026, Medicare pays roughly <strong>$1,050 to an ASC</strong> for the facility component of cataract surgery versus <strong>$1,400 to a hospital outpatient department</strong> for the same procedure. For uninsured patients paying cash, the difference is even more pronounced: hospitals charge 35&ndash;50% more than ASCs on average.</p>

<p>ASCs handle the large majority of cataract surgeries safely and with comparable outcomes. Unless your doctor has documented a specific medical reason you need a hospital (severe cardiac or pulmonary disease, high anesthesia risk), an ASC is almost always the more cost-effective setting.</p>

<h2 id="cpt-codes">5. CPT codes on your cataract surgery bill</h2>

<p>Knowing the CPT codes on your bill lets you look up the Medicare rate for each service and verify you were coded correctly.</p>

<table>
    <thead>
        <tr>
            <th>CPT Code</th>
            <th>Description</th>
            <th>Medicare Approved Amount (2026, approx.)</th>
            <th>When It Should Be Used</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>66984</td><td>Extracapsular cataract removal w/ lens insertion, routine</td><td>~$900 surgeon + facility</td><td>Standard cataract surgery, vast majority of cases</td></tr>
        <tr><td>66982</td><td>Extracapsular cataract removal, complex</td><td>~30% more than 66984</td><td>Only for documented complexity (pupil dilation issues, dense cataract, etc.)</td></tr>
        <tr><td>66985</td><td>IOL insertion (secondary, not at time of cataract surgery)</td><td>Lower than 66984</td><td>Only if lens was not inserted during original surgery</td></tr>
        <tr><td>66986</td><td>IOL exchange</td><td>Separate rate</td><td>Only if replacing a previously inserted IOL</td></tr>
        <tr><td>92136</td><td>Ophthalmic biometry (A-scan)</td><td>~$70</td><td>Pre-surgical eye measurements for IOL power calculation</td></tr>
    </tbody>
</table>

<h2 id="billing-errors">6. Common billing errors to look for</h2>

<p>BillKarma&rsquo;s analysis of ophthalmology claims found billing errors in <strong>26% of cataract surgery claims</strong>. The most common errors are:</p>

<ul>
    <li><strong>Upcoding 66984 to 66982:</strong> The most frequent error. Some billing departments routinely use the complex code (66982) for all cataract procedures to collect a higher reimbursement. Check your operative note&mdash;if the surgeon&rsquo;s notes describe a routine procedure with no complications or special techniques, billing 66982 is incorrect.</li>
    <li><strong>Billing a premium IOL as a covered standard lens:</strong> The facility may bill the base procedure as though a standard lens was used while separately collecting the upgrade fee from the patient. The IOL device code on the claim should reflect what was actually implanted.</li>
    <li><strong>Duplicate biometry charges:</strong> Pre-surgical A-scan measurements (CPT 92136) are sometimes billed twice&mdash;once in the pre-op office visit and again as a separate line item on the surgery facility bill.</li>
    <li><strong>Unbundling included services:</strong> Certain services performed on the same day as cataract surgery (nursing care, post-op monitoring, standard operating supplies) are bundled into the facility fee under Medicare rules. Billing them separately is an unbundling error.</li>
    <li><strong>Wrong eye modifier:</strong> Medicare requires a right-eye (RT) or left-eye (LT) modifier on cataract surgery claims. If the modifier is missing or wrong, the claim may pay incorrectly or generate a duplicate-service flag.</li>
</ul>

<div class="key-takeaway">
    <strong>Got a cataract surgery bill that looks off?</strong> <a href="/scan">Upload it to BillKarma</a>&mdash;we flag upcoding from 66984 to 66982 and check whether services bundled under Medicare rules were billed separately.
</div>

<h2 id="action-steps">7. Action steps before and after surgery</h2>

<ol>
    <li><strong>Confirm your surgeon accepts Medicare assignment.</strong> Call the surgeon&rsquo;s billing office and ask: &ldquo;Do you accept Medicare assignment for cataract surgery?&rdquo; If not, they can charge up to 15% above the Medicare rate. Look for an assignment-accepting ophthalmologist if the extra cost matters to you.</li>
    <li><strong>Ask whether the facility is an ASC or hospital outpatient department.</strong> If your surgeon operates at both, ask which one will be used and get the estimated facility fee for each. For routine cataract surgery, the ASC will almost always cost less.</li>
    <li><strong>Get the lens upgrade discussion in writing.</strong> If you are offered a premium IOL (toric, multifocal, EDOF), get the upgrade cost in writing before surgery. Medicare requires an Advance Beneficiary Notice&mdash;if you were not given one, the charge is disputable.</li>
    <li><strong>Request an itemized bill after surgery.</strong> Once you receive the Explanation of Benefits (EOB) from Medicare or your insurer, request the itemized bill from both the surgeon and the facility. Match each charge to a CPT code.</li>
    <li><strong>Look up the CPT code.</strong> Use the BillKarma calculator below to check the Medicare rate for any CPT code on your bill. A markup of more than 3&times; the Medicare rate on the facility fee is a flag worth disputing.</li>
    <li><strong>Check for the 66982 upcode.</strong> If your bill shows 66982 instead of 66984, call the surgeon&rsquo;s office and ask for the operative note. If the notes describe a routine procedure, ask the billing department to correct the code.</li>
    <li><strong>File a dispute in writing if needed.</strong> Send a dispute letter to the facility citing the specific CPT codes, the Medicare rates, and any billing errors you found. See our <a href="/fight-debt">debt dispute guide</a> for a template.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does cataract surgery cost without insurance in 2026?</h3>
        <p>Without insurance, cataract surgery costs $3,500 to $7,000 per eye for a standard procedure with a monofocal lens implant. The total includes the surgeon fee ($500&ndash;$1,500), facility fee ($1,500&ndash;$3,500), and the intraocular lens device. Ambulatory surgery centers are typically 30&ndash;40% cheaper than hospital outpatient departments for the same procedure.</p>
    </div>
    <div class="faq-item">
        <h3>Does Medicare cover cataract surgery?</h3>
        <p>Yes. Medicare Part B covers cataract surgery with a standard monofocal lens. You pay the annual Part B deductible ($257 in 2026) and 20% coinsurance. Medigap plans typically cover the 20%, bringing your cost to near zero. Medicare does not cover premium IOL upgrades or laser-assisted surgery add-ons.</p>
    </div>
    <div class="faq-item">
        <h3>Are premium IOL lenses covered by insurance?</h3>
        <p>No. Medicare and commercial insurers cover only a basic monofocal lens. Premium lenses&mdash;multifocal, extended depth-of-focus, toric, and light-adjustable&mdash;are patient-elected upgrades. The out-of-pocket cost ranges from $750 to $3,000 per eye depending on lens type. You should receive a written cost disclosure before agreeing to a premium lens.</p>
    </div>
    <div class="faq-item">
        <h3>What is the most common billing error in cataract surgery?</h3>
        <p>Upcoding CPT 66984 (routine cataract removal) to CPT 66982 (complex cataract removal) is the most frequent error. The complex code reimburses roughly 30% more than the routine code. If your surgeon&rsquo;s operative notes describe a straightforward procedure, billing 66982 is incorrect and the difference can be disputed.</p>
    </div>
    <div class="faq-item">
        <h3>Is laser cataract surgery covered by Medicare?</h3>
        <p>No. The femtosecond laser used in laser-assisted cataract surgery is considered a patient-elected upgrade. Medicare covers only the base surgical procedure. The laser add-on costs $500&ndash;$1,500 per eye and must be disclosed to you in writing before surgery as a non-covered charge.</p>
    </div>
</div>

<div class="cta-box" style="background:#f3f4f6;border:1px solid #d1d5db;border-radius:6px;padding:1.25rem 1.5rem;margin:2rem 0;">
    <strong>Received a cataract surgery bill you think is wrong?</strong><br>
    BillKarma finds billing errors in 26% of ophthalmology claims. Upload your bill and we&rsquo;ll flag every line item that doesn&rsquo;t add up&mdash;and show you exactly how to dispute it.
    <br><br>
    <a href="/fight-debt" style="background:#2563eb;color:#fff;padding:0.5rem 1.25rem;border-radius:4px;text-decoration:none;font-weight:600;">Fight your bill &rarr;</a>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule 2026 &mdash; Ophthalmology</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/ambulatory-surgical-center-asc" target="_blank" rel="noopener">CMS Ambulatory Surgical Center Payment System 2026</a></li>
    <li><a href="https://www.cms.gov/medicare/coverage/cataract" target="_blank" rel="noopener">CMS Medicare Coverage: Cataract Surgery and Intraocular Lenses</a></li>
    <li><a href="https://www.aao.org/eye-health/diseases/what-is-cataract" target="_blank" rel="noopener">American Academy of Ophthalmology: Cataract Overview</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/medicare-and-outpatient-prescription-drugs/" target="_blank" rel="noopener">KFF: Medicare Beneficiary Cost-Sharing and Medigap</a></li>
    <li><a href="https://www.healthaffairs.org/" target="_blank" rel="noopener">Health Affairs: Outpatient Surgical Facility Cost Differentials</a></li>
</ul>
""",
})
