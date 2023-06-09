from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    # DATABASE_PORT: int
    # POSTGRES_PASSWORD: str
    # POSTGRES_USER: str
    # POSTGRES_DB: str
    # POSTGRES_HOST: str
    # POSTGRES_HOSTNAME: str
    #
    # JWT_PUBLIC_KEY: str
    # JWT_PRIVATE_KEY: str
    # REFRESH_TOKEN_EXPIRES_IN: int
    # ACCESS_TOKEN_EXPIRES_IN: int
    # JWT_ALGORITHM: str
    # CLIENT_ORIGIN: str
    BOT_TOKEN: SecretStr

    class Config:
        env_file = 'default.env'
        env_file_encoding = 'utf-8'


config = Settings()
