import { useState } from "react";
import type { CaseStudy } from "../content/experience";

export default function CaseStudyCard({ study, reverse }: { study: CaseStudy; reverse: boolean }) {
  const [showSourcing, setShowSourcing] = useState(false);

  return (
    <article className="py-16 border-b border-ink-200 last:border-b-0">
      <div className="grid lg:grid-cols-12 gap-10">
        <div className="lg:col-span-4">
          <p className="font-mono text-xs uppercase tracking-wide text-signal">
            {study.dates}
          </p>
          <h3 className="mt-2 font-serif text-2xl font-semibold text-ink-950">
            {study.company}
          </h3>
          <p className="mt-1 text-sm text-ink-500">
            {study.title}
            {study.titleNote && (
              <sup className="ml-1 cursor-help text-signal" title={study.titleNote}>
                [note]
              </sup>
            )}
          </p>
          <p className="mt-1 text-xs text-ink-400">{study.location}</p>
          <p className="mt-5 text-ink-700 leading-relaxed">{study.dek}</p>

          <ol className="mt-8 flex flex-wrap gap-x-2 gap-y-3" aria-label="System flow">
            {study.systemStages.map((stage, i) => (
              <li key={stage} className="flex items-center gap-2">
                <span className="rounded-sm border border-ink-200 bg-ink-50 px-2.5 py-1 font-mono text-[11px] text-ink-700">
                  {stage}
                </span>
                {i < study.systemStages.length - 1 && (
                  <span className="text-ink-300" aria-hidden="true">
                    →
                  </span>
                )}
              </li>
            ))}
          </ol>
        </div>

        <div className={`lg:col-span-8 ${reverse ? "lg:order-first" : ""}`}>
          <div className="space-y-4">
            {study.narrative.map((p, i) => (
              <p key={i} className="text-ink-700 leading-relaxed">
                {p}
              </p>
            ))}
          </div>

          {study.tradeoff && (
            <div className="mt-6 border-l-2 border-signal pl-5 py-1">
              <p className="font-mono text-xs uppercase tracking-wide text-signal mb-2">
                {study.tradeoff.heading}
              </p>
              <p className="text-ink-700 leading-relaxed text-sm">{study.tradeoff.body}</p>
            </div>
          )}

          <div className="mt-8 grid sm:grid-cols-2 gap-4">
            {study.metrics.map((m) => (
              <div key={m.label} className="border border-ink-200 p-4">
                <div className="font-serif text-xl font-semibold text-ink-950">
                  {m.value}
                </div>
                <div className="mt-1 text-xs text-ink-500">{m.label}</div>
                {m.note && (
                  <div className="mt-2 text-[11px] text-ink-400 leading-snug border-t border-ink-100 pt-2">
                    {m.note}
                  </div>
                )}
              </div>
            ))}
          </div>

          {study.sourcingNote && (
            <div className="mt-4">
              <button
                type="button"
                onClick={() => setShowSourcing((s) => !s)}
                className="font-mono text-[11px] uppercase tracking-wide text-ink-400 hover:text-ink-700"
              >
                {showSourcing ? "Hide sourcing note −" : "Sourcing note +"}
              </button>
              {showSourcing && (
                <p className="mt-2 text-xs text-ink-500 leading-relaxed max-w-lg">
                  {study.sourcingNote}
                </p>
              )}
            </div>
          )}
        </div>
      </div>
    </article>
  );
}
