from handlers import handler
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/activate", methods=['GET', 'POST'])
def activate():
    return handler.activate()

@app.route("/deactivate", methods=['GET','POST'])
def inactivate():
    return handler.deactivate()

if __name__ == "__main__":
    app.run(debug=True)
