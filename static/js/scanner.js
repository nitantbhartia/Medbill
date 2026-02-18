/* ============================================================
   BillKarma - Scanner / File Upload Handler
   Vanilla JS - no frameworks
   ============================================================ */

(function () {
  "use strict";

  // ---- State ----
  let pages = []; // Array of { file: File, dataUrl: string }

  // ---- DOM refs (resolved after DOMContentLoaded) ----
  let dropZone;
  let fileInput;
  let previewContainer;
  let addMoreBtn;
  let scanForm;
  let submitBtn;
  let loadingOverlay;
  let errorMessage;
  let pageCounter;

  // ---- Initialisation ----
  document.addEventListener("DOMContentLoaded", init);

  function init() {
    dropZone = document.getElementById("drop-zone");
    fileInput = document.getElementById("file-input");
    previewContainer = document.getElementById("page-previews");
    addMoreBtn = document.getElementById("add-more-btn");
    scanForm = document.getElementById("scan-form");
    submitBtn = document.getElementById("submit-btn");
    loadingOverlay = document.getElementById("loading-overlay");
    errorMessage = document.getElementById("error-message");
    pageCounter = document.getElementById("page-counter");

    if (!dropZone || !fileInput || !scanForm) return; // Not on the scan page

    // File input change
    fileInput.addEventListener("change", handleFileSelect);

    // Drop zone click opens file picker
    dropZone.addEventListener("click", function () {
      fileInput.click();
    });

    // Drag & drop
    dropZone.addEventListener("dragover", function (e) {
      e.preventDefault();
      dropZone.classList.add("drag-over");
    });

    dropZone.addEventListener("dragleave", function () {
      dropZone.classList.remove("drag-over");
    });

    dropZone.addEventListener("drop", function (e) {
      e.preventDefault();
      dropZone.classList.remove("drag-over");
      var files = e.dataTransfer.files;
      if (files.length) {
        addFiles(files);
      }
    });

    // "Add more pages" button
    if (addMoreBtn) {
      addMoreBtn.addEventListener("click", function () {
        fileInput.click();
      });
    }

    // Form submission
    scanForm.addEventListener("submit", handleSubmit);
  }

  // ---- File handling ----

  function handleFileSelect(e) {
    var files = e.target.files;
    if (files.length) {
      addFiles(files);
    }
    // Reset input so the same file can be re-selected if removed
    fileInput.value = "";
  }

  function addFiles(fileList) {
    for (var i = 0; i < fileList.length; i++) {
      var file = fileList[i];
      if (!file.type.startsWith("image/")) {
        showError("Please upload image files only (JPG, PNG, HEIC, etc.).");
        continue;
      }
      if (file.size > 20 * 1024 * 1024) {
        showError("File \"" + file.name + "\" exceeds the 20 MB limit.");
        continue;
      }
      readAndAddPage(file);
    }
  }

  function readAndAddPage(file) {
    var reader = new FileReader();
    reader.onload = function (e) {
      var page = { file: file, dataUrl: e.target.result };
      pages.push(page);
      renderPreviews();
    };
    reader.readAsDataURL(file);
  }

  function removePage(index) {
    pages.splice(index, 1);
    renderPreviews();
  }

  // ---- Render preview thumbnails ----

  function renderPreviews() {
    if (!previewContainer) return;
    previewContainer.innerHTML = "";

    if (pages.length === 0) {
      // Show the drop zone, hide previews / add-more
      dropZone.style.display = "";
      if (addMoreBtn) addMoreBtn.style.display = "none";
      if (submitBtn) submitBtn.disabled = true;
      if (pageCounter) pageCounter.textContent = "";
      return;
    }

    // Hide the initial drop zone, show the previews area
    dropZone.style.display = "none";
    if (addMoreBtn) addMoreBtn.style.display = "";
    if (submitBtn) submitBtn.disabled = false;
    if (pageCounter) {
      pageCounter.textContent = pages.length + (pages.length === 1 ? " page" : " pages");
    }

    pages.forEach(function (page, idx) {
      var thumb = document.createElement("div");
      thumb.className = "page-thumb";

      var img = document.createElement("img");
      img.src = page.dataUrl;
      img.alt = "Page " + (idx + 1);
      thumb.appendChild(img);

      // Remove button
      var removeBtn = document.createElement("button");
      removeBtn.type = "button";
      removeBtn.className = "remove-btn";
      removeBtn.innerHTML = "&times;";
      removeBtn.title = "Remove page";
      removeBtn.setAttribute("data-index", idx);
      removeBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        var i = parseInt(this.getAttribute("data-index"), 10);
        removePage(i);
      });
      thumb.appendChild(removeBtn);

      // Page number label
      var label = document.createElement("span");
      label.className = "page-label";
      label.textContent = "Page " + (idx + 1);
      thumb.appendChild(label);

      previewContainer.appendChild(thumb);
    });
  }

  // ---- Form submission ----

  function handleSubmit(e) {
    e.preventDefault();
    hideError();

    if (pages.length === 0) {
      showError("Please upload at least one bill image.");
      return;
    }

    // Build FormData
    var formData = new FormData();
    pages.forEach(function (page) {
      formData.append("files", page.file);
    });

    // Optional fields
    var zipInput = document.getElementById("zip-code");
    var emailInput = document.getElementById("email");
    if (zipInput && zipInput.value.trim()) {
      formData.append("zip_code", zipInput.value.trim());
    }
    if (emailInput && emailInput.value.trim()) {
      formData.append("email", emailInput.value.trim());
    }

    // Show loading state
    setLoading(true);

    fetch("/api/scan", {
      method: "POST",
      body: formData,
    })
      .then(function (res) {
        if (!res.ok) {
          return res.json().then(function (body) {
            throw new Error(body.detail || "Upload failed (status " + res.status + ")");
          });
        }
        return res.json();
      })
      .then(function (json) {
        if (json.status === "ok" && json.data && json.data.bill_id) {
          // Redirect to confirm page
          window.location.href = "/confirm/" + json.data.bill_id;
        } else {
          throw new Error("Unexpected response from server.");
        }
      })
      .catch(function (err) {
        setLoading(false);
        showError(err.message || "Something went wrong. Please try again.");
      });
  }

  // ---- Loading state ----

  function setLoading(on) {
    if (loadingOverlay) {
      if (on) {
        loadingOverlay.classList.add("active");
      } else {
        loadingOverlay.classList.remove("active");
      }
    }
    if (submitBtn) {
      submitBtn.disabled = on;
    }
  }

  // ---- Error display ----

  function showError(msg) {
    if (!errorMessage) return;
    var textEl = errorMessage.querySelector(".error-text") || errorMessage;
    textEl.textContent = msg;
    errorMessage.classList.add("visible");

    // Auto-dismiss after 8 seconds
    clearTimeout(errorMessage._timer);
    errorMessage._timer = setTimeout(hideError, 8000);
  }

  function hideError() {
    if (!errorMessage) return;
    errorMessage.classList.remove("visible");
  }
})();
