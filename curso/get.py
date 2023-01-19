import requests

URL = 'http://httpbin.org/get'

response = requests.get(URL)

print(response) #objeto response
print(response.status_code) # para conocer el codigo de status
print(response.text) # para conocer el cuerpo de la respuesta, pero es un objeto de tipo str
print(response.json()) # serializa la respuesta y nos permite acceder a los atributos de la respuesta
payload = response.json()
print(payload.get('origin'))
print(response.url)