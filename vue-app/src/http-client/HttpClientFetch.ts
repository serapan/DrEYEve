import IHttpClient from './IHttpClient';

class HttpClientFetch implements IHttpClient {
    constructor(public readonly baseUrl: string) {
    }

    private handleApiResponse(response): Promise<any> {
        if (!response)
            throw new Error('Invalid response object!');
        let contentType: string = '';
        if (response.headers && response.headers.has('content-type'))
            contentType = response.headers.get('content-type');
        // let isJson: boolean = false;
        let responseContentPromise: Promise<any>;
        if (contentType.includes('application/json')) {
            // isJson = true;
            responseContentPromise = response.json();
        } else {
            responseContentPromise = response.text();
        }
        if (response.ok) {
            return responseContentPromise;
        }
        else {
            return responseContentPromise.then(err => {
                /*
                if (isJson)
                    err = JSON.stringify(err);
                */
                return Promise.reject(err);
            });
        }
    }

    public request(options: any): Promise<any> {
        options = options || {};
        const requestUrl = `${this.baseUrl}/${options.url}`;
        return fetch(requestUrl, options)
            .then(response => this.handleApiResponse(response));
    }

    public get(url: string, options?: any): Promise<any> {
        options = options || {};
        const requestUrl = `${this.baseUrl}/${url}`;
        options.method = 'GET';
        return fetch(requestUrl, options)
            .then(response => this.handleApiResponse(response));
    }

    public post(url: string, data: any, options?: any): Promise<any> {
        options = options || {};
        const requestUrl = `${this.baseUrl}/${url}`;
        options.method = 'POST';
        options.body = JSON.stringify(data);
        return fetch(requestUrl, options)
            .then(response => this.handleApiResponse(response));
    }

    public delete(url: string, options?: any): Promise<any> {
        options = options || {};
        const requestUrl = `${this.baseUrl}/${url}`;
        options.method = 'DELETE';
        return fetch(requestUrl, options)
            .then(response => this.handleApiResponse(response));
    }

    public put(url: string, data: any, options?: any): Promise<any> {
        options = options || {};
        const requestUrl = `${this.baseUrl}/${url}`;
        options.method = 'PUT';
        options.body = JSON.stringify(data);
        return fetch(requestUrl, options)
            .then(response => this.handleApiResponse(response));
    }
}

export default HttpClientFetch;
