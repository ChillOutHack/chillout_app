from datetime import datetime
import json
import pprint
from flask import current_app

class EventTrackingHandler(object):

    @staticmethod
    def clear_events():
        from server import db, Event
        db.session.query(Event).all().delete()
        db.session.commit()

    @staticmethod
    def get_events():
        """
            Fetches all events

            @rtype: StringType
        """
        events = EventTrackingHandler.read_events()
        return json.dumps([event.to_dict() for event in events])

    @staticmethod
    def update_event(data):
        """
            Add a new event, or update an existing one (if id is provided): 
            determine name and time, add this to whatever data was passed in.

            @type date: DictType
        """
        from server import db, Event
        # parse the request
        events = EventTrackingHandler.read_events()

        if "id" in data:
            # Editing existing event: find event and overwrite any keys in given data
            ev = db.session.query(Event).filter(Event.id == data['id'])
            if ev.count() == 1:
                for key, value in data.items():
                    setattr(ev[0], key, value)
            db.session.commit()
        else:
            EventTrackingHandler.write_event(data)

        """
            Return value irrelevant; print events for testing purposes.
        """
        return '<pre>' + pprint.pformat(events) + '</pre>'

    @staticmethod
    def read_events():
        from server import db, Event
        events = db.session.query(Event).all()
        return events

    @staticmethod
    def write_event(event):
        from server import db, Event
        event = Event(
            peltier=event['peltier'],
            pentiometer=event['potentiometer'],
            temp=event['temperature']
        )
        db.session.add(event)
        db.session.commit()
