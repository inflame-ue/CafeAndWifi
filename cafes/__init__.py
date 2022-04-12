# imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
from config import configs

# init extensions
bootstrap = Bootstrap()


# sqlalchemy setup
class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    Integer: Callable
    Float: Callable
    String: Callable
    Boolean: Callable
    Text: Callable
    ForeignKey: Callable


db = MySQLAlchemy()


# application factory
def create_app(config_name):
    # init the app
    app = Flask(__name__)
    app.config.from_object(configs[config_name])
    configs[config_name].init_app(app)

    # init the extensions(properly)
    bootstrap.init_app(app)
    db.init_app(app)

    # register the blueprints to the application
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
