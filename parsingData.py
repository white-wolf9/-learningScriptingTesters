import requests
url = 'http://demo9067635.mockable.io/getMockPayload'
response = requests.get(url)
print(response.json())

for key in response.json().keys():
    print(key)
    
print(response.json()['picture'])