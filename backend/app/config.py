import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_URL = os.getenv("DB_URL")
    JWT_SECRET = os.getenv("JWT_SECRET")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

settings = Settings()