#!/usr/bin/env python3
#
# Copyright (c) 2020 Murilo Ijanc' <mbsd@m0x.ru>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
"""
This module contains a set of functions for http request operations
and methods.
"""
import argparse
import datetime
import http.client
import json
import logging
import os
import sys
import urllib.parse

# Default Api Version
APIVERSI = "2.5"
# iClinic User-Agent
USERAGENT = "iclinic"
# ContentType
CONTTYPE = "application/json"
# Host
HOST = "api.openweathermap.org"
# ApiKey
APIKEY = os.environ.get("APIKEY", None)
APIERROS = []
log = logging.getLogger("iclinic-weather")

def val_fpos(value):
    """
    Validate if float is positive.
    """
    nval = float(value)
    msg = "%s is not a positive value"

    if nval <= 0:
        raise argparse.ArgumentTypeError(msg % value)

    return nval

def val_empty(value):
    """
    Validate if value is empty.
    """
    msg = "is empty value"

    if len(value) == 0:
        raise argparse.ArgumentTypeError(msg)

    return value


def handler_err(resp):
    """."""
    if resp.status > 300:
        log.error("status code error: %d %s" % (resp.status, resp.read()))
        resp = None
    return resp


def req(api_method, params, timeout=10):
    """
    Request function.

    Parameters
    ----------
    api_method : str
        The city name
    params: dict
        The request timeout
    timeout : float, optional
        The request timeout

    Returns
    -------
    resp: request

    Examples
    --------
    >>> params = {'q': 'Ribeirão Preto', 'appid': 'API KEY'}
    >>> req("forecast", params=params, timeout=15)

    """
    if len(api_method) == 0:
        raise ValueError("required api method name")
    if timeout <= 0:
        raise ValueError("timeout needs to be positive")
    if bool(params) is False:
        raise ValueError("empty params")

    headers = {
        "User-Agent": USERAGENT,
        "Accept": CONTTYPE
    }
    base_path = "/data/{ver}/{met}?"
    # Eg path: /data/2.5/forecast?q=...
    path = "{}{}".format(
        base_path.format(ver=APIVERSI, met=api_method),
        urllib.parse.urlencode(params)
    )
    log.debug("Request GET /%s" % api_method)

    conn = http.client.HTTPSConnection(HOST, timeout=timeout)
    conn.request("GET", path, None, headers)
    resp = conn.getresponse()
    # handler error
    handler_err(resp)


    return resp


def ut2weekday(unixtimestamp):
    """
    Return weekday name based on unix time.

    Parameters
    ----------
    unixtimestamp: int
        Unix timestamp

    Returns
    -------
    resp: string
    """
    if unixtimestamp > 0:
        return datetime.datetime.fromtimestamp(unixtimestamp).strftime("%A")
    raise ValueError("invalid unixtimestamp: %d" % (unixtimestamp))


def forecast(api_key, city_name):
    """
    Forecast.

    Parameters
    ----------
    city_name : str
        The city name
    timeout : str
        The api key

    Returns
    -------
    resp: request

    Examples
    --------
    >>> forecast("Ribeirão Preto", timeout=15)
    """
    params = {
        "q": city_name,
        "appid": api_key,
    }

    log.info("Forecast: %s" % city_name)
    return req("forecast", params)


def umbrella(args):
    days = []
    msg_tpl = "You should take an umbrella in these days: %s"
    fore = forecast(args.api_key, args.city)
    if args.limit <= 0:
        raise ValueError("limit greathe")

    for fcast in json.loads(fore.read())['list']:
        day = ut2weekday(fcast['dt'])
        if 'main' in fcast.keys():
            hum = fcast['main']['humidity']
            if hum > args.limit and day not in days:
                days.append(day)
        else:
            print("Not found key: `main` in %s" % str(fcast))

    # has forecast
    weekdays = ""
    len_days = len(days)
    if len_days > 0:
        for num, day in enumerate(days):
            if (num == len_days - 1):
                weekdays += "and "
                weekdays += day
            else:
                weekdays += day
                weekdays += ", "
        weekdays += "."
        print(msg_tpl % weekdays)
    else:
        log.info("you won't need an umbrella")


def main():
    """."""
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG,
                        format='%(name)s (%(levelname)s): %(message)s')

    try:
        args = parser.parse_args()
        log.setLevel(max(3 - args.verbose_count, 0) * 10)
        umbrella(args)
    except ValueError as e:
        log.exception(e)
    except KeyboardInterrupt:
        log.error('bye!')
    finally:
        logging.shutdown()


# parser command line arguments
parser = argparse.ArgumentParser(description='IClini Weather Challenge.')
parser.add_argument('api_key',
                    help='api key: https://home.openweathermap.org/api_keys')
parser.add_argument('city', help='city name eg: "Ribeirão Preto"',
                    type=val_empty)
parser.add_argument('-l', '--limit', type=val_fpos,
                    help='limit humidity eg: 70',
                    default=70.0)
parser.add_argument("-v", "--verbose", dest="verbose_count",
                    action="count", default=0,
                    help="increases log verbosity for each occurence.")

if __name__ == '__main__':
    main()
