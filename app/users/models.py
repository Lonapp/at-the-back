#
# User Models
#
# This is the user class. Eventually it will interface
# with our authenication system.
#
# users/models.py
#

from app import graph_db
from app.base.models import BaseNode
from datetime import datetime

class User(BaseNode):
    attr = BaseNode.attr + ('userid', 'username','realname','email','password','phone')

    def __init__(self, **kwargs):
        # optional argument
        if 'userid' not in kwargs: kwargs['userid'] = -1
        BaseNode.__init__(self, **kwargs)

    def save(self):
        BaseNode.save(self)
        self.node.add_labels("User")

    def __repr__(self):
        return ("%d %s %s (%s)") % (self.userid, self.username, self.email, datetime.fromtimestamp(self.date_created))

    def __str__(self):
        return ("%d %s %s (%s)") % (self.userid, self.username, self.email, datetime.fromtimestamp(self.date_created))
