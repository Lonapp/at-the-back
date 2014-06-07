#
# Post Models
#
# This is the post class. It's the most fundamental unit of media in the app.

from flask import g

db = getattr(g, 'db', None)
message_len = 500

class Post(db.Model):
	__tablename__ = "posts"
	
    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String(message_len))
