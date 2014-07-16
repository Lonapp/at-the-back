#
# Post Models
#
# This is the post class. It's the most fundamental unit of media in the app.
#
# posts/models.py
#

from json import dumps

from app import db
from app.base.models import BaseModel

MESSEGE_LEN = 500
class Post(BaseModel):
    __tablename__ = "posts"

    object_id = db.Column('id', db.Integer, primary_key=True)
    message = db.Column(db.String(MESSEGE_LEN))

    # OriginalPost is null if Post is original and has an ID if it was lonned from another post
    # Do post have an original post?
    originalPost = db.Column(db.Integer, db.ForeignKey('posts.id'))

    #The number of Posts that were lonned from the current one (easy to retreive instead of counting everytime we view)
    numOfShares = db.Column(db.Integer)

    def __init__(self, message, originalPost = None):
        self.message = message
        self.originalPost = originalPost
        self.numOfShares = 0

    def __repr__(self):
        return ""

    @property
    def json(self):
        return { 'id':                  str(self.object_id)
               , 'date_created':        str(self.date_created)
               , 'date_modified':       str(self.date_modified)
               , 'message':             str(self.message)
               , 'Lonned_Posts_Id':      str(self.LonnedPostsID)
               , 'num_of_posts_lonned': str(self.numOfPostsLonned)
               }

    def get_message():
        return self.message

    def set_message(new_message):
        self.message = new_message
        self.save()

    def getUser():
        #void
        pass

    def getColor():
        #void
        pass

    def setColor(color):
        #return type bool
        pass

    def addComment(comm):
        #return type bool
        pass

    def getComment(limit = 2):
        #return type Comment
        pass

    def getAllComments():
        #return type Comment
        pass

    def getLonnedPosts():
        #return type Post
        LonnedPosts = []
        if self.numOfShares != 0:
            #try self.query
            LonnedPosts = db.session.query.filter(LonnedPostsID != null).all()
            return LonnedPosts
        else:
            return LonnedPosts

    def sharePost():
        self.numOfShares += 1
        return self

    def hasImage():
        #return type bool
        pass

    def getImage():
        #return type Picture
        pass

    def setImage(caption, pic):
        #return type bool
        pass

    def getNumOfShares():
        #return type int
        return self.NumOfShares

