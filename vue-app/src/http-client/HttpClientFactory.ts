import IHttpClient from './IHttpClient';
import HttpClientAxios from './HttpClientAxios';
import HttpClientFetch from './HttpClientFetch';
import config from '@/config';

const constructorsDict: any = {
    'axios': HttpClientAxios,
    'fetch': HttpClientFetch
};

class HttpClientFactory {
    createHttpClient(baseUrl: string = config.BACKEND_API_URL): IHttpClient {
        const clientConstructor = constructorsDict[config.HTTP_CLIENT_IMPL] || HttpClientAxios;
        return new clientConstructor(baseUrl);
    }
}

const httpClientFactory: HttpClientFactory = new HttpClientFactory();

const createHttpClient = (baseUrl: string = config.BACKEND_API_URL) => httpClientFactory.createHttpClient(baseUrl);

export {
    IHttpClient,
    HttpClientFactory,
    httpClientFactory,
    createHttpClient
};

