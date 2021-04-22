module.exports = {
    filenameHashing: true,
    productionSourceMap: true,
    css: {
        sourceMap: true
    },
    transpileDependencies: [
        'vuetify'
    ],
    pluginOptions: {
        i18n: {
            locale: 'en',
            fallbackLocale: 'en',
            localeDir: 'locales',
            enableInSFC: false
        }
    }
};
