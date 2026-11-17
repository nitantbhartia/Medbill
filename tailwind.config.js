const ink = {
  50: '#EEF0F3', 100: '#E3E6EB', 200: '#C5CCD6', 300: '#8E99A8', 400: '#3B4658',
  500: '#0E1726', 600: '#2B3648', 700: '#0E1726', 800: '#2B3648', 900: '#0E1726',
};
const mark = { 50: '#FFFBE6', 100: '#FFF7CC', 200: '#FFEC8C' };

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js",
  ],
  safelist: [
    // Dynamic color classes used in Python/Jinja
    {pattern: /^(bg|text|border)-(red|green|yellow|amber|blue|gray|accent|grade)-(50|100|200|300|400|500|600|700|800|900)$/},
    {pattern: /^(rounded|px|py|p|m|mt|mb|mx|my|gap|grid-cols|col-span)-/},
    "bg-green-100", "text-green-800", "bg-amber-100", "text-amber-800",
    "bg-red-100", "text-red-800", "bg-gray-100", "text-gray-600",
  ],
  theme: {
    extend: {
      // Older templates use Tailwind colour utilities. These map every family they use onto the
      // site palette in static/css/site.css, so a rebuild matches the hand-written styles.
      colors: {
        accent: ink, blue: ink, emerald: ink, green: ink, purple: ink,
        gray: {
          50: '#F4F5F7', 100: '#E9ECF0', 200: '#E3E6EB', 300: '#C5CCD6', 400: '#8E99A8',
          500: '#5B6676', 600: '#4A5567', 700: '#3B4658', 800: '#2B3648', 900: '#0E1726',
        },
        red: { 50: '#FBECE7', 100: '#F6D6D3', 200: '#ECB2AD', 500: '#B3261E', 600: '#A32E10', 700: '#781813', 800: '#601410' },
        amber: mark, yellow: mark,
        grade: { a: '#00824F', b: '#38A169', c: '#D69E2E', d: '#DD6B20', f: '#E53E3E' },
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        mono: ['IBM Plex Mono', 'ui-monospace', 'Menlo', 'monospace'],
      }
    }
  },
  plugins: [],
}
