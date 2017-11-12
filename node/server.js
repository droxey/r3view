const express = require('express');
const config = require('./config/conf');
const cors = require('cors');

let app = express();
app.options('*', cors());

let expressWs = require('express-ws')(app);
let server = app.listen(config.port);

require('./config/express')(app, config, server);

app.listen(config.port, function () {
  console.log('Server listening on port:', config.port);
  require('./config/sock')(app, server);
});
