import datetime
import json
import time
import unittest

from Weather import Weather

"""En ensta clase vamos a probar los métodos de la clase Weather"""
class Weather_test(unittest.TestCase):

    clima = Weather()

    """Prueba que dado un conjunto de peticiones mayor a 60, haga la pausa de 1 minuto para evitar ser baneada"""
    def test_make_api_request_by_coordinates(self):
        instante_inicial = datetime.datetime.now()
        peticiones = [('19.3371', '-99.566'), ('25.7785', '-100.107'), ('19.4363', '-99.0721'), ('22.2964', '-97.8659'),
                      ('20.5218', '-103.311'), ('31.6361', '-106.429'), ('21.0365', '-86.8771'), ('32.5411', '-116.97'),
                      ('29.0959', '-111.048'), ('18.6537', '-91.799'), ('20.937', '-89.6577'), ('18.5047', '-88.3268'),
                      ('19.1459', '-96.1873'), ('16.9999', '-96.7266'), ('15.7753', '-96.2626'), ('17.6016', '-101.461'),
                      ('20.6801', '-105.254'), ('20.6801', '-105.2541'), ('-12.0219', '-77.1143'), ('22.9892', '-82.4091'),
                      ('20.7901', '-105.254'), ('21.6801', '-105.2541'), ('-10.0219', '-77.1143'), ('25.9892', '-82.4091'),
                      ('4.70159', '-74.1469'), ('25.7932', '-80.2906'), ('33.9425', '-118.408'), ('40.6398', '-73.7789'),
                      ('25.5683', '-103.411'), ('15.8769', '-97.0891'), ('16.7571', '-99.754'), ('23.1614', '-106.266'),
                      ('15.5683', '-103.411'), ('15.8769', '-91.0891'), ('16.7571', '-99.954'), ('23.1614', '-206.266'),
                      ('14.5833', '-90.5275'), ('21.7056', '-102.318'), ('17.997', '-92.8174'), ('17.5391', '-88.3082'),
                      ('32.8968', '-97.038'), ('20.5224', '-86.9256'), ('41.9786', '-87.9048'), ('33.4343', '-112.012'),
                      ('28.7029', '-105.965'), ('20.6173', '-100.186'), ('20.9935', '-101.481'), ('19.1581', '-98.3714'),
                      ('39.8719', '-75.2411'), ('22.2543', '-100.931'), ('35.214', '-80.9431'), ('43.6772', '-79.6306'),
                      ('29.9844', '-95.3414'), ('49.1939', '-123.184'), ('49.0128', '2.55'), ('22.8971', '-102.687'),
                      ('52.3086', '4.76389'), ('33.6367', '-84.4281'), ('27.3926', '-109.833'), ('40.4719', '-3.56264'),
                      ('52.3086', '4.86389'), ('32.6367', '-84.4281'), ('25.3926', '-109.833'), ('39.4719', '-3.56264'),
                      ('-33.393', '-70.7858')]

        for peticion in peticiones:
            self.clima.make_api_request_by_coordinates(peticion[0], peticion[1])
        instante_final = datetime.datetime.now()
        duración = instante_final - instante_inicial
        self.assertTrue(duración.seconds >= 59)

    def test_parse_time(self):
        hora = 1602462419
        formato_correcto = "7:26 PM (CDT)"
        self.assertEqual(formato_correcto, Weather.formato_de_horas(self, hora))
        self.assertEqual(formato_correcto, Weather.formato_de_horas(self, hora))

    def test_parse_info(self):
        example_json = {"cod":"404", "message":"city not found"}
        error_msj = 'ERROR\nNo se pudo consultar la información\n'
        Weather.parse_weather_info(self, example_json)
        self.assertEqual(error_msj, Weather.parse_weather_info(self, example_json) )

    def tearDown(self):
        print("\n------------------Test de Weather completos------------------")

if __name__ == "__main__":
    unittest.main()

