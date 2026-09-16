// How I Think: product principles, each grounded in a real example from
// the Work section — no generic PM aphorisms without evidence attached.

export interface Principle {
  id: string;
  title: string;
  body: string;
  example: string;
}

export const PRINCIPLES: Principle[] = [
  {
    id: "trust-is-a-tradeoff",
    title: "Trust is a tunable dial, not a fixed setting",
    body: "Precision and recall trade against each other, and every threshold you set is a business decision wearing an engineering costume. The job is deciding where the line sits, and revisiting it as conditions change — not treating 'ship the fraud model' as a one-time task.",
    example:
      "At SurveyMonkey, every fraud-detection threshold trades reviewer cost and buyer fulfillment speed against the risk of low-quality responses reaching a buyer. That line moves by buyer segment and geography — it's owned, not set once.",
  },
  {
    id: "funnel-bets-beat-features",
    title: "A funnel redesign beats another feature",
    body: "Teams default to shipping something new. Often the highest-leverage move is redesigning the path a user already walks — where they qualify, where they drop, what they're asked and when.",
    example:
      "At Emeritus, redesigning the product pages and qualification flow — not adding a feature — lifted qualified leads by 50%. The upGrad referral engine and instant-score screening test did the same for top-of-funnel volume: 10–11x, by changing the path, not adding to the app.",
  },
  {
    id: "evidence-over-consensus",
    title: "Preserve disagreement in the data — don't average it away",
    body: "A synthesized answer that smooths over contradictory evidence is a worse answer than one that shows the contradiction and states its confidence honestly. This matters most in regulated or high-stakes domains, where the wrong kind of confidence is expensive.",
    example:
      "It's the core design principle behind BrandBrain's evidence model for pharma brand teams: every output cites an atomic source, contradictions are preserved rather than averaged, and confidence is stated honestly rather than implied.",
  },
  {
    id: "launch-before-scale",
    title: "Earn the right to scale before you optimize for it",
    body: "A 0-to-1 build should prove the mechanic works before it's asked to be efficient. The team, the architecture, and the roadmap cadence should match the stage — not the ambition.",
    example:
      "Mind Wars went from zero to a 15-person cross-functional team shipping 50+ HTML5 games and 100+ features across 10+ sprint cycles, reaching Top 10 in the Play Store's Trivia section, before the platform's personalization and experimentation infrastructure was asked to carry more weight.",
  },
  {
    id: "commercial-instinct",
    title: "Read the market before you read the backlog",
    body: "Years spent selling pumps and pricing a defense program teach a different instinct than years spent writing PRDs: what a buyer actually weighs, where the real objection is, what a number in a bid actually costs. That instinct doesn't disappear when the product is software.",
    example:
      "That's the throughline from Ingersoll Rand (23.8% of North India zone pump sales) and L&T (pricing and commercial bid submission on an ₹80mn defense program) into every acquisition and pricing decision made since — at upGrad, Emeritus, Zee, and SurveyMonkey.",
  },
];
