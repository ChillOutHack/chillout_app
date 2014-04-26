from flask import Blueprint, render_template
import os
main = Blueprint('main', __name__, template_folder='templates', static_url_path='')

@main.route("/")
def render_main():
    """
    Renders the main (base) page.
    """
    return render_template("main.html")

@main.route('/<string:filepath>.<string(minlength=2, maxlength=4):extension>')
def frontend_files(filepath, extension):
    print "match file {0}".format(filepath)
    from server import app
    return app.send_static_file(os.path.join("{0}.{1}".format(filepath, extension)))

@main.route('/static/<path:filepath>.<string(minlength=2, maxlength=4):extension>')
def frontend_static_files(filepath, extension):
    print "match file {0}".format(filepath)
    from server import app
    return app.send_static_file(os.path.join("{0}.{1}".format(filepath, extension)))

@main.route('/<path:filepath>.<string(minlength=2, maxlength=4):extension>')
def frontend_path_files(filepath, extension):
    print "match file {0}".format(filepath)
    from server import app
    return app.send_static_file(os.path.join("{0}.{1}".format(filepath, extension)))