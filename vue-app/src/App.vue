<template>
    <v-app>
        <AppHeader />
        <v-main>
            <v-container fluid>
                <router-view></router-view>
            </v-container>
        </v-main>
        <AppFooter />
    </v-app>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import AppHeader from '@/components/AppHeader.vue';
import AppFooter from '@/components/AppFooter.vue';

@Component({
    name: 'App',
    components: {
        AppHeader,
        AppFooter
    }
})
export default class App extends Vue {}
</script>
