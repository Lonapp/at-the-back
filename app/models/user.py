#
# User Model
#
# This is the user class. It uses the graph database to store its information
# into nodes. Each node in the graph is a user.

from flask import g

db = getattr(g, 'db', None)

class User(db.Model):
	__tablename__ = "users"
	
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128))
	password = db.Column(db.String(40)) #TODO encrypt


