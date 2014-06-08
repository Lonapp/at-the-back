#
# app/__init__.py
#

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Build the application
app = Flask(__name__)
app.config.from_object('config')

# Build the database object
db = SQLAlchemy(app)

# Include modules
from app.posts.controllers import posts as posts_module
from app.users.controllers import users as users_module

# Register modules
app.register_blueprint(posts_module)
app.register_blueprint(users_module)

# This will create the database file
db.create_all()
