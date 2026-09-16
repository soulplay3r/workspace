import { CONTACT, RESUME_PATH } from "../content/metrics";

export default function Contact() {
  return (
    <section id="contact" className="py-28 container-px scroll-mt-16 bg-ink-950 text-paper">
      <div className="max-w-content mx-auto text-center">
        <p className="section-eyebrow mb-3">09 — Contact</p>
        <h2 className="font-serif text-3xl sm:text-4xl lg:text-5xl font-semibold tracking-tight max-w-2xl mx-auto">
          Building something difficult? Let's talk.
        </h2>

        <div className="mt-10 flex flex-wrap justify-center gap-4">
          <a
            href={`mailto:${CONTACT.email}`}
            className="inline-flex items-center rounded-sm bg-paper text-ink-950 px-6 py-3 font-mono text-xs uppercase tracking-wide hover:bg-ink-100 transition-colors"
          >
            {CONTACT.email}
          </a>
          <a
            href={CONTACT.linkedin}
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center rounded-sm border border-ink-600 px-6 py-3 font-mono text-xs uppercase tracking-wide hover:border-paper transition-colors"
          >
            LinkedIn ↗
          </a>
          <a
            href={RESUME_PATH}
            download
            className="inline-flex items-center rounded-sm border border-ink-600 px-6 py-3 font-mono text-xs uppercase tracking-wide hover:border-paper transition-colors"
          >
            Résumé ↓
          </a>
        </div>

        <p className="mt-8 font-mono text-xs text-ink-500">
          {CONTACT.location} · {CONTACT.phone}
        </p>
      </div>
    </section>
  );
}
