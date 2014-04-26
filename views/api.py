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
        Route handler for data resources.
    """
    return EventTrackingHandler.update_event(request.args.to_dict())
