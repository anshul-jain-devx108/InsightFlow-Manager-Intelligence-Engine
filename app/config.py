import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

class Settings:
    APP_NAME: str = "People Insights"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./people_insights.db")
    EMAIL_FROM: str = os.getenv("EMAIL_FROM")
    SMTP_SERVER: str = os.getenv("SMTP_SERVER")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", 587))
    SMTP_USERNAME: str = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD")

settings = Settings()
