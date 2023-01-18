# autenticacion basica
# se envia un usuario con su correspondiente contraseña

import requests
from getpass import getpass

URL = 'http://httpbin.org/basic-auth/vane/1234'

password = getpass('ingresa tu contraseña:   ')

session = requests.Session()
session.auth = ('vane', password)

response = session.get(URL)

if response.status_code == 200:
    print(response.json())

if response.status_code == 401:
    print('autenticacion fallida.')



