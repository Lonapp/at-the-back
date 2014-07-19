#
# app/__init__.py
#

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from py2neo import neo4j

# Build the application
app = Flask(__name__)
app.config.from_object('config')

# Build the database object
db = SQLAlchemy(app)

graph_db = neo4j.GraphDatabaseService(app.config['NEO4J_DATABASE_URI'])

# Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Include modules
from app.base.controllers import BaseModel as base_module
from app.auth.controllers import auth as auth_module
from app.posts.controllers import posts as posts_module
from app.users.controllers import users as users_module
from app.comments.controllers import comments as comments_module
from app.colors.controllers import colors as colors_module

# Register modules
#app.register_blueprint(base_module)
app.register_blueprint(auth_module)
app.register_blueprint(posts_module)
app.register_blueprint(users_module)
app.register_blueprint(comments_module)
app.register_blueprint(colors_module)

# This will create the database file
db.create_all()
