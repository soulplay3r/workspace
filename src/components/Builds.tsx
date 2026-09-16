import { useState } from "react";
import { BUILDS, PENDING_BUILDS } from "../content/projects";
import SectionHeading from "./SectionHeading";

function BuildCard({ build }: { build: (typeof BUILDS)[number] }) {
  const [open, setOpen] = useState(false);

  return (
    <article className="border border-ink-200 flex flex-col">
      <div className="p-6 flex-1">
        <div className="flex items-start justify-between gap-4">
          <div>
            <h3 className="font-serif text-xl font-semibold text-ink-950">
              {build.name}
            </h3>
            {build.link ? (
              <a
                href={build.link}
                target="_blank"
                rel="noreferrer"
                className="text-xs text-signal hover:underline"
              >
                {build.domain} ↗
              </a>
            ) : (
              <span className="text-xs text-ink-400">{build.domain}</span>
            )}
          </div>
          <span className="shrink-0 rounded-sm border border-ink-300 px-2 py-1 font-mono text-[10px] uppercase tracking-wide text-ink-500">
            {build.stage}
          </span>
        </div>

        <dl className="mt-5 space-y-3 text-sm">
          <div>
            <dt className="font-mono text-[10px] uppercase tracking-wide text-signal">
              Problem
            </dt>
            <dd className="mt-1 text-ink-700 leading-relaxed">{build.problem}</dd>
          </div>
          <div>
            <dt className="font-mono text-[10px] uppercase tracking-wide text-signal">
              Insight
            </dt>
            <dd className="mt-1 text-ink-700 leading-relaxed">{build.insight}</dd>
          </div>
          <div>
            <dt className="font-mono text-[10px] uppercase tracking-wide text-signal">
              What I Built
            </dt>
            <dd className="mt-1 text-ink-700 leading-relaxed">{build.whatIBuilt}</dd>
          </div>

          {open && (
            <>
              <div>
                <dt className="font-mono text-[10px] uppercase tracking-wide text-signal">
                  What I Learned
                </dt>
                <dd className="mt-1 text-ink-700 leading-relaxed">{build.whatILearned}</dd>
              </div>
              <div>
                <dt className="font-mono text-[10px] uppercase tracking-wide text-signal">
                  What Happened Next
                </dt>
                <dd className="mt-1 text-ink-700 leading-relaxed">{build.whatsNext}</dd>
              </div>
              {build.sourcingNote && (
                <p className="text-[11px] text-ink-400 leading-relaxed border-t border-ink-100 pt-3">
                  {build.sourcingNote}
                </p>
              )}
            </>
          )}
        </dl>
      </div>
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        className="border-t border-ink-200 py-3 font-mono text-[11px] uppercase tracking-wide text-ink-500 hover:text-ink-900 hover:bg-ink-50 transition-colors"
      >
        {open ? "Show less −" : "What I learned & what's next +"}
      </button>
    </article>
  );
}

export default function Builds() {
  return (
    <section id="builds" className="py-24 container-px scroll-mt-16">
      <div className="max-w-content mx-auto">
        <SectionHeading
          eyebrow="03 — Builds"
          title="Independent products, honestly staged"
          dek="Problem → insight → what got built → what got learned. Prototype-stage work is labeled as prototype-stage — no traction numbers that don't exist."
        />

        <div className="mt-14 grid md:grid-cols-2 gap-6">
          {BUILDS.map((b) => (
            <BuildCard key={b.id} build={b} />
          ))}

          {PENDING_BUILDS.map((p) => (
            <div
              key={p.id}
              className="border border-dashed border-ink-300 p-6 flex flex-col items-start justify-center min-h-[200px] bg-ink-50/50"
            >
              <span className="rounded-sm border border-ink-300 px-2 py-1 font-mono text-[10px] uppercase tracking-wide text-ink-500 mb-3">
                Awaiting source material
              </span>
              <h3 className="font-serif text-xl font-semibold text-ink-400">{p.name}</h3>
              <p className="mt-2 text-sm text-ink-500 leading-relaxed">{p.status}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
