import pandas as pd
import csv


class Reader:

    def __init__(self):
        self.__dict = {}

    def readNonRepeated(self, filename) -> list:
        with open(filename) as File:
            reader = csv.reader(File, delimiter=',', quotechar='"')
            for row in reader:
                self.__dict.setdefault(row[0], row[1])
            print(self.__dict)

    def readFile(self, filename) -> list:
        data = []
        with open(filename) as File:
            reader = csv.DictReader(File)
            for row in reader:
                data.append(row)
        return data


