#
# Post Models
#
# This is the post class. It's the most fundamental unit of media in the app.
#
# posts/models.py
#

from app import db

message_len = 500

class Base(db.Model):
    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Post(Base):
    __tablename__ = "posts"

    message = db.Column(db.String(message_len))

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "<Post: %r>" % self.message

    def getMessage():
        return self.message

    def setMessage(newMessage):
        self.message = newMessage
