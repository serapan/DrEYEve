<template>
    <canvas ref="prof" id="prof" width="600px" height="220px" />
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator';
import Chart from 'chart.js';
import Profile from '@/models/Profile';

@Component({
    name: 'ProfileChart'
})
export default class ProfileChart extends Vue {
    @Prop()
    public profile!: Profile;
    @Prop()
    public type!: string;
    @Prop()
    public title!: string;
    public labels: Array<string> = [
        'NORMAL',
        'SLIGHTLY AGGRESSIVE',
        'FAIRLY AGGRESSIVE',
        'HIGHLY AGGRESSIVE',
        'EXTREMELY AGGRESSIVE'
    ];
    public scales: any = {};
    get profileDataAsArray(): Array<number> {
        if (this.type == 'doughnut') {
            return [
                Math.round(this.profile.normal * 10000) / 100,
                Math.round(this.profile.slightly_aggressive * 10000) / 100,
                Math.round(this.profile.fairly_aggressive * 10000) / 100,
                Math.round(this.profile.highly_aggressive * 10000) / 100,
                Math.round(this.profile.extremely_aggressive * 10000) / 100
            ];
        } else {
            this.scales = {
                yAxes: [
                    {
                        ticks: {
                            beginAtZero: true
                        }
                    }
                ]
            };
            return [
                this.profile.normal,
                this.profile.slightly_aggressive,
                this.profile.fairly_aggressive,
                this.profile.highly_aggressive,
                this.profile.extremely_aggressive
            ];
        }
    }
    createBar(params: any): void {
        const canvas = this.$refs.prof as HTMLCanvasElement;
        new Chart(canvas, params);
    }
    mounted(): void {
        this.createBar({
            type: this.type,
            data: {
                labels: this.labels,
                datasets: [
                    {
                        label: '',
                        data: this.profileDataAsArray,
                        backgroundColor: [
                            'rgba(0, 230, 64, 0.8)',
                            'rgba(255, 203, 5, 0.8)',
                            'rgba(248, 148, 6, 0.8)',
                            'rgba(242, 38, 19, 0.8)',
                            'rgba(207, 0, 15, 0.8)'
                        ],
                        borderColor: [
                            'rgba(0, 230, 64, 1)',
                            'rgba(255, 203, 5, 1)',
                            'rgba(248, 148, 6, 1)',
                            'rgba(242, 38, 19, 1)',
                            'rgba(207, 0, 15, 1)'
                        ],
                        borderWidth: 1
                    }
                ]
            },
            options: {
                title: {
                    display: true,
                    fontSize: 24,
                    fontColor: 'rgba(0, 0, 0, 1)',
                    text: this.title
                },
                scales: this.scales
            }
        });
    }
}
</script>