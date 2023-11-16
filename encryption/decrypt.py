from .create_crypto import fernet


def get_decrypt_password(password):
    decrypt_password = fernet.decrypt(password.encode()).decode()
    return decrypt_password


def get_decrypt_data(data):
    password = data.get('password')
    data['password'] = get_decrypt_password(password)

    return data
