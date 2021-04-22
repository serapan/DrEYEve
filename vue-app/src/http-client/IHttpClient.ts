interface IHttpClient {
    baseUrl: string;
    request(options: any): Promise<any>;
    get(url: string, options?: any): Promise<any>;
    post(url: string, data: any, options?: any): Promise<any>;
    delete(url: string, options?: any): Promise<any>;
    put(url: string, data: any, options?: any): Promise<any>;
}

export default IHttpClient;
