from .create_crypto import fernet


def get_encrypted_password(password: str) -> str:
    """Шифруем пароль"""

    encrypt_password: str = fernet.encrypt(password.encode()).decode()
    return encrypt_password
