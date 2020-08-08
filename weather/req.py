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
import json
import http.client

from .version import version as __version__

__all__ = ['IClinicHTTPClient']

# Default Api Version
DF_APIVERSI = "2.5"
# Default iClinic User-Agent
DF_USERAGENT = "iclinic/%s"
# Default http client timeout 15 seconds
DF_TIMEOUT = 15
# Api Base url
DF_CONTTYPE_JSON = "application/json"


class IClinicHTTPClient(http.client.HTTPSConnection):
    """."""

    __timeout = DF_TIMEOUT
    __host = "api.openweathermap.org"
    __is_ssl = True
    __headers = {
        "User-Agent": DF_USERAGENT % (__version__),
        "Accept": DF_CONTTYPE_JSON
    }
    __base_path = "/data/%s%s?"  # /data/<api_version><service>

    def __init__(self, *args, **kwargs):
        super().__init__(host=self.__host, *args, **kwargs)
        self.__resp = None  # Response object
        self.__body = None  # Body str
        self.__agent = None  # User-Agent
        self.__params = {}

    @property
    def agent(self):
        return self.__agent

    @agent.setter
    def agent(self, value):
        """."""
        if len(value) == 0:
            raise ValueError("user agent")
        self.__agent = value
        return True

        def add_param(self, name, value, replace=True):
            pass

        def del_param(self, name):
            pass

    @property
    def status_code(self):
        """."""
        return self.__resp.status if self.__resp else 500

    @property
    def body(self):
        """."""
        return self.__body

    def to_json(self):
        """."""
        if self.__body:
            try:
                return json.loads(self.__body)
            except Exception as e:
                raise ValueError(e)
        return None

    def http_get(self, path, params=None):
        """."""
        if len(path) == 0:
            raise ValueError("length path")
        # TODO: mount path
        path = self.__base_path % (DF_APIVERSI, path)
        # print(path)
        # print(params)
        self.request("GET", path+params, None, self.__headers)
        self.__resp = self.getresponse()
        self.__body = self.__resp.read()
        # print(self.__body)
        return self

    def is_ok(self):
        """."""
        if self.__resp and self.__resp.status < 300:
            return True
        return False
