from flask import Blueprint

from app.comments.models import Comment

comments = Blueprint('comments', __name__, url_prefix='/posts/<post_id>/comments')

@comments.route('/<user_id>', methods = ['GET'])
def getComment(post_id, user_id):
    pass

@comments.route('/<user_id>/voters', methods = ['GET'])
def getCommentVoters(post_id, user_id):
    pass

@comments.route('/', methods = ['PUT'])
def editComment(post_id):
    #see the user logged in and give them access if the post is their's
    pass

@comments.route('/<user_id>', methods = ['DELETE'])
def deleteComment(post_id, user_id):
    pass

@comments.route('/<user_id>', methods = ['POST'])
def postComment(post_id, user_id):
    pass

@comments.route('/<user_id>/vote', methods = ['POST'])
def postCommentVote(post_id, user_id):
    pass
