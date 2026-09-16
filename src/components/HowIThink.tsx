import { PRINCIPLES } from "../content/principles";
import SectionHeading from "./SectionHeading";

export default function HowIThink() {
  return (
    <section id="how-i-think" className="py-24 container-px scroll-mt-16">
      <div className="max-w-content mx-auto">
        <SectionHeading
          eyebrow="05 — How I Think"
          title="Principles, backed by an example each time"
        />

        <div className="mt-14 space-y-10">
          {PRINCIPLES.map((p, i) => (
            <div key={p.id} className="grid lg:grid-cols-12 gap-6 pb-10 border-b border-ink-200 last:border-b-0">
              <div className="lg:col-span-1 font-mono text-2xl text-ink-200">
                {String(i + 1).padStart(2, "0")}
              </div>
              <div className="lg:col-span-5">
                <h3 className="font-serif text-xl font-semibold text-ink-950">
                  {p.title}
                </h3>
                <p className="mt-3 text-ink-600 leading-relaxed text-sm">{p.body}</p>
              </div>
              <div className="lg:col-span-6 bg-ink-50 border border-ink-200 p-5">
                <p className="font-mono text-[10px] uppercase tracking-wide text-signal mb-2">
                  In practice
                </p>
                <p className="text-ink-700 leading-relaxed text-sm">{p.example}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
