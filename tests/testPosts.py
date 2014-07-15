#This is a test file for the model posts, for each method created in posts we
#will create automatic tests that run here using nose. 
from flask import Flask, current_app
import os, sys, inspect
import unittest, urllib2, urllib, json

from flask.ext.testing import LiveServerTestCase

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0,parentdir)

from app import app

class TestPosts(LiveServerTestCase):
    """ Tests the module 'Posts' """

    def create_app(self):

        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 5000
        #We will need to reset the db everytime we test
        return app

    def test_url_works(self):
        url = self.get_server_url() + '/posts/'
        response = urllib2.urlopen(url)
        self.assertEqual(response.code,200)

    def test_add_get_posts(self):
        url = self.get_server_url() + '/posts/'
        values = {'message': 'First Post Eva'}

        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        responseJson = json.load(response)

        self.assertEqual(responseJson['message'],'First Post Eva')
        self.assertEqual(response.code,200)

        TheID = responseJson['id']

        url = self.get_server_url() + '/posts/' + str(TheID)
        response = urllib2.urlopen(req)
        responseJson = json.load(response)

        self.assertEqual(responseJson['message'],'First Post Eva')
        self.assertEqual(response.code,200)




if __name__ == "__main__":
    unittest.main()
