import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
# password = getpass()
# response = requests.get(endpoint, params={'status':200})
auth_response = requests.post(auth_endpoint, json={"username": 'admin', "password": '123'})

print(auth_response.text)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    get_endpoint = "http://localhost:8000/api/products/"
    get_response = requests.get(get_endpoint, headers=headers)

    print(get_response.text)
    print(get_response.json())
