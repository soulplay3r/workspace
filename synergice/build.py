#!/usr/bin/env python3
"""Static site generator for the Synergice B2B molecule site.

    python3 build.py                 # writes ./dist
    SITE_URL=https://www.synergice.com \
    FORM_ENDPOINT=https://... CHAT_ENDPOINT=https://.../api/chat python3 build.py

No dependencies beyond the Python 3.12+ standard library. Every page is plain,
crawlable HTML with JSON-LD; JavaScript only enhances (search, chat, forms).
"""

import json
import os
import re
import shutil
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "content"))

from therapies import THERAPIES  # noqa: E402
from molecules_a import MOLECULES_A  # noqa: E402
from molecules_b import MOLECULES_B  # noqa: E402
from molecules_c import MOLECULES_C  # noqa: E402
from framework_fields import FIELDS  # noqa: E402
from pages import (ABOUT, ARTICLES, COMPANY_FACTS, CONTACT, COUNTRIES, DISCLAIMER,  # noqa: E402
                   FAQ_FIXED, HEAR_ABOUT, HOME, INFO_QUALITY, INFO_SUPPLY, RESPONSE_PROMISE)

SITE = {
    "name": "Synergice",
    "url": os.environ.get("SITE_URL", "https://www.synergice.com").rstrip("/"),
    "parent": "Strides Pharma Science Limited",
    "parent_url": "https://www.strides.com",
    "form_endpoint": os.environ.get("FORM_ENDPOINT", ""),
    "chat_endpoint": os.environ.get("CHAT_ENDPOINT", ""),
    "privacy_url": os.environ.get("PRIVACY_POLICY_URL", ""),  # empty = placeholder privacy.html
    "updated": "2026-10-21",
    "updated_label": "21 October 2026",
}

DIST = ROOT / "dist"
MOLECULES = sorted(MOLECULES_A + MOLECULES_B + MOLECULES_C, key=lambda m: m["name"].lower())
for _m in MOLECULES:
    _m.update(FIELDS[_m["slug"]])
MOL = {m["slug"]: m for m in MOLECULES}
THER = {t["slug"]: t for t in THERAPIES}
for t in THERAPIES:
    t["molecules"] = [m for m in MOLECULES if m["therapy"] == t["slug"]]

e = escape


# --------------------------------------------------------------- URL helpers
def mol_path(m):
    return f"molecule/{m['slug']}.html"


def ther_path(t):
    return f"therapy/{t['slug']}.html"


def art_path(a):
    return f"insights/{a['slug']}.html"


def canonical(path):
    return SITE["url"] + "/" + ("" if path == "index.html" else path)


def lower_first(s):
    return s[0].lower() + s[1:] if s and not s[:2].isupper() else s


# -------------------------------------------------------------------- icons
ICONS = {
    "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/><path d="M5 12h3l1.5-3 2.5 6 1.5-3H19"/>',
    "ribbon": '<path d="M12 3a3.5 3.5 0 0 0-3.5 3.5c0 2.6 2 5.4 3.5 7.5 1.5-2.1 3.5-4.9 3.5-7.5A3.5 3.5 0 0 0 12 3z"/><path d="M10 16.5 6.5 21M14 16.5l3.5 4.5M12 14l-3.5 4.5M12 14l3.5 4.5"/>',
    "shield": '<path d="M12 3 5 6v5c0 4.5 3 8.3 7 10 4-1.7 7-5.5 7-10V6l-7-3z"/><path d="m9 12 2 2 4-4"/>',
    "bolt": '<circle cx="12" cy="12" r="9"/><path d="m13 6-4 7h4l-2 5 5-7h-4l1-5z"/>',
    "neuron": '<circle cx="12" cy="12" r="3"/><path d="M12 9V4M9.4 13.5 5 16M14.6 13.5 19 16M12 4l-2-1M12 4l2-1M5 16l-1 2M19 16l1 2M15 12h4"/>',
    "virus": '<circle cx="12" cy="12" r="5"/><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.9 2.9M15.5 15.5l2.9 2.9M5.6 18.4l2.9-2.9M15.5 8.5l2.9-2.9"/><circle cx="12" cy="12" r="1.2"/>',
    "mosquito": '<path d="M12 7v11"/><circle cx="12" cy="6" r="1.5"/><path d="M12 10c-3-3-6-3-7.5-1.5S6 13 12 12M12 10c3-3 6-3 7.5-1.5S18 13 12 12"/><path d="M12 14l-4 4M12 14l4 4M12 16l-3 5M12 16l3 5"/>',
    "capsule": '<rect x="3" y="8.5" width="18" height="7" rx="3.5" transform="rotate(-35 12 12)"/><path d="m9.2 8 5.6 8"/>',
    "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/><path d="M9.5 15a2.5 2.5 0 0 0 2.5 2.5"/>',
    "hexagon": '<path d="m12 3 7.5 4.5v9L12 21l-7.5-4.5v-9L12 3z"/><path d="m12 8 3.5 2v4L12 16l-3.5-2v-4L12 8z"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9 7 7M17 17l2.1 2.1M4.9 19.1 7 17M17 7l2.1-2.1"/>',
    "venus": '<circle cx="12" cy="9" r="5"/><path d="M12 14v7M9 18h6"/>',
}


def icon(name, cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            f'{ICONS[name]}</svg>')


# Faceted S mark, a stand-in drawn from the Strides logo; replace with the
# official SVG from the brand team before launch (see CONTENT_REVIEW.md).
S_MARK = ('<svg class="smark" viewBox="0 0 60 80" aria-hidden="true"><path d="M47 15 39 7H19L9 17v9l10 10 22 8 10 10v9L41 74H21l-8-8" '
          'fill="none" stroke="currentColor" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>')


# -------------------------------------------------------------- page shell
def org_ld():
    return {
        "@type": "Organization",
        "@id": SITE["url"] + "/#org",
        "name": "Synergice",
        "url": SITE["url"] + "/",
        "logo": SITE["url"] + "/assets/img/synergice-mark.svg",
        "description": "The B2B partnering platform of Strides Pharma Science Limited.",
        "parentOrganization": {"@type": "Organization", "name": SITE["parent"], "url": SITE["parent_url"]},
    }


def website_ld():
    return {"@type": "WebSite", "@id": SITE["url"] + "/#website", "url": SITE["url"] + "/",
            "name": "Synergice", "publisher": {"@id": SITE["url"] + "/#org"}}


def crumbs_ld(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": name, "item": canonical(path)}
        for i, (name, path) in enumerate(crumbs)]}


def faq_ld(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


NAV = [("Home", "index.html"), ("About us", "about.html"), ("Products", "products.html"),
       ("Insights", "insights.html"), ("Contact us", "contact.html")]


def shell(path, title, description, body, graph, active=None):
    r = "../" * path.count("/")
    nav = "".join(
        f'<a href="{r}{href}"{" aria-current=page" if href == active else ""}>{label}</a>'
        for label, href in NAV)
    ld = json.dumps({"@context": "https://schema.org", "@graph": [org_ld(), website_ld()] + graph},
                    ensure_ascii=False, separators=(",", ":"))
    chat_attr = f' data-endpoint="{e(SITE["chat_endpoint"])}"' if SITE["chat_endpoint"] else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{canonical(path)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Synergice">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{canonical(path)}">
<meta name="robots" content="index, follow, max-snippet:-1">
<link rel="icon" href="{r}assets/img/synergice-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{r}assets/css/site.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="{r}index.html" aria-label="Synergice home">{S_MARK}<span class="brand-text"><span class="brand-name">Synergice<sup>®</sup></span><span class="brand-sub">by Strides</span></span></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <a class="btn btn-small nav-cta" href="{r}contact.html">Send an enquiry</a>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <p class="foot-name">{S_MARK}<span>Synergice<sup>®</sup></span></p>
      <p>The B2B partnering platform of Strides Pharma Science Limited. Molecule information and partnering enquiries for licensing partners, marketing authorisation holders and distributors.</p>
    </div>
    <div>
      <p class="foot-h">Products</p>
      <ul>{"".join(f'<li><a href="{r}{ther_path(t)}">{e(t["name"])}</a></li>' for t in THERAPIES[:6])}<li><a href="{r}products.html">All therapy areas</a></li></ul>
    </div>
    <div>
      <p class="foot-h">Company</p>
      <ul><li><a href="{r}about.html">About us</a></li><li><a href="{r}insights.html">Insights</a></li><li><a href="{r}contact.html">Contact us</a></li><li><a href="{r}llms.txt">llms.txt</a></li></ul>
    </div>
  </div>
  <div class="wrap foot-legal">
    <p>This site is intended for pharmaceutical business partners and is not directed at patients or the general public. Molecule pages summarise public prescribing information and are not medical advice. Brand names are trademarks of their respective owners and are cited for reference only.</p>
    <p>© 2026 Synergice, a Strides Pharma Science company. Last updated {SITE["updated_label"]}.</p>
  </div>
</footer>
<script src="{r}assets/js/site.js" defer></script>
<script src="{r}assets/js/chat.js" data-root="{r}"{chat_attr} defer></script>
</body>
</html>
"""


def crumbs_html(path, crumbs):
    r = "../" * path.count("/")
    parts = []
    for i, (name, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            parts.append(f'<span aria-current="page">{e(name)}</span>')
        else:
            parts.append(f'<a href="{r}{p}">{e(name)}</a>')
    return f'<nav class="crumbs" aria-label="Breadcrumb">{" <span aria-hidden=true>›</span> ".join(parts)}</nav>'


def faq_html(faqs, heading="Frequently asked questions"):
    items = "".join(f"<details><summary><h3>{e(q)}</h3></summary><p>{e(a)}</p></details>" for q, a in faqs)
    return f'<section class="block" id="faq"><h2>{heading}</h2><div class="faq">{items}</div></section>'


def kv_table(rows, cls="facts"):
    return (f'<div class="table-wrap"><table class="{cls}"><tbody>'
            + "".join(f'<tr><th scope="row">{e(k)}</th><td>{v}</td></tr>' for k, v in rows)
            + "</tbody></table></div>")


def timeline_table(rows):
    return ('<div class="table-wrap"><table class="timeline"><thead><tr><th scope="col">Year</th>'
            '<th scope="col">Milestone</th></tr></thead><tbody>'
            + "".join(f'<tr><td class="yr">{e(y)}</td><td>{e(t)}</td></tr>' for y, t in rows)
            + "</tbody></table></div>")


def paras(ps):
    return "".join(f"<p>{e(p)}</p>" for p in ps)


def enquiry_form(path, molecule=None, heading="Request this product", intro=None):
    r = "../" * path.count("/")
    uid = molecule["slug"] if molecule else "general"
    req = '<span class="req" aria-hidden="true">*</span>'
    if molecule:
        product = (f'<div class="field"><p class="label">Product enquired about</p><p class="product-locked">{e(molecule["name"])}</p>'
                   f'<input type="hidden" name="product" value="{e(molecule["name"])}"></div>')
    else:
        opts = '<option value="">Select a product (optional)</option>' + "".join(
            f"<option>{e(m['name'])}</option>" for m in MOLECULES) + "<option>A product not listed here</option>"
        product = f'<div class="field"><label for="{uid}-product">Product enquired about</label><select id="{uid}-product" name="product">{opts}</select></div>'
    countries = '<option value="">Select your country</option>' + "".join(f"<option>{e(c)}</option>" for c in COUNTRIES)
    hear = '<option value="">Select one</option>' + "".join(f"<option>{e(h)}</option>" for h in HEAR_ABOUT)
    endpoint = f' data-endpoint="{e(SITE["form_endpoint"])}"' if SITE["form_endpoint"] else ""
    privacy = SITE["privacy_url"] or f"{r}privacy.html"
    intro_html = f'<p class="form-intro">{e(intro)}</p>' if intro else ""
    return f"""<form class="enquiry" id="enquiry-{uid}" novalidate{endpoint}>
  <h2 class="form-h">{e(heading)}</h2>{intro_html}
  {product}
  <div class="grid2">
    <div class="field"><label for="{uid}-name">Full name {req}</label><input id="{uid}-name" name="name" autocomplete="name" required></div>
    <div class="field"><label for="{uid}-email">Email ID {req}</label><input id="{uid}-email" name="email" type="email" autocomplete="email" required></div>
    <div class="field"><label for="{uid}-company">Company name {req}</label><input id="{uid}-company" name="company" autocomplete="organization" required></div>
    <div class="field"><label for="{uid}-country">Country {req}</label><select id="{uid}-country" name="country" autocomplete="country-name" required>{countries}</select></div>
  </div>
  <div class="field"><label for="{uid}-hear">How did you hear about us? {req}</label><select id="{uid}-hear" name="heard_about" required>{hear}</select></div>
  <div class="field"><label for="{uid}-message">Message: what would you like to know?</label><textarea id="{uid}-message" name="message" rows="4" placeholder="For example: strengths and pack sizes for Kenya, registration position, quotation"></textarea></div>
  <div class="field check"><input id="{uid}-consent" name="consent" type="checkbox" required><label for="{uid}-consent">I agree that Synergice may use these details to respond to my enquiry, in line with the <a href="{e(privacy)}">privacy policy</a>. {req}</label></div>
  <input type="hidden" name="page" value="{e(path)}">
  <button class="btn" type="submit">Submit enquiry</button>
  <p class="form-note">{e(RESPONSE_PROMISE)}</p>
  <p class="form-status" role="status" aria-live="polite"></p>
</form>"""


def mol_card(m, r):
    t = THER[m["therapy"]]
    return (f'<a class="mol-card" href="{r}{mol_path(m)}"><span class="mol-card-t">{e(t["name"])}</span>'
            f'<span class="mol-card-n">{e(m["name"])}</span><span class="mol-card-c">{e(m["klass"])}</span>'
            f'<span class="mol-card-f">First approved {e(m["first_approval"].split(",")[0])}</span></a>')


def therapy_tiles(r):
    return '<div class="tiles">' + "".join(
        f'<a class="tile" href="{r}{ther_path(t)}"><span class="tile-ico">{icon(t["icon"])}</span>'
        f'<span class="tile-name">{e(t["name"])}</span>'
        f'<span class="tile-count">{len(t["molecules"])} molecule{"s" if len(t["molecules"]) != 1 else ""} <span aria-hidden="true">→</span></span></a>'
        for t in THERAPIES) + "</div>"


# ------------------------------------------------------------------- pages
def article_for(phrase):
    return "an" if phrase[:1].lower() in "aeiou" or phrase.startswith("HMG") else "a"


def first_sentence(text):
    return re.split(r"(?<=[.!?])\s+", text, maxsplit=1)[0]


def framework_text(m):
    """Templated framework fields, built from the product fields."""
    name, lname = m["name"], lower_first(m["name"])
    form = lower_first(m["form"])
    st = m.get("strengths")
    pack = m.get("pack_config")
    confirmed = m["portfolio"] != "confirm"
    if confirmed:
        manufacture = (f"Synergice manufactures {lname} as {form}" + (f", in strengths of {st}" if st else "") + ". "
                       "Production takes place within the Strides Pharma Science manufacturing network under Good "
                       "Manufacturing Practice, and every batch is released against its approved specification. The product "
                       "is supplied to marketing authorisation holders, distributors and licensing partners; the forms, "
                       "strengths and packs available for each market are confirmed on enquiry.")
        q1 = (f"Yes. Synergice manufactures {lname} as {form}" + (f", in {st}." if st else ". Available strengths are confirmed on enquiry."))
        q3 = (f"{name} is available as {form}" + (f", in {st}." if st else ".") +
              (f" Pack configuration: {pack}." if pack else " Strengths and pack configurations for your market are confirmed on enquiry."))
    else:
        manufacture = (f"{name} is listed on Synergice for partnering enquiries. Where Synergice supplies it, production "
                       "takes place within the Strides Pharma Science manufacturing network under Good Manufacturing "
                       "Practice, with every batch tested and released against its approved specification. Current manufacture, "
                       "dosage forms, strengths and pack configurations for your market are confirmed on enquiry.")
        q1 = (f"{name} is listed for partnering enquiries. Contact our business development team through the form on "
              "this page to confirm current manufacture, dosage forms and strengths for your market.")
        q3 = (f"Dosage forms and strengths of {lname} for your market are confirmed on enquiry. "
              f"The reference product is presented as {form}.")
    formulation = (f"{name} is presented as {form}" + (f", in strengths of {st}" if st else "") + ". " +
                   (f"Pack configuration: {pack}. " if pack else
                    "Pack configurations, such as blister and bottle presentations, are set per market and confirmed on enquiry. ") +
                   "Artwork, labelling and language variants are developed for the destination market. Full composition, "
                   "including excipients, is shared under confidentiality during technical evaluation.")
    kl = lower_first(m["klass"])
    q2 = f"{name} is classified as {article_for(kl)} {kl}. {first_sentence(m['overview_molecule'])}"
    faqs = [(f"Does Synergice manufacture {lname}?", q1),
            (f"What drug class is {lname}?", q2),
            ("What strengths and dosage forms are available?", q3)] + FAQ_FIXED
    return {"manufacture": manufacture, "formulation": formulation, "faqs": faqs}


def spec_cards(m, r):
    t = THER[m["therapy"]]
    atc = m["atc"].split(" ")[0]
    cards = [
        ("Therapeutic category", f'<a href="{r}{ther_path(t)}">{e(t["name"])}</a>'),
        ("Dosage form", e(m["form"])),
        ("Strength", e(m.get("strengths") or "")),
        ("CAS number", e(m.get("cas_number") or "")),
        ("Availability status", e(m.get("availability") or "")),
        ("Pack configuration", e(m.get("pack_config") or "")),
        ("Regulatory filings available", "".join(f'<span class="tag">{e(x)}</span>' for x in m.get("regulatory_filings") or [])),
        ("ATC code", f'<a href="https://atcddd.fhi.no/atc_ddd_index/?code={e(atc)}" rel="noopener">{e(m["atc"])}</a>'),
        ("First approved", e(m["first_approval"])),
    ]
    # Framework rule: an empty field hides its row.
    return "".join(f'<div class="spec"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in cards if v)


def build_molecule(m):
    path = mol_path(m)
    r = "../"
    t = THER[m["therapy"]]
    fw = framework_text(m)
    name, lname = m["name"], lower_first(m["name"])
    confirmed = m["portfolio"] != "confirm"
    crumbs = [("Home", "index.html"), ("Products", "products.html"), (t["name"], ther_path(t)), (name, path)]
    alt = m.get("image_alt") or f"{name} {lower_first(m['form'])}"
    if m.get("image"):
        image = f'<img class="prod-img" src="{r}{e(m["image"])}" alt="{e(alt)}" width="800" height="800">'
    else:
        image = (f'<div class="prod-img prod-img-ph" role="img" aria-label="{e(alt)}">{S_MARK}'
                 f'<span class="ph-name">{e(name)}</span><span class="ph-form">{e(m["form"])}</span></div>')
    sub = f'{e(m["klass"])} · {e(m["form"])}' + (" · Manufactured by Synergice" if confirmed else "")
    related = [MOL[s2] for s2 in m["related"][:3] if s2 in MOL]
    toc = [("about", f"About {name}"), ("clinical", "Clinical information"), ("product", "Product information"),
           ("faq", "FAQs"), ("enquire", "Request this product")]
    dq = e(f"How does {lname} work?")
    body = f"""
<div class="wrap">
{crumbs_html(path, crumbs)}
<header class="page-head mol-head">
  <h1>{e(name)}</h1>
  <p class="sub">{sub}</p>
</header>
<section class="prod-top" aria-label="Product details">
  {image}
  <dl class="spec-grid">{spec_cards(m, r)}</dl>
</section>
<div class="mol-layout">
<article class="prose">
  <section class="block" id="about"><h2>About {e(name)}</h2><p>{e(m["overview_molecule"])}</p><p>{e(fw["manufacture"])}</p></section>
  <section class="block" id="clinical"><h2>Clinical information</h2>
    <h3 id="moa">Mechanism of action</h3><p>{e(m["moa_short"])}</p>
    <h3 id="indication">Indication</h3><p>{e(m["indication"])}</p>
    <h3 id="history">Approval history</h3>{timeline_table(m["timeline"])}
    <p class="meta">Sources: <a href="https://dailymed.nlm.nih.gov/dailymed/search.cfm?query={e(m["slug"].split("-")[0])}" rel="noopener">US prescribing information (DailyMed)</a> · <a href="https://www.ema.europa.eu/en/search?search_api_fulltext={e(m["slug"].split("-")[0])}" rel="noopener">European Medicines Agency</a></p>
  </section>
  <section class="block" id="product"><h2>Product information</h2>
    <h3 id="formulation">Formulation and presentation</h3><p>{e(fw["formulation"])}</p>
    <h3 id="quality">Manufacturing and quality</h3><p>{e(INFO_QUALITY)}</p>
    <h3 id="supply">Supply and partnership</h3><p>{e(INFO_SUPPLY)}</p>
  </section>
  {faq_html(fw["faqs"])}
</article>
<aside class="side">
  <nav class="toc" aria-label="On this page"><p class="toc-h">On this page</p>{"".join(f'<a href="#{i}">{e(l)}</a>' for i, l in toc)}</nav>
  <div class="side-card"><p class="side-h">Request this product</p><p>Send an enquiry to our business development team. {e(RESPONSE_PROMISE)}</p><a class="btn btn-block" href="#enquire">Submit an enquiry</a><button class="btn btn-ghost btn-block" type="button" data-chat-open data-q="{dq}">Ask the assistant</button></div>
</aside>
</div>
<section class="block"><h2>Related products</h2><div class="mol-grid">{"".join(mol_card(x, r) for x in related)}</div><p class="more"><a href="{r}{ther_path(t)}">All {e(t["name"].lower())} products →</a></p></section>
<section class="disclaimer" aria-label="Disclaimer"><p class="disclaimer-h">Disclaimer</p><p>{e(DISCLAIMER)}</p><p>Last updated {SITE["updated_label"]}.</p></section>
</div>
<section class="band band-mint" id="enquire"><div class="wrap narrow">{enquiry_form(path, m, "Request this product", "Send an enquiry to our business development team.")}</div></section>
"""
    graph = [
        {"@type": "MedicalWebPage", "@id": canonical(path) + "#webpage", "url": canonical(path),
         "name": f"{name}: drug class, mechanism of action and supply",
         "description": m["overview_molecule"], "lastReviewed": SITE["updated"], "dateModified": SITE["updated"],
         "inLanguage": "en", "isPartOf": {"@id": SITE["url"] + "/#website"},
         "about": {"@id": canonical(path) + "#drug"}, "publisher": {"@id": SITE["url"] + "/#org"},
         "audience": {"@type": "Audience", "audienceType": "Pharmaceutical business partners"}},
        {"@type": "Drug", "@id": canonical(path) + "#drug", "name": name, "nonProprietaryName": name,
         "alternateName": m["aka"][:4], "description": m["overview_molecule"],
         "drugClass": {"@type": "DrugClass", "name": m["klass"]},
         "mechanismOfAction": m["moa_short"], "administrationRoute": m["route"], "dosageForm": m["form"],
         "code": {"@type": "MedicalCode", "code": m["atc"].split(" ")[0], "codingSystem": "ATC"},
         "url": canonical(path)},
        faq_ld(fw["faqs"]), crumbs_ld(crumbs)]
    title = f"{name}: drug class, mechanism of action and supply | Synergice"
    ov = m["overview_molecule"]
    desc = ov[:155].rsplit(" ", 1)[0] + "…" if len(ov) > 158 else ov
    return path, shell(path, title, desc, body, graph, "products.html")


def build_privacy():
    path = "privacy.html"
    body = f"""
<div class="wrap prose">
{crumbs_html(path, [("Home", "index.html"), ("Privacy policy", path)])}
<header class="page-head"><h1>Privacy policy</h1></header>
<p>This page is a placeholder. The privacy policy for enquiries submitted through this site is supplied by Strides Pharma Science legal. Set PRIVACY_POLICY_URL when building the site to link the enquiry forms to the published policy instead.</p>
</div>
"""
    html = shell(path, "Privacy policy | Synergice", "Privacy policy for enquiries submitted to Synergice.", body, [], None)
    return path, html.replace('content="index, follow, max-snippet:-1"', 'content="noindex"')


def build_therapy(t):
    path = ther_path(t)
    r = "../"
    crumbs = [("Home", "index.html"), ("Products", "products.html"), (t["name"], path)]
    mols = t["molecules"]
    names = ", ".join(m["name"] for m in mols)
    rows = "".join(
        f'<tr><td><a href="{r}{mol_path(m)}">{e(m["name"])}</a></td><td>{e(m["klass"])}</td><td>{e(m["first_approval"])}</td><td>{e(m["atc"].split(" ")[0])}</td></tr>'
        for m in mols)
    faqs = t["faqs"]
    body = f"""
<div class="wrap">
{crumbs_html(path, crumbs)}
<header class="page-head ther-head">
  <span class="tile-ico big">{icon(t["icon"])}</span>
  <div><p class="eyebrow">Therapy area</p><h1>{e(t["name"])}</h1><p class="sub">{e(t["tagline"])}</p></div>
</header>
<section class="answer"><p class="answer-label">In brief</p><p>Synergice lists {len(mols)} {e(t["name"].lower())} molecule{"s" if len(mols) != 1 else ""} from the Strides portfolio: {e(names)}. Select a molecule to read its approval history, mechanism of action and key facts, and to send an enquiry.</p></section>
<section class="block"><h2>Molecules in {e(t["name"].lower())}</h2><div class="mol-grid">{"".join(mol_card(m, r) for m in mols)}</div></section>
<div class="prose">
<section class="block"><h2>About this therapy area</h2>{paras(t["intro"])}</section>
<section class="block"><h2>Molecule summaries</h2>{"".join(f'<h3><a href="{r}{mol_path(m)}">{e(m["name"])}</a></h3><p>{e(m["summary"])}</p>' for m in mols)}</section>
<section class="block"><h2>At a glance</h2><div class="table-wrap"><table class="list"><thead><tr><th scope="col">Molecule</th><th scope="col">Drug class</th><th scope="col">First approval</th><th scope="col">ATC</th></tr></thead><tbody>{rows}</tbody></table></div></section>
{faq_html(faqs)}
</div>
</div>
<section class="band band-dark"><div class="wrap cta"><div><h2>Looking for a {e(t["name"].lower())} molecule that is not listed?</h2><p>Tell us the molecule, dosage form and market. The partnering team will confirm what is available.</p></div><a class="btn btn-light" href="{r}contact.html">Contact the partnering team</a></div></section>
"""
    graph = [
        {"@type": "CollectionPage", "@id": canonical(path) + "#webpage", "url": canonical(path),
         "name": f"{t['name']} molecules", "description": t["intro"][0], "isPartOf": {"@id": SITE["url"] + "/#website"},
         "mainEntity": {"@type": "ItemList", "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "name": m["name"], "url": canonical(mol_path(m))} for i, m in enumerate(mols)]}},
        faq_ld(faqs), crumbs_ld(crumbs)]
    title = f"{t['name']} molecules: {names[:60]}{'…' if len(names) > 60 else ''} | Synergice"
    return path, shell(path, title, f"{t['name']} molecules in the Strides portfolio: {names}. Approval history, mechanism of action and partnering enquiries.", body, graph, "products.html")


def build_products():
    path = "products.html"
    r = ""
    crumbs = [("Home", "index.html"), ("Products", path)]
    rows = "".join(
        f'<tr data-q="{e((m["name"] + " " + " ".join(m["aka"]) + " " + THER[m["therapy"]]["name"] + " " + m["klass"]).lower())}">'
        f'<td><a href="{mol_path(m)}">{e(m["name"])}</a></td><td><a href="{ther_path(THER[m["therapy"]])}">{e(THER[m["therapy"]]["name"])}</a></td>'
        f'<td>{e(m["klass"])}</td><td>{e(m["first_approval"].split(",")[0])}</td></tr>' for m in MOLECULES)
    faqs = [
        ("How are products organised on Synergice?", f"Products are organised into {len(THERAPIES)} therapy areas, from cardiovascular and oncology to women's health. Each therapy area lists its molecules, and each molecule has its own page with key facts, approval history and mechanism of action."),
        ("What does each molecule page include?", "An answer-first summary, a key facts table, approval history, mechanism of action, approved uses, pharmacokinetics at a glance, frequently asked questions and an enquiry form."),
        ("Can I enquire about a product that is not on this list?", "Yes. The Strides partner portfolio includes more than 250 formulations. Use the contact form and name the molecule, dosage form and market."),
    ]
    body = f"""
<div class="wrap">
{crumbs_html(path, crumbs)}
<header class="page-head"><p class="eyebrow">Products</p><h1>Molecules by therapy area</h1><p class="sub">{len(MOLECULES)} molecules across {len(THERAPIES)} therapy areas. Choose a therapy area, or search the full list below.</p></header>
<section class="answer"><p class="answer-label">In brief</p><p>Synergice lists molecules from the Strides Pharma Science portfolio in {len(THERAPIES)} therapy areas. Each molecule page explains when the molecule was first approved, how it works and its key facts, and includes an enquiry form for business partners.</p></section>
<section class="block"><h2>Therapy areas</h2>{therapy_tiles(r)}</section>
<section class="block" id="all"><h2>All molecules A–Z</h2>
  <div class="filter"><label for="mol-filter">Filter molecules</label><input id="mol-filter" type="search" placeholder="Type a molecule, brand, class or therapy area" data-filter="#mol-table tbody tr"></div>
  <div class="table-wrap"><table class="list" id="mol-table"><thead><tr><th scope="col">Molecule</th><th scope="col">Therapy area</th><th scope="col">Drug class</th><th scope="col">First approved</th></tr></thead><tbody>{rows}</tbody></table></div>
  <p class="filter-empty" hidden>No molecules match. <a href="contact.html">Ask the partnering team</a> about it instead.</p>
</section>
<div class="prose">{faq_html(faqs)}</div>
</div>
"""
    graph = [{"@type": "CollectionPage", "@id": canonical(path) + "#webpage", "url": canonical(path),
              "name": "Molecules by therapy area", "isPartOf": {"@id": SITE["url"] + "/#website"},
              "mainEntity": {"@type": "ItemList", "itemListElement": [
                  {"@type": "ListItem", "position": i + 1, "name": m["name"], "url": canonical(mol_path(m))} for i, m in enumerate(MOLECULES)]}},
             faq_ld(faqs), crumbs_ld(crumbs)]
    return path, shell(path, "Products: molecules by therapy area | Synergice",
                       f"Browse {len(MOLECULES)} molecules from the Strides portfolio across {len(THERAPIES)} therapy areas, with approval history, mechanism of action and enquiry forms.",
                       body, graph, path)


def build_home():
    path = "index.html"
    r = ""
    featured = [MOL[s] for s in ["mycophenolate-mofetil", "colchicine", "naproxen-sodium", "potassium-chloride"]]
    search_data = json.dumps([{"n": m["name"], "u": mol_path(m), "t": THER[m["therapy"]]["name"],
                               "k": " ".join(m["aka"]).lower()} for m in MOLECULES], ensure_ascii=False)
    steps = "".join(f'<li><span class="step-n">{i + 1}</span><h3>{e(h)}</h3><p>{e(p)}</p></li>' for i, (h, p) in enumerate(HOME["steps"]))
    aud = "".join(f"<li><h3>{e(h)}</h3><p>{e(p)}</p></li>" for h, p in HOME["audiences"])
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">{e(HOME["eyebrow"])}</p>
      <h1>{e(HOME["h1"])}</h1>
      <p class="lead">{e(HOME["lead"])}</p>
      <div class="search" role="search">
        <label for="hero-search">Find a molecule</label>
        <div class="search-box"><input id="hero-search" type="search" autocomplete="off" placeholder="Try atorvastatin, tacrolimus or Coartem" aria-controls="hero-results" aria-expanded="false"><a class="btn" href="products.html">Browse all</a></div>
        <ul id="hero-results" class="search-results" role="listbox" hidden></ul>
        <script type="application/json" id="molecule-index">{search_data}</script>
      </div>
      <dl class="stats"><div><dt>Molecules listed</dt><dd>{len(MOLECULES)}</dd></div><div><dt>Therapy areas</dt><dd>{len(THERAPIES)}</dd></div><div><dt>Countries supplied by Strides</dt><dd>100+</dd></div></dl>
    </div>
    <div class="hero-art" aria-hidden="true">{S_MARK}{S_MARK}{S_MARK}</div>
  </div>
</section>
<section class="wrap block" id="therapy-areas"><div class="sec-head"><h2>Browse by therapy area</h2><p>Select a therapy area to see its molecules.</p></div>{therapy_tiles(r)}</section>
<section class="band band-mint"><div class="wrap"><div class="sec-head"><h2>How an enquiry works</h2></div><ol class="steps">{steps}</ol></div></section>
<section class="wrap block"><div class="sec-head"><h2>Molecules with recent Strides approvals</h2><p>US FDA approvals and portfolio additions reported by Strides.</p></div><div class="mol-grid">{"".join(mol_card(m, r) for m in featured)}</div></section>
<section class="wrap block"><div class="sec-head"><h2>Who we work with</h2></div><div class="prose"><p>{e(HOME["about"])} <a href="about.html">More about Synergice</a></p></div><ul class="audiences">{aud}</ul></section>
<div class="wrap prose">{faq_html(HOME["faqs"])}</div>
<section class="band band-dark"><div class="wrap cta"><div><h2>Have a molecule in mind?</h2><p>Send one short enquiry. The Synergice partnering team at Strides replies directly.</p></div><a class="btn btn-light" href="contact.html">Contact us</a></div></section>
"""
    graph = [{"@type": "WebPage", "@id": canonical(path) + "#webpage", "url": canonical(path),
              "name": "Synergice: molecules and partnering enquiries from Strides Pharma Science",
              "isPartOf": {"@id": SITE["url"] + "/#website"}, "about": {"@id": SITE["url"] + "/#org"}},
             faq_ld(HOME["faqs"])]
    return path, shell(path, "Synergice | Molecules and partnering enquiries from Strides Pharma Science",
                       "Synergice is the B2B partnering platform of Strides Pharma Science. Browse molecules by therapy area, read approval history and mechanism of action, and enquire directly.",
                       body, graph, path)


def build_about():
    path = "about.html"
    crumbs = [("Home", "index.html"), ("About us", path)]
    secs = "".join(f'<section class="block"><h2>{e(h)}</h2>{paras(ps)}</section>' for h, ps in ABOUT["sections"])
    body = f"""
<div class="wrap">
{crumbs_html(path, crumbs)}
<header class="page-head"><p class="eyebrow">About us</p><h1>{e(ABOUT["h1"])}</h1></header>
<div class="prose">
<section class="answer"><p class="answer-label">In brief</p><p>{e(ABOUT["summary"])}</p></section>
<section class="block"><h2>Key facts</h2>{kv_table([(k, e(v)) for k, v in COMPANY_FACTS])}</section>
{secs}
<section class="block"><h2>Milestones</h2>{timeline_table(ABOUT["timeline"])}</section>
{faq_html(ABOUT["faqs"])}
</div>
</div>
<section class="band band-dark"><div class="wrap cta"><div><h2>Talk to the partnering team</h2><p>Ask about any molecule in the portfolio, or one you do not see listed.</p></div><a class="btn btn-light" href="contact.html">Contact us</a></div></section>
"""
    graph = [{"@type": "AboutPage", "@id": canonical(path) + "#webpage", "url": canonical(path), "name": "About Synergice",
              "description": ABOUT["summary"], "isPartOf": {"@id": SITE["url"] + "/#website"}, "about": {"@id": SITE["url"] + "/#org"}},
             faq_ld(ABOUT["faqs"]), crumbs_ld(crumbs)]
    return path, shell(path, "About Synergice, the B2B partnering platform of Strides Pharma Science",
                       "Synergice brings the Strides Pharma Science partner portfolio of 250+ formulations into one place for licensing partners, MAHs and distributors in 100+ countries.",
                       body, graph, path)


def build_contact():
    path = "contact.html"
    crumbs = [("Home", "index.html"), ("Contact us", path)]
    nxt = "".join(f'<li><span class="step-n">{i + 1}</span><h3>{e(h)}</h3><p>{e(p)}</p></li>' for i, (h, p) in enumerate(CONTACT["next"]))
    body = f"""
<div class="wrap">
{crumbs_html(path, crumbs)}
<header class="page-head"><p class="eyebrow">Contact us</p><h1>{e(CONTACT["h1"])}</h1></header>
<div class="contact-grid">
  <div class="prose">
    <section class="answer"><p class="answer-label">In brief</p><p>{e(CONTACT["summary"])}</p></section>
    <section class="block"><h2>What to include</h2><ul class="ticks">{"".join(f"<li>{e(i)}</li>" for i in CONTACT["include"])}</ul></section>
    <section class="block"><h2>Offices</h2>{kv_table([(k, e(v)) for k, v in CONTACT["offices"]])}</section>
  </div>
  <div class="form-card">{enquiry_form(path, None, "Send an enquiry")}</div>
</div>
<section class="block"><h2>What happens after you enquire</h2><ol class="steps">{nxt}</ol></section>
<div class="prose">{faq_html(CONTACT["faqs"])}</div>
</div>
"""
    graph = [{"@type": "ContactPage", "@id": canonical(path) + "#webpage", "url": canonical(path), "name": "Contact the Synergice partnering team",
              "description": CONTACT["summary"], "isPartOf": {"@id": SITE["url"] + "/#website"}},
             faq_ld(CONTACT["faqs"]), crumbs_ld(crumbs)]
    return path, shell(path, "Contact the Synergice partnering team | Strides Pharma Science",
                       "Send an enquiry about any molecule in the Strides portfolio. Tell us your name, email, how you heard about us and what you want to know.",
                       body, graph, path)


def build_insights_index():
    path = "insights.html"
    crumbs = [("Home", "index.html"), ("Insights", path)]
    cards = "".join(f'<a class="art-card" href="{art_path(a)}"><span class="art-date">{e(a["date"])}</span><span class="art-t">{e(a["title"])}</span><span class="art-d">{e(a["description"])}</span></a>' for a in ARTICLES)
    body = f"""
<div class="wrap">
{crumbs_html(path, crumbs)}
<header class="page-head"><p class="eyebrow">Insights</p><h1>Insights for partners</h1><p class="sub">Short, practical guides for regulatory and sourcing teams.</p></header>
<div class="art-grid">{cards}</div>
</div>
"""
    graph = [{"@type": "CollectionPage", "@id": canonical(path) + "#webpage", "url": canonical(path), "name": "Insights for partners",
              "isPartOf": {"@id": SITE["url"] + "/#website"}}, crumbs_ld(crumbs)]
    return path, shell(path, "Insights for pharmaceutical partners | Synergice",
                       "Practical guides for regulatory and sourcing teams: dossier formats, bioequivalence, stability and supplier evaluation.",
                       body, graph, path)


def build_article(a):
    path = art_path(a)
    crumbs = [("Home", "index.html"), ("Insights", "insights.html"), (a["title"], path)]
    secs = "".join(f'<section class="block"><h2>{e(h)}</h2>{paras(ps)}</section>' for h, ps in a["sections"])
    body = f"""
<div class="wrap">
{crumbs_html(path, crumbs)}
<article class="prose article">
<header class="page-head"><p class="eyebrow">Insights · {e(a["date"])}</p><h1>{e(a["title"])}</h1></header>
<section class="answer"><p class="answer-label">Summary</p><p>{e(a["summary"])}</p></section>
{secs}
{faq_html(a["faqs"])}
</article>
</div>
<section class="band band-dark"><div class="wrap cta"><div><h2>Evaluating a product?</h2><p>Ask the partnering team about dossier format, bioequivalence and site approvals for any molecule.</p></div><a class="btn btn-light" href="../contact.html">Contact us</a></div></section>
"""
    graph = [{"@type": "Article", "@id": canonical(path) + "#article", "headline": a["title"], "description": a["description"],
              "datePublished": a["date"], "dateModified": a["date"], "url": canonical(path),
              "author": {"@id": SITE["url"] + "/#org"}, "publisher": {"@id": SITE["url"] + "/#org"},
              "isPartOf": {"@id": SITE["url"] + "/#website"}},
             faq_ld(a["faqs"]), crumbs_ld(crumbs)]
    return path, shell(path, f"{a['title']} | Synergice Insights", a["description"], body, graph, "insights.html")


# --------------------------------------------- machine-readable companions
def search_index():
    """Chunks for the on-site assistant's retrieval (one per section)."""
    out = []

    def add(title, url, text, mol="", aka=None):
        out.append({"t": title, "u": url, "x": text, "m": mol, **({"k": aka} if aka else {})})

    for m in MOLECULES:
        u, n = mol_path(m), m["name"]
        fw = framework_text(m)
        aka = m["aka"] + ([m["short"]] if m.get("short") else [])
        add(f"{n}: about", u + "#about", m["overview_molecule"] + " " + fw["manufacture"] + " Also known as: " + ", ".join(aka) + ".", n, aka)
        add(f"{n}: key facts", u,
            f"{n}. Drug class: {m['klass']}. ATC code: {m['atc']}. Reference product: {m['reference']}. First approved: {m['first_approval']}. Dosage form: {m['form']}."
            + (f" Strengths: {m['strengths']}." if m.get("strengths") else "") + f" Therapeutic category: {THER[m['therapy']]['name']}.", n)
        add(f"{n}: mechanism of action", u + "#moa", m["moa_short"], n)
        add(f"{n}: indication", u + "#indication", m["indication"], n)
        add(f"{n}: approval history", u + "#history", f"When was {n} approved? " + " ".join(f"{y}: {t}" for y, t in m["timeline"]), n)
        add(f"{n}: formulation and presentation", u + "#formulation", fw["formulation"], n)
    add("Manufacturing and quality", "products.html", INFO_QUALITY)
    add("Supply and partnership", "products.html", INFO_SUPPLY)
    for q, a in FAQ_FIXED:
        add(q, "contact.html", f"{q} {a}")
    for t in THERAPIES:
        add(f"{t['name']} therapy area", ther_path(t), " ".join(t["intro"]) + " Molecules: " + ", ".join(m["name"] for m in t["molecules"]) + ".")
        for q, a in t["faqs"]:
            add(f"{t['name']}: {q}", ther_path(t) + "#faq", f"{q} {a}")
    add("About Synergice", "about.html", ABOUT["summary"] + " " + " ".join(f"{k}: {v}." for k, v in COMPANY_FACTS))
    for h, ps in ABOUT["sections"]:
        add(f"About: {h}", "about.html", " ".join(ps))
    for q, a in HOME["faqs"] + ABOUT["faqs"]:
        add(q, "about.html#faq", f"{q} {a}")
    add("How to send an enquiry", "contact.html",
        "To send an enquiry, use the form at the end of any molecule page or on the contact page. Give your full name, work email, "
        "how you heard about us and what you would like to know, such as your market, the dosage form and strengths you need, and "
        "whether you hold a marketing authorisation. The Synergice partnering team at Strides replies directly.")
    add("Contact the partnering team", "contact.html", CONTACT["summary"] + " Include: " + "; ".join(CONTACT["include"]) + ".")
    for q, a in CONTACT["faqs"]:
        add(q, "contact.html#faq", f"{q} {a}")
    for a in ARTICLES:
        add(a["title"], art_path(a), a["summary"])
        for h, ps in a["sections"]:
            add(f"{a['title']}: {h}", art_path(a), " ".join(ps))
    return out


def llms_txt():
    lines = ["# Synergice", "",
             "> Synergice is the B2B partnering platform of Strides Pharma Science Limited (Bengaluru, India; European hub in Zug, Switzerland). "
             "This site lists molecules from the Strides portfolio with approval history, mechanism of action and key facts, and takes partnering enquiries. "
             "It is intended for pharmaceutical business partners, not patients.", "",
             "## Company", f"- [About Synergice]({canonical('about.html')}): who we are, key facts and milestones",
             f"- [Contact the partnering team]({canonical('contact.html')}): enquiry form (name, email, how you heard about us, what you want to know)", "",
             "## Therapy areas"]
    lines += [f"- [{t['name']}]({canonical(ther_path(t))}): " + ", ".join(m["name"] for m in t["molecules"]) for t in THERAPIES]
    lines += ["", "## Molecules"]
    lines += [f"- [{m['name']}]({canonical(mol_path(m))}): {m['klass']}; first approved {m['first_approval']}; ATC {m['atc'].split(' ')[0]}" for m in MOLECULES]
    lines += ["", "## Insights"]
    lines += [f"- [{a['title']}]({canonical(art_path(a))}): {a['description']}" for a in ARTICLES]
    return "\n".join(lines) + "\n"


def robots_txt():
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "Bingbot", "Googlebot"]
    return ("# Answer engines and AI assistants are welcome to read and cite this site.\n"
            + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots)
            + "User-agent: *\nAllow: /\n\n" + f"Sitemap: {SITE['url']}/sitemap.xml\n")


def sitemap(paths):
    urls = "".join(f"<url><loc>{e(canonical(p))}</loc><lastmod>{SITE['updated']}</lastmod></url>" for p in paths)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n'


# --------------------------------------------------------------- word count
LIMITS = {"overview_molecule": (60, 90), "moa_short": (30, 60), "indication": (30, 60),
          "manufacture": (50, 80), "formulation": (40, 70)}


def words(text):
    return len(re.findall(r"[A-Za-z0-9][\w'’\-/.]*", text))


def framework_checks():
    """Build notes: report any framework field outside its word range."""
    out = []
    for label, text, lo, hi in [("INFO_QUALITY", INFO_QUALITY, 50, 80), ("INFO_SUPPLY", INFO_SUPPLY, 40, 70)]:
        if not lo <= words(text) <= hi:
            out.append(f"{label}: {words(text)} words (target {lo}-{hi})")
    for m in MOLECULES:
        fw = framework_text(m)
        for key, (lo, hi) in LIMITS.items():
            n = words(m.get(key) or fw.get(key, ""))
            if not lo <= n <= hi:
                out.append(f"{m['slug']}.{key}: {n} words (target {lo}-{hi})")
    return out


def visible_words(html):
    main = html.split('<main id="main">', 1)[1].split("</main>", 1)[0]
    main = re.sub(r"<script.*?</script>", " ", main, flags=re.S)
    main = re.sub(r"<form.*?</form>", " ", main, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", main)
    return len(re.findall(r"[A-Za-z0-9][\w'’\-]*", text))


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "assets").mkdir(parents=True)
    shutil.copytree(ROOT / "static", DIST / "assets", dirs_exist_ok=True)

    pages = [build_home(), build_about(), build_products(), build_contact(), build_insights_index()]
    pages += [build_therapy(t) for t in THERAPIES]
    pages += [build_molecule(m) for m in MOLECULES]
    pages += [build_article(a) for a in ARTICLES]
    extra = [build_privacy()]

    report = []
    for path, html in pages + extra:
        out = DIST / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        report.append((path, visible_words(html)))

    (DIST / "assets" / "search-index.json").write_text(
        json.dumps(search_index(), ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (DIST / "llms.txt").write_text(llms_txt(), encoding="utf-8")
    (DIST / "robots.txt").write_text(robots_txt(), encoding="utf-8")
    (DIST / "sitemap.xml").write_text(sitemap([p for p, _ in pages]), encoding="utf-8")

    print(f"Built {len(pages) + len(extra)} pages into {DIST.relative_to(ROOT)}/")
    problems = framework_checks()
    print("Framework v2.0 word limits: " + ("all within range" if not problems else f"{len(problems)} outside range"))
    for p in problems:
        print("  " + p)
    print(f"{'words':>6}  page")
    for path, n in report:
        # The 600-1,200 word target applies to answer pages, not hubs or forms.
        target = path.startswith(("molecule/", "insights/")) or path in ("index.html", "about.html")
        flag = "  < 600" if target and n < 600 else ("  > 1200" if target and n > 1200 else "")
        print(f"{n:>6}  {path}{flag}")


if __name__ == "__main__":
    main()
