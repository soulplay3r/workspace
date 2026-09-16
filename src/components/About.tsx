import { CAREER_ARC, EDUCATION } from "../content/education";
import { CAPABILITY_AREAS, CERTIFICATIONS, LANGUAGES, SKILL_GROUPS } from "../content/skills";
import SectionHeading from "./SectionHeading";

export default function About() {
  return (
    <section id="about" className="py-24 container-px scroll-mt-16 bg-ink-50/60">
      <div className="max-w-content mx-auto">
        <SectionHeading
          eyebrow="06 — About"
          title="The arc, briefly"
          dek="Product Leader with 12+ years building intelligent, data-driven systems at global scale — spanning marketplaces, experimentation platforms, and human-in-the-loop ML products. Specialized in AI-powered quality, fraud, and monetization layers across two-sided platforms."
        />

        <div className="mt-12 flex flex-wrap items-center gap-3" aria-label="Career arc">
          {CAREER_ARC.map((stage, i) => (
            <span key={stage} className="flex items-center gap-3">
              <span className="rounded-sm border border-ink-300 bg-paper px-3 py-1.5 font-mono text-xs text-ink-700">
                {stage}
              </span>
              {i < CAREER_ARC.length - 1 && (
                <span className="text-signal" aria-hidden="true">
                  →
                </span>
              )}
            </span>
          ))}
        </div>

        <div className="mt-16 grid lg:grid-cols-2 gap-12">
          <div>
            <p className="font-mono text-xs uppercase tracking-wide text-signal mb-4">
              Capability areas
            </p>
            <ul className="grid grid-cols-2 gap-x-4 gap-y-2">
              {CAPABILITY_AREAS.map((c) => (
                <li key={c} className="text-sm text-ink-700 leading-snug">
                  {c}
                </li>
              ))}
            </ul>

            <p className="font-mono text-xs uppercase tracking-wide text-signal mt-8 mb-4">
              Education
            </p>
            <ul className="space-y-3">
              {EDUCATION.map((e) => (
                <li key={e.institution} className="text-sm">
                  <span className="text-ink-900 font-medium">{e.institution}</span>
                  <span className="text-ink-500"> — {e.program}</span>
                  {e.years && <span className="text-ink-400"> ({e.years})</span>}
                  {e.programNote && (
                    <span
                      className="ml-1 cursor-help text-signal text-xs"
                      title={e.programNote}
                    >
                      [note]
                    </span>
                  )}
                </li>
              ))}
            </ul>
          </div>

          <div>
            <p className="font-mono text-xs uppercase tracking-wide text-signal mb-4">
              Tools & skills
            </p>
            <div className="space-y-5">
              {SKILL_GROUPS.map((g) => (
                <div key={g.label}>
                  <p className="text-xs text-ink-500 mb-1.5">{g.label}</p>
                  <div className="flex flex-wrap gap-1.5">
                    {g.items.map((item) => (
                      <span
                        key={item}
                        className="rounded-sm bg-ink-100 px-2 py-1 text-xs text-ink-700"
                      >
                        {item}
                      </span>
                    ))}
                  </div>
                </div>
              ))}
            </div>

            <p className="font-mono text-xs uppercase tracking-wide text-signal mt-8 mb-4">
              Certifications
            </p>
            <ul className="space-y-1.5">
              {CERTIFICATIONS.map((c) => (
                <li key={c.name} className="text-sm text-ink-700">
                  {c.name}
                  {c.note && (
                    <span className="ml-1 cursor-help text-signal text-xs" title={c.note}>
                      [note]
                    </span>
                  )}
                </li>
              ))}
            </ul>

            <p className="font-mono text-xs uppercase tracking-wide text-signal mt-8 mb-4">
              Languages
            </p>
            <p className="text-sm text-ink-700">
              {LANGUAGES.map((l) => `${l.name} (${l.level})`).join(" · ")}
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
