import Point from '@/models/Point';
import Profile from '@/models/Profile';
import User from '@/models/User';

export default class Route {
    public route_id: number = 0;
    public date: string = '';
    public is_active: number = 0;
    public user?: User;
    public profile?: Profile;
    public count?: Profile;
    public points?: Array<Point>;
    public constructor(options: any = null) {
        if (options) {
            this.route_id = options.route_id || 0;
            this.date = options.date || '';
            this.is_active = options.is_active || 0;
            this.user = new User(options);
            this.profile = new Profile (options.score);
            this.count = new Profile (options.count);
            this.points = options.route?.map((x: any) => new Point(x));
        }
    }
}
