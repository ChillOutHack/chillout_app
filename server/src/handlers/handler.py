import json
import pprint

def activate(data):
    events = json.loads(open("data/sample.json").read())
    return 'i have ' + str(len(events)) + ' events: ' + pprint.pformat(data)

