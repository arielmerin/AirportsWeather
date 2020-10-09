import csv
""" === READER ==="""
"""Se encarga de leer los archivos csv y preprocesar en caso de ser necesario"""

class Reader:

    """Tiene asignada la creación de una lista con tuplas de coordenadas, esta lista no tiene elementos repetidos"""
    def read_no_repeated_coordinates(self, filename: str) -> list:
        dicti = []
        with open(filename) as File:
            reader = csv.reader(File, delimiter=',', quotechar='"')
            for id, row in enumerate(reader):
                if id == 0:
                    continue
                origin = (row[2], row[3])
                destino = (row[4], row[5])
                if not (origin in dicti):
                    dicti.append(origin)
                if not (destino in dicti):
                    dicti.append(destino)
        return dicti

    """ Se encarga de leer el archivo csv y regresar una lista con un diccionario de cada linea """
    def read_csv_file(self, filename) -> list:
        data = []
        try:
            with open(filename) as File:
                reader = csv.DictReader(File)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print("Error, escribe una ruta válida")
            exit(1)
        except FileExistsError:
            print("Error, archivo válido")
            exit(1)

        return data

    """Tiene la responsabilidad de leer la primera linea de un archivo y represar los valores separados por comas en una lista"""
    def read_headers(self, filename):
        with open(filename, 'r') as F:
            lector = csv.DictReader(F)
            return lector.fieldnames

