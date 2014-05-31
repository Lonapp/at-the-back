#
# Models
#
# This could and probably should be split into individual model files
# such as app/models/user.py instead of app/models.py
#

from flask import g

db = getattr(g, 'db', None)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128))

