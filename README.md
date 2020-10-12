# Climas en origen y destino de un vuelo
Para correr el programa necesitaremos los siguientes comandos
 para instalar las librerías necesarias: 
 
`$ pip3 install -r requirements.txt
`
 
 o de forma alternativa 
 
 `$ source venv/bin/activate`

Finalmente para correr el programa:

` $ python3 src/main.py ruta/al/archivo.csv
` 

 Sólo acepta un archivo a la vez y tiene que ser enviado al menos un archivo.
 Por ejemplo:
 
` (venv) ~/AirportsWeather$ python3 src/main.py resources/dataset1.csv  
` 
## Características del archivo csv
 Debe comenzar con el la sigiente linea
 
` origin,destination,origin_latitude,origin_longitude,destination_latitude,destination_longitude
` 

Sólo de esta forma logrará ser leído por nuestro programa
;) 

