#This is a test file for the model posts, for each method created in posts we
#will create automatic tests that run here using nose. 
from flask import Flask, current_app
import os, sys, unittest, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0,parentdir)

from app.posts.models import Post

class TestPosts(unittest.TestCase):

    def SetUp(self):
        app = Flask(__name__)
        with app.app_context():
            current_app.config['Testing'] = True
            return current_app


    def test_app(self):
        assert(True)


if __name__ == "__main__":
    unittest.main()
