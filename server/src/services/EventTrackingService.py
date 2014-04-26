from types import DictType

class EventTrackingService (object):
    """
        Implementation of a service handling that tracks individual events.
        Not done
    """

    @staticmethod
    def track_event(eventObject):
        """
            Tracks an event, for now accepts a Dictionary... might turn into JSON string, or individual params?

            @type eventObject: DictType
        """
        assert isinstance(eventObject, DictType)
