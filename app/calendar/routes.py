from flask import Blueprint, jsonify

from app.calendar.calendar_functions import get_next_event

bp = Blueprint('calendar', __name__, url_prefix='/calendar')

@bp.route('/next-event', methods=['GET'])
def get_next_calendar_event():
    # Logic to fetch events from the Google Calendar API using calendar_services
    events = get_next_event()
    # Return the events as JSON
    return jsonify(events)
