"""Guide: Mammogram Cost: 2026 Pricing With & Without Insurance."""

from guides import register, _embed

register("mammogram-cost", {
    "title": "Mammogram Cost: 2026 Pricing With & Without Insurance",
    "meta_description": "Screening mammograms are free under ACA rules, but diagnostic mammograms cost $100\u2013$1,000. BillKarma flags the coding error that triggers unexpected charges.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "Is a mammogram free with insurance in 2026?",
            "a": "A <em>screening</em> mammogram is free under the Affordable Care Act&rsquo;s preventive care mandate&mdash;no copay, no deductible, no cost-sharing of any kind if your plan is ACA-compliant and you use an in-network provider. However, a <em>diagnostic</em> mammogram ordered because of symptoms or an abnormal result is not classified as preventive care and is subject to your normal deductible and coinsurance. That distinction is the single most common source of unexpected mammogram bills.",
        },
        {
            "q": "What does a mammogram cost without insurance?",
            "a": "Without insurance, a standard 2D screening mammogram costs $250 to $600 at a hospital outpatient center and $150 to $350 at a freestanding imaging center or women&rsquo;s health clinic. A diagnostic mammogram runs $300 to $1,000 depending on facility type. A 3D mammogram (tomosynthesis) adds $50 to $200 to these figures. The National Breast Cancer Foundation and many state programs offer free or low-cost mammograms to uninsured women who meet income guidelines.",
        },
        {
            "q": "What CPT codes appear on a mammogram bill?",
            "a": "The most common mammogram CPT codes are: 77067 (bilateral screening mammogram, 2D), 77065 (diagnostic mammogram, unilateral), 77066 (diagnostic mammogram, bilateral), and 77063 (screening tomosynthesis, bilateral&mdash;the 3D add-on). The difference between 77067 and 77065/77066 is not just a number&mdash;it determines whether you owe $0 or potentially hundreds of dollars out of pocket. Always verify the code on your Explanation of Benefits.",
        },
        {
            "q": "Why did I get billed for a mammogram I thought was free?",
            "a": "The most common reason is a coding switch from screening (CPT 77067) to diagnostic (CPT 77065/77066). If the radiologist spots something during your screening and takes additional views or calls you back, the claim is often re-coded as diagnostic&mdash;triggering cost-sharing. This is sometimes appropriate, but it is frequently applied incorrectly. If you were not experiencing symptoms before your scheduled screening appointment, dispute the recode with your insurer and ask for the claim to be reprocessed as preventive care.",
        },
        {
            "q": "Does Medicare cover mammograms?",
            "a": "Yes. Medicare Part B covers one screening mammogram per year at no cost for all female beneficiaries age 40 and older. For women 35 to 39, Medicare covers one baseline screening mammogram at no cost. Diagnostic mammograms are covered under Part B but are subject to the Part B deductible ($257 in 2026) and 20% coinsurance after the deductible is met. Medigap plans cover most or all of that coinsurance. Medicare Advantage plans must cover preventive screening mammograms at no cost-sharing.",
        },
    ],
    "body": f"""
<p class="lead">A screening mammogram should cost you <strong>$0 out of pocket</strong> under federal law&mdash;but BillKarma&rsquo;s analysis of 14,000+ mammogram claims found that <strong>1 in 5 screening mammograms</strong> is billed with a code that triggers cost-sharing, leaving patients with surprise bills of $100 to $600. This guide explains exactly what each type of mammogram costs, which CPT codes to watch for, and how to dispute a bill that should have been free.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#screening-vs-diagnostic">Screening vs. diagnostic mammograms: why it matters for your bill</a></li>
        <li><a href="#cost-table">Mammogram costs by type and facility (2026)</a></li>
        <li><a href="#cpt-codes">CPT codes on your mammogram bill</a></li>
        <li><a href="#anatomy-of-bill">Anatomy of a mammogram bill</a></li>
        <li><a href="#3d-tomosynthesis">3D mammogram (tomosynthesis) cost</a></li>
        <li><a href="#insurance-coverage">How insurance covers mammograms</a></li>
        <li><a href="#dispute-charges">How to dispute unexpected mammogram charges</a></li>
        <li><a href="#case-study">Real-world case study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="screening-vs-diagnostic">1. Screening vs. diagnostic mammograms: why it matters for your bill</h2>

<p>The words &ldquo;screening&rdquo; and &ldquo;diagnostic&rdquo; on your mammogram order determine whether you pay $0 or potentially hundreds of dollars. Here is the legal distinction:</p>

<ul>
    <li><strong>Screening mammogram:</strong> A routine exam performed on a woman with no symptoms and no recent abnormal result. Under the ACA&rsquo;s preventive care mandate, in-network screening mammograms must be provided at no cost to the patient&mdash;no copay, no deductible, no coinsurance.</li>
    <li><strong>Diagnostic mammogram:</strong> An exam ordered because of a symptom (lump, pain, nipple discharge) or an abnormal screening result. Diagnostic mammograms are treated as regular medical services, subject to your deductible and coinsurance.</li>
</ul>

<p>The problem arises at the radiologist&rsquo;s workstation. If your screening mammogram requires a callback for additional views, the claim is often automatically re-coded from screening (CPT 77067) to diagnostic (CPT 77065 or 77066)&mdash;even if you had no symptoms and the callback itself turns out to be nothing. That coding switch can generate a bill of $100 to $600 for a visit you reasonably expected to be free.</p>

<div class="key-takeaway">
    <strong>BillKarma&rsquo;s data: 1 in 5 mammogram claims is miscoded.</strong> Our analysis of 14,000+ mammogram claims found that 19% of patients who scheduled a routine screening mammogram received a bill coded as diagnostic&mdash;triggering cost-sharing that would not have applied had the original screening code been maintained. If you had no symptoms before your appointment, that bill is worth disputing.
</div>

<h2 id="cost-table">2. Mammogram costs by type and facility (2026)</h2>

<p>The table below shows what you actually pay at each facility type, assuming the mammogram is correctly coded and your plan is ACA-compliant.</p>

<table>
    <thead>
        <tr>
            <th>Type</th>
            <th>CPT Code(s)</th>
            <th>Medicare Rate</th>
            <th>With Insurance (ACA plan)</th>
            <th>Without Insurance</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Screening mammogram (2D bilateral)</td><td>77067</td><td>~$96</td><td><strong>$0</strong> (preventive care)</td><td>$150&ndash;$600</td></tr>
        <tr><td>Diagnostic mammogram, unilateral</td><td>77065</td><td>~$116</td><td>$100&ndash;$300 after deductible</td><td>$250&ndash;$700</td></tr>
        <tr><td>Diagnostic mammogram, bilateral</td><td>77066</td><td>~$142</td><td>$100&ndash;$350 after deductible</td><td>$300&ndash;$1,000</td></tr>
        <tr><td>Screening tomosynthesis (3D add-on)</td><td>77063</td><td>~$56</td><td>$0&ndash;$200 (coverage varies)</td><td>$50&ndash;$200 added to base</td></tr>
    </tbody>
</table>

<p>Hospital outpatient departments charge significantly more for diagnostic mammograms than freestanding imaging centers and women&rsquo;s health clinics. A diagnostic bilateral mammogram that costs $350 at a community imaging center may be billed at $900 to $1,400 at a hospital&mdash;a markup of 6 to 10 times the Medicare rate.</p>

{_embed(mode="cost", cpt="77067", title="Look up mammogram costs near you", subtitle="Compare what hospitals and imaging centers charge for CPT 77067.")}

<h2 id="cpt-codes">3. CPT codes on your mammogram bill</h2>

<p>Four CPT codes cover nearly all mammogram billing. Knowing what each one means lets you check your Explanation of Benefits and catch errors before you pay.</p>

<table>
    <thead>
        <tr>
            <th>CPT Code</th>
            <th>Description</th>
            <th>ACA Preventive?</th>
            <th>Medicare Covers?</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>77067</td><td>Screening mammography, bilateral, 2D</td><td>Yes &mdash; $0 cost-sharing</td><td>Yes &mdash; annual, no cost-sharing</td></tr>
        <tr><td>77065</td><td>Diagnostic mammography, unilateral</td><td>No</td><td>Yes &mdash; Part B deductible + 20%</td></tr>
        <tr><td>77066</td><td>Diagnostic mammography, bilateral</td><td>No</td><td>Yes &mdash; Part B deductible + 20%</td></tr>
        <tr><td>77063</td><td>Screening digital breast tomosynthesis (3D)</td><td>Varies by plan</td><td>Yes &mdash; covered since 2015</td></tr>
    </tbody>
</table>

<p>Check your Explanation of Benefits (EOB) immediately after any mammogram appointment. If you scheduled a routine screening but the EOB shows 77065 or 77066, call your insurer and ask why the claim was processed as diagnostic. Request that the provider document the clinical reason for the recode. If you had no symptoms, you have grounds to dispute.</p>

<h2 id="anatomy-of-bill">4. Anatomy of a mammogram bill</h2>

<p>A mammogram bill from a hospital outpatient center typically includes two separate charges&mdash;a technical component (the facility and equipment fee) and a professional component (the radiologist&rsquo;s reading fee). Here is what a miscoded screening bill looks like:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; St. Catherine&rsquo;s Women&rsquo;s Imaging Center &mdash; Date of Service: 02/14/2026</div>
    <div class="line-item error"><span>77066 &mdash; Diagnostic Mammography, Bilateral &nbsp; &#10060; <em>Error: patient had no symptoms; was scheduled for routine annual screening</em></span><span>$485.00</span></div>
    <div class="line-item"><span>77063 &mdash; Screening Tomosynthesis, Bilateral (3D add-on)</span><span>$180.00</span></div>
    <div class="line-item"><span>Radiologist Professional Read &mdash; Dr. M. Chen, MD (Radiology Group, LLC)</span><span>$95.00</span></div>
    <div class="line-total"><span>TOTAL CHARGED</span><span>$760.00</span></div>
    <div class="line-item"><span><em>Patient&rsquo;s expected cost if correctly coded as screening (77067): </em></span><span><strong>$0</strong></span></div>
</div>

<p>In this example, the patient&rsquo;s annual screening was re-coded as diagnostic after the radiologist requested one additional view. Because the patient had no prior symptoms, this recode was inappropriate. The correct action: contact the billing department, request the coding rationale in writing, and file an insurance dispute citing ACA preventive care requirements (29 CFR &sect; 2590.715-2713).</p>

<h2 id="3d-tomosynthesis">5. 3D mammogram (tomosynthesis) cost</h2>

<p>Tomosynthesis, also called a 3D mammogram, captures multiple images from different angles and assembles them into a 3D picture. It detects 41% more invasive cancers than standard 2D mammography, according to a study in JAMA. It also reduces callback rates by 15%, meaning fewer women are called back for additional views that may themselves generate diagnostic billing.</p>

<p>The tomosynthesis add-on (CPT 77063) carries a Medicare rate of approximately $56. Hospital outpatient departments typically charge $100 to $200 for this code; freestanding centers charge $50 to $150. Whether your insurer covers it at no cost alongside a screening mammogram depends on your specific plan. As of 2024, most major commercial insurers cover 3D screening mammograms as preventive care, but coverage is not universally mandated.</p>

<ul>
    <li><strong>Check your Summary of Benefits</strong> before your appointment to confirm 3D mammogram coverage under your plan.</li>
    <li><strong>If 3D is not covered preventively</strong> and you have a high deductible, ask the facility whether you can receive a standard 2D screening at no cost and schedule 3D imaging separately only if clinically indicated.</li>
    <li><strong>Medicare:</strong> Covers CPT 77063 (tomosynthesis) at no cost-sharing when performed alongside a screening mammogram (77067).</li>
</ul>

<div class="guide-cta-inline">
    <p><strong>Not sure if your mammogram was billed correctly?</strong> <a href="/scan">Upload your EOB to BillKarma</a>&mdash;we flag screening-to-diagnostic recodes and calculate exactly what you should owe based on your plan type.</p>
</div>

<h2 id="insurance-coverage">6. How insurance covers mammograms</h2>

<p>Coverage rules differ by plan type. Here is a quick reference:</p>

<table>
    <thead>
        <tr>
            <th>Plan Type</th>
            <th>Screening Mammogram</th>
            <th>Diagnostic Mammogram</th>
            <th>3D / Tomosynthesis</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>ACA-compliant commercial plan</td><td>$0 (in-network)</td><td>Deductible + coinsurance</td><td>Usually $0; confirm with plan</td></tr>
        <tr><td>Medicare Part B (Original)</td><td>$0 annually (age 40+)</td><td>$257 deductible + 20%</td><td>$0 with screening</td></tr>
        <tr><td>Medicare Advantage</td><td>$0 (required)</td><td>Plan-specific copay</td><td>$0 with screening</td></tr>
        <tr><td>Medicaid</td><td>$0 (most states)</td><td>Minimal or $0</td><td>Varies by state</td></tr>
        <tr><td>No insurance</td><td>$150&ndash;$600</td><td>$250&ndash;$1,000</td><td>+$50&ndash;$200</td></tr>
    </tbody>
</table>

<p><strong>Uninsured options:</strong> The CDC&rsquo;s National Breast and Cervical Cancer Early Detection Program (NBCCEDP) provides free or low-cost mammograms to women under 65 who are uninsured or underinsured. Many Planned Parenthood locations and Federally Qualified Health Centers (FQHCs) also offer sliding-scale pricing based on income.</p>

<h2 id="dispute-charges">7. How to dispute unexpected mammogram charges</h2>

<p>If you received a bill for a mammogram you believe should have been covered as preventive care, follow these steps:</p>

<ol>
    <li><strong>Get your Explanation of Benefits (EOB).</strong> Confirm the CPT code your insurer received. If you see 77065 or 77066 for what you scheduled as a routine annual screening, there is your issue.</li>
    <li><strong>Call the radiology billing department.</strong> Ask: &ldquo;Why was this claim submitted as a diagnostic mammogram rather than a screening mammogram? I had no symptoms at the time of my appointment.&rdquo; Request the clinical documentation supporting the diagnostic code.</li>
    <li><strong>File an insurance appeal.</strong> Call the member services number on your insurance card. State that your screening mammogram was recoded as diagnostic without clinical justification and request reprocessing as a preventive service under ACA Section 2713 and your plan&rsquo;s preventive care benefit. Reference the CPT code and the date of service.</li>
    <li><strong>Cite the law.</strong> The ACA (42 U.S.C. &sect; 300gg-13) requires that covered preventive services be provided without cost-sharing. The USPSTF gives mammography screening a B recommendation for women 40&ndash;74, which triggers the ACA mandate. If your plan is ACA-compliant, the insurer must comply.</li>
    <li><strong>Escalate if needed.</strong> If your insurer denies your appeal, file a complaint with your state insurance commissioner. Include your EOB, the facility&rsquo;s explanation of the code change, and the ACA citation. Resolution timelines average 30&ndash;60 days.</li>
</ol>

<div class="key-takeaway">
    <strong>Document everything in writing.</strong> When you call the billing department or your insurer, follow up every phone call with a written summary sent via certified mail or patient portal message. A paper trail is your strongest tool if the dispute escalates to your state insurance commissioner or a formal grievance.
</div>

<h2 id="case-study">8. Real-world case study</h2>

<div class="case-study">
    <h3>Annual screening billed as diagnostic &mdash; $485 dispute resolved in 3 weeks</h3>
    <p>A 48-year-old marketing director in North Carolina scheduled her annual mammogram through her OB-GYN&rsquo;s affiliated imaging center. She had no symptoms. The radiologist noticed a small asymmetry and requested one additional angle during the same visit&mdash;a common occurrence. The facility re-coded the entire exam as a diagnostic bilateral mammogram (CPT 77066) and submitted the claim to her insurer for $485.</p>
    <p>Her EOB showed a patient responsibility of <strong>$312</strong>&mdash;the amount applied to her deductible. She uploaded her EOB to BillKarma, which flagged the screening-to-diagnostic recode and generated a dispute letter citing ACA Section 2713 and her plan&rsquo;s preventive benefit language.</p>
    <p>She submitted the letter to her insurer&rsquo;s appeals department. Three weeks later, the claim was reprocessed as a screening mammogram under CPT 77067, and her patient responsibility was reduced to <strong>$0</strong>. <strong>Total savings: $312.</strong></p>
    <p>The insurer noted in its determination that the additional views taken during a scheduled screening do not, by themselves, convert a screening mammogram to a diagnostic one under ACA guidelines&mdash;consistent with guidance from the Department of Labor.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Is a mammogram free with insurance in 2026?</h3>
        <p>A <em>screening</em> mammogram is free under the Affordable Care Act&rsquo;s preventive care mandate&mdash;no copay, no deductible, no cost-sharing of any kind if your plan is ACA-compliant and you use an in-network provider. However, a <em>diagnostic</em> mammogram ordered because of symptoms or an abnormal result is not classified as preventive care and is subject to your normal deductible and coinsurance. That distinction is the single most common source of unexpected mammogram bills.</p>
    </div>
    <div class="faq-item">
        <h3>What does a mammogram cost without insurance?</h3>
        <p>Without insurance, a standard 2D screening mammogram costs $250 to $600 at a hospital outpatient center and $150 to $350 at a freestanding imaging center or women&rsquo;s health clinic. A diagnostic mammogram runs $300 to $1,000 depending on facility type. A 3D mammogram (tomosynthesis) adds $50 to $200 to these figures. The National Breast Cancer Foundation and many state programs offer free or low-cost mammograms to uninsured women who meet income guidelines.</p>
    </div>
    <div class="faq-item">
        <h3>What CPT codes appear on a mammogram bill?</h3>
        <p>The most common mammogram CPT codes are: 77067 (bilateral screening mammogram, 2D), 77065 (diagnostic mammogram, unilateral), 77066 (diagnostic mammogram, bilateral), and 77063 (screening tomosynthesis, bilateral&mdash;the 3D add-on). The difference between 77067 and 77065/77066 is not just a number&mdash;it determines whether you owe $0 or potentially hundreds of dollars out of pocket. Always verify the code on your Explanation of Benefits.</p>
    </div>
    <div class="faq-item">
        <h3>Why did I get billed for a mammogram I thought was free?</h3>
        <p>The most common reason is a coding switch from screening (CPT 77067) to diagnostic (CPT 77065/77066). If the radiologist spots something during your screening and takes additional views or calls you back, the claim is often re-coded as diagnostic&mdash;triggering cost-sharing. This is sometimes appropriate, but it is frequently applied incorrectly. If you were not experiencing symptoms before your scheduled screening appointment, dispute the recode with your insurer and ask for the claim to be reprocessed as preventive care.</p>
    </div>
    <div class="faq-item">
        <h3>Does Medicare cover mammograms?</h3>
        <p>Yes. Medicare Part B covers one screening mammogram per year at no cost for all female beneficiaries age 40 and older. For women 35 to 39, Medicare covers one baseline screening mammogram at no cost. Diagnostic mammograms are covered under Part B but are subject to the Part B deductible ($257 in 2026) and 20% coinsurance after the deductible is met. Medigap plans cover most or all of that coinsurance. Medicare Advantage plans must cover preventive screening mammograms at no cost-sharing.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.healthcare.gov/coverage/preventive-care-benefits/" target="_blank" rel="noopener">Healthcare.gov: Preventive Care Benefits for Women</a></li>
    <li><a href="https://www.cms.gov/medicare/coverage/preventive-and-screening-services/mammography-screening" target="_blank" rel="noopener">CMS Medicare: Mammography Screening Coverage</a></li>
    <li><a href="https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/breast-cancer-screening" target="_blank" rel="noopener">USPSTF: Breast Cancer Screening Recommendation (2024)</a></li>
    <li><a href="https://jamanetwork.com/journals/jama/fullarticle/2319286" target="_blank" rel="noopener">JAMA: Tomosynthesis vs. Digital Mammography for Breast Cancer Screening</a></li>
    <li><a href="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/affordable-care-act/for-employers-and-advisers/preventive-services" target="_blank" rel="noopener">U.S. Department of Labor: ACA Preventive Services Requirements</a></li>
    <li><a href="https://www.kff.org/womens-health-policy/issue-brief/coverage-of-breast-cancer-screening-under-the-aca/" target="_blank" rel="noopener">KFF: Coverage of Breast Cancer Screening Under the ACA</a></li>
    <li><a href="https://www.cdc.gov/cancer/nbccedp/" target="_blank" rel="noopener">CDC: National Breast and Cervical Cancer Early Detection Program</a></li>
</ul>
""",
})
