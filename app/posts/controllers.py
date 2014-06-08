from flask import Blueprint, request, redirect, url_for

from app import db
from app.posts.models import Post

posts = Blueprint('posts', __name__, url_prefix='/posts')

@posts.route('/', methods = ['GET'])
def index():
    return "GET Posts"
