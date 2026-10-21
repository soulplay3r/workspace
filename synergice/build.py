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
from pages import (ABOUT, ARTICLES, COMPANY_FACTS, CONTACT, HEAR_ABOUT,  # noqa: E402
                   HOME)

SITE = {
    "name": "Synergice",
    "url": os.environ.get("SITE_URL", "https://www.synergice.com").rstrip("/"),
    "parent": "Strides Pharma Science Limited",
    "parent_url": "https://www.strides.com",
    "form_endpoint": os.environ.get("FORM_ENDPOINT", ""),
    "chat_endpoint": os.environ.get("CHAT_ENDPOINT", ""),
    "updated": "2026-10-21",
    "updated_label": "21 October 2026",
}

DIST = ROOT / "dist"
MOLECULES = sorted(MOLECULES_A + MOLECULES_B + MOLECULES_C, key=lambda m: m["name"].lower())
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


def enquiry_form(path, molecule=None, heading="Send an enquiry", intro=None):
    uid = molecule["slug"] if molecule else "general"
    opts = '<option value="">Select a molecule (optional)</option>' + "".join(
        f'<option{" selected" if molecule and m["slug"] == molecule["slug"] else ""}>{e(m["name"])}</option>'
        for m in MOLECULES) + "<option>A molecule not listed here</option>"
    hear = '<option value="">Select one</option>' + "".join(f"<option>{e(h)}</option>" for h in HEAR_ABOUT)
    endpoint = f' data-endpoint="{e(SITE["form_endpoint"])}"' if SITE["form_endpoint"] else ""
    intro_html = f'<p class="form-intro">{e(intro)}</p>' if intro else ""
    return f"""<form class="enquiry" id="enquiry-{uid}" novalidate{endpoint}>
  <h2 class="form-h">{e(heading)}</h2>{intro_html}
  <div class="grid2">
    <div class="field"><label for="{uid}-name">Full name</label><input id="{uid}-name" name="name" autocomplete="name" required></div>
    <div class="field"><label for="{uid}-company">Company</label><input id="{uid}-company" name="company" autocomplete="organization"></div>
    <div class="field"><label for="{uid}-email">Work email</label><input id="{uid}-email" name="email" type="email" autocomplete="email" required></div>
    <div class="field"><label for="{uid}-country">Country or market</label><input id="{uid}-country" name="country" autocomplete="country-name"></div>
    <div class="field"><label for="{uid}-molecule">Molecule</label><select id="{uid}-molecule" name="molecule">{opts}</select></div>
    <div class="field"><label for="{uid}-hear">How did you hear about us?</label><select id="{uid}-hear" name="heard_about" required>{hear}</select></div>
  </div>
  <div class="field"><label for="{uid}-message">What would you like to know?</label><textarea id="{uid}-message" name="message" rows="4" required placeholder="For example: registration position in Kenya, available strengths, dossier format"></textarea></div>
  <div class="field check"><input id="{uid}-consent" name="consent" type="checkbox" required><label for="{uid}-consent">I agree that Strides Pharma Science may use these details to respond to my enquiry.</label></div>
  <input type="hidden" name="page" value="{e(path)}">
  <button class="btn" type="submit">Send enquiry</button>
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
def build_molecule(m):
    path = mol_path(m)
    r = "../"
    t = THER[m["therapy"]]
    short = f" ({m['short']})" if m.get("short") else ""
    crumbs = [("Home", "index.html"), ("Products", "products.html"), (t["name"], ther_path(t)), (m["name"], path)]
    atc_link = m["atc"].split(" ")[0]
    facts = [
        ("Generic name", e(m["name"]) + e(short)),
        ("Drug class", e(m["klass"])),
        ("ATC code", f'<a href="https://atcddd.fhi.no/atc_ddd_index/?code={e(atc_link)}" rel="noopener">{e(m["atc"])}</a>'),
        ("Reference product", e(m["reference"])),
        ("First approval", e(m["first_approval"])),
        ("Route", e(m["route"])),
        ("Dosage form", e(m["form"])),
        ("Therapy area", f'<a href="{r}{ther_path(t)}">{e(t["name"])}</a>'),
    ]
    if m.get("portfolio_note"):
        facts.append(("Strides portfolio", e(m["portfolio_note"])))
    lname = lower_first(m["name"])
    faqs = m["faqs"] + [(
        f"How do I enquire about sourcing {lname} from Synergice?",
        f"Use the enquiry form on this page. Give your name, work email, how you heard about us and what you want to know about {lname}, such as your market and the strengths you need. The Synergice partnering team at Strides replies directly.")]
    sourcing = [
        f"Synergice is the B2B partnering platform of Strides Pharma Science Limited. If you are evaluating {lname} for your market, the partnering team can tell you what Strides holds for this molecule, where it is registered and how a partnership could work, from dossier licensing to contract supply.",
        "Send an enquiry from this page with your market and the information you need first. Detailed documentation, such as dossier status, stability and bioequivalence summaries and manufacturing site approvals, is shared directly during evaluation.",
    ]
    related = [MOL[s] for s in m["related"] if s in MOL]
    toc = [("facts", "Key facts"), ("overview", "Overview"), ("history", "Approval history"),
           ("moa", "Mechanism of action"), ("uses", "Approved uses"), ("pk", "Pharmacokinetics"),
           ("faq", "FAQs"), ("enquire", "Enquire")]
    dq = e(f"How does {lname} work?")
    body = f"""
<div class="wrap">
{crumbs_html(path, crumbs)}
<header class="page-head mol-head">
  <p class="eyebrow"><a href="{r}{ther_path(t)}">{e(t["name"])}</a></p>
  <h1>{e(m["name"])}{e(short)}</h1>
  <p class="sub">{e(m["klass"])} · ATC {e(m["atc"].split(" ")[0])}</p>
  <div class="actions"><a class="btn" href="#enquire">Enquire about {e(lname)}</a><button class="btn btn-ghost" type="button" data-chat-open data-q="{dq}">Ask the assistant</button></div>
</header>
<div class="mol-layout">
<article class="prose">
  <section class="answer" aria-label="In brief"><p class="answer-label">In brief</p><p>{e(m["summary"])}</p></section>
  <section class="block" id="facts"><h2>Key facts</h2>{kv_table(facts)}</section>
  <section class="block" id="overview"><h2>Overview</h2>{paras(m["overview"])}</section>
  <section class="block" id="history"><h2>Approval history</h2><p>When {e(lname)} was first approved and the milestones that shaped its use.</p>{timeline_table(m["timeline"])}</section>
  <section class="block" id="moa"><h2>Mechanism of action</h2>{paras(m["moa"])}</section>
  <section class="block" id="uses"><h2>Approved uses</h2><p>Indications in reference prescribing information. Approved uses differ between markets; local labelling applies.</p><ul class="ticks">{"".join(f"<li>{e(i)}</li>" for i in m["indications"])}</ul></section>
  <section class="block" id="pk"><h2>Pharmacokinetics at a glance</h2>{kv_table([(k, e(v)) for k, v in m["pk"]], "facts pk")}</section>
  <section class="block" id="sourcing"><h2>Sourcing {e(lname)} through Synergice</h2>{paras(sourcing)}</section>
  {faq_html(faqs)}
  <section class="block refs" id="refs"><h2>References</h2><ul>
    <li><a href="https://dailymed.nlm.nih.gov/dailymed/search.cfm?query={e(m["slug"].split("-")[0])}" rel="noopener">US prescribing information (DailyMed)</a></li>
    <li><a href="https://atcddd.fhi.no/atc_ddd_index/?code={e(atc_link)}" rel="noopener">WHO ATC/DDD index: {e(atc_link)}</a></li>
    <li><a href="https://www.ema.europa.eu/en/search?search_api_fulltext={e(m["slug"].split("-")[0])}" rel="noopener">European Medicines Agency</a></li>
  </ul><p class="meta">Content summarises public prescribing information for business partners. Last updated {SITE["updated_label"]}.</p></section>
</article>
<aside class="side">
  <nav class="toc" aria-label="On this page"><p class="toc-h">On this page</p>{"".join(f'<a href="#{i}">{l}</a>' for i, l in toc)}</nav>
  <div class="side-card"><p class="side-h">Interested in {e(lname)}?</p><p>Ask the partnering team about registration, dossier status and supply for your market.</p><a class="btn btn-block" href="#enquire">Send an enquiry</a></div>
</aside>
</div>
</div>
<section class="band band-mint" id="enquire"><div class="wrap narrow">{enquiry_form(path, m, f"Enquire about {lname}", "Tell us who you are and what you want to know. Your enquiry goes directly to the Synergice partnering team.")}</div></section>
<section class="wrap block"><h2>Related molecules</h2><div class="mol-grid">{"".join(mol_card(x, r) for x in related)}</div><p class="more"><a href="{r}{ther_path(t)}">All {e(t["name"].lower())} molecules →</a></p></section>
"""
    graph = [
        {"@type": "MedicalWebPage", "@id": canonical(path) + "#webpage", "url": canonical(path),
         "name": f"{m['name']}: approval history, mechanism of action and key facts",
         "description": m["summary"], "lastReviewed": SITE["updated"], "dateModified": SITE["updated"],
         "inLanguage": "en", "isPartOf": {"@id": SITE["url"] + "/#website"},
         "about": {"@id": canonical(path) + "#drug"}, "publisher": {"@id": SITE["url"] + "/#org"},
         "audience": {"@type": "Audience", "audienceType": "Pharmaceutical business partners"}},
        {"@type": "Drug", "@id": canonical(path) + "#drug", "name": m["name"],
         "nonProprietaryName": m["name"], "alternateName": [a for a in m["aka"][:4]],
         "drugClass": {"@type": "DrugClass", "name": m["klass"]},
         "mechanismOfAction": m["moa"][0], "administrationRoute": m["route"], "dosageForm": m["form"],
         "code": {"@type": "MedicalCode", "code": m["atc"].split(" ")[0], "codingSystem": "ATC"},
         "url": canonical(path)},
        faq_ld(faqs), crumbs_ld(crumbs)]
    title = f"{m['name']}{short}: approval history, mechanism of action and key facts | Synergice"
    desc = m["summary"][:155].rsplit(" ", 1)[0] + "…" if len(m["summary"]) > 158 else m["summary"]
    return path, shell(path, title, desc, body, graph, "products.html")


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
        k = " Also known as: " + ", ".join(m["aka"]) + "."
        add(f"{n}: in brief", u + "#facts", m["summary"] + k, n, m["aka"] + ([m["short"]] if m.get("short") else []))
        add(f"{n}: key facts", u + "#facts",
            f"{n}. Class: {m['klass']}. ATC code: {m['atc']}. Reference product: {m['reference']}. First approval: {m['first_approval']}. Route: {m['route']}. Dosage form: {m['form']}. Therapy area: {THER[m['therapy']]['name']}." + (" " + m["portfolio_note"] if m.get("portfolio_note") else ""), n)
        add(f"{n}: overview", u + "#overview", " ".join(m["overview"]), n)
        add(f"{n}: approval history", u + "#history", " ".join(f"{y}: {t}" for y, t in m["timeline"]), n)
        add(f"{n}: mechanism of action", u + "#moa", " ".join(m["moa"]), n)
        add(f"{n}: approved uses", u + "#uses", f"{n} is used for: " + "; ".join(m["indications"]) + ".", n)
        add(f"{n}: pharmacokinetics", u + "#pk", "; ".join(f"{k2}: {v}" for k2, v in m["pk"]) + ".", n)
        for q, a in m["faqs"]:
            add(f"{n}: {q}", u + "#faq", f"{q} {a}", n)
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

    report = []
    for path, html in pages:
        out = DIST / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        report.append((path, visible_words(html)))

    (DIST / "assets" / "search-index.json").write_text(
        json.dumps(search_index(), ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (DIST / "llms.txt").write_text(llms_txt(), encoding="utf-8")
    (DIST / "robots.txt").write_text(robots_txt(), encoding="utf-8")
    (DIST / "sitemap.xml").write_text(sitemap([p for p, _ in pages]), encoding="utf-8")

    print(f"Built {len(pages)} pages into {DIST.relative_to(ROOT)}/")
    print(f"{'words':>6}  page")
    for path, n in report:
        # The 600-1,200 word target applies to answer pages, not hubs or forms.
        target = path.startswith(("molecule/", "insights/")) or path in ("index.html", "about.html")
        flag = "  < 600" if target and n < 600 else ("  > 1200" if target and n > 1200 else "")
        print(f"{n:>6}  {path}{flag}")


if __name__ == "__main__":
    main()
