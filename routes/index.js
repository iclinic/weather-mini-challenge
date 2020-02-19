const express = require('express');
const router = express.Router();

const OpenWheatherApiClient = require('../services/open-weather-api-client');
const UmbrellaPredictor = require('../services/umbrella-predictor');

const apiClient = new OpenWheatherApiClient(process.env.OPEN_WEATHER_API_APP_ID);
const predictor = new UmbrellaPredictor(apiClient);

/* GET home page. */
router.get('/', function(req, res, next) {
  const CITY_NAME = 'Ribeirao Preto';
  const HUMIDITY_THRESHOLD = 70;

  predictor.getPrediction(CITY_NAME, HUMIDITY_THRESHOLD)
    .then(prediction => res.send(prediction))
    .catch(err => res.send(err));
});

module.exports = router;
