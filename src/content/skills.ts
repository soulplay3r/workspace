export interface SkillGroup {
  label: string;
  items: string[];
}

export const SKILL_GROUPS: SkillGroup[] = [
  {
    label: "AI & Data",
    items: [
      "SQL",
      "Python (working)",
      "Snowflake",
      "Splunk",
      "Tableau",
      "Amplitude",
      "Mixpanel",
      "Claude Code",
      "GPT",
      "Gemini",
      "Replit",
      "Lovable",
    ],
  },
  {
    label: "Product & Experimentation",
    items: ["A/B Testing", "Jira", "Confluence", "PostHog", "Google Analytics"],
  },
  {
    label: "Infra & APIs",
    items: ["AWS", "Postman", "Microservices", "APIs"],
  },
  {
    label: "Design & Collaboration",
    items: ["Figma", "Canva", "Magic Patterns", "Miro"],
  },
];

export const CAPABILITY_AREAS: string[] = [
  "AI Marketplace & Platform Strategy",
  "Human-in-the-Loop ML Systems",
  "Trust, Safety & Fraud Detection",
  "Experimentation & Evaluation Frameworks",
  "Monetization & Usage-Based Pricing",
  "Large-Scale Funnel Optimization",
  "Cross-Functional Leadership",
  "Go-to-Market Strategy",
];

export const CERTIFICATIONS: { name: string; source: string; note?: string }[] = [
  { name: "Certified Scrum Product Owner (CSPO)", source: "LinkedIn & Resume" },
  { name: "Generative AI", source: "LinkedIn" },
  { name: "Google AdWords Certified Professional", source: "LinkedIn" },
  { name: "Python Data Structures", source: "LinkedIn" },
  {
    name: "AWS Cloud Practitioner",
    source: "Resume",
    note: "Listed on the resume only — not present on LinkedIn.",
  },
  {
    name: "SwaggerHub API Product Owner",
    source: "Resume",
    note: "Listed on the resume only — not present on LinkedIn.",
  },
];

export const LANGUAGES: { name: string; level: string }[] = [
  { name: "Bengali", level: "Native / bilingual" },
  { name: "Hindi", level: "Full professional" },
  { name: "English", level: "Full professional" },
  { name: "Spanish", level: "Elementary" },
];
