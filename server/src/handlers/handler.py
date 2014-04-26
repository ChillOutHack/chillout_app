import json
import pprint

def activate(query):
    events = json.loads(open("data/sample.json").read())
    return 'just for one day'
#    return 'i have ' + str(len(events)) + ' events: ' + pprint.pformat(query)

def deactivate():
    return 'i have been deactivated'
