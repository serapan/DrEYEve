<template>
    <div class="route" v-if="route">
        <div v-if="route.is_active == 1">
            <v-container fill-height fluid>
                <h3>This is a route that takes place right now. If you want to watch it live, click this button</h3>
                <router-link
                    class="nav-link"
                    :to="{
                        name: 'ActiveRoute',
                        params: {
                            user_id: this.$route.params.user_id,
                            route_id: this.$route.params.route_id
                        }
                    }"
                >
                    <v-btn style="margin-left:15px" depressed small>
                        Watch Live
                        <v-icon color="orange darken-4" right>live_tv</v-icon>
                    </v-btn>
                </router-link>
            </v-container>
        </div>
        <RouteChart :route="route" title="Route Events" /><br /><br />
        <ProfileChart :profile="route.profile" type="doughnut" title="Route Profiling" /><br /><br />
        <ProfileChart :profile="route.count" type="bar" title="Events Count" />
    </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import ProfileChart from '@/components/ProfileChart.vue';
import RouteChart from '@/components/RouteChart.vue';

@Component({
    name: 'Route',
    components: {
        ProfileChart,
        RouteChart
    }
})
export default class Route extends Vue {
    private route: Route | null = null;
    async created() {
        await this.loadData();
    }
    async loadData() {
        await this.$store.dispatch('getRoute', this.$route.params);
        this.route = this.$store.state.route;
    }
}
</script>
<style scoped>
.nav-link {
    text-decoration: none;
    color: inherit;
}
</style>
