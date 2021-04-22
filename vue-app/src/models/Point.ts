export default class Point {
    public score_id: number = 0;
    public start_time: number = 0;
    public end_time: number = 0;
    public aggressive_score: number = 0;
    public normal_score: number = 0;
    public profile: string = '';
    public constructor(options: any = null) {
        if (options) {
            this.score_id = options.score_id || 0;
            this.start_time = options.start_time || 0;
            this.end_time = options.end_time || 0;
            this.aggressive_score = options.aggressive_score || 0;
            this.normal_score = options.normal_score || 0;
            this.profile = options.profile || '';
        }
    }
}
