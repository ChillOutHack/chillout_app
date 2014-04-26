from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates')

@main.route("/")
def render_main():
    """
        Renders the main (base) page.
    """
    return render_template("main.html")