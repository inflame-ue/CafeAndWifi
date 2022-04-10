# TODO: Create basic flask application with basic application structure

# imports
from flask import Flask
import dotenv
import os

# load dotenv file
dotenv.load_dotenv("C://EnvironmentalVariables//.env")

# application initialization
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = os.environ.get("MY_SECRET_KEY") or "hard_to_guess_string"

# handle circular imports
from cafes import routes
