const axios = require('axios');

/**
 * A client class for OpenWheather API.
 * 
 * @author Siderlan Santos
 * @uses axios
 */
class OpenWeatherApiClient {
  /**
   * Creates an instance of OpenWheatherApi
   * 
   * @param {*} appId 
   */
  constructor(appId) {
    this.appId = appId;

    this.axios = axios.create({
      baseURL: 'http://api.openweathermap.org/data/2.5'
    });
  }

  /**
   * Perform an http request using axios library.
   * 
   * @param {*} options 
   */
  async _makeRequest(options) {
    return await this.axios.request(options);
  }

  /**
   * Retrieve 5 days / 3 hours forecast data from a city.
   * 
   * @param {string} cityName The city name
   */
  async getForecastByCityName(cityName) {
    try {
      const { data } = await this._makeRequest({
        url: `/forecast?q=${cityName}&appid=${this.appId}`,
        method: 'get'
      });

      return data;
    } catch (err) {
      if (err.response) {
        return err.response.data;
      } else if (err.request) {
        return err.request;
      } else {
        return err.message;
      }
    }
  }
}

module.exports = OpenWeatherApiClient;