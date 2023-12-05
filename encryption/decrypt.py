from copy import deepcopy

from .create_crypto import fernet


def get_decrypt_password(password):
    """Шифруем пароль"""
    decrypt_password = fernet.decrypt(password.encode()).decode()
    return decrypt_password


def get_decrypt_data(data):
    password = data.get('password')
    data['password'] = get_decrypt_password(password)

    return data


def get_many_decrypt_data(many_data):
    for data in many_data:
        password = data.get('password')
        data['password'] = get_decrypt_password(password)

    return many_data
