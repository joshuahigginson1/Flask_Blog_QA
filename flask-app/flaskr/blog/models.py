"""

Dev Notes:This file is used define the schema for our blog post database.

"""

# Imports --------------------------------------------------------------------------------

from flaskr import db  # import our database instance, stored as 'variable' in our __init__.py file.


# Classes --------------------------------------------------------------------------------

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return ''.join(
            ['User: ', self.first_name, ' ', self.last_name, '\r\n',
             'Title: ', self.title, '\r\n', self.content]
        )