import os
from dotenv import load_dotenv
from datetime import timedelta

class Config(object):
    load_dotenv()
    # Get secret key from environment variable or use a default one
    CALENDAR_ID = os.getenv('CALENDAR_ID')
    # Google API key
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    # Flask app
    FLASK_APP = os.getenv('FLASK_APP')
    # SQL URI
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    # JWT key
    JWT_SECRET_KEY="please-remember-to-change-me"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)