from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_secret: str = "change-me-in-production"
    firebase_credentials: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
