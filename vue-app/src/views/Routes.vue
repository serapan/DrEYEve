<template>
    <div class="routes" v-if="availRoutes">
        <v-card>
            <v-card-title>
                <v-container fill-height fluid>
                    <v-row align="start" justify="start">
                        <v-col cols="auto"> Routes </v-col>
                        <v-col cols="auto">
                            <v-dialog
                                ref="startDialog"
                                v-model="startModal"
                                :return-value.sync="startDate"
                                persistent
                                width="290px"
                            >
                                <template v-slot:activator="{ on, attrs }">
                                    <v-text-field
                                        v-model="startDate"
                                        label="Date From"
                                        prepend-icon="calendar_today"
                                        readonly
                                        v-bind="attrs"
                                        v-on="on"
                                    ></v-text-field>
                                </template>
                                <v-date-picker v-model="startDate" scrollable>
                                    <v-spacer></v-spacer>
                                    <v-btn text color="primary" @click="startModal = false"> Cancel </v-btn>
                                    <v-btn text color="primary" @click="$refs.startDialog.save(startDate)"> OK </v-btn>
                                    <v-btn text color="primary" @click="startDate = ''"> RESET </v-btn>
                                </v-date-picker>
                            </v-dialog>
                        </v-col>
                        <v-col cols="auto">
                            <v-dialog
                                ref="endDialog"
                                v-model="endModal"
                                :return-value.sync="endDate"
                                persistent
                                width="290px"
                            >
                                <template v-slot:activator="{ on, attrs }">
                                    <v-text-field
                                        v-model="endDate"
                                        label="Date To"
                                        prepend-icon="calendar_today"
                                        readonly
                                        v-bind="attrs"
                                        v-on="on"
                                    ></v-text-field>
                                </template>
                                <v-date-picker v-model="endDate" scrollable>
                                    <v-spacer></v-spacer>
                                    <v-btn text color="primary" @click="endModal = false"> Cancel </v-btn>
                                    <v-btn text color="primary" @click="$refs.endDialog.save(endDate)"> OK </v-btn>
                                    <v-btn text color="primary" @click="endDate = ''"> RESET </v-btn>
                                </v-date-picker>
                            </v-dialog>
                        </v-col>
                        <v-col cols="5">
                            <v-text-field v-model="filterText" prepend-icon="search"> </v-text-field>
                        </v-col>
                        <v-col cols="auto">
                            <v-menu v-model="optionsMenu" :close-on-content-click="true" :nudge-width="200" offset-x>
                                <template v-slot:activator="{ on, attrs }">
                                    <v-btn color="indigo" dark v-bind="attrs" v-on="on"> Options </v-btn>
                                </template>
                                <v-list>
                                    <v-list-item>
                                        <v-list-item-action>
                                            <v-switch v-model="activeRoutes" color="purple"></v-switch>
                                        </v-list-item-action>
                                        <v-list-item-title>Show only active routes</v-list-item-title>
                                    </v-list-item>
                                </v-list>
                            </v-menu>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card-title>
            <v-data-table
                :headers="headers"
                :items="filteredRoutes"
                :items-per-page="10"
                item-key="user.firstname"
                class="elevation-1"
            >
                <template v-slot:[`item.date`]="{ item }">
                    {{ item.date }}
                    <router-link
                        class="nav-link"
                        :to="{
                            name: 'Route',
                            params: {
                                user_id: item.user.user_id,
                                route_id: item.route_id
                            }
                        }"
                        style="margin-left: 100px"
                    >
                        <v-btn depressed small>
                            View Route
                            <v-icon color="orange darken-4" right>open_in_new</v-icon>
                        </v-btn>
                    </router-link>
                    <router-link
                        class="nav-link"
                        :to="{
                            name: 'ActiveRoute',
                            params: {
                                user_id: item.user.user_id,
                                route_id: item.route_id
                            }
                        }"
                        style="margin-left: 70px"
                    >
                        <v-btn v-if="item.is_active==1" depressed small>
                            Watch Live
                            <v-icon color="orange darken-4" right>live_tv</v-icon>
                        </v-btn>
                    </router-link>
                </template>
            </v-data-table>
        </v-card>
    </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import Route from '@/models/Route';
import RouteListItem from '@/components/RouteListItem.vue';
import dayjs from 'dayjs';

@Component({
    name: 'Routes',
    components: {
        RouteListItem
    }
})
export default class Routes extends Vue {
    public filterText: string = '';
    public startDate: string = '';
    public startModal: boolean = false;
    public endDate: string = '';
    public endModal: boolean = false;
    public optionsMenu: boolean = false;
    public activeRoutes: boolean = false;
    private headers: Array<any> = [
        { text: 'Firstname', value: 'user.firstname' },
        { text: 'Lastname', value: 'user.lastname' },
        { text: 'Date', value: 'date' }
    ];
    created() {
        this.$store.dispatch('getRoutes');
    }
    get availRoutes(): Array<Route> {
        if (this.activeRoutes) {
            return this.$store.state.routes.filter((x: Route) => {
                if (this.activeRoutes) {
                    if (!x.is_active) {
                        return false;
                    }
                }
                return true;
            });
        }
        return this.$store.state.routes;
    }
    get filteredRoutes(): Array<Route> {
        if (!this.filterText && !this.startDate && !this.endDate) {
            return this.availRoutes;
        }
        const queryText = this.filterText.toLowerCase();
        return this.availRoutes.filter((x) => {
            if (this.filterText) {
                if (
                    !x.user?.firstname.toLowerCase().includes(queryText) &&
                    !x.user?.lastname.toLowerCase().includes(queryText)
                )
                    return false;
            }
            const dX = dayjs(x.date, 'YYYY-MM-DD');
            if (this.startDate) {
                const dStart = dayjs(this.startDate + 'T00:00:00', 'YYYY-MM-DDTHH:mm:ss');
                if (dX < dStart) {
                    return false;
                }
            }
            if (this.endDate) {
                const dEnd = dayjs(this.endDate + 'T23:59:59', 'YYYY-MM-DDTHH:mm:ss');
                if (dX > dEnd) {
                    return false;
                }
            }
            return true;
        });
    }
}
</script>

<style>
</style>