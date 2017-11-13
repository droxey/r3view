var SockjsClient = require('sockjs-client');
var createClientChannel = require('sock-channels');

clientRootChannel = createClientChannel(new SockjsClient('/ws'));
