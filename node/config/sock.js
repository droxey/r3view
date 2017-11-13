var express = require('express');
var router = express.Router();
var sockjs = require('sockjs');


module.exports = function(app, server) {
    app.use('/', router);

    var sockJSEcho = sockjs.createServer();
    var clientID;
    var clients = {};
    var eventTypes = {
        GH_LOAD_TREE: 'GH_LOAD_TREE',
        GH_USER_SELECT_FILE: 'GH_USER_SELECT_FILE',
        CHAT_SEND_MESSAGE: 'SEND_CHAT_MESSAGE',
        CHAT_RECEIVED_MESSAGE: 'CHAT_RECEIVED_MESSAGE',
        CHAT_LOAD_STREAM: 'CHAT_LOAD_STREAM',
    };
    var chatStream;

    sockJSEcho.on('connection', function(conn) {
        conn.write("[info] Server WebSocket connection established.");
        clientID = conn.id;
        clients[clientID] = conn;

        conn.on('data', function(message) {
          console.log(JSON.stringify(message))
          // this is where you'd persist it
        });

        conn.on('close', function() {
            conn.write('[info] User disconnected.');
            conn.end();
            delete clients[conn.id];
        });
    });

    sockJSEcho.installHandlers(server,  { prefix: '/echo' });
    return clients[clientID];
};
