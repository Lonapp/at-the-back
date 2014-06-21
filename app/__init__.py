#
# app/__init__.py
#

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy
from py2neo import neo4j

# Build the application
app = Flask(__name__)
app.config.from_object('config')

# Build the database object
db = SQLAlchemy(app)

graph_db = neo4j.GraphDatabaseService(app.config['NEO4J_DATABASE_URI'])

# Include modules
from app.base.controllers import BaseModel as base_module
from app.posts.controllers import posts as posts_module
from app.users.controllers import users as users_module
from app.comments.controllers import comments as comments_module

# Register modules
#app.register_blueprint(base_module)
app.register_blueprint(posts_module)
app.register_blueprint(users_module)
app.register_blueprint(comments_module)

# This will create the database file
db.create_all()
