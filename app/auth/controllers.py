from flask import Blueprint, request

from flask.ext.login import login_user, logout_user, login_required
from app.users.models import User
from app.users.controllers import getUserByUsername, hash_pw
from app import login_manager

auth = Blueprint('auth', __name__, url_prefix='/auth')

#todo remove GET
@auth.route('/login', methods = ['GET','POST'])
def login():
    args = ['username','password']
    failmsg = "username and/or password invalid"
    try:
        for i in args:
            assert i in request.args, 'missing ' + i
        u = getUserByUsername(request.args['username'])

        assert u != None, failmsg
        assert hash_pw(request.args['password']) == u.password, failmsg

        login_user(u)

        result = '',200

    except AssertionError, e:
        result = str(e),401
    return result

@auth.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return '',200

@login_manager.unauthorized_handler
def unauthorized():
    return '',401
