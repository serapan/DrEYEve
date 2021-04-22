import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import en from 'vuetify/src/locale/en';
import el from 'vuetify/src/locale/el';
// import i18n from '@/i18n';

Vue.use(Vuetify);

const locale: string = process.env.VUE_APP_I18N_LOCALE || 'en';

const lang: any = {
    locales: { en, el },
    current: locale
    // , t: (key, ...params) => i18n.t(key, params)
};

export default new Vuetify({
    lang,
    icons: {
        iconfont: 'md'
    }
});
