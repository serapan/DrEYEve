import Vue from 'vue';
import Vuex from 'vuex';
import { IHttpClient, createHttpClient } from '@/http-client/HttpClientFactory';
import User from '@/models/User';
import Route from '@/models/Route';
import Profile from '@/models/Profile';

Vue.use(Vuex);

const httpClient: IHttpClient = createHttpClient();

class State {
    public users: Array<User>=[];
    public user: User|null=null;
    public routes: Array<Route>=[];
    public route: Route|null=null;
    public usersCounts: Profile|null=null;
    public allUsersProfile: Profile|null=null;
}

export default new Vuex.Store({
    state: new State(),
    getters: {
        getActiveRoutes(state: State): Array<Route>{
            return state.routes.filter(x => x.is_active);
        }
    },
    mutations: {
        updateUsers(state, users) {
            state.users = users.map((x: any) => new User(x));
        },
        updateUser(state, user) {
            state.user = new User(user);
        },
        updateRoutes(state, routes) {
            state.routes = routes.map((x: any) => new Route(x));
        },
        updateRoute(state, route) {
            state.route = new Route(route);
        },
        updateUsersCounts(state, profile) {
            state.usersCounts = new Profile(profile);
        },
        updateAllUsersProfile(state, profile) {
            state.allUsersProfile = new Profile(profile);
        }
    },
    actions: {
        async getUsers({ commit }) {
            const response = await httpClient.get('users');
            commit('updateUsers', response.data.users);
        },
        async getUser({ commit }, userId) {
            const url = `users/${userId}?include_routes&include_scores&include_profile`;
            const response = await httpClient.get(url);
            commit('updateUser', response.data);
        },
        async getRoutes({ commit }) {
            const response = await httpClient.get('routes');
            commit('updateRoutes', response.data.routes);
        },
        async getRoute({ commit }, routeParams) {
            const userId = routeParams.user_id;
            const routeId = routeParams.route_id;
            const url = `users/${userId}/routes/${routeId}?include_labels&include_score`;
            const response = await httpClient.get(url);
            commit('updateRoute', response.data);
        },
        async getUsersCounts({ commit }) {
            const response = await httpClient.get('stats/users');
            commit('updateUsersCounts', response.data);
        },
        async getAllUsersProfile({ commit }) {
            const response = await httpClient.get('stats/routes');
            commit('updateAllUsersProfile', response.data);
        }
    }
});
