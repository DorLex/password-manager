from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvConfig(BaseSettings):
    # Backend
    django_secret_key: str
    django_debug: bool = False
    cryptography_key: str

    # Database
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


env_config: EnvConfig = EnvConfig()
