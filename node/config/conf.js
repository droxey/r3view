const path = require('path');
const rootPath = path.normalize(__dirname + '/..');
const env = process.env.NODE_ENV || 'development';


var config = {
  development: {
    root: rootPath,
    app: {
      name: 'r3view-dev'
    },
    port: process.env.PORT || 7888,
  },
  production: {
    root: rootPath,
    app: {
      name: 'r3view-live'
    },
    port: process.env.PORT || 7888,
  }
};


module.exports = config[env];
