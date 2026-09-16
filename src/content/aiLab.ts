// AI Lab: forward-looking systems thinking. None of these are shipped
// products — every entry is explicitly labeled by stage and framed as
// problem + intended architecture, not as a delivered result.

export type LabStage = "CONCEPT" | "IN DEVELOPMENT" | "EXPERIMENT";

export interface LabProject {
  id: string;
  name: string;
  stage: LabStage;
  problem: string;
  approach: string[];
}

export const AI_LAB: LabProject[] = [
  {
    id: "model-router",
    name: "Adaptive Model Router",
    stage: "CONCEPT",
    problem:
      "Every LLM call is a quality/cost/latency decision, and most product teams hardcode one model for every request regardless of how hard the request actually is. That's a product-economics problem before it's an engineering one — the same failure mode as a marketplace that prices every transaction the same regardless of risk.",
    approach: [
      "Classify incoming requests by task difficulty and downstream cost of a wrong answer, not just by input length.",
      "Route low-stakes, high-volume requests to cheaper/faster models; reserve frontier models for requests where the cost of an error is high.",
      "Track quality drift per route with a lightweight eval set, so routing decisions degrade gracefully instead of silently.",
      "Treat the router's thresholds the same way the SurveyMonkey fraud thresholds get treated: a tunable business decision, not a fixed setting.",
    ],
  },
  {
    id: "experiment-analyst",
    name: "Experiment Analyst",
    stage: "CONCEPT",
    problem:
      "Reading out an A/B test correctly — significance, guardrail metrics, segment effects, novelty decay — takes analyst time that most product teams don't have for every experiment they run.",
    approach: [
      "Ingest raw experiment results and produce a structured readout: primary metric, guardrails, segment splits, and a plain-language call on ship/hold/kill.",
      "Flag common statistical traps (peeking, underpowered segments, novelty effects) rather than silently trusting the topline number.",
      "Keep a human decision-maker in the loop for the ship call — the tool's job is to make the evidence legible fast, not to make the call.",
    ],
  },
  {
    id: "prd-doctor",
    name: "PRD Doctor",
    stage: "CONCEPT",
    problem:
      "Most PRD feedback happens late, from a senior reviewer, on prose — after the thinking is already locked in. Gaps in the actual reasoning (unstated assumptions, missing failure modes, no rollback plan) are the expensive kind to catch late.",
    approach: [
      "Read a draft PRD against a structural checklist: problem framing, success metrics, failure modes, rollback plan, and who owns the tradeoffs.",
      "Surface the gaps as questions, not rewrites — the goal is sharper thinking from the author, not a templated document.",
      "Calibrate the checklist against real PRDs from marketplace, trust & safety, and experimentation domains rather than a generic template.",
    ],
  },
  {
    id: "agent-eval-lab",
    name: "Agent Evaluation Lab",
    stage: "EXPERIMENT",
    problem:
      "Agentic products fail in ways a single accuracy number doesn't capture — a tool-calling loop that technically completes but takes an unsafe path, or a system that looks fine per-turn but drifts over a long session.",
    approach: [
      "Build task-specific eval suites that score full trajectories, not just final outputs — where a fraud-review agent or a support agent went, not just where it ended up.",
      "Borrow the precision/recall/escalation-threshold framing from the SurveyMonkey trust work and apply it to agent outputs: false positives and false negatives both have a cost, and the eval should say which.",
      "Start narrow — one agent, one task family — before generalizing the harness.",
    ],
  },
  {
    id: "strategy-swarm",
    name: "Multi-Agent Product Strategy Swarm",
    stage: "CONCEPT",
    problem:
      "Early-stage product strategy work benefits from adversarial framing — a market-research view, a finance view, a systems-risk view — that's normally distributed across different people in different meetings, slowly.",
    approach: [
      "Stand up a small set of role-specific agents (market, finance, systems-risk, customer-voice) that critique the same strategy brief from different angles in parallel.",
      "Force explicit disagreement to the surface rather than averaging it into a bland consensus summary — the same 'preserve contradictions' principle behind the BrandBrain evidence model.",
      "Treat the output as a sharper set of questions for a human strategy review, not a decision.",
    ],
  },
];
