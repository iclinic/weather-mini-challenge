const axios = require('axios');
const OpenWeatherApiClient = require('../open-weather-api-client');

jest.mock('axios');

beforeEach(() => {
  axios.mockClear();
})

it('should creates an instance of OpenWeatherApiClient', () => {
  const openWeatherApiClient = new OpenWeatherApiClient('app-id');
  expect(openWeatherApiClient).toBeTruthy();
  expect(axios.create).toHaveBeenCalledTimes(1);
})