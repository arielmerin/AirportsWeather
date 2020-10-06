from Weather import Weather
from CSVReader import Reader
climita = Weather()
lector = Reader()
# print(climita.makeApiRequest('19.3371', '-99.566'))
data = lector.readFile("resources/dataset1.csv")
print(data)
