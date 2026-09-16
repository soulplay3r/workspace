import { WRITING_STATUS } from "../content/writing";

export default function Writing() {
  return (
    <section id="writing" className="py-24 container-px scroll-mt-16">
      <div className="max-w-content mx-auto text-center max-w-prose mx-auto">
        <p className="section-eyebrow mb-3">07 — Field Notes</p>
        <h2 className="section-heading">{WRITING_STATUS.headline}</h2>
        <p className="mt-4 text-ink-600 text-lg leading-relaxed">{WRITING_STATUS.body}</p>
        <div className="mt-8 inline-flex items-center rounded-sm border border-dashed border-ink-300 px-4 py-2 font-mono text-xs uppercase tracking-wide text-ink-400">
          Coming soon
        </div>
      </div>
    </section>
  );
}
