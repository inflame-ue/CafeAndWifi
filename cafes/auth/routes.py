# TODO: Create routes for the authentication functionality of the application

# imports
from flask import render_template, redirect, url_for, flash
from cafes.auth import auth


# login route
@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("auth/login.html")


# register route
@auth.route("/register", methods=["GET", "POST"])
def register():
    return render_template("auth/register.html")


# logout route
@auth.route("/logout")
def logout():
    pass
