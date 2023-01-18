# las cookies son un mecanismo q implementa el cliente para poder almacenar informacion q enviará al servidor.

# esto para cada una de las peticiones q realice

import requests

URL = 'http://httpbin.org/cookies'

# enviar cookies al servidor

cookies = { 
    'sessions':'abc123',
    'name':'vane'
}

response = requests.get(URL, cookies=cookies)

if response.status_code == 200:
    print(response.json())

    