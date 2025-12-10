from cryptography.fernet import Fernet

from core.envs import env_config

fernet: Fernet = Fernet(env_config.cryptography_key)
