#
# User Models
#
# This is the user class. Eventually it will interface
# with our authenication system.
#
# users/models.py
#

from app import db

# TODO: Abstract these Base models to app.base.model or something
class Base(db.Model):
    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class User(Base):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(40)) #TODO encrypt
