"""
Dev Notes:


"""

# Imports --------------------------------------------------------------------------------

# import Flask class from the flask module

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql
import os

# create a new instance of Flask, and store it in variable app.
app = Flask(__name__)

# Flask-SQLAlchemy Config ----------------------------------------------------------------
database_uri = "mysql+pymysql://root:W33Y15nITj*I&k97@localhost:3306/blog_database"

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = SQLAlchemy(app)  # Create an instance of our database, and assign it as a variable called 'database'.

# import the ./application/routes.py file

from application import routes
