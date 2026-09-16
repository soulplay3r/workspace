import { DOMAINS } from "../content/domains";
import SectionHeading from "./SectionHeading";

export default function WhatIBuild() {
  return (
    <section aria-labelledby="what-i-build-heading" className="py-24 container-px">
      <div className="max-w-content mx-auto">
        <SectionHeading
          eyebrow="What I Build"
          title="Five domains, one operating pattern"
        />
        <div className="mt-14 grid sm:grid-cols-2 lg:grid-cols-5 gap-px bg-ink-200">
          {DOMAINS.map((d, i) => (
            <div key={d.id} className="bg-paper p-6 flex flex-col">
              <span className="font-mono text-xs text-ink-400">
                {String(i + 1).padStart(2, "0")}
              </span>
              <h3 className="mt-3 font-serif text-lg font-semibold text-ink-950">
                {d.name}
              </h3>
              <p className="mt-3 text-sm text-ink-600 leading-relaxed">{d.body}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
