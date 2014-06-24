from flask import Blueprint, request, redirect, url_for

from app import db, graph_db, app
from app.users.models import User
from random import randint
from hashlib import sha256

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/get', methods = ['GET'])
def get():
    args = ['username']
    result = ''
    try:
        for i in args:
            assert i in request.args, 'missing ' + i

        l = list(graph_db.find("User","username",request.args['username']))

        if len(l) == 1: result = str(User.fromNode(l[0]))
        else: result = "user not found"

    except AssertionError, e:
        result = str(e)
    return result

@users.route('/create', methods = ['GET'])
def create():
    args = ['username', 'realname', 'email', 'pw', 'phone']
    result = ''
    try:
        for i in args:
            assert i in request.args, 'missing ' + i

        assert len(list(graph_db.find("User","username",request.args['username']))) == 0, "user already exists"
        assert len(list(graph_db.find("User","email",request.args['email']))) == 0, "email already exists"

        u = User(username=request.args['username'],
                 realname=request.args['realname'],
                 email=request.args['email'],
                 password=sha256(request.args['pw']).hexdigest(),
                 phone=request.args['phone'])

        while True:
            u.userid = randint(app.config['UID_START'],app.config['UID_END'])
            if len(list(graph_db.find("User","id",u.userid))) == 0: break

        u.save()

        result = "user %s created" % u.userid

    except AssertionError, e:
        result = str(e)
    return result
