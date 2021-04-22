import Vue from 'vue';
import Vuetify from 'vuetify';
import { shallowMount, Wrapper } from '@vue/test-utils';
import AppFooter from '@/components/AppFooter.vue';

Vue.use(Vuetify);

describe('AppFooter', () => {
    let vuetify: Vuetify;
    let wrapper: Wrapper<Vue>;

    beforeEach(() => {
        vuetify = new Vuetify();
        wrapper = shallowMount(AppFooter, {
            vuetify,
            mocks: {
                $t: (key: string) => {
                    return key;
                }
            }
        });
    });

    afterEach(() => {
        wrapper.destroy();
    });

    it('should mount', () => {
        expect(wrapper).toBeTruthy();
        expect(wrapper.vm).toBeTruthy();
        expect(wrapper.vm.$el).toBeTruthy();
    });

    it('should have footer', () => {
        expect(wrapper.find('#main-app-footer').exists()).toEqual(true);
    });
});