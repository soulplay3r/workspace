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
      if (!ok) { first.focus(); return; }

      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      data.submitted_at = new Date().toISOString();
      var endpoint = form.getAttribute("data-endpoint");
      status.className = "form-status";
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
})();
