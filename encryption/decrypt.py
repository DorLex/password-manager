from .create_crypto import fernet


def decrypt_password(encrypted_password: str):
    """Дешифруем пароль"""

    decrypt_password = fernet.decrypt(encrypted_password.encode()).decode()
    return decrypt_password


def get_decrypt_data(data: dict) -> dict:
    encrypted_password: str = data.get('encrypted_password')
    data['password'] = decrypt_password(encrypted_password)

    return data


def get_many_decrypt_data(many_data: list[dict]) -> list[dict]:
    for data in many_data:
        encrypted_password = data.get('encrypted_password')
        data['password'] = decrypt_password(encrypted_password)

    return many_data
