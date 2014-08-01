#
#
#Comment Models
#
#

from json import dumps

from app import db
from app.base.models import BaseModel

MESSEGE_LEN = 250
class Comment(BaseModel):
    __tablename__ = "comments"
    
    #not sure about BigInteger. I think it is similar to
    #long int, but may want to double check. Also, we may
    #need to add a foreign key for this.
    post = db.Column(db.BigInteger, primary_key=True)
    user = db.Column(db.BigInteger, primary_key=True)
    color = db.Column(db.BigInteger)
    message = db.Column(db.String(MESSEGE_LEN))
    voteCount = db.Column(db.BigInteger)

    def __init__(self, post, user, color, message):
        self.post = post
        self.user = user
        self.color = color
        self.message = message
        self.voteCount = 0

    def __repr__(self):
        return self.json

    @property
    def json(self):
        return {"post": str(self.post),
                "user": str(self.user),
                "color": str(self.color),
                "message": str(self.message),
                "voteCount": str(self.voteCount)
               }

    def getMessage(self):
        return self.message

    def setMessage(self, newMessage):
        #void
        self.message = newMessage

    def getVoteCount(self):
        #return long int
        return self.voteCount

    def setVoteCount(self, newVoteCount):
        #void
        self.voteCount = newVoteCount

    def addCount(self, num = 1):
        #return bool
        self.voteCount = self.voteCount + num
        return True

    def getColor(self):
        return self.color

    def getUser(self):
        return self.user

    def getPost(self):
        return self.post
