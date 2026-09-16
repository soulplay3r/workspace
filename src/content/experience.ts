// Career case studies for the Work section. Reverse chronological.
// Only SurveyMonkey, Zee (Mind Wars), Emeritus and upGrad get full case-study
// treatment, per the brief. Earlier roles (L&T, Cummins, Ingersoll Rand, IEEE,
// NTPC) are compact — see EARLY_CAREER below.

export interface CaseStudyMetric {
  label: string;
  value: string;
  source: "LinkedIn" | "Resume" | "Public reference";
  note?: string;
}

export interface CaseStudy {
  id: string;
  company: string;
  title: string;
  titleNote?: string;
  dates: string;
  location: string;
  dek: string;
  systemStages: string[];
  narrative: string[];
  tradeoff?: { heading: string; body: string };
  metrics: CaseStudyMetric[];
  sourcingNote?: string;
}

export const CASE_STUDIES: CaseStudy[] = [
  {
    id: "surveymonkey",
    company: "SurveyMonkey",
    title: "Senior Product Manager, AI & Marketplace",
    titleNote:
      'LinkedIn lists this role as "Senior AI Product Manager"; the resume lists it as "Senior Product Manager." Rendered neutrally here — see CONTENT_REVIEW.md.',
    dates: "Nov 2024 – Present",
    location: "Bengaluru",
    dek: "End-to-end ownership of a global two-sided marketplace connecting survey buyers to a 335M+ panelist supply pool — plus the AI systems that keep it trustworthy.",
    systemStages: [
      "Buyer acquisition",
      "Pricing & fulfillment",
      "Panelist supply",
      "Response quality",
      "Fraud detection (ML)",
      "Trust & repeat demand",
    ],
    narrative: [
      "SurveyMonkey's Audience Marketplace is a global two-sided platform, live on web and mobile app, matching 10k+ demand-side buyers against a supply pool of 335M+ panelists across 130+ countries. I own product strategy end to end, across both sides of the market.",
      "On the demand side, that means growth experimentation and funnel optimization across acquisition, pricing, and fulfillment — using A/B testing and behavioral data to find where buyers drop off and why.",
      "On the supply side, I own the mobile app experience for panelist acquisition, engagement, response quality, and fraud monitoring across the panel pool. That supply pool is the marketplace's real asset, and its integrity is what buyers are actually paying for.",
      "The product surface I spend the most time on is the roadmap for AI-driven quality and fraud detection — working with ML and data science to set precision/recall tradeoffs, escalation thresholds, and reviewer workflows. Cross-functional partners span engineering, design, data science, legal, project delivery, PMM, and research, across timezones, inside a regulated, high-ambiguity environment.",
    ],
    tradeoff: {
      heading: "The quality/cost/latency/trust tradeoff",
      body: "Every fraud-detection threshold is a trade: tighten precision and you burn reviewer time and slow down buyer fulfillment; loosen it and low-quality or fraudulent responses reach buyers and erode trust in the panel. There's no single correct threshold — it moves with buyer segment, geography, and the cost of a reviewer escalation. That's the day-to-day judgment call behind the roadmap: not 'ship a fraud model,' but decide where on that curve the business should sit, and keep moving that line as the panel and the abuse patterns evolve.",
    },
    metrics: [
      {
        label: "Panelist supply pool",
        value: "335M+ across 130+ countries",
        source: "LinkedIn",
      },
      {
        label: "Demand-side buyers",
        value: "10k+",
        source: "LinkedIn",
      },
      {
        label: "Revenue contribution",
        value: "~11% of company revenue (LinkedIn)",
        source: "LinkedIn",
        note: "Stated on LinkedIn; the resume leaves this figure as an unfilled placeholder. Treated as unverified — not used as a headline metric. See CONTENT_REVIEW.md.",
      },
    ],
  },
  {
    id: "mind-wars",
    company: "Zee Entertainment Enterprises Limited",
    title: "Associate Director, Product Management — Chairman's Office",
    dates: "Jun 2021 – May 2024",
    location: "Bengaluru",
    dek: "Built and led a 15-person cross-functional team as Product Lead for Mind Wars, a gamification platform, reporting to the CBO — as Intrapreneur in Residence and Change Manager for the business unit.",
    systemStages: [
      "Content (50+ HTML5 games)",
      "Gamification & personalization",
      "Leaderboards",
      "Wallets",
      "Experimentation infra",
      "Engagement (incl. AI voice)",
    ],
    narrative: [
      "Mind Wars was a gamification platform built on a microservices architecture: content personalization, leaderboards, wallets, and an experimentation layer underneath. I led product for it as Intrapreneur in Residence in the Chairman's Office, building and running a 15-person cross-functional team — SPM, APM, frontend, backend, cloud, Android, iOS, ML, and HTML5 developers — reporting to the CBO.",
      "Over roughly 10+ sprint cycles the team shipped 50+ HTML5 games and 100+ platform features and change requests, including AI-powered voice and engagement elements. The app reached the Top 10 of the Trivia section on the Play Store and carried a 4.2 rating across Play Store and App Store (LinkedIn).",
      "In the same period I led prototype development and deployment of Zee's first Gen AI-powered conversational assistant. LinkedIn describes it as reaching 'a higher than industry benchmark of accuracy, precision score' — no specific number is available anywhere in the source material, so that's reported qualitatively here rather than as a metric.",
    ],
    metrics: [
      {
        label: "Downloads (0 → launch)",
        value: "2.5M+",
        source: "Resume",
        note: "LinkedIn states '2mn+ downloads & registrations' — close but not identical to the resume's 2.5M+. Both are shown; resume used as primary per CONTENT_REVIEW.md.",
      },
      {
        label: "Monthly active users",
        value: "1M+",
        source: "Resume",
      },
      {
        label: "YouTube organic audience",
        value: "1M+ (Resume) / 100k+ (LinkedIn)",
        source: "Resume",
        note: "The two source documents give different YouTube figures. Shown as-is rather than reconciled — see CONTENT_REVIEW.md.",
      },
      {
        label: "Social reach (FB/Instagram, other platforms)",
        value: "200k–300k combined",
        source: "LinkedIn",
        note: "LinkedIn: 300k+ combined FB & Instagram. Resume: 200k+ on 'other platforms.' Ranges differ slightly; both cited.",
      },
      {
        label: "Public reference point",
        value: "111k downloads on Google Play (Mar 2023)",
        source: "Public reference",
        note: "An earlier, lower figure from a Business Standard press release dated March 2023 — cited as a dated public data point, not the current headline number.",
      },
    ],
    sourcingNote:
      "Mind Wars numbers differ between LinkedIn and the resume; both are shown above rather than silently reconciled. Full detail in CONTENT_REVIEW.md.",
  },
  {
    id: "emeritus",
    company: "Emeritus",
    title: "Product Manager",
    dates: "Dec 2019 – Mar 2021",
    location: "Mumbai",
    dek: "Zero-to-one exposure at what Srest describes as his career's second unicorn — owning the Insights App and the experimentation program behind it.",
    systemStages: [
      "Content search & recommendation",
      "A/B testing across journeys",
      "Product pages & qualification flow",
      "Bounce rate & ARPU",
      "Qualified leads",
    ],
    narrative: [
      "At Emeritus — working alongside branding, design, marketing, outreach, tech, and university partners including Columbia, MIT, Northwestern, and London School of Business — I owned the Emeritus Insights App experience: search and recommendation across blogs and videos.",
      "I led a cross-functional pod to implement A/B testing across user journeys. The before/after was direct: bounce rate down 15%, ARPU up 60%.",
      "Separately, I redesigned the product pages and qualification flows, which lifted qualified leads by 50% — a funnel bet on asking better questions earlier, rather than optimizing the top of funnel.",
    ],
    metrics: [
      { label: "Bounce rate", value: "−15%", source: "Resume" },
      { label: "ARPU", value: "+60%", source: "Resume" },
      { label: "Qualified leads", value: "+50%", source: "Resume" },
    ],
  },
  {
    id: "upgrad",
    company: "upGrad.com",
    title: "Product Strategist",
    dates: "Mar 2018 – Dec 2019",
    location: "Mumbai",
    dek: "0-to-1 build of the Digital Marketing vertical — market research through GTM, scaled 3.5x on a referral engine and an instant-score screening test.",
    systemStages: [
      "Market research & user stories",
      "Wireframes & GTM",
      "Screening test (instant score)",
      "Referral engine (OTP-verified)",
      "Top-of-funnel volume",
      "Revenue via referrals",
    ],
    narrative: [
      "I owned the 0-to-1 stage of upGrad's Digital Marketing vertical end to end — market research, user stories, wireframes, and go-to-market — and scaled it from $1M to $3.5M ARR by designing scalable acquisition and referral systems.",
      "Two shipped bets did most of the work: a screening test with an instant score built into onboarding, and a scalable referral engine with OTP verification. Together they expanded top-of-funnel volume 10–11x, with more than 20% of total revenue eventually coming through referrals.",
      "This was during the period LinkedIn describes as upGrad's run from 'soonicorn to unicorn' — cited here as market context, not as a personal outcome.",
    ],
    metrics: [
      { label: "ARR scaled", value: "$1M → $3.5M", source: "Resume" },
      {
        label: "Top-of-funnel volume",
        value: "10–11x",
        source: "Resume",
      },
      {
        label: "Revenue via referrals",
        value: ">20% of total",
        source: "Resume",
      },
    ],
  },
];

export interface EarlyRole {
  company: string;
  title: string;
  titleNote?: string;
  dates: string;
  location: string;
  note: string;
}

export const EARLY_CAREER: EarlyRole[] = [
  {
    company: "Larsen & Toubro",
    title: "Marketing Manager",
    titleNote:
      'LinkedIn: "Marketing Manager," start ~Jun 2016. Resume: "Assistant Manager," start ~May 2016. Rendered neutrally — see CONTENT_REVIEW.md.',
    dates: "2016 – 2018",
    location: "Mumbai",
    note: "Pre-sales, project risk management, and working capital optimization for L&T Defence — including pricing analysis and commercial bid submission on the K9 Vajra armoured vehicle program (an $80mn defense project per the resume), recognized as Top Performer for cost optimization.",
  },
  {
    company: "Cummins Inc.",
    title: "Summer Intern",
    dates: "Apr – May 2015",
    location: "India",
    note: "Market research on purchase drivers for HT alternators; customer segmentation by potential; strategy formulation to grow Cummins' share among high-potential non-Cummins customers.",
  },
  {
    company: "Ingersoll Rand",
    title: "Application Sales Engineer",
    dates: "Aug 2012 – May 2014",
    location: "North India (Delhi NCR)",
    note: "Generated 23.8% (₹2.38 Cr) of North India zone sales of industrial diaphragm pumps; monitored distributor performance, acquired key competitor accounts, and managed customer collections.",
  },
];

export const EARLY_CAREER_LEDE =
  "This is where the commercial foundation was built: selling industrial pumps, then pricing and risk on an ₹80mn defense program. Before product, before AI — the muscle for reading a market and closing a deal.";
