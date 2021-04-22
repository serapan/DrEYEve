import { IHttpClient, createHttpClient } from '@/http-client/HttpClientFactory';

describe('HttpClientFactory', () => {
    let client: IHttpClient;

    beforeEach(() => {
        client = createHttpClient();
    });

    it('http client is valid', () => {
        expect(client).toBeTruthy();
    });

    it('http client has baseurl property', () => {
        expect(client.baseUrl).not.toBeUndefined();
        expect(client.baseUrl).not.toBeNull();
    });
});
