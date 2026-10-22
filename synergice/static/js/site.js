/* Synergice site enhancements: molecule search, table filter, enquiry forms.
   Every page works without this file; it only adds convenience. */
(function () {
  "use strict";

  // ---------------------------------------------------------- hero search
  var input = document.getElementById("hero-search");
  var list = document.getElementById("hero-results");
  var dataEl = document.getElementById("molecule-index");
  if (input && list && dataEl) {
    var mols = JSON.parse(dataEl.textContent);
    var active = -1;
    var render = function () {
      var q = input.value.trim().toLowerCase();
      list.innerHTML = "";
      active = -1;
      if (!q) { list.hidden = true; input.setAttribute("aria-expanded", "false"); return; }
      var hits = mols.filter(function (m) {
        return m.n.toLowerCase().indexOf(q) !== -1 || m.k.indexOf(q) !== -1 || m.t.toLowerCase().indexOf(q) !== -1;
      }).slice(0, 7);
      if (!hits.length) {
        list.innerHTML = '<li><a href="contact.html"><span>No match. Ask us about “' +
          q.replace(/[<>&"]/g, "") + '”</span><small>Contact →</small></a></li>';
      } else {
        list.innerHTML = hits.map(function (m) {
          return '<li role="option"><a href="' + m.u + '"><span>' + m.n + "</span><small>" + m.t + "</small></a></li>";
        }).join("");
      }
      list.hidden = false;
      input.setAttribute("aria-expanded", "true");
    };
    input.addEventListener("input", render);
    input.addEventListener("keydown", function (ev) {
      var links = list.querySelectorAll("a");
      if (!links.length) return;
      if (ev.key === "ArrowDown" || ev.key === "ArrowUp") {
        ev.preventDefault();
        active = (active + (ev.key === "ArrowDown" ? 1 : -1) + links.length) % links.length;
        links.forEach(function (a, i) { a.setAttribute("aria-selected", i === active ? "true" : "false"); });
      } else if (ev.key === "Enter") {
        ev.preventDefault();
        (links[active] || links[0]).click();
      } else if (ev.key === "Escape") {
        list.hidden = true;
      }
    });
    document.addEventListener("click", function (ev) {
      if (!list.contains(ev.target) && ev.target !== input) list.hidden = true;
    });
  }

  // -------------------------------------------------------- table filter
  document.querySelectorAll("[data-filter]").forEach(function (box) {
    var rows = document.querySelectorAll(box.getAttribute("data-filter"));
    var empty = document.querySelector(".filter-empty");
    box.addEventListener("input", function () {
      var q = box.value.trim().toLowerCase();
      var shown = 0;
      rows.forEach(function (tr) {
        var hit = !q || tr.getAttribute("data-q").indexOf(q) !== -1;
        tr.hidden = !hit;
        if (hit) shown++;
      });
      if (empty) empty.hidden = shown !== 0;
    });
  });

  // ------------------------------------------------------- enquiry forms
  // POSTs JSON to data-endpoint (CRM webhook, Formspree, HubSpot, etc.).
  // Without an endpoint the form validates and explains that nothing was sent.
  document.querySelectorAll("form.enquiry").forEach(function (form) {
    var status = form.querySelector(".form-status");
    var clearErr = function (field) {
      field.classList.remove("invalid");
      var err = field.querySelector(".err");
      if (err) err.remove();
    };
    var setErr = function (field, msg) {
      clearErr(field);
      field.classList.add("invalid");
      var p = document.createElement("p");
      p.className = "err";
      p.textContent = msg;
      field.appendChild(p);
    };
    form.addEventListener("input", function (ev) {
      var f = ev.target.closest(".field");
      if (f) clearErr(f);
    });
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var ok = true;
      var first = null;
      form.querySelectorAll("[required]").forEach(function (el) {
        var field = el.closest(".field");
        var valid = el.type === "checkbox" ? el.checked : el.value.trim() !== "";
        if (valid && el.type === "email") valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value.trim());
        if (!valid) {
          ok = false;
          first = first || el;
          var label = form.querySelector('label[for="' + el.id + '"]');
          var name = label ? label.textContent.replace(/\s*\*\s*$/, "").replace(/\?$/, "") : "This field";
          setErr(field, el.type === "checkbox" ? "Please tick to agree." : el.tagName === "SELECT" ? name + ": choose an option." :
            el.type === "email" && el.value.trim() ? "Enter an email address like name@company.com." :
            name + " is required.");
        }
      });
      if (!ok) {
        var sec = first.closest("details");
        if (sec) sec.open = true;
        first.focus();
        return;
      }
      if (form.hasAttribute("data-netlify-recaptcha")) {
        // Netlify's reCAPTCHA needs a normal (non-script) submission; it then shows thank-you.html.
        form.submit();
        return;
      }

      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      data.submitted_at = new Date().toISOString();
      var endpoint = form.getAttribute("data-endpoint");
      status.className = "form-status";
      if (form.hasAttribute("data-netlify")) {
        var btnN = form.querySelector("button[type=submit]");
        btnN.disabled = true;
        status.textContent = "Sending…";
        fetch("/", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: new URLSearchParams(new FormData(form)).toString() })
          .then(function (res) {
            if (!res.ok) throw new Error(res.status);
            form.reset();
            status.className = "form-status ok";
            status.textContent = "Thank you. Your enquiry has been sent to the Synergice partnering team.";
          })
          .catch(function () {
            status.className = "form-status note";
            status.textContent = "Your enquiry could not be sent. Check your connection and try again.";
          })
          .then(function () { btnN.disabled = false; });
        return;
      }
      if (!endpoint) {
        status.className = "form-status note";
        status.textContent = "Preview build: the enquiry form is not connected to an inbox yet, so this enquiry was not sent. Set FORM_ENDPOINT when building the site to connect it.";
        return;
      }
      var btn = form.querySelector("button[type=submit]");
      btn.disabled = true;
      status.textContent = "Sending…";
      fetch(endpoint, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
        .then(function (res) {
          if (!res.ok) throw new Error(res.status);
          form.reset();
          status.className = "form-status ok";
          status.textContent = "Thank you. Your enquiry has been sent to the Synergice partnering team.";
        })
        .catch(function () {
          status.className = "form-status note";
          status.textContent = "Your enquiry could not be sent. Check your connection and try again.";
        })
        .then(function () { btn.disabled = false; });
    });
  });

  // ------------------------------------------------------- text to speech
  // Browser speech synthesis (no service, no cost). Long text is read in
  // sentence-sized chunks because some browsers stop long utterances early.
  var synth = window.speechSynthesis;
  var Speech = { supported: !!(synth && window.SpeechSynthesisUtterance) };
  var token = 0, queue = [], lit = null, onDone = null, paused = false;
  var pickVoice = function () {
    var vs = synth.getVoices();
    var prefs = ["en-GB", "en-IN", "en-US", "en"];
    for (var i = 0; i < prefs.length; i++) {
      for (var j = 0; j < vs.length; j++) {
        if (vs[j].lang.replace("_", "-").indexOf(prefs[i]) === 0) return vs[j];
      }
    }
    return null;
  };
  var split = function (text) {
    var parts = text.replace(/\s+/g, " ").trim().match(/[^.!?;]+[.!?;]*\s*/g) || [];
    var out = [], cur = "";
    parts.forEach(function (p) {
      if ((cur + p).length > 220 && cur) { out.push(cur.trim()); cur = ""; }
      cur += p;
    });
    if (cur.trim()) out.push(cur.trim());
    return out;
  };
  var highlight = function (el) {
    if (lit) lit.classList.remove("speaking");
    lit = el || null;
    if (lit) {
      lit.classList.add("speaking");
      var r = lit.getBoundingClientRect();
      if (r.top < 80 || r.bottom > window.innerHeight) lit.scrollIntoView({ block: "center", behavior: "smooth" });
    }
  };
  var finish = function () {
    highlight(null);
    paused = false;
    var cb = onDone;
    onDone = null;
    if (cb) cb();
  };
  var next = function (my) {
    if (my !== token) return;
    if (!queue.length) { finish(); return; }
    var it = queue.shift();
    highlight(it.el);
    var u = new SpeechSynthesisUtterance(it.text);
    var v = pickVoice();
    if (v) { u.voice = v; u.lang = v.lang; } else { u.lang = "en-GB"; }
    u.rate = 0.98;
    u.onend = function () { next(my); };
    u.onerror = function () { next(my); };
    synth.speak(u);
  };
  Speech.speakItems = function (items, cb) {
    Speech.stop();
    var my = ++token;
    onDone = cb || null;
    items.forEach(function (it) {
      split(it.text).forEach(function (t) { queue.push({ text: t, el: it.el }); });
    });
    next(my);
  };
  Speech.speak = function (text, cb) { Speech.speakItems([{ text: text }], cb); };
  Speech.stop = function () {
    token++;
    queue = [];
    if (Speech.supported) synth.cancel();
    finish();
  };
  Speech.pause = function () { paused = true; synth.pause(); };
  Speech.resume = function () { paused = false; synth.resume(); };
  Speech.isPaused = function () { return paused; };
  window.SynergiceSpeech = Speech;

  // "Listen to this page" buttons: read the page title, then each heading,
  // paragraph, list item and table row inside the target sections.
  var readable = function (selectors) {
    var items = [];
    var h1 = document.querySelector("h1");
    var sub = document.querySelector(".page-head .sub");
    if (h1) items.push({ text: h1.textContent + ".", el: h1 });
    if (sub) items.push({ text: sub.textContent.replace(/\s*·\s*/g, ", ") + ".", el: sub });
    selectors.split(",").forEach(function (sel) {
      var root = document.querySelector(sel.trim());
      if (!root) return;
      root.querySelectorAll("h2, h3, p, li, tr").forEach(function (el) {
        if (el.closest(".actions, .meta, .page-head, form, nav")) return;
        var text = el.tagName === "TR"
          ? Array.prototype.map.call(el.children, function (c) { return c.textContent.trim(); }).join(": ")
          : el.textContent.trim();
        if (!text || el.closest("thead")) return;
        if (/^H[23]$/.test(el.tagName) || el.tagName === "TR") text += ".";
        items.push({ text: text, el: el.tagName === "H3" && el.closest("summary") ? el.closest("summary") : el });
      });
    });
    return items;
  };
  document.querySelectorAll("button.listen").forEach(function (btn) {
    if (!Speech.supported) return;
    var label = btn.querySelector(".listen-label");
    var stopBtn = btn.parentNode.querySelector(".listen-stop");
    var state = "idle";
    var reset = function () { state = "idle"; label.textContent = "Listen to this page"; stopBtn.hidden = true; };
    btn.hidden = false;
    btn.addEventListener("click", function () {
      if (state === "idle") {
        state = "playing";
        label.textContent = "Pause";
        stopBtn.hidden = false;
        Speech.speakItems(readable(btn.getAttribute("data-listen")), reset);
      } else if (state === "playing") {
        state = "paused";
        label.textContent = "Resume";
        Speech.pause();
      } else {
        state = "playing";
        label.textContent = "Pause";
        Speech.resume();
      }
    });
    stopBtn.addEventListener("click", function () { Speech.stop(); reset(); });
    window.addEventListener("pagehide", function () { Speech.stop(); });
  });

  // ------------------------------------------------------ language menu
  // Uses Google's website translator: the choice is stored in the standard
  // "googtrans" cookie and the translator script is loaded only when needed.
  var langSel = document.getElementById("lang-select");
  var readLang = function () {
    var m = document.cookie.match(/(?:^|;\s*)googtrans=\/[^/]*\/([^;]+)/);
    return m ? decodeURIComponent(m[1]) : "en";
  };
  var setCookie = function (val) {
    var host = location.hostname;
    var expire = val ? "" : "; expires=Thu, 01 Jan 1970 00:00:00 GMT";
    var v = val || "";
    document.cookie = "googtrans=" + v + "; path=/" + expire;
    if (host.indexOf(".") > 0) {
      document.cookie = "googtrans=" + v + "; path=/; domain=" + host + expire;
      document.cookie = "googtrans=" + v + "; path=/; domain=." + host + expire;
    }
  };
  if (langSel) {
    var current = readLang();
    if (langSel.querySelector('option[value="' + current + '"]')) langSel.value = current;
    langSel.addEventListener("change", function () {
      var code = langSel.value;
      setCookie(code === "en" ? "" : "/en/" + code);
      location.reload();
    });
    if (current !== "en") {
      document.documentElement.setAttribute("dir", /^(ar|he|fa|ur)$/.test(current) ? "rtl" : "ltr");
      var holder = document.createElement("div");
      holder.id = "gt-el";
      document.body.appendChild(holder);
      window.synergiceGT = function () {
        new window.google.translate.TranslateElement({ pageLanguage: "en", autoDisplay: false }, "gt-el");
      };
      var sc = document.createElement("script");
      sc.src = "https://translate.google.com/translate_a/element.js?cb=synergiceGT";
      sc.async = true;
      document.body.appendChild(sc);
    }
  }
})();
