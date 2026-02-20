/* Free maps for hospital and comparison pages (Leaflet + OSM).
 * Loads Leaflet only when map containers enter viewport.
 */
(function () {
  "use strict";

  var MAP_SELECTOR = ".bk-free-map[data-map-source]";
  var leafletLoadPromise = null;

  function parseJsonScript(id) {
    var el = document.getElementById(id);
    if (!el) return null;
    try {
      return JSON.parse(el.textContent || "{}");
    } catch (_err) {
      return null;
    }
  }

  function loadCss(href) {
    return new Promise(function (resolve, reject) {
      var existing = document.querySelector('link[href="' + href + '"]');
      if (existing) return resolve();
      var link = document.createElement("link");
      link.rel = "stylesheet";
      link.href = href;
      link.onload = function () { resolve(); };
      link.onerror = reject;
      document.head.appendChild(link);
    });
  }

  function loadJs(src) {
    return new Promise(function (resolve, reject) {
      if (window.L) return resolve();
      var existing = document.querySelector('script[src="' + src + '"]');
      if (existing) {
        existing.addEventListener("load", function () { resolve(); }, { once: true });
        existing.addEventListener("error", reject, { once: true });
        return;
      }
      var s = document.createElement("script");
      s.src = src;
      s.async = true;
      s.onload = function () { resolve(); };
      s.onerror = reject;
      document.body.appendChild(s);
    });
  }

  function ensureLeaflet() {
    if (leafletLoadPromise) return leafletLoadPromise;
    leafletLoadPromise = Promise.all([
      loadCss("https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"),
      loadJs("https://unpkg.com/leaflet@1.9.4/dist/leaflet.js")
    ]);
    return leafletLoadPromise;
  }

  function markerHtml(grade, color, isCurrent) {
    var size = isCurrent ? 28 : 22;
    var border = isCurrent ? "3px solid #111827" : "2px solid #ffffff";
    return (
      '<div style="' +
      "width:" + size + "px;" +
      "height:" + size + "px;" +
      "border-radius:9999px;" +
      "background:" + color + ";" +
      "color:#111827;" +
      "font-weight:700;" +
      "font-size:12px;" +
      "line-height:" + (size - 2) + "px;" +
      "text-align:center;" +
      "border:" + border + ";" +
      "box-shadow:0 2px 6px rgba(0,0,0,.2);" +
      '">' + (grade || "N/A") + "</div>"
    );
  }

  function addTileLayer(map) {
    var url = (window.BILLKARMA_MAP_TILE_URL || "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png");
    var attribution = (window.BILLKARMA_MAP_ATTRIBUTION ||
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors');
    var maxZoom = parseInt(window.BILLKARMA_MAP_MAX_ZOOM || "18", 10);
    L.tileLayer(url, { attribution: attribution, maxZoom: maxZoom }).addTo(map);
  }

  function popupHtml(marker) {
    var title = marker.name || "Hospital";
    var grade = marker.grade || "N/A";
    var markup = (marker.avg_markup_vs_medicare !== null && marker.avg_markup_vs_medicare !== undefined)
      ? (Number(marker.avg_markup_vs_medicare).toFixed(1) + "x Medicare")
      : "Markup unavailable";
    var distance = (marker.distance_miles !== null && marker.distance_miles !== undefined)
      ? (Number(marker.distance_miles).toFixed(1) + " miles away")
      : "";
    var link = marker.profile_url
      ? '<div style="margin-top:6px;"><a href="' + marker.profile_url + '" style="color:#1f2937;text-decoration:underline;">View Profile →</a></div>'
      : "";
    return (
      '<div style="font-size:12px;line-height:1.3;">' +
      '<div style="font-weight:700;margin-bottom:4px;">' + title + "</div>" +
      "<div>Grade: <strong>" + grade + "</strong></div>" +
      "<div>" + markup + "</div>" +
      (distance ? "<div>" + distance + "</div>" : "") +
      link +
      "</div>"
    );
  }

  function renderHospitalMap(container, data) {
    var current = data.current;
    if (!current) return;
    var map = L.map(container, { zoomControl: true, scrollWheelZoom: false });
    addTileLayer(map);

    var currentIcon = L.divIcon({
      className: "bk-map-marker",
      html: markerHtml(current.grade, current.grade_color || "#9CA3AF", true),
      iconSize: [28, 28],
      iconAnchor: [14, 14]
    });
    var curr = L.marker([current.lat, current.lon], { icon: currentIcon }).addTo(map);
    curr.bindPopup(popupHtml(current));

    var bounds = L.latLngBounds([[current.lat, current.lon]]);
    (data.nearby || []).forEach(function (item) {
      if (item.lat === null || item.lat === undefined || item.lon === null || item.lon === undefined) return;
      var icon = L.divIcon({
        className: "bk-map-marker",
        html: markerHtml(item.grade, item.grade_color || "#9CA3AF", false),
        iconSize: [22, 22],
        iconAnchor: [11, 11]
      });
      var m = L.marker([item.lat, item.lon], { icon: icon }).addTo(map);
      m.bindPopup(popupHtml(item));
      bounds.extend([item.lat, item.lon]);
    });
    if (bounds.isValid()) {
      map.fitBounds(bounds.pad(0.2), { maxZoom: 14 });
    } else {
      map.setView([current.lat, current.lon], 14);
    }
  }

  function renderCompareMap(container, data) {
    var hs = data.hospitals || [];
    if (hs.length < 2) return;
    var a = hs[0];
    var b = hs[1];
    if (a.lat === null || a.lon === null || b.lat === null || b.lon === null) return;
    var map = L.map(container, { zoomControl: true, scrollWheelZoom: false });
    addTileLayer(map);

    [a, b].forEach(function (item) {
      var icon = L.divIcon({
        className: "bk-map-marker",
        html: markerHtml(item.grade, item.grade_color || "#9CA3AF", true),
        iconSize: [26, 26],
        iconAnchor: [13, 13]
      });
      var m = L.marker([item.lat, item.lon], { icon: icon }).addTo(map);
      m.bindPopup(popupHtml(item));
    });

    var bounds = L.latLngBounds([[a.lat, a.lon], [b.lat, b.lon]]);
    map.fitBounds(bounds.pad(0.25));

    if (data.line && data.line.show) {
      L.polyline([[a.lat, a.lon], [b.lat, b.lon]], {
        color: "#6b7280",
        weight: 2,
        opacity: 0.8,
        dashArray: "6,6"
      }).addTo(map);
      var midLat = (a.lat + b.lat) / 2.0;
      var midLon = (a.lon + b.lon) / 2.0;
      L.marker([midLat, midLon], {
        icon: L.divIcon({
          className: "bk-map-distance",
          html: '<div style="background:#fff;border:1px solid #d1d5db;border-radius:9999px;padding:2px 8px;font-size:11px;color:#111827;">' +
            Number(data.line.distance_miles || 0).toFixed(1) + " mi</div>",
          iconSize: [72, 20],
          iconAnchor: [36, 10]
        })
      }).addTo(map);
    }
  }

  function initContainer(container) {
    if (container.dataset.mapReady === "1") return;
    var sourceId = container.dataset.mapSource;
    var type = container.dataset.freeMap;
    var payload = parseJsonScript(sourceId);
    if (!payload) return;
    ensureLeaflet()
      .then(function () {
        if (!window.L) return;
        if (type === "hospital") renderHospitalMap(container, payload);
        if (type === "compare") renderCompareMap(container, payload);
        container.dataset.mapReady = "1";
      })
      .catch(function (_err) {
        // No-op: fallback text already present for accessibility.
      });
  }

  function boot() {
    var nodes = Array.prototype.slice.call(document.querySelectorAll(MAP_SELECTOR));
    if (!nodes.length) return;
    if (!("IntersectionObserver" in window)) {
      nodes.forEach(initContainer);
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        initContainer(entry.target);
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.1 });
    nodes.forEach(function (n) { observer.observe(n); });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
