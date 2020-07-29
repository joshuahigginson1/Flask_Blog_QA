from application import create_app as app
from flask_testing import LiveServerTestCase
import unittest

import time
import urllib.request.urlopen
from selenium import webdriver, webdriver.chrome.options.Options

import Webdriver
import Options


def create_app(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DB_URI'))
    app.config['SECRET_KEY'] = getenv('TEST_SECRET_KEY')
    return app


def setUp(self):
    # ensure there is no data in the test database when the test starts
    db.session.commit()
    db.drop_all()
    db.create_all()

    # create test admin user
    hashed_pw = bcrypt.generate_password_hash('admin2016')
    admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password=hashed_pw)

    # create test non-admin user
    hashed_pw_2 = bcrypt.generate_password_hash('test2016')
    employee = Users(first_name="test", last_name="user", email="test@user.com", password=hashed_pw_2)

    # save users to database
    db.session.add(admin)
    db.session.add(employee)
    db.session.commit()
    return app


def tearDown(self):
    db.session.remove()
    db.drop_all()
    return app
