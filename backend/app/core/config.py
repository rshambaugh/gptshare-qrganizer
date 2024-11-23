from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "QRganizer"
    database_url: str = "sqlite:///./test.db"  # Update with your database URL

    class Config:
        env_file = ".env"

settings = Settings()
