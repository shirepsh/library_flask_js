from flask import render_template, Blueprint

"""
in this file we are defining the core blue print setting & wrote all the end points that related to core (homepage)
"""

core = Blueprint('core', __name__, template_folder='templates')

@core.route("/")
def home():
    return render_template('homePage.html')