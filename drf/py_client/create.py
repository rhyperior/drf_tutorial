import requests

endpoint = "http://localhost:8000/api/products/"

headers = {"Authorization": "Bearer 4c7f8025d6da8ee2af8e011a50a3f15181fcdbb5"}
# response = requests.get(endpoint, params={'status':200})
response = requests.post(endpoint, json={"title": "Jason Holding"}, headers=headers)

print(response.text)
# print(response.json())
print(response.status_code)
print(response.headers)
# print(response.json())