"""Copy for the home, about, contact and insights pages.

Company facts are taken from public Strides/Synergice announcements and are
listed for verification in CONTENT_REVIEW.md.
"""

COMPANY_FACTS = [
    ("Platform", "Synergice, the B2B partnering platform of Strides Pharma Science Limited"),
    ("Parent company", "Strides Pharma Science Limited, listed on the NSE and BSE in India"),
    ("Founded", "1990 (Strides)"),
    ("Headquarters", "Bengaluru, India"),
    ("European B2B hub", "Strides Pharma International AG, Zug, Switzerland"),
    ("Partner portfolio", "More than 250 formulations"),
    ("Portfolio categories", "Generics, sterile injectables and value-added products, women's health hormones, lyophilised orally dissolving tablets and biopharmaceutical CDMO services"),
    ("Reach", "Products supplied to more than 100 countries"),
    ("Regulatory approvals across the network", "Including US FDA, UK MHRA, Australian TGA, EU GMP and WHO"),
]

HOME = {
    "eyebrow": "B2B partnering platform of Strides Pharma Science",
    "h1": "Molecule information and partnering enquiries in one place",
    "lead": "Browse the Strides portfolio by therapy area. Each molecule page explains when the molecule was approved, how it works and the facts a sourcing or regulatory team checks first, with a direct line to our partnering team.",
    "about": "Synergice is the B2B partnering platform of Strides Pharma Science Limited, a pharmaceutical company founded in 1990 and headquartered in Bengaluru, India. Strides manufactures finished dosage forms in sites approved by regulators including the US FDA, the UK MHRA, Australia's TGA and the WHO, and supplies more than 100 countries. Synergice brings its partner-ready portfolio of more than 250 formulations into one place, so partners can find a molecule and reach the people who hold its evidence.",
    "steps": [
        ("Find the molecule", "Search by name or browse a therapy area. Every molecule page gives an answer-first summary, a key facts table, the approval history and the mechanism of action."),
        ("Send an enquiry", "Tell us who you are, how you heard about us and what you want to know. One short form, on the molecule page or the contact page."),
        ("Talk to the partnering team", "Your enquiry goes to the Synergice partnering team at Strides, the manufacturer, not to a distributor or broker."),
    ],
    "audiences": [
        ("Licensing partners", "Companies looking to in-license a dossier or a finished product for their own markets."),
        ("Marketing authorisation holders", "Companies that hold an authorisation and need a qualified manufacturing source or second source."),
        ("Distributors and importers", "Partners entering a therapy area who want a manufacturer with regulatory support."),
        ("Institutional and tender buyers", "Procurement agencies and programmes that need documentation for public tenders."),
    ],
    "faqs": [
        ("What is Synergice?", "Synergice is the B2B partnering platform of Strides Pharma Science Limited. It brings Strides' partner-ready portfolio together in one place so that licensing partners, marketing authorisation holders and distributors can find molecules and contact the partnering team directly."),
        ("Who can send an enquiry?", "Pharmaceutical companies, distributors, licensing partners and institutional buyers. The site is intended for business partners and is not directed at patients or the general public."),
        ("What information is on each molecule page?", "An answer-first summary, a key facts table (class, ATC code, reference product, first approval, route and dosage form), the approval history, the mechanism of action, approved uses, pharmacokinetics at a glance and frequently asked questions."),
        ("Can I ask about a molecule that is not listed?", "Yes. Use the contact form and name the molecule, dosage form and market. The partnering team will tell you whether it is available within the Strides portfolio or through in-licensing."),
        ("Does Synergice give medical advice?", "No. Molecule pages summarise public prescribing information for business partners. Patients should speak to a healthcare professional."),
    ],
}

ABOUT = {
    "h1": "About Synergice",
    "summary": "Synergice is the B2B partnering platform of Strides Pharma Science Limited, a global pharmaceutical company founded in 1990 and headquartered in Bengaluru, India. It brings a partner-ready portfolio of more than 250 formulations into one place for licensing partners, marketing authorisation holders, distributors and institutional buyers in more than 100 countries.",
    "sections": [
        ("Who we are", [
            "Strides Pharma Science develops and manufactures finished dosage forms for regulated and emerging markets. Its manufacturing network holds approvals from authorities including the US FDA, the UK MHRA, Australia's TGA and the WHO, and its products reach patients in more than 100 countries.",
            "In November 2024 Strides consolidated its business-to-business activities under Synergice, with its European hub at Strides Pharma International AG in Zug, Switzerland. Synergice is the single front door to the products Strides makes available to partners.",
        ]),
        ("What Synergice does", [
            "Synergice connects partners with the Strides portfolio. A partner can find a molecule, read the essential facts about it and send an enquiry to the people who can answer it. Behind that enquiry sit the regulatory, quality and manufacturing teams that hold the evidence for each product.",
            "The portfolio covers generics, sterile injectables and value-added products, women's health hormones, lyophilised orally dissolving tablets and biopharmaceutical contract development and manufacturing. Partnerships range from dossier licensing to contract supply and supply with registration support, chosen around the partner's market and authorisation position.",
        ]),
        ("How we approach partnering", [
            "We keep the first step simple. Partners should not have to read through specification sheets and supply terms to find out whether a molecule is relevant. Each molecule page answers the first questions in plain language, and the enquiry form asks only for what the partnering team needs to reply.",
            "Detailed documentation, such as dossier status, registration position, stability and bioequivalence data and site inspection history, is shared directly with partners during evaluation, in the format their regulator requires.",
            "Enquiries are handled by the Strides partnering team, so there is no intermediary between a partner and the manufacturing organisation.",
        ]),
        ("Why this site is built the way it is", [
            "Buyers increasingly start their search in AI assistants and answer engines as well as in search engines. Every page on this site opens with a direct answer, uses consistent headings and fact tables, and carries structured data, so that people and machines can find accurate information about our molecules quickly.",
        ]),
    ],
    "timeline": [
        ("1990", "Strides is incorporated in India."),
        ("2022", "Strides reports US approvals including colchicine, amantadine softgels, naproxen sodium OTC softgels and potassium chloride oral solution, and an immunosuppressant portfolio."),
        ("2024", "Strides consolidates its European B2B business under Synergice, based in Zug, Switzerland."),
    ],
    "faqs": [
        ("Is Synergice part of Strides Pharma Science?", "Yes. Synergice is the B2B partnering platform of Strides Pharma Science Limited, and enquiries are handled by the Strides partnering team."),
        ("Where is Synergice based?", "Strides is headquartered in Bengaluru, India. Its European B2B hub is Strides Pharma International AG in Zug, Switzerland."),
        ("Does Synergice sell to patients or pharmacies?", "No. Synergice works with pharmaceutical businesses, such as licensing partners, marketing authorisation holders, distributors and institutional buyers."),
        ("Which regulators have approved Strides sites?", "Strides' manufacturing network holds approvals from authorities including the US FDA, UK MHRA, Australia's TGA, EU GMP inspectorates and the WHO. Which approvals apply to a given product depends on the site that makes it."),
    ],
}

CONTACT = {
    "h1": "Contact the partnering team",
    "summary": "Send an enquiry about any molecule in the Strides portfolio, or about one you do not see listed. Tell us your name, email, how you heard about us and what you want to know. Your enquiry goes directly to the Synergice partnering team at Strides Pharma Science.",
    "include": [
        "The molecule, dosage form and strengths you are interested in",
        "The markets you want to supply or register in",
        "Whether you already hold a marketing authorisation",
        "What you need first: product information, dossier status, samples or commercial terms",
    ],
    "next": [
        ("We read your enquiry", "The partnering team reviews your enquiry and routes it to the right regional and regulatory colleagues."),
        ("We reply with the essentials", "You hear back about the molecule's position for your market and what information can be shared at this stage."),
        ("We share detail under confidentiality", "Dossier, stability, bioequivalence and site information follow under a confidentiality agreement when there is a fit."),
    ],
    "offices": [
        ("Strides Pharma Science Limited", "Bengaluru, India (headquarters)"),
        ("Strides Pharma International AG", "Zug, Switzerland (European B2B hub)"),
    ],
    "faqs": [
        ("What should I include in my enquiry?", "Name the molecule, dosage form and market, and say whether you hold an authorisation. The more specific the question, the faster the partnering team can give a useful answer."),
        ("Can I enquire about more than one molecule?", "Yes. List them in the message field, or choose the main molecule from the list and mention the others in your message."),
        ("Who will reply to my enquiry?", "A member of the Synergice partnering team at Strides Pharma Science. There is no third-party distributor or broker in between."),
        ("Do you share pricing on the website?", "No. Commercial terms depend on the market, volume and partnership model, and are discussed directly with the partnering team."),
    ],
}

HEAR_ABOUT = [
    "Search engine (Google, Bing)",
    "AI assistant (ChatGPT, Perplexity, Gemini, Copilot)",
    "LinkedIn",
    "Trade show or conference",
    "Industry directory or database",
    "Colleague or referral",
    "Existing relationship with Strides",
    "Other",
]

ARTICLES = [
    {
        "slug": "ctd-ectd-actd-dossier-formats",
        "title": "CTD, eCTD and ACTD: a short guide to dossier formats",
        "description": "What the Common Technical Document, its electronic version and the ASEAN variant contain, and what they mean for a partner licensing a generic product.",
        "date": "2026-10-21",
        "summary": "The Common Technical Document (CTD) is the internationally agreed structure for a medicine's marketing authorisation dossier, organised in five modules. The eCTD is its electronic form and is mandatory for most submissions in the US and EU. The ASEAN Common Technical Dossier (ACTD) is a regional variant organised in four parts. A generic product's dossier usually needs to be adapted to the format of each destination market.",
        "sections": [
            ("Why dossier format matters", [
                "When a partner licenses a generic product, the dossier is the asset that changes hands. It contains the evidence that the product is made consistently, meets its specification and is equivalent to the reference medicine. If the dossier is not in the format the destination regulator expects, it has to be restructured before filing, which takes time and money.",
                "Knowing which format a dossier is in, and which format the destination market requires, is therefore one of the first questions in any licensing discussion.",
            ]),
            ("The Common Technical Document", [
                "The CTD was agreed through the International Council for Harmonisation (ICH) under guideline M4 in November 2000. It became the mandatory format in the European Union and Japan in July 2003 and is the format the US FDA expects. Many other regulators, and the WHO Prequalification programme, use it as well.",
                "The CTD is organised in five modules. Module 1 holds regional administrative information, such as application forms and product labelling, and is not harmonised. Module 2 contains summaries and overviews, including the quality overall summary. Module 3 holds the quality data: manufacture, specifications, analytical methods and stability. Module 4 contains non-clinical study reports and Module 5 the clinical study reports.",
                "For a generic medicine, Module 4 is usually replaced by references to published literature, and Module 5 centres on the bioequivalence study against the reference product.",
            ]),
            ("The electronic CTD (eCTD)", [
                "The eCTD is the CTD delivered as a structured electronic submission, defined by ICH guideline M2. Each document sits in a defined place in a folder structure, with an XML backbone that lets the regulator track every change across the product's life cycle.",
                "The US FDA has required eCTD for new drug, abbreviated new drug and biologics licence applications since May 2017. In the EU, eCTD became mandatory in stages and now applies across procedures. A dossier held only as paper or as unstructured PDFs needs to be converted before it can be filed in these markets.",
            ]),
            ("The ASEAN Common Technical Dossier (ACTD)", [
                "Member states of the Association of Southeast Asian Nations use the ACTD, a regional format organised in four parts: Part I for administrative data and product information, Part II for quality, Part III for non-clinical and Part IV for clinical data.",
                "The ACTD's quality content is broadly aligned with the CTD, but its structure, administrative requirements and some data expectations differ. Stability data, for example, must cover the hot and humid climatic conditions of the region.",
            ]),
            ("What to ask a licensing partner", [
                "Ask in which format the dossier exists today, whether it has been filed or approved anywhere, and against which reference product the bioequivalence study was run. Ask whether stability data covers the climatic zone of your market. And ask how quickly the dossier can be adapted to your regulator's Module 1 or Part I requirements.",
            ]),
        ],
        "faqs": [
            ("What are the five modules of the CTD?", "Module 1 is regional administrative information, Module 2 summaries, Module 3 quality, Module 4 non-clinical study reports and Module 5 clinical study reports."),
            ("Is eCTD mandatory?", "The US FDA has required eCTD for NDAs, ANDAs and BLAs since May 2017, and eCTD is mandatory across procedures in the EU. Other regulators are at different stages."),
            ("What is the difference between CTD and ACTD?", "The ACTD is the ASEAN regional format with four parts instead of five modules. Quality content is broadly aligned, but structure and some requirements differ."),
        ],
    },
    {
        "slug": "questions-before-sourcing-a-finished-dosage-form",
        "title": "Five questions to ask before sourcing a finished dosage form",
        "description": "The questions regulatory and sourcing teams ask a manufacturer before commercial terms are discussed, and why each one matters.",
        "date": "2026-10-21",
        "summary": "Before discussing price, a partner sourcing a finished dosage form should confirm five things: which regulator inspected the manufacturing site, what dossier exists and in which format, whether bioequivalence was shown against the reference product of their own market, whether stability data covers their climatic zone, and how supply and changes will be managed after launch.",
        "sections": [
            ("Why the questions come before price", [
                "In mature generic categories, the molecule is the same everywhere. What differs is the evidence behind a specific product and the reliability of the manufacturer that makes it. A low price is of no value if the dossier cannot be filed, or if a stock-out follows two years spent securing an authorisation.",
            ]),
            ("1. Which regulator inspected the manufacturing site, and when?", [
                "A product supplied to a regulated market must come from a site that the market's authority, or one it recognises, has inspected and found compliant. Ask for the site name, the authorities that have approved it and the date and outcome of the most recent inspection. Ask whether you can audit the site before committing.",
            ]),
            ("2. What dossier exists, and in which format?", [
                "Ask whether the dossier is in CTD, eCTD or ACTD format, whether it is ready to file, already filed or approved somewhere, and how quickly it can be adapted to your regulator's administrative requirements. A dossier already approved by a stringent authority shortens review in many markets.",
            ]),
            ("3. Was bioequivalence shown against my market's reference product?", [
                "Each regulator names its own reference product. A bioequivalence study against the US reference listed drug may not be accepted in the EU or in other markets without additional justification or a new study. Ask which reference product was used and where the study was conducted.",
            ]),
            ("4. Does the stability data cover my climatic zone?", [
                "ICH divides the world into climatic zones, from temperate Zone I to hot and very humid Zone IVb. Stability studies must cover the conditions of the destination market, and a product's shelf life and storage statement depend on them. Ask for the zones covered and the shelf life supported.",
            ]),
            ("5. How will supply and changes be managed?", [
                "Ask how forecasts, minimum order quantities and lead times are agreed, how launch stock is planned, and how you will be notified of any manufacturing change that requires a variation to your authorisation. Good change control protects both the partner's licence and patients' continuity of treatment.",
            ]),
            ("Putting the answers to work", [
                "Collect the answers in writing before commercial negotiation begins, and share them with your regulatory, quality and supply chain colleagues at the same time. Gaps found early, such as a missing climatic zone or a bioequivalence study against the wrong reference product, can often be closed while the commercial terms are agreed. Gaps found after signature usually cost a filing cycle.",
            ]),
        ],
        "faqs": [
            ("What is a finished dosage form?", "A finished dosage form is the final medicine as given to patients, such as a tablet, capsule or oral solution, as opposed to the bulk active pharmaceutical ingredient (API)."),
            ("Why does the reference product matter for bioequivalence?", "Regulators require equivalence to the reference product authorised in their own market. A study against a different market's reference may need extra justification or a new study."),
            ("What are ICH climatic zones?", "ICH climatic zones group countries by temperature and humidity, from Zone I (temperate) to Zone IVb (hot and very humid). Stability studies must match the zone of the destination market."),
        ],
    },
]


# ---------------------------------------------------------------------------
# Product page framework v2.0: text that is IDENTICAL on every product page.
# INFO_QUALITY and INFO_SUPPLY are owned by marketing/QA; DISCLAIMER by legal.

INFO_QUALITY = (
    "Products are manufactured under Good Manufacturing Practice, with in-process controls at each stage of "
    "production and finished-product release testing of every batch against its approved specification. "
    "Stability is established under ICH conditions for the climatic zones of the markets supplied. "
    "Site-specific regulatory status, including the inspecting authorities and the most recent inspection "
    "outcome, is confirmed on enquiry."
)

INFO_SUPPLY = (
    "Synergice works with partners through contract supply, dossier-based partnerships and volume agreements, "
    "structured around each partner's market and authorisation position. Forecasts, lead times and order "
    "quantities are agreed per market. For questions about a specific market, registration or commercial "
    "terms, use the enquiry form on this page."
)

FAQ_FIXED = [
    ("Can Synergice supply this product to my market?",
     "Registration status varies by market. Tell us your country in the enquiry form on this page and our "
     "business development team will confirm whether the product is registered there or can be supplied "
     "through another route."),
    ("How do I request a quotation?",
     "Use the enquiry form on this page. Enter your details, your country and the strengths or pack sizes you "
     "need. We reply within one business day."),
]

DISCLAIMER = (
    "This page is intended for pharmaceutical industry professionals and business partners only and is not "
    "directed at patients or the general public. Product information is provided for business discussion, may "
    "differ from the approved labelling in your country and is not medical advice. Dosage forms, strengths and "
    "availability vary by market, and not every product is registered or available in every territory. Brand "
    "names mentioned are trademarks of their respective owners."
)

RESPONSE_PROMISE = "We reply within one business day."

COUNTRIES = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
    "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
    "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
    "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad",
    "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Côte d'Ivoire", "Croatia", "Cuba", "Cyprus",
    "Czechia", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji",
    "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland", "India",
    "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
    "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
    "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
    "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia",
    "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand",
    "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau",
    "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
    "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
    "Samoa", "San Marino", "São Tomé and Príncipe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
    "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
    "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria",
    "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
    "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen",
    "Zambia", "Zimbabwe",
]
