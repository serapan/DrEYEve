import Vue from 'vue';
import Vuetify from 'vuetify';
import { shallowMount, Wrapper } from '@vue/test-utils';
import App from '@/App.vue';

Vue.use(Vuetify);

describe('App', () => {
    let wrapper: Wrapper<Vue>;

    beforeEach(() => {
        wrapper = shallowMount(App, {
            mocks: {
                $t: (key: string) => {
                    return key;
                }
            },
            stubs: [
                'router-view'
            ]
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
});
