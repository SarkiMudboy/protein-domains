import requests


ROOT_URL = 'http://127.0.0.1:8000/api/'

token_urls = {
    'api_token_auth': ROOT_URL + 'login/',
    'token': ROOT_URL + 'token/',
    'refresh': ROOT_URL + 'token/refresh/',
}

# user data
create_user_data = {
    'username': 'sdotgo02',
    'password': 'abdulsamad',
    'password2': 'abdulsamad',
    'email': 'sdotgo@gmail.com'
}

login_data = {
    'username': create_user_data.get('username'),
    'password': create_user_data.get('password')
}

partial_update_user_data = {
    'username': 'ursulaaa101'
}

update_user_data = partial_update_user_data | {'password': '2580twice', 'email': 'resesd@email.com'}


# create a user

# create_user_response = requests.post(ROOT_URL + 'register/', create_user_data)
# print(create_user_response.json())


# obtain token
print(login_data)
obtain_token_response = requests.post(token_urls.get('api_token_auth'), data=login_data)
response_data = obtain_token_response.json()
print(response_data)
# token = response_data.get('token')
# user_id = response_data.get('user_id')


# get a user

# construct the auth header

# token = 'd919c28af0b5f825d47a7b566da7570282fe8d4b'
# auth = {'Authorization': 'Bearer ' + token}
# print(auth)
# user_id = 9

# get_response = requests.get(ROOT_URL + 'researchers/' + str(user_id), headers=auth)
# user = get_response.json()
# print(user, get_response.status_code)


# update a user
# update_response = requests.put(ROOT_URL + 'researchers/')

o = {
    "username":"swelle22",
    "password": "2580twice"
}
p = {
    "username":"sdotgo02",
    "password": "abdulsamad"
}