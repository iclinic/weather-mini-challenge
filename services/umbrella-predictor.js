const CacheService = require('./cache-service');
const Utils = require('../utils');

/**
 * UmbrellaPredictor class
 * 
 * @author Siderlan Santos
 * @since 1.0.0
 */
class UmbrellaPredictor {
  /**
   * Creates an instance of the class.
   * 
   * @param {*} openWeatherApiClient An instance of OpenWeatherApiClient class.
   */
  constructor(openWeatherApiClient) {
    this.apiClient = openWeatherApiClient;

    // cache for 10 minutes based on update time of
    // OpenWeather API
    const ttl = 60 * 10;
    this._cache = new CacheService(ttl);
  }
  
  /**
   * Retrieve a message that contains a prediction
   * whether you'll need to take an umbrella or not for the next 5 days.
   * 
   * @param {string} cityName The name of the city from which the forecast data is obtained.
   * @param {number} humidityThreshold The humidity threshold to determine if is a rainy day.
   * @param {boolean} flushCache If is true the cache will be invalidated. Default is false.
   */
  async getPrediction(cityName, humidityThreshold, flushCache = false) {
    const cacheKey = `getPrediction_${cityName.replace(/\s/g, '')}`;

    if (flushCache) {
      this._cache.remove(cacheKey);
    }
    
    try {
      const forecastData = await this._cache.get(cacheKey, () => this.apiClient.getForecastByCityName(cityName));
      const rainyForecasts = this._getForecastsWithHighUmidity(forecastData.list, humidityThreshold);
      return this._formatPredictionOutput(cityName, rainyForecasts);
    } catch (err) {
      return `Ops! An unexpected error has occurred: ${err}`;
    }
  }

  /**
   * Select only forecasts that exceeds the humidity threshold.
   * 
   * @param {array} forecasts The forecast data from the OpenWeather API.
   * @param {number} humidityThreshold The humidity threshold to determine if is a rainy day.
   */
  _getForecastsWithHighUmidity(forecasts, humidityThreshold) {
    return forecasts.filter(f => f.main.humidity > humidityThreshold);
  }

  /**
   * Format the message to be displayed.
   * 
   * @param {string} city The name of the city from which the forecast data is obtained.
   * @param {array} data The list with forecasts to be displayed.
   */
  _formatPredictionOutput(city, data) {
    if (data.length === 0) {
      return "You won't need to take an umbrella for the next 5 days."
    }

    // Get the day names from the forecasts dates.
    const rainyDays = data.map(item => {
      const dt = new Date(item.dt)
      return Utils.getDayName(dt.getDay());
    })

    // As well as the forecast data has an interval of three hours
    // we should select only distinct days.
    const distinctDays = [... new Set(rainyDays)];

    // Handling pluralization
    const daySentence = distinctDays.length > 1
      ? 'in these next days'
      : 'on that next day'

    return `You should take an umbrella ${daySentence}: ${distinctDays.join(', ')}`;
  }
}

module.exports = UmbrellaPredictor;