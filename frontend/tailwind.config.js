/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        background: '#FAF7F2',
        surface: '#FFFFFF',
        primary: '#222222',
        secondary: '#717171',
        accent: '#2F6D6A',
        highlight: '#F28C6B',
        border: '#EDE5DA',
        error: '#EF4444',
        star: '#F59E0B',
        rain: '#3B82F6',
      },
      fontFamily: {
        sans: ['"DM Sans"', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        card: '1.125rem',
        pill: '9999px',
      },
      boxShadow: {
        card: '0 4px 24px rgba(34, 34, 34, 0.06)',
        'card-hover': '0 8px 32px rgba(34, 34, 34, 0.1)',
        elevated: '0 8px 30px rgba(34, 34, 34, 0.12)',
        nav: '0 1px 0 rgba(237, 229, 218, 0.8)',
      },
      maxWidth: {
        content: '1280px',
      },
      spacing: {
        18: '4.5rem',
        22: '5.5rem',
      },
    },
  },
  plugins: [],
};
