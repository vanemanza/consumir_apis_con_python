import requests

# 1) crear una  variable(constante) con la url del servidor donde queremos hacer la petiicion
URL = "http://httpbin.org/get"

# 2) resalizar la  peticion a traves de la funcion get de request
response  = requests.get(URL) # como arg recibe la URL
# Retorna un objeto de tipo response q se puede guardar en otra variable
print(response) # <Response [200]> --> objeto response
# Otros atributos del objeto:
print(response.status_code) # 200
print(response.text) # cuerpo de la respuesta: {
                                            #   "args": {}, 
                                            #   "headers": {
                                            #     "Accept": "*/*", 
                                            #     "Accept-Encoding": "gzip, deflate", 
                                            #     "Host": "httpbin.org", 
                                            #     "User-Agent": "python-requests/2.25.0", 
                                            #     "X-Amzn-Trace-Id": "Root=1-63c61174-4cb2169a7505bc504c4ccb4d"
                                            #   }, 
                                            #   "origin": "190.17.11.196", 
                                            #   "url": "http://httpbin.org/get"
                                            # } Tipo Str
print(response.json()) # tipo dict
payload = response.json()
print( payload.get('args'))   
print(response.url)                                   


