import requests

pfam_id = 'PF09133'
taxa_id = '53326'


protein_id = 'A0A0P6DPH2'

data = {
    'id': '9989',
    'protein_id': 'QWERTYCOSTOM',
    'sequence': 'QWERTYUIOPASDFGHkkkk'
}

# endpoint = f'http://127.0.0.1:8000/api/pfam/domain'
endpoint = f'http://127.0.0.1:8000/api/protein/delete/QWERTYCOSTOM'

response = requests.delete(endpoint, json=data)

data = response.json()

print(data)
