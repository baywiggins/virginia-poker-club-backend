import os
from dotenv import load_dotenv

class Config(object):
    load_dotenv()
    # Get secret key from environment variable or use a default one
    CALENDAR_ID = os.getenv('CALENDAR_ID') or 'you-will-never-guess'

    # Google API key
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY') or 'poo'