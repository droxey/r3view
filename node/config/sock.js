var express = require('express');
var router = express.Router();
var sockjs = require('sockjs');


module.exports = function(app, server) {
    app.use('/', router);

    var sockJSEcho = sockjs.createServer();
    var clientID;
    var clients = {};

    sockJSEcho.on('connection', function(conn) {
        conn.write("[info] Server WebSocket connection established.");
        clientID = conn.id;
        clients[clientID] = conn;
        require('../modules/github')(conn, 'b88af26d794446443e7a1f835846d6e0a64f7ed5');

        conn.on('data', function(message) {
            conn.write('[info] Server received data:', JSON.stringify(message));
              // iterate through each client in clients object
              for (var client in clients) {
                // send the message to that client
                conn.write(message);
              }
        });

        conn.on('close', function() {
            conn.write('[info] User disconnected.');
            delete clients[conn.id];
        });
    });

    sockJSEcho.installHandlers(server,  { prefix: '/echo' });
    return clients[clientID];
};


