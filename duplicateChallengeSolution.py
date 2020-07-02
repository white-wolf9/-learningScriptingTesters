import requests
url = 'http://demo9067635.mockable.io/getDuplicateUrlsPayload'
response = requests.get(url)
data = response.json()
print(data)
rawDataList = []
refinedDataSet = set()

for object in data:
   rawDataList.append(object['url'])
   
print(len(rawDataList))
refindeDataSet = set(rawDataList)
print(len(refindeDataSet))