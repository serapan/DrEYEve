<template>
    <div class="users" v-if="availUsers">
        <v-text-field v-model="filterText" prepend-icon="search"> </v-text-field>
        <v-container fill-height fluid>
            <v-row no-gutters align="start" justify="center">
                <div class="user" v-for="user in filteredUsers" :key="user.user_id">
                    <UserListItem :user="user" />
                </div>
            </v-row>
        </v-container>
    </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import User from '@/models/User';
import UserListItem from '@/components/UserListItem.vue';

@Component({
    name: 'Users',
    components: {
        UserListItem
    }
})
export default class Users extends Vue {
    public filterText: string = '';
    created() {
        this.$store.dispatch('getUsers');
    }
    get availUsers(): Array<User> {
        return this.$store.state.users;
    }
    get filteredUsers(): Array<User> {
        if (!this.filterText) {
            return this.availUsers;
        }
        const queryText = this.filterText.toLowerCase();
        return this.availUsers.filter((x) => {
            if (x.firstname.toLowerCase().includes(queryText)) return true;
            if (x.lastname.toLowerCase().includes(queryText)) return true;
            return false;
        });
    }
}
</script>

<style scoped>
</style>