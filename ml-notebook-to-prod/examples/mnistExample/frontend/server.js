const express = require('express');
const webpack = require('webpack');
const http = require('http');
const proxy = require('express-http-proxy');
const webpackDevMiddleware = require('webpack-dev-middleware');
const apiHost = process.env.API_HOST || 'http://localhost:8081/'

const app = express();
app.use(require('morgan')('short'));

app.use('/mnist/', proxy(apiHost));
console.log('Proxy set to host ', apiHost);

const webpackConfig = require('./webpack.config.js');
const compiler = webpack(webpackConfig);

app.use(require("webpack-dev-middleware")(compiler, {
    noInfo: true,
    publicPath: webpackConfig.output.publicPath
}));

app.use(require("webpack-hot-middleware")(compiler, {
    log: console.log,
    path: '/__webpack_hmr',
    heartbeat: 10 * 1000
}));

let server = http.createServer(app);
server.listen(process.env.PORT || 4444, function () {
    console.log("Listening on %j", server.address());
});
