import json
import requests
from Weather import Weather

climita = Weather()

# res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=4bc2be4c4fc75d1df5568e38fd570019').json()

print(climita.makeApiRequest('19.3371', '-99.566'))
