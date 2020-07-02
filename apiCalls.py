import requests
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
print (response.json())

jsonPayload = {'album':'Vivid', 'song':'Cult Of Personality', 'artist':'Living Color', 'year':1988}
response = requests.post(url,json = jsonPayload)
print(response.json())

url = 'https://jsonplaceholder.typicode.com/photos/100'
response = requests.put(url, json = jsonPayload)
print(response.json())

newJsonPayload = {'album':'Vivid', 'song':'Cult Of Personality', 'artist':'Living Color', 'year':1988, 'newInformation':'Some Text'}
response = requests.put(url, json = newJsonPayload)
print(response.json())

response = requests.delete(url)
print(response.json())
