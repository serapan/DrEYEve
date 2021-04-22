<template>
    <div class="stats">
        <div v-if="usersCounts">
            <TotalProfileChart :profile="usersCounts" type="bar" title="Different Profiles Frequency vs Total Users" /><br><br>
        </div>
        <div v-if="allUsersProfile">
            <ProfileChart :profile="allUsersProfile" type="doughnut" title="Average User Profile" />
        </div>
    </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import TotalProfileChart from '@/components/TotalProfileChart.vue';
import ProfileChart from '@/components/ProfileChart.vue';
import Profile from '@/models/Profile';

@Component({
    name: 'Stats',
    components: {
        TotalProfileChart,
        ProfileChart
    }
})
export default class Stats extends Vue {
    private usersCounts: Profile | null = null;
    private allUsersProfile: Profile | null = null;
    async created() {
        await this.$store.dispatch('getUsersCounts');
        this.usersCounts = this.$store.state.usersCounts;
        await this.$store.dispatch('getAllUsersProfile');
        this.allUsersProfile = this.$store.state.allUsersProfile;
    }
}
</script>
<style scoped>
.nav-link {
    text-decoration: none;
    color: inherit;
}
</style>
