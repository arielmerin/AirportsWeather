import json
import unittest
import urllib3
import pytest


class Weather_test(unittest.TestCase):
    def test_make_api_request_by_coordinates(self,lat,lon):
        testurl = 'http://api.openweathermap.org/data/2.5/weather?'
        #print(testurl)
        response = urllib3.urlopen(testurl)
        ans = response.read()
        self.assertTrue()

    def tearDown(self):
        print("-------TEST IS OVER--------")


if __name__ == "__main__":
    unittest.main()

    """def test_make_api_request_by_coordinates(self, lat, lon):
        assert (True, False)"""


