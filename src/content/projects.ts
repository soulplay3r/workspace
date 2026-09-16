// Builds section: personal / independent products, honestly staged.
// Digsparks and Pathwiz were built during a May–Oct 2024 self-employed period
// (LinkedIn frames this as a formal engagement; the resume lists the same
// work under "Projects & Extracurriculars" with no explicit dates — see
// CONTENT_REVIEW.md). Brainlee/BrandBrain is an ongoing, separate build,
// sourced from its own repository rather than the resume or LinkedIn.

export interface Build {
  id: string;
  name: string;
  domain: string;
  link?: string;
  stage: "MVP / prototype" | "In-progress build" | "Shipped microsite";
  problem: string;
  insight: string;
  whatIBuilt: string;
  whatILearned: string;
  whatsNext: string;
  sourcingNote?: string;
}

export const BUILDS: Build[] = [
  {
    id: "brainlee",
    name: "BrandBrain",
    domain: "brainlee.tech",
    link: "https://brainlee.tech",
    stage: "In-progress build",
    problem:
      "Pharma brand teams sit on a fragmented research estate — market studies, HCP interviews, claims substantiation, competitive intel — scattered across formats, with no defensible way to turn it into an answer a medical/legal/regulatory reviewer will sign off on.",
    insight:
      "In a regulated category, the output that matters isn't a synthesized answer — it's a defensible one. Every claim needs an atomic citation, contradictions in the evidence need to be preserved rather than averaged away, and confidence needs to be stated honestly rather than implied.",
    whatIBuilt:
      "BrandBrain: trust-first evidence intelligence for pharma brand teams, with a governed human-review gate in the loop. The architecture is a modular monolith (FastAPI) with ten internal services — ingestion, evidence store, retrieval, synthesizer, brand brain, MLR, trust, audit, recommendation, notification — talking over an event bus, backed by Postgres with pgvector, Redis, S3/MinIO, OIDC, and OpenTelemetry.",
    whatILearned:
      "The marketing site and an interactive prototype (at demo.brainlee.tech) are complete and demo-ready on synthetic data — that's where the trust-and-governance story is easiest to show without real customer data in the loop. The backend is a scaffold with stubbed service methods, not yet a running API. Getting the evidence-and-citation model right, on paper, came before getting a single endpoint live.",
    whatsNext:
      "Turn the scaffold into a running service, starting with ingestion and the evidence store — the two services the trust model depends on most.",
    sourcingNote:
      "Sourced from BrandBrain's own repository (README/handoff docs), not from the resume or LinkedIn — this project predates or runs alongside those documents and isn't listed on either.",
  },
  {
    id: "digsparks",
    name: "Digsparks",
    domain: "digsparks.com",
    link: "https://www.digsparks.com",
    stage: "MVP / prototype",
    problem:
      "Inbound sales conversations are a bottleneck: every lead needs a human on the phone before qualification even starts, and that doesn't scale evenly with lead volume.",
    insight:
      "A speech-to-speech agent that can hold a real conversation — not a scripted IVR tree — can absorb the first pass of an inbound sales conversation and automate the qualification step.",
    whatIBuilt:
      "Led product development for an MVP conversational AI agent that converses with a caller over speech-to-speech, aimed at automating inbound sales conversations.",
    whatILearned:
      "Built and framed as an MVP-stage product — the source material doesn't include customer names, usage numbers, or revenue, so none are claimed here. This is presented as a build-stage case study, not a traction story.",
    whatsNext:
      "No confirmed roadmap in the source material. Flagged in CONTENT_REVIEW.md for the owner to add current status if this is still active.",
  },
  {
    id: "pathwiz",
    name: "Pathwiz",
    domain: "pathwiz.in",
    link: "https://www.pathwiz.in",
    stage: "MVP / prototype",
    problem:
      "Career discovery is usually either a generic aptitude test or unstructured advice — neither adapts to the specific person answering it.",
    insight:
      "Combining structured assessments with personalization and recommendation logic can make career counselling more adaptive than a static test, without requiring a human counsellor for every session.",
    whatIBuilt:
      "Co-created Pathwiz, an AI-enabled career discovery and counselling platform combining assessments, personalization, and recommendation logic.",
    whatILearned:
      "As with Digsparks, no user or scale numbers are available in the source material — this is presented as a co-built platform at prototype stage, not as a scaled product.",
    whatsNext:
      "No confirmed roadmap in the source material.",
  },
  {
    id: "hamara-parivar",
    name: "Hamara Parivar",
    domain: "hamara-parivar.com",
    link: "https://www.hamara-parivar.com",
    stage: "Shipped microsite",
    problem:
      "Zee needed a lightweight, standalone web presence for a PR rebrand exercise.",
    insight:
      "A microsite outside the core product stack, standing up quickly on WordPress, was the right scope for a PR-driven brief.",
    whatIBuilt:
      "Conceptualized and developed a WordPress microsite for Zee as part of a PR rebrand exercise.",
    whatILearned:
      "A small, contained build — included here for completeness rather than as a full case study.",
    whatsNext: "N/A — shipped and scoped as a one-off microsite.",
  },
];

export interface PendingBuild {
  id: string;
  name: string;
  status: string;
}

// No source material exists for OatBuddy anywhere in the resume, LinkedIn PDF,
// or the BrandBrain repo. Rather than invent details, it's shown as an
// explicit placeholder. See CONTENT_REVIEW.md, item #1.
export const PENDING_BUILDS: PendingBuild[] = [
  {
    id: "oatbuddy",
    name: "OatBuddy",
    status: "Case study pending — awaiting source material from the owner.",
  },
];
