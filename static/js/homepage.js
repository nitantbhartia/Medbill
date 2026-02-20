/* BillKarma Homepage — Vanilla JS Components */

/* --- Autocomplete --- */
function initAutocomplete(inputEl, resultsEl) {
    var timer = null;

    function gradeClass(grade) {
        var map = {A: "ac-grade-a", B: "ac-grade-b", C: "ac-grade-c", D: "ac-grade-d", F: "ac-grade-f"};
        return map[grade] || "ac-grade-na";
    }

    function render(items) {
        if (!items.length) {
            resultsEl.innerHTML = "";
            resultsEl.classList.remove("open");
            return;
        }
        resultsEl.innerHTML = items.map(function (h) {
            var url = "/hospitals/" + h.state_slug + "/" + h.city_slug + "/" + h.slug + "/";
            var badge = h.billing_grade
                ? '<span class="ac-badge ' + gradeClass(h.billing_grade) + '">' + h.billing_grade + '</span>'
                : '';
            return '<a href="' + url + '" class="ac-item">' +
                badge +
                '<span class="ac-info"><span class="ac-name">' + h.name + '</span>' +
                '<span class="ac-loc">' + h.city + ', ' + h.state + '</span></span>' +
                '</a>';
        }).join("");
        resultsEl.classList.add("open");
    }

    function fetchResults() {
        var q = inputEl.value.trim();
        if (q.length < 2) { render([]); return; }
        fetch("/api/hospitals/search?q=" + encodeURIComponent(q) + "&limit=6")
            .then(function (r) { return r.json(); })
            .then(function (json) {
                if (json.status === "ok") render(json.data || []);
            })
            .catch(function () { render([]); });
    }

    inputEl.addEventListener("input", function () {
        clearTimeout(timer);
        timer = setTimeout(fetchResults, 200);
    });

    inputEl.addEventListener("focus", function () {
        if (inputEl.value.trim().length >= 2) fetchResults();
    });

    inputEl.addEventListener("keydown", function (e) {
        var items = resultsEl.querySelectorAll(".ac-item");
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
            if (items[idx]) items[idx].classList.add("active");
        } else if (e.key === "ArrowUp") {
            e.preventDefault();
            if (active) active.classList.remove("active");
            idx = idx <= 0 ? items.length - 1 : idx - 1;
            if (items[idx]) items[idx].classList.add("active");
        } else if (e.key === "Enter") {
            if (active) { e.preventDefault(); window.location.href = active.getAttribute("href"); }
        } else if (e.key === "Escape") {
            render([]);
            inputEl.blur();
        }
    });

    document.addEventListener("click", function (e) {
        if (!inputEl.contains(e.target) && !resultsEl.contains(e.target)) {
            resultsEl.classList.remove("open");
        }
    });
}


/* --- CountUp Animation --- */
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


/* --- Scroll-triggered Animations --- */
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

            if (entry.target.classList.contains("fade-up")) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, {threshold: 0.2});

    document.querySelectorAll("[data-count-target], .fade-up").forEach(function (el) {
        observer.observe(el);
    });
}


/* --- Grade Distribution Bar Animation --- */
function initGradeViz() {
    var bars = document.querySelectorAll(".grade-bar");
    bars.forEach(function (bar, i) {
        var width = bar.getAttribute("data-width");
        setTimeout(function () {
            bar.style.width = width + "%";
        }, 150 + i * 150);
    });
}


/* --- Mobile Nav Toggle --- */
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


/* --- Init --- */
document.addEventListener("DOMContentLoaded", function () {
    var heroInput = document.getElementById("heroSearch");
    var heroResults = document.getElementById("heroResults");
    if (heroInput && heroResults) initAutocomplete(heroInput, heroResults);

    var sampleInput = document.getElementById("sampleSearch");
    var sampleResults = document.getElementById("sampleResults");
    if (sampleInput && sampleResults) initAutocomplete(sampleInput, sampleResults);

    initScrollTriggers();
    initGradeViz();
    initMobileNav();
});
