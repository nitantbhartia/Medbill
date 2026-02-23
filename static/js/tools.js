(function () {
  var tool = window.BILLKARMA_TOOL;
  if (!tool) return;

  function byId(id) { return document.getElementById(id); }

  var form = byId('tool-run-form');
  var submitBtn = byId('tool-submit');
  var resultsEl = byId('tool-results');
  var headlineEl = byId('result-headline');
  var summaryEl = byId('result-summary');
  var detailsEl = byId('result-details');
  var ctaBox = byId('result-cta');
  var ctaHeadline = byId('cta-headline');
  var ctaBody = byId('cta-body');
  var ctaPrimary = byId('cta-primary');
  var ctaSecondary = byId('cta-secondary');
  var ctaFootnote = byId('cta-footnote');

  function collectPayload(formEl) {
    var fd = new FormData(formEl);
    var payload = {};
    fd.forEach(function (value, key) {
      payload[key] = value;
    });
    return payload;
  }

  function escapeHtml(text) {
    return String(text || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function renderDetails(details) {
    if (!details || typeof details !== 'object') {
      detailsEl.innerHTML = '<div class="result-kv"><div>No additional details.</div></div>';
      return;
    }

    if (details.letter || details.script) {
      var text = details.letter || details.script;
      detailsEl.innerHTML = '<pre style="white-space:pre-wrap;font-size:0.86rem;line-height:1.45;margin:0;">' + escapeHtml(text) + '</pre>';
      return;
    }

    if (details.decoded_items && Array.isArray(details.decoded_items)) {
      var rows = details.decoded_items.map(function (row) {
        return '<div><strong>' + escapeHtml(row.description) + ':</strong> ' + escapeHtml(row.plain_english) + '</div>';
      }).join('');
      if (details.discrepancies && details.discrepancies.length) {
        rows += '<div style="margin-top:8px;"><strong>Discrepancies:</strong><ul>' + details.discrepancies.map(function (d) { return '<li>' + escapeHtml(d) + '</li>'; }).join('') + '</ul></div>';
      }
      detailsEl.innerHTML = '<div class="result-kv">' + rows + '</div>';
      return;
    }

    var html = '<div class="result-kv">';
    Object.keys(details).forEach(function (key) {
      var value = details[key];
      if (value == null) return;
      if (typeof value === 'object') {
        html += '<div><strong>' + escapeHtml(key.replace(/_/g, ' ')) + ':</strong> <code>' + escapeHtml(JSON.stringify(value)) + '</code></div>';
      } else {
        html += '<div><strong>' + escapeHtml(key.replace(/_/g, ' ')) + ':</strong> ' + escapeHtml(value) + '</div>';
      }
    });
    html += '</div>';
    detailsEl.innerHTML = html;
  }

  function renderResult(result) {
    resultsEl.hidden = false;
    headlineEl.textContent = (result.result_state || '').replace(/_/g, ' ').toUpperCase();
    summaryEl.textContent = result.summary || 'Done.';
    renderDetails(result.details);

    if (result.cta) {
      ctaBox.hidden = false;
      ctaHeadline.textContent = result.cta.headline || '';
      ctaBody.textContent = result.cta.body || '';
      ctaPrimary.textContent = result.cta.primary_label || 'Upload My Bill — Free Audit';
      ctaPrimary.href = result.cta.primary_url || '/scan';

      if (result.cta.secondary_label && result.cta.secondary_url) {
        ctaSecondary.hidden = false;
        ctaSecondary.textContent = result.cta.secondary_label;
        ctaSecondary.href = result.cta.secondary_url;
      } else {
        ctaSecondary.hidden = true;
      }
      if (ctaFootnote) ctaFootnote.textContent = result.cta.footnote || 'Free audit. $29-149 to fight it. No savings? Full refund.';
    }
  }

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var payload = collectPayload(form);
      submitBtn.disabled = true;
      submitBtn.textContent = 'Running...';

      fetch('/api/tools/' + encodeURIComponent(tool.slug) + '/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
      .then(function (res) {
        if (!res.ok) return res.json().then(function (b) { throw new Error(b.detail || 'Tool run failed'); });
        return res.json();
      })
      .then(function (result) {
        renderResult(result);
      })
      .catch(function (err) {
        resultsEl.hidden = false;
        ctaBox.hidden = true;
        headlineEl.textContent = 'ERROR';
        summaryEl.textContent = err.message || 'Could not run tool.';
        detailsEl.innerHTML = '';
      })
      .finally(function () {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Run Tool';
      });
    });
  }

  var leadForm = byId('tool-lead-form');
  var leadStatus = byId('lead-status');
  if (leadForm) {
    leadForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = (byId('lead-email').value || '').trim();
      if (!email) return;

      fetch('/api/tools/lead-capture', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: email,
          tool_slug: tool.slug,
          lead_magnet_key: (tool.lead_magnet && tool.lead_magnet.key) || '',
          context: { source: 'tool_page' }
        })
      })
      .then(function (res) {
        if (!res.ok) return res.json().then(function (b) { throw new Error(b.detail || 'Could not capture lead'); });
        return res.json();
      })
      .then(function () {
        leadStatus.hidden = false;
        leadStatus.textContent = 'Sent. Check your inbox.';
        leadForm.reset();
      })
      .catch(function (err) {
        leadStatus.hidden = false;
        leadStatus.textContent = err.message || 'Could not submit email.';
        leadStatus.style.color = '#991b1b';
      });
    });
  }
})();
