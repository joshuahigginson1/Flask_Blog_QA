"""
Creates the Schema used to store our app's user information.
"""

# Imports --------------------------------------------------------------------------------

from flaskr import db  # import our database instance, stored as 'variable' in our __init__.py file.


# Classes --------------------------------------------------------------------------------

class Users(db.Model):  # Creates the schema for a 'Users table' within our database.
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):  # Define the self representation of our data.
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])
