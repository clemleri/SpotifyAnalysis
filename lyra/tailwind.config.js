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
      screens: {
        'xs': '400px', // 👈 pour cibler les petits écrans précis
      },
      colors: {
        primary: {
          DEFAULT: '#8a5cf6', // couleur principale par défaut
          200: "#e5def7",
          light: '#8a5cf6',   // une nuance plus claire
          dark: '#653acb',
          lightDeep: '#301b61',
          darkDeep: '#28184e'    // une nuance plus foncée
        },
        background: {
          DEFAULT: '#0f0f0f',
          500: '#080808',
          600: '#262629',
        }

        // ajoute d'autres couleurs selon tes besoins
      },
      animation: {
        'fade-in': 'fadeIn 1s ease forwards',
        'fade-in-up': 'fadeInUp 1s ease forwards',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: 0 },
          '100%': { opacity: 1 },
        },
        fadeInUp: {
          '0%': { opacity: 0, transform: 'translateY(20px)' },
          '100%': { opacity: 1, transform: 'translateY(0)' },
        },
      }
    },
  },
  plugins: [
    require('@tailwindcss/line-clamp'),
  ],
}
