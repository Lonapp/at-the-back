from flask import Blueprint, request, redirect, url_for

from sqlalchemy.ext.serializer import dumps
from sqlalchemy.orm import sessionmaker

from app import db
from app.posts.models import Post

posts = Blueprint('posts', __name__, url_prefix='/posts')

@posts.route('/', methods = ['GET'])
def index():
    return str([i.json for i in Post.query.all()])

@posts.route('/', methods = ['POST'])
def store():
    # Create new post
    post = Post(request.form['message'])

    # Commit new post to db
    post.save()

    # Respond with completed post object
    return str(post.json)
