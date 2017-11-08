var express = require('express');
var router = express.Router();
var sockjs = require('sockjs');


module.exports = function(app, server) {
    app.use('/', router);

    var sockJSEcho = sockjs.createServer();
    sockJSEcho.on('connection', function(conn) {
        conn.write("[info] Server WebSocket connection established.");

        conn.on('data', function(message) {
            for (var c = 0; c < connections.length; c++) {
                connections[c].write("User " + number + " says: " + message);
            }
        });
        conn.on('close', function() {
            for (var c = 0; c < connections.length; c++) {
                connections[c].write("User " + number + " has disconnected");
            }
        });
    });

    sockJSEcho.installHandlers(server,  { prefix: '/echo' });
};
