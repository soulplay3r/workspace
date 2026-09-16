/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: {
          950: "#0b0d0f",
          900: "#111417",
          800: "#191d22",
          700: "#242a31",
          600: "#3a424c",
          500: "#5a6470",
          400: "#828d99",
          300: "#aab3bd",
          200: "#ced5db",
          100: "#e7eaed",
          50: "#f5f6f7",
        },
        paper: "#faf9f6",
        signal: {
          DEFAULT: "#c65d2e",
          light: "#e07a49",
          dark: "#9c4620",
        },
      },
      fontFamily: {
        serif: ["'Source Serif 4'", "Georgia", "serif"],
        sans: [
          "'Inter'",
          "-apple-system",
          "BlinkMacSystemFont",
          "Segoe UI",
          "sans-serif",
        ],
        mono: ["'IBM Plex Mono'", "ui-monospace", "monospace"],
      },
      maxWidth: {
        content: "72rem",
        prose: "42rem",
      },
    },
  },
  plugins: [],
};
