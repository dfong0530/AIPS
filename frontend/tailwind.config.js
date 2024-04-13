/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    colors: {
      red: {
        default: '#FF3500',
        bg: '#DA2D00'
      },
      gray: {
        default: '#2e2d2d',
        light: '#CFCFCF',
        bg: '#5E5E5E'
      },
      white: {
        default: '#FFFFFF'
      }
    }
  },
  plugins: [],
}

