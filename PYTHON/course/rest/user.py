import requests

URL = 'http://192.168.2.115:3000/user'

def get_users():
    response = requests.get(URL)
    return response.json()

def add_user(**kwargs):
    response = requests.post(URL, json=kwargs)
    return response.status_code

def update_user(id, **kwargs):
    response = requests.put(URL + f'/{id}', json=kwargs)
    return response.status_code

def delete_user(id):
    response = requests.delete(URL + f'/{id}')
    return response.status_code

def get_user(id):
    response = requests.get(URL + f'/{id}')
    return response.status_code






