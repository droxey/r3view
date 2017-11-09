var express = require('express');
var router = express.Router();
var sockjs = require('sockjs');


module.exports = function(app, server) {
    app.use('/', router);

    var sockJSEcho = sockjs.createServer();

    sockJSEcho.on('connection', function(conn) {
        conn.write("[info] Server WebSocket connection established.");

        conn.on('data', function(message) {
            conn.write('[info] Server received data:', message);
        });

        conn.on('close', function() {
            conn.write('[info] User disconnected.');
        });
    });

    sockJSEcho.installHandlers(server,  { prefix: '/echo' });
};
