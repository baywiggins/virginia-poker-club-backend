from flask import current_app
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime


def get_next_event():
    api_key = current_app.config.get('GOOGLE_API_KEY')
    calendar_id = current_app.config.get('CALENDAR_ID')
    session = build('calendar', 'v3', developerKey=api_key)
    
    now = datetime.datetime.utcnow().isoformat() + 'Z'  


    event_result = session.events().list(
        calendarId=calendar_id,
        timeMin=now,
        maxResults=1,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = event_result.get('items', [])
    
    if not events:
        return None

    closest_event = events[0]
    return closest_event
