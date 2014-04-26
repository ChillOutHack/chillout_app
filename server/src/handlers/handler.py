import json
import pprint

EVENTS_FILE = "data/sample.json"

def add_event(data):
    events = json.loads(open(EVENTS_FILE).read())
    return 'i have ' + str(len(events)) + ' events: ' + pprint.pformat(data)
