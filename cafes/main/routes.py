# imports
from flask import render_template

from . import main


# simple home page setup
@main.route("/home")
@main.route("/index")
@main.route("/")
def home():
    return render_template("index.html")
