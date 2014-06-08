from flask import Blueprint, request, redirect, url_for

from app import db
from app.users.models import User

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/', methods = ['GET'])
def index():
    return "GET Users"
