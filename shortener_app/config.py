from pydantic import BaseSettings
from functools import lru_cache

"""
The Settings class that you defined is a subclass of BaseSettings. 
The BaseSettings class comes in handy to define environment variables in your application. 
You only have to define the variables that you want to use, and pydantic takes care of the rest. 
In other words, pydantic will automatically assume those default values 
if it doesn’t find the corresponding environment variables. 
"""

class Settings(BaseSettings):
    env_name: str = "Local"     # name of current environment
    base_url: str = "http://localhost:8000"     # Domain of app
    db_url: str = "sqlite:///./shortener.db"        # Address of database

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for {settings.env_name}")
    return settings


