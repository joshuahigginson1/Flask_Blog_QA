"""
Creates the Schema used to store our app's user information.
"""

# Imports --------------------------------------------------------------------------------

from flaskr import db  # import our database instance, stored as 'variable' in our __init__.py file.
from flaskr import login_manager
from flask_login import UserMixin


@login_manager.user_loader  # Declares the table in which we are loading user data from.
def load_user(id):
    return Users.query.get(int(id))


# Classes --------------------------------------------------------------------------------

class Users(db.Model, UserMixin):  # Creates the schema for a 'Users table' within our database...
    # The child class inherits from both db.Model & UserMixin parent classes.

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])
