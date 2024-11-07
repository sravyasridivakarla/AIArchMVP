from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

@lru_cache()
def get_settings():
    try:
        settings = Settings()
        # Debug print - remove in production
        if settings.OPENAI_API_KEY.startswith('sk-'):
            print(settings.OPENAI_API_KEY)
        else:
            print("Warning: API key doesn't start with 'sk-'")
        return settings
    except Exception as e:
        print(f"Error loading settings: {e}")
        print(f"Current OPENAI_API_KEY value: {os.getenv('OPENAI_API_KEY')}")
        raise 