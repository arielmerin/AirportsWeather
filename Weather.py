import csv
import requests
import amadeus
from cachetools import cached, TTLCache
from datetime import datetime
import tzlocal
""""
Esta clase se encarga de hacer las peticiones al servidor para conocer el clima y manejar los posibles errores
"""


class Weather:
    caching = TTLCache(maxsize=100, ttl=1200)

    def __init__(self):
        self.address = 'http://api.openweathermap.org/data/2.5/weather?'
        self.apiID = '&APPID=4bc2be4c4fc75d1df5568e38fd570019'
        self.idi = '&lang=es'
        self.units = '&units=metric'

    @cached(caching)
    def make_api_request_by_city_name(self, name) -> str:
        respuesta = requests.get(self.address + 'q=' + name + self.idi)
        return self.parse_weather_info(respuesta)

    @cached(caching)
    def makeApiRequest_by_coordinates(self, lat, lon) -> str:
        datos_obtenidos = requests.get(self.address +
                                       '&lat=' + str(lat) +
                                       '&lon=' + str(lon) +
                                       self.apiID + self.idi +
                                       self.units).json()
        return self.parse_weather_info(datos_obtenidos)

    def parse_weather_info(self, respuesta) -> str:
        contenido = ''
        try:
            descripcion = respuesta['weather'][0]['description']
            humedad = respuesta['main']['humidity']
            temperatura_actual = respuesta['main']['temp']
            temperatura_minima = respuesta['main']['temp_min']
            temperatura_maxima = respuesta['main']['temp_max']
            amanecer = self.formato_de_horas(respuesta['sys']['sunrise'])
            atardecer = self.formato_de_horas(respuesta['sys']['sunset'])
        except KeyError:
            print('hi')
        return 'El pronóstico del clima es: {}, humedad: {} ' \
               '\nTemperatura actual: {}°C, mínima: {}°C, máxima: {}°C' \
               '\nAmanecer: {} Puesta del sol: {}'.format(descripcion,humedad,
                                                        temperatura_actual, temperatura_minima, temperatura_maxima,
                                                        amanecer, atardecer)

    """ """
    def formato_de_horas(self, unix_time) -> str:
        unix_timestamp = float(unix_time)
        local_timezone = tzlocal.get_localzone()
        local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
        return local_time.strftime("%-I:%M %p (%Z)")
""" Manejar los errores de las peticiones """
