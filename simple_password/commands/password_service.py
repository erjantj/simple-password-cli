"""The password service."""

from .api import auth_token
from . import api
import sys

@auth_token
def all(headers):
    action='password'
    response = api.get(action, {}, headers)
    response_body = response.json()
    if response.ok:
        return response_body
    return []

@auth_token
def get(headers, id):
    action='password'
    response = api.get(action, {}, headers)
    response_body = response.json()
    id = int(id)
    if response.ok:
        for row in response_body:
            if row['id'] == id:
                return row

    print('Password not found', id)
    sys.exit(1)

@auth_token
def unlock(headers, id, master_password):
    action='password/unlock/{id}'.format(id=id)
    data = {
        'master_password': master_password
    }
    response = api.post(action, data, headers)
    response_body = response.json()
    if response.ok:
        return response_body['password']
        
    print('Problem occurred while unlocking password', id)
    print(response_body)
    sys.exit(1)

@auth_token
def create(headers, name, account_name, password):
    action='password'
    data = {
        'name': name,
        'account_name': account_name,
        'password': password
    }

    response = api.post(action, data, headers)
    response_body = response.json()
    if response.ok:
        return response_body
    
    print('Problem occurred while creating new password')
    print(response_body)
    sys.exit(1)

@auth_token
def update(headers, id, name, account_name, password, master_password):
    action='password/{id}'.format(id=id)
    data = {
        'name': name,
        'account_name': account_name,
        'password': password,
        'master_password': master_password
    }

    response = api.post(action, data, headers)
    response_body = response.json()
    if response.ok:
        return response_body
        
    print('Problem occurred while updating password')
    print(response_body)
    sys.exit(1)

@auth_token
def delete(headers, id, master_password):
    action='password/{id}'.format(id=id)
    data = {
        'master_password': master_password
    }

    response = api.delete(action, data, headers)
    response_body = response.json()
    if response.ok:
        return response_body
        
    print('Problem occurred while deleting password')
    print(response_body)
    sys.exit(1)

@auth_token
def change(headers, old_password, new_password, new_password_confirmation):
    action='master-password'
    data = {
        'old_password': old_password,
        'new_password': new_password,
        'new_password_confirmation': new_password_confirmation,
    }

    response = api.post(action, data, headers)
    response_body = response.json()
    if response.ok:
        return response_body
        
    print('Problem occurred while changing master password')
    print(response_body)
    sys.exit(1)
