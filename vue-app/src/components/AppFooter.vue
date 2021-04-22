<template>
    <v-footer id="main-app-footer">
        <v-row no-gutters>
            <v-col cols="12" class="d-flex justify-space-between">
                <div>
                    <span>DrEYEve</span>
                    &nbsp;&copy;&nbsp;
                    <span>{{ yearStr }}</span>
                </div>
                <div>
                    <span>{{ dateStr }}</span>
                </div>
            </v-col>
        </v-row>
    </v-footer>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import dayjs from 'dayjs';

@Component({
    name: 'AppFooter'
})
export default class AppFooter extends Vue {
    private get yearStr(): string {
        const d: dayjs.Dayjs = dayjs();
        return d.format('YYYY');
    }

    private get dateStr(): string {
        const d: dayjs.Dayjs = dayjs();
        return d.format('L');
    }
}
</script>
