import json
import pprint
from services.EventTrackingService import EventTrackingService

class EventTrackingHandler(object):

    EVENTS_FILE = "data/sample.json"

    @staticmethod
    def add_event(data):
        """
            Handles adding events.
        """
        # parse the request
        events = json.loads(open(EventTrackingHandler.EVENTS_FILE).read())

        #for now return a stringified list of the response of track_event
        return str(EventTrackingService.track_event(events))
