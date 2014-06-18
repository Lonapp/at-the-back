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

    message = db.Column(db.String(MESSEGE_LEN))

    #not sure about BigInteger. I think it is similar to
    #long int, but may want to double check. Also, we may
    #need to add a foreign key for this.
    voteCount = db.Column(db.BigInteger)

    def __init__(self, message):
        self.message = message
        self.voteCount = 0

    def __repr__(self):
        return self.json

    @property
    def json(self):
        return { "id" : str(self.object_id),
                "message": str(self.message),
                "voteCount": str(self.voteCount)
               }

    def getMessage():
        return self.message

    def setMessage(newMessage):
        #void
        self.message = newMessage

    def getVoteCount():
        #return long int
        return self.voteCount

    def setVoteCount(newVoteCount):
        #void
        self.voteCount = newVoteCount

    def addCount(num = 1):
        #return bool
        self.voteCount = self.voteCount + num
        return True

    def getColor():
        #return color
        pass

    def getUser():
        #return user
        pass
