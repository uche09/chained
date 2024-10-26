/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        dongle: [
          "Dongle", 
          "sans-serif",
        ]
      }
    },
  },
  plugins: [],
}