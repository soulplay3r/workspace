// Site-wide constants and the hero proof strip.
// Every figure here traces to the resume or LinkedIn PDF. Anything with looser
// sourcing carries a `note` that renders on click/expand — see CONTENT_REVIEW.md
// for the full discrepancy log.

export const CONTACT = {
  name: "Srest Das",
  legalName: "Srestangsh Das",
  email: "srestangsh21dec@gmail.com",
  phone: "+91 77588 37293",
  linkedin: "https://www.linkedin.com/in/srest-das-a6a18949",
  // No GitHub profile URL was found in any source document. Placeholder —
  // owner to confirm and this link to be updated. See CONTENT_REVIEW.md.
  github: "https://github.com/soulplay3r",
  githubIsPlaceholder: true,
  location: "Bengaluru, Karnataka, India",
};

// No resume PDF file was supplied. Placeholder path — drop a real resume.pdf
// into /public and this will resolve. See CONTENT_REVIEW.md.
export const RESUME_PATH = "/resume-placeholder.md";
export const RESUME_IS_PLACEHOLDER = true;

export interface ProofMetric {
  id: string;
  value: string;
  label: string;
  context: string;
  source: "LinkedIn" | "Resume" | "LinkedIn & Resume";
}

export const PROOF_METRICS: ProofMetric[] = [
  {
    id: "years",
    value: "12+ yrs",
    label: "product & commercial experience",
    context:
      "Career arc from industrial pump sales (Ingersoll Rand, 2012) through marketing (L&T), product strategy (upGrad, Emeritus) to AI product leadership (Zee, SurveyMonkey).",
    source: "Resume",
  },
  {
    id: "panel",
    value: "335M+",
    label: "panelists on the marketplace supply side",
    context:
      "SurveyMonkey Audience Marketplace panel pool across 130+ countries, spanning 10k+ demand-side buyers, owned end-to-end since Nov 2024.",
    source: "LinkedIn",
  },
  {
    id: "downloads",
    value: "2.5M+",
    label: "downloads, Mind Wars (Zee)",
    context:
      "Resume figure for the Mind Wars gamification platform (0→2.5M+ downloads, 1M+ MAU). LinkedIn separately states 2mn+ downloads & registrations — the two sources don't fully reconcile; see CONTENT_REVIEW.md.",
    source: "Resume",
  },
  {
    id: "arc",
    value: "$1M → $3.5M ARR",
    label: "Digital Marketing vertical scaled, upGrad",
    context:
      "0-to-1 build of upGrad's Digital Marketing vertical: scaled from $1M to $3.5M ARR via a referral engine and screening-test funnel that expanded top-of-funnel volume 10–11x.",
    source: "Resume",
  },
  {
    id: "countries",
    value: "130+",
    label: "countries in the panel network",
    context:
      "Geographic footprint of the SurveyMonkey Audience Marketplace's supply side, which spans web and mobile app.",
    source: "LinkedIn",
  },
];
