import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Home from '../views/Home.vue';
import About from '../views/About.vue';
import Users from '../views/Users.vue';
import Routes from '../views/Routes.vue';
import User from '../views/User.vue';
import Route from '../views/Route.vue';
import ActiveRoute from '../views/ActiveRoute.vue';
import Stats from '../views/Stats.vue';
import NotFound from '../views/NotFound.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        component: About
    },
    {
        path: '/users',
        name: 'Users',
        component: Users
    },
    {
        path: '/users/:user_id',
        name: 'User',
        component: User
    },
    {
        path: '/routes',
        name: 'Routes',
        component: Routes
    },
    {
        path: '/users/:user_id/:route_id',
        name: 'Route',
        component: Route
    },
    {
        path: '/active_routes/:user_id/:route_id',
        name: 'ActiveRoute',
        component: ActiveRoute
    },
    {
        path: '/stats',
        name: 'Stats',
        component: Stats
    },
    {
        path: '/:catchAll(.*)',
        name: 'not_found',
        component: NotFound
    }
];

const router = new VueRouter({
    routes
});

export default router;
