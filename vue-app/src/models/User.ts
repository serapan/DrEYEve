import Profile from '@/models/Profile';
import Route from '@/models/Route';

export default class User {
    public user_id: number = 0;
    public firstname: string = '';
    public lastname: string = '';
    public profile?: Profile;
    public routes?: Array<Route>;
    public constructor(options: any = null) {
        if (options) {
            this.user_id = options.user_id || 0;
            this.firstname = options.firstname || '';
            this.lastname = options.lastname || '';
            this.profile = new Profile(options.profile);
            this.routes = options.routes?.map((x: any) => new Route(x));
        }
    }
}
