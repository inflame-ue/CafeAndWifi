# TODO: Create models that will reflect an already existing database

# imports
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


# model definition
class Cafe(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, index=True, nullable=False)
    map_url = db.Column(db.String(150), unique=True, nullable=False)
    img_url = db.Column(db.String(150), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(50), nullable=False)
    coffee_price = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Cafe <{self.name}>"


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    # change the representation of the model
    def __repr__(self):
        return f"User <{self.username}>"

    # customize password property
    @property
    def password(self):
        raise AttributeError("This attribute is not readable.")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

