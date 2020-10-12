from Weather import Weather
from CSVReader import Reader
import sys, re

dataset1 = "resources/dataset1.csv"
dataset2 = "resources/dataset2.csv"
db_ciudades = "resources/city.list.json"
climita = Weather()
lector = Reader()

"""Aquí se concretarán las peticiones y formato de respuestas a nuestros clientes"""
def run():
    validate_file(sys.argv)

    """Aquí tenemos una lista de diccionarios con las peticiones de climas a resolver"""
    entradas = lector.read_csv_file(sys.argv[1])

    solicitudes_no_repetidas = lector.read_no_repeated_coordinates(sys.argv[1])
    """Busca y selecciona las peticiones no repetidas para posteriormente enviarlas al servidor"""
    peticiones = {}
    for solicitud in solicitudes_no_repetidas:
        peticion = climita.make_api_request_by_coordinates(solicitud[0], solicitud[1])
        peticiones.setdefault(solicitud, peticion)

    """Selecciona y asigna a cada linea del archivo original su solicitud completada"""
    for entrada in entradas:
        print("CLIMA DE ORIGEN ({}):\n".format(entrada['origin'])+ peticiones[(entrada['origin_latitude'], entrada['origin_longitude'])] +
              "\nCLIMA DE DESTINO ({}):\n".format(entrada['destination']) + peticiones[(entrada['destination_latitude'], entrada['destination_longitude'])] +"\n\n\n")


"""=== Validación del archivo ==="""
"""Se encarga de verificar la consistencia del archivo enviado como parámetro, de otra forma termina el programa informándole a la usuaria qué error tuvo"""
def validate_file(argumento):
    """Valida que le haya sido enviado uno y sólo un argumento"""
    if len(argumento) != 2:
        print("Error\nDebe indicar la ruta a un archivo csv")
        exit(1)

    """Valida que el archivo pasado como argumento tenga extensión .csv"""
    if (not re.match('.*\.csv', argumento[1])):
        print("Error, sólo admito archivos csv")
        exit(1)

    cabezera = ['origin', 'destination', 'origin_latitude', 'origin_longitude', 'destination_latitude',
                'destination_longitude']
    entrada_cabezera = lector.read_headers(argumento[1])

    """Revisa si el número de columnas es correcto"""
    if len(entrada_cabezera) != len(cabezera):
            print("ERROR\nEl archivo csv debe tener los siguientes encabezados:"
                  "\norigin, destination, origin_latitude, origin_longitude, destination_latitude, destination_longitude")
            exit(1)

    """Valida que cada nombre de columna sea consistente con los solicitados"""
    for cabeza in entrada_cabezera:
        if cabeza not in cabezera:
            print("ERROR\nEl archivo csv debe tener los siguientes encabezados:"
                  "\norigin, destination, origin_latitude, origin_longitude, destination_latitude, destination_longitude")
            exit(1)


if __name__ == '__main__':
    run()
