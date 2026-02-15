/* BillScan - Global utilities */
(function () {
  "use strict";

  window.BillScan = window.BillScan || {};

  // Currency formatting
  function formatCurrency(value) {
    var num = parseFloat(value);
    if (isNaN(num)) return "$0.00";
    var neg = num < 0;
    num = Math.abs(num);
    var parts = num.toFixed(2).split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    return (neg ? "-" : "") + "$" + parts[0] + "." + parts[1];
  }

  window.BillScan.formatCurrency = formatCurrency;

  // Toast
  function showToast(message, type) {
    type = type || "info";
    var toast = document.getElementById("app-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "app-toast";
      toast.className = "toast";
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.className = "toast toast-" + type;
    void toast.offsetWidth;
    toast.classList.add("show");
    clearTimeout(toast._t);
    toast._t = setTimeout(function () { toast.classList.remove("show"); }, 3000);
  }

  window.BillScan.showToast = showToast;

  // Copy to clipboard
  function copyToClipboard(triggerEl) {
    var targetId = triggerEl.getAttribute("data-copy-target");
    var text = targetId
      ? (document.getElementById(targetId) || {}).innerText || ""
      : triggerEl.getAttribute("data-copy-text") || "";
    if (!text) return;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        showToast("Copied to clipboard!", "success");
      });
    }
  }

  window.BillScan.copyToClipboard = copyToClipboard;
})();
