#
# Base Models
#
# This is the Base class.The other models inherit from this model.
#
# base/models.py
#

from json import dumps

from app import db, graph_db
from time import time

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

class BaseNode():
    attr = ('date_created',)

    def __init__(self,**kwargs):
        # optional argument:
        if 'date_created' not in kwargs: kwargs['date_created'] = time()

        # set a keyworded arg as a class attribute if present in self.attr
        for i in self.attr:
            if i in kwargs: setattr(self,i,kwargs[i])

    @classmethod
    def fromNode(cls, node):
        # passes node properties as keyworded args to __init__, creating a new instance
        u = cls(**node._properties)
        u.node = node
        return u

    def save(self):
        # if a node already exists for the instance in the DB
        if hasattr(self,'node'):
            self.node.setProperties(dict([(i,self.node[i]) for i in self.attr]))
        else:
            self.node, = graph_db.create(dict([(i,getattr(self,i)) for i in self.attr]))
