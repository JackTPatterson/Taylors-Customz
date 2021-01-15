module.exports = {
    darkMode: false,
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
    purge: {
        enabled: true, //true for production build
        content: [
            '../**/templates/*.html',
            '../**/templates/**/*.html'
        ]
    },
    theme: {
        extend: {
            colors: {
                'primary': '#00B4D8',
                'secondary': '#0096C7',
                'dark': '#023E8A'
            }
        },
    },
    variants: {},
    plugins: [
        require('@tailwindcss/forms'),
    ],
}
