from flask import Blueprint, request
from services.EventsTrackingHandler import EventTrackingHandler

api = Blueprint('api', __name__, template_folder='templates')

@api.route("/clear")
def clear():
    """
        Clear all user data.
    """
    return EventTrackingHandler.clear_events()

@api.route("/data")
def data():
    """
        Route handler to fetch all events.
    """
    return EventTrackingHandler.get_events(request.args.to_dict())

@api.route("/update")
def update():
    """
        Route handler to update an event.
    """
    return EventTrackingHandler.update_event(request.args.to_dict())
