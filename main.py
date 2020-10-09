from Weather import Weather
from CSVReader import Reader
import json

dataset1 = "resources/dataset1.csv"
dataset2 = "resources/dataset2.csv"
climita = Weather()
lector = Reader()
# print(climita.makeApiRequest('19.3371', '-99.566'))
# data = lector.readFile(ruta_archivo)
# print(data)
# print("Separated\n\n\n")
# print(toGet)
# print(lector.read_airports_db('resources/city.list.json'))

# climita.makeApiRequest_by_coordinates(19.3317, -99.566)
# print(climita.make_api_request_by_coordinates(19.3317, -99.566))



def encontrar_ciudad(ciudad, ruta_ciudades_validas)-> bool:
    json_nombre = json.load(open(ruta_ciudades_validas))

    for i in json_nombre:
        if ciudad.lower() in i['name'].lower():
            return True
    return False
toGet = lector.readNonRepeated(dataset1)
print(lector.read_headers(dataset1))
print(toGet)
print(len(toGet))

climas = []

for coordenadas in toGet:
    peticion= climita.make_api_request_by_coordinates(coordenadas[0], coordenadas[1])
    climas.append(peticion)
    print(peticion)

# if encontrar_ciudad('Canada', 'resources/city.list.json'):
#     print('lo hallé')

# print(climita.make_api_request_by_city_name('Ash Shuhadā'))

#
# keywords = ('tax', 'policy', 'regulation', 'spending', 'budget', 'central bank')
#
# with open('resources/city.list.json') as json_file:
#
#     # read json file line by line
#     for line in json_file.readlines():
#
#         # create python dict from json object
#         json_dict = json.loads(line)
#
#         # check if "body" (lowercased) contains any of the keywords
#         if any(keyword in json_dict["body"].lower() for keyword in keywords):
#             print(json_dict["date"])
