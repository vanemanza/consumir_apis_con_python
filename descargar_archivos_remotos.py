import requests

# 1) realizamos la peticion
URL = 'https://codigofacilito.com/images/cody' # RETORNA UNA imagen png

#  como queremos descargar un archivo de un servidor remoto,
# hay q crear una via o tunel x donde pueda descargarse este archivo
# para eso se usa el parametro 'stream'
# esto le indica a la libreria requests q realice la peticion al servidor
# pero q la peticion no se cierre
# asi se puede recibir el archivo en fragmentos, en chunks? 
# solo se cierra cuando el archivo es descargado en su totalidad

response = requests.get(URL, stream=True) # 2) mantenemos la peticion activa hasta q el archivo haya sido descargado en su totalidad

if response.status_code == 200: # 3) validamos q la resp x parte del servidor es exitosa
    with open('images/cody.png', 'wb') as file: # 4) creamos un archivo en el servidor local
        for chunk in response.iter_content(1024): # 5) itermos en fragmentos sobre el archivo remoto
            file.write(chunk) # 6) descargando y escribiendo de forma local cada fragmento

