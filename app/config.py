import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    # Nueva forma de indicar el .env
    model_config = SettingsConfigDict(env_file=".env")

    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool = False
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    BASE_DATOS_DOCKER: str = Field(..., env="BASE_DATOS_DOCKER")
    
    # Agrega la URL base de tu auth_api (puede venir de .env)
    AUTH_API_URL: str = Field(..., env="AUTH_API_URL")
    

settings = Settings()