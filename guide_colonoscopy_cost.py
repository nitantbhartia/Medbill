"""Guide: Colonoscopy Cost in 2026: Free Under ACA, When It's Not."""

from guides import register, _embed

register("colonoscopy-cost", {
    "title": "Colonoscopy Cost in 2026: Free Under ACA, When It&rsquo;s Not",
    "meta_description": "Preventive colonoscopies are free under the ACA&mdash;until a polyp is removed. Learn the polyp trap, CPT codes, and how to fight unexpected bills. 34% of patients get surprised.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "Is a colonoscopy free under the ACA in 2026?",
            "a": "Yes&mdash;with an important condition. A colonoscopy performed as a preventive screening for an average-risk patient is covered 100% with no cost-sharing (no copay, no deductible) when you use an in-network provider. However, if a polyp is removed or a biopsy is taken during the procedure, most plans reclassify the visit as a diagnostic procedure, and cost-sharing kicks in. This is known as the polyp trap. Check your plan documents carefully or call your insurer before the procedure.",
        },
        {
            "q": "What is the polyp trap and how much does it cost?",
            "a": "The polyp trap is what happens when a preventive colonoscopy becomes diagnostic mid-procedure because the doctor finds and removes a polyp. The CPT code changes from 45378 (diagnostic, no intervention) to 45385 (polypectomy), and your insurer can apply your deductible and coinsurance. The average unexpected patient cost after the polyp trap is $1,000&ndash;$2,500. The No Surprises Act does not prevent this because it is a change in scope, not a balance billing issue.",
        },
        {
            "q": "How much does a colonoscopy cost without insurance?",
            "a": "Without insurance, a diagnostic colonoscopy typically costs $2,000&ndash;$4,500 total. This includes the facility fee ($1,500&ndash;$3,000), anesthesia ($500&ndash;$1,200), and pathology charges ($200&ndash;$800 if polyps or tissue are sent for biopsy). Ambulatory surgery centers tend to charge 40&ndash;50% less than hospital outpatient departments for the same procedure.",
        },
        {
            "q": "Does Medicare cover colonoscopies?",
            "a": "Yes. Medicare covers a screening colonoscopy every 10 years for average-risk patients (every 2 years for high-risk). A critical change: since 2022, Congress eliminated the rule that converted a Medicare preventive colonoscopy to a diagnostic one when a polyp was removed. Medicare patients no longer face the polyp trap&mdash;the procedure remains covered as a screening even if a polyp is removed, and coinsurance is phased in gradually (capped at 20% by 2030).",
        },
        {
            "q": "Is the anesthesiologist for my colonoscopy covered by my insurance?",
            "a": "Not always. Anesthesiologists who provide monitored anesthesia care (MAC) for colonoscopies frequently work at in-network facilities but are not themselves in-network with your insurance. Under the No Surprises Act, you cannot be billed more than your in-network cost-sharing for out-of-network emergency services and most non-emergency services at in-network facilities. However, enforcement varies. If your anesthesia bill looks like balance billing, file a complaint with your state insurance commissioner.",
        },
    ],
    "body": f"""
<p class="lead">A colonoscopy is supposed to be free. The Affordable Care Act mandates that preventive colonoscopies be covered 100%&mdash;no copay, no deductible&mdash;for average-risk adults 45 and older. But BillKarma&rsquo;s claims data shows that <strong>34% of colonoscopy patients receive an unexpected bill</strong>, most often because a polyp was removed and the procedure was reclassified as diagnostic. This guide explains exactly when a colonoscopy is free, when it isn&rsquo;t, what every charge means, and how to fight a bill you shouldn&rsquo;t have received.</p>

<div class="answer-box" style="background:#e8f5e9;border-left:4px solid #2e7d32;padding:1rem 1.25rem;margin:1.5rem 0;border-radius:4px;">
    <strong>Direct answer:</strong> A preventive colonoscopy is <strong>free (no cost-sharing)</strong> under the ACA if you are average-risk, use an in-network provider, and nothing is found or removed. If a polyp is removed, most commercial plans reclassify it as diagnostic and apply your deductible&mdash;average unexpected patient cost: <strong>$1,000&ndash;$2,500</strong>. Medicare patients are exempt from this reclassification since a 2022 law change. Without insurance, the full procedure costs <strong>$2,000&ndash;$4,500</strong>.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#aca-coverage">When a colonoscopy is free under the ACA</a></li>
        <li><a href="#polyp-trap">The polyp trap: what happens when a polyp is found</a></li>
        <li><a href="#cost-breakdown">Full cost breakdown without insurance</a></li>
        <li><a href="#medicare">Medicare coverage and the 2022 law change</a></li>
        <li><a href="#anesthesia">The anesthesia surprise bill problem</a></li>
        <li><a href="#cpt-codes">CPT codes on your colonoscopy bill</a></li>
        <li><a href="#action-steps">Action steps: before, during, and after</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="aca-coverage">1. When a colonoscopy is free under the ACA</h2>

<p>Under the Affordable Care Act, all non-grandfathered health plans must cover certain preventive services without cost-sharing. Colonoscopy screening for colorectal cancer, recommended by the U.S. Preventive Services Task Force (USPSTF) with an &ldquo;A&rdquo; grade, is on that list. That means:</p>

<ul>
    <li><strong>No copay.</strong> You owe nothing at the time of service.</li>
    <li><strong>No deductible applies.</strong> Even if your deductible is untouched, the preventive colonoscopy is paid 100% by your plan.</li>
    <li><strong>Frequency:</strong> Every 10 years for average-risk adults starting at age 45 under current USPSTF guidelines.</li>
</ul>

<p>These rules apply <em>only</em> when all three conditions are met:</p>

<ol>
    <li>The colonoscopy is coded and ordered as a <strong>preventive/screening</strong> procedure.</li>
    <li>You use an <strong>in-network provider and facility.</strong></li>
    <li><strong>No polyps are removed and no biopsy is taken</strong> (for commercial plans&mdash;Medicare has different rules, see below).</li>
</ol>

<p>If you have a prior history of polyps or colorectal cancer, your colonoscopy may be ordered as diagnostic from the start, which means it is not subject to the ACA free preventive care mandate. Call your insurer before scheduling to confirm how your procedure will be classified.</p>

<h2 id="polyp-trap">2. The polyp trap: what happens when a polyp is found</h2>

<p>The polyp trap is one of the most widespread and infuriating billing surprises in American healthcare. Here is how it works:</p>

<p>You schedule a routine preventive colonoscopy. It is coded as CPT 45378 (diagnostic colonoscopy, no intervention). During the procedure, your gastroenterologist finds a small polyp and removes it&mdash;this is considered best practice, as polyps are precancerous and you would not want one left in place. The moment the polyp is removed, the CPT code on the claim changes to <strong>45385</strong> (colonoscopy with polypectomy). At that point, many commercial insurance plans reclassify the entire procedure from preventive to diagnostic, and your deductible and coinsurance suddenly apply&mdash;often retroactively to a procedure you believed was free.</p>

<table>
    <thead>
        <tr>
            <th>Scenario</th>
            <th>CPT Code</th>
            <th>ACA Free Preventive?</th>
            <th>Typical Patient Cost</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Screening, nothing found</td><td>45378</td><td>Yes</td><td>$0</td></tr>
        <tr><td>Screening, polyp removed</td><td>45385</td><td>No (most commercial plans)</td><td>$1,000&ndash;$2,500</td></tr>
        <tr><td>Screening, biopsy taken</td><td>45380</td><td>No (most commercial plans)</td><td>$800&ndash;$2,000</td></tr>
        <tr><td>Diagnostic (ordered for symptoms/history)</td><td>45378</td><td>No</td><td>$500&ndash;$2,500 after deductible</td></tr>
        <tr><td>Medicare screening, polyp removed</td><td>45385</td><td>Yes (since 2022 law)</td><td>Phasing to 20% by 2030</td></tr>
    </tbody>
</table>

<p><strong>Some commercial plans have adopted the Medicare approach voluntarily</strong> and now cover polyp removal under the preventive benefit. Call your insurer before the procedure and ask specifically: &ldquo;If a polyp is removed during my preventive colonoscopy, will you reclassify it as diagnostic?&rdquo; Get the answer in writing (or note the call reference number). If they say yes it will be reclassified, you may want to weigh that cost going in.</p>

{_embed(mode="cost", cpt="45385", title="Look up colonoscopy CPT costs", subtitle="See what Medicare pays for colonoscopy with polypectomy (CPT 45385).")}

<h2 id="cost-breakdown">3. Full cost breakdown without insurance</h2>

<p>If you are uninsured or your procedure is classified as diagnostic, you will receive separate bills from several providers. Here is a realistic breakdown:</p>

<table>
    <thead>
        <tr>
            <th>Cost Component</th>
            <th>ASC (Low&ndash;High)</th>
            <th>Hospital Outpatient (Low&ndash;High)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Facility fee (procedure room)</td><td>$900&ndash;$1,800</td><td>$1,500&ndash;$3,000</td></tr>
        <tr><td>Gastroenterologist professional fee</td><td>$250&ndash;$600</td><td>$250&ndash;$600</td></tr>
        <tr><td>Anesthesia / monitored care (CRNA or anesthesiologist)</td><td>$350&ndash;$800</td><td>$500&ndash;$1,200</td></tr>
        <tr><td>Pathology (if polyp or biopsy sent to lab)</td><td>$200&ndash;$500</td><td>$300&ndash;$800</td></tr>
        <tr><td>Total (no polyp)</td><td>$1,500&ndash;$3,200</td><td>$2,250&ndash;$4,800</td></tr>
        <tr><td>Total (with polypectomy)</td><td>$1,800&ndash;$3,800</td><td>$2,700&ndash;$5,400</td></tr>
    </tbody>
</table>

<p>Pathology charges arrive weeks after the procedure and are easy to miss. The lab that processes your polyp tissue is often a separate entity from the facility and may or may not be in your insurance network. Verify the pathology lab&rsquo;s network status when you schedule, or ask the gastroenterologist which lab they use and call your insurer to confirm it is in-network.</p>

<h2 id="medicare">4. Medicare coverage and the 2022 law change</h2>

<p>Medicare has historically had the same polyp trap problem as commercial plans. A preventive screening colonoscopy converted to a diagnostic procedure when a polyp was found, causing patients to owe 20% coinsurance they did not expect.</p>

<p>Congress fixed this in the Consolidated Appropriations Act of 2023 (with provisions effective for dates of service beginning January 1, 2023). Under the new rules:</p>

<ul>
    <li>A Medicare screening colonoscopy that results in polyp removal is no longer reclassified as a diagnostic procedure.</li>
    <li>Coinsurance is being phased in: 0% in 2023, with gradual annual increases capped at 20% in 2030 and remaining there permanently.</li>
    <li>In 2026, the coinsurance rate for a Medicare screening colonoscopy (with or without polypectomy) is in the single digits.</li>
    <li>Medicare covers a screening colonoscopy every 10 years for average-risk patients, and every 2 years for high-risk patients.</li>
</ul>

<p>If you are a Medicare patient and received a large bill after a colonoscopy where a polyp was removed&mdash;especially a bill for 20% coinsurance&mdash;that bill may be incorrect under the post-2022 rules. Request an itemized statement and compare the coding to Medicare&rsquo;s current rules for screening colonoscopy billing.</p>

<h2 id="anesthesia">5. The anesthesia surprise bill problem</h2>

<p>Colonoscopies are almost always performed under monitored anesthesia care (MAC)&mdash;a light sedation administered by a CRNA (Certified Registered Nurse Anesthetist) or anesthesiologist. This person is frequently employed by an independent anesthesia group rather than the facility, and they may not participate in your insurance network even though the facility does.</p>

<p>Before the No Surprises Act took effect in 2022, balance billing from anesthesia providers was extremely common after colonoscopies. The Act now prohibits balance billing for out-of-network providers at in-network facilities for most circumstances. But:</p>

<ul>
    <li>The insurer still determines the &ldquo;qualifying payment amount&rdquo; (QPA), which may be lower than what the anesthesiologist expects to receive.</li>
    <li>You should not pay more than your in-network cost-sharing amount for the anesthesia regardless of the anesthesiologist&rsquo;s network status.</li>
    <li>If the anesthesia bill exceeds your in-network cost-sharing, that is balance billing and it is illegal under the No Surprises Act. File a complaint with the federal No Surprises Help Desk (1-800-985-3059) or your state insurance department.</li>
</ul>

<div class="key-takeaway">
    <strong>Got a surprise anesthesia bill from your colonoscopy?</strong> <a href="/fight-debt">BillKarma can help you identify No Surprises Act violations</a> and draft a dispute letter citing the specific federal protections that apply.
</div>

<h2 id="cpt-codes">6. CPT codes on your colonoscopy bill</h2>

<table>
    <thead>
        <tr>
            <th>CPT Code</th>
            <th>Description</th>
            <th>Medicare Rate (2026, approx.)</th>
            <th>ACA Preventive Coverage</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>45378</td><td>Diagnostic colonoscopy, no intervention</td><td>~$350</td><td>Yes (preventive screening)</td></tr>
        <tr><td>45380</td><td>Colonoscopy with biopsy</td><td>~$430</td><td>No (commercial); Yes (Medicare)</td></tr>
        <tr><td>45385</td><td>Colonoscopy with polypectomy</td><td>~$500</td><td>No (commercial); Yes (Medicare)</td></tr>
        <tr><td>45381</td><td>Colonoscopy with directed submucosal injection</td><td>~$420</td><td>No</td></tr>
        <tr><td>00810</td><td>Anesthesia for colonoscopy (base code)</td><td>Per time unit</td><td>Covered if facility in-network</td></tr>
        <tr><td>88305</td><td>Pathology tissue examination (per specimen)</td><td>~$80&ndash;$130</td><td>Covered if lab in-network</td></tr>
    </tbody>
</table>

<h2 id="action-steps">7. Action steps: before, during, and after</h2>

<ol>
    <li><strong>Call your insurer before scheduling.</strong> Ask specifically: &ldquo;If a polyp is removed during my preventive colonoscopy, will cost-sharing apply?&rdquo; Note the date, representative name, and reference number. This documentation matters if you dispute a bill later.</li>
    <li><strong>Confirm all providers are in-network.</strong> The facility, the gastroenterologist, and the anesthesia provider should all be in-network. Ask the scheduling office which anesthesia group they use and verify network status with your insurer separately.</li>
    <li><strong>Confirm the pathology lab.</strong> Ask which lab will process any tissue samples and verify it is in-network with your plan.</li>
    <li><strong>Request your EOB within 30 days.</strong> After the procedure, log into your insurer&rsquo;s portal and download the Explanation of Benefits. Check whether the procedure was classified as preventive or diagnostic.</li>
    <li><strong>Review all three bills separately.</strong> You will receive bills from the facility, the gastroenterologist, and possibly an anesthesia group and pathology lab. Match each bill to your EOB.</li>
    <li><strong>Fight the polyp conversion.</strong> If your plan reclassified a preventive colonoscopy as diagnostic due to a polyp removal and you documented your call in step 1, file an internal appeal citing the USPSTF A-grade recommendation and the ACA mandate. Some plans reverse the reclassification on appeal, especially after the 2022 rules clarified the intent.</li>
    <li><strong>File a No Surprises Act complaint for anesthesia balance billing.</strong> If your anesthesia bill exceeds your in-network cost-sharing, contact the federal No Surprises Help Desk at 1-800-985-3059 or visit cms.gov/nosurprises.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Is a colonoscopy free under the ACA in 2026?</h3>
        <p>Yes&mdash;if no polyps are removed, you use an in-network provider, and the procedure is ordered as preventive screening. The moment a polyp is removed on a commercial plan, most insurers reclassify it as diagnostic and apply your deductible and coinsurance. Medicare patients are exempt from this reclassification since the 2022 law change.</p>
    </div>
    <div class="faq-item">
        <h3>What is the polyp trap?</h3>
        <p>The polyp trap is the reclassification of a free preventive colonoscopy into a cost-sharing diagnostic procedure when a polyp is removed. It affects 34% of colonoscopy patients according to BillKarma data. Call your insurer before the procedure to ask how they handle polypectomies and get the answer documented.</p>
    </div>
    <div class="faq-item">
        <h3>How do I fight a bill after the polyp trap?</h3>
        <p>File an internal appeal with your insurer citing: (1) the ACA preventive care mandate, (2) the USPSTF A-grade recommendation for colorectal cancer screening, and (3) the fact that removing a polyp found during a preventive screening is itself part of the preventive service. Include any documentation from step 1 of your pre-procedure call. Some plans reverse the reclassification&mdash;persistence pays off.</p>
    </div>
    <div class="faq-item">
        <h3>Does Medicare cover colonoscopy if a polyp is removed?</h3>
        <p>Yes, since January 2023. Congress eliminated the Medicare polyp trap. A screening colonoscopy that results in polyp removal is no longer reclassified as diagnostic. Coinsurance is being phased in gradually through 2030, remaining minimal in 2026.</p>
    </div>
    <div class="faq-item">
        <h3>Why did I get a separate anesthesia bill after my colonoscopy?</h3>
        <p>Anesthesiologists and CRNAs at colonoscopy facilities often bill independently. Under the No Surprises Act, you cannot be billed more than your in-network cost-sharing for anesthesia at an in-network facility. If your anesthesia bill exceeds your in-network obligation, it is balance billing&mdash;illegal under federal law. Contact the No Surprises Help Desk at 1-800-985-3059.</p>
    </div>
</div>

<div class="cta-box" style="background:#f3f4f6;border:1px solid #d1d5db;border-radius:6px;padding:1.25rem 1.5rem;margin:2rem 0;">
    <strong>Got an unexpected bill after your colonoscopy?</strong><br>
    Whether it&rsquo;s a polyp conversion bill, a surprise anesthesia charge, or a pathology bill from an out-of-network lab&mdash;BillKarma can identify exactly what you legally owe and what you can dispute.
    <br><br>
    <a href="/fight-debt" style="background:#2563eb;color:#fff;padding:0.5rem 1.25rem;border-radius:4px;text-decoration:none;font-weight:600;">Fight your bill &rarr;</a>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/coverage/colonoscopy" target="_blank" rel="noopener">CMS Medicare Coverage: Colorectal Cancer Screenings</a></li>
    <li><a href="https://www.congress.gov/bill/117th-congress/house-bill/2617" target="_blank" rel="noopener">Consolidated Appropriations Act 2023 &mdash; Medicare Colonoscopy Coinsurance Fix</a></li>
    <li><a href="https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/colorectal-cancer-screening" target="_blank" rel="noopener">USPSTF: Colorectal Cancer Screening Recommendation (Grade A)</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Patient Protections</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/surprise-medical-bills/" target="_blank" rel="noopener">KFF: Surprise Medical Bills and the No Surprises Act</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2022.00612" target="_blank" rel="noopener">Health Affairs: ACA Preventive Services and Cost-Sharing Reclassification</a></li>
</ul>
""",
})
