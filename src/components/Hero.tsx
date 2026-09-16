import { CONTACT, RESUME_PATH } from "../content/metrics";

export default function Hero() {
  return (
    <section id="home" className="relative pt-32 pb-20 container-px scroll-mt-16">
      <div className="max-w-content mx-auto">
        <p className="section-eyebrow mb-6">AI Product Leader · Bengaluru</p>
        <h1 className="font-serif text-4xl sm:text-5xl lg:text-6xl font-semibold tracking-tight text-ink-950 max-w-4xl leading-[1.08]">
          I build businesses <span className="text-signal">through</span> products.
        </h1>
        <p className="mt-7 text-lg sm:text-xl text-ink-600 max-w-2xl leading-relaxed">
          Most product managers build features. Over the last 12+ years — starting
          in industrial sales, then marketing, then product — I've built and scaled
          global digital platforms across AI, marketplaces, pricing, and
          experimentation: trust and fraud systems at SurveyMonkey, a
          gamification platform at Zee, growth engines at upGrad and Emeritus.
          The edge isn't writing PRDs. It's seeing the pattern in the data and
          taking the decision.
        </p>

        <div className="mt-10 flex flex-wrap items-center gap-4">
          <a
            href="#work"
            className="inline-flex items-center rounded-sm bg-ink-950 text-paper px-6 py-3 font-mono text-xs uppercase tracking-wide hover:bg-ink-800 transition-colors"
          >
            View My Work
          </a>
          <a
            href="#contact"
            className="inline-flex items-center rounded-sm border border-ink-300 px-6 py-3 font-mono text-xs uppercase tracking-wide text-ink-900 hover:border-ink-900 transition-colors"
          >
            Let's Talk
          </a>
          <a
            href={CONTACT.github}
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center px-2 py-3 font-mono text-xs uppercase tracking-wide text-ink-500 hover:text-ink-900 transition-colors"
          >
            View GitHub ↗
          </a>
          <a
            href={RESUME_PATH}
            download
            className="inline-flex items-center px-2 py-3 font-mono text-xs uppercase tracking-wide text-ink-500 hover:text-ink-900 transition-colors"
          >
            Download Résumé ↓
          </a>
        </div>
      </div>
    </section>
  );
}
