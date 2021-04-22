<template>
    <div id="main-app-header">
        <v-app-bar app color="primary" dark>
            <v-app-bar-nav-icon id="main-nav-icon" large @click.stop="toggleDrawer"></v-app-bar-nav-icon>
            <div class="d-flex align-center">
                <v-img
                    id="main-logo"
                    to="/"
                    alt="Logo"
                    class="shrink mx-2"
                    contain
                    src="../assets/logo.svg"
                    transition="scale-transition"
                    :style="{ cursor: 'pointer', 'max-width': '32px', 'max-height': '32px' }"
                    @click="goTo('/')"
                />
            </div>
            <div id="main-title" style="cursor: pointer" @click="goTo('/')">
                <h3>{{ $t('applicationTitle') }}</h3>
            </div>
            <v-spacer></v-spacer>
            <div id="button-about" style="cursor: pointer" @click="goTo('/about')">
                <v-icon large>info_outline</v-icon>
            </div>
        </v-app-bar>
        <v-navigation-drawer id="main-nav-drawer" v-model="drawer" absolute temporary>
            <div id="main-nav-user" class="d-flex justify-space-around align-center py-2">
                <div>
                    <div class="subtitle-2">DrEYEve</div>
                </div>
                <div>
                    <v-btn id="button-nav-drawer-close" icon @click.stop="toggleDrawer">
                        <v-icon middle dark>cancel</v-icon>
                    </v-btn>
                </div>
            </div>
            <v-divider></v-divider>
            <v-list id="main-nav-items" nav dense>
                <v-list-item to="/" id="main-nav-item-home" class="main-nav-item" @click="navItemClick">
                    <v-list-item-icon>
                        <v-icon>home</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>Home</v-list-item-title>
                </v-list-item>
                <v-list-item to="/users" id="main-nav-item-home" class="main-nav-item" @click="navItemClick">
                    <v-list-item-icon>
                        <v-icon>group</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>Users</v-list-item-title>
                </v-list-item>
                <v-list-item to="/routes" id="main-nav-item-home" class="main-nav-item" @click="navItemClick">
                    <v-list-item-icon>
                        <v-icon>alt_route</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>Routes</v-list-item-title>
                </v-list-item>
                <v-list-item to="/stats" id="main-nav-item-home" class="main-nav-item" @click="navItemClick">
                    <v-list-item-icon>
                        <v-icon>query_stats</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>Statistics</v-list-item-title>
                </v-list-item>
                <v-list-item to="/about" id="main-nav-item-about" class="main-nav-item" @click="navItemClick">
                    <v-list-item-icon>
                        <v-icon>info</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>About</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

@Component({
    name: 'AppHeader'
})
export default class AppHeader extends Vue {
    private drawer: boolean = false;

    private toggleDrawer(): void {
        this.drawer = !this.drawer;
    }

    private goTo(target: string): void {
        if (!this.$route || !this.$router) return;
        if (this.$route.path !== target) {
            this.$router.push(target);
        }
    }

    private navItemClick() {
        this.drawer = false;
    }
}
</script>
