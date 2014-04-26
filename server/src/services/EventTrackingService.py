from types import DictType
from datetime import datetime

class EventTrackingService (object):
    """
        Implementation of a service handling that tracks individual events.
        Not done
    """

    @staticmethod
    def track_event (eventObject):
        """
            Tracks an event, for now accepts a Dictionary... might turn into JSON string, or individual params?

            @type eventObject: DictType
        """
        assert isinstance(eventObject, DictType)

    @staticmethod
    def fetch_events (start_time, end_time):
        """
            Fetches events that fall between the L{start_time} and L{end_time}.

            @type start_time: datetime
            @type end_time: datetime
            @precondition: start_time < end_time
        """
        assert isinstance(start_time, datetime), type(start_time)
        assert isinstance(end_time, datetime), type(end_time)
        assert start_time < end_time

