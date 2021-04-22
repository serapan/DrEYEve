const path = require('path');
const express = require('express');
const compression = require('compression');

const cachingMaxAge = process.env.CACHING_MAXAGE !== undefined ? process.env.CACHING_MAXAGE : 0;
const cachingETag = process.env.CACHING_ETAG !== undefined ? (process.env.CACHING_ETAG === 'true') : true;
const cachingLastModified = process.env.CACHING_LASTMODIFIED !== undefined ? (process.env.CACHING_LASTMODIFIED === 'true') : true;
const port = process.env.PORT || 8080;
let serveRootPath = process.env.SERVER_ROOT_PATH || './dist';
if (process.argv && process.argv.length > 2) {
    serveRootPath = process.argv[2];
}

const app = express();

app.use(compression());

app.use(express.static(path.join(__dirname, serveRootPath), {
    etag: cachingETag,
    lastModified: cachingLastModified,
    maxAge: cachingMaxAge * 1000,
    setHeaders: function (res, path) {
        if (path.endsWith('service-worker.js'))
            res.set('Cache-Control', 'public, max-age=0');
    }
}));


app.listen(port, () => {
    console.log('Caching MaxAge:', cachingMaxAge);
    console.log('Caching ETag:', cachingETag);
    console.log('Caching LastModified:', cachingLastModified);
    console.log(`Express server (${serveRootPath}) listening at port ${port} ... `);
});
