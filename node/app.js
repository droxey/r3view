const express = require('express');
const config = require('./conf/config');
const docsearch = require('./modules/docsearch');

let app = express();
let expressWs = require('express-ws')(app);
let server = app.listen(config.port);

require('./conf/express')(app, config, server);
require('./conf/sock')(app, server);

app.listen(config.port, function () {
  console.log('Server listening on port:', config.port);
  docsearch.searchDocumentation('js date');
});
