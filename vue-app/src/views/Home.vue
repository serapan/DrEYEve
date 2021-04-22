<template>
    <div class="home">
        <HelloWorld :message="$t('welcomeMessage')" />
        <br><br><br><br>
        <v-img class="white--text align-end" src="img/car.png" width="813" height="307" style="margin-left:auto; margin-right:auto;">
        </v-img>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HelloWorld from '@/components/HelloWorld.vue';

@Component({
    components: {
        HelloWorld
    }
})
export default class Home extends Vue {}
</script>
