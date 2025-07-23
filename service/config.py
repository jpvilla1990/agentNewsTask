from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """
    Configuration settings for the application.
    """    
    # Search Configuration
    SEARCH_URL: str = Field(default="SEARCH_URL")
    SEARCH_KEY: str = Field(default="SEARCH_KEY")
    # Scraper Configuration
    SCRAPER_URL: str = Field(default="SCRAPER_URL")
    SCRAPER_KEY: str = Field(default="SCRAPER_KEY")
    # OpenAI Configuration
    OPENAI_API_KEY: str = Field(default="OPENAI_API_KEY")

    SMTP_SERVER: str = Field(default="SMTP_SERVER")
    SMTP_PORT: str = Field(default="SMTP_PORT")

    SMTP_USERNAME: str = Field(default="SMTP_USERNAME")
    SMTP_PASSWORD: str = Field(default="SMTP_PASSWORD")

    class Config:
        env_file = ".env"