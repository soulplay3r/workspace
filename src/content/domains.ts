export interface Domain {
  id: string;
  name: string;
  body: string;
}

export const DOMAINS: Domain[] = [
  {
    id: "ai-systems",
    name: "AI & Intelligent Systems",
    body: "Human-in-the-loop ML for quality and fraud detection at SurveyMonkey; a Gen AI conversational assistant at Zee; a speech-to-speech sales agent at Digsparks. Precision/recall and escalation thresholds as product decisions, not engineering settings.",
  },
  {
    id: "marketplaces",
    name: "Marketplaces",
    body: "SurveyMonkey's Audience Marketplace: 335M+ panelists across 130+ countries on the supply side, 10k+ buyers on demand. Owning both sides of a two-sided market at once, not just the storefront.",
  },
  {
    id: "experimentation",
    name: "Experimentation & Analytics",
    body: "A/B testing across user journeys at Emeritus cut bounce rate 15% and lifted ARPU 60%. Experimentation infrastructure underneath Mind Wars' leaderboards and wallets. Data patterns, not opinions, decide the roadmap.",
  },
  {
    id: "growth",
    name: "Growth & Monetization",
    body: "Scaled upGrad's Digital Marketing vertical from $1M to $3.5M ARR with a referral engine and an instant-score screening test — a 10–11x lift in top-of-funnel volume from redesigning the funnel, not adding features.",
  },
  {
    id: "zero-to-one",
    name: "Zero-to-One Products",
    body: "Mind Wars from zero to a 15-person team and 2.5M+ downloads. BrandBrain from a README to a demo-ready prototype. The instinct for what to build first, and what to leave a stub, transfers across both.",
  },
];
