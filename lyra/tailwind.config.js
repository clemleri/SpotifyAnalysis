/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  darkMode: 'class', // ← active le dark mode basé sur une classe
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#8a5cf6', // couleur principale par défaut
          light: '#8a5cf6',   // une nuance plus claire
          dark: '#653acb',
          lightDeep: '#301b61',
          darkDeep: '#28184e'    // une nuance plus foncée
        },
        background: {
          DEFAULT: '#0f0f0f',
          darker: '#080808',
          darkBright: '#262629',
        }

        // ajoute d'autres couleurs selon tes besoins
      },
    },
  },
  plugins: [],
}
