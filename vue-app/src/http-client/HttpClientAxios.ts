import IHttpClient from './IHttpClient';
import axios from 'axios';

class HttpClientAxios implements IHttpClient {
    constructor(public readonly baseUrl: string) {
    }

    public request(options: any): Promise<any> {
        options = options || {};
        options.url = `${this.baseUrl}/${options.url}`;
        return axios(options);
    }

    public get(url: string, options?: any): Promise<any> {
        const requestUrl = `${this.baseUrl}/${url}`;
        return axios.get(requestUrl, options);
    }

    public post(url: string, data: any, options?: any): Promise<any> {
        options = options || {};
        const requestUrl = `${this.baseUrl}/${url}`;
        options.data = data;
        return axios.post(requestUrl, options);
    }

    public delete(url: string, options?: any): Promise<any> {
        const requestUrl = `${this.baseUrl}/${url}`;
        return axios.delete(requestUrl, options);
    }

    public put(url: string, data: any, options?: any): Promise<any> {
        options = options || {};
        const requestUrl = `${this.baseUrl}/${url}`;
        options.data = data;
        return axios.put(requestUrl, options);
    }
}

export default HttpClientAxios;
