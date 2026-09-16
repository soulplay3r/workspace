import { PURSUITS, VOLUNTEER } from "../content/personal";

export default function Beyond() {
  return (
    <section id="beyond" className="py-16 container-px scroll-mt-16 bg-ink-50/60">
      <div className="max-w-content mx-auto">
        <p className="section-eyebrow mb-3">08 — Beyond the Roadmap</p>
        <div className="flex flex-wrap items-center gap-x-3 gap-y-2 text-ink-500 text-sm">
          {PURSUITS.map((p, i) => (
            <span key={p}>
              {p}
              {i < PURSUITS.length - 1 && <span className="text-ink-300 ml-3">·</span>}
            </span>
          ))}
        </div>
        <p className="mt-3 text-ink-400 text-sm">{VOLUNTEER}</p>
      </div>
    </section>
  );
}
