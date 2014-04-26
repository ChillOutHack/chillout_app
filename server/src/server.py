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
    return EventTrackingHandler.update_event(request.args.to_dict())

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
