/* BillKarma Homepage — Procedure-first interactions */

function escapeHtml(s) {
    return String(s || "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

function highlightMatch(text, query) {
    var raw = String(text || "");
    var q = String(query || "").trim();
    if (!q) return escapeHtml(raw);
    var idx = raw.toLowerCase().indexOf(q.toLowerCase());
    if (idx === -1) return escapeHtml(raw);
    var pre = raw.slice(0, idx);
    var match = raw.slice(idx, idx + q.length);
    var post = raw.slice(idx + q.length);
    return escapeHtml(pre) + "<strong>" + escapeHtml(match) + "</strong>" + escapeHtml(post);
}


function initUnifiedSearch(inputEl, resultsEl, formEl) {
    if (!inputEl || !resultsEl) return;

    var timer = null;
    var lastJson = null;

    function hide() {
        resultsEl.classList.remove("open");
    }

    function buildProcedureItem(item, q) {
        return '' +
            '<a class="ac-item" data-selectable="1" href="' + escapeHtml(item.url || ("/procedures/" + item.cpt_code + "/")) + '">' +
                '<div class="ac-info">' +
                    '<span class="ac-name">' + highlightMatch(item.description || item.cpt_code, q) + '</span>' +
                    '<span class="ac-loc">CPT ' + escapeHtml(item.cpt_code || "") + '</span>' +
                '</div>' +
            '</a>';
    }

    function buildFacilityItem(item, q) {
        return '' +
            '<a class="ac-item" data-selectable="1" href="' + escapeHtml(item.url || "#") + '">' +
                '<div class="ac-info">' +
                    '<span class="ac-name">' + highlightMatch(item.name || "", q) + '</span>' +
                    '<span class="ac-loc">' + escapeHtml(item.city || "") + ', ' + escapeHtml(item.state || "") + '</span>' +
                '</div>' +
            '</a>';
    }

    function renderEmpty(q) {
        resultsEl.innerHTML =
            '<div class="ac-empty">No results for "' + escapeHtml(q) + '". ' +
            '<a href="/procedures/">Browse all procedures →</a> or ' +
            '<a href="/hospitals/">Browse all hospitals →</a></div>';
        resultsEl.classList.add("open");
    }

    function render(json, q) {
        var procedures = (json && json.procedures) || [];
        var facilities = (json && json.facilities) || [];
        var html = "";

        if (!procedures.length && !facilities.length) {
            renderEmpty(q);
            return;
        }

        if (procedures.length) {
            html += '<div class="ac-group-title">Procedures</div>';
            for (var i = 0; i < procedures.length; i++) html += buildProcedureItem(procedures[i], q);
        }
        if (facilities.length) {
            html += '<div class="ac-group-title">Hospitals &amp; Facilities</div>';
            for (var j = 0; j < facilities.length; j++) html += buildFacilityItem(facilities[j], q);
        }

        html += '<div class="ac-group-title">Search</div>' +
            '<a class="ac-item ac-search-all" data-selectable="1" href="/search?q=' + encodeURIComponent(q) + '">Search all results for "' + escapeHtml(q) + '"</a>';

        resultsEl.innerHTML = html;
        resultsEl.classList.add("open");
    }

    function smartRoute(q) {
        fetch("/api/search/unified?q=" + encodeURIComponent(q) + "&procedure_limit=5&facility_limit=4")
            .then(function (r) { return r.json(); })
            .then(function (json) {
                var isZip = !!json.is_zip;
                if (json.exact_procedure && json.exact_procedure.url) {
                    window.location.href = json.exact_procedure.url;
                    return;
                }
                if (json.exact_facility && json.exact_facility.url) {
                    window.location.href = json.exact_facility.url;
                    return;
                }
                if (isZip) {
                    window.location.href = "/find/?zip=" + encodeURIComponent(q) + "&type=all";
                    return;
                }
                window.location.href = "/search?q=" + encodeURIComponent(q);
            })
            .catch(function () {
                window.location.href = "/search?q=" + encodeURIComponent(q);
            });
    }

    function fetchResults() {
        var q = inputEl.value.trim();
        if (q.length < 2) {
            hide();
            return;
        }
        fetch("/api/search/unified?q=" + encodeURIComponent(q) + "&procedure_limit=5&facility_limit=4")
            .then(function (r) { return r.json(); })
            .then(function (json) {
                lastJson = json;
                render(json, q);
            })
            .catch(function () {
                hide();
            });
    }

    inputEl.addEventListener("input", function () {
        clearTimeout(timer);
        timer = setTimeout(fetchResults, 180);
    });

    inputEl.addEventListener("focus", function () {
        if (inputEl.value.trim().length >= 2) fetchResults();
    });

    inputEl.addEventListener("keydown", function (e) {
        var items = resultsEl.querySelectorAll(".ac-item[data-selectable='1']");
        if (!items.length) return;
        var active = resultsEl.querySelector(".ac-item.active");
        var idx = -1;
        if (active) {
            for (var i = 0; i < items.length; i++) {
                if (items[i] === active) { idx = i; break; }
            }
        }

        if (e.key === "ArrowDown") {
            e.preventDefault();
            if (active) active.classList.remove("active");
            idx = (idx + 1) % items.length;
            items[idx].classList.add("active");
        } else if (e.key === "ArrowUp") {
            e.preventDefault();
            if (active) active.classList.remove("active");
            idx = idx <= 0 ? items.length - 1 : idx - 1;
            items[idx].classList.add("active");
        } else if (e.key === "Enter") {
            if (active) {
                e.preventDefault();
                window.location.href = active.getAttribute("href");
            } else if (!formEl) {
                var q = inputEl.value.trim();
                if (q) {
                    e.preventDefault();
                    smartRoute(q);
                }
            }
        } else if (e.key === "Escape") {
            hide();
            inputEl.blur();
        }
    });

    document.addEventListener("click", function (e) {
        if (!inputEl.contains(e.target) && !resultsEl.contains(e.target)) hide();
    });

    if (formEl) {
        formEl.addEventListener("submit", function (e) {
            e.preventDefault();
            var q = inputEl.value.trim();
            if (!q) return;

            var active = resultsEl.querySelector(".ac-item.active");
            if (active && active.getAttribute("href")) {
                window.location.href = active.getAttribute("href");
                return;
            }
            smartRoute(q);
        });
    }
}

function countUp(el, target, duration, isDecimal) {
    var prefix = el.getAttribute("data-prefix") || "";
    var suffix = el.getAttribute("data-suffix") || "";
    var startTime = null;

    function step(ts) {
        if (!startTime) startTime = ts;
        var progress = Math.min((ts - startTime) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        var current = target * eased;
        if (isDecimal) {
            el.textContent = prefix + current.toFixed(1) + suffix;
        } else {
            el.textContent = prefix + Math.round(current).toLocaleString() + suffix;
        }
        if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
}

function initScrollTriggers() {
    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (!entry.isIntersecting) return;
            if (entry.target.hasAttribute("data-count-target")) {
                var raw = entry.target.getAttribute("data-count-target");
                var isDecimal = raw.indexOf(".") !== -1;
                var target = parseFloat(raw);
                countUp(entry.target, target, 1500, isDecimal);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    document.querySelectorAll("[data-count-target]").forEach(function (el) {
        observer.observe(el);
    });
}


function initMobileNav() {
    var toggle = document.getElementById("navToggle");
    var menu = document.getElementById("mobileMenu");
    var overlay = document.getElementById("mobileOverlay");
    if (!toggle || !menu) return;

    function open() {
        menu.classList.add("open");
        if (overlay) overlay.classList.add("open");
        document.body.style.overflow = "hidden";
    }
    function close() {
        menu.classList.remove("open");
        if (overlay) overlay.classList.remove("open");
        document.body.style.overflow = "";
    }

    toggle.addEventListener("click", function () {
        menu.classList.contains("open") ? close() : open();
    });
    if (overlay) overlay.addEventListener("click", close);
    menu.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", close);
    });
}

document.addEventListener("DOMContentLoaded", function () {
    initUnifiedSearch(
        document.getElementById("heroSearch"),
        document.getElementById("heroResults"),
        document.getElementById("heroSearchForm")
    );

    initUnifiedSearch(
        document.getElementById("mobileMenuSearch"),
        document.getElementById("mobileMenuResults"),
        null
    );

    initScrollTriggers();
    initMobileNav();
});
