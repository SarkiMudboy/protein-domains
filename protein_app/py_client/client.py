import requests
import json
import getpass
import os


pfam_id = 'PF09133'
taxa_id = '53326'

protein_id = 'A0A0P6DPH2'

def refresh():

    credentials = {}

    if os.path.exists('creds.json'):
        with open('creds.json', 'r') as infile:
            credentials = json.load(infile)
            token = credentials.get('refresh')

    data = {'refresh': token}
    token_endpoint = 'http://127.0.0.1:8000/api/token/refresh/'

    response = requests.post(token_endpoint, json=data)
    response_data = response.json()

    if response.status_code == 401:
        print('new one')
        credentials = get_credentials()
    else:
        # print('refreshed')
        credentials['access'] = response_data['access']

    with open('creds.json', 'w') as outfile:
        json.dump(credentials, outfile)

    return credentials

def get_credentials():

    credentials = None

    username = input('username?: ')
    password = getpass.getpass('password?: ')

    data = {
        'username': username,
        'password': password
    }

    token_endpoint = 'http://127.0.0.1:8000/api/token/'

    response = requests.post(token_endpoint, json=data)
    credentials = response.json()

    with open('creds.json', 'w') as outfile:
        json.dump(credentials, outfile)

    return credentials


def get_protein_data(taxa_id):

    credentials = None
    protein_data = None
    response = None

    endpoint = f'http://127.0.0.1:8000/api/protein/{taxa_id}/'

    if os.path.exists('creds.json'):
        with open('creds.json', 'r') as infile:
            credentials = json.load(infile)
    else:
        credentials = get_credentials()

    print(credentials)
    if credentials:
        
        response = None

        access = credentials.get('access')

        response = get_data(endpoint, access)

        print(response.status_code, response)

        if response.status_code == 401:

            creds = refresh()
            access = creds['access']
            response = get_data(endpoint, access)

        protein_data = response.json()

        return protein_data


def get_data(endpoint, token):

    response = None
    
    headers = {
        'Authorization': f'Bearer {token}'
    }

    try:
        response = requests.get(endpoint, headers=headers)
    except Exception as e:
        print(str(e))

    return response


data = get_protein_data(taxa_id)
print(data)
