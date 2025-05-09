module.exports = {
    purge: ['./templates/**/*.html', './static/**/*.js'], // Adjust paths as needed
    darkMode: false, // or 'media' or 'class'
    theme: {
      extend: {
        colors: {
          'primary': '#eb2128',
          'secondary': '#151314',
          'third': "#090a1a",
        },
        animation: {
          scroll:
            "scroll var(--animation-duration, 40s) var(--animation-direction, forwards) linear infinite",
        },
        keyframes: {
          scroll: {
            to: {
              transform: "translate(calc(-50% - 0.5rem))",
            },
          },
        },
      },
    },
    variants: {
        extend: {},
    },
    plugins: [],
  };