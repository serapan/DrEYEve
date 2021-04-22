<template>
    <div class="hello-world">
        <h1>{{ message }}</h1>
    </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';

@Component({
    name: 'HelloWorld'
})
export default class HelloWorld extends Vue {
    @Prop({ default: 'Hello World!' })
    private message?: string;
}
</script>
