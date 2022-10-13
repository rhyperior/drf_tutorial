import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/products/"

# response = requests.get(endpoint, params={'status':200})
response = requests.post(endpoint, params={"abc": 123}, json={"title":"product creation"} )
# response = requests.get(endpoint, params={"abc": 123}, json={"title":"product creation"} )

print(response.text)
# print(response.json())
print(response.status_code)
print(response.headers)
print(len(response.json()))