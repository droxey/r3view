const express = require("express");
const favicon = require("serve-favicon");
const cookieParser = require("cookie-parser");
const bodyParser = require("body-parser");
const compress = require("compression");
const methodOverride = require("method-override");
const handlebars = require("express-handlebars");
const path = require("path");


module.exports = function(app, config, server) {
  var env = process.env.NODE_ENV || "development";
  app.locals.ENV = env;
  app.locals.ENV_DEVELOPMENT = env == "development";

  app.engine("handlebars", handlebars({ defaultLayout: "main" }));
  app.set("view engine", "handlebars");

  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));
  app.use(cookieParser());
  app.use(compress());
  app.use(express.static(path.join(config.root, 'public')));
  app.use(methodOverride());

  app.use(function(req, res, next) {
    var err = new Error("404: Not Found");
    err.status = 404;
    next(err);
  });

  if (app.get("env") === "development") {
    app.use(function(err, req, res, next) {
      res.status(err.status || 500);
      res.render("error", {
        message: err.message,
        error: err,
        title: "error"
      });
    });
  }

  app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render("error", {
      message: err.message,
      error: {},
      title: "error"
    });
  });
};
