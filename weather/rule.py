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
from .forecast import Forecast
from .misc import ut2day

__all__ = ['umbrella']


def umbrella(city_name, limit=70):
    """."""
    days = {}
    f = Forecast()
    data = f.days5(city_name)
    if not data:
        print("ops, no data from: %s", city_name)
        return
    for forecast in data:
        day = ut2day(forecast['dt'])
        if 'main' in forecast.keys():
            hum = forecast['main']['humidity']
            if hum > 70.0 and day not in days.keys():
                days[day] = True
        else:
            print("Not found key: `main` in %s" % str(forecast))
    if len(days.keys()) > 0:
        info = "You should take an umbrella in these days: %s" % ",".join(
            days.keys())
        print(info)
    else:
        print("you can leave keep calm")
