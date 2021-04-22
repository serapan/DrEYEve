<template>
    <div class="route">
        <router-link
            class="nav-link"
            :to="{
                name: 'Route',
                params: {
                    user_id: route.user.user_id,
                    route_id: route.route_id
                }
            }"
        >
            <div class="clickable-route">{{ route.date }}</div>
        </router-link>
    </div>
</template>

<script lang='ts'>
import { Vue, Component, Prop } from 'vue-property-decorator';
import Route from '@/models/Route';

@Component({
    name: 'RouteListItem'
})
export default class RouteListItem extends Vue {
    @Prop()
    public route!: Route;
}
</script>

<style scoped>
.nav-link {
    text-decoration: none;
    color: inherit;
}
</style>