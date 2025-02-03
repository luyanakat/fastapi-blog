import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from sqlalchemy.engine import URL
import urllib.parse



BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
load_dotenv(os.path.join(BASE_DIR, '.env'))

def parse_conn_string() -> str:
    encoded = urllib.parse.quote_plus(os.getenv('DATABASE_URL'))
    return encoded


class Settings(BaseSettings):
    DATABASE_URL: str = parse_conn_string()
  
settings = Settings()