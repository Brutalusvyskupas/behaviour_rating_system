module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  }, 
  purge: {
      enabled: false, //true for production build
      content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html'
      ]
  },
  theme: {
    container: {
      center: true,
    },
    extend: {},
  },
  variants: {
    display: ['responsive', 'group-hover', 'group-focus'],
  },
  plugins: [],
}
