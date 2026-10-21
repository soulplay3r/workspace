"""Product page framework v2.0 fields, one entry per molecule slug.

Hand-written fields (word limits enforced by build.py):
  overview_molecule  60-90 words; what it is, class, mechanism in plain terms,
                     what it treats; no brand names
  moa_short          30-60 words; from the reference monograph
  indication         30-60 words; factual, no efficacy or comparative claims
Optional product fields (row hides when absent, as the framework specifies):
  strengths, cas_number, availability, pack_config, regulatory_filings (list),
  image (path to an 800x800 WebP), image_alt
Strengths are filled only where Strides has reported them or the agency draft
listed them; everything else is confirmed on enquiry (CONTENT_REVIEW.md).
"""

FIELDS = {
    "atorvastatin": {
        "strengths": "10 mg, 20 mg, 40 mg, 80 mg",
        "overview_molecule": "Atorvastatin is a synthetic lipid-lowering medicine from the statin class (HMG-CoA reductase inhibitors). It reduces the amount of cholesterol the liver makes, which leads the liver to clear more LDL cholesterol from the blood. It is used to treat high cholesterol and mixed dyslipidaemia and to lower the risk of heart attack, stroke and revascularisation in adults with, or at high risk of, cardiovascular disease. It was first approved by the US FDA in December 1996.",
        "moa_short": "Atorvastatin competitively inhibits HMG-CoA reductase, the rate-limiting enzyme of hepatic cholesterol synthesis. Lower intracellular cholesterol increases LDL receptor expression on liver cells, which increases clearance of LDL cholesterol from plasma. Active metabolites extend inhibitory activity to 20 to 30 hours.",
        "indication": "Atorvastatin is indicated, as an adjunct to diet, to reduce LDL cholesterol in primary hyperlipidaemia and mixed dyslipidaemia, including heterozygous familial hypercholesterolaemia in children aged 10 years and older, and to reduce the risk of myocardial infarction, stroke and revascularisation in adults at increased cardiovascular risk.",
    },
    "rosuvastatin": {
        "strengths": "5 mg, 10 mg, 20 mg, 40 mg",
        "overview_molecule": "Rosuvastatin is a lipid-lowering medicine from the statin class (HMG-CoA reductase inhibitors). It is hydrophilic, concentrates in the liver and is only minimally metabolised by cytochrome P450 enzymes, which gives it fewer metabolic drug interactions than some other statins. It lowers LDL cholesterol and triglycerides, slows atherosclerosis and is used for primary prevention of cardiovascular events in adults at increased risk. It was first approved by the US FDA in August 2003.",
        "moa_short": "Rosuvastatin competitively inhibits HMG-CoA reductase in hepatocytes, reducing conversion of HMG-CoA to mevalonate. The liver responds by expressing more LDL receptors, increasing uptake and clearance of LDL cholesterol. Uptake into liver cells depends on the OATP1B1 transporter.",
        "indication": "Rosuvastatin is indicated as an adjunct to diet for primary hyperlipidaemia, mixed dyslipidaemia and hypertriglyceridaemia, for homozygous and heterozygous familial hypercholesterolaemia, to slow progression of atherosclerosis, and for primary prevention of cardiovascular disease in adults at increased risk.",
    },
    "clopidogrel": {
        "strengths": "75 mg",
        "overview_molecule": "Clopidogrel is an oral antiplatelet medicine from the thienopyridine class (P2Y12 inhibitors). It is a prodrug that the liver converts into an active metabolite, which permanently blocks a receptor platelets need to clump together. It is used to prevent heart attack and stroke after acute coronary syndrome, recent myocardial infarction or ischaemic stroke, and in peripheral arterial disease, often together with aspirin. It was first approved by the US FDA in November 1997.",
        "moa_short": "Clopidogrel's active thiol metabolite, formed mainly via CYP2C19, binds irreversibly to the platelet P2Y12 ADP receptor. This prevents ADP-mediated activation of the glycoprotein IIb/IIIa complex and platelet aggregation for the remaining life of the platelet, about 7 to 10 days.",
        "indication": "Clopidogrel is indicated to reduce the rate of myocardial infarction and stroke in patients with acute coronary syndrome, together with aspirin, and in patients with recent myocardial infarction, recent ischaemic stroke or established peripheral arterial disease.",
    },
    "amlodipine": {
        "strengths": "5 mg, 10 mg",
        "overview_molecule": "Amlodipine is a long-acting calcium channel blocker of the dihydropyridine class. It relaxes the smooth muscle in artery walls, widening blood vessels and lowering blood pressure, and it reduces the heart's oxygen demand in angina. Its long half-life allows smooth control with one dose a day. It is used for hypertension, chronic stable angina and vasospastic angina, often in combination with other medicines. It was first approved by the US FDA in July 1992.",
        "moa_short": "Amlodipine inhibits calcium influx through L-type voltage-gated calcium channels, acting more on vascular smooth muscle than on cardiac muscle. Peripheral arterial vasodilation lowers vascular resistance and blood pressure; in angina it reduces afterload and myocardial oxygen demand and relieves coronary spasm.",
        "indication": "Amlodipine is indicated for the treatment of hypertension, alone or with other antihypertensive agents, for chronic stable angina and vasospastic (Prinzmetal's) angina, and to reduce the risk of hospitalisation for angina in patients with angiographically documented coronary artery disease.",
    },
    "metoprolol": {
        "strengths": "25 mg, 50 mg, 100 mg",
        "overview_molecule": "Metoprolol is a beta-1 selective adrenergic blocker, a beta blocker that acts mainly on the heart. It slows the heart rate and reduces the force of contraction, lowering blood pressure and the heart's workload. It is used for hypertension and angina, after myocardial infarction and, as an extended-release form, in heart failure with reduced ejection fraction. Metoprolol tartrate was first approved by the US FDA in 1978.",
        "moa_short": "Metoprolol competitively blocks beta-1 adrenergic receptors in the heart, reducing heart rate, contractility and cardiac output, particularly during exercise or stress. It also reduces renin release. It has no intrinsic sympathomimetic activity, and its beta-1 selectivity diminishes at higher doses.",
        "indication": "Metoprolol is indicated for hypertension and angina pectoris. Immediate-release metoprolol tartrate is indicated in acute myocardial infarction, and extended-release metoprolol succinate is indicated for stable, symptomatic heart failure with reduced ejection fraction.",
    },
    "letrozole": {
        "overview_molecule": "Letrozole is an oral non-steroidal aromatase inhibitor used in breast cancer. After menopause most estrogen is made in peripheral tissues by the aromatase enzyme; letrozole blocks this enzyme and lowers estrogen levels sharply, removing the growth signal for hormone receptor-positive tumours. It is used in postmenopausal women as adjuvant, extended adjuvant and advanced-disease therapy. It was first approved by the US FDA in July 1997.",
        "moa_short": "Letrozole binds reversibly to the haem group of aromatase (CYP19A1) and blocks conversion of androgens to estrogens. In postmenopausal women it suppresses plasma estradiol by more than 75 percent without meaningful effects on adrenal corticosteroid or aldosterone synthesis.",
        "indication": "Letrozole is indicated in postmenopausal women for adjuvant treatment of hormone receptor-positive early breast cancer, extended adjuvant treatment after tamoxifen, first-line treatment of hormone receptor-positive or unknown advanced breast cancer, and advanced breast cancer after antiestrogen therapy.",
    },
    "anastrozole": {
        "overview_molecule": "Anastrozole is an oral non-steroidal aromatase inhibitor used to treat hormone receptor-positive breast cancer in postmenopausal women. By blocking the aromatase enzyme in fat, muscle and breast tissue, it lowers circulating estrogen by around 80 percent and deprives estrogen-dependent tumour cells of their growth signal. It is taken once daily as adjuvant therapy for early breast cancer and in advanced disease. It was first approved by the US FDA in December 1995.",
        "moa_short": "Anastrozole is a triazole that competitively and reversibly binds the haem iron of aromatase (CYP19A1), blocking aromatisation of androstenedione and testosterone to estrone and estradiol. At 1 mg daily it reduces estradiol by about 80 percent and does not meaningfully affect cortisol or aldosterone synthesis.",
        "indication": "Anastrozole is indicated in postmenopausal women for adjuvant treatment of hormone receptor-positive early breast cancer, first-line treatment of hormone receptor-positive or unknown advanced breast cancer, and advanced breast cancer that has progressed after tamoxifen therapy.",
    },
    "capecitabine": {
        "overview_molecule": "Capecitabine is an oral chemotherapy medicine from the fluoropyrimidine class of antimetabolites. It is a prodrug that is absorbed intact and converted in three enzymatic steps to 5-fluorouracil, the last step concentrated in tumour tissue. It gives patients an oral alternative to infused 5-fluorouracil and is used in colorectal and breast cancer, alone or with other agents. It was first approved by the US FDA in April 1998.",
        "moa_short": "Capecitabine is converted to 5-fluorouracil by carboxylesterase, cytidine deaminase and thymidine phosphorylase. 5-fluorouracil metabolites inhibit thymidylate synthase, blocking DNA synthesis, and are incorporated into RNA. Dihydropyrimidine dehydrogenase (DPD) deficiency increases the risk of severe toxicity.",
        "indication": "Capecitabine is indicated for adjuvant treatment of stage III colon cancer, for metastatic colorectal cancer, and for metastatic breast cancer alone or in combination with docetaxel. Some markets approve additional gastrointestinal cancer indications; local labelling applies.",
    },
    "imatinib": {
        "overview_molecule": "Imatinib is an oral targeted cancer medicine and the first tyrosine kinase inhibitor to reach the market. It blocks the BCR-ABL fusion protein that drives chronic myeloid leukaemia, and also the KIT and PDGFR receptors, which explains its activity in gastrointestinal stromal tumours and several rarer cancers. It turned chronic myeloid leukaemia into a long-term manageable disease for most patients. It was first approved by the US FDA in May 2001.",
        "moa_short": "Imatinib binds the ATP-binding pocket of the ABL kinase domain and holds it in the inactive conformation, blocking BCR-ABL autophosphorylation and downstream signalling in Philadelphia chromosome-positive cells. It also inhibits the KIT and PDGFR receptor tyrosine kinases.",
        "indication": "Imatinib is indicated for Philadelphia chromosome-positive chronic myeloid leukaemia and acute lymphoblastic leukaemia, KIT-positive gastrointestinal stromal tumours in adjuvant and metastatic settings, and dermatofibrosarcoma protuberans, hypereosinophilic syndrome, systemic mastocytosis and PDGFR-rearranged myelodysplastic or myeloproliferative diseases.",
    },
    "mycophenolate-mofetil": {
        "overview_molecule": "Mycophenolate mofetil is an oral immunosuppressant used to prevent organ rejection after transplantation. It is a prodrug of mycophenolic acid, which blocks an enzyme lymphocytes depend on to make the guanine nucleotides they need to multiply, so it suppresses the immune response to a transplanted organ. It is used with a calcineurin inhibitor and corticosteroids after kidney, heart and liver transplantation. It was first approved by the US FDA in May 1995.",
        "moa_short": "Mycophenolate mofetil is hydrolysed to mycophenolic acid, a selective, reversible, uncompetitive inhibitor of inosine monophosphate dehydrogenase. This depletes guanosine nucleotides in T and B lymphocytes, which rely on de novo purine synthesis, producing a cytostatic effect and reduced antibody formation.",
        "indication": "Mycophenolate mofetil is indicated for the prophylaxis of organ rejection in recipients of allogeneic kidney, heart or liver transplants, in combination with other immunosuppressants such as a calcineurin inhibitor and corticosteroids.",
    },
    "tacrolimus": {
        "overview_molecule": "Tacrolimus is a macrolide immunosuppressant from the calcineurin inhibitor class, discovered in 1984 from the soil bacterium Streptomyces tsukubaensis. It stops T lymphocytes from activating in response to a transplanted organ and is the most widely used immunosuppressant after solid organ transplantation. It has a narrow therapeutic index, so doses are guided by whole-blood trough levels. It was first approved by the US FDA in April 1994.",
        "moa_short": "Tacrolimus binds the intracellular protein FKBP12. The complex inhibits calcineurin, preventing dephosphorylation and nuclear translocation of NFAT and so blocking transcription of interleukin-2 and other cytokines needed for T-cell activation and proliferation.",
        "indication": "Tacrolimus is indicated for the prophylaxis of organ rejection in adult and paediatric recipients of kidney, liver, heart or lung transplants, in combination with other immunosuppressants such as mycophenolate and corticosteroids.",
    },
    "cyclosporine": {
        "overview_molecule": "Cyclosporine, also known as ciclosporin, is a cyclic peptide immunosuppressant from the calcineurin inhibitor class, derived from the fungus Tolypocladium inflatum. It suppresses T-cell activation without broadly suppressing the bone marrow, and its introduction made routine organ transplantation possible. It is used to prevent rejection after kidney, liver and heart transplantation and, in microemulsion form, for severe psoriasis and rheumatoid arthritis. It was first approved by the US FDA in November 1983.",
        "moa_short": "Cyclosporine binds cyclophilin inside T lymphocytes. The complex inhibits calcineurin, preventing activation of the transcription factor NFAT and blocking transcription of interleukin-2 and other early cytokines, so helper and cytotoxic T cells do not expand.",
        "indication": "Cyclosporine is indicated for prophylaxis of organ rejection in kidney, liver and heart transplantation. The microemulsion form is also indicated for severe active rheumatoid arthritis not responding to methotrexate and for severe recalcitrant plaque psoriasis.",
    },
    "naproxen-sodium": {
        "strengths": "220 mg (OTC)",
        "overview_molecule": "Naproxen sodium is a non-steroidal anti-inflammatory drug (NSAID) of the propionic acid class. It relieves pain, reduces fever and dampens inflammation by blocking the production of prostaglandins. The sodium salt is absorbed faster than naproxen itself, and its long half-life allows dosing every 8 to 12 hours. It is used over the counter for minor aches, pains and fever and on prescription for arthritis. Naproxen was first approved by the US FDA in 1976.",
        "moa_short": "Naproxen reversibly inhibits cyclooxygenase-1 and cyclooxygenase-2, reducing synthesis of prostaglandins that sensitise pain receptors, mediate inflammation and raise the hypothalamic temperature set point. COX-1 inhibition in the gut and platelets accounts for its gastrointestinal and bleeding risks.",
        "indication": "Over the counter, naproxen sodium 220 mg is indicated for temporary relief of minor aches and pains and to reduce fever. Prescription naproxen is indicated for rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, tendonitis, bursitis, acute gout and primary dysmenorrhoea.",
    },
    "ibuprofen": {
        "overview_molecule": "Ibuprofen is a short-acting non-steroidal anti-inflammatory drug (NSAID) of the propionic acid class. It relieves pain, reduces fever and dampens inflammation by blocking prostaglandin production, and at over-the-counter doses it has a comparatively favourable gastrointestinal profile among NSAIDs. It is one of the most widely used medicines in the world and is listed on the WHO Model List of Essential Medicines. It was first approved by the US FDA in 1974.",
        "moa_short": "Ibuprofen reversibly inhibits cyclooxygenase-1 and cyclooxygenase-2, lowering prostaglandin synthesis. It is supplied as a racemic mixture; the S-enantiomer provides most of the activity, and the body converts much of the R-enantiomer into the S-form.",
        "indication": "Over the counter, ibuprofen is indicated for temporary relief of minor aches and pains, headache, toothache, menstrual cramps and fever. On prescription it is indicated for rheumatoid arthritis, osteoarthritis, mild to moderate pain and primary dysmenorrhoea.",
    },
    "colchicine": {
        "strengths": "0.6 mg",
        "overview_molecule": "Colchicine is an alkaloid originally obtained from the autumn crocus and used against gout for centuries. It is not a painkiller and does not lower uric acid; instead it dampens the inflammatory response of white blood cells to urate crystals. It is used to treat and prevent gout flares and is the standard treatment for familial Mediterranean fever. It has a narrow therapeutic index. A single-ingredient oral tablet was first approved by the US FDA in July 2009.",
        "moa_short": "Colchicine binds tubulin and inhibits microtubule polymerisation, impairing neutrophil migration, adhesion and degranulation. It also interferes with NLRP3 inflammasome activation, reducing release of interleukin-1 beta, a key driver of gout flares.",
        "indication": "Colchicine is indicated for prophylaxis and treatment of gout flares in adults and for familial Mediterranean fever in adults and children aged 4 years and older. Dose adjustment or avoidance is required with strong CYP3A4 or P-glycoprotein inhibitors.",
    },
    "amantadine": {
        "strengths": "100 mg",
        "overview_molecule": "Amantadine is an adamantane derivative with antiparkinsonian and antiviral activity. First approved by the US FDA in 1966 to prevent influenza A, it was found by chance in 1969 to improve Parkinson's disease, which is now its main use. It helps tremor, rigidity and slowness of movement and reduces levodopa-induced dyskinesia. It is excreted mostly unchanged by the kidneys, so doses are reduced in renal impairment.",
        "moa_short": "In Parkinson's disease amantadine acts as a weak non-competitive NMDA receptor antagonist and increases dopamine release while reducing its reuptake, with mild anticholinergic effects. Against influenza A it blocks the viral M2 proton channel, though most current strains are resistant.",
        "indication": "Amantadine is indicated for Parkinson's disease and parkinsonism and for drug-induced extrapyramidal reactions. It is also labelled for influenza A prophylaxis and treatment, but public health agencies no longer recommend it for influenza because of widespread resistance.",
    },
    "methylphenidate": {
        "overview_molecule": "Methylphenidate is a central nervous system stimulant and the most widely used medicine for attention-deficit/hyperactivity disorder. It increases the availability of dopamine and noradrenaline in brain regions that control attention and impulse control, and it is also used for narcolepsy. Because of its potential for misuse it is a controlled substance in most countries, which affects manufacture and cross-border supply. It was first approved by the US FDA in 1955.",
        "moa_short": "Methylphenidate blocks the dopamine transporter and the noradrenaline transporter on presynaptic neurons, increasing extracellular dopamine and noradrenaline in the prefrontal cortex and striatum. Its activity comes mainly from the d-threo enantiomer and from reuptake inhibition rather than monoamine release.",
        "indication": "Methylphenidate is indicated for attention-deficit/hyperactivity disorder in children aged 6 years and older, adolescents and adults as part of a total treatment programme. Immediate-release forms are also indicated for narcolepsy.",
    },
    "tenofovir-lamivudine-efavirenz": {
        "overview_molecule": "Tenofovir disoproxil fumarate, lamivudine and efavirenz (TLE) is a fixed-dose antiretroviral combination for HIV-1, taken as one tablet once daily. It combines two nucleoside/nucleotide reverse transcriptase inhibitors with a non-nucleoside reverse transcriptase inhibitor. It was the WHO-preferred first-line regimen from 2013 until 2019 and remains an alternative regimen. Its components were first approved by the US FDA between 1995 and 2001.",
        "moa_short": "Tenofovir and lamivudine are phosphorylated inside cells and incorporated into viral DNA by HIV reverse transcriptase, terminating the chain. Efavirenz binds an allosteric pocket of HIV-1 reverse transcriptase and blocks it non-competitively. Lamivudine and tenofovir are also active against hepatitis B.",
        "indication": "Tenofovir disoproxil fumarate, lamivudine and efavirenz is indicated as a complete regimen for the treatment of HIV-1 infection in adults and adolescents weighing at least 40 kg. Efavirenz is not active against HIV-2.",
    },
    "tenofovir-lamivudine-dolutegravir": {
        "overview_molecule": "Tenofovir disoproxil fumarate, lamivudine and dolutegravir (TLD) is a fixed-dose antiretroviral combination for HIV-1, taken as one tablet once daily. It combines two nucleoside/nucleotide reverse transcriptase inhibitors with the integrase inhibitor dolutegravir, which suppresses the virus quickly and has a high barrier to resistance. The WHO has recommended TLD as the preferred first-line regimen for adults and adolescents since 2019. Dolutegravir was first approved by the US FDA in August 2013.",
        "moa_short": "Dolutegravir binds the active site of HIV integrase and blocks the strand-transfer step that inserts viral DNA into the host genome. Tenofovir and lamivudine are phosphorylated inside cells and terminate the viral DNA chain made by reverse transcriptase.",
        "indication": "Tenofovir disoproxil fumarate, lamivudine and dolutegravir is used as a complete regimen for the treatment of HIV-1 infection in adults and adolescents weighing at least 30 kg, and is the WHO-preferred first-line and second-line regimen.",
    },
    "artemether-lumefantrine": {
        "overview_molecule": "Artemether-lumefantrine is an artemisinin-based combination therapy for malaria. It pairs artemether, a fast-acting derivative of artemisinin that rapidly reduces the number of parasites, with lumefantrine, a long-acting partner drug that clears the parasites that remain. Combining two drugs protects each against resistance. It is the most widely used treatment for uncomplicated falciparum malaria worldwide. It was first registered in 1999 and approved by the US FDA in April 2009.",
        "moa_short": "Artemether and its metabolite dihydroartemisinin are activated by haem iron inside the parasite, generating free radicals that damage parasite proteins. Lumefantrine is thought to block detoxification of haem into haemozoin, so toxic haem accumulates in the parasite.",
        "indication": "Artemether-lumefantrine is indicated for the treatment of acute, uncomplicated malaria caused by Plasmodium falciparum, including mixed infections, in adults and children weighing at least 5 kg. It is not indicated for prevention of malaria or for severe malaria.",
    },
    "nitrofurantoin": {
        "overview_molecule": "Nitrofurantoin is an oral antibacterial of the nitrofuran class used for bladder infections. It is cleared so quickly into urine that it reaches high concentrations in the bladder but very low levels in blood and tissues, which limits its effect on gut bacteria. Resistance among Escherichia coli remains low after seven decades of use, and guidelines recommend it first-line for uncomplicated cystitis. It was first approved by the US FDA in 1953.",
        "moa_short": "Nitrofurantoin is reduced by bacterial flavoproteins to reactive intermediates that attack ribosomal proteins, DNA, RNA and enzymes of energy metabolism and cell wall synthesis. Acting on many targets at once makes resistance from single mutations uncommon.",
        "indication": "Nitrofurantoin is indicated for the treatment of urinary tract infections caused by susceptible strains of Escherichia coli, enterococci, Staphylococcus aureus and certain Klebsiella and Enterobacter species. It is not indicated for pyelonephritis or perinephric abscesses.",
    },
    "dutasteride": {
        "overview_molecule": "Dutasteride is an oral 5-alpha reductase inhibitor used for benign prostatic hyperplasia. It blocks both forms of the enzyme that converts testosterone into dihydrotestosterone, the hormone that drives prostate growth, lowering dihydrotestosterone by about 90 percent. Over months this shrinks the prostate, improves urinary symptoms and reduces the risk of urinary retention and surgery. It is supplied as a soft gelatin capsule. It was first approved by the US FDA in November 2001.",
        "moa_short": "Dutasteride competitively inhibits both type 1 and type 2 5-alpha reductase, blocking conversion of testosterone to dihydrotestosterone. Serum dihydrotestosterone falls by about 85 to 90 percent within two weeks, and prostate volume decreases over the following months.",
        "indication": "Dutasteride is indicated for the treatment of symptomatic benign prostatic hyperplasia in men with an enlarged prostate, alone or with the alpha blocker tamsulosin, to improve symptoms and reduce the risk of acute urinary retention and BPH-related surgery.",
    },
    "prednisone": {
        "strengths": "2.5 mg, 5 mg",
        "overview_molecule": "Prednisone is a synthetic glucocorticoid, or corticosteroid, taken by mouth. It is a prodrug that the liver converts to prednisolone, which suppresses inflammation and immune activity across many tissues. One molecule covers a very wide range of conditions, from asthma and arthritis to autoimmune disease, transplant rejection and some blood cancers, at doses from a few milligrams to high-dose courses. It was first approved by the US FDA in 1955.",
        "moa_short": "Prednisolone binds the cytoplasmic glucocorticoid receptor, which moves to the nucleus and switches on anti-inflammatory genes while repressing pro-inflammatory transcription factors such as NF-kappa-B and AP-1. Cytokine, prostaglandin and leukotriene production falls and immune cell migration is reduced.",
        "indication": "Prednisone is indicated for a wide range of endocrine, rheumatic, collagen, dermatological, allergic, ophthalmic, respiratory, haematological, neoplastic, oedematous and gastrointestinal conditions that respond to glucocorticoids, including asthma, rheumatoid arthritis, lupus and nephrotic syndrome.",
    },
    "potassium-chloride": {
        "overview_molecule": "Potassium chloride is an electrolyte replenisher used to treat and prevent low blood potassium, a common effect of diuretics and gastrointestinal losses. Low potassium causes muscle weakness and can trigger dangerous heart rhythm disturbances. Oral extended-release forms release potassium slowly to avoid irritation of the gut, and liquid and powder forms suit patients who cannot swallow tablets. The chloride salt also corrects the chloride loss that often accompanies hypokalaemia.",
        "moa_short": "Potassium is the main intracellular cation and sets the resting membrane potential of nerve and muscle cells. Potassium chloride restores body potassium stores, and the chloride component allows the kidney to correct hypochloraemic metabolic alkalosis, which otherwise sustains renal potassium loss.",
        "indication": "Potassium chloride is indicated for the treatment and prevention of hypokalaemia, with or without metabolic alkalosis, including in digitalis intoxication and hypokalaemic familial periodic paralysis, and in patients at risk of potassium depletion such as those taking diuretics.",
    },
    "ergocalciferol": {
        "overview_molecule": "Ergocalciferol is vitamin D2, a fat-soluble prohormone made by ultraviolet irradiation of ergosterol from yeast and fungi. The liver and kidney convert it into the active hormone, which increases absorption of calcium and phosphate from the gut and supports normal bone mineralisation. High-strength soft capsules are used for hypoparathyroidism, refractory rickets and familial hypophosphataemia, and widely to correct vitamin D deficiency under clinical supervision.",
        "moa_short": "Ergocalciferol is hydroxylated in the liver to 25-hydroxyvitamin D2 and in the kidney to 1,25-dihydroxyvitamin D2. The active hormone binds the nuclear vitamin D receptor and increases intestinal calcium and phosphate absorption and renal calcium reabsorption.",
        "indication": "Ergocalciferol is indicated for hypoparathyroidism, refractory rickets (vitamin D-resistant rickets) and familial hypophosphataemia. High-strength capsules are also used to treat vitamin D deficiency under clinical supervision, according to local labelling and practice.",
    },
    "progesterone": {
        "overview_molecule": "Progesterone is the natural hormone produced by the corpus luteum. Micronised progesterone suspended in oil in a soft capsule makes oral dosing practical despite the hormone's poor natural absorption. It protects the lining of the womb from overgrowth in postmenopausal women taking estrogen, and it is used to treat secondary amenorrhoea. Many clinicians prefer it to synthetic progestins in menopausal hormone therapy. Oral micronised progesterone was first approved by the US FDA in May 1998.",
        "moa_short": "Progesterone activates nuclear progesterone receptors PR-A and PR-B, converting estrogen-primed proliferative endometrium into secretory endometrium and opposing estrogen-driven endometrial hyperplasia. Some metabolites, such as allopregnanolone, act on GABA-A receptors and cause drowsiness.",
        "indication": "Oral micronised progesterone is indicated for prevention of endometrial hyperplasia in postmenopausal women with a uterus who are receiving estrogen, and for secondary amenorrhoea. Some markets approve additional uses such as luteal phase support; local labelling applies.",
    },
}
