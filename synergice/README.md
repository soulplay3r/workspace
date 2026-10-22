# Synergice B2B site

A simple, GEO/AEO-friendly website for **Synergice**, the B2B partnering platform of
Strides Pharma Science. It replaces the agency's dense product pages with four
things only: **Home, About us, Products (therapy area → molecule), Contact us**,
plus an on-site **RAG assistant**, **read-aloud** (text to speech) and a **Latest articles** section on the home page for answer engines.

**Before going live, read [`CONTENT_REVIEW.md`](./CONTENT_REVIEW.md).** It lists the
portfolio and company facts the Strides BD, regulatory and medical teams must confirm.

## What's in it

| Page | Purpose |
|---|---|
| `index.html` | Hero with molecule search, the clickable **therapy map** (12 therapy areas around a molecule core, Intas-style), how an enquiry works, latest articles, FAQ |
| `products.html` | The therapy map plus a filterable A–Z table of all molecules |
| `therapy/<slug>.html` | One page per therapy area: molecule cards, summaries, comparison table, FAQ |
| `molecule/<slug>.html` | One page per molecule, built to the agency's **Product Page Framework v2.0** (see below) |
| `about.html`, `contact.html` | Company facts and the enquiry form: product, full name, email, company, country (all required, per the framework), **how did you hear about us**, and a message (**what would you like to know?**) |
| `articles/*.html` | Articles listed in the home page's **Latest articles** section, newest first (there is no separate Insights tab) |
| `llms.txt`, `robots.txt`, `sitemap.xml` | Machine-readable map for AI crawlers and search engines |

### Product page (Framework v2.0)

Each molecule page follows the framework's fixed structure: header (name, drug class · dosage
form · "Manufactured by Synergice"), a 1:1 product image slot, product field cards, About (two
paragraphs), Clinical information (mechanism of action, indication), Product information
(formulation, manufacturing and quality, supply and partnership), five FAQs (Q1–Q3 generated
from product fields, Q4–Q5 fixed), related products, a legal disclaimer and the
"Request this product" form.

- Hand-written fields live in `content/framework_fields.py`; templated and fixed text in `build.py`
  (`framework_text`) and `content/pages.py` (`INFO_QUALITY`, `INFO_SUPPLY`, `FAQ_FIXED`, `DISCLAIMER`).
- `build.py` checks every field against the framework's word limits and prints any that fall outside.
- Optional fields (`strengths`, `cas_number`, `availability`, `pack_config`, `regulatory_filings`,
  `image`) hide their card when empty, as the framework specifies.
- Kept from the original brief and added to the framework: **ATC code** and **First approved** cards,
  an **Approval history** table under Clinical information, and **"How did you hear about us?"** in the form.
- Not used: the optional "Markets and registration" module, per the brief's removal of market registration.

Removed from the agency template on purpose: format & availability box, regulatory
dossier, market registration, quality & compliance, packaging & supply, partnership models.
Those details are shared with partners after an enquiry.

## Deploy a demo to Netlify

```bash
cd synergice
NETLIFY_FORMS=1 NOINDEX=1 python3 build.py
cd dist && zip -r ../synergice-b2b-site.zip . && cd ..
```

Drag the zip (or the `dist` folder) onto https://app.netlify.com/drop. `NETLIFY_FORMS=1` sends
enquiries to Netlify Forms (enable form detection under Site configuration › Forms, then
redeploy once); `NOINDEX=1` keeps the demo out of search engines and AI crawlers. Leave
`NOINDEX` unset for the real launch so the GEO/AEO set-up can work.

## GEO / AEO features

- **Answer-first:** every page opens with an "In brief" block that answers the page's main question in 2–3 sentences.
- **Fact tables:** key facts, approval history and pharmacokinetics as real HTML tables.
- **FAQ on every page**, mirrored in `FAQPage` JSON-LD.
- **Structured data:** `Organization`, `WebSite`, `MedicalWebPage` + `Drug` (ATC code, class, mechanism, route), `CollectionPage`/`ItemList`, `Article`, `BreadcrumbList`.
- **Length:** molecule, about and article pages fall in the 600–1,200 word range; the build prints a word count per page and flags pages outside it.
- **Crawlable:** static HTML, no client-side rendering; `robots.txt` explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended and others; `llms.txt` lists every page.
- **Attribution:** "How did you hear about us?" includes *AI assistant*, so the team can measure answer-engine referrals.

## Build

Python 3.12+ only, no packages:

```bash
cd synergice
python3 build.py                     # writes dist/
npx http-server dist -p 8080         # preview locally
```

Content lives in `content/` as plain Python data (`therapies.py`, `molecules_a/b/c.py`,
`pages.py`). Add a molecule by appending a dict with the same fields; the therapy page,
products table, sitemap, `llms.txt` and assistant index update automatically.

Build-time settings (environment variables):

| Variable | Default | Use |
|---|---|---|
| `SITE_URL` | `https://www.synergice.com` | Canonical URLs, sitemap, JSON-LD |
| `FORM_ENDPOINT` | *(empty)* | URL that receives enquiry JSON (CRM webhook, HubSpot, Formspree…). Empty = preview mode: forms validate but say nothing was sent. |
| `CHAT_ENDPOINT` | *(empty)* | URL of `api/chat.mjs`. Empty = the assistant answers from retrieval alone. |
| `NETLIFY_FORMS` | *(unset)* | `1` = forms post to Netlify Forms instead of `FORM_ENDPOINT` |
| `NOINDEX` | *(unset)* | `1` = demo build: `noindex` on every page and a `robots.txt` that blocks all crawlers |
| `PRIVACY_POLICY_URL` | *(empty)* | Privacy policy linked from the consent checkbox. Empty = a placeholder `privacy.html` (noindex). |

## Language menu

The top bar has a language menu (English, French, Spanish, German, Portuguese, Arabic, Swahili,
Hausa, Yoruba, Igbo, Zulu, Amharic, Hindi). It uses Google's website translator: the choice is
saved in the standard `googtrans` cookie and the page reloads translated; English removes it.
Brand and product names are marked `notranslate`. Edit `LANGUAGES` in `build.py` to change the list.
Translation needs the site to be served from a normal web host (it does not run inside the Claude preview).

## Product list download

`product_list_block()` shows "Download the Product List" with a QR code
(`static/img/product-list-qr.svg`) that points to the same PDF as synergice.co
(`PRODUCT_LIST_URL` in `build.py`). It appears on the home, products and molecule pages and in the footer.

## Read aloud (text to speech)

Molecule and article pages have a **Listen to this page** button (Pause / Resume / Stop) that
reads the title, then each section, highlighting the paragraph being read. The assistant has a
**Listen** button on every answer and a **Read aloud** switch that speaks new answers
automatically. Both use the browser's built-in speech synthesis (`window.speechSynthesis`):
no service, no API key, no cost. Voices depend on the visitor's device; the code prefers
British, then Indian, then US English. Browsers without speech synthesis don't show the buttons.

## The assistant (RAG bot)

`static/js/chat.js` loads `assets/search-index.json` (one chunk per page section) and
ranks chunks with BM25, boosting the molecule named in the question and the section it
asks about (mechanism, approval, uses, pharmacokinetics). With no backend it replies with
the best-matching sentences and links to its sources. It routes price, MOQ, supply and
registration questions to the enquiry form and declines personal medical advice.

To have Claude write the answers, deploy `api/chat.mjs` as a serverless function
(Vercel / Netlify Functions v2 / Cloudflare Workers), set `ANTHROPIC_API_KEY` (and
optionally `ALLOWED_ORIGIN`), and rebuild with `CHAT_ENDPOINT`. The browser still does
retrieval and sends only the top passages; the function tells the model to answer only
from them. If the endpoint fails, the widget falls back to retrieval-only answers.
The function uses server-side refusal fallbacks (`fallbacks: "default"`) so a declined
request is retried on a fallback model instead of failing.

## Brand

Colours and type follow the Strides brand guideline: Charcoal `#383536`, Green Bright
`#00955e`, Green Medium `#00724a`, Green Dark `#00402c`; Zilla Slab with Rockwell as the
fallback. Buttons and links use Green Medium because white text on Green Bright does not
meet WCAG AA contrast. The S mark in `build.py` / `static/img` is a hand-drawn stand-in;
replace it with the official logo files.
