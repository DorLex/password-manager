from .create_crypto import fernet


def get_encrypt_password(password):
    encrypt_password = fernet.encrypt(password.encode()).decode()
    return encrypt_password


def get_encrypt_data(data):
    password = data.get('password')
    data['password'] = get_encrypt_password(password)

    return data
