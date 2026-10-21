# Content review before launch

The site was built without access to the live Synergice or Strides product catalogue
(both domains were unreachable from the build environment). Molecule science is
summarised from public prescribing information; portfolio membership is **not**
confirmed for every molecule. Please work through this list.

## 1. Portfolio: confirm every molecule (BD team)

Each molecule has a `portfolio` field in `content/molecules_*.py`:

| Status | Meaning | Molecules |
|---|---|---|
| `reported` | Strides publicly reported a US FDA approval or portfolio entry (press, 2022) | Mycophenolate mofetil, Tacrolimus, Cyclosporine, Naproxen sodium (OTC softgel), Colchicine 0.6 mg, Amantadine (softgel + tablets), Prednisone 2.5/5 mg, Potassium chloride (ER caps/tabs, powder, oral solution) |
| `agency` | Listed on the agency's Synergice draft pages | Atorvastatin, Rosuvastatin, Clopidogrel, Amlodipine, Metoprolol |
| `confirm` | Placeholder chosen to fill a therapy area; **remove or confirm** | Letrozole, Anastrozole, Capecitabine, Imatinib, Ibuprofen, Methylphenidate, TLE, TLD, Artemether/Lumefantrine, Nitrofurantoin, Dutasteride, Ergocalciferol, Progesterone |

The "Strides portfolio" row in a molecule's key facts table only appears for `reported`
molecules. Remove any molecule Strides does not want to promote; therapy areas with no
molecules left should be removed from `content/therapies.py`.

Also confirm the US approval dates attributed to Strides (colchicine Mar 2022, amantadine
softgel Feb 2022, naproxen sodium OTC softgel Aug 2022, potassium chloride oral solution
Nov 2022) and the prednisone strengths.

## 2. Medical / regulatory review

- All molecule pages: approval years, ATC codes, indications, pharmacokinetic values and
  interaction statements. These follow US labelling unless stated; adjust for the
  markets Synergice targets.
- TLD's ATC code is shown at group level (J05AR) because the 7-character code was not verified.
- Dates labelled "Today", "Recent" or "Later" in timelines are deliberately vague; replace with exact years if wanted.
- Methylphenidate is a controlled substance; confirm Strides wants it listed.

## 3. Company facts (corporate communications)

`content/pages.py` → `COMPANY_FACTS`, `ABOUT`, `CONTACT`:

- Founded 1990; HQ Bengaluru; listed NSE/BSE.
- Synergice launched Nov 2024 as the consolidated European B2B business, Strides Pharma International AG, Zug (source: Strides press release, 29 Nov 2024).
- "250+ formulations", "100+ countries", portfolio categories (from the same release).
- Regulators named (US FDA, MHRA, TGA, EU GMP, WHO). The agency copy cited "8 sites, 4 continents, 215+ ANDAs"; these were left out because public figures differ (a 2022 filing cites 259 approved ANDAs).
- Group companies the brief mentioned (OneSource, Steriscience and others) are not named on the site; add them to About if wanted.
- Office list on the contact page: add full addresses, phone and a partnering email.

## 4. Before go-live (web team)

- Replace the stand-in S mark (`S_MARK` in `build.py`, `static/img/synergice-mark.svg`) with the official Strides/Synergice logo SVGs.
- Set `SITE_URL`, `FORM_ENDPOINT` and (optionally) `CHAT_ENDPOINT`, then rebuild.
- Add a privacy notice link next to the consent checkbox.
- Submit `sitemap.xml` in Google Search Console and Bing Webmaster Tools (Bing feeds Copilot and ChatGPT search).
