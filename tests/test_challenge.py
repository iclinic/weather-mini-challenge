import argparse
import io
import unittest

from iclinic_wea import (
    req,
    ut2weekday,
    val_fpos,
    val_empty,
	handler_err
)

class MockFile:
    """Mock file"""
    def read(self, count=None):
        pass

    def readline(self, count=None):
        pass

    def close(self):
        pass

class MockHTTPResponse(io.IOBase):
    """Mock http response"""

    def __init__(self, fp, msg, status, reason):
        self.fp = fp
        self.msg = msg
        self.status = status
        self.reason = reason
        self.code = 200

    def read(self):
        return self.msg

    def info(self):
        return {}

    def geturl(self):
        return self.url

class IClinigChallenge(unittest.TestCase):
    city_name = 'Ribeirão Preto'

    def test_val_empty_failed(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            val_empty("")

    def test_val_empty_ok(self):
            self.assertEqual(val_empty("iclinic"), "iclinic")
            self.assertEqual(len(val_empty("iclinic")), len("iclinic"))

    def test_val_fpos_negative_value(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            val_fpos(-1)

    def test_val_fpos_positive_value(self):
            self.assertEqual(val_fpos(1), 1)

    def test_ut2weekday_ok(self):
        self.assertEqual(ut2weekday(1596286800), "Saturday")

    def test_ut2weekday_negative_time(self):
        with self.assertRaises(ValueError):
            ut2weekday(-1)

    def test_req_invalid_method_name(self):
        with self.assertRaises(ValueError):
            req("", {}, timeout=10)

    def test_req_empty_params(self):
        with self.assertRaises(ValueError):
            req("forecast", {}, timeout=10)

    def test_req_negative_timeout(self):
        with self.assertRaises(ValueError):
            req("forecast", {'q': self.city_name}, timeout=-10)

    def test_req_handler_err_401(self):
        resp = MockHTTPResponse(MockFile(), "{}", 401, "Not Authorized")
        with self.assertRaises(ValueError):
            handler_err(resp)

    def test_req_handler_err_404(self):
        resp = MockHTTPResponse(MockFile(), "{}", 404, "Not Found")
        with self.assertRaises(ValueError):
            handler_err(resp)

    def test_req_handler_err_429(self):
        resp = MockHTTPResponse(MockFile(), "{}", 429, "To Many Requests")
        with self.assertRaises(ValueError):
            handler_err(resp)

    def test_req_handler_err_500(self):
        resp = MockHTTPResponse(MockFile(), "{}", 429, "Error")
        with self.assertRaises(ValueError):
            handler_err(resp)

    def test_req_handler_ok_200(self):
        resp = MockHTTPResponse(MockFile(), "{}", 200, "OK")
        data = handler_err(resp)
        self.assertEqual(data, "{}")



if __name__ == '__main__':
    unittest.main()
