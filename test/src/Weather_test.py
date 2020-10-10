import json
import unittest
import urllib3
import pytest


class Weather_test(unittest.TestCase):

    def setUp(self):
        self.ApiUrl = "http://api.openweathermap.org/data/2.5/weather?"
        self.ApiKey = "4bc2be4c4fc75d1df5568e38fd570019"

    def test_make_api_request_by_coordinates(self,lat,lon):
        testurl = (self.ApiUrl+"&"+"lat="+ 45.325562 +"&"+"lon=" +8.26423+"&"+"APPID="+self.ApiKey)
        
        response=urllib3.urlopen(testurl)
        ans = response.read()
        json_data=json.loads(ans)
        coordinates = json_data["lat"]
        print("coordinates are:"+coordinates)
        self.assertTrue(coordinates == 45.325562 )



    def tearDown(self):
        print("-------TEST IS OVER--------")


if __name__ == "__main__":
    unittest.main()

    """def test_make_api_request_by_coordinates(self, lat, lon):
        assert (True, False)"""


