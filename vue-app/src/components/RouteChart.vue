<template>
    <div>
        <canvas ref="canv" id="canv" width="1000px" height="440px" />
        <v-dialog v-model="dialog" width="500">
            <v-card>
                <v-card-title class="headline grey lighten-2"> Specific Route Point Details </v-card-title>
                <v-card-text>
                    Start Time: {{ point.start_time }} (seconds since start)<br />
                    End Time: {{ point.end_time }} (seconds since start)<br />
                    Aggressive Score: {{ point.aggressive_score }}<br />
                    Normal Score: {{ point.normal_score }}<br />
                    Label: {{ point.profile }}
                </v-card-text>
                <v-divider></v-divider>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="dialog = false"> CLOSE </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script lang="ts">
import { Vue, Component, Prop, Watch} from 'vue-property-decorator';
import Chart from 'chart.js';
import Route from '@/models/Route';
import Point from '@/models/Point';

@Component({
    name: 'RouteChart'
})
export default class RouteChart extends Vue {
    @Prop()
    public route!: Route;
    @Watch('route')
    private onRouteChanged(newVal: any, oldVal:any) {
        this.createGraph();
    }
    @Prop()
    public title!: string;
    public dialog: boolean = false;
    public i: number = -1;
    public point?: Point = new Point();
    public colors: any = {
        NORMAL: 'rgba(0, 230, 64, 1)',
        'SLIGHTLY AGGRESSIVE': 'rgba(255, 203, 5, 1)',
        'FAIRLY AGGRESSIVE': 'rgba(248, 148, 6, 1)',
        'HIGHLY AGGRESSIVE': 'rgba(242, 38, 19, 1)',
        'EXTREMELY AGGRESSIVE': 'rgba(207, 0, 15, 0.8)'
    };
    get routeLabelsAsArray(): Array<string> | undefined {
        return this.route.points?.map((x: Point) => x.profile);
    }
    get routeAggressivePointsAsArray(): Array<number> | undefined {
        return this.route.points?.map((x: Point) => x.aggressive_score);
    }
    clickHandler(event: any, elementsAtEvent: any): void {
        if (!elementsAtEvent[0]) {
            return;
        }
        this.i = elementsAtEvent[0]._index;
        this.dialog = true;
        if (!this.route.points) {
            this.point = new Point();
        } else {
            this.point = this.route.points[this.i];
        }
    }
    createLine(params: any): void {
        const canvas = this.$refs.canv as HTMLCanvasElement;
        new Chart(canvas, params);
    }
    createGraph(): void {
        this.createLine({
            type: 'line',
            data: {
                labels: this.routeLabelsAsArray,
                datasets: [
                    {
                        label: '',
                        data: this.routeAggressivePointsAsArray,
                        backgroundColor: 'rgba(0, 0, 0, 0.6)',
                        borderColor: 'rgba(0, 0, 0, 0.6)',
                        pointBackgroundColor: this.routeLabelsAsArray?.map((x) => this.colors[x]),
                        borderWidth: 1
                    }
                ]
            },
            options: {
                onClick: this.clickHandler,
                scales: {},
                title: {
                    display: true,
                    fontSize: 24,
                    fontColor: 'rgba(0, 0, 0, 1)',
                    text: this.title
                },
                animation: {
                    duration: 0
                }
            }
        });
    }
    mounted() {
        this.createGraph();
    }
}
</script>