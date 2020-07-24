"""
Dev Notes: This file is used within the command line in order to create the schema for our database.
The schema was defined in our file models.py

"""

# Imports --------------------------------------------------------------------------------

from application import db
from application.models import Posts

db.create_all()