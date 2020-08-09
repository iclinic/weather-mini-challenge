import unittest

from iclinic_wea import ut2weekday, forecast, req

class IClinigChallenge(unittest.TestCase):
    city_name = 'Ribeirão Preto'

    def test_ut2weekday_ok(self):
        self.assertEqual(ut2weekday(1596933260), "Saturday")

    def test_ut2weekday_negative_time(self):
        with self.assertRaises(ValueError):
            ut2weekday(-1)

    def test_forecast_invalid_city_name(self):
        with self.assertRaises(ValueError):
            forecast("", timeout=10)

    def test_req_invalid_method_name(self):
        with self.assertRaises(ValueError):
            req("", {}, timeout=10)

    def test_req_empty_params(self):
        with self.assertRaises(ValueError):
            req("forecast", {}, timeout=10)

    def test_req_negative_timeout(self):
        with self.assertRaises(ValueError):
            req("forecast", {'q': self.city_name}, timeout=-10)

if __name__ == '__main__':
    unittest.main()
