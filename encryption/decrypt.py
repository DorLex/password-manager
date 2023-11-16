from copy import deepcopy

from .create_crypto import fernet


def get_decrypt_password(password):
    """Шифруем пароль"""
    decrypt_password = fernet.decrypt(password.encode()).decode()
    return decrypt_password


def get_decrypt_data(data):
    decrypt_data = data.copy()  # Делаем копию, т. к. QueryDict из request.data неизменяемый
    password = data.get('password')
    decrypt_data['password'] = get_decrypt_password(password)

    return decrypt_data


def get_many_decrypt_data(many_data):
    many_decrypt_data = deepcopy(many_data)  # Делаем копию, т. к. QueryDict из request.data неизменяемый

    for data in many_decrypt_data:
        password = data.get('password')
        data['password'] = get_decrypt_password(password)

    return many_decrypt_data
