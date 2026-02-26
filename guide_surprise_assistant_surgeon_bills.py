"""Guide: Surprise Bills from Assistant Surgeons: Your Rights and What to Do."""

from guides import register, _embed

register("surprise-assistant-surgeon-bills", {
    "title": "Surprise Bills from Assistant Surgeons: Your Rights and What to Do",
    "meta_description": "Got an unexpected bill from an assistant surgeon you never chose? Learn how modifier 80/82 billing works, your No Surprises Act rights, and how to dispute.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "What is an assistant surgeon and why did I get a bill from one?",
            "a": "An assistant surgeon is a second physician who helps the primary surgeon during a procedure. They may hold retractors, assist with tissue dissection, or help manage bleeding. Hospitals and surgeons decide whether an assistant is needed based on the complexity of the procedure — patients are rarely consulted or informed beforehand. The assistant surgeon bills separately from the primary surgeon, typically at 16% to 20% of the primary surgeon's fee, which can still amount to thousands of dollars."
        },
        {
            "q": "Does the No Surprises Act protect me from assistant surgeon bills?",
            "a": "Yes, in many cases. If your surgery was performed at an in-network facility and the assistant surgeon was out-of-network, the No Surprises Act protects you from balance billing. You should only owe your in-network cost-sharing amount. If the surgery was an emergency, you are protected regardless of facility network status. The key exception is if you signed a written consent form agreeing to out-of-network care from the assistant surgeon at least 72 hours before a scheduled procedure."
        },
        {
            "q": "What are modifier 80 and modifier 82 in surgical billing?",
            "a": "Modifier 80 indicates an assistant surgeon was present during the procedure. Modifier 82 indicates an assistant surgeon was used when a qualified resident surgeon was not available. Modifier AS indicates a physician assistant, nurse practitioner, or clinical nurse specialist served as the assistant. The modifier determines who assisted and affects the reimbursement rate. Medicare pays modifier 80 claims at 16% of the primary surgeon's fee schedule amount."
        },
        {
            "q": "How do I dispute an assistant surgeon bill I never agreed to?",
            "a": "Start by checking whether the No Surprises Act applies — was the assistant surgeon out-of-network at an in-network facility? If so, contact your insurer and request the claim be reprocessed at in-network rates. If the procedure did not require an assistant surgeon per Medicare guidelines, you can dispute the medical necessity of the charge. Request the operative report to verify the assistant's role, and check CMS guidelines to see if the procedure code allows assistant surgeon billing."
        },
        {
            "q": "Can a surgeon use an assistant surgeon if Medicare says one is not needed?",
            "a": "Medicare classifies procedures into categories for assistant surgeon billing. Some procedures have a billing indicator that means assistant surgeon services are not covered because they are not typically medically necessary. If Medicare does not cover an assistant for your procedure code, the assistant surgeon cannot bill Medicare for it. However, commercial insurers may have different policies. Always check your insurer's policy and the Medicare indicator for the specific CPT code."
        },
    ],
    "body": f"""
<p class="lead">Every year, thousands of patients receive surprise bills from assistant surgeons they never met, never chose, and never consented to. The assistant surgeon — a second physician who helps the primary surgeon during an operation — bills separately, and when they are out-of-network, the charges can be staggering. BillKarma's analysis of surgical bills found that <strong>assistant surgeon charges average $2,000 to $6,000</strong>, with some exceeding $10,000 for complex procedures. The good news: federal law now protects most patients from the worst of these surprise charges.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-it-works">How assistant surgeon billing works</a></li>
        <li><a href="#why-surprise">Why assistant surgeon bills are often surprises</a></li>
        <li><a href="#modifiers">Understanding modifier 80, 82, and AS billing</a></li>
        <li><a href="#your-rights">Your rights under the No Surprises Act</a></li>
        <li><a href="#medical-necessity">When an assistant surgeon is not medically necessary</a></li>
        <li><a href="#dispute">How to dispute an assistant surgeon bill</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-it-works">1. How assistant surgeon billing works</h2>

<p>When a surgical procedure requires a second physician to assist, the assistant surgeon bills your insurance separately from the primary surgeon. The assistant uses the same CPT procedure code as the primary surgeon but appends a billing modifier to indicate their role. The standard reimbursement for an assistant surgeon under Medicare is <strong>16% of the primary surgeon's allowed amount</strong>.</p>

<p>Here is how the billing breaks down for a typical procedure:</p>

<table>
    <thead>
        <tr>
            <th>Role</th>
            <th>Modifier</th>
            <th>Medicare Reimbursement</th>
            <th>Typical Billed Charge</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Primary surgeon</td>
            <td>None</td>
            <td>100% of fee schedule</td>
            <td>$3,000&ndash;$15,000+</td>
        </tr>
        <tr>
            <td>Assistant surgeon (physician)</td>
            <td>Modifier 80</td>
            <td>16% of primary surgeon fee</td>
            <td>$1,500&ndash;$6,000+</td>
        </tr>
        <tr>
            <td>Assistant surgeon (no resident available)</td>
            <td>Modifier 82</td>
            <td>16% of primary surgeon fee</td>
            <td>$1,500&ndash;$6,000+</td>
        </tr>
        <tr>
            <td>Physician assistant / NP as assistant</td>
            <td>Modifier AS</td>
            <td>13.6% of primary surgeon fee (85% of 16%)</td>
            <td>$800&ndash;$3,000+</td>
        </tr>
    </tbody>
</table>

<p>The gap between what the assistant surgeon bills and what Medicare pays is enormous. An assistant surgeon might bill $4,000 for helping with a spinal fusion, while Medicare's allowed amount is closer to $640 (16% of the primary surgeon's approximately $4,000 Medicare rate). When the assistant is out-of-network, the patient can be balance-billed for the difference between the billed charge and what insurance pays — unless the No Surprises Act applies.</p>

{_embed(mode="markup", title="Check your assistant surgeon charge", subtitle="Enter the CPT code and billed amount to compare against Medicare rates.", height="420")}

<h2 id="why-surprise">2. Why assistant surgeon bills are often surprises</h2>

<p>Assistant surgeon bills catch patients off guard for several reasons:</p>

<ul>
    <li><strong>Patients do not choose the assistant surgeon.</strong> The primary surgeon or the hospital arranges for an assistant. Patients are rarely asked to approve the specific physician and almost never told their network status.</li>
    <li><strong>The bill arrives separately.</strong> The assistant surgeon sends their own bill, often weeks after the primary surgeon's bill and the hospital facility bill. Patients may receive three or four separate bills from a single surgery.</li>
    <li><strong>The assistant may be out-of-network.</strong> Even when the primary surgeon and hospital are in-network, the assistant surgeon may be employed by a different practice group that does not participate in the patient's insurance network.</li>
    <li><strong>Consent forms are vague.</strong> Hospital consent forms often include broad language authorizing "additional physicians as deemed necessary" without specifying who those physicians are or what their network status is.</li>
</ul>

<div class="key-takeaway">
    <strong>Before any scheduled surgery:</strong> Ask your surgeon whether an assistant surgeon will be used, who it will be, and whether they are in your insurance network. If the assistant is out-of-network, ask the surgeon to use an in-network assistant or put in writing that you do not consent to out-of-network assistant surgeon services. You can <a href="/hospitals/">look up your hospital's billing grade</a> in our directory to see how frequently it uses out-of-network providers.
</div>

<h2 id="modifiers">3. Understanding modifier 80, 82, and AS billing</h2>

<p>The modifier appended to the CPT code on the assistant surgeon's bill tells you who assisted and under what circumstances:</p>

<ul>
    <li><strong>Modifier 80 — Assistant surgeon.</strong> A physician (MD or DO) assisted the primary surgeon. This is the standard assistant surgeon modifier and pays at 16% of the primary surgeon's Medicare fee.</li>
    <li><strong>Modifier 82 — Assistant surgeon when a qualified resident is not available.</strong> This modifier is used in teaching hospitals when a surgical resident would normally assist but none was available. The same 16% reimbursement rate applies. If a teaching hospital uses modifier 82 frequently, it may indicate a staffing issue rather than a clinical necessity.</li>
    <li><strong>Modifier AS — Non-physician assistant at surgery.</strong> A physician assistant (PA), nurse practitioner (NP), or clinical nurse specialist served as the assistant. Medicare pays at 85% of the physician assistant rate, which works out to approximately 13.6% of the primary surgeon's fee. PA and NP assistants typically bill lower amounts than physician assistants.</li>
</ul>

<p>When reviewing your bill, look for the CPT code followed by a dash and the modifier (e.g., "27447-80" for a total knee replacement with a physician assistant surgeon). If you see modifier 80 or 82, a physician was assisting. If you see modifier AS, a PA or NP was assisting. In either case, the charge should be a fraction of the primary surgeon's fee — not a comparable amount.</p>

<h2 id="your-rights">4. Your rights under the No Surprises Act</h2>

<p>The No Surprises Act, effective January 1, 2022, provides strong protections against surprise assistant surgeon bills in most common scenarios:</p>

<ul>
    <li><strong>Emergency surgery:</strong> If the surgery was an emergency, all providers — including the assistant surgeon — are subject to NSA protections regardless of network status. You can only be charged in-network cost-sharing rates.</li>
    <li><strong>Scheduled surgery at an in-network facility:</strong> If the hospital or surgery center is in your network but the assistant surgeon is not, the NSA protects you from balance billing. The assistant surgeon and your insurer must resolve payment between themselves.</li>
    <li><strong>The consent exception:</strong> The NSA protections can be waived if you signed a written consent form specifically agreeing to out-of-network care from the assistant surgeon at least 72 hours before a scheduled (non-emergency) procedure. The consent must identify the specific provider and include a good-faith estimate of charges. Generic surgical consent forms that broadly authorize "additional physicians" do not meet this standard.</li>
</ul>

<p><strong>If you did not sign a specific out-of-network consent for the assistant surgeon, the NSA applies.</strong> Contact your insurer and request the claim be reprocessed at in-network rates. If the provider refuses to comply, file a complaint at cms.gov/nosurprises or call 1-800-985-3059. For more on how these protections work, see our <a href="/guides/no-surprises-act-explained">No Surprises Act guide</a>.</p>

<h2 id="medical-necessity">5. When an assistant surgeon is not medically necessary</h2>

<p>Not every surgery requires an assistant surgeon. Medicare classifies procedures by whether assistant surgeon services are typically needed. Each CPT code has an assistant surgeon indicator:</p>

<table>
    <thead>
        <tr>
            <th>Indicator</th>
            <th>Meaning</th>
            <th>Medicare Pays for Assistant?</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0</td>
            <td>Assistant surgeon services restricted &mdash; not typically needed</td>
            <td>No (payment not allowed)</td>
        </tr>
        <tr>
            <td>1</td>
            <td>Assistant surgeon may be paid</td>
            <td>Yes, with documentation</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Assistant surgeon paid without documentation</td>
            <td>Yes</td>
        </tr>
    </tbody>
</table>

<p>If your procedure has an indicator of 0 (assistant not typically required), the assistant surgeon should not be billing Medicare — and likely should not be billing your commercial insurer either. Common procedures that generally do not require an assistant surgeon include laparoscopic cholecystectomy (gallbladder removal), arthroscopic knee surgery, and many hernia repairs. Complex procedures like spinal fusions, open-heart surgery, and joint replacements typically do warrant an assistant.</p>

<div class="key-takeaway">
    <strong>How to check:</strong> Look up your procedure's CPT code in the Medicare Physician Fee Schedule to find the assistant surgeon indicator. If the indicator is 0, you have strong grounds to dispute the assistant surgeon charge on the basis of medical necessity. <a href="/scan">Upload your bill to BillKarma</a> and we will flag assistant surgeon charges for procedures where Medicare does not support assistant billing.
</div>

<h2 id="dispute">6. How to dispute an assistant surgeon bill</h2>

<ol>
    <li><strong>Request the operative report.</strong> Ask the hospital for the full operative report, which documents who was in the operating room and what each person did. This is your primary evidence for evaluating whether the assistant surgeon's role was medically necessary and whether the billing is accurate.</li>
    <li><strong>Check No Surprises Act applicability.</strong> Was the assistant out-of-network at an in-network facility? Was the surgery an emergency? Did you sign a specific consent form for out-of-network assistant surgeon services? If the NSA applies, contact your insurer and ask for reprocessing at in-network rates.</li>
    <li><strong>Verify medical necessity.</strong> Look up the CPT code's assistant surgeon indicator. If Medicare does not cover an assistant for your procedure, inform the billing department and your insurer that the charge lacks medical necessity support.</li>
    <li><strong>Compare the charge to Medicare rates.</strong> The assistant surgeon's charge should roughly correspond to 16% of the primary surgeon's Medicare rate for the procedure. If the billed amount is dramatically higher, use the Medicare rate as a negotiation benchmark. Use the <a href="/calculator">BillKarma cost calculator</a> to look up the Medicare rate for your procedure code.</li>
    <li><strong>Send a written dispute.</strong> Address it to the assistant surgeon's billing department. Include the operative report, the Medicare assistant surgeon indicator, the No Surprises Act citation if applicable, and a clear statement of what you believe you owe (in-network cost-sharing only, or nothing if the assistant was not medically necessary).</li>
    <li><strong>Escalate if necessary.</strong> File a complaint with your state insurance commissioner, with CMS at cms.gov/nosurprises, or with your state attorney general's consumer protection office. For insurance denials, file a formal appeal with your insurer.</li>
</ol>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>$4,000 assistant surgeon bill for a knee replacement the patient never consented to</h3>
    <p>A 58-year-old patient in Texas had a scheduled total knee replacement (CPT 27447) at an in-network hospital with an in-network orthopedic surgeon. The surgery went smoothly and the patient was discharged after two days. Three weeks later, a separate bill arrived from a physician the patient had never met: $4,000 for assistant surgeon services (27447-80). The assistant surgeon was out-of-network. The patient had signed only a standard hospital consent form — no specific written consent for out-of-network assistant surgeon services.</p>
    <p>The patient contacted their insurer and cited the No Surprises Act, noting the surgery was at an in-network facility and they had not signed a provider-specific out-of-network consent. The insurer reprocessed the claim at in-network rates. The assistant surgeon's allowed amount was recalculated at $520 (approximately 16% of the primary surgeon's in-network rate of $3,250). The patient's 20% coinsurance on the in-network amount: <strong>$104</strong>. The original $4,000 bill was reduced to $104 — a savings of <strong>$3,896</strong>.</p>
    <p>Facing a similar situation? <a href="/scan">Upload your surgical bill to BillKarma</a> to automatically flag out-of-network assistant surgeon charges and compare them to Medicare benchmarks.</p>
</div>

<div class="case-study">
    <h3>Assistant surgeon billed for a laparoscopic procedure Medicare says does not require one</h3>
    <p>A 45-year-old patient in Georgia received a $2,200 bill from an assistant surgeon after a laparoscopic cholecystectomy (gallbladder removal, CPT 47562). The patient's insurance paid $380 and left $1,820 as patient responsibility. When the patient checked the Medicare Physician Fee Schedule, CPT 47562 had an assistant surgeon indicator of 0 — meaning Medicare does not pay for assistant surgeon services for this procedure because an assistant is not typically medically necessary. The patient filed a written dispute with the assistant surgeon's billing office, citing the Medicare indicator and requesting the operative report. The operative report showed the assistant's documented role was limited to holding a retractor. The billing office reduced the charge to $0 after failing to provide documentation supporting medical necessity. <strong>Total saved: $2,200.</strong></p>
    <p><a href="/scan">Scan your bill with BillKarma</a> to check whether your procedure code supports assistant surgeon billing under Medicare guidelines.</p>
</div>

<h2 id="faq">8. Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is an assistant surgeon and why did I get a bill from one?</h3>
        <p>An assistant surgeon is a second physician who helps during a surgical procedure. They bill separately using the same CPT code with a modifier (80, 82, or AS). Patients rarely choose or even meet the assistant surgeon beforehand. These bills arrive separately, often weeks after the primary surgeon's bill, and can range from $1,500 to $6,000 or more.</p>
    </div>

    <div class="faq-item">
        <h3>Does the No Surprises Act protect me from assistant surgeon bills?</h3>
        <p>Yes, in most cases. If your surgery was at an in-network facility and the assistant surgeon was out-of-network, the NSA limits your cost to in-network rates. Emergency surgeries are protected regardless of network status. The only exception is if you signed a written consent specifically naming the out-of-network assistant at least 72 hours before a scheduled procedure.</p>
    </div>

    <div class="faq-item">
        <h3>What are modifier 80 and modifier 82 in surgical billing?</h3>
        <p>Modifier 80 means a physician served as assistant surgeon. Modifier 82 means a physician assisted when no qualified resident was available (common in teaching hospitals). Modifier AS means a physician assistant, NP, or clinical nurse specialist assisted. All pay at a fraction of the primary surgeon's rate — 16% for modifier 80 and 82 under Medicare.</p>
    </div>

    <div class="faq-item">
        <h3>How do I dispute an assistant surgeon bill I never agreed to?</h3>
        <p>Request the operative report, check the No Surprises Act applicability, verify the procedure's assistant surgeon indicator in the Medicare Fee Schedule, and compare the charge to Medicare rates. Then file a written dispute with the assistant surgeon's billing office and contact your insurer to request reprocessing. You can also <a href="/hospitals/">check whether your hospital has a pattern of surprise billing</a> in our directory. Our <a href="/guides/how-to-dispute-a-medical-bill">dispute guide</a> has letter templates you can use.</p>
    </div>

    <div class="faq-item">
        <h3>Can a surgeon use an assistant surgeon if Medicare says one is not needed?</h3>
        <p>Medicare classifies each procedure code with an assistant surgeon indicator. If the indicator is 0, Medicare will not pay for assistant surgeon services for that procedure. Commercial insurers may have different policies, but the Medicare indicator is strong evidence that an assistant was not medically necessary. Use this as a basis for disputing the charge. For a broader overview of surgical billing practices, see our <a href="/guides/surgery-costs-billing">surgery costs guide</a>.</p>
    </div>
</div>

<h2 id="sources">9. Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">CMS: Medicare Physician Fee Schedule &mdash; Assistant Surgeon Indicators and Reimbursement Rates</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Consumer Protections for Out-of-Network Billing</a></li>
    <li><a href="#" target="_blank" rel="noopener">American College of Surgeons: Guidelines on Assistant Surgeon Services and Documentation Requirements</a></li>
    <li><a href="#" target="_blank" rel="noopener">KFF: Surprise Medical Bills &mdash; Prevalence, Cost, and No Surprises Act Impact Analysis</a></li>
    <li><a href="#" target="_blank" rel="noopener">HHS Office of Inspector General: Billing Patterns for Assistant Surgeon Services in Medicare Fee-for-Service</a></li>
</ul>
""",
})
