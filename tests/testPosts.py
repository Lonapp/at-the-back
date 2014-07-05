#This is a test file for the model posts, for each method created in posts we
#will create automatic tests that run here using nose. 
from flask import Flask, current_app
import os, sys, unittest, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0,parentdir)

from app.posts.models import Post
from app import db

class TestPosts(unittest.TestCase):
    """ Tests the module 'Posts' """

    def SetUp(self):
        """Does a setup for the testing in the file."""

        self.app = Flask(__name__)
        db.init_app(current_app)
        with self.app.app_context():
            current_app.config['Testing'] = True
            db.create_all()

    def tearDown(self):
        """Ensures that database is emptied for next time"""

        self.app = Flask(__name__)
        db.init_app(current_app)
        with self.app.app_context():
            db.drop_all()


    def test_app(self):
        with self.app.app_context():
            assert(True)

    def test_full(self):
        assert(False)



if __name__ == "__main__":
    unittest.main()
