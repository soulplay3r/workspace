import { CASE_STUDIES, EARLY_CAREER, EARLY_CAREER_LEDE } from "../content/experience";
import CaseStudyCard from "./CaseStudy";
import SectionHeading from "./SectionHeading";

export default function Work() {
  return (
    <section id="work" className="py-24 container-px scroll-mt-16 bg-ink-50/60">
      <div className="max-w-content mx-auto">
        <SectionHeading
          eyebrow="02 — Work"
          title="Product stories, not a bullet timeline"
          dek="Four roles, told as systems: what fed what, where the tradeoff lived, and what moved because of it."
        />

        <div className="mt-8">
          {CASE_STUDIES.map((study, i) => (
            <CaseStudyCard key={study.id} study={study} reverse={i % 2 === 1} />
          ))}
        </div>

        <div className="mt-4 pt-12 border-t border-ink-200">
          <p className="section-eyebrow mb-2">Earlier career</p>
          <p className="text-ink-600 max-w-2xl mb-8">{EARLY_CAREER_LEDE}</p>
          <div className="grid sm:grid-cols-3 gap-6">
            {EARLY_CAREER.map((role) => (
              <div key={role.company} className="border border-ink-200 p-5">
                <p className="font-mono text-[11px] text-ink-400">{role.dates}</p>
                <h4 className="mt-1 font-serif text-lg font-semibold text-ink-950">
                  {role.company}
                </h4>
                <p className="text-sm text-ink-500">
                  {role.title}
                  {role.titleNote && (
                    <sup className="ml-1 cursor-help text-signal" title={role.titleNote}>
                      [note]
                    </sup>
                  )}
                </p>
                <p className="mt-3 text-xs text-ink-600 leading-relaxed">{role.note}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
