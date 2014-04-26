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

        if "id" in data:
            # Editing existing event: find event and overwrite any keys in given data
            index = 0
            while index < len(events) and str(data["id"]) != str(events[index]["id"]):
                index = index + 1
            if index >= len(events):
                raise Exception("could not find event with id " + data["id"])
            for key, value in data.items():
                events[index][key] = value
        else:
            # Adding new event: set id and timestamp, then add to list
            data["id"] = events[-1]["id"] + 1
            data["time"] = str(datetime.now())
            events.append(data)
        return '<pre>' + pprint.pformat(events) + '</pre>'

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
