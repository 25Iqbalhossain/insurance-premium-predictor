/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",  // ✅ এটা না থাকলে Tailwind CSS detect করে না
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
