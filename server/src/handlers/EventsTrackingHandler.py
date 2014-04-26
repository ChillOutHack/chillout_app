from datetime import datetime
import json
import pprint
from services.EventTrackingService import EventTrackingService

class EventTrackingHandler(object):

    EVENTS_FILE = "data/sample.json"

    @staticmethod
    def update_event(data):
        """
            Add a new event, or update an existing one (if id is provided): 
            determine name and time, add this to whatever data was passed in.
        """
        # parse the request
        events = EventTrackingHandler.get_events()

        # add id, if necessary, and timestamp
        if "id" not in data:
            data["id"] = EventTrackingHandler.get_id()
        data["time"] = str(datetime.now())
        return 'new event: ' + pprint.pformat(data)

    @staticmethod
    def get_events():
        """
            Parse file to get all current events.
        """
        return json.loads(open(EventTrackingHandler.EVENTS_FILE).read())

    @staticmethod
    def get_id():
        """
            Find the next new id, by linearly searching all events.
            Joys of flat file storage.
        """
        id = 1 
        events = EventTrackingHandler.get_events()
        for event in events:
            if ("id" in event and event["id"] >= id):
                id = event["id"] + 1
        return id
