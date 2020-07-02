import requests
url = 'https://api.github.com/user'
response = requests.get(url)
print(response.json())

response = requests.get(url, auth=('username','password'))
print(response.json())

response = requests.get(url, headers={'Authorization':'Bearer _inserBearerHere_'})
print(response.json())

