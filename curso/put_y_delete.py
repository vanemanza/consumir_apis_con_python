import requests


# TODAS las funciones de requests ( get, post, put y delete) retornan
# un objeto de tipo response
# y permiten enviar valores a traves del query, de la data y de los encabezados

# URL = 'http://httpbin.org/put'

# response = requests.put(URL, 
#                     params={'name':'vane'}, 
#                     headers={'version':'2.0'},
#                     data={'id':1}
#                     )
# if response.status_code == 200:
#     print(response.text)

URL = 'http://httpbin.org/delete'

response = requests.delete(URL, 
                    params={'name':'vane'}, 
                    headers={'version':'2.0'},
                    data={'id':1}
                    )
if response.status_code == 200:
    print(response.text)