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

@app.route("/activate")
def activate():
    return handler.activate(request.query_string)

@app.route("/deactivate")
def inactivate():
    return handler.deactivate()

if __name__ == "__main__":
    app.run(debug=True)
