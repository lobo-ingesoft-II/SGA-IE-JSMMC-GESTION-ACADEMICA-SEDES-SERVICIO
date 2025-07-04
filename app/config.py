from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Nueva forma de indicar el .env
    model_config = SettingsConfigDict(env_file=".env")

    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool = False
    CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:3000"]
    HOST: str = "127.0.0.1"
    PORT: int = 8000

settings = Settings()
