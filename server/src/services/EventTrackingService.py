from data.Engine import connection
from types import ListType, DictType, IntType
from datetime import datetime
import sqlite3

class EventTrackingService (object):
    """
        Implementation of a service handling that tracks individual events.
        Not done
    """
    def __init__(self):
        self.cursor = connection.cursor()

    def track_event(self, events):
        """
            Tracks an event, for now accepts a Dictionary... might turn into JSON string, or individual params?

            @type events: ListType
        """

        self.fetch_events(None, None)

        assert isinstance(events, ListType)
        for e in events:
            EventTrackingService.__save_event(e)

        return events

    def fetch_events(self, start_time, end_time):
        """
            Fetches events that fall between the L{start_time} and L{end_time}.

            @type start_time: datetime
            @type end_time: datetime
            @precondition: start_time < end_time
        """
        #assert isinstance(start_time, datetime), type(start_time)
        #assert isinstance(end_time, datetime), type(end_time)
        #assert start_time < end_time

        #this is crap...
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * from events")
        print c.fetchone()

    def __save_event(self, event_type, time_stamp, skin_temp, peltier_temp, delta_temp, voltage):
        """
            This contract is fucked
            @type event_type: IntType
            @type time_stamp:
        """
        #assert isinstance(event, DictType), type(event)
        #c = connection.cursor()

        row_args = {
            'event_type': event_type,
            'time_stamp': time_stamp,
            'skin_temp': skin_temp,
            'peltier_temp': peltier_temp,
            'delta_temp': delta_temp,
            'voltage': voltage
        }

        #inline sql for now
        exec_cmd = "INSERT INTO events VALUES (%(event_type), %(time_stamp), %(skin_temp), %(peltier_temp), %(delta_temp), %(voltage))" % row_args
        self.cursor.execute(exec_cmd)
        connection.commit()


    __EVENT_PARMS = ('event_type',
                     'time_stamp',
                     'skin_temp',
                     'peltier_temp',
                     #'delta_temp',
                     'voltage')