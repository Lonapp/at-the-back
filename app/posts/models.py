#
# Post Models
#
# This is the post class. It's the most fundamental unit of media in the app.
#
# posts/models.py
#

from json import dumps

from app import db

MESSEGE_LEN = 500

class Base(db.Model):
    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @property
    def json(self):
        return { 'id':              str(self.id)
               , 'message':         str(self.message)
               , 'date_created':    str(self.date_created)
               , 'date_modified':   str(self.date_modified)
               }

class Post(Base):
    __tablename__ = "posts"

    message = db.Column(db.String(MESSEGE_LEN))

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return self.json

    def get_message():
        return self.message

    def set_message(new_message):
        self.message = new_message
	
	def getTimePosted():
		#return time and date
		pass
	
	def setTimePosted(timePosted):
		#void
		pass
	
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
		pass
	
	def hasImage():
		#return type bool
		pass
	
	def getImage():
		#return type Picture
		pass
	
	def setImage(caption, pic):
		#return type bool
		pass
	
	def getNumOfLonnedPosts():
		#return type int
		return 2
	
	def setNumOfLonnedPosts(NumOfLonnedPosts):
		#void
		NumOfLonnedPosts = 2
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	








