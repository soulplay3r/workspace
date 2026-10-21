/* Synergice assistant: retrieval-augmented answers from this site's content.

   Retrieval runs in the browser (BM25 over assets/search-index.json), so the
   assistant works on a static host with no backend. When the <script> tag
   carries data-endpoint, the top passages are sent to that endpoint (see
   api/chat.mjs) and an LLM writes the answer, grounded in those passages. */
(function () {
  "use strict";
  var me = document.currentScript;
  var ROOT = (me && me.getAttribute("data-root")) || "";
  var ENDPOINT = me && me.getAttribute("data-endpoint");

  var STOP = ("a an and are as at be by can do does for from has have how i in is it its me my of on or our "
    + "the this to was what when where which who why with you your about tell please there their than that "
    + "these those them they will would should could also any all more most into used use uses").split(" ");
  var stop = {};
  STOP.forEach(function (w) { stop[w] = 1; });

  var tokens = function (s) {
    return (s.toLowerCase().match(/[a-z0-9]+/g) || [])
      .filter(function (w) { return !stop[w] && w.length > 1; })
      .map(function (w) { return w.length > 5 ? w.replace(/(ing|ed|es|al|s)$/, "") : w; });
  };

  var docs = null, df = {}, avgLen = 0, molNames = [];
  var load = function () {
    if (docs) return Promise.resolve();
    return fetch(ROOT + "assets/search-index.json").then(function (r) { return r.json(); }).then(function (raw) {
      docs = raw.map(function (d) {
        var tk = tokens(d.t + " " + d.x);
        var tf = {};
        tk.forEach(function (w) { tf[w] = (tf[w] || 0) + 1; });
        Object.keys(tf).forEach(function (w) { df[w] = (df[w] || 0) + 1; });
        return { d: d, tf: tf, len: tk.length };
      });
      avgLen = docs.reduce(function (s, x) { return s + x.len; }, 0) / docs.length;
      raw.forEach(function (d) {
        if (d.k) molNames.push({ n: d.m, a: [d.m].concat(d.k).map(function (a) { return a.toLowerCase(); }) });
      });
    });
  };

  // Question words that point at a section of a molecule page.
  var INTENTS = [
    [/\b(work|works|mechanism|moa|act|acts|action|target|inhibit)/i, ["mechanism", "action"], "mechanism"],
    [/\b(approv|when|launch|history|first|discover|year|generic)/i, ["approval", "approved", "history"], "approval"],
    [/\b(used|use|uses|indicat|treat|for what|condition)/i, ["used", "indication", "uses"], "uses"],
    [/\b(half|pharmacokinetic|pk|metaboli|absorb|absorption|eliminat|bioavailab|cyp)/i, ["pharmacokinetics", "metabolism", "half"], "pharmacokinetics"],
    [/\b(class|atc|code|reference|brand|originator|dosage form|route)/i, ["class", "atc", "reference"], "key facts"],
    [/\b(enquir|inquir|contact|reach|email)/i, ["enquiry", "enquire", "contact"], "enquiry"]
  ];

  var search = function (q) {
    var qt = tokens(q);
    var sections = [];
    INTENTS.forEach(function (it) {
      if (it[0].test(q)) { qt = qt.concat(it[1]); sections.push(it[2]); }
    });
    var ql = q.toLowerCase();
    var N = docs.length, k1 = 1.4, b = 0.75;
    var words = " " + ql.replace(/[^a-z0-9]+/g, " ") + " ";
    var named = molNames.filter(function (mn) {
      return mn.a.some(function (a) {
        return a.split(/[\s/]+/).some(function (w) { return w.length > 2 && words.indexOf(" " + w.replace(/[^a-z0-9]/g, "") + " ") !== -1; });
      });
    }).map(function (mn) { return mn.n; });
    var hits = docs.map(function (x) {
      var s = 0;
      qt.forEach(function (w) {
        var f = x.tf[w];
        if (!f) return;
        var idf = Math.log(1 + (N - df[w] + 0.5) / (df[w] + 0.5));
        s += idf * (f * (k1 + 1)) / (f + k1 * (1 - b + b * x.len / avgLen));
      });
      if (named.length && x.d.m) s *= named.indexOf(x.d.m) !== -1 ? 2.2 : 0.35;
      var tl = x.d.t.toLowerCase();
      qt.forEach(function (w) { if (tl.indexOf(w) !== -1) s *= 1.15; });
      sections.forEach(function (sec) { if (tl.indexOf(sec) !== -1) s *= 1.8; });
      return { d: x.d, s: s };
    }).filter(function (r) { return r.s > 0; }).sort(function (a, b2) { return b2.s - a.s; });
    hits.named = named;
    return hits;
  };

  var bestSentences = function (text, q, n) {
    var qt = tokens(q);
    var sents = text.match(/[^.!?]+[.!?]+(\s|$)/g) || [text];
    var scored = sents.map(function (s, i) {
      var st = tokens(s);
      var hit = qt.filter(function (w) { return st.indexOf(w) !== -1; }).length;
      return { s: s.trim(), i: i, h: hit };
    });
    var top = scored.slice().sort(function (a, b2) { return b2.h - a.h || a.i - b2.i; }).slice(0, n);
    return top.sort(function (a, b2) { return a.i - b2.i; }).map(function (x) { return x.s; }).join(" ");
  };

  var esc = function (s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; });
  };

  var COMMERCIAL = /\b(price|pricing|cost|quote|moq|minimum order|lead time|supply|supplier|availability|available|stock|dossier|sample|registration|register|licen[cs]|distribut|tender|order|buy|purchase)\w*/i;
  var MEDICAL = /\b(should i|can i take|my (dose|doctor|child|mother|father|wife|husband|patient)|i am taking|i'm taking|side effects? (for|in) me|overdose|pregnan\w* .*take)\b/i;

  // ---------------------------------------------------------------- UI
  var fab = document.createElement("button");
  fab.className = "chat-fab";
  fab.type = "button";
  fab.innerHTML = '<span class="dot" aria-hidden="true"></span>Ask Synergice';
  fab.setAttribute("aria-haspopup", "dialog");

  var panel = document.createElement("section");
  panel.className = "chat-panel";
  panel.hidden = true;
  panel.setAttribute("role", "dialog");
  panel.setAttribute("aria-label", "Synergice assistant");
  panel.innerHTML =
    '<div class="chat-head"><svg class="smark" viewBox="0 0 60 80" aria-hidden="true"><path d="M47 15 39 7H19L9 17v9l10 10 22 8 10 10v9L41 74H21l-8-8" fill="none" stroke="currentColor" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>' +
    '<div><p class="chat-title">Synergice assistant</p><p class="chat-subtitle">Answers from our molecule library</p></div>' +
    '<button class="chat-close" type="button" aria-label="Close assistant">×</button></div>' +
    '<div class="chat-log" aria-live="polite"></div>' +
    '<form class="chat-form"><label class="vh" for="chat-input" hidden>Your question</label>' +
    '<input id="chat-input" autocomplete="off" placeholder="Ask about a molecule…" maxlength="400">' +
    '<button class="btn" type="submit">Ask</button></form>' +
    '<p class="chat-note">For business partners. Not medical advice.</p>';
  document.body.appendChild(fab);
  document.body.appendChild(panel);

  var log = panel.querySelector(".chat-log");
  var form = panel.querySelector(".chat-form");
  var field = panel.querySelector("#chat-input");
  var greeted = false;

  var add = function (html, who) {
    var div = document.createElement("div");
    div.className = "msg msg-" + who;
    div.innerHTML = html;
    log.appendChild(div);
    log.scrollTop = log.scrollHeight;
    return div;
  };

  var pageMolecule = function () {
    var h = document.querySelector(".mol-head h1");
    return h ? h.textContent.replace(/\s*\(.*\)$/, "") : null;
  };

  var greet = function () {
    if (greeted) return;
    greeted = true;
    var m = pageMolecule();
    var qs = m
      ? ["How does " + m + " work?", "When was " + m + " approved?", "What is " + m + " used for?", "How do I enquire about " + m + "?"]
      : ["What is tacrolimus used for?", "Which oncology molecules do you list?", "When was atorvastatin approved?", "How do I send an enquiry?"];
    var el = add("<p>Hello. I answer questions using the molecule pages on this site: approval history, mechanism of action and key facts. For supply or commercial questions I'll point you to the partnering team.</p>" +
      '<div class="chips">' + qs.map(function (q) { return '<button class="chip" type="button">' + esc(q) + "</button>"; }).join("") + "</div>", "bot");
    el.querySelectorAll(".chip").forEach(function (c) {
      c.addEventListener("click", function () { ask(c.textContent); });
    });
  };

  var open = function (q) {
    panel.hidden = false;
    fab.hidden = true;
    greet();
    load();
    if (q) ask(q); else field.focus();
  };
  var close = function () { panel.hidden = true; fab.hidden = false; fab.focus(); };

  fab.addEventListener("click", function () { open(); });
  panel.querySelector(".chat-close").addEventListener("click", close);
  panel.addEventListener("keydown", function (ev) { if (ev.key === "Escape") close(); });
  document.querySelectorAll("[data-chat-open]").forEach(function (b) {
    b.addEventListener("click", function () { open(b.getAttribute("data-q")); });
  });

  var sourcesHtml = function (hits) {
    var seen = {}, out = [];
    var floor = hits.length ? hits[0].s * 0.45 : 0;
    hits.forEach(function (h) {
      if (h.s < floor) return;
      var base = h.d.u.split("#")[0];
      if (seen[base] || out.length >= 3) return;
      seen[base] = 1;
      out.push('<a href="' + esc(ROOT + h.d.u) + '">' + esc(h.d.t) + "</a>");
    });
    return out.length ? '<div class="src">Sources' + out.join("") + "</div>" : "";
  };

  var enquiryLink = function () {
    return document.getElementById("enquire") ? "#enquire" : ROOT + "contact.html";
  };

  var ask = function (q) {
    q = (q || "").trim();
    if (!q) return;
    add("<p>" + esc(q) + "</p>", "user");
    var wait = add('<p class="typing">Looking that up…</p>', "bot");
    load().then(function () {
      var hits = search(q);
      var prefix = "";
      if (MEDICAL.test(q)) {
        prefix = "<p>I can't give personal medical advice. Please speak to a doctor or pharmacist. Here is what the prescribing information says in general:</p>";
      }
      var commercial = COMMERCIAL.test(q);
      var tail = commercial
        ? '<p>Supply, registration and commercial questions are answered by our partnering team. <a href="' + enquiryLink() + '">Send an enquiry</a> with your market and what you need.</p>'
        : "";

      if (ENDPOINT && hits.length) {
        return fetch(ENDPOINT, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            question: q,
            page: location.pathname,
            passages: hits.slice(0, 6).map(function (h) { return { title: h.d.t, url: h.d.u, text: h.d.x }; })
          })
        }).then(function (r) {
          if (!r.ok) throw new Error(r.status);
          return r.json();
        }).then(function (res) {
          var body = String(res.answer || "").split(/\n{2,}/).map(function (p) { return "<p>" + esc(p) + "</p>"; }).join("");
          wait.innerHTML = prefix + body + tail + sourcesHtml(hits.slice(0, 4));
        }).catch(function () { localAnswer(); });
      }
      localAnswer();

      function localAnswer() {
        if (!hits.length || hits[0].s < 1.5) {
          wait.innerHTML = prefix + "<p>I couldn't find that in our molecule library. The partnering team can help with molecules and questions that aren't covered here.</p>" +
            '<p><a href="' + ROOT + 'contact.html">Contact the partnering team</a> or <a href="' + ROOT + 'products.html">browse all molecules</a>.</p>';
          return;
        }
        if (commercial) {
          var page = hits.named.length && hits.filter(function (h) { return h.d.m === hits.named[0]; })[0];
          wait.innerHTML = prefix + tail + (page
            ? '<p>Meanwhile, the <a href="' + esc(ROOT + page.d.u.split("#")[0]) + '">' + esc(page.d.m) + " page</a> has its key facts and approval history.</p>"
            : '<p>You can also <a href="' + ROOT + 'products.html">browse all molecules</a> first.</p>');
          return;
        }
        var top = hits[0];
        var parts = ["<p>" + esc(bestSentences(top.d.x, q, 2)) + "</p>"];
        var second = hits[1];
        if (second && second.s >= top.s * 0.6 && second.d.m === top.d.m && second.d.u !== top.d.u) {
          parts.push("<p>" + esc(bestSentences(second.d.x, q, 2)) + "</p>");
        }
        wait.innerHTML = prefix + parts.join("") + tail + sourcesHtml(hits);
      }
    }).catch(function () {
      wait.innerHTML = '<p>The assistant could not load. <a href="' + ROOT + 'contact.html">Contact the partnering team</a> instead.</p>';
    });
  };

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var q = field.value;
    field.value = "";
    ask(q);
  });
})();
