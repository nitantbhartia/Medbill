/* ============================================================
   BillScan - General Application JavaScript
   Vanilla JS - no frameworks
   ============================================================ */

(function () {
  "use strict";

  // ----------------------------------------------------------
  // Currency Formatting
  // ----------------------------------------------------------

  /**
   * Format a number as USD currency: $1,234.56
   * Handles strings, null, undefined gracefully.
   */
  function formatCurrency(value) {
    var num = parseFloat(value);
    if (isNaN(num)) return "$0.00";
    var negative = num < 0;
    num = Math.abs(num);
    var parts = num.toFixed(2).split(".");
    var whole = parts[0];
    var decimals = parts[1];
    // Add commas
    whole = whole.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    return (negative ? "-" : "") + "$" + whole + "." + decimals;
  }

  // Auto-format any element with data-currency attribute on page load
  function formatCurrencyElements() {
    var els = document.querySelectorAll("[data-currency]");
    els.forEach(function (el) {
      var raw = el.getAttribute("data-currency") || el.textContent;
      el.textContent = formatCurrency(raw);
    });
  }

  // Expose globally so other scripts / inline handlers can use it
  window.BillScan = window.BillScan || {};
  window.BillScan.formatCurrency = formatCurrency;

  // ----------------------------------------------------------
  // Copy to Clipboard
  // ----------------------------------------------------------

  /**
   * Copy text to clipboard and show a brief confirmation toast.
   * Attach to buttons via: onclick="BillScan.copyToClipboard(this)"
   * The button should have a data-copy-target attribute pointing
   * to the id of the element whose text should be copied, OR
   * a data-copy-text attribute with literal text.
   */
  function copyToClipboard(triggerEl) {
    var text;
    var targetId = triggerEl.getAttribute("data-copy-target");
    if (targetId) {
      var targetEl = document.getElementById(targetId);
      text = targetEl ? targetEl.innerText : "";
    } else {
      text = triggerEl.getAttribute("data-copy-text") || "";
    }

    if (!text) return;

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        showToast("Copied to clipboard!", "success");
      }).catch(function () {
        fallbackCopy(text);
      });
    } else {
      fallbackCopy(text);
    }
  }

  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.left = "-9999px";
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      showToast("Copied to clipboard!", "success");
    } catch (e) {
      showToast("Failed to copy.", "error");
    }
    document.body.removeChild(ta);
  }

  window.BillScan.copyToClipboard = copyToClipboard;

  // ----------------------------------------------------------
  // Toast Notifications
  // ----------------------------------------------------------

  function showToast(message, type) {
    type = type || "info";
    // Re-use existing toast or create one
    var toast = document.getElementById("app-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "app-toast";
      toast.className = "toast";
      document.body.appendChild(toast);
    }

    toast.textContent = message;
    toast.className = "toast toast-" + type;

    // Force reflow to restart transition
    void toast.offsetWidth;
    toast.classList.add("show");

    clearTimeout(toast._hideTimer);
    toast._hideTimer = setTimeout(function () {
      toast.classList.remove("show");
    }, 3000);
  }

  window.BillScan.showToast = showToast;

  // ----------------------------------------------------------
  // Animated Counter (count-up on page load)
  // ----------------------------------------------------------

  /**
   * Animates elements with class "counter-value" from 0 to their
   * data-target value. Supports integers and currency.
   */
  function animateCounters() {
    var counters = document.querySelectorAll(".counter-value[data-target]");
    if (!counters.length) return;

    var duration = 1800; // ms

    counters.forEach(function (el) {
      var target = parseFloat(el.getAttribute("data-target")) || 0;
      var isCurrency = el.hasAttribute("data-counter-currency");
      var startTime = null;

      // Use easeOutExpo for a satisfying deceleration
      function easeOutExpo(t) {
        return t === 1 ? 1 : 1 - Math.pow(2, -10 * t);
      }

      function step(timestamp) {
        if (!startTime) startTime = timestamp;
        var elapsed = timestamp - startTime;
        var progress = Math.min(elapsed / duration, 1);
        var easedProgress = easeOutExpo(progress);
        var current = easedProgress * target;

        if (isCurrency) {
          el.textContent = formatCurrency(current);
        } else {
          el.textContent = Math.floor(current).toLocaleString();
        }

        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          // Final exact value
          if (isCurrency) {
            el.textContent = formatCurrency(target);
          } else {
            el.textContent = Math.floor(target).toLocaleString();
          }
          // Trigger pulse class briefly
          el.classList.add("counting");
          setTimeout(function () {
            el.classList.remove("counting");
          }, 600);
        }
      }

      // Use IntersectionObserver to start animation when visible
      if ("IntersectionObserver" in window) {
        var observer = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              requestAnimationFrame(step);
              observer.unobserve(el);
            }
          });
        }, { threshold: 0.2 });
        observer.observe(el);
      } else {
        // Fallback: animate immediately
        requestAnimationFrame(step);
      }
    });
  }

  // ----------------------------------------------------------
  // Smooth Scroll to Sections
  // ----------------------------------------------------------

  function initSmoothScroll() {
    // Any link with href starting with # scrolls smoothly
    var links = document.querySelectorAll('a[href^="#"]');
    links.forEach(function (link) {
      link.addEventListener("click", function (e) {
        var targetId = this.getAttribute("href");
        if (targetId === "#") return;
        var target = document.querySelector(targetId);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: "smooth", block: "start" });
          // Update URL hash without jumping
          history.replaceState(null, "", targetId);
        }
      });
    });
  }

  // ----------------------------------------------------------
  // Confirm Page: Inline Edit Line Items
  // ----------------------------------------------------------

  function initConfirmPage() {
    var confirmContainer = document.getElementById("confirm-container");
    if (!confirmContainer) return;

    var billId = confirmContainer.getAttribute("data-bill-id");
    if (!billId) return;

    // Make cells editable on click
    var editableCells = confirmContainer.querySelectorAll(".editable-cell");
    editableCells.forEach(function (cell) {
      cell.addEventListener("click", function () {
        startEditing(cell);
      });
    });

    // Confirm button submits all items
    var confirmBtn = document.getElementById("confirm-btn");
    if (confirmBtn) {
      confirmBtn.addEventListener("click", function () {
        submitConfirmedItems(billId);
      });
    }
  }

  function startEditing(cell) {
    // Prevent double-editing
    if (cell.querySelector("input")) return;

    var currentValue = cell.textContent.trim();
    var field = cell.getAttribute("data-field");
    var row = cell.closest(".line-item-row");
    if (row) row.classList.add("editing");

    var input = document.createElement("input");
    input.type = "text";
    input.value = currentValue;
    // For currency fields, strip the $ and commas for easier editing
    if (field && (field.indexOf("amount") !== -1 || field.indexOf("paid") !== -1 ||
        field.indexOf("adjustment") !== -1 || field.indexOf("responsibility") !== -1)) {
      input.value = currentValue.replace(/[$,]/g, "");
      input.type = "number";
      input.step = "0.01";
    }

    cell.textContent = "";
    cell.appendChild(input);
    input.focus();
    input.select();

    function finishEditing() {
      var newValue = input.value.trim();
      cell.textContent = newValue;
      if (row) row.classList.remove("editing");

      // If it is a currency field, re-format for display
      if (field && (field.indexOf("amount") !== -1 || field.indexOf("paid") !== -1 ||
          field.indexOf("adjustment") !== -1 || field.indexOf("responsibility") !== -1)) {
        var num = parseFloat(newValue);
        if (!isNaN(num)) {
          cell.textContent = formatCurrency(num);
          cell.setAttribute("data-raw-value", num.toFixed(2));
        }
      }
    }

    input.addEventListener("blur", finishEditing);
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        input.blur();
      }
      if (e.key === "Escape") {
        cell.textContent = currentValue;
        if (row) row.classList.remove("editing");
      }
    });
  }

  /**
   * Gather all line items from the confirm table and POST to /api/confirm-items.
   */
  function submitConfirmedItems(billId) {
    var rows = document.querySelectorAll(".line-item-row");
    var items = [];

    rows.forEach(function (row) {
      var item = {};
      var cells = row.querySelectorAll(".editable-cell");
      cells.forEach(function (cell) {
        var field = cell.getAttribute("data-field");
        if (!field) return;

        var raw = cell.getAttribute("data-raw-value") || cell.textContent.trim();
        // Clean currency values
        if (field.indexOf("amount") !== -1 || field.indexOf("paid") !== -1 ||
            field.indexOf("adjustment") !== -1 || field.indexOf("responsibility") !== -1) {
          raw = raw.replace(/[$,]/g, "");
          var num = parseFloat(raw);
          item[field] = isNaN(num) ? null : num;
        } else if (field === "quantity") {
          item[field] = parseInt(raw, 10) || 1;
        } else {
          item[field] = raw || null;
        }
      });

      // Only include rows that have at least a description or CPT code
      if (item.description || item.cpt_code) {
        items.push(item);
      }
    });

    if (items.length === 0) {
      showToast("No line items to confirm.", "error");
      return;
    }

    // Build form data
    var formData = new FormData();
    formData.append("bill_id", billId);
    formData.append("confirmed_items", JSON.stringify(items));

    // Disable button while submitting
    var confirmBtn = document.getElementById("confirm-btn");
    if (confirmBtn) {
      confirmBtn.disabled = true;
      confirmBtn.textContent = "Confirming...";
    }

    fetch("/api/confirm-items", {
      method: "POST",
      body: formData,
    })
      .then(function (res) {
        if (!res.ok) {
          return res.json().then(function (body) {
            throw new Error(body.detail || "Failed to confirm items.");
          });
        }
        return res.json();
      })
      .then(function (json) {
        if (json.status === "ok") {
          showToast("Items confirmed! Redirecting to results...", "success");
          setTimeout(function () {
            window.location.href = "/results/" + billId;
          }, 1200);
        } else {
          throw new Error("Unexpected response.");
        }
      })
      .catch(function (err) {
        showToast(err.message || "Something went wrong.", "error");
        if (confirmBtn) {
          confirmBtn.disabled = false;
          confirmBtn.textContent = "Confirm & Analyze";
        }
      });
  }

  // ----------------------------------------------------------
  // Remove a single line item row on the confirm page
  // ----------------------------------------------------------

  function initRemoveLineItems() {
    document.addEventListener("click", function (e) {
      if (e.target.closest(".remove-line-item")) {
        var btn = e.target.closest(".remove-line-item");
        var row = btn.closest(".line-item-row");
        if (row) {
          row.style.transition = "opacity 0.2s, transform 0.2s";
          row.style.opacity = "0";
          row.style.transform = "translateX(20px)";
          setTimeout(function () {
            row.remove();
            // Update page counter if present
            var remaining = document.querySelectorAll(".line-item-row");
            var counter = document.getElementById("item-count");
            if (counter) {
              counter.textContent = remaining.length + (remaining.length === 1 ? " item" : " items");
            }
          }, 200);
        }
      }
    });
  }

  // ----------------------------------------------------------
  // Bootstrap Everything on DOMContentLoaded
  // ----------------------------------------------------------

  document.addEventListener("DOMContentLoaded", function () {
    formatCurrencyElements();
    animateCounters();
    initSmoothScroll();
    initConfirmPage();
    initRemoveLineItems();
  });
})();
