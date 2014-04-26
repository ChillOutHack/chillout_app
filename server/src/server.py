from flask import Flask, render_template, request
from handlers.EventsTrackingHandler import EventTrackingHandler

app = Flask(__name__)

#for now define routes inline with server.py
@app.route("/")
def render_main():
    """
        Renders the main (base) page.
    """
    return render_template("main.html")

@app.route("/clear")
def clear():
    """
        Clear all user data.
    """
    return EventTrackingHandler.clear_events()

@app.route("/data")
def data():
    """
        Route handler for data resources.
    """
    pairs = request.query_string.split('&')
    data = {}
    for pair in pairs:
        (key, value) = pair.split("=")
        data[key] = value
    return EventTrackingHandler.update_event(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
