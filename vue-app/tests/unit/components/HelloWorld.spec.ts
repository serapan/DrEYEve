import { shallowMount, Wrapper } from '@vue/test-utils';
import HelloWorld from '@/components/HelloWorld.vue';

describe('HelloWorld', () => {
    let wrapper: Wrapper<Vue>;
    
    beforeEach(() => {
        wrapper = shallowMount(HelloWorld);
    });
    afterEach(() => {
        wrapper.destroy(); 
    });

    it('should mount', () => {
        expect(wrapper).toBeTruthy();
        expect(wrapper.vm).toBeTruthy();
        expect(wrapper.vm.$el).toBeTruthy();
    });

    it('should render message prop', async () => {
        const message: string = 'new message';
        await wrapper.setProps({ message });
        expect(wrapper.text()).toMatch(message);
    });
});
