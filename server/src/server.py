from handlers import handler
from flask import Flask, render_template, request
app = Flask(__name__)

#for now define routes inline with server.py
@app.route("/")
def render_main():
    """
        Renders the main (base) page.
    """
    return render_template("main.html")

@app.route("/data")
def data():
    pairs = request.query_string.split('&')
    data = {}
    for pair in pairs:
        (key, value) = pair.split("=")
        data[key] = value
    return handler.update_event(data)

if __name__ == "__main__":
    app.run(debug=True)
