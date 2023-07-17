from flask import current_app
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
from dateutil.parser import parse



import datetime

def get_next_event():
    api_key = current_app.config.get('GOOGLE_API_KEY')
    calendar_id = current_app.config.get('CALENDAR_ID')
    session = build('calendar', 'v3', developerKey=api_key)
    # Get current time of request, to get the nearest meeting
    now = datetime.datetime.utcnow().isoformat() + 'Z'  

    # Make API call to get the soonest calendar item
    event_result = session.events().list(
        calendarId=calendar_id,
        timeMin=now,
        maxResults=1,
        singleEvents=True,
        orderBy='startTime'
    ).execute().get('items', [])
    # If no event to get, return None
    if not event_result:
        return None
    # Parse and return only the information needed by the website
    
    closest_event = event_result[0]

    start_time = datetime.datetime.strptime(closest_event['start']['dateTime'], '%Y-%m-%dT%H:%M:%S%z')
    end_time = datetime.datetime.strptime(closest_event['end']['dateTime'], '%Y-%m-%dT%H:%M:%S%z')

    next_event = {
        "name": closest_event.get("summary"),
        "room": closest_event.get("location"),
        "room_number": closest_event.get("description"),
        "date": start_time.date().isoformat(),
        "start_time": start_time.strftime('%I:%M %p'),  # Format time as 12-hour clock
        "end_time": end_time.strftime('%I:%M %p')  # Format time as 12-hour clock
    }

    return next_event

