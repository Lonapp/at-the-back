from flask import Blueprint, request

import json

from app import db
from app.posts.models import Post
from app.comments.models import Comment
from app.colors.controllers import isColorValid
from app.base.controllers import args
from flask.ext.login import current_user, login_required

comments = Blueprint('comments', __name__, url_prefix='/posts/<post_id>/comments')

@comments.route('/<user_id>', methods = ['GET'])
def getComment(post_id, user_id):
    result = Comment.query.get((post_id, user_id))
    if result != None: json.dumps(result.json),200
    else: return '',404

@comments.route('/<user_id>/voters', methods = ['GET'])
def getCommentVoters(post_id, user_id):
    pass

@comments.route('/', methods = ['PUT'])
@login_required
@args(['message']) #new message
def editComment(post_id):
    #see the user logged in and give them access if the post is their's
    post = Post.query.get(post_id)
    if post == None: return '',404
    if post.getUser() == current_user.userid:
        comment = Comment.query.get((post_id,post.getUser()))
        print str(comment.json)
        if comment == None: return '',404
        comment.setMessage(request.form['message'])
        db.session.add(comment)
        db.session.commit()
        return '',200
    return '',403

@comments.route('/', methods = ['DELETE'])
@login_required
def deleteComment(post_id):
    result = Comment.query.get((post_id,current_user.userid))
    if result != None:
        db.session.delete(result)
        db.session.commit()
        return '',200
    else: return '',404

@comments.route('/', methods = ['POST'])
@login_required
@args(['message','color'])
def postComment(post_id):
    if existsColor(int(request.args['color'])):
        comment = Comment(post_id,current_user.userid,request.args['message'],int(request.args['color']))
        db.session.add(comment)
        db.session.commit()
        return '',200
    else:
        return 'color does not exist', 400

@comments.route('/<user_id>/vote', methods = ['POST'])
def postCommentVote(post_id, user_id):
    pass
