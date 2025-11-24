from cryptography.fernet import Fernet

from core.envs import env_config

key: str = env_config.cryptography_key

fernet = Fernet(key)
