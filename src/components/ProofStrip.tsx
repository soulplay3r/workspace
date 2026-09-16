import { useState } from "react";
import { PROOF_METRICS } from "../content/metrics";

export default function ProofStrip() {
  const [openId, setOpenId] = useState<string | null>(null);

  return (
    <section aria-label="Career proof points" className="border-y border-ink-200 bg-ink-950">
      <div className="max-w-content mx-auto container-px py-10">
        <div className="grid grid-cols-2 sm:grid-cols-5 gap-6 sm:gap-4">
          {PROOF_METRICS.map((m) => {
            const isOpen = openId === m.id;
            return (
              <button
                key={m.id}
                type="button"
                onClick={() => setOpenId(isOpen ? null : m.id)}
                aria-expanded={isOpen}
                className="text-left group"
              >
                <div className="font-serif text-2xl sm:text-3xl font-semibold text-paper">
                  {m.value}
                </div>
                <div className="mt-1 text-xs text-ink-400 leading-snug group-hover:text-ink-300">
                  {m.label}
                </div>
                <div className="mt-1 font-mono text-[10px] uppercase tracking-wide text-signal-light">
                  {isOpen ? "Hide source −" : "Source & context +"}
                </div>
              </button>
            );
          })}
        </div>

        {openId && (
          <div className="mt-6 border-t border-ink-800 pt-5 text-sm text-ink-300 leading-relaxed max-w-2xl">
            <span className="font-mono text-[10px] uppercase tracking-wide text-signal-light mr-2">
              {PROOF_METRICS.find((m) => m.id === openId)?.source}
            </span>
            {PROOF_METRICS.find((m) => m.id === openId)?.context}
          </div>
        )}
      </div>
    </section>
  );
}
