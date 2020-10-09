import pandas as pd
import csv
import json


class Reader:

    def __init__(self):
        self.__dict = {}

    def readNonRepeated(self, filename: str) -> list:
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

    def readFile(self, filename) -> list:
        data = []
        with open(filename) as File:
            reader = csv.DictReader(File)
            for row in reader:
                data.append(row)
        return data

    def read_headers(self, filename):
        with open(filename, 'r') as F:
            lector = csv.DictReader(F)
            return lector.fieldnames

    def read_airports_db(self, filename):
        return json.load(open(filename))
