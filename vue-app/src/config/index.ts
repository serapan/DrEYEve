export class Config {
    public readonly ARTIFICIAL_NETWORK_DELAY: number = 0;
    public readonly HTTP_CLIENT_IMPL: string = 'axios';
    public readonly BACKEND_API_URL: string = 'http://localhost:8080/api';
}

const config: Config = new Config();

export default config;
