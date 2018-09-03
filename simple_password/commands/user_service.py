"""The user service."""

from . import api
import sys

def login(username, password):
    action='login'
    data = {
        'email': username, 
        'password': password
    }

    response = api.post(action, data)
    response_body = response.json()
    if response.ok:
        api_key = response_body['api_key']
        api.set_token(api_key)

        return True

    print(response_body)
    return False    

def logout():
    api.set_token(None)