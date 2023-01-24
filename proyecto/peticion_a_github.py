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


