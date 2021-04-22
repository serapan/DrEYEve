import { shallowMount, Wrapper } from '@vue/test-utils';
import About from '@/views/About.vue';

describe('About', () => {
    let wrapper: Wrapper<Vue>;

    beforeEach(() => {
        wrapper = shallowMount(About);
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
