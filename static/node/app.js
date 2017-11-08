const express = require('express');
const config = require('./conf/config');


let app = express();
let expressWs = require('express-ws')(app);
let server = require('http').createServer(app);


require('./conf/express')(app, config, server);


app.listen(config.port, function () {
  console.log(JSON.stringify(config));
  console.log('Server listening on port:', config.port);
});
