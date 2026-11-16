"""Guide: upcoding and unbundling on hospital bills."""

from guides import register, _embed

register("upcoding-unbundling-hospital-bills", {
    "title": "Upcoding and Unbundling on Hospital Bills: How to Spot Them",
    "meta_description": "Upcoding bills a higher level than the care you got; unbundling bills one service as several. How to spot both on an itemized bill and ask for a correction.",
    "published": "2026-11-11",
    "author": "BillKarma Team",
    "category": "Billing Errors",
    "faqs": [
        {
            "q": "What is the difference between upcoding and unbundling?",
            "a": "Upcoding means a service is billed at a higher level than the care you received, such as a level 5 emergency visit for a sprained ankle. Unbundling means a service that has one code is billed as several separate codes, which raises the total.",
        },
        {
            "q": "Is upcoding the same as fraud?",
            "a": "No. Coding mistakes happen, and a high level can be correct for a complex visit. Knowingly billing a higher level than the care justified is fraud, but you can't tell intent from a bill. Ask the hospital in writing to review the code before drawing that conclusion.",
        },
        {
            "q": "Can modifier 59 on a bill be legitimate?",
            "a": "Yes. Modifier 59 and the X modifiers (XE, XS, XP, XU) tell the payer that two services that are usually bundled were distinct, for example done in separate sessions or on different body sites. They are legitimate when the medical record supports them and a flag worth questioning when it doesn't.",
        },
        {
            "q": "What should I ask the hospital for?",
            "a": "An itemized bill with the billing code on every line, and a coding review of the specific lines you question. You can also request a copy of your medical record to compare it with what was billed.",
        },
        {
            "q": "Where do I report suspected Medicare fraud?",
            "a": "Medicare patients can report suspected fraud to the Office of Inspector General at HHS, and anyone can call the fraud line printed on their insurer's member materials. Do that in addition to, not instead of, disputing the charge with the hospital.",
        },
    ],
    "body": f"""
<p class="lead"><strong>Upcoding</strong> means a hospital bills a higher level of service than the care you received. <strong>Unbundling</strong> means it bills separately for pieces of one service. Both raise your bill, both can be honest mistakes, and both can be questioned in writing with an itemized bill in hand.</p>

<p>Neither is proof of fraud, and neither is rare enough to ignore. Federal auditors have found the pattern in the data: the HHS Office of Inspector General reported that physicians shifted emergency department billing toward the highest code, 99285, by 21% between 2001 and 2010 while billing the four lower levels less often. The same report cautions that high-level codes don't necessarily mean fraud. A later OIG report found the highest-severity hospital stays rose almost 20% from fiscal 2014 to 2019 and reached nearly half of Medicare spending on inpatient stays, which OIG said made them vulnerable to upcoding.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#upcoding">What upcoding looks like</a></li>
        <li><a href="#unbundling">What unbundling looks like</a></li>
        <li><a href="#example">A bill with both problems</a></li>
        <li><a href="#when-legit">When it is not an error</a></li>
        <li><a href="#what-to-do">What to do about it</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="upcoding">1. What upcoding looks like</h2>

<p>Emergency visits are billed on a five-level scale. The level is meant to reflect how serious the problem was and how much work it took to treat.</p>

<table>
    <thead>
        <tr><th>Code</th><th>Level</th><th>Typical problem</th></tr>
    </thead>
    <tbody>
        <tr><td>99281</td><td>1</td><td>Small cut, minor rash</td></tr>
        <tr><td>99282</td><td>2</td><td>Sprained ankle, ear infection</td></tr>
        <tr><td>99283</td><td>3</td><td>Abdominal pain, asthma attack, broken bone</td></tr>
        <tr><td>99284</td><td>4</td><td>Chest pain, severe allergic reaction</td></tr>
        <tr><td>99285</td><td>5</td><td>Heart attack, stroke, major trauma</td></tr>
    </tbody>
</table>

<p>Compare the level on your bill with why you went and what was done. A level 5 charge after a visit that ended with an elastic bandage is worth a question. Each level is priced above the one below it, so the difference between levels shows up directly on the bill.</p>

<div class="key-takeaway">
    <strong>Ask which level and why.</strong> Write to billing and ask what criteria the hospital used to assign the level on your visit. <a href="/scan">BillKarma's free check</a> flags level 4 and 5 emergency visits so you know which lines to ask about.
</div>

<h2 id="unbundling">2. What unbundling looks like</h2>

<p>Unbundling is billing several codes for something one code already covers. Medicare's National Correct Coding Initiative (NCCI) publishes pairs of codes that normally shouldn't be billed together for the same patient on the same day; each pair has a modifier indicator that says whether an exception is allowed. Many private insurers use the same logic.</p>

<p>Three pairs show up constantly on lab and ER bills:</p>

<table>
    <thead>
        <tr><th>Billed together</th><th>Why it's a question</th></tr>
    </thead>
    <tbody>
        <tr><td>80048 basic metabolic panel and 80053 comprehensive metabolic panel</td><td>The basic panel is a subset of the comprehensive one</td></tr>
        <tr><td>85025 blood count with differential and 85027 blood count without</td><td>The second is included in the first</td></tr>
        <tr><td>36415 venipuncture and 36416 capillary blood draw</td><td>One blood collection, two collection charges</td></tr>
    </tbody>
</table>

{_embed(mode="markup", title="How far above Medicare is your charge?", subtitle="Enter a billing code and the amount charged.", height="420")}

<h2 id="example">3. A bill with both problems</h2>

<p>This is an illustrative emergency bill for a sprained ankle. The amounts are made up to show the pattern.</p>

<table>
    <thead>
        <tr><th>Code</th><th>Description</th><th>Charged</th><th>Question</th></tr>
    </thead>
    <tbody>
        <tr><td>99285</td><td>Emergency visit, level 5</td><td class="bk-num">$4,500</td><td>Level 5 is for threats to life; this visit ended with a splint</td></tr>
        <tr><td>73610</td><td>Ankle X-ray</td><td class="bk-num">$610</td><td>None</td></tr>
        <tr><td>80048</td><td>Basic metabolic panel</td><td class="bk-num">$142</td><td>Included in the next line</td></tr>
        <tr><td>80053</td><td>Comprehensive metabolic panel</td><td class="bk-num">$198</td><td>Billed with the basic panel</td></tr>
        <tr><td>36415</td><td>Venipuncture</td><td class="bk-num">$38</td><td>None</td></tr>
        <tr><td>36416</td><td>Capillary blood draw</td><td class="bk-num">$41</td><td>Second collection charge for one draw</td></tr>
    </tbody>
</table>

<p>Two of these lines ($142 and $41) are likely billing errors that the hospital should remove. The level 5 charge is a question for the hospital's coding team: a lower level would reduce it by an amount depending on the hospital's price list. Each is a separate line you can dispute in writing.</p>

<h2 id="when-legit">4. When it is not an error</h2>

<ul>
    <li><strong>Distinct services.</strong> Modifier 59, or one of the X modifiers (XE, XS, XP, XU), tells the payer the two services were separate: different sessions, different sites or different organ systems. When the record supports it, billing both is correct.</li>
    <li><strong>A complicated visit.</strong> A sprained ankle in a patient on blood thinners with a head injury is not a simple visit. The level depends on what was evaluated, not only on the final diagnosis.</li>
    <li><strong>Two real blood draws.</strong> If you were stuck twice at different times, two collection charges can be right.</li>
</ul>

<p>That is why the right move is a written question, not an accusation. Ask for the coding to be reviewed and for the reason if it stands.</p>

<h2 id="what-to-do">5. What to do about it</h2>

<ol>
    <li><strong>Get the itemized bill with codes.</strong> A summary bill won't show them. See <a href="/guides/how-to-get-itemized-hospital-bill/">how to get an itemized hospital bill</a>.</li>
    <li><strong>Mark the lines.</strong> Circle the emergency level, any code pair like those above and any line with a modifier.</li>
    <li><strong>Write to billing.</strong> Name each line, say what you think is wrong, and ask for a coding review and a corrected bill. Our guide to <a href="/guides/how-to-dispute-a-medical-bill/">disputing a medical bill</a> has the letter structure.</li>
    <li><strong>Protect the account.</strong> Ask the hospital to keep the bill out of collections while the dispute is open, and keep copies of everything you send.</li>
</ol>

<div class="key-takeaway">
    <strong>Want it sent for you?</strong> BillKarma checks every line, writes the dispute and mails it for a flat $29&ndash;$149, with a refund if the bill isn't reduced in 45 days. <a href="/scan">Start with the free check.</a>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the difference between upcoding and unbundling?</h3>
        <p>Upcoding means a service is billed at a higher level than the care you received, such as a level 5 emergency visit for a sprained ankle. Unbundling means a service that has one code is billed as several separate codes, which raises the total.</p>
    </div>
    <div class="faq-item">
        <h3>Is upcoding the same as fraud?</h3>
        <p>No. Coding mistakes happen, and a high level can be correct for a complex visit. Knowingly billing a higher level than the care justified is fraud, but you can't tell intent from a bill. Ask the hospital in writing to review the code before drawing that conclusion.</p>
    </div>
    <div class="faq-item">
        <h3>Can modifier 59 on a bill be legitimate?</h3>
        <p>Yes. Modifier 59 and the X modifiers tell the payer that two services that are usually bundled were distinct. They are legitimate when the medical record supports them and a flag worth questioning when it doesn't.</p>
    </div>
    <div class="faq-item">
        <h3>What should I ask the hospital for?</h3>
        <p>An itemized bill with the billing code on every line, and a coding review of the specific lines you question. You can also request a copy of your medical record to compare it with what was billed.</p>
    </div>
    <div class="faq-item">
        <h3>Where do I report suspected Medicare fraud?</h3>
        <p>Medicare patients can report suspected fraud to the Office of Inspector General at HHS, and anyone can call the fraud line printed on their insurer's member materials. Do that in addition to, not instead of, disputing the charge with the hospital.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://aapc.com/codes/scc_articles/article_pdf/44/compliance-oig-to-send-cms-names-of-1700-docs-who-overbilled-high-level-em-codes-111243" target="_blank" rel="noopener">AAPC: summary of the HHS-OIG report on Medicare E/M coding trends, 2001&ndash;2010 (OEI-04-10-00180)</a></li>
    <li><a href="https://www.nelsonmullins.com/insights/blogs/healthcare_essentials/federal-healthcare-policy-developments/increased-enforcement-activity-expected-relating-to-healthcare-provider-billing-upcoding" target="_blank" rel="noopener">Nelson Mullins: summary of OIG's report on rising highest-severity inpatient stays, FY2014&ndash;2019</a></li>
    <li><a href="https://www.cms.gov/files/document/r13701cp.pdf" target="_blank" rel="noopener">CMS: Claims Processing Manual, Chapter 23 section 20.9, National Correct Coding Initiative</a></li>
    <li><a href="https://med.noridianmedicare.com/web/jfb/topics/claim-submission/ncci" target="_blank" rel="noopener">Noridian Medicare: NCCI edits and modifiers 59 and X{{EPSU}}</a></li>
    <li><a href="https://www.regence.com/web/regence_provider/bundling-edits" target="_blank" rel="noopener">Regence: bundling edits policy, definition of unbundling</a></li>
</ul>
""",
})
