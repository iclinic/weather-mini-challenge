[![Travis (.org) branch](https://img.shields.io/travis/murilobsd/weather-mini-challenge/master?style=for-the-badge)](https://travis-ci.com/github/murilobsd/weather-mini-challenge)
[![Codecov](https://img.shields.io/codecov/c/github/murilobsd/weather-mini-challenge?style=for-the-badge)](https://codecov.io/gh/murilobsd/weather-mini-challenge)
[![Read the Docs](https://img.shields.io/readthedocs/iclinic-weather?label=DOCS&style=for-the-badge)](http://iclinic-weather.rtfd.io/)

# Weather Mini Challenge
Suppose you live in Ribeirão Preto. Should you take an umbrella?

You tell us!

If the air humidity on a given day is **greater** than **70%**, it is a good idea to take an umbrella with you.
Your goal is to fetch the Ribeirão Preto air humidity forecast for the next **five** days from https://openweathermap.org/api and display the following message template:

*You should take an umbrella in these days: ....*

For instance, if on the next five days air humidity will be greater than 70% on Monday, Tuesday and Wednesday, you must display the message:

*You should take an umbrella in these days: Monday, Tuesday and Wednesday.*

## Requirements
- Python 3>
- Just get an access key on the website:
[https://openweathermap.org/](https://openweathermap.org/)

## Setup

```sh
$ pip install --user .
```

## Run

There are two ways for you to enjoy the umbrella challenge:

### Running the simple script

In that case you can use the -h option to return help on how to use the script.

```sh
$ iclinic_wea.py --help
usage: iclinic_wea.py [-h] [-l LIMIT] [-t TIMEOUT] [-v] api_key city

IClinic Weather Challenge.

positional arguments:
  api_key               api key: https://home.openweathermap.org/api_keys
  city                  city name eg: "Ribeirão Preto"

optional arguments:
  -h, --help            show this help message and exit
  -l LIMIT, --limit LIMIT
                        limit humidity eg: 70
  -t TIMEOUT, --timeout TIMEOUT
                        connection timeout default: 10
  -v, --verbose         increases log verbosity for each occurence.
```

The example below checks if I will need the umbrella for the next five days in
the city of ribeirão preto.

```sh
$ export APIKEY=.....
$ iclinic_wea.py --limit 70 "$APIKEY" "Ribeirão Preto"
```

> Note the **limit** argument has a default value of 70, but it can be changed.

```sh
$ export APIKEY=.....
$ iclinic_wea.py --limit 41.1 "$APIKEY" "Ribeirão Preto"
You should take an umbrella in these days: Monday, Tuesday, Wednesday, Thursday and Friday.
```
If you want to view in a more verbose way, increase -v.

```sh
$ export APIKEY=.....
$ iclinic_wea.py --limit 41.1 "$APIKEY" "Ribeirão Preto" -v
iclinic-weather (INFO): Forecast: [Ribeirão Preto]
iclinic-weather (INFO): you won't need an umbrella
```

### Importing the module

```py
from iclinic_wea import umbrella

_args = {'city': 'Ribeirão Preto', 'appid': 'API KEY', 'limit': 70, 'timeout': 10}
umbrella(_args)
You should take an umbrella in these days: Tuesday and Wednesday.
```

## Docs
> Required [Sphinx](https://www.sphinx-doc.org/)
```
$ cd docs/
$ make html
$ python3 -m http.server --directory __build/html
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/)

```

## Tests

```sh
$ make test
```
