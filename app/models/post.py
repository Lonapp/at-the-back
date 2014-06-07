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

	def __init__(self, id, message):
		self.id = id
		self.message = message
	
	def __repr__(self):
		return "<Post: %r>" % self.message
	
	def getMessage():
		return self.message
	
	def setMessage(newMessage):
		self.message = newMessage
