from flask import Flask
from flask import current_app

@current_app.route("/")
def index():
    return "Welcome to Lon!"
