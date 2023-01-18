import requests

#URL = 'https://randomuser.me/api/?results=100'

# ahora en vez de pasar los parametros x query, lo hago de forma dinamica, en vez de pasar result x url
# se lo paso en la funcion get de requests, luego de la URK

URL = 'https://randomuser.me/api/'

count= int(input('indica la cantidad de usuarios que deseas ver: '))

response = requests.get(URL, params={'results': count})

if response.status_code == 200:
    payload = response.json()
    results = payload.get('results')
    for user in results:
        name = user.get('name')
        #print(f'{name["title"]} {name["first"]} {name["last"]}')
        # otra forma mejor de hacer lo mismo 
        print("{title} {first} {last}".format(**name))

    print(len(results))    