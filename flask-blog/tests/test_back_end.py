import unittest
import time
from flask import url_for
from application import create_app as app
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import db, bcrypt
from application.models import Users

test_admin_first_name = "admin"
test_admin_last_name = "admin"
test_admin_email = "admin@email.com"
test_admin_password = "admin2020"


class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                          SECRET_KEY=getenv('TEST_SECRET_KEY'))
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="<PATH TO chromedriver executable>",
                                       chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print(
            "--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)


class TestViews(TestBase):

    def test_homepage_view(self):
        # Test that homepage is accessible without logging in.
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


class TestPosts(TestBase):

    def test_add_new_post(self):
        # Test that when I add a new post, I am redirected to the homepage with the new post visible
        with self.client:
            response = self.client.post(
                '/post',
                data=dict(
                    title="Test Title",
                    content="Test Content"
                ),
                follow_redirects=True
            )
            self.assertIn(b'Test Title', response.data)
