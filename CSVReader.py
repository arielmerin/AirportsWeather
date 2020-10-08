import pandas as pd
import csv
import json


class Reader:

    def __init__(self):
        self.__dict = {}

    def readNonRepeated(self, filename) -> list:
        dicti =[]
        with open(filename) as File:
            reader = csv.reader(File, delimiter=',', quotechar='"')
            for id, row in enumerate(reader):
                if id == 0:
                    continue
                if not (row[0] in dicti):
                    dicti.append(row[0])
                if not (row[1] in dicti):
                    dicti.append(row[1])
        dicti.sort()
        return dicti

    def readFile(self, filename) -> list:
        data = []
        with open(filename) as File:
            reader = csv.DictReader(File)
            for row in reader:
                data.append(row)
        return data

    def read_airports_db(self, filename):
        return json.load(open(filename))
