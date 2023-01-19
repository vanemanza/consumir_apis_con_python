import requests

access_token = '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'

URL = 'https://api.github.com/user'

headers = { 
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {access_token}'
}
response = requests.get(URL, headers=headers)

if response.status_code == 200:
    username = response.json().get('login')
    print(username)


print(response.status_code)
print(response.text)


# PASOS:
# 1) CREAR UNA APLICACION EN GITHUB
# 2) OBTENER EL CODIGO DEL USUARIO, REALIZANDO UNA PETICION A "https://github.com/login/oauth/authorize?client_id=<cliente id>&scope=user"
#    el unico parametro requerido es el CLIENT_ID, que se obtiene al momento de crear la aplicacion
# 3) OPCIONALMENTE SE PUEDE DEFINIR UN SCOPE (ALCANCE DE LA APLICACION) 
# 4) REALIZAR UNA PETICION PARA OBTENER EL ACCESS TOKEN USANDO UN POST:
    # "https://github.com/login/oauth/access_token"
# 5) a la peticion le enviamos por parametros el client_id, el client_secret  y el codigo.    
# ahora si se puede acceder a info de usuario