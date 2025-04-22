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
          dark: '#653acb',    // une nuance plus foncée
        },
        secondary: '#FF6B6B',
        accent: '#FBBF24',
        customGray: '#6B7280',
        // ajoute d'autres couleurs selon tes besoins
      },
    },
  },
  plugins: [],
}
