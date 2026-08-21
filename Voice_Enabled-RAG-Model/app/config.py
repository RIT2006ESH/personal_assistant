# app/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    ollama_api_key: str
    # Add other configuration settings here

    class Config:
        env_file = ".env"

settings = Settings()
