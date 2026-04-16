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
      colors: {
        accent: {
          50:  '#E6F4EA',
          100: '#C8E6D0',
          200: '#8BCFA0',
          300: '#4EB873',
          400: '#00A05E',
          500: '#00824F',
          600: '#00663D',
          700: '#1A1A1A',
          800: '#333333',
          900: '#111111',
        },
        grade: { a: '#00824F', b: '#38A169', c: '#D69E2E', d: '#DD6B20', f: '#E53E3E' },
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'system-ui', 'Segoe UI', 'sans-serif'],
        mono: ['SF Mono', 'Menlo', 'Consolas', 'monospace'],
      }
    }
  },
  plugins: [],
}
