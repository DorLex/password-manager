from .create_crypto import fernet


def get_encrypt_password(password):
    """Дешифруем пароль"""
    encrypt_password = fernet.encrypt(password.encode()).decode()
    return encrypt_password


def get_encrypt_data(data):
    encrypt_data = data.copy()  # Делаем копию, т. к. QueryDict из request.data неизменяемый
    password = data.get('password')
    encrypt_data['password'] = get_encrypt_password(password)

    return encrypt_data
