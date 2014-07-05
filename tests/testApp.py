#This is a test file for the model posts, for each method created in posts we
#will create automatic tests that run here using nose. 
from flask import Flask, current_app
import os, sys, inspect
import unittest, urllib2

from flask.ext.testing import LiveServerTestCase

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0,parentdir)

#from app.posts.models import Post
from app import app
#import app

class TestApp(LiveServerTestCase):
    """ Tests the module 'Posts' """

    def create_app(self):
        #app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 5000
        return app

    def test_app(self):
        url = self.get_server_url() + '/posts'
        response = urllib2.urlopen(url)
        self.assertEqual(response.code,200)


if __name__ == "__main__":
    unittest.main()
