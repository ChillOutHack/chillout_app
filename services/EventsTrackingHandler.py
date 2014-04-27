import json
import pprint
from types import IntType
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

        events_list = [event.to_dict() for event in EventTrackingHandler.__fetch_events()]

        return json.dumps({
            'max_peltier': max(events_list, key=lambda x: x['peltier'])['peltier'],
            'min_peltier': min(events_list, key=lambda x: x['peltier'])['peltier'],

            'max_pentiometer': max(events_list, key=lambda x: x['pentiometer'])['pentiometer'],
            'min_pentiometer': min(events_list, key=lambda x: x['pentiometer'])['pentiometer'],

            'max_temp': max(events_list, key=lambda x: x['temp'])['temp'],
            'min_temp': min(events_list, key=lambda x: x['temp'])['temp'],

            'events': events_list
        })

        return json.dumps([event.to_dict() for event in EventTrackingHandler.__fetch_events()])

    @staticmethod
    def update_event(data):
        """
            Add a new event, or update an existing one (if id is provided): 
            determine name and time, add this to whatever data was passed in.

            @type date: DictType
        """
        from server import db, Event

        if "id" in data:
            # Editing existing event: find event and overwrite any keys in given data
            ev = db.session.query(Event).filter(Event.id == data['id'])
            if ev.count() == 1:
                for key, value in data.items():
                    setattr(ev[0], key, value)
            db.session.commit()
        else:
            EventTrackingHandler.__write_event(data)

        #always return "success"
        return "success"

    @staticmethod
    def __fetch_events(num_to_fetch=None):
        """
            Fetches events sorted descendingly based on the created date.
            L{num_to_fetch} is an optional parameter

            @type num_to_fetch: IntType or None
            @rtype: GeneratorType
        """
        from server import db, Event

        if not num_to_fetch:
            return (x for x in db.session.query(Event)\
                        .order_by(Event.created.desc()))
        else:
            assert isinstance(num_to_fetch, IntType), type(num_to_fetch)

            return (x for x in db.session.query(Event)\
                        .order_by(Event.created.desc())\
                        .limit(num_to_fetch))

    @staticmethod
    def __write_event(event):
        from server import db, Event
        event = Event(
            peltier=event['peltier'],
            pentiometer=event['potentiometer'],
            temp=event['temperature']
        )
        db.session.add(event)
        db.session.commit()
