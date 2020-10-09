import pandas as pd
import csv
import json


class Reader:

    def __init__(self):
        self.__dict = {}

    def readNonRepeated(self, headers: list, fields: list, filename: str) -> list:
        dicti = []
        keywords = {}
        for i, header in enumerate(headers):
            keywords.setdefault(header, i)
        with open(filename) as File:
            reader = csv.reader(File, delimiter=',', quotechar='"')
            for id, row in enumerate(reader):
                if id == 0:
                    continue
                for i in range(len(fields)):
                    if not (row[keywords[fields[i]]] in dicti):
                        dicti.append(row[keywords[fields[i]]])
        dicti.sort()
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
