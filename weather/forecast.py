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
This module contains a set of functions for forecast weather data
operations and methods.
"""
import os

from .req import IClinicHTTPClient

__all__ = ['Forecast']


class Forecast:
    """."""
    __base_path = "/forecast"

    def __init__(self):
        """."""
        self.__cli = IClinicHTTPClient(api_key=os.environ.get("APIKEY"))

    def __mount_path(self, path):
        """."""
        new_path = "%s%s"

        if len(path) == 0:
            return self.__base_path
        if path.startswith("/"):
            return new_path % (self.__base_path, path)

        return new_path % (self.__base_path, "/"+path)

    def days5(self, city_name):
        """."""
        data = None
        path = self.__mount_path("")
        # add paramers to cli
        self.__cli.add_param("q", city_name)

        if self.__cli.http_get(path).is_ok():
            data = self.__cli.to_json()
        if data and 'list' in data.keys() and len(data) > 0:
            data = [forecast for forecast in data['list']]

        return data
