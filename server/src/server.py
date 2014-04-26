from flask import Flask, render_template
app = Flask(__name__)

#for now define routes inline with server.py
@app.route("/")
def render_main():
    """
        Renders the main (base) page.
    """
    return render_template("main.html")

if __name__ == "__main__":
    app.run()