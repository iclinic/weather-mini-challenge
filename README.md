## Weather Mini Challenge
Suppose you live in Ribeirão Preto. Should you take an umbrella?

You tell us!

Based on weather api https://openweathermap.org/api you should make a request on this api and return the Ribeirão Preto weather forecast for the week, based on:

- Humidity
- Wind
- Temperature
- Cloudiness
- Pressure

```
Humidity probability:
- 0% No chance of rain
- ~10% slight chance of isolated rains
- ~20% a small chance of rain
- 30-50% considerable chance of scattered rain
- 60-70% scattered rain
- 80-100% rainy (strong or weak)
```

If air humidity is greater than **70%**, display the message: **You should take an umbrella in these days: ...**
