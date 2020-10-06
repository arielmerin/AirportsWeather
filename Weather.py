import csv
import requests
import json
import amadeus
from cachetools import cached, TTLCache

class Weather:

    def __init__(self):
        self.address = 'http://api.openweathermap.org/data/2.5/weather?'
        self.apiID = '&APPID=4bc2be4c4fc75d1df5568e38fd570019'
        self.idi = '&lang=es'
        self.lat = '&lat='
        self.lon = '&lon='


    def makeApiRequest(self, lat, lon):
        return requests.get(self.address + self.lat + lat + self.lon + lon + self.apiID + self.idi).json()


""" Manejar los errores de las peticiones """




