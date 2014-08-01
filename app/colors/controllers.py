from flask import Blueprint, request, redirect, url_for

from app import db, graph_db, app
from app.colors.models import Color
from random import randint
from hashlib import sha256
from py2neo.neo4j import CypherQuery

colors = Blueprint('colors', __name__, url_prefix='/colors')

@colors.route('/get', methods = ['GET'])
def get():
    args = ['colorid']
    result = ''
    try:
        for i in args:
            assert i in request.args, 'missing ' + i

        l = list(graph_db.find("Color","colorid",int(request.args['colorid'])))

        if len(l) == 1: result = str(Color.fromNode(l[0]))
        else: result = "color not found"

    except AssertionError, e:
        result = str(e)
    return result

@colors.route('/create', methods = ['GET'])
def create():
    args = ['hexstr', 'description', 'fromdate', 'todate']
    result = ''
    try:
        for i in args:
            assert i in request.args, 'missing ' + i

        cnt = CypherQuery(graph_db, "MATCH (n:Color) return count(n)").execute().data[0].values[0]

        c = Color(hexstr=request.args['hexstr'],
                  description=request.args['description'],
                  fromdate=request.args['fromdate'],
                  todate=request.args['todate'])
        c.colorid = cnt

        c.save()

        result = "color %s created" % c.colorid

    except AssertionError, e:
        result = str(e)
    return result

def isColorValid(id):
    l = list(graph_db.find("Color","colorid",id))
    if len(l) == 1: return True
    else: return False
