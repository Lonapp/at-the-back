from flask import Blueprint

from app.comments.models import Comment

comments = Blueprint('comments', __name__, url_prefix='/comments')
