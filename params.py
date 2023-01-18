import requests

# URL = 'http://httpbin.org/get?name=vane&password=123'

# query : sirve para enviar informacion al servidor mediante la url, es todo lo q esta despues del ?
# los parametros se veran en el cuerpo de la peticion, en 'args'

# hay otra forma mas simple de generar la query

URL = 'http://httpbin.org/get'

params = { 
    'name':'vane',
    'password':'123'
}



response = requests.get(URL, params=params)

if response.status_code == 200:
    payload = response.json()
    params = payload['args']
    
    print(response.text)
    print(params['name'])
    print(params['password'])

print(response.url)