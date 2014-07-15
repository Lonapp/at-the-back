from flask import Blueprint, request, redirect, url_for

from sqlalchemy.ext.serializer import dumps
from sqlalchemy.orm import sessionmaker

import json

from app import db
from app.posts.models import Post

posts = Blueprint('posts', __name__, url_prefix='/posts')

@posts.route('/', methods = ['GET'])
def index():
    return json.dumps([i.json for i in Post.query.all()])

@posts.route('/<post_id>', methods = ['GET'])
def getPost(post_id):
    #TODO refactor
    return json.dumps([i.json for i in Post.query(Post).get(post_id)])


@posts.route('/<post_id>/voters', methods = ['GET'])
def getPostVoters(post_id):
    pass

@posts.route('/<post_id>/lonners', methods = ['GET'])
def getPostLonners(post_id):
    pass

@posts.route('/<post_id>', methods = ['DELETE'])
def deletePost(post_id):
    #TODO refactor
    #DO we delete all lonned posts too?
    ThePost = Post.query(Post).get(post_id)
    Post.delete(ThePost)
    #see the count and return 200 OK if 0, 404 otherwise
    return True

@posts.route('/<post_id>/lon', methods = ['POST'])
def lonPost(post_id):
    pass

@posts.route('/', methods = ['POST'])
def postPost():
    # Create new post
    post = Post(request.form['message'])

    # Commit new post to db
    post.save()

    # Respond with completed post object
    return json.dumps(post.json)

@posts.route('/<post_id>/comments/<user_id>', methods = ['GET'])
def getComment(post_id,user_id):
    pass

@posts.route('/<post_id>/comments/<user_id>/voters', methods = ['GET'])
def getCommentVoters(post_id, user_id):
    pass

@posts.route('/<post_id>/comments', methods = ['PUT'])
def editComment(post_id):
    #see the user logged in and give them access if the post is their's
    pass

@posts.route('/<post_id>/comments/<user_id>', methods = ['DELETE'])
def deleteComment(post_id, user_id):
    pass


@posts.route('/<post_id>/comments/<user_id>', methods = ['POST'])
def postComment(post_id,user_id):
    pass


@posts.route('/<post_id>/comments/<user_id>/vote', methods = ['POST'])
def postCommentVote(post_id,user_id):
    pass


