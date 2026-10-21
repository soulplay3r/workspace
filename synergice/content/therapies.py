"""Therapy areas shown as clickable tiles on the home and products pages.

Each therapy page is generated from this list plus the molecules that point
at it (see molecules_*.py). `intro` paragraphs are written for the page itself
so that every therapy page has its own crawlable copy, not boilerplate.
"""

THERAPIES = [
    {
        "slug": "cardiovascular",
        "name": "Cardiovascular",
        "icon": "heart",
        "tagline": "Statins, antiplatelets, calcium channel blockers and beta blockers.",
        "intro": [
            "Cardiovascular disease is the leading cause of death worldwide, and the molecules used to manage it are among the most widely prescribed medicines in every market. Most are now off-patent and supplied as generics, so partners compare suppliers on evidence and reliability rather than on the molecule itself.",
            "The cardiovascular molecules listed here cover the main pillars of long-term risk management: lowering LDL cholesterol (atorvastatin, rosuvastatin), preventing platelet-driven thrombosis (clopidogrel), and controlling blood pressure, angina and heart rate (amlodipine, metoprolol). Each molecule page sets out when the molecule was first approved, how it works and the facts a regulatory or sourcing team checks first.",
        ],
        "faqs": [
            ("Which cardiovascular molecules can I enquire about?", "You can enquire about atorvastatin, rosuvastatin, clopidogrel, amlodipine and metoprolol. Each molecule has its own page with approval history, mechanism of action and key facts, and an enquiry form that goes directly to the Synergice partnering team."),
            ("Are these cardiovascular products finished dosage forms?", "Yes. Synergice partners on finished dosage forms, such as tablets and capsules, made within the Strides Pharma Science network. Ask the partnering team about dosage forms and strengths for your market."),
        ],
    },
    {
        "slug": "oncology",
        "name": "Oncology",
        "icon": "ribbon",
        "tagline": "Aromatase inhibitors, oral fluoropyrimidines and kinase inhibitors.",
        "intro": [
            "Oral oncology medicines have changed how many cancers are treated, moving long courses of therapy from infusion chairs to patients' homes. For partners, oral oncology products bring specific requirements: containment during manufacture, cytotoxic handling in the supply chain, and close attention to bioequivalence because the therapeutic margin is narrow.",
            "The oncology molecules listed here include two aromatase inhibitors used in hormone receptor-positive breast cancer (letrozole, anastrozole), an oral prodrug of 5-fluorouracil used in colorectal and breast cancer (capecitabine), and the first targeted tyrosine kinase inhibitor, imatinib, which turned chronic myeloid leukaemia into a manageable chronic condition.",
        ],
        "faqs": [
            ("Which oncology molecules does Synergice list?", "The oncology section lists letrozole, anastrozole, capecitabine and imatinib. Each page explains the molecule's approval history and mechanism of action, with an enquiry form for partners."),
            ("Can I discuss an oncology molecule that is not listed?", "Yes. Use the contact form and name the molecule, dosage form and market. The partnering team will tell you whether it is available within the Strides portfolio or through in-licensing."),
        ],
    },
    {
        "slug": "transplant-immunology",
        "name": "Transplant & Immunology",
        "icon": "shield",
        "tagline": "Calcineurin inhibitors and antimetabolite immunosuppressants.",
        "intro": [
            "Transplant patients take immunosuppressants for life, usually as a combination of a calcineurin inhibitor, an antiproliferative agent and a corticosteroid. These are narrow therapeutic index medicines: small changes in exposure can mean rejection on one side or toxicity on the other, so regulators and clinicians scrutinise generic versions closely.",
            "Strides has built an immunosuppressant portfolio around the three most widely used molecules: mycophenolate mofetil, tacrolimus and cyclosporine. The molecule pages below explain how each one blocks T-cell activation, how they are combined in practice, and the pharmacokinetic facts that matter for switching and therapeutic drug monitoring.",
        ],
        "faqs": [
            ("Which immunosuppressants are in the Strides portfolio?", "Strides has reported a US immunosuppressant portfolio that includes mycophenolate mofetil tablets and capsules, tacrolimus capsules and cyclosporine softgel capsules. Contact the partnering team for the position in your market."),
            ("Why do transplant immunosuppressants need extra care when switching supplier?", "Tacrolimus and cyclosporine have narrow therapeutic indices and variable absorption, so blood levels are monitored after any change of product. Partners usually ask for bioequivalence data and plan switch protocols with prescribers."),
        ],
    },
    {
        "slug": "pain-inflammation",
        "name": "Pain & Inflammation",
        "icon": "bolt",
        "tagline": "NSAIDs for pain and fever, and colchicine for gout.",
        "intro": [
            "Pain and inflammation products span prescription and over-the-counter markets. Non-steroidal anti-inflammatory drugs (NSAIDs) are among the most used medicines in the world, and the dosage form often decides commercial success: liquid-filled softgel capsules, for example, are valued by consumers for fast onset and easy swallowing.",
            "Strides is one of the larger softgel manufacturers supplying regulated markets. This section covers naproxen sodium and ibuprofen, both propionic acid NSAIDs, and colchicine, an alkaloid used for gout flares and familial Mediterranean fever that works through a completely different, anti-inflammatory mechanism.",
        ],
        "faqs": [
            ("Does Synergice offer OTC pain products?", "Yes. Strides received US FDA approval for naproxen sodium 220 mg OTC softgel capsules in 2022, and the portfolio includes other NSAIDs. Ask the partnering team about OTC and prescription presentations for your market."),
            ("Is colchicine an NSAID?", "No. Colchicine is a plant alkaloid that binds tubulin and dampens neutrophil-driven inflammation. It is used for gout flares and familial Mediterranean fever, and it has a narrow therapeutic index with important drug interactions."),
        ],
    },
    {
        "slug": "central-nervous-system",
        "name": "Central Nervous System",
        "icon": "neuron",
        "tagline": "Parkinson's disease, ADHD and narcolepsy.",
        "intro": [
            "Central nervous system (CNS) medicines are chronic-use products where patients and prescribers value consistency. Several, including methylphenidate, are controlled substances, so partners need manufacturing sites and logistics that can handle quota, import and export permits under the UN Convention on Psychotropic Substances.",
            "This section covers amantadine, an older molecule whose second life in Parkinson's disease was discovered by chance, and methylphenidate, the most widely used stimulant for attention-deficit/hyperactivity disorder (ADHD).",
        ],
        "faqs": [
            ("Which CNS molecules are listed?", "Amantadine and methylphenidate are listed. Strides received US FDA approval for amantadine hydrochloride softgel capsules in 2022 and also holds an approval for amantadine tablets."),
            ("Can Synergice supply controlled substances?", "Supply of controlled substances depends on the destination market's import rules and the manufacturing site's licences. Name the molecule and market in your enquiry and the partnering team will confirm what is possible."),
        ],
    },
    {
        "slug": "hiv-antiretrovirals",
        "name": "HIV / Antiretrovirals",
        "icon": "virus",
        "tagline": "Fixed-dose combinations for first-line HIV treatment.",
        "intro": [
            "Fixed-dose combinations changed HIV treatment in low- and middle-income countries. Putting three antiretrovirals in one daily tablet improves adherence, simplifies procurement and reduces cost, and most first-line treatment in these markets is now supplied by generic manufacturers, many of them in India.",
            "Strides has a long history in antiretrovirals supplied through donor-funded and public procurement programmes. This section covers the two backbone regimens that have defined first-line treatment: tenofovir, lamivudine and efavirenz (TLE), and its successor, tenofovir, lamivudine and dolutegravir (TLD), which the World Health Organization has recommended as the preferred first-line regimen since 2019.",
        ],
        "faqs": [
            ("What is the difference between TLE and TLD?", "Both combine tenofovir disoproxil fumarate and lamivudine. TLE adds efavirenz, a non-nucleoside reverse transcriptase inhibitor. TLD adds dolutegravir, an integrase inhibitor with a higher barrier to resistance and better tolerability, which is why WHO now prefers TLD."),
            ("Are these products available for tender supply?", "Antiretrovirals are often bought through national tenders and donor-funded programmes that require WHO prequalification or a stringent regulatory approval. Ask the partnering team for the product's current status."),
        ],
    },
    {
        "slug": "anti-malarials",
        "name": "Anti-malarials",
        "icon": "mosquito",
        "tagline": "Artemisinin-based combination therapy.",
        "intro": [
            "Malaria still causes hundreds of thousands of deaths every year, most of them among young children in sub-Saharan Africa. Artemisinin-based combination therapies (ACTs) are the WHO-recommended first-line treatment for uncomplicated Plasmodium falciparum malaria, and much of the global supply is procured through public tenders and donor programmes.",
            "Artemether-lumefantrine is the most widely used ACT. It pairs a fast-acting artemisinin derivative with a long-acting partner drug, so the parasite load drops quickly and the residual parasites are cleared over the following days.",
        ],
        "faqs": [
            ("Why are anti-malarials given as combinations?", "Combining two drugs with different mechanisms and half-lives clears parasites faster and makes it much harder for resistance to emerge to either drug. WHO recommends against artemisinin monotherapy for this reason."),
            ("Who buys anti-malarial finished products?", "Most anti-malarials are procured by national malaria programmes, the Global Fund and other donor-funded buyers, which usually require WHO prequalification or a stringent regulatory approval."),
        ],
    },
    {
        "slug": "anti-infectives",
        "name": "Anti-infectives",
        "icon": "capsule",
        "tagline": "Antibacterials for urinary tract infections.",
        "intro": [
            "Antimicrobial resistance has made older antibiotics with low resistance rates more valuable, not less. Molecules that act at a single site of infection and spare the gut flora are now preferred by stewardship guidelines because they treat the infection with less pressure on resistance.",
            "Nitrofurantoin is a good example. It has been in use since the 1950s, reaches therapeutic concentrations almost only in urine, and is recommended as a first-line treatment for uncomplicated cystitis in many guidelines.",
        ],
        "faqs": [
            ("Which anti-infective molecules are listed?", "Nitrofurantoin is listed. Strides' US portfolio covers antibiotics and antivirals more broadly, so name any other molecule in your enquiry and the partnering team will confirm availability."),
            ("Why is nitrofurantoin used only for bladder infections?", "Nitrofurantoin is cleared rapidly into urine and reaches very low concentrations in blood and tissues, so it works in the bladder but not for kidney or bloodstream infections."),
        ],
    },
    {
        "slug": "urology",
        "name": "Urology",
        "icon": "drop",
        "tagline": "5-alpha reductase inhibitors for benign prostatic hyperplasia.",
        "intro": [
            "Benign prostatic hyperplasia (BPH) affects a large share of men over 50 and is treated for years, often for life. Treatment combines alpha blockers, which relax smooth muscle for fast symptom relief, with 5-alpha reductase inhibitors, which shrink the prostate over months and reduce the risk of urinary retention and surgery.",
            "Dutasteride is supplied as a soft gelatin capsule, a dosage form in which Strides has specialist manufacturing capability. The molecule page explains why dutasteride inhibits both 5-alpha reductase isoenzymes and what its five-week half-life means for patients and handling.",
        ],
        "faqs": [
            ("Is dutasteride supplied as a softgel?", "Dutasteride is formulated as a 0.5 mg soft gelatin capsule in reference products. Ask the partnering team about presentations available for your market."),
            ("Can dutasteride be combined with tamsulosin?", "Yes. Dutasteride is used alone or with the alpha blocker tamsulosin, and fixed-dose combinations of the two exist in several markets."),
        ],
    },
    {
        "slug": "endocrine-corticosteroids",
        "name": "Endocrine & Corticosteroids",
        "icon": "hexagon",
        "tagline": "Oral glucocorticoids.",
        "intro": [
            "Oral corticosteroids are among the most versatile medicines in use. They treat inflammatory, autoimmune, allergic and some malignant diseases, and they replace hormones in adrenal insufficiency. Because doses range from a few milligrams to high-dose pulses, a full range of strengths matters to prescribers and pharmacies.",
            "Prednisone is the reference oral glucocorticoid in many markets. Strides received US FDA approval for prednisone tablets in 2.5 mg and 5 mg strengths.",
        ],
        "faqs": [
            ("Which corticosteroids can I enquire about?", "Prednisone is listed. Name any other corticosteroid or endocrine molecule in your enquiry and the partnering team will confirm what is available."),
            ("What is the difference between prednisone and prednisolone?", "Prednisone is a prodrug that the liver converts to prednisolone, the active steroid. They are used for the same conditions, and different markets prefer one or the other."),
        ],
    },
    {
        "slug": "vitamins-electrolytes",
        "name": "Vitamins & Electrolytes",
        "icon": "sun",
        "tagline": "Potassium supplementation and high-strength vitamin D.",
        "intro": [
            "Vitamin and electrolyte products correct deficiencies that are common in hospital and community practice: low potassium from diuretics or gastrointestinal losses, and low vitamin D from limited sun exposure, malabsorption or kidney disease. They look simple, but the dosage form matters. Extended-release potassium forms were developed to avoid gut injury, and high-strength vitamin D needs a stable oil-based formulation.",
            "Strides has a broad potassium chloride franchise in the US, covering extended-release capsules and tablets, powder for oral solution and oral solution, and it supplies vitamin D products as soft gelatin capsules.",
        ],
        "faqs": [
            ("Which potassium chloride dosage forms does Strides have?", "Strides has reported a potassium chloride franchise in the US that includes extended-release capsules, extended-release tablets, powder for oral solution and oral solution."),
            ("Is ergocalciferol the same as vitamin D3?", "No. Ergocalciferol is vitamin D2, made from plant and fungal sterols. Cholecalciferol is vitamin D3. Both are converted to active hormone in the liver and kidney."),
        ],
    },
    {
        "slug": "womens-health",
        "name": "Women's Health",
        "icon": "venus",
        "tagline": "Natural progesterone and hormone products.",
        "intro": [
            "Women's health hormones are a specialist area. Partners need manufacturing segregation for hormones, stable formulations of poorly soluble steroids, and a regulatory file that addresses the safety profile regulators expect for long-term use.",
            "Synergice lists women's health hormones as one of its core portfolio categories. Micronised progesterone in an oil-filled soft capsule is the example shown here: it is used to protect the endometrium during estrogen therapy and to treat secondary amenorrhoea.",
        ],
        "faqs": [
            ("Which women's health products can I ask about?", "Progesterone is listed. Synergice's women's health category covers further hormone products, so name the molecule and market in your enquiry."),
            ("Why is oral progesterone micronised?", "Natural progesterone is poorly absorbed. Reducing the particle size and suspending it in oil increases the amount absorbed and makes oral dosing practical."),
        ],
    },
]
