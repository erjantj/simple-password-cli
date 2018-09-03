"""Api client."""

import requests
from requests import ConnectTimeout
import pickle
import sys

baseUrl = 'http://localhost:8000/api/v1'
timeout = 10

def post(action, data={}, headers={}):
    url = "{baseUrl}/{action}".format(baseUrl=baseUrl, action=action)

    try:
        return requests.post(url, data=data, headers=headers, timeout=timeout)
    except ConnectTimeout as e:
        print('Connection timeout to:', url)
    except Exception as e:
        print(e, baseUrl)

def get(action, data={}, headers={}):
    url = "{baseUrl}/{action}".format(baseUrl=baseUrl, action=action)
    try:
        return requests.get(url, data=data, headers=headers, timeout=timeout)
    except ConnectTimeout as e:
        print('Connection timeout to:', url)
    except Exception as e:
        print(e, baseUrl)

def delete(action, data={}, headers={}):
    url = "{baseUrl}/{action}".format(baseUrl=baseUrl, action=action)
    try:
        return requests.delete(url, data=data, headers=headers, timeout=timeout)
    except ConnectTimeout as e:
        print('Connection timeout to:', url)
    except Exception as e:
        print(e, baseUrl)

def get_token():
    pickle_off = open("auth.pickle","rb")
    return pickle.load(pickle_off)

def set_token(api_key):
    pickling_on = open("auth.pickle","wb")
    pickle.dump(api_key, pickling_on)
    pickling_on.close()

def authorized(func):
    def wrapper(*args):
        api_key = get_token()
        if not api_key:
            print('Invalid token, please login')
            sys.exit(1)
        return func(*args)
    return wrapper

def auth_token(func):
    def wrapper(*args):
        api_key = get_token()
        if not api_key:
            print('Invalid token, please login')
            sys.exit(1)
        return func({'Authorization': 'Bearer ' + api_key}, *args)
    return wrapper

def me():
    action = 'me'
    data = {}
    headers = {
        'Authorization': 'Bearer ' + get_token()
    }

    response = get(action, data, headers)
    if response.ok:
        return response.json()
    return False
