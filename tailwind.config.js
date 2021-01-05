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
        colors: {
            'primary': '#0096C7',
            'secondary': '#023E8A',
            'dark': '#03045E'
        }
    },
    variants: {},
    plugins: [
        require('@tailwindcss/forms'),
    ],
}