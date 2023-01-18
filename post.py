import requests

URL = 'http://httpbin.org/post'


# para enviar informacion usando post, lo hacemos mediante el parametro data
# se recibe en el cuerpo de la respuesta en forms

data = { 
    'username': 'vane',
    'password':'123'
}

response = requests.post(URL, data=data)

if response.status_code == 200: # otra opcion requests.codes.ok 

    payload = response.json()

    print(payload)

    # la informacion ya no se envia en la url,  se puede confirmar imprimiendo response.url
    print(response.url)