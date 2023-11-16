from cryptography.fernet import Fernet
from django.conf import settings

key = settings.CRYPTOGRAPHY_KEY

fernet = Fernet(key)
