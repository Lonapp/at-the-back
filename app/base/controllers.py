from flask import Blueprint, request, redirect, url_for

from sqlalchemy.ext.serializer import dumps
from sqlalchemy.orm import sessionmaker

from app.base.models import BaseModel

#a decorator that checks if all arguments are supplied
class args():
    def __init__(self,args):
        self.args = args
    def __call__(self,func):
        def inner(**kwargs):
            try:
                for i in self.args:
                    assert i in request.args, 'missing ' + i
                result = func(**kwargs)
            except AssertionError, e:
                result = str(e),400
            return result
        return inner
