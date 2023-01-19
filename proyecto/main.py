import requests
from settings import *

code='e5f7719e18422be37f26'

URL = 'https://github.com/login/oauth/access_token'

params = { 
    'client_id': CLIENT_ID,
    'client_secret': SECRET_ID,
    'code': code
}

headers = { 
    'Accept': 'application/json'
}

response = requests.post(URL, params=params, headers=headers)

if response.status_code == 200:
    print(response.json())
    # {'access_token': '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', 'token_type': 'bearer', 'scope': 'user'}
