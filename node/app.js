const express = require('express');
const config = require('./conf/config');
const cors = require('cors');

let app = express();
app.options('*', cors());

let expressWs = require('express-ws')(app);
let server = app.listen(config.port);

require('./conf/express')(app, config, server);

app.listen(config.port, function () {
  console.log('Server listening on port:', config.port);
  var socket = require('./conf/sock')(app, server);
  //require('./modules/github')(socket, 'b88af26d794446443e7a1f835846d6e0a64f7ed5');
});
