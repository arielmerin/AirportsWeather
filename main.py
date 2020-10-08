from Weather import Weather
from CSVReader import Reader

ruta_archivo = "resources/dataset1.csv"
climita = Weather()
lector = Reader()
# print(climita.makeApiRequest('19.3371', '-99.566'))
data = lector.readFile(ruta_archivo)
toGet = lector.readNonRepeated(ruta_archivo)
print(data)
print("Separated\n\n\n")
print(toGet)
print(len(toGet))
print(lector.read_airports_db('resources/city.list.json'))
