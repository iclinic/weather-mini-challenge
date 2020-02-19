const express = require('express');
const logger = require('morgan');

require('dotenv').config()

const indexRouter = require('./routes/index');

const app = express();

app.use(logger('dev'));

app.use('/', indexRouter);

module.exports = app;
