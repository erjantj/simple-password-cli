"""The password service."""
import os
import sys
import getpass
import pickle
import json
import base64

from passlib.hash import sha256_crypt
from cryptography.fernet import Fernet

DATA_PATH = '/usr/local/etc/simple-password'
DATA_FILE = 'data.pickle'
ENCODING = 'utf-8'

def all():
    data = get_data()
    return data

def get(id):
    data = get_data()
    id = int(id) - 1
    try:
        return data['passwords'][id]
    except IndexError:
        print('Password not found', (id+1))
        sys.exit(1)

def change(old_password, new_password):
    data = get_data()    
    if not check_hash(old_password, data['master_password']):
        print('Error: Master password mismatch.')
        sys.exit(1)

    for i in range(len(data['passwords'])):
        data['passwords'][i]['password_encrypted'] = encrypt(
            decrypt(data['passwords'][i]['password_encrypted'], old_password),
            new_password
        )

    data['master_password'] = make_hash(new_password)

    set_data(data)


def get_data():
    verify_file_path(DATA_PATH)
    file_path = os.path.join(DATA_PATH, DATA_FILE)

    try:
        pickle_off = open(file_path,'rb')
        return pickle.load(pickle_off)
    except (OSError, IOError) as e:
        return require_master_password()

"""
Data structure
{
    master_password: "",
    passwords: [{
        id,
        name,
        account_name,
        password_encrypted
    }]
}
"""
def set_data(data):
    verify_file_path(DATA_PATH)
    file_path = os.path.join(DATA_PATH, DATA_FILE)
    pickling_on = open(file_path,'wb')
    pickle.dump(data, pickling_on)
    pickling_on.close()

def verify_file_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

def require_master_password():
    print('Please, set master password to start')
    
    master_password = ''
    while not master_password:
        master_password = getpass.getpass('Master password: ')
        if not master_password:
            print('The Master password field is required')

    data = {
        'master_password': make_hash(master_password),
        'passwords': []
    }

    set_data(data)
    return data

def make_hash(string):
    return sha256_crypt.encrypt(string)
            
def check_hash(string, hash):
    return sha256_crypt.verify(string, hash)
            
def encrypt(password, master_password):
    key = Fernet.generate_key()
    merged_key = key+(master_password.encode(ENCODING))
    encryptor = Fernet(merged_key)
    ciphertext = encryptor.encrypt(password.encode(ENCODING))
    data = {
        'key': base64.b64encode(key).decode(ENCODING), 
        'ciphertext': base64.b64encode(ciphertext).decode(ENCODING), 
    }

    data_string = json.dumps(data)
    return pack(data_string)


def decrypt(packed_string, master_password):
    data_string = unpack(packed_string)
    password_encrypted_data = json.loads(data_string)
    key = base64.b64decode(password_encrypted_data['key'])
    ciphertext = base64.b64decode(password_encrypted_data['ciphertext'])
    merged_key = key+(master_password.encode(ENCODING))
    decryptor = Fernet(key)

    return decryptor.decrypt(ciphertext).decode(ENCODING)

def pack(data_string):
    return base64.b64encode(data_string.encode(ENCODING)).decode(ENCODING)

def unpack(packed_string):
    return base64.b64decode(packed_string)


def create(name, account_name, password, master_password):
    data = get_data()    

    if not check_hash(master_password, data['master_password']):
        print('Error: Master password mismatch.')
        sys.exit(1)

    password_record = {
        'name': name,
        'account_name': account_name,
        'password_encrypted': encrypt(password, master_password)
    }

    data['passwords'].append(password_record)
    set_data(data)

    return password_record

def unlock(id, master_password):
    data = get_data()    
    if not check_hash(master_password, data['master_password']):
        print('Error: Master password mismatch.')
        sys.exit(1)

    password_record = get(id)

    return decrypt(password_record['password_encrypted'], master_password)

def delete(id, master_password):
    data = get_data()    
    if not check_hash(master_password, data['master_password']):
        print('Error: Master password mismatch.')
        sys.exit(1)

    password_record = get(id)

    data = get_data()
    data['passwords'].pop((int(id)-1))

    set_data(data)
