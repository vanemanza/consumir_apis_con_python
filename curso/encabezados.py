import requests

URL = 'http://httpbin.org/post'

# HEMOS ENVIADO INFO X LA URL (QUERY) -> GET (params)
# POR EL CUERPO -> POST
# AHORA ENVIAREMOS METADATA X EL ENCABEZADO 

# todos los metodos ( get-post-put-patch-delete) nos permiten enviar informacion ya sea x la url, el cuerpo o el encabezado.

headers = { 

    'curso':'Curso de python',
    'version': '2.0',
    'author': 'vane'
}

params = { 
    'plataforma':'codigo facilito'
}

data = { 
    'username':'vane',
}

response = requests.post(URL, headers=headers, params=params, data=data)

if response.status_code == 200:
    print(response.text)

# podemos enviar valores atraves del query (params) mas comun para get, la informacion es visible
# podemos enviar valores a traves del encabezado (headers), la informacion es publica
# podemos enviar valores a traves del cuerpo de la peticion (data) mas comun para post, la informacion no se expone

