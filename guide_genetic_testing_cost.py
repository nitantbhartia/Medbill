"""Guide: Genetic Testing Cost & Insurance Coverage."""

from guides import register, _embed

register("genetic-testing-cost", {
    "title": "Genetic Testing Cost & Insurance Coverage in 2026",
    "meta_description": "Genetic testing costs range from $100 for carrier screening to $5,000+ for whole exome sequencing. Learn what insurance covers, when BRCA testing is free under ACA rules, and how billing errors affect 31% of genetic testing claims.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "Is genetic testing covered by insurance?",
            "a": "It depends on the type and indication. BRCA1/2 testing for high-risk individuals is covered with no cost-sharing under the ACA preventive mandate. Carrier screening during pregnancy is covered as preventive care. Diagnostic genetic testing for a specific suspected condition is usually covered when medically indicated. Ancestry or wellness genetic tests (23andMe, AncestryDNA) are never covered.",
        },
        {
            "q": "How much does BRCA testing cost?",
            "a": "Through certified labs (Myriad, Invitae, Ambry, GeneDx), BRCA1/2 sequencing costs $250&ndash;$500 with insurance or direct-to-patient pricing. Hospital-based genetic testing can run $1,000&ndash;$5,000 without insurance. For qualifying high-risk individuals, BRCA testing is required to be covered at no cost by ACA-compliant commercial plans under the USPSTF preventive mandate.",
        },
        {
            "q": "What is GINA and does it protect my genetic information?",
            "a": "GINA (the Genetic Information Nondiscrimination Act) prohibits health insurers and employers from using genetic information to make coverage, eligibility, or premium decisions. However, GINA does not apply to life insurance, disability insurance, or long-term care insurance. If you are concerned about genetic discrimination in those areas, discuss it with your genetic counselor before testing.",
        },
        {
            "q": "Does insurance cover prenatal genetic testing like NIPT?",
            "a": "Non-invasive prenatal testing (NIPT) is covered as preventive care for all pregnant people under ACA-compliant plans, typically with no cost-sharing. Amniocentesis and CVS are also covered when medically indicated (advanced maternal age, abnormal NIPT result, family history). Coverage rules vary by plan for optional expanded NIPT panels testing for additional conditions.",
        },
        {
            "q": "What is pharmacogenomic testing and is it covered?",
            "a": "Pharmacogenomic testing analyzes how your genes affect your response to medications. Coverage is inconsistent: some plans cover it when there is a specific clinical indication (e.g., testing before prescribing a medication with known genetic variability like warfarin, certain antidepressants, or chemotherapy agents). General wellness pharmacogenomic panels without a specific medication indication are usually not covered.",
        },
    ],
    "body": f"""
<p class="lead">Genetic testing has become dramatically more accessible&mdash;and more confusing from a billing standpoint. Costs range from <strong>under $100 for targeted carrier screening</strong> to <strong>$5,000 or more for whole exome sequencing</strong>. Insurance coverage depends heavily on the type of test, the clinical indication, and which lab you use. BillKarma data shows that <strong>genetic testing billing errors affect 31% of claims</strong>, mostly from incorrect CPT code selection for the specific gene tested. Here is what you need to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#types-costs">Types of genetic testing and costs</a></li>
        <li><a href="#insurance-coverage">What insurance covers and when</a></li>
        <li><a href="#brca-aca">BRCA testing and the ACA preventive mandate</a></li>
        <li><a href="#prenatal">Prenatal genetic testing coverage</a></li>
        <li><a href="#gina">GINA: genetic information protections</a></li>
        <li><a href="#labs-pricing">Lab companies and patient assistance programs</a></li>
        <li><a href="#billing-codes">CPT codes for genetic testing</a></li>
        <li><a href="#billing-errors">Billing errors: wrong codes and unbundling</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="types-costs">1. Types of genetic testing and costs</h2>

<p>Genetic testing is not a single service&mdash;it encompasses a spectrum of tests with very different clinical purposes, methodologies, and price points:</p>

<table>
    <thead>
        <tr><th>Test Type</th><th>What It Does</th><th>Cost Without Insurance</th><th>Covered by Insurance?</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Carrier screening</strong></td><td>Determines if you carry a gene for an inherited condition (cystic fibrosis, spinal muscular atrophy, etc.)</td><td>$100&ndash;$400</td><td>Usually covered as preventive during pregnancy</td></tr>
        <tr><td><strong>Diagnostic genetic testing</strong></td><td>Identifies whether a specific condition (hereditary cancer, genetic disorder) is present</td><td>$250&ndash;$2,000+</td><td>Usually covered when medically indicated</td></tr>
        <tr><td><strong>BRCA1/2 hereditary cancer panel</strong></td><td>Tests for BRCA1 and BRCA2 variants associated with breast/ovarian cancer risk</td><td>$250&ndash;$500 (labs); $1,000&ndash;$5,000 (hospital)</td><td>Free under ACA for high-risk individuals</td></tr>
        <tr><td><strong>Prenatal NIPT</strong></td><td>Screens for chromosomal conditions (Down syndrome, trisomy 18/13) from maternal blood</td><td>$800&ndash;$2,500</td><td>Covered as preventive; no cost-sharing for most</td></tr>
        <tr><td><strong>Amniocentesis / CVS</strong></td><td>Diagnostic chromosomal testing of fetal cells</td><td>$1,500&ndash;$3,500</td><td>Covered when medically indicated</td></tr>
        <tr><td><strong>Pharmacogenomic testing</strong></td><td>How your genes affect drug metabolism and response</td><td>$200&ndash;$500</td><td>Inconsistent; covered for specific medication indications</td></tr>
        <tr><td><strong>Whole exome sequencing (WES)</strong></td><td>Sequences all protein-coding regions of the genome; used for rare/undiagnosed diseases</td><td>$1,000&ndash;$5,000+</td><td>Sometimes covered for pediatric undiagnosed disease</td></tr>
        <tr><td><strong>Consumer / ancestry tests</strong></td><td>Ethnicity, ancestry, wellness traits (23andMe, AncestryDNA)</td><td>$99&ndash;$299</td><td>Never covered</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The single most important rule:</strong> The same genetic test can cost very different amounts depending on which lab performs it. Invitae, Ambry, and GeneDx have aggressive direct-to-patient pricing that can be far lower than hospital-based genetic testing. Always ask your ordering provider which lab they use and whether a lower-cost lab option is available.
</div>

{_embed(mode="cost", cpt="81211", title="Look up genetic testing costs", subtitle="See what Medicare pays for BRCA and other genetic panels.")}

<h2 id="insurance-coverage">2. What insurance covers and when</h2>

<p>Insurance coverage for genetic testing follows clinical guidelines more strictly than almost any other category of testing. Coverage decisions are driven by established professional society guidelines (USPSTF, ACOG, NCCN) and whether the test will change clinical management.</p>

<p><strong>Generally covered:</strong></p>
<ul>
    <li>BRCA1/2 testing for individuals meeting USPSTF high-risk criteria (family history of breast/ovarian cancer, Ashkenazi Jewish ancestry with family history)</li>
    <li>Carrier screening for common recessive conditions during pregnancy (cystic fibrosis, SMA, hemoglobinopathies, fragile X)</li>
    <li>Hereditary cancer panels (Lynch syndrome, hereditary breast/ovarian cancer) when personal or family history meets criteria</li>
    <li>Diagnostic genetic testing when a specific genetic condition is suspected based on clinical presentation</li>
    <li>Prenatal NIPT as preventive care for all pregnancies under ACA-compliant plans</li>
    <li>Diagnostic confirmatory testing after abnormal NIPT</li>
</ul>

<p><strong>Usually requires prior authorization:</strong></p>
<ul>
    <li>Multi-gene hereditary cancer panels beyond BRCA1/2</li>
    <li>Whole exome or whole genome sequencing</li>
    <li>Pharmacogenomic panels</li>
    <li>Testing for rare or newly discovered genetic variants</li>
</ul>

<p><strong>Generally not covered:</strong></p>
<ul>
    <li>Consumer ancestry or wellness testing (23andMe, AncestryDNA, Color for general wellness)</li>
    <li>Preimplantation genetic testing (PGT) in most states and plans</li>
    <li>Expanded carrier screening beyond established medical guidelines</li>
    <li>Repeat testing without clinical indication for change in results</li>
</ul>

<h2 id="brca-aca">3. BRCA testing and the ACA preventive mandate</h2>

<p>The Affordable Care Act requires ACA-compliant health plans to cover USPSTF Grade B preventive services with <strong>no cost-sharing</strong>. BRCA-related risk assessment, genetic counseling, and BRCA testing for high-risk women is a Grade B USPSTF recommendation, meaning it must be covered at no cost to the patient on all ACA-compliant commercial plans.</p>

<p><strong>Who qualifies as high-risk:</strong></p>
<ul>
    <li>Personal or family history of breast cancer, ovarian cancer, tubal cancer, or peritoneal cancer</li>
    <li>Ashkenazi Jewish ancestry with one or more first-degree relatives with breast or ovarian cancer</li>
    <li>Known BRCA1 or BRCA2 variant in the family</li>
    <li>Any individual whose risk assessment score (via a validated tool) suggests elevated hereditary risk</li>
</ul>

<p><strong>How to access no-cost BRCA testing:</strong></p>
<ol>
    <li>See your primary care provider or OB-GYN and discuss your family history.</li>
    <li>Ask for a referral to a genetic counselor for formal risk assessment.</li>
    <li>The genetic counselor submits the BRCA testing order with documentation that you meet USPSTF criteria.</li>
    <li>The test must be billed as preventive under the ACA mandate for no-cost coverage. If it is billed as diagnostic, cost-sharing applies.</li>
</ol>

<p><strong>Important note:</strong> If you have already had breast or ovarian cancer, BRCA testing is diagnostic (not preventive) and therefore not subject to the no-cost-sharing requirement. Coverage and cost-sharing will depend on your plan&rsquo;s standard benefits for diagnostic genetic testing.</p>

<h2 id="prenatal">4. Prenatal genetic testing coverage</h2>

<p>Prenatal genetic testing coverage has expanded significantly. Most prenatal testing is now covered as preventive care:</p>

<table>
    <thead>
        <tr><th>Test</th><th>Timing</th><th>What It Screens For</th><th>Coverage</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>NIPT (non-invasive prenatal testing)</strong></td><td>10+ weeks</td><td>Trisomy 21, 18, 13; sex chromosome conditions; optional microdeletions</td><td>Covered as preventive (no cost-sharing) for all pregnancies under ACA plans</td></tr>
        <tr><td><strong>First trimester combined screening</strong></td><td>11&ndash;13 weeks</td><td>Down syndrome, trisomy 18 (blood + ultrasound)</td><td>Covered as preventive</td></tr>
        <tr><td><strong>Cell-free DNA (cfDNA) expanded panel</strong></td><td>10+ weeks</td><td>Additional chromosomal conditions beyond standard NIPT</td><td>Coverage varies; expanded panels may have cost-sharing</td></tr>
        <tr><td><strong>Carrier screening</strong></td><td>Before or early in pregnancy</td><td>Recessive genetic conditions the baby could inherit</td><td>Covered as preventive</td></tr>
        <tr><td><strong>Amniocentesis</strong></td><td>15&ndash;20 weeks</td><td>Diagnostic chromosomal testing of fetal cells</td><td>Covered when medically indicated (abnormal screening, AMA, family history)</td></tr>
        <tr><td><strong>CVS (chorionic villus sampling)</strong></td><td>10&ndash;13 weeks</td><td>Earlier diagnostic chromosomal testing</td><td>Covered when medically indicated</td></tr>
    </tbody>
</table>

<p><strong>Watch for expanded NIPT cost issues:</strong> Standard NIPT is covered as preventive with no cost-sharing. However, some labs offer expanded panels that test for many additional conditions beyond what USPSTF guidelines recommend. Insurers may treat these expanded panels as diagnostic rather than preventive, resulting in cost-sharing. Ask your provider which version of NIPT is being ordered before the draw.</p>

<h2 id="gina">5. GINA: genetic information protections</h2>

<p>The Genetic Information Nondiscrimination Act (GINA) provides federal protections against genetic discrimination in two areas:</p>

<p><strong>Health insurance (Title II of GINA):</strong> Health insurers cannot use genetic information to make eligibility, coverage, underwriting, or premium-setting decisions. A positive BRCA test cannot cause your insurer to raise your premium or deny coverage. Health insurers cannot require you to take genetic tests as a condition of coverage.</p>

<p><strong>Employment (Title I of GINA):</strong> Employers cannot use genetic information in hiring, firing, pay, job assignments, or other employment decisions.</p>

<p><strong>What GINA does NOT cover:</strong></p>
<ul>
    <li>Life insurance: life insurers can ask about and use genetic test results</li>
    <li>Disability insurance: same as life insurance</li>
    <li>Long-term care insurance: same as life insurance</li>
    <li>Military service</li>
    <li>Employers with fewer than 15 employees</li>
</ul>

<p>If you are considering genetic testing and have concerns about impact on life or disability insurance, discuss timing with a genetic counselor. Some people choose to obtain those policies before testing.</p>

<h2 id="labs-pricing">6. Lab companies and patient assistance programs</h2>

<p>The genetic testing lab market is dominated by a few large companies, and pricing varies significantly between them:</p>

<table>
    <thead>
        <tr><th>Lab</th><th>Known For</th><th>With Insurance</th><th>Without Insurance</th><th>Patient Assistance</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Invitae</strong></td><td>Broad panels, aggressive pricing</td><td>$0&ndash;$250 (most panels)</td><td>$100&ndash;$250 (many panels)</td><td>Yes; financial assistance program for low-income patients</td></tr>
        <tr><td><strong>Myriad Genetics</strong></td><td>BRCA testing pioneer; BRACAnalysis</td><td>Variable; often covered</td><td>$250&ndash;$500+</td><td>MyRisk patient assistance; Myriad ACCESS program</td></tr>
        <tr><td><strong>Ambry Genetics</strong></td><td>Hereditary cancer and cardiology panels</td><td>Variable</td><td>$250&ndash;$1,000</td><td>AmbryShare program</td></tr>
        <tr><td><strong>GeneDx</strong></td><td>Rare disease, pediatric genetics, WES</td><td>Variable; prior auth usually needed</td><td>$500&ndash;$5,000+</td><td>GeneDx Cares program</td></tr>
        <tr><td><strong>Hospital lab</strong></td><td>All types; billed through hospital system</td><td>Standard insurance rates</td><td>$1,000&ndash;$10,000+</td><td>Hospital financial assistance programs</td></tr>
    </tbody>
</table>

<p><strong>Invitae&rsquo;s pricing model</strong> is worth understanding: they charge a flat fee of $100&ndash;$250 for most panels when paid directly, and $0&ndash;$250 with insurance depending on plan. For patients without insurance or with high deductibles, going directly to Invitae and paying out of pocket can be less expensive than having it billed through a hospital lab to insurance. Ask your ordering provider which lab they are sending the sample to and whether a lower-cost option exists.</p>

<h2 id="billing-codes">7. CPT codes for genetic testing</h2>

<p>Genetic testing CPT codes are highly specific&mdash;different codes exist for different genes, sequencing methods, and variant types. This specificity is the source of the most common billing error:</p>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Description</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>81211</strong></td><td>BRCA1/2; full sequence analysis and deletion/duplication analysis</td><td>Most comprehensive BRCA test; standard for hereditary cancer evaluation</td></tr>
        <tr><td><strong>81213</strong></td><td>BRCA1/2; uncommon duplication/deletion variants</td><td>Add-on to 81211 for additional variant detection</td></tr>
        <tr><td><strong>81215</strong></td><td>BRCA2; full sequence analysis</td><td>When only BRCA2 is analyzed</td></tr>
        <tr><td><strong>81162</strong></td><td>BRCA1/2 comprehensive analysis (next-generation sequencing)</td><td>NGS-based full analysis; may be used instead of 81211 at some labs</td></tr>
        <tr><td><strong>81401&ndash;81479</strong></td><td>Molecular pathology procedures; various gene analyses</td><td>Hundreds of specific codes; must match exact gene tested</td></tr>
        <tr><td><strong>81099</strong></td><td>Unlisted molecular pathology procedure</td><td>Used when no specific code exists; requires documentation; frequently denied</td></tr>
        <tr><td><strong>81415</strong></td><td>Exome sequence analysis; trio (patient and both parents)</td><td>For rare/undiagnosed disease workup</td></tr>
        <tr><td><strong>81416</strong></td><td>Exome sequence analysis; proband only</td><td>Single patient WES without parental comparison</td></tr>
    </tbody>
</table>

<h2 id="billing-errors">8. Billing errors: wrong codes and unbundling</h2>

<p>BillKarma data shows that <strong>genetic testing billing errors affect 31% of claims</strong>. The errors are different from other medical billing categories because they almost always involve coding specificity rather than simple duplicate or upcoding issues.</p>

<p><strong>Incorrect CPT code for the specific gene tested (most common):</strong> The CPT code system for molecular pathology (81401&ndash;81479) has specific codes for hundreds of individual genes. Billing CPT 81479 (unlisted molecular pathology) when a specific code exists for the gene is both incorrect and almost guaranteed to trigger a denial. Conversely, billing a more expensive panel code when a targeted single-gene test was actually performed is an upcoding error. Both errors are common when billing staff are not familiar with the molecular pathology code set.</p>

<p><strong>Unbundling individual gene codes when a panel code should be used:</strong> Some labs bill each gene in a multi-gene panel as a separate 81401&ndash;81479 code instead of using the appropriate panel code (81432 for hereditary breast/ovarian cancer panel, for example). This unbundling can inflate costs and violates correct coding guidelines.</p>

<p><strong>Billing preventive BRCA testing as diagnostic:</strong> If BRCA testing qualifies for the ACA no-cost-sharing preventive mandate but is billed under a diagnostic code, you will be charged cost-sharing that should not apply. The diagnosis code and billing context must identify the service as preventive (Z-code diagnosis) to trigger the no-cost-sharing benefit.</p>

<div class="case-study">
    <h3>Case study: Preventive BRCA test billed as diagnostic</h3>
    <p><strong>Situation:</strong> Diane, 42, had a strong family history of BRCA-related breast cancer and qualified for free BRCA testing under the ACA preventive mandate. Her genetic counselor ordered the test and it was performed through a hospital-affiliated genetics center. Diane received a bill for $847.</p>
    <p><strong>The problem:</strong> The hospital lab billed the BRCA test under a diagnostic code (Z15.01, genetic susceptibility to malignant neoplasm) rather than as a preventive service (Z13.88, encounter for screening for disorder). This triggered Diane&rsquo;s $1,500 deductible, of which $847 had not yet been met.</p>
    <p><strong>What she did:</strong> Diane <a href="/fight-debt">filed a dispute through BillKarma</a>. We identified that her testing met the USPSTF criteria for no-cost-sharing preventive coverage and that the diagnostic billing code was incorrect for her clinical situation. We requested the lab resubmit under the correct preventive code with a letter documenting her USPSTF qualifying criteria.</p>
    <p><strong>Result:</strong> The claim was reprocessed as preventive. Diane&rsquo;s bill was reduced to $0. <strong>Savings: $847.</strong></p>
</div>

<p>If you have received a genetic testing bill that seems inconsistent with your insurance coverage, <a href="/fight-debt">let BillKarma review it</a>. Genetic testing billing errors require specific expertise to identify and correct.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Is genetic testing covered by insurance?</h3>
        <p>It depends on the type and indication. BRCA testing is free for high-risk individuals under the ACA. Carrier screening during pregnancy is covered as preventive. Diagnostic testing for a specific suspected condition is usually covered. Consumer ancestry tests are never covered.</p>
    </div>

    <div class="faq-item">
        <h3>How much does BRCA testing cost?</h3>
        <p>Through certified labs, $250&ndash;$500 self-pay. Hospital-based testing can reach $1,000&ndash;$5,000 without insurance. For qualifying high-risk individuals, BRCA testing is free under ACA-compliant commercial plans when billed as preventive care.</p>
    </div>

    <div class="faq-item">
        <h3>What is GINA and does it protect my genetic information?</h3>
        <p>GINA prohibits health insurers and employers from using genetic information to discriminate. It does not apply to life insurance, disability insurance, or long-term care insurance. If those policies concern you, discuss timing of testing with a genetic counselor before proceeding.</p>
    </div>

    <div class="faq-item">
        <h3>Does insurance cover prenatal genetic testing like NIPT?</h3>
        <p>Yes. NIPT is covered as preventive care with no cost-sharing for all pregnancies under ACA-compliant plans. Amniocentesis and CVS are covered when medically indicated. Expanded NIPT panels beyond standard screening may have cost-sharing depending on your plan.</p>
    </div>

    <div class="faq-item">
        <h3>What is pharmacogenomic testing and is it covered?</h3>
        <p>Pharmacogenomic testing analyzes how your genes affect drug response. Coverage is inconsistent: some plans cover it for specific medication indications (before prescribing warfarin, certain antidepressants, or chemotherapy). General wellness pharmacogenomic panels are usually not covered.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">U.S. Preventive Services Task Force: BRCA-Related Cancer Risk Assessment (2019)</a></li>
    <li><a href="#" target="_blank" rel="noopener">HealthCare.gov: Preventive Care Coverage Requirements (ACA)</a></li>
    <li><a href="#" target="_blank" rel="noopener">National Human Genome Research Institute: Genetic Information Nondiscrimination Act (GINA)</a></li>
    <li><a href="#" target="_blank" rel="noopener">ACOG: Carrier Screening in the Age of Genomic Medicine</a></li>
    <li><a href="#" target="_blank" rel="noopener">American College of Medical Genetics: Molecular Pathology CPT Coding Guide (2026)</a></li>
</ul>
""",
})
