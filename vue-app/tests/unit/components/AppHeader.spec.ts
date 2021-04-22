import Vue from 'vue';
import Vuetify from 'vuetify';
import { shallowMount, Wrapper } from '@vue/test-utils';
import AppHeader from '@/components/AppHeader.vue';

Vue.use(Vuetify);

describe('AppHeader', () => {
    let vuetify: Vuetify;
    let wrapper: Wrapper<Vue>;

    beforeEach(() => {
        vuetify = new Vuetify();
        wrapper = shallowMount(AppHeader, {
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

    it('should have header', () => {
        expect(wrapper.find('#main-app-header').exists()).toEqual(true);
    });

    it('should contain main nav icon', () => {
        expect(wrapper.find('#main-nav-icon').exists()).toEqual(true);
    });

    it('should contain main logo', () => {
        expect(wrapper.find('#main-logo').exists()).toEqual(true);
    });

    it('should contain main title', () => {
        expect(wrapper.find('#main-title').exists()).toEqual(true);
        expect(wrapper.find('#main-title').text()).toEqual('applicationTitle');
    });

    it('should contain about button', () => {
        expect(wrapper.find('#button-about').exists()).toEqual(true);
    });

    it('should contain main nav drawer', () => {
        expect(wrapper.find('#main-nav-drawer').exists()).toEqual(true);
    });

    it('should contain main nav user', () => {
        expect(wrapper.find('#main-nav-user').exists()).toEqual(true);
    });

    it('should contain main nav items', () => {
        expect(wrapper.find('#main-nav-items').exists()).toEqual(true);
    });

    it('should contain 2 nav items', () => {
        expect(wrapper.find('#main-nav-items .main-nav-item').exists()).toEqual(true);
        expect(wrapper.findAll('#main-nav-items .main-nav-item').length).toEqual(2);
    });

    it('should contain nav item home', () => {
        expect(wrapper.find('#main-nav-items #main-nav-item-home').exists()).toEqual(true);
    });

    it('should contain nav item about', () => {
        expect(wrapper.find('#main-nav-items #main-nav-item-about').exists()).toEqual(true);
    });
});