<template>
    <div class="route" v-if="route">
        <v-snackbar v-if="route.points && route.points.length>0" v-model="labelBar" :timeout="2000" absolute top right light color="rgba(230, 126, 34, 0.85)" elevation="24">
            <div v-if="route.points[route.points.length - 1].profile" style="font-size:25px; text-align:center">
                {{ route.points[route.points.length - 1].profile }}
            </div>
        </v-snackbar>
        <RouteChart :route="route" title="Route Events" />
    </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import ProfileChart from '@/components/ProfileChart.vue';
import RouteChart from '@/components/RouteChart.vue';

@Component({
    name: 'ActiveRoute',
    components: {
        ProfileChart,
        RouteChart
    }
})
export default class Route extends Vue {
    private route: Route | null = null;
    private intervalHandler: any;
    public labelBar: boolean = false;
    public len: number = 0;
    async created() {
        await this.loadData();
        this.intervalHandler = setInterval(() => {
            this.loadData();
        }, 20000);
    }
    async loadData() {
        await this.$store.dispatch('getRoute', this.$route.params);
        this.route = this.$store.state.route;
        this.labelBar = true;
    }
    beforeDestroy() {
        if (this.intervalHandler) {
            clearInterval(this.intervalHandler);
        }
    }
}
</script>
<style scoped>
.nav-link {
    text-decoration: none;
    color: inherit;
}
</style>
