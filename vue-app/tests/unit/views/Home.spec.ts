import { shallowMount, Wrapper } from '@vue/test-utils';
import Home from '@/views/Home.vue';

describe('Home', () => {
    let wrapper: Wrapper<Vue>;

    beforeEach(() => {
        wrapper = shallowMount(Home, {
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
});
