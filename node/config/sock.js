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

    sockJSEcho.on('connection', function(conn) {
        conn.write("[info] Server WebSocket connection established.");
        clientID = conn.id;
        clients[clientID] = conn;

        conn.on('data', function(message) {
            conn.write('[info] Server received data:', JSON.stringify(message));
            switch (message.event) {
              case eventTypes.GH_LOAD_TREE:
                require('./github')(
                  conn,
                  message.token,
                  message.data.username,
                  message.data.repo,
                  message.data.branch);
                break;
              case eventTypes.GH_USER_SELECT_FILE:
                break;
              case eventTypes.CHAT_SEND_MESSAGE:
                break;
              case eventTypes.CHAT_RECEIVED_MESSAGE:
                break;
              case eventTypes.CHAT_LOAD_STREAM:
                break;
              default:
                console.log('Unkown event type:', message.event);
                break;
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
