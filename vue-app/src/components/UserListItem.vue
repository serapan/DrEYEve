<template>
    <div class="user">
        <router-link
            class="nav-link"
            :to="{
                name: 'User',
                params: {
                    user_id: user.user_id
                }
            }"
        >
            <v-col cols="auto">
                <v-card elevation="14" width="250" height="250">
                    <v-img class="white--text align-end" :src="userImg" width="250" height="250">
                        <v-card-title class="clickable-user">{{ user.lastname }} {{ user.firstname }}</v-card-title>
                    </v-img>
                    <!-- <div class="clickable-user">{{ user.lastname }} {{ user.firstname }}</div> -->
                </v-card>
            </v-col>
        </router-link>
    </div>
</template>

<script lang='ts'>
import { Vue, Component, Prop } from 'vue-property-decorator';
import User from '@/models/User';

@Component({
    name: 'UserListItem'
})
export default class UserListItem extends Vue {
    @Prop()
    public user!: User;
    get userImg(): string {
        if (!this.user) {
            return '';
        }
        return `img/${this.user.user_id}.jpg`;
    }
}
</script>

<style scoped>
.nav-link {
    text-decoration: none;
    color: inherit;
}
</style>