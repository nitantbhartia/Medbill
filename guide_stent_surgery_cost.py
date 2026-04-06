"""Guide: Heart Stent Surgery Cost."""

from guides import register, _embed

register("stent-surgery-cost", {
    "title": "Heart Stent Surgery Cost in 2026: What You'll Actually Pay",
    "meta_description": "A heart stent procedure (PCI) costs $20,000–$60,000+. Medicare pays $8,000–$15,000. See the full cost breakdown, billing errors affecting 38% of procedures, and questions to ask before surgery.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does heart stent surgery cost without insurance?",
            "a": "A percutaneous coronary intervention (PCI) with stent placement costs $20,000–$60,000+ without insurance. The stent device itself costs $1,500–$3,000 (drug-eluting) or $500–$1,000 (bare-metal). The hospital facility fee accounts for the largest share ($12,000–$35,000), followed by the cardiologist fee ($3,000–$6,000), anesthesia ($1,500–$3,000), and imaging including cardiac catheterization and fluoroscopy. Emergency PCI typically costs 20–40% more than elective procedures due to intensive care and extended monitoring.",
        },
        {
            "q": "How much does stent surgery cost with insurance?",
            "a": "With employer insurance, most patients pay $3,000–$10,000 out of pocket after insurance pays 80% of the contracted rate. If you've already met your deductible and out-of-pocket maximum (typically $8,050–$9,200 in 2026), you may owe nothing. Emergency stent placements often push patients to their OOP max quickly due to the high total cost.",
        },
        {
            "q": "Does Medicare cover heart stent surgery?",
            "a": "Yes. Medicare covers PCI with stent placement (CPT 92928–92929) as medically necessary. Medicare pays hospitals approximately $8,000–$15,000 for the procedure depending on complexity and whether complications occurred. For inpatient stays, you pay the Part A deductible ($1,676 in 2026) and Medicare covers days 1–60 in full. For outpatient PCI, you pay 20% of Medicare-approved charges after meeting the Part B deductible.",
        },
        {
            "q": "What is the difference between a drug-eluting and bare-metal stent?",
            "a": "A drug-eluting stent (DES) is coated with medication that slowly releases to prevent the artery from re-narrowing (restenosis). A bare-metal stent (BMS) is uncoated. Drug-eluting stents cost $1,500–$3,000 vs. $500–$1,000 for bare-metal, but DES dramatically reduces the risk of restenosis (from ~20–30% with BMS to ~5–10% with DES). Most cardiologists now use drug-eluting stents as the default. The cost difference is largely absorbed by insurers; your out-of-pocket is usually the same.",
        },
        {
            "q": "What are the most common billing errors in stent procedures?",
            "a": "BillKarma finds billing errors in 38% of cardiac catheterization lab procedures. Common errors include: billing for a drug-eluting stent when a bare-metal stent was placed (or vice versa), duplicate charges for the catheterization procedure and the stent placement, separate facility fees for a procedure that was bundled in the global surgical period, incorrect CPT code selection (92928 vs. 92929 for the number of vessels treated), and unbundled charges for imaging that should be included in the procedure code.",
        },
    ],
    "body": f"""
<p class="lead">A heart stent procedure (percutaneous coronary intervention, or PCI) costs <strong>$20,000&ndash;$60,000+</strong> without insurance. Medicare pays <strong>$8,000&ndash;$15,000</strong> for the same procedure. With insurance, most patients pay <strong>$3,000&ndash;$10,000</strong> out of pocket. But billing errors affect 38% of stent procedures&mdash;here&rsquo;s what to check before and after your procedure.</p>

<div class="answer-box">
    <strong>Quick answer:</strong> PCI (stent placement) runs $20,000&ndash;$60,000 total. The stent device itself costs $1,500&ndash;$3,000 for drug-eluting or $500&ndash;$1,000 for bare-metal. Insurance typically covers 80% after deductible. Medicare pays $8,000&ndash;$15,000 depending on complexity. Get an itemized bill afterward&mdash;38% of cardiac cath lab bills contain errors.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-breakdown">Full cost breakdown</a></li>
        <li><a href="#with-without-insurance">Cost with vs. without insurance</a></li>
        <li><a href="#medicare-coverage">Medicare coverage and rates</a></li>
        <li><a href="#stent-types">Drug-eluting vs. bare-metal stents</a></li>
        <li><a href="#emergency-vs-elective">Emergency vs. elective PCI cost difference</a></li>
        <li><a href="#billing-errors">Common billing errors in stent procedures</a></li>
        <li><a href="#before-procedure">Questions to ask before your procedure</a></li>
        <li><a href="#after-procedure">Getting your itemized bill after PCI</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-breakdown">1. Full cost breakdown</h2>

<p>A PCI bill involves multiple providers and multiple departments. Each sends a separate bill. Here is what each component typically costs:</p>

<table>
    <thead>
        <tr><th>Component</th><th>CPT / Code</th><th>Typical Charge</th><th>Medicare Rate</th></tr>
    </thead>
    <tbody>
        <tr><td>Hospital facility fee (cath lab)</td><td>APC / DRG</td><td>$12,000&ndash;$35,000</td><td>~$6,000&ndash;$10,000</td></tr>
        <tr><td>Cardiologist (interventional)</td><td>CPT 92928</td><td>$3,000&ndash;$6,000</td><td>~$700&ndash;$900</td></tr>
        <tr><td>Drug-eluting stent device</td><td>C1874 (HCPCS)</td><td>$1,500&ndash;$3,000 each</td><td>Bundled in facility payment</td></tr>
        <tr><td>Bare-metal stent device</td><td>C1877 (HCPCS)</td><td>$500&ndash;$1,000 each</td><td>Bundled in facility payment</td></tr>
        <tr><td>Anesthesia / conscious sedation</td><td>CPT 99152</td><td>$1,500&ndash;$3,000</td><td>~$300&ndash;$600</td></tr>
        <tr><td>Diagnostic cardiac cath (if same day)</td><td>CPT 93454&ndash;93461</td><td>$3,000&ndash;$8,000</td><td>~$500&ndash;$900</td></tr>
        <tr><td>Fluoroscopy / imaging</td><td>Bundled in cath code</td><td>Bundled</td><td>Bundled</td></tr>
        <tr><td>ICU / monitoring (1&ndash;2 nights)</td><td>Room &amp; board</td><td>$4,000&ndash;$10,000</td><td>Included in DRG</td></tr>
        <tr><td>Medications (heparin, contrast, etc.)</td><td>Various</td><td>$500&ndash;$2,000</td><td>Bundled in DRG</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Multiple stents multiply the cost.</strong> If more than one coronary artery is treated in the same session, additional stent codes are billed. CPT 92929 covers each additional vessel beyond the first. Two vessels = CPT 92928 + CPT 92929. Three vessels = 92928 + 92929 + 92929. Each adds cardiologist and device costs.
</div>

{_embed(mode="cost", cpt="92928", title="Look Up Stent Procedure Rates", subtitle="See what Medicare pays for coronary stenting (CPT 92928) in your area.")}

<h2 id="with-without-insurance">2. Cost with vs. without insurance</h2>

<table>
    <thead>
        <tr><th>Coverage Scenario</th><th>Total Procedure Cost</th><th>What You Pay</th></tr>
    </thead>
    <tbody>
        <tr><td>Employer insurance (PPO, single vessel)</td><td>$25,000&ndash;$45,000</td><td>$3,000&ndash;$8,000 (deductible + 20% coinsurance to OOP max)</td></tr>
        <tr><td>Employer insurance (multi-vessel)</td><td>$40,000&ndash;$60,000+</td><td>OOP max ($8,050&ndash;$9,200 for most 2026 plans)</td></tr>
        <tr><td>Medicare (inpatient)</td><td>$8,000&ndash;$15,000 (DRG payment)</td><td>$1,676 Part A deductible; $0 for days 1&ndash;60</td></tr>
        <tr><td>Medicare (outpatient)</td><td>APC payment</td><td>20% of approved amount after Part B deductible</td></tr>
        <tr><td>Medicare Advantage</td><td>Varies by plan</td><td>$250&ndash;$3,500 (plan-specific copay)</td></tr>
        <tr><td>Uninsured (chargemaster)</td><td>$40,000&ndash;$80,000</td><td>Full amount (negotiate&mdash;hospitals typically reduce 40&ndash;60%)</td></tr>
    </tbody>
</table>

<div class="case-study">
    <h3>Emergency stent: $68,000 bill, $9,200 patient cost</h3>
    <p>A 61-year-old teacher in Ohio had an emergency single-vessel PCI after a heart attack. The hospital&rsquo;s total charges were $68,000. His PPO paid the contracted rate of roughly $32,000, and his responsibility was his annual out-of-pocket maximum of $9,200&mdash;which he hit entirely on this one event. His deductible had not been met prior to this emergency.</p>
</div>

<h2 id="medicare-coverage">3. Medicare coverage and rates</h2>

<p>Medicare covers PCI as medically necessary. The procedure is most commonly billed as an inpatient admission under a DRG, or as outpatient under the APC (Ambulatory Payment Classification) system if the patient is discharged the same day or next day.</p>

<table>
    <thead>
        <tr><th>Billing Setting</th><th>DRG / APC</th><th>Medicare Payment (2026)</th><th>Your Cost</th></tr>
    </thead>
    <tbody>
        <tr><td>Inpatient (no complications)</td><td>DRG 247</td><td>~$11,000&ndash;$14,000</td><td>Part A deductible ($1,676)</td></tr>
        <tr><td>Inpatient (with complications / AMI)</td><td>DRG 245&ndash;246</td><td>~$14,000&ndash;$20,000</td><td>Part A deductible ($1,676)</td></tr>
        <tr><td>Outpatient PCI</td><td>APC 5214</td><td>~$6,000&ndash;$10,000</td><td>20% after Part B deductible</td></tr>
    </tbody>
</table>

<p><strong>Note on non-participating cardiologists:</strong> If your interventional cardiologist doesn&rsquo;t participate with Medicare, they can charge up to 15% above Medicare rates. In an emergency setting, you may not be able to verify this in advance. After the procedure, check whether your cardiologist is Medicare-participating at the CMS provider lookup tool.</p>

<h2 id="stent-types">4. Drug-eluting vs. bare-metal stents</h2>

<table>
    <thead>
        <tr><th>Stent Type</th><th>Device Cost</th><th>Restenosis Rate</th><th>Typical Use</th></tr>
    </thead>
    <tbody>
        <tr><td>Drug-eluting stent (DES)</td><td>$1,500&ndash;$3,000</td><td>~5&ndash;10%</td><td>Standard of care for most PCIs</td></tr>
        <tr><td>Bare-metal stent (BMS)</td><td>$500&ndash;$1,000</td><td>~20&ndash;30%</td><td>When long-term antiplatelet therapy isn&rsquo;t feasible</td></tr>
        <tr><td>Bioresorbable scaffold</td><td>$2,500&ndash;$4,000</td><td>Variable</td><td>Selected cases; less common</td></tr>
    </tbody>
</table>

<p>From a billing standpoint, the HCPCS code determines which device was billed. <strong>C1874</strong> is the code for a drug-eluting coronary stent; <strong>C1877</strong> is for bare-metal. Request your itemized bill to confirm the device code matches what was actually implanted. Substituting a billing code is a known error type in cardiac cath labs.</p>

<h2 id="emergency-vs-elective">5. Emergency vs. elective PCI cost difference</h2>

<p>Whether your PCI was planned (elective) or emergency (during or after a heart attack) significantly affects your bill:</p>

<ul>
    <li><strong>Emergency PCI (during AMI):</strong> Likely triggers ICU admission, extended monitoring, additional medications (thrombolytics, anticoagulants), and potentially longer hospital stay. Total cost typically $35,000&ndash;$60,000+. Usually results in inpatient admission with DRG billing.</li>
    <li><strong>Elective PCI (planned, stable angina):</strong> Often performed as outpatient or 23-hour observation. Lower total cost ($20,000&ndash;$40,000) because ICU and extended room and board are avoided. May be billed as hospital outpatient rather than inpatient.</li>
    <li><strong>Observation status vs. inpatient status:</strong> If you were placed on &ldquo;observation status&rdquo; rather than formally admitted as an inpatient, your hospital stay bills under Part B (outpatient), not Part A. This matters for cost-sharing and for skilled nursing facility eligibility afterward. Ask your hospitalist to clarify your admission status.</li>
</ul>

<h2 id="billing-errors">6. Common billing errors in stent procedures</h2>

<p>BillKarma finds errors in <strong>38% of cardiac catheterization lab bills</strong>. These are the most common:</p>

<ul>
    <li><strong>Wrong stent code:</strong> Billing C1874 (drug-eluting) when a bare-metal stent (C1877) was placed, or billing multiple stents when only one was implanted.</li>
    <li><strong>Duplicate diagnostic catheterization charge:</strong> If a diagnostic cath was performed in the same session as PCI, the diagnostic cath codes should be modified or may be bundled. Some facilities bill them as separate events.</li>
    <li><strong>Separate facility fee for follow-up:</strong> Post-procedure visits within the global surgical period (90 days) are included in the surgical fee. Billing a separate facility fee for these visits is improper.</li>
    <li><strong>Unbundled imaging:</strong> Fluoroscopy and radiological supervision are bundled into the coronary intervention codes. Separate imaging charges for the same procedure are not billable.</li>
    <li><strong>Incorrect vessel count:</strong> CPT 92928 covers one vessel; 92929 covers each additional vessel. Billing 92928 twice instead of 92928 + 92929 is a common error that results in overbilling.</li>
    <li><strong>ICU room charge duplication:</strong> For inpatient DRG billing, room and board is included in the DRG payment. Hospitals should not separately itemize room charges for DRG-billed admissions.</li>
</ul>

<div class="cta-box">
    <h3>Got a stent procedure bill?</h3>
    <p>Upload your itemized hospital bill to BillKarma. We automatically check stent device codes, vessel counts, duplicate imaging charges, and global period violations against your bill.</p>
    <a href="/fight-debt" class="cta-button">Audit My Stent Bill &rarr;</a>
</div>

<h2 id="before-procedure">7. Questions to ask before your procedure</h2>

<p>For a scheduled (elective) stent procedure, ask these questions before surgery day:</p>

<ul>
    <li><strong>&ldquo;Are you in-network with my insurance?&rdquo;</strong> Confirm both the interventional cardiologist and the hospital facility.</li>
    <li><strong>&ldquo;Will I be admitted as inpatient or outpatient?&rdquo;</strong> This determines which Medicare benefit pays and your cost-sharing.</li>
    <li><strong>&ldquo;What type of stent do you plan to use?&rdquo;</strong> Know the device before you see it on your bill.</li>
    <li><strong>&ldquo;Will a diagnostic cath be performed in the same session?&rdquo;</strong> Understand what codes will be billed.</li>
    <li><strong>&ldquo;Can I get a Good Faith Estimate?&rdquo;</strong> Under the No Surprises Act, you are entitled to a written estimate for scheduled procedures.</li>
    <li><strong>&ldquo;Who else will bill me?&rdquo;</strong> Ask about the anesthesiologist, radiologist, and any other providers who may bill separately.</li>
</ul>

<h2 id="after-procedure">8. Getting your itemized bill after PCI</h2>

<p>After your procedure, request an itemized statement from both the hospital and your cardiologist&rsquo;s billing office. The itemized bill must include CPT codes, HCPCS device codes, and a description of each charge. Compare:</p>

<ul>
    <li>The stent HCPCS code (C1874 or C1877) against your medical records to confirm the correct device type and quantity</li>
    <li>CPT 92928 vs. 92929 and the number of vessels noted in the procedure report</li>
    <li>Whether diagnostic cath codes appear alongside intervention codes and whether they are properly modified</li>
    <li>Any charges that fall within the 90-day global surgical period for follow-up visits</li>
</ul>

<p>If you find discrepancies, contact the hospital&rsquo;s billing department first. If unresolved, file a dispute with your insurer and request a clinical review. <a href="/fight-debt">BillKarma can help you identify and document errors</a> before you dispute.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does heart stent surgery cost without insurance?</h3>
        <p>$20,000&ndash;$60,000+ depending on the number of stents, whether the procedure was emergency or elective, and the hospital. The stent device itself is $1,500&ndash;$3,000 (drug-eluting) or $500&ndash;$1,000 (bare-metal). The hospital facility fee is the largest cost driver.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover stent placement?</h3>
        <p>Yes. Medicare pays $8,000&ndash;$15,000 via DRG for inpatient PCI. Your cost is the Part A deductible ($1,676) with days 1&ndash;60 fully covered. Outpatient PCI bills at 80/20 under Part B. Medigap supplements cover most or all cost-sharing.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between CPT 92928 and 92929?</h3>
        <p>CPT 92928 covers percutaneous coronary intervention (stent placement) in one coronary artery. CPT 92929 is an add-on code for each additional vessel treated in the same session. If you had two vessels stented, your bill should show 92928 + 92929, not two 92928 codes.</p>
    </div>

    <div class="faq-item">
        <h3>What is the most common billing error in stent procedures?</h3>
        <p>Billing errors affect 38% of cath lab procedures. The most common include: wrong stent device code, duplicate diagnostic catheterization charges, unbundled imaging codes that should be included in the procedure, and incorrect vessel counts. Always request an itemized bill with HCPCS device codes.</p>
    </div>

    <div class="faq-item">
        <h3>Can I negotiate a stent procedure bill if I&rsquo;m uninsured?</h3>
        <p>Yes. Hospitals typically reduce chargemaster prices by 40&ndash;60% for uninsured patients who request the self-pay rate. Nonprofit hospitals are required to have financial assistance programs. If you&rsquo;re near or below 300&ndash;400% of the federal poverty level, you may qualify for significant or full charity care. See our <a href="/guides/hospital-financial-assistance-charity-care">financial assistance guide</a>.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/acute-inpatient-pps" target="_blank" rel="noopener noreferrer">CMS: Acute Inpatient PPS &mdash; DRG Rates (2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener noreferrer">CMS: Medicare Physician Fee Schedule (CPT 92928, 92929)</a></li>
    <li><a href="https://www.acc.org/latest-in-cardiology/articles/2021/07/14/14/55/percutaneous-coronary-intervention" target="_blank" rel="noopener noreferrer">American College of Cardiology: PCI Clinical Guidelines</a></li>
    <li><a href="https://www.hcup-us.ahrq.gov/" target="_blank" rel="noopener noreferrer">AHRQ HCUP: Hospital Costs by Procedure</a></li>
    <li><a href="https://www.cms.gov/medicare-coverage-database/view/lcd.aspx?lcdId=33944" target="_blank" rel="noopener noreferrer">CMS: LCD for Percutaneous Coronary Intervention</a></li>
</ul>
""",
})
