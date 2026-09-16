# Srest Das — Personal Site

A single-page, editorial-style personal site for Srest Das (Srestangsh Das),
positioning him as a senior AI Product Leader: hero → proof → work → AI Lab
→ builds → how he thinks → about → contact, navigable in under 90 seconds.

**Before editing content, read [`CONTENT_REVIEW.md`](./CONTENT_REVIEW.md)** —
it lists every resume/LinkedIn discrepancy, unverified claim, and missing
asset (GitHub URL, resume PDF, OatBuddy source material) that still needs
the owner's input.

## Stack

- [Vite](https://vitejs.dev/) + React 18 + TypeScript
- [Tailwind CSS](https://tailwindcss.com/) for styling
- No routing library — the site is a single scrollable page with
  anchor-based sticky navigation (`src/components/Nav.tsx`) and section IDs
- Deployed to GitHub Pages via GitHub Actions

## Project structure

```
.
├── .github/workflows/deploy.yml   # Build + deploy to GitHub Pages on push to main
├── public/                        # Static assets served as-is (favicon, robots.txt, sitemap.xml, résumé)
├── src/
│   ├── content/                   # All copy lives here as typed data — see "Editing content" below
│   │   ├── metrics.ts             # Contact info, resume path, hero proof-strip metrics
│   │   ├── experience.ts          # Work case studies (SurveyMonkey, Zee, Emeritus, upGrad) + early career
│   │   ├── projects.ts            # Builds (Digsparks, Pathwiz, BrandBrain, hamara-parivar, OatBuddy placeholder)
│   │   ├── aiLab.ts                # AI Lab concept/experiment projects
│   │   ├── principles.ts          # "How I Think" principles + examples
│   │   ├── domains.ts             # "What I Build" — 5 domains on the home page
│   │   ├── education.ts           # Education + career arc labels
│   │   ├── skills.ts              # Skills, certifications, languages
│   │   ├── personal.ts            # "Beyond the Roadmap" pursuits
│   │   └── writing.ts             # Field Notes "coming soon" copy
│   ├── components/                 # One component per section, named to match (Hero, Work, Builds, AILab, …)
│   ├── App.tsx                     # Assembles all sections in order
│   ├── main.tsx
│   └── index.css                   # Tailwind entrypoint + a few base/component layer rules
├── tailwind.config.js               # Color palette (ink/paper/signal), type scale, fonts
└── vite.config.ts                   # Reads VITE_BASE_PATH for GitHub Pages subpath deploys
```

## Editing content

You should almost never need to touch a component file to change copy.
Every section reads from a typed data file in `src/content/`. For example,
to update the SurveyMonkey case study numbers, edit the `CASE_STUDIES` array
in `src/content/experience.ts` — the `Work` and `CaseStudy` components will
pick up the change automatically. To add a new AI Lab concept, add an entry
to `AI_LAB` in `src/content/aiLab.ts`.

A few fields intentionally carry sourcing/discrepancy notes (`note`,
`titleNote`, `sourcingNote`) that render inline on the page (as a hover
`[note]` marker or an expandable "Sourcing note" toggle) — keep this pattern
when you add new content that has any ambiguity, rather than silently
picking one version of a fact.

## Local development

Requires Node 20+.

```bash
npm install
npm run dev       # starts a dev server, usually at http://localhost:5173
npm run build      # type-checks and builds to dist/
npm run preview    # serves the production build locally
npm run lint        # ESLint
```

## Deploying to GitHub Pages

The site deploys automatically via `.github/workflows/deploy.yml` on every
push to `main` (or `master`). It builds with Vite and publishes `dist/`
using `actions/deploy-pages`.

**One-time setup in the GitHub repo:**
1. Go to **Settings → Pages**.
2. Under **Build and deployment → Source**, select **GitHub Actions**.
3. Push to `main`/`master` (or merge this PR) — the workflow will run and
   publish the site.

The workflow automatically resolves the correct base path for a
`https://<owner>.github.io/<repo>/` project-page URL via
`actions/configure-pages`, and passes it to Vite as `VITE_BASE_PATH` — no
manual base-path edits are needed. If you later attach a custom domain
(e.g. `srestdas.dev`) via **Settings → Pages → Custom domain**, add a
`public/CNAME` file containing that domain, and update the canonical URLs
in `index.html`, `public/sitemap.xml`, and `public/robots.txt` (currently
placeholder `https://srestdas.dev/` values — see `CONTENT_REVIEW.md` item
3.6).

## SEO / meta

Title, meta description, Open Graph, and Twitter Card tags live in
`index.html`. `public/sitemap.xml` and `public/robots.txt` are static —
update the domain in both once a real one is confirmed.

## Known gaps (see CONTENT_REVIEW.md for full detail)

- No real GitHub profile URL, resume PDF, or Field Notes articles exist yet — placeholders are wired in and clearly marked.
- OatBuddy has no source material anywhere and is shown only as a "case study pending" placeholder card, not a written project.
