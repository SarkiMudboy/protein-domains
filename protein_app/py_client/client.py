import requests

domain_id = 'PF17219'
taxa_id = ''

endpoint = f'http://127.0.0.1:8000/api/protein/{domain_id}'

response = requests.get(endpoint)

data = response.json()

print(data)
