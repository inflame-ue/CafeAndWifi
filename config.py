# TODO: Create configs for the project

# imports
import dotenv
import os
import secrets

# constants
basedir = os.path.abspath(os.path.dirname(__file__))

# load .env file from the local system
dotenv.load_dotenv("C://EnvironmentalVariables//.env")


# create a base config
class BaseConfig:
    SECRET_KEY = os.environ.get("MY_SECRET_KEY") or secrets.token_hex(64)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    CAFES_MAIL_SUBJECT_PREFIX = "[Cafes]"
    CAFES_MAIL_SENDER = "Flasky Admin <youremail@gmail.com>"
    CAFES_ADMIN = os.environ.get("CAFES_ADMIN")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") or \
        f"sqlite:///{os.path.join(basedir, 'cafes-dev.db')}"


class TestingConfig(BaseConfig):
    Testing = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI") or \
        f"sqlite:///{os.path.join(basedir, 'cafes-test.db')}"


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or \
        f"sqlite:///{os.path.join(basedir, 'cafes.db')}"


configs = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig,
}
