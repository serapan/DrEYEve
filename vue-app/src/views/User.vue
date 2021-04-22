<template>
    <div class="user" v-if="user">
        <v-container fill-height fluid>
            <v-row align="start" justify="start">
                <UserListItem :user="user" />
                <v-col cols="1"> </v-col>
                <v-col cols="auto" align-self="start">
                    <v-card class="mx-auto" width="800" max-height="250">
                        <v-card-title class="white--text orange darken-4">
                            Routes Directory
                            <v-spacer></v-spacer>
                            <v-icon>alt_route</v-icon>
                        </v-card-title>
                        <v-virtual-scroll :items="user.routes" item-height="50" max-height="185">
                            <template v-slot:default="{ item }">
                                <v-list-item :key="item.route_id">
                                    <v-icon style="margin-right: 10px">event</v-icon>
                                    <span style="margin-right: 203px">Start Date</span>
                                    <v-list-item-content>
                                        <v-list-item-title>
                                            {{ item.date }}
                                        </v-list-item-title>
                                    </v-list-item-content>
                                    <v-list-item-action>
                                        <router-link
                                            class="nav-link"
                                            :to="{
                                                name: 'Route',
                                                params: {
                                                    user_id: user.user_id,
                                                    route_id: item.route_id
                                                }
                                            }"
                                        >
                                            <v-btn depressed small>
                                                View Route
                                                <v-icon color="orange darken-4" right>open_in_new</v-icon>
                                            </v-btn>
                                        </router-link>
                                    </v-list-item-action>
                                </v-list-item>
                                <v-divider></v-divider>
                            </template>
                        </v-virtual-scroll>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
        <ProfileChart :profile="user.profile" type="doughnut" title="User Profile"/>
    </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import UserListItem from '@/components/UserListItem.vue';
import ProfileChart from '@/components/ProfileChart.vue';

@Component({
    name: 'User',
    components: {
        UserListItem,
        ProfileChart
    }
})
export default class User extends Vue {
    private user: User|null = null;
    async created() {
        await this.$store.dispatch('getUser', this.$route.params.user_id);
        this.user = this.$store.state.user;
    }
}
</script>

<style scoped>
.nav-link {
    text-decoration: none;
    color: inherit;
}
</style>