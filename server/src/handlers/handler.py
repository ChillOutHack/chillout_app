from datetime import datetime
import json
import pprint

EVENTS_FILE = "data/sample.json"

'''
Add a new event, or update an existing one (if id is provided): 
determine name and time, add this to whatever data was passed in
'''
def update_event(data):
    data["id"] = get_id()
    data["time"] = datetime.now()
    return 'new event: ' + pprint.pformat(data)

'''
Parse file to get all current events.
'''
def get_events():
    return json.loads(open(EVENTS_FILE).read())

'''
Find the next new id, by linearly searching all events.
Joys of flat file storage.
'''
def get_id():
    id = 1
    events = get_events()
    for event in events:
        if ("id" in event and event["id"] >= id):
            id = event["id"] + 1
    return id
