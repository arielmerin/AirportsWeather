import csv
import requests
import json

from cachetools import cached, TTLCache

class Weather:
    caching = TTLCache(maxsize=256, ttl=1200)
    def __init__(self):
        self.address = 'http://api.openweathermap.org/data/2.5/weather?'
        self.apiID = '&APPID=4bc2be4c4fc75d1df5568e38fd570019'
        self.idi = '&lang=es'
        self.lat = '&lat='
        self.lon = '&lon='

    @cached(caching)
    def makeApiRequest(self, lat, lon):
        return requests.get(self.address + self.lat + lat + self.lon + lon + self.apiID + self.idi).json()







