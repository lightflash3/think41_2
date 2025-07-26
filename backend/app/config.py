from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"

    class Config:
        env_file = ".env"

settings = Settings()
