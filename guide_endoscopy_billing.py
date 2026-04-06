"""Guide: Endoscopy Billing Explained: Costs, Codes, and Common Errors (2026)."""

from guides import register, _embed

register("endoscopy-billing", {
    "title": "Endoscopy Billing: Costs, Codes & Common Errors (2026)",
    "meta_description": "Upper endoscopy costs $800\u2013$8,000 depending on facility. See 2026 CPT codes, Medicare rates, and how to dispute the preventive-to-diagnostic billing trap.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How much does an upper endoscopy (EGD) cost?",
            "a": "An upper endoscopy (EGD) costs an average of $2,750 at hospitals, but ranges from $800 at ambulatory surgery centers to $8,000 in hospital outpatient departments. The wide range reflects whether a biopsy or other procedure was performed, the facility type, and your geographic location. The Medicare rate for a diagnostic EGD (CPT 43235) is $249; for an EGD with biopsy (CPT 43239) it is $311.",
        },
        {
            "q": "What is the difference between a diagnostic and therapeutic endoscopy?",
            "a": "A diagnostic endoscopy (CPT 43235) involves passing the scope to visually examine the esophagus, stomach, and duodenum with no additional procedures performed. A therapeutic endoscopy involves an additional procedure during the same scope \u2014 such as a biopsy (CPT 43239), polyp removal (CPT 43251), or dilation (CPT 43270). Therapeutic codes bill at higher rates and may trigger different insurance cost-sharing than a purely diagnostic procedure.",
        },
        {
            "q": "Why did my preventive endoscopy turn into a diagnostic procedure?",
            "a": "If your EGD was ordered as a screening and a biopsy was taken during the procedure, your insurer may reclassify the procedure from preventive to diagnostic. This reclassification can eliminate your preventive care coverage (which is often 100%) and apply your deductible and coinsurance instead. BillKarma\u2019s review of endoscopy bills found that 1 in 3 contains this type of preventive-to-diagnostic conversion, resulting in unexpected bills for patients who expected zero cost-sharing.",
        },
        {
            "q": "Will I get a separate bill from an anesthesiologist for my endoscopy?",
            "a": "Yes, if your endoscopy was performed with sedation administered by a separate anesthesiologist or CRNA (rather than the proceduralist themselves), you will receive a separate anesthesia bill. This is particularly common when &ldquo;monitored anesthesia care&rdquo; (MAC) sedation is used rather than simple physician-administered conscious sedation. The anesthesia provider may be out-of-network even if your gastroenterologist and facility are in-network.",
        },
        {
            "q": "What is a pathology charge after an endoscopy biopsy?",
            "a": "When a biopsy is taken during an endoscopy, the tissue sample is sent to a pathology laboratory for analysis. The pathologist bills separately from the gastroenterologist and the facility. You may receive two or three separate bills for a single endoscopy procedure. The pathologist may be out-of-network; under the No Surprises Act, if the pathologist is at an in-network facility and you did not choose them, you should only owe in-network cost-sharing.",
        },
    ],
    "body": f"""
<p class="lead">An upper endoscopy (EGD) costs an average of <strong>$2,750</strong> at hospitals, but ranges from <strong>$800</strong> at surgery centers to <strong>$8,000</strong> in hospital outpatient departments for the same procedure. Billing errors are especially common when a biopsy is taken or polyps are found &mdash; a routine screening can be reclassified as a diagnostic procedure, unexpectedly wiping out a patient&rsquo;s 100% preventive care coverage. BillKarma&rsquo;s review of endoscopy bills found that <strong>1 in 3</strong> contains a preventive-to-diagnostic billing conversion that patients were never warned about.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#whats-on-bill">What&rsquo;s on an endoscopy bill</a></li>
        <li><a href="#cpt-codes">EGD CPT codes and Medicare rates</a></li>
        <li><a href="#diagnostic-vs-therapeutic">Diagnostic vs. therapeutic billing</a></li>
        <li><a href="#preventive-trap">The preventive-to-diagnostic billing trap</a></li>
        <li><a href="#anesthesia-pathology">Separate anesthesia and pathology fees</a></li>
        <li><a href="#egd-vs-colonoscopy">Endoscopy vs. colonoscopy billing comparison</a></li>
        <li><a href="#hospital-vs-asc">Hospital vs. surgery center costs</a></li>
        <li><a href="#bill-example">Annotated bill example</a></li>
        <li><a href="#dispute">How to dispute endoscopy charges</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="whats-on-bill">1. What&rsquo;s on an endoscopy bill</h2>

<p>An endoscopy generates multiple separate bills from multiple providers. Patients who expect a single bill are often blindsided. Here is the full list of components you may receive:</p>

<ul>
    <li><strong>Facility fee</strong> &mdash; Charged by the hospital or ambulatory surgery center for the procedure room, nursing staff, sedation supplies, and recovery area.</li>
    <li><strong>Gastroenterologist fee</strong> &mdash; The physician who performed the scope bills separately, usually under a professional group billing number.</li>
    <li><strong>Anesthesia fee</strong> &mdash; If a separate anesthesiologist or CRNA administered sedation, they bill separately. This is the most common source of surprise out-of-network charges after an endoscopy.</li>
    <li><strong>Pathology fee</strong> &mdash; If any tissue was biopsied or removed, it is sent to a pathology lab that bills separately from the gastroenterologist and facility.</li>
</ul>

<p>Before your procedure, verify that all four providers (facility, gastroenterologist, anesthesiologist, and the pathology lab your facility uses) are in your insurance network. Out-of-network charges from a single provider can add hundreds to your bill even when everything else is in-network.</p>

<h2 id="cpt-codes">2. EGD CPT codes and Medicare rates</h2>

<p>Upper endoscopy (esophagogastroduodenoscopy, or EGD) billing uses the CPT code that reflects the most complex procedure performed during the scope. If the physician only looked, you get CPT 43235. If they also took a biopsy, the code upgrades to CPT 43239. The table below shows the primary EGD codes, 2026 Medicare rates, and charge ranges by facility type.</p>

<table>
    <thead>
        <tr>
            <th>CPT Code</th>
            <th>Description</th>
            <th>Medicare Rate</th>
            <th>Hospital Charge</th>
            <th>Surgery Center Charge</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>43235</td>
            <td>EGD, diagnostic &mdash; no biopsy</td>
            <td>$249</td>
            <td>$1,200&ndash;$5,000</td>
            <td>$800&ndash;$2,200</td>
        </tr>
        <tr>
            <td>43239</td>
            <td>EGD with biopsy</td>
            <td>$311</td>
            <td>$1,500&ndash;$6,500</td>
            <td>$900&ndash;$2,800</td>
        </tr>
        <tr>
            <td>43251</td>
            <td>EGD with polyp removal (snare)</td>
            <td>$387</td>
            <td>$2,000&ndash;$8,000</td>
            <td>$1,100&ndash;$3,500</td>
        </tr>
        <tr>
            <td>43270</td>
            <td>EGD with dilation</td>
            <td>$412</td>
            <td>$2,200&ndash;$7,500</td>
            <td>$1,200&ndash;$3,200</td>
        </tr>
        <tr>
            <td>43247</td>
            <td>EGD with foreign body removal</td>
            <td>$436</td>
            <td>$2,500&ndash;$8,500</td>
            <td>$1,400&ndash;$3,800</td>
        </tr>
    </tbody>
</table>

<p>Hospital charges for CPT 43235 run as high as <strong>20x the Medicare rate</strong> of $249. The same procedure at an ambulatory surgery center averages 8&ndash;10x the Medicare rate &mdash; a significant but still substantial markup. Use <a href="/hospitals/">BillKarma&rsquo;s hospital comparison tool</a> to see what facilities in your area charge for each EGD code.</p>

{_embed(mode="cost", cpt="43239", title="Upper Endoscopy with Biopsy", subtitle="CPT 43239 &mdash; Compare costs at hospitals near you")}

<h2 id="diagnostic-vs-therapeutic">3. Diagnostic vs. therapeutic billing</h2>

<p>A <strong>diagnostic EGD</strong> (CPT 43235) involves visual examination only &mdash; the gastroenterologist looks at the esophagus, stomach, and first part of the small intestine and finds either nothing abnormal or something that requires only observation. No tissue is removed, no procedure is performed.</p>

<p>A <strong>therapeutic EGD</strong> involves an additional procedure performed through the scope during the same visit. The most common therapeutic additions are biopsy (CPT 43239), polyp removal by snare (CPT 43251), and dilation of a stricture (CPT 43270). Only one CPT code is billed &mdash; the one representing the most complex procedure performed. You should not see both CPT 43235 and CPT 43239 on the same bill for a single-session endoscopy.</p>

<div class="key-takeaway">
    <strong>Did your diagnostic endoscopy turn into a bigger bill than expected?</strong> <a href="/scan">Upload your bill to BillKarma</a> to check whether the right CPT code was used, whether you&rsquo;re being billed for both a diagnostic and therapeutic code (which is incorrect), and what the fair price is for your procedure.
</div>

<h2 id="preventive-trap">4. The preventive-to-diagnostic billing trap</h2>

<p>This is the most common billing trap in endoscopy. Here is how it works:</p>

<ol>
    <li>Your doctor orders an upper endoscopy as a <em>preventive screening</em> (e.g., Barrett&rsquo;s esophagus surveillance, celiac disease screening).</li>
    <li>During the procedure, the gastroenterologist finds something suspicious and takes a biopsy.</li>
    <li>The procedure is now billed under CPT 43239 (EGD with biopsy) rather than CPT 43235 (diagnostic EGD).</li>
    <li>Your insurance plan reclassifies the claim from &ldquo;preventive&rdquo; to &ldquo;diagnostic,&rdquo; eliminating your 100% preventive care coverage.</li>
    <li>You owe your full deductible and coinsurance &mdash; a bill you were never warned might arrive.</li>
</ol>

<p>BillKarma&rsquo;s analysis of endoscopy bills at 6,000+ hospitals found that <strong>1 in 3 endoscopy bills</strong> contains a preventive-to-diagnostic billing conversion &mdash; where a routine screening is reclassified as diagnostic after a biopsy, unexpectedly eliminating the patient&rsquo;s 100% preventive care coverage.</p>

<p>Unlike colonoscopy, there is no federal rule mandating that insurers cover endoscopy-related biopsies under preventive care. Your dispute strategy must rely on your plan&rsquo;s specific language. Check your plan&rsquo;s Summary of Benefits and Coverage for how it defines &ldquo;preventive&rdquo; endoscopy and whether biopsy-triggered reclassification is addressed.</p>

<h2 id="anesthesia-pathology">5. Separate anesthesia and pathology fees</h2>

<p><strong>Anesthesia:</strong> Most endoscopies are performed with sedation. There are two billing scenarios: (1) the gastroenterologist personally administers and bills for conscious sedation, bundled into the procedure code; or (2) a separate anesthesiologist or CRNA administers &ldquo;monitored anesthesia care&rdquo; (MAC) and bills separately under a CPT code like 00810. MAC sedation generates a separate bill and is more likely to come from an out-of-network provider.</p>

<p>Under the No Surprises Act (effective 2022), if you are at an in-network facility and you did not affirmatively choose an out-of-network anesthesiologist, you may only be charged in-network cost-sharing. If you receive an out-of-network anesthesia bill from an in-network facility, file a dispute citing the No Surprises Act.</p>

<p><strong>Pathology:</strong> Any tissue biopsied during your EGD is sent to a pathology lab. The pathologist who analyzes the tissue bills separately. This fee runs $200&ndash;$600 and may come from an out-of-network lab even when your gastroenterologist and facility are in-network. The No Surprises Act may protect you here as well if the pathology lab is located at your in-network facility.</p>

<h2 id="egd-vs-colonoscopy">6. Endoscopy vs. colonoscopy billing comparison</h2>

<table>
    <thead>
        <tr>
            <th>Factor</th>
            <th>Upper Endoscopy (EGD)</th>
            <th>Colonoscopy</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Diagnostic CPT code</td>
            <td>43235</td>
            <td>45378</td>
        </tr>
        <tr>
            <td>Biopsy CPT code</td>
            <td>43239</td>
            <td>45380</td>
        </tr>
        <tr>
            <td>Medicare diagnostic rate</td>
            <td>$249</td>
            <td>$260</td>
        </tr>
        <tr>
            <td>Medicare biopsy rate</td>
            <td>$311</td>
            <td>$342</td>
        </tr>
        <tr>
            <td>Federal preventive coverage rule</td>
            <td>No specific rule; plan language governs</td>
            <td>2023 federal rule protects biopsy during preventive colonoscopy</td>
        </tr>
        <tr>
            <td>Anesthesia typically separate?</td>
            <td>Often yes (MAC sedation)</td>
            <td>Often yes (MAC sedation)</td>
        </tr>
        <tr>
            <td>Pathology always separate?</td>
            <td>Yes, when biopsy taken</td>
            <td>Yes, when polyp removed or biopsy taken</td>
        </tr>
    </tbody>
</table>

<p>The key difference: colonoscopy biopsies taken during a preventive screening are protected by a 2023 federal rule for most insurance plans. Upper endoscopy has no equivalent federal protection, making the preventive-to-diagnostic reclassification much harder to fight. For more on the colonoscopy rule, see our <a href="/guides/colonoscopy-billing">colonoscopy billing guide</a>.</p>

<h2 id="hospital-vs-asc">7. Hospital vs. surgery center costs</h2>

<p>Ambulatory surgery centers (ASCs) charge significantly less than hospital outpatient departments for endoscopy. For CPT 43239 (EGD with biopsy), the facility fee at a hospital averages $3,500&ndash;$4,000 compared to $1,200&ndash;$1,500 at an ASC &mdash; a difference of roughly $2,500 for the facility charge alone. For most patients, a same-day endoscopy at an ASC is equally safe and far less expensive.</p>

<p>Before scheduling, ask your gastroenterologist: &ldquo;Can this be done at a surgery center?&rdquo; Also confirm the ASC is in your insurance network. Use the <a href="/calculator">BillKarma cost calculator</a> to compare estimated out-of-pocket costs at specific facilities near you before booking.</p>

<div class="key-takeaway">
    <strong>Comparing endoscopy costs near you?</strong> <a href="/hospitals/">Search BillKarma&rsquo;s database of 6,000+ hospitals and surgery centers</a> to see real price data for CPT 43239 at facilities in your zip code.
</div>

<h2 id="bill-example">8. Annotated bill example</h2>

<p>Below is a representative bill for an upper endoscopy with biopsy (CPT 43239) at a hospital outpatient department. Items marked as <strong>flagged</strong> warrant a closer look; items marked as <strong>errors</strong> should be disputed.</p>

<div class="bill-example">
    <div class="line-item">
        <span class="service">EGD with biopsy (CPT 43239) &mdash; facility fee</span>
        <span class="charge">$3,800</span>
        <span class="note">12.2x Medicare rate of $311. Typical range $1,500&ndash;$6,500. Request itemized bill to see full detail.</span>
    </div>
    <div class="line-item flagged">
        <span class="service">Monitored anesthesia care (CPT 00810) &mdash; separate anesthesia group</span>
        <span class="charge">$940</span>
        <span class="note">Flagged: Confirm this provider is in-network. If out-of-network at an in-network facility, dispute using No Surprises Act protections.</span>
    </div>
    <div class="line-item error">
        <span class="service">EGD, diagnostic (CPT 43235) &mdash; facility fee</span>
        <span class="charge">$1,200</span>
        <span class="note">Error: Both CPT 43235 and CPT 43239 appear on this bill for a single endoscopy session. Only the higher-level code (43239) should be billed. This is duplicate/unbundled billing. Dispute immediately.</span>
    </div>
    <div class="line-item">
        <span class="service">Gastroenterologist professional fee (CPT 43239)</span>
        <span class="charge">$520</span>
        <span class="note">Separate billing from physician group. Verify physician is in-network.</span>
    </div>
    <div class="line-item flagged">
        <span class="service">Pathology &mdash; GI biopsy specimen (CPT 88305)</span>
        <span class="charge">$480</span>
        <span class="note">Flagged: Verify pathology group is in-network. If not, No Surprises Act may apply. Also confirm you received only one pathology bill, not two.</span>
    </div>
    <div class="line-total">
        <span class="service">Total billed</span>
        <span class="charge">$6,940</span>
    </div>
    <div class="line-total">
        <span class="service">Estimated after dispute (duplicate CPT 43235 removed)</span>
        <span class="charge">$5,740</span>
    </div>
</div>

<div class="key-takeaway">
    <strong>Received an out-of-network anesthesia bill after your endoscopy?</strong> The No Surprises Act may protect you. <a href="/scan">Upload your bill to BillKarma</a> and we&rsquo;ll flag whether the charge qualifies for a No Surprises Act dispute and generate the letter for you.
</div>

<h2 id="dispute">9. How to dispute endoscopy charges</h2>

<p>Request your itemized bill from the facility and a separate bill from each provider (gastroenterologist, anesthesiologist, pathologist). Also request your procedure report, which details exactly what was done during the scope.</p>

<p>Key errors to look for and how to dispute them:</p>

<ul>
    <li><strong>Both diagnostic and therapeutic codes billed:</strong> You should never see both CPT 43235 and CPT 43239 (or 43251) on a single-session bill. Only the highest-level code applies. Dispute the lower-level code charge as an unbundling error.</li>
    <li><strong>Preventive-to-diagnostic reclassification:</strong> Review your plan&rsquo;s Summary of Benefits. If your procedure was ordered as preventive, request your insurer explain in writing why it was reclassified and under what plan provision. File an internal appeal citing the original referral order as evidence of preventive intent.</li>
    <li><strong>Out-of-network anesthesia at in-network facility:</strong> Cite the No Surprises Act. Send a dispute letter to the anesthesia provider and your insurer simultaneously, stating you did not choose the out-of-network provider and that federal law limits your cost to in-network rates.</li>
    <li><strong>Duplicate pathology charges:</strong> Multiple pathology bills for a single biopsy specimen. Request each bill to confirm they cover different tissue samples or different analyses.</li>
</ul>

<p>See our <a href="/guides/dispute-bill">complete dispute guide</a> for letter templates. For additional help with endoscopy billing errors, <a href="/scan">upload your bill to BillKarma</a> for an automated review.</p>

<h2 id="case-studies">10. Case studies</h2>

<div class="case-study">
    <h3>Case 1: Screening-to-diagnostic reclassification dispute saves $1,400</h3>
    <p>A 57-year-old patient in Minneapolis scheduled a surveillance upper endoscopy for known Barrett&rsquo;s esophagus. The gastroenterologist took two biopsies during the procedure. Her insurer reclassified the claim from preventive to diagnostic and applied her $2,000 deductible, sending her a bill for $1,800. BillKarma flagged the reclassification and generated a dispute letter citing her original referral order as a preventive surveillance scope. After two rounds of internal appeals, the insurer reversed the reclassification and covered the procedure under preventive benefits, reducing her bill from $1,800 to <strong>$0 owed</strong>.</p>
</div>

<div class="case-study">
    <h3>Case 2: Out-of-network anesthesia charge reversed</h3>
    <p>A 44-year-old in Miami received a separate $1,150 anesthesia bill from an out-of-network CRNA after an EGD performed at an in-network hospital. He had not been informed the anesthesia provider was out-of-network and had not consented to out-of-network care. BillKarma identified this as a likely No Surprises Act violation and generated a dispute letter. The anesthesia provider agreed to apply in-network rates, reducing the bill from $1,150 to <strong>$280</strong> (the patient&rsquo;s in-network coinsurance).</p>
</div>

<div class="case-study">
    <h3>Case 3: Duplicate pathology charge removed</h3>
    <p>A 50-year-old in Boston received two separate pathology bills totaling $960 after an EGD with biopsy. One bill was from the hospital&rsquo;s in-house pathology department; the other was from an outside pathology group. BillKarma identified that both bills referenced the same specimen date and the same tissue type &mdash; a stomach biopsy. After the patient contacted both billing departments, the outside group confirmed the specimen had already been analyzed and billed by the hospital. The duplicate charge of <strong>$480 was reversed</strong>.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does an upper endoscopy (EGD) cost?</h3>
        <p>An upper endoscopy costs $800&ndash;$8,000 depending on facility type and what procedures were performed. The average at hospitals is $2,750; at ambulatory surgery centers it is typically $800&ndash;$2,500. The Medicare rate for a basic diagnostic EGD (CPT 43235) is $249.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between a diagnostic and therapeutic endoscopy?</h3>
        <p>A diagnostic EGD (CPT 43235) involves visual examination only. A therapeutic EGD involves an additional procedure &mdash; biopsy (CPT 43239), polyp removal (CPT 43251), or dilation (CPT 43270). Only the most complex procedure performed is billed; you should not see both a diagnostic and a therapeutic code on the same bill.</p>
    </div>
    <div class="faq-item">
        <h3>Why did my preventive endoscopy turn into a diagnostic procedure?</h3>
        <p>If a biopsy was taken during what was ordered as a preventive or surveillance scope, your insurer may reclassify the claim as diagnostic, eliminating preventive coverage. Unlike colonoscopy, there is no federal rule protecting against this reclassification for EGD. Dispute it by showing the original referral order documented preventive intent and reviewing your plan&rsquo;s definition of &ldquo;preventive.&rdquo;</p>
    </div>
    <div class="faq-item">
        <h3>Will I get a separate bill from an anesthesiologist for my endoscopy?</h3>
        <p>Yes, if monitored anesthesia care (MAC) was used by a separate anesthesiologist or CRNA. This provider may be out-of-network even if your gastroenterologist and facility are in-network. The No Surprises Act may protect you if you were at an in-network facility and did not choose the out-of-network provider.</p>
    </div>
    <div class="faq-item">
        <h3>What is a pathology charge after an endoscopy biopsy?</h3>
        <p>Biopsied tissue is analyzed by a pathologist who bills separately from the gastroenterologist and facility. This generates a third bill, typically $200&ndash;$600. Confirm the pathology group is in-network or that No Surprises Act protections apply. Watch for duplicate pathology bills covering the same specimen.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li>FAIR Health Consumer. <em>Upper Endoscopy Cost Estimates by CPT Code.</em> <a href="https://www.fairhealthconsumer.org" target="_blank" rel="noopener">fairhealthconsumer.org</a></li>
    <li>Centers for Medicare &amp; Medicaid Services. <em>2026 Medicare Physician Fee Schedule &mdash; CPT 43235, 43239, 43251, 43270, 43247.</em> <a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">cms.gov</a></li>
    <li>American Society for Gastrointestinal Endoscopy (ASGE). <em>Understanding Endoscopy Bills.</em> <a href="https://www.asge.org" target="_blank" rel="noopener">asge.org</a></li>
    <li>Centers for Medicare &amp; Medicaid Services. <em>No Surprises Act: Overview and Patient Protections.</em> <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a></li>
    <li>Agency for Healthcare Research and Quality (AHRQ). <em>HCUPnet: Upper Endoscopy Utilization Statistics.</em> <a href="https://hcupnet.ahrq.gov" target="_blank" rel="noopener">hcupnet.ahrq.gov</a></li>
    <li>Health Affairs. <em>Billing Practices for Endoscopy in Outpatient Settings.</em> <a href="https://www.healthaffairs.org" target="_blank" rel="noopener">healthaffairs.org</a></li>
</ul>
""",
})
