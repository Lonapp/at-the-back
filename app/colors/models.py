#
# Color Models
#
# colors/models.py
#

from app import graph_db
from app.base.models import BaseNode
from time import time
from datetime import datetime

class Color(BaseNode):
    attr = BaseNode.attr + ('colorid', 'hexstr','description','fromdate','todate')

    def __init__(self, **kwargs):
        # optional argument:
        if 'colorid' not in kwargs: kwargs['colorid'] = -1
        BaseNode.__init__(self,**kwargs)

    def save(self):
        BaseNode.save(self)
        self.node.add_labels("Color")

    def __repr__(self):
        return ("%d %s \"%s\" (%s)") % (self.colorid, self.hexstr, self.description, datetime.fromtimestamp(self.date_created))

    def __str__(self):
        return ("%d %s \"%s\" (%s)") % (self.colorid, self.hexstr, self.description, datetime.fromtimestamp(self.date_created))
