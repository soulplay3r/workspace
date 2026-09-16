# Content Review — Srest Das personal site

This document tracks everything that needs owner confirmation before this
site is considered final. It was generated while building V1 from Srest
Das's resume PDF, LinkedIn profile PDF, and (for BrandBrain only) the
`dixshadas/brandbrain` repository. Nothing outside those sources was used —
where the sources disagreed or were silent, that's flagged below rather than
guessed.

## 0. Top priority — action needed before publishing

### #1. OatBuddy has zero source material
**OatBuddy does not appear anywhere in the resume, the LinkedIn PDF, or the
BrandBrain repo.** There is currently no sourced information about it —
no dates, no description of what was built, no outcomes.

To avoid inventing details (formulation, packaging, FSSAI approval, retail
distribution, etc. — none of which are sourced), OatBuddy is **omitted from
the live Builds section** in this V1 and instead shown only as a clearly
labeled placeholder card: *"Case study pending — awaiting source material."*

**Ask for the owner:** please supply what OatBuddy actually was — timeframe,
what you built or did, what happened — so a real case study can be written
in the same Problem → Insight → What I Built → What I Learned → What
Happened Next format as the other Builds entries.

## 1. Resume vs. LinkedIn discrepancies

| # | Topic | LinkedIn says | Resume says | How it's rendered on the site |
|---|---|---|---|---|
| 1 | SurveyMonkey title | "Senior AI Product Manager" | "Senior Product Manager" | Neutral: "Senior Product Manager, AI & Marketplace," with the AI scope covered in the narrative. Both versions footnoted in the case study `[note]`. |
| 2 | SurveyMonkey revenue contribution | States "11%" | Left as an unfilled "xx%" placeholder | Shown softly in the case study body, sourced to LinkedIn, explicitly marked unverified. **Not** used in the hero proof strip. |
| 3 | Mind Wars downloads | "2mn+ downloads (& registrations in Zee5)" | "0 → 2.5M+ downloads" | Resume's 2.5M+ used as primary (more precise), LinkedIn's 2mn+ shown as a footnote in the same metric card. |
| 4 | Mind Wars YouTube audience | "100k+" | "1M+ organic audience" | Both shown side by side in the metric card; not reconciled. |
| 5 | Mind Wars social reach (other platforms) | "FB & Instagram 300k+ combined" | "200k+ (other platforms)" | Both shown as a range, sourced separately. |
| 6 | "0→50M+ Users, 2x" (LinkedIn headline tagline) | Appears in the LinkedIn headline | Not present on resume; no supporting calculation found anywhere | **Not used as a hard metric anywhere on the site**, including the hero proof strip. Flagged here as unverified — needs owner confirmation before use. |
| 7 | Self-employed / consultant period | Framed as a formal ~6-month engagement, May–Oct 2024 | Same work (Digsparks, Pathwiz, hamara-parivar) listed under "Projects & Extracurriculars," no explicit employment dates | Site frames these as Builds with the LinkedIn date range noted, not as a formal role in the Work timeline. |
| 8 | L&T title | "Marketing Manager," start ~Jun 2016 | "Assistant Manager," start ~May 2016 | Rendered neutrally as "Marketing Manager" with a `[note]` flagging both the title and start-month discrepancy. |
| 9 | Kellogg / Northwestern program name | "Executive Program in Organizational Leadership" | "AI Strategies - Northwestern University" | Combined into one line: "Executive Program, Organizational Leadership & AI Strategies," with a `[note]` explaining the discrepancy. |
| 10 | Certifications | Google AdWords, Python Data Structures, CSPO, Generative AI | Same four, plus AWS Cloud Practitioner and SwaggerHub API Product Owner | AWS and SwaggerHub shown with a "resume-only, not present on LinkedIn" note — not treated as a conflict, just unconfirmed elsewhere. |
| 11 | Zee Gen AI assistant accuracy | States it "achieved a higher than industry benchmark of accuracy, precision score" | Not mentioned | No specific number exists anywhere in either source. Stated qualitatively on the site — no number invented. |

## 2. Claims shown but explicitly marked unverified on-page

- **SurveyMonkey "~11% of company revenue"** — LinkedIn-only, resume left blank. Shown in the case study metrics grid with an inline note, not in the hero proof strip.
- **"0→50M+ Users, 2x"** — no supporting calculation found in either source; excluded entirely from metric tiles per the build brief. If this number is real and the owner can confirm the basis for it, it can be added back as a sourced proof point.
- **Mind Wars YouTube / social numbers** — both source figures shown side by side rather than picking one, since they don't reconcile cleanly.

## 3. Missing information (placeholders in the codebase)

All of the below are marked in code with a comment and, where relevant, a `note`/`Note` string that renders on the page itself so nobody mistakes them for real content:

1. **GitHub profile URL** — no GitHub username or profile URL exists in the resume or LinkedIn PDF. The site currently links to `https://github.com/soulplay3r` (the repo owner used for this build) as a placeholder — see `src/content/metrics.ts` (`CONTACT.github`, `githubIsPlaceholder: true`). **Owner: please confirm your actual GitHub profile URL, or say to remove the "View GitHub" CTA if you don't want it linked.**
2. **Resume PDF file** — no resume file was supplied. `src/content/metrics.ts` (`RESUME_PATH`) currently points at `/public/resume-placeholder.md`, a text stand-in. **Drop a real `resume.pdf` into `/public` and update `RESUME_PATH` to `/resume.pdf`.**
3. **Real screenshots for BrandBrain / OatBuddy** — the Builds section currently has no product screenshots (by design, to avoid mocking up something that doesn't exist). If you want visuals for BrandBrain, a screenshot of `demo.brainlee.tech` would be the most honest source.
4. **Field Notes articles** — none exist yet. The Field Notes section is shown honestly as "coming soon" rather than populated with placeholder posts.
5. **Digsparks / Pathwiz current status** — no roadmap or "what's next" information exists in the source material for either project. Their Build cards say so explicitly rather than guessing.
6. **Canonical domain** — `index.html`, `sitemap.xml`, and `robots.txt` currently reference `https://srestdas.dev/` as a placeholder canonical domain. Update this once the real custom domain (or the GitHub Pages URL) is decided — see README.md.

## 4. Assumptions made in the absence of data

- Treated the LinkedIn summary and the resume summary as complementary rather than conflicting — used the LinkedIn summary for hero/about tone, and the resume summary's phrasing ("intelligent, data-driven systems," "human-in-the-loop ML") for the About section dek.
- For Mind Wars, used the **resume's** numbers as the primary headline figures (they're more precise/itemized) and footnoted LinkedIn's looser figures, per the build brief's own recommendation.
- Assumed the "career's second unicorn" line (Emeritus) and "soonicorn to unicorn" line (upGrad) are LinkedIn's characterizations of the companies' trajectories, not personal outcomes Srest is claiming credit for — used as background color only, worded to make that distinction ("cited here as market context, not as a personal outcome").
- Assumed hamara-parivar.com and the earlier-career strip (L&T/Cummins/Ingersoll Rand) warrant compact treatment rather than full case studies, per the brief.
- Used "Bengaluru, Karnataka, India" as the single location shown on the site (current role location), rather than listing every past city.

## 5. Recommended future content

- A written case study for OatBuddy once source material is supplied (see #1 above) — likely the single highest-impact addition, since founder/builder stories test well with both recruiters and CPOs.
- 2–3 Field Notes essays on marketplace trust economics, the SurveyMonkey precision/recall tradeoff, or the Mind Wars 0-to-1 build — the site's principles section already outlines the raw material for these.
- Real product screenshots or short screen-recordings for BrandBrain (from `demo.brainlee.tech`) once the owner is comfortable sharing them publicly.
- A confirmed, numeric version of the SurveyMonkey revenue-contribution figure and the "0→50M+ users, 2x" headline claim, if they can be substantiated — both would strengthen the proof strip meaningfully once verified.
- Confirm whether Digsparks and Pathwiz are still active; if so, add a current-status line to each Build card.

## 6. Where these notes live in the code

Every discrepancy and placeholder above has a matching comment (and, in most
cases, a `note`/`titleNote`/`sourcingNote` field that surfaces in the UI —
click "Source & context," "Sourcing note," or hover the `[note]` markers
throughout the site) in:

- `src/content/metrics.ts`
- `src/content/experience.ts`
- `src/content/projects.ts`
- `src/content/education.ts`
- `src/content/skills.ts`

so future edits to this content stay honest by construction rather than
relying on this document alone.
