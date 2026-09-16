import { CONTACT } from "../content/metrics";

export default function Footer() {
  return (
    <footer className="py-8 container-px border-t border-ink-200">
      <div className="max-w-content mx-auto flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-ink-400">
        <span>© {new Date().getFullYear()} {CONTACT.legalName}</span>
        <span>Built with React, TypeScript & Tailwind CSS.</span>
      </div>
    </footer>
  );
}
