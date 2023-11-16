from cryptography.fernet import Fernet
from django.conf import settings

# key = Fernet.generate_key()


key = settings.CRYPTOGRAPHY_KEY

fernet = Fernet(key)
