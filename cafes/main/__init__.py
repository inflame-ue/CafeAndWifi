# TODO: Create a main blueprint for the application

# imports
from flask import Blueprint

# init the blueprint
main = Blueprint("main", __name__)

# import the routes and error handlers, to avoid circular imports
from . import errors, routes
