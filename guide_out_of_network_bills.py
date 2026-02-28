"""Guide: Out-of-Network Medical Bills."""

from guides import register, _embed

register("out-of-network-medical-bills", {
    "title": "Out-of-Network Medical Bills: Your Rights, Protections, and How to Fight Back",
    "meta_description": "Out-of-network bills can cost 2-5x more than in-network. Learn your rights under the No Surprises Act, how insurance calculates OON reimbursement, and 7 steps to fight back.",
    "published": "2026-02-28",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What does out-of-network mean on a medical bill?",
            "a": "Out-of-network means the provider does not have a contract with your insurance company. Without a contract, the provider can charge whatever they want (their full chargemaster rate), and your insurer will only reimburse a fraction of that amount — often 50-80% of what they consider 'usual and customary.' You are responsible for the gap between the insurer's payment and the provider's full charge, which is called a balance bill.",
        },
        {
            "q": "Am I protected from surprise out-of-network bills?",
            "a": "Under the No Surprises Act (effective January 1, 2022), you are protected from surprise out-of-network bills in three situations: emergency services at any facility, care from out-of-network providers at in-network facilities you didn't choose, and air ambulance transport. In these cases, you can only be charged in-network cost-sharing rates. You are NOT protected for ground ambulance, elective out-of-network care you chose, or post-stabilization care where you gave written consent.",
        },
        {
            "q": "How much more does out-of-network care cost compared to in-network?",
            "a": "Out-of-network care typically costs 2-5 times more than in-network care. For example, an in-network MRI might cost $500 after insurance, while the same MRI out-of-network could cost $2,000-$3,500 because your insurer pays less and the provider charges more. The gap is largest for facility-based services like surgeries and hospital stays, where out-of-network charges can run tens of thousands of dollars above what insurance covers.",
        },
        {
            "q": "Can I negotiate an out-of-network medical bill?",
            "a": "Yes. Out-of-network bills are often the most negotiable because the provider's chargemaster rate is not a contracted price — it's their starting ask. Request a cash-pay or self-pay discount (many providers offer 30-60% off). Use the Medicare rate or FAIR Health benchmark as a negotiating anchor. Ask for an itemized bill first to identify errors. Many providers will accept significantly less than the initial charge rather than send the account to collections.",
        },
        {
            "q": "What is an in-network exception and how do I get one?",
            "a": "An in-network exception (also called a gap exception or network adequacy exception) is when your insurer agrees to cover an out-of-network provider at in-network rates. Insurers typically grant these when there is no in-network specialist within a reasonable distance (often 30-60 miles), when you need continuity of care with an existing provider who left the network, or when no in-network provider has the specific expertise you need. Submit a written request to your insurer with supporting documentation from your doctor.",
        },
        {
            "q": "How does my insurance calculate out-of-network reimbursement?",
            "a": "Insurers use one of several methods: a percentage of the Medicare rate (e.g., 150-200% of Medicare), the 'usual, customary, and reasonable' (UCR) rate based on what providers in your area charge, or a FAIR Health benchmark (a nonprofit database of actual charges). The method your insurer uses matters enormously — a procedure reimbursed at 150% of Medicare might pay $300, while the same procedure reimbursed at the 80th percentile of FAIR Health data might pay $800. Check your plan documents to see which method applies.",
        },
    ],
    "body": f"""
<p class="lead">An out-of-network doctor can charge whatever they want &mdash; and your insurance may cover only a fraction. The average out-of-network bill is <strong>2&ndash;5 times higher</strong> than what you&rsquo;d pay in-network, and patients are often left with thousands in unexpected charges. But since the No Surprises Act took effect in 2022, you have more protections than ever. This guide covers when you&rsquo;re protected, when you&rsquo;re not, and exactly how to fight unfair out-of-network charges.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-oon-means">What &ldquo;out-of-network&rdquo; actually means</a></li>
        <li><a href="#no-surprises-act">No Surprises Act protections (2022+)</a></li>
        <li><a href="#cost-comparison">How much more out-of-network costs</a></li>
        <li><a href="#balance-billing">The &ldquo;balance billing&rdquo; trap</a></li>
        <li><a href="#reimbursement-methods">How insurance calculates out-of-network reimbursement</a></li>
        <li><a href="#how-to-fight">How to fight an out-of-network bill</a></li>
        <li><a href="#in-network-exception">Getting an in-network exception</a></li>
        <li><a href="#elective-oon">When you chose to go out-of-network</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-oon-means">1. What &ldquo;out-of-network&rdquo; actually means</h2>

<p>When a doctor or hospital is &ldquo;in-network,&rdquo; they have a contract with your insurance company. That contract sets a <strong>negotiated rate</strong> for every service &mdash; and the provider agrees to accept that rate as payment in full. You pay your cost-sharing (copay, coinsurance, deductible) based on that negotiated rate, and the provider writes off the rest.</p>

<p>When a provider is <strong>out-of-network</strong>, there is no contract. Two things happen that dramatically increase your costs:</p>

<ul>
    <li><strong>The provider charges their full &ldquo;chargemaster&rdquo; rate.</strong> This is the sticker price &mdash; often 3&ndash;10x the Medicare rate for the same service. Without a contract, they have no obligation to discount anything.</li>
    <li><strong>Your insurer pays based on their &ldquo;allowed amount&rdquo; for out-of-network care.</strong> This is typically far less than the provider&rsquo;s full charge. The insurer might allow $400 for a service the provider billed at $2,000.</li>
</ul>

<p>The gap between the provider&rsquo;s charge and what your insurance pays is called the <strong>balance</strong> &mdash; and the provider can bill you for it. This is the core problem with out-of-network care.</p>

<div class="bill-example">
    <div class="bill-header">In-Network vs. Out-of-Network: Same Service, Different Cost</div>
    <div class="line-item">
        <span><strong>In-network scenario</strong></span>
        <span></span>
    </div>
    <div class="line-item">
        <span>Provider&rsquo;s billed charge</span>
        <span>$2,000.00</span>
    </div>
    <div class="line-item">
        <span>Negotiated (contracted) rate</span>
        <span>$800.00</span>
    </div>
    <div class="line-item">
        <span>Insurance pays (80% coinsurance)</span>
        <span>$640.00</span>
    </div>
    <div class="line-item">
        <span>You pay (20% of negotiated rate)</span>
        <span>$160.00</span>
    </div>
    <div class="line-item">
        <span><strong>Out-of-network scenario (same service)</strong></span>
        <span></span>
    </div>
    <div class="line-item">
        <span>Provider&rsquo;s billed charge</span>
        <span>$2,000.00</span>
    </div>
    <div class="line-item">
        <span>Insurer&rsquo;s allowed amount (OON)</span>
        <span>$400.00</span>
    </div>
    <div class="line-item">
        <span>Insurance pays (60% of allowed)</span>
        <span>$240.00</span>
    </div>
    <div class="line-item error">
        <span>You pay (40% coinsurance + balance bill) &nbsp; &#10060;</span>
        <span>$1,760.00</span>
    </div>
</div>

<p>In this example, the same $2,000 service costs you <strong>$160 in-network</strong> versus <strong>$1,760 out-of-network</strong> &mdash; an 11x difference. The out-of-network cost is driven by two factors: your insurer pays less (the allowed amount is lower), and you&rsquo;re responsible for the entire gap between the allowed amount and the provider&rsquo;s full charge.</p>

<div class="key-takeaway">
    <strong>The key concept:</strong> In-network, you&rsquo;re protected by a contract that caps what you pay. Out-of-network, there is no cap &mdash; the provider&rsquo;s full charge becomes your problem. Understanding this difference is the first step to protecting yourself.
</div>

<h2 id="no-surprises-act">2. No Surprises Act protections (2022+)</h2>

<p>The <a href="/guides/no-surprises-act-explained">No Surprises Act (NSA)</a>, effective January 1, 2022, created the first comprehensive federal protections against unexpected out-of-network charges. Here&rsquo;s what it covers and what it doesn&rsquo;t.</p>

<h3>You ARE protected in these situations</h3>

<p><strong>Emergency services (always protected):</strong> If you go to any emergency room, every provider who treats you &mdash; ER physicians, radiologists, anesthesiologists, surgeons &mdash; must bill you at in-network cost-sharing rates, regardless of their network status. This applies even if the hospital itself is out-of-network. You cannot be balance billed for emergency care.</p>

<p><strong>Surprise bills at in-network facilities:</strong> If you schedule a procedure at an in-network hospital or surgery center and are treated by an out-of-network provider you didn&rsquo;t choose (the anesthesiologist, the pathologist, the assistant surgeon), you&rsquo;re protected. That out-of-network provider cannot balance bill you &mdash; you pay only your in-network cost-sharing.</p>

<p><strong>Air ambulance transport:</strong> Out-of-network air ambulance providers (helicopter and fixed-wing) cannot balance bill you. Your cost-sharing is calculated at in-network rates.</p>

<h3>You are NOT protected in these situations</h3>

<ul>
    <li><strong>Ground ambulance:</strong> The biggest gap in the law. Ground ambulance bills average $1,200&ndash;$2,500, and out-of-network ground ambulance providers can still balance bill you the full gap.</li>
    <li><strong>Post-stabilization care with consent:</strong> After an ER visit, once you&rsquo;re medically stable, a provider can ask you to consent to out-of-network care. If you sign a valid written consent (given at least 72 hours or 3 hours before the service, depending on scheduling), you may waive your NSA protections.</li>
    <li><strong>Out-of-network facilities you chose:</strong> If you voluntarily go to an out-of-network hospital or clinic for non-emergency care, the NSA&rsquo;s balance billing ban does not apply.</li>
    <li><strong>Medicare, Medicaid, TRICARE, VA:</strong> These programs have their own billing protections. The NSA applies to commercial insurance plans.</li>
</ul>

<div class="key-takeaway">
    <strong>Bottom line:</strong> The No Surprises Act protects you when the out-of-network element was not your choice &mdash; emergencies, and providers you didn&rsquo;t pick at in-network facilities. If you chose to go out-of-network, the protections generally don&rsquo;t apply. For a full breakdown of what&rsquo;s covered, see our <a href="/guides/no-surprises-act-explained">No Surprises Act guide</a>.
</div>

<h2 id="cost-comparison">3. How much more out-of-network costs</h2>

<p>The cost difference between in-network and out-of-network care varies by procedure, but the pattern is consistent: out-of-network care costs <strong>2&ndash;5 times more</strong> on average. For some services, the gap is even wider.</p>

<table>
    <thead>
        <tr><th>Procedure</th><th>Typical In-Network Cost (after insurance)</th><th>Typical Out-of-Network Cost (after insurance)</th><th>Difference</th></tr>
    </thead>
    <tbody>
        <tr><td>ER visit (Level 4, CPT 99284)</td><td>$250&ndash;$500</td><td>$1,500&ndash;$4,000</td><td>3&ndash;8x more</td></tr>
        <tr><td>MRI (brain, CPT 70553)</td><td>$300&ndash;$600</td><td>$1,200&ndash;$3,500</td><td>3&ndash;6x more</td></tr>
        <tr><td>Knee replacement surgery (CPT 27447)</td><td>$5,000&ndash;$10,000</td><td>$20,000&ndash;$50,000</td><td>3&ndash;5x more</td></tr>
        <tr><td>Childbirth (vaginal delivery, CPT 59400)</td><td>$2,000&ndash;$5,000</td><td>$8,000&ndash;$20,000</td><td>3&ndash;4x more</td></tr>
        <tr><td>Colonoscopy (CPT 45378)</td><td>$200&ndash;$500</td><td>$1,000&ndash;$3,000</td><td>3&ndash;6x more</td></tr>
        <tr><td>Physical therapy session (CPT 97110)</td><td>$30&ndash;$75</td><td>$150&ndash;$350</td><td>3&ndash;5x more</td></tr>
    </tbody>
</table>

<p>These ranges reflect national averages. Your actual cost depends on your plan&rsquo;s out-of-network benefits (deductible, coinsurance, out-of-pocket maximum), the provider&rsquo;s charges, and how your insurer calculates out-of-network reimbursement.</p>

<p><strong>Why the gap is so large:</strong> It&rsquo;s not just that the provider charges more &mdash; your insurer also covers less. In-network, your plan might cover 80% of the negotiated rate. Out-of-network, it might cover only 50&ndash;60% of a much lower &ldquo;allowed amount.&rdquo; You get squeezed on both sides.</p>

<p><a href="/scan">Upload your out-of-network bill to BillKarma</a> to see how your charges compare to Medicare rates and FAIR Health benchmarks. We&rsquo;ll show you exactly how much above the market rate you were charged.</p>

{_embed(mode="cost", title="Compare your out-of-network charges", subtitle="Enter a CPT code to see Medicare and fair-market rates for your area.", height="420")}

<h2 id="balance-billing">4. The &ldquo;balance billing&rdquo; trap</h2>

<p><a href="/guides/balance-billing">Balance billing</a> is what happens when an out-of-network provider bills you for the difference between their full charge and what your insurance paid. It&rsquo;s the single biggest financial risk of out-of-network care.</p>

<p><strong>How it works:</strong> A surgeon charges $15,000 for a procedure. Your insurer&rsquo;s out-of-network allowed amount is $5,000. The insurer pays 60% of that ($3,000) and applies the other $2,000 to your coinsurance. The surgeon then sends you a <strong>balance bill</strong> for the remaining $10,000 ($15,000 minus the insurer&rsquo;s $5,000 allowed amount). Your total cost: $12,000 &mdash; the $2,000 coinsurance plus the $10,000 balance bill.</p>

<p>The No Surprises Act banned balance billing in certain situations (see Section 2 above), but it&rsquo;s still legal for elective out-of-network care in many cases. However, <strong>many states have their own balance billing protections</strong> that go further than federal law.</p>

<h3>States with balance billing protections beyond federal law</h3>

<table>
    <thead>
        <tr><th>State</th><th>Key Protection</th><th>Effective</th></tr>
    </thead>
    <tbody>
        <tr><td>California</td><td>Comprehensive ban on balance billing for emergency and non-emergency at in-network facilities; covers ground ambulance in many cases</td><td>2017</td></tr>
        <tr><td>New York</td><td>Emergency and surprise bill protections with independent arbitration; covers most facility-based providers</td><td>2015</td></tr>
        <tr><td>Texas</td><td>Balance billing ban for emergency care and facility-based providers at in-network facilities; state IDR process</td><td>2020</td></tr>
        <tr><td>Colorado</td><td>Surprise billing protections including ground ambulance in certain situations; covers HMO and PPO plans</td><td>2020</td></tr>
        <tr><td>Illinois</td><td>Prohibits balance billing for emergency and non-emergency OON providers at in-network facilities</td><td>2022</td></tr>
        <tr><td>Florida</td><td>Balance billing protections for HMO and PPO members; covers emergency and facility-based providers</td><td>2016</td></tr>
        <tr><td>Connecticut</td><td>Prohibits balance billing for emergency services and surprise out-of-network care</td><td>2016</td></tr>
        <tr><td>Georgia</td><td>Surprise billing protections for emergency and non-emergency services at in-network facilities</td><td>2021</td></tr>
        <tr><td>Maryland</td><td>Prohibits balance billing for covered emergency services and at in-network facilities</td><td>2021</td></tr>
        <tr><td>New Jersey</td><td>Comprehensive surprise bill law covering emergency, out-of-network referrals, and inadvertent OON care</td><td>2019</td></tr>
        <tr><td>New Mexico</td><td>Surprise billing protections for emergency care and facility-based providers</td><td>2019</td></tr>
        <tr><td>Oregon</td><td>Prohibits balance billing for emergency services; covers some non-emergency OON care</td><td>2020</td></tr>
        <tr><td>Virginia</td><td>Balance billing protections for emergency services and certain elective procedures at in-network facilities</td><td>2021</td></tr>
        <tr><td>Washington</td><td>Balance billing ban for emergency services; covers behavioral health and surgical services at in-network facilities</td><td>2019</td></tr>
        <tr><td>Michigan</td><td>Surprise billing protections for emergency and non-emergency at in-network hospitals; applies to fully insured plans</td><td>2022</td></tr>
        <tr><td>Ohio</td><td>Prohibits balance billing for emergency care and surprise OON providers at in-network hospitals</td><td>2023</td></tr>
    </tbody>
</table>

<p><strong>Federal vs. state overlap:</strong> When both federal and state protections apply, you get whichever is more favorable. Some state laws cover situations the No Surprises Act doesn&rsquo;t &mdash; like ground ambulance (California, Colorado) or broader definitions of surprise billing. Check your state&rsquo;s insurance commissioner website for the most current rules.</p>

<div class="key-takeaway">
    <strong>Even if you live in a state without additional protections,</strong> the federal No Surprises Act covers surprise out-of-network bills in emergencies and at in-network facilities. For a deep dive into balance billing law and state-specific protections, see our <a href="/guides/balance-billing">balance billing guide</a>.
</div>

<h2 id="reimbursement-methods">5. How insurance calculates out-of-network reimbursement</h2>

<p>When you receive out-of-network care, your insurer doesn&rsquo;t just pick a random number to reimburse. They use a specific method &mdash; and which method your plan uses can mean a difference of <strong>hundreds or thousands of dollars</strong> in what you owe.</p>

<h3>Method 1: Percentage of Medicare</h3>
<p>Your insurer pays a multiple of the Medicare rate for the service &mdash; typically 125&ndash;200% of Medicare. Example: If Medicare pays $500 for a procedure and your plan uses 150% of Medicare, the allowed amount is $750. This method tends to produce the <strong>lowest reimbursement</strong> because Medicare rates are well below commercial rates.</p>

<h3>Method 2: Usual, Customary, and Reasonable (UCR)</h3>
<p>Your insurer determines a &ldquo;reasonable&rdquo; charge based on what providers in your geographic area typically charge for the service. This sounds fair, but insurers often use outdated or narrow data sets, setting the UCR well below what most providers actually charge. The term &ldquo;usual and customary&rdquo; is defined by the insurer, not an independent body.</p>

<h3>Method 3: FAIR Health benchmark</h3>
<p>Some plans use data from <a href="https://www.fairhealth.org" target="_blank" rel="noopener">FAIR Health</a>, a nonprofit that maintains a database of actual billed charges from providers across the country. Plans might reimburse at the 70th, 80th, or 90th percentile of FAIR Health data for your region. This method typically produces the <strong>highest reimbursement</strong> and is considered the most transparent.</p>

<h3>Why the method matters</h3>

<div class="bill-example">
    <div class="bill-header">Same Service, Three Reimbursement Methods &mdash; CPT 27447 (Knee Replacement)</div>
    <div class="line-item">
        <span>Provider&rsquo;s charge</span>
        <span>$40,000.00</span>
    </div>
    <div class="line-item">
        <span>Medicare rate for this service</span>
        <span>$8,200.00</span>
    </div>
    <div class="line-item">
        <span><strong>Method 1:</strong> 150% of Medicare &mdash; allowed amount</span>
        <span>$12,300.00</span>
    </div>
    <div class="line-item">
        <span><strong>Method 2:</strong> UCR (insurer&rsquo;s data) &mdash; allowed amount</span>
        <span>$18,500.00</span>
    </div>
    <div class="line-item">
        <span><strong>Method 3:</strong> FAIR Health 80th percentile &mdash; allowed amount</span>
        <span>$28,400.00</span>
    </div>
</div>

<p>In this example, the allowed amount ranges from $12,300 to $28,400 &mdash; a <strong>$16,100 difference</strong> depending on which method your insurer uses. That $16,100 comes directly out of your pocket as a larger balance bill.</p>

<p><strong>Where to find your plan&rsquo;s method:</strong> Check your Summary of Benefits and Coverage (SBC) or plan documents. Look for terms like &ldquo;out-of-network reimbursement,&rdquo; &ldquo;allowed amount,&rdquo; &ldquo;maximum allowable charge,&rdquo; or &ldquo;reasonable and customary.&rdquo; If the documents are unclear, call your insurer and ask directly: &ldquo;How do you calculate the allowed amount for out-of-network claims?&rdquo;</p>

<h2 id="how-to-fight">6. How to fight an out-of-network bill</h2>

<p>If you&rsquo;ve received an out-of-network bill that seems unreasonable, don&rsquo;t pay it immediately. Follow these seven steps to reduce or eliminate the charges.</p>

<h3>Step 1: Get an itemized bill</h3>
<p>Request a detailed itemized bill showing every CPT code, description, and charge. Many out-of-network bills arrive as a single lump sum, which makes it impossible to evaluate whether the charges are reasonable. You have a legal right to an itemized statement. For help reading yours, see our <a href="/guides/how-to-get-itemized-hospital-bill">itemized bill guide</a>.</p>

<h3>Step 2: Compare charges to FAIR Health and Medicare benchmarks</h3>
<p>Look up each CPT code on <a href="https://www.fairhealthconsumer.org" target="_blank" rel="noopener">FAIR Health Consumer</a> and check the Medicare rate. If the provider&rsquo;s charge is significantly above the 80th percentile of FAIR Health data &mdash; or more than 3x the Medicare rate &mdash; you have strong evidence that the bill is inflated.</p>

<p><a href="/scan">Upload your bill to BillKarma</a> and we&rsquo;ll automatically compare every line item to Medicare and fair-market benchmarks, so you can see exactly where you&rsquo;re being overcharged.</p>

<h3>Step 3: Check if the No Surprises Act applies</h3>
<p>Was it an emergency? Were you at an in-network facility treated by an out-of-network provider you didn&rsquo;t choose? If yes, the <a href="/guides/no-surprises-act-explained">No Surprises Act</a> likely protects you. Contact your insurer and the provider, cite the NSA, and request the bill be reprocessed at in-network rates.</p>

<h3>Step 4: File an appeal with your insurance company</h3>
<p>If your insurer processed the claim at out-of-network rates and you believe it should be in-network (or the allowed amount is unreasonably low), file a formal appeal. Include FAIR Health data, Medicare rates, and any evidence that the charge exceeds reasonable market rates. For a step-by-step walkthrough, see our <a href="/guides/how-to-appeal-insurance-denial-and-win">appeal guide</a>.</p>

<h3>Step 5: Negotiate a cash-pay rate with the provider</h3>
<p>Call the provider&rsquo;s billing department and ask: &ldquo;What is your cash-pay or self-pay rate for this service?&rdquo; Many providers offer a cash-pay discount of 30&ndash;60% off their chargemaster rate. If the cash-pay rate is lower than what you owe after insurance, it may be cheaper to pay cash and skip insurance entirely.</p>

<h3>Step 6: Request an in-network exception</h3>
<p>If you had a valid reason for seeing an out-of-network provider (no in-network specialist available, continuity of care), ask your insurer for an in-network exception. This means they&rsquo;ll reprocess the claim at in-network rates. See Section 7 below for details on how to request one.</p>

<h3>Step 7: File a complaint</h3>
<p>If the provider refuses to negotiate or is violating the No Surprises Act, file a complaint with CMS at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> (federal) and with your state insurance commissioner. If you&rsquo;re being pursued for debt you don&rsquo;t owe, visit our <a href="/fight-debt">fight debt resources</a> for tools to protect yourself.</p>

<div class="case-study">
    <h3>Case study: Fighting a $14,200 out-of-network surgery bill</h3>
    <p>A patient had scheduled shoulder surgery at an in-network surgical center. The surgeon was in-network, but the anesthesiologist was out-of-network. The anesthesiologist billed <strong>$6,200</strong> (CPT 01630). The patient&rsquo;s insurer processed it out-of-network, allowing only $1,800 and leaving the patient with a $4,400 balance bill plus $200 in coinsurance.</p>
    <p>The patient followed the steps above: she confirmed the surgical center was in-network and she had not chosen the anesthesiologist. She cited the No Surprises Act to her insurer, which reprocessed the claim at in-network rates. Her final cost: a <strong>$50 in-network copay</strong>. Total savings: <strong>$4,550</strong>.</p>
    <p>Had the NSA not applied (e.g., if she had chosen to go to an out-of-network facility), she could still have negotiated: the Medicare rate for CPT 01630 is approximately $900, and the FAIR Health 80th percentile is approximately $2,100 &mdash; both far below the $6,200 billed charge.</p>
</div>

<h2 id="in-network-exception">7. Getting an in-network exception</h2>

<p>An in-network exception (sometimes called a &ldquo;gap exception,&rdquo; &ldquo;network adequacy exception,&rdquo; or &ldquo;single case agreement&rdquo;) is when your insurer agrees to cover an out-of-network provider at in-network benefit levels. This can save you thousands of dollars.</p>

<h3>When insurers typically grant exceptions</h3>

<ul>
    <li><strong>No in-network specialist within a reasonable distance:</strong> If the nearest in-network provider for your condition is 60+ miles away (thresholds vary by plan and state), your insurer may be required to grant an exception under network adequacy rules.</li>
    <li><strong>Continuity of care:</strong> If your doctor leaves your insurance network mid-treatment, many states require the insurer to allow you to continue seeing that provider at in-network rates for a transition period (typically 90 days, sometimes longer for active treatment like chemotherapy or pregnancy).</li>
    <li><strong>Specialized expertise:</strong> If no in-network provider has the specific sub-specialty expertise you need (e.g., a rare cancer requiring a specialist at a particular academic medical center), your insurer may grant an exception.</li>
</ul>

<h3>How to request an in-network exception</h3>

<ol>
    <li><strong>Call your insurer&rsquo;s member services line</strong> and ask for the &ldquo;network exception&rdquo; or &ldquo;gap exception&rdquo; process. Get the name and fax/email of the department that handles these requests.</li>
    <li><strong>Get a letter from your doctor</strong> explaining why the out-of-network provider is medically necessary. The letter should state that no in-network alternative is available or appropriate for your condition.</li>
    <li><strong>Submit a written request</strong> with your doctor&rsquo;s letter, documentation showing there is no adequate in-network alternative (search results from the insurer&rsquo;s own provider directory), and a statement of the specific services needed.</li>
    <li><strong>Follow up within 10 business days.</strong> If denied, appeal. Many initial denials are overturned on appeal, especially when documentation is strong.</li>
</ol>

<h3>Template language for your request</h3>

<div class="case-study">
    <h3>Sample in-network exception request language</h3>
    <p>&ldquo;I am writing to request an in-network exception for [Provider Name], [specialty], NPI [number]. I have been unable to locate an in-network provider within [X] miles of my home who can provide [specific treatment/service]. I searched your provider directory on [date] and contacted [number] listed providers, [X] of whom are not accepting new patients and [X] of whom do not treat my condition ([diagnosis]). My treating physician, Dr. [Name], has confirmed that [out-of-network provider] is the appropriate specialist for my care. I am attaching Dr. [Name]&rsquo;s letter of medical necessity. I respectfully request that [Provider Name] be approved as an in-network provider for this course of treatment.&rdquo;</p>
</div>

<p>Use our <a href="/calculator">cost calculator</a> to estimate what you&rsquo;d save if the claim is reprocessed at in-network rates versus out-of-network rates.</p>

<h2 id="elective-oon">8. When you chose to go out-of-network</h2>

<p>Sometimes you know a provider is out-of-network and you want to see them anyway &mdash; maybe they&rsquo;re the best surgeon for your procedure, or they were recommended by someone you trust. Elective out-of-network care is your right, but it requires financial planning.</p>

<h3>What to ask before scheduling</h3>

<ul>
    <li><strong>&ldquo;Will you request a single case agreement (SCA) with my insurer?&rdquo;</strong> An SCA is a one-time contract between the provider and your insurer for a specific service. If the provider agrees, your insurer negotiates a rate and you pay in-network cost-sharing. Not all providers or insurers will agree, but it&rsquo;s always worth asking.</li>
    <li><strong>&ldquo;Will you apply for a gap exception on my behalf?&rdquo;</strong> Some providers will submit the in-network exception paperwork for you. This is especially common with specialists at academic medical centers.</li>
    <li><strong>&ldquo;What is your cash-pay rate?&rdquo;</strong> Compare this to what you&rsquo;d owe going through insurance at out-of-network rates. Sometimes paying cash is cheaper than using your out-of-network benefits, especially if you haven&rsquo;t met your out-of-network deductible.</li>
    <li><strong>&ldquo;Can I get a written cost estimate?&rdquo;</strong> Under the No Surprises Act, uninsured and self-pay patients have a right to a Good Faith Estimate. Even if you have insurance, you can request an estimate of the total charges.</li>
    <li><strong>&ldquo;What does my insurance plan&rsquo;s out-of-network benefit look like?&rdquo;</strong> Call your insurer and ask: What is my out-of-network deductible? What is the coinsurance rate? What is the out-of-network out-of-pocket maximum? How do you calculate the allowed amount (Medicare percentage, UCR, FAIR Health)?</li>
</ul>

<h3>Financial planning for elective out-of-network care</h3>

<p>Before committing to out-of-network care, do the math:</p>

<ol>
    <li><strong>Get the provider&rsquo;s estimated total charges.</strong></li>
    <li><strong>Call your insurer</strong> and ask what the allowed amount would be for those CPT codes at out-of-network rates.</li>
    <li><strong>Calculate your cost-sharing:</strong> Apply your out-of-network deductible (if not yet met) and coinsurance to the allowed amount.</li>
    <li><strong>Add the balance bill:</strong> The provider&rsquo;s total charge minus the insurer&rsquo;s allowed amount is the balance you&rsquo;ll owe.</li>
    <li><strong>Compare to the cash-pay rate.</strong> If the cash-pay rate is lower than your total out-of-network cost (cost-sharing + balance bill), pay cash.</li>
</ol>

<div class="key-takeaway">
    <strong>Before going out-of-network electively,</strong> always ask about a single case agreement and a gap exception first. These can convert an out-of-network visit into an in-network claim and save you thousands. If neither option works, get a written estimate and calculate your total exposure before scheduling.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What does out-of-network mean on a medical bill?</h3>
        <p>It means the provider does not have a contract with your insurance company. Without a contract, the provider charges their full rate and your insurer reimburses only a fraction. You&rsquo;re responsible for the gap between the insurer&rsquo;s payment and the provider&rsquo;s charge &mdash; known as a <a href="/guides/balance-billing">balance bill</a>. In-network providers, by contrast, accept a negotiated rate and cannot bill you beyond your contracted cost-sharing.</p>
    </div>

    <div class="faq-item">
        <h3>Am I protected from surprise out-of-network bills?</h3>
        <p>Under the <a href="/guides/no-surprises-act-explained">No Surprises Act</a> (effective 2022), you are protected from surprise out-of-network bills for emergency services, care from out-of-network providers at in-network facilities you didn&rsquo;t choose, and air ambulance transport. You are NOT protected for ground ambulance, elective out-of-network care, or post-stabilization care where you gave valid written consent.</p>
    </div>

    <div class="faq-item">
        <h3>How much more does out-of-network care cost compared to in-network?</h3>
        <p>Typically 2&ndash;5 times more, sometimes higher. An in-network MRI might cost $400 after insurance, while the same MRI out-of-network could cost $2,000&ndash;$3,500. The gap exists because (1) the provider charges their full rate instead of a negotiated rate, and (2) your insurer covers a smaller percentage. <a href="/scan">Upload your bill</a> to see how your charges compare to fair-market benchmarks.</p>
    </div>

    <div class="faq-item">
        <h3>Can I negotiate an out-of-network medical bill?</h3>
        <p>Yes &mdash; out-of-network bills are often the most negotiable because the chargemaster rate is a starting price, not a contract. Request a cash-pay discount (often 30&ndash;60% off), use the Medicare rate or FAIR Health data as a benchmark, and get an itemized bill to identify errors. Many providers will accept significantly less than their initial charge rather than pursue collections.</p>
    </div>

    <div class="faq-item">
        <h3>What is an in-network exception and how do I get one?</h3>
        <p>An in-network exception is when your insurer agrees to cover an out-of-network provider at in-network rates. Insurers grant these when there&rsquo;s no in-network specialist nearby, for continuity of care when a provider leaves the network, or when a specific sub-specialty is needed. Submit a written request with a letter of medical necessity from your doctor and documentation that no in-network alternative is available.</p>
    </div>

    <div class="faq-item">
        <h3>How does my insurance calculate out-of-network reimbursement?</h3>
        <p>Insurers use one of three main methods: a percentage of the Medicare rate (typically 125&ndash;200%), the &ldquo;usual, customary, and reasonable&rdquo; (UCR) rate, or a FAIR Health benchmark (a percentile of actual charges in your area). The method matters enormously &mdash; reimbursement for the same procedure can vary by thousands of dollars depending on the method. Check your plan documents or call your insurer to find out which method your plan uses.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Overview and Consumer Protections</a></li>
    <li><a href="https://www.fairhealth.org" target="_blank" rel="noopener">FAIR Health &mdash; Independent Nonprofit Health Cost Data</a></li>
    <li><a href="https://www.ncsl.org/health/balance-billing-protections-state-laws" target="_blank" rel="noopener">National Conference of State Legislatures: State Balance Billing Laws</a></li>
    <li><a href="https://www.kff.org/private-insurance/issue-brief/no-surprises-act-implementation/" target="_blank" rel="noopener">Kaiser Family Foundation: No Surprises Act Implementation &mdash; What to Know</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/surprise-medical-bills/" target="_blank" rel="noopener">Kaiser Family Foundation: Surprise Medical Bills &mdash; Data and Analysis</a></li>
    <li><a href="https://www.cms.gov/files/document/federal-independent-dispute-resolution-idr-process-guidance-disputes.pdf" target="_blank" rel="noopener">CMS: Federal Independent Dispute Resolution (IDR) Process Guidance</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2019.01451" target="_blank" rel="noopener">Health Affairs: Prevalence and Magnitude of Surprise Out-of-Network Bills</a></li>
</ul>
""",
})
