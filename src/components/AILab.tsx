import { AI_LAB, type LabStage } from "../content/aiLab";

const STAGE_STYLES: Record<LabStage, string> = {
  CONCEPT: "border-ink-300 text-ink-500",
  "IN DEVELOPMENT": "border-signal text-signal",
  EXPERIMENT: "border-ink-600 text-ink-700",
};

export default function AILab() {
  return (
    <section id="ai-lab" className="py-24 container-px scroll-mt-16 bg-ink-950 text-paper">
      <div className="max-w-content mx-auto">
        <p className="section-eyebrow mb-3">04 — AI Lab</p>
        <h2 className="font-serif text-3xl sm:text-4xl font-semibold tracking-tight">
          Forward-looking systems thinking
        </h2>
        <p className="mt-4 text-ink-300 text-lg leading-relaxed max-w-prose">
          None of this is shipped. Each entry is a problem framed as a product
          question, with the intended architecture — not a delivered result.
        </p>

        <div className="mt-14 grid md:grid-cols-2 gap-px bg-ink-800">
          {AI_LAB.map((project) => (
            <div key={project.id} className="bg-ink-950 p-7">
              <div className="flex items-center justify-between gap-4">
                <h3 className="font-serif text-xl font-semibold">{project.name}</h3>
                <span
                  className={`shrink-0 rounded-sm border px-2 py-1 font-mono text-[10px] uppercase tracking-wide ${STAGE_STYLES[project.stage]}`}
                >
                  {project.stage}
                </span>
              </div>
              <p className="mt-4 text-sm text-ink-300 leading-relaxed">{project.problem}</p>
              <ul className="mt-4 space-y-2">
                {project.approach.map((step, i) => (
                  <li key={i} className="flex gap-3 text-sm text-ink-400 leading-relaxed">
                    <span className="font-mono text-[10px] text-signal-light pt-0.5">
                      {String(i + 1).padStart(2, "0")}
                    </span>
                    {step}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
