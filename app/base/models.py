#
# Base Models
#
# This is the Base class.The other models inherit from this model.
#
# base/models.py
#

from json import dumps

from app import db

class BaseModel(db.Model):
    __abstract__  = True

    object_id = db.Column('id', db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self,date_created, date_modified):
        self.date_created = date_created
        self.date_modified = date_modified

    def save(self):
        db.session.add(self)
        db.session.commit()

    def getDateCreated(self):
        return self.date_created

    def getDateModified(self):
        return self.date_modified

    @property
    def json(self):
        return { 'id':              str(self.object_id)
               , 'date_created':    str(self.date_created)
               , 'date_modified':   str(self.date_modified)
               }


