import requests

domain_id = 'PF17219'
taxa_id = ''

protein_id = 'A0A0P6DPH2'

data = {
    'protein_id': 'QWERTYCOSTOM',
    'sequence': 'QWERTYUIOPASDFGHJKL'
}

endpoint = f'http://127.0.0.1:8000/api/protein/get/{protein_id}/'
# endpoint = f'http://127.0.0.1:8000/api/protein/'

response = requests.get(endpoint)

data = response.json()

print(data)
