# TODO: Creates routes, custom error hadnlers for the application

# imports
from cafes import app
from flask import render_template


# simple home page setup
@app.route("/home")
@app.route("/index")
@app.route("/")
def home():
    return render_template("index.html")
