# TODO: Create an authentication blueprint for the project.

# imports
from flask import Blueprint

# init the auth blueprint
auth = Blueprint("auth", __name__)

# import the routes to avoid circular imports
from . import routes
