# The __init__.py serves double duty. It will contain the application factory.
# It also tells Python that the 'flaskr' directory should be treated as a package.


# Imports --------------------------------------------------------------------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import getenv

# Globally Accessible Libraries ---------------------------------------------------------

# Setting plugins as global variables outside of create_app() makes them  accessible to other parts of our application. 
# However, we can't actually use them until after they have been initialised by our app.

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


# Functions -----------------------------------------------------------------------------

def create_app():  # Initialises the core application.

    # Create our Flask app object.
    app = Flask(__name__, instance_relative_config=False)

    # State that it should be configured using a class called Config, in a file named config.py.

    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')

    # Initialise our Globally Accessible Libraries
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Any part of our app which is not imported, initialised, or registered within the with app.app_context(): block...
    # ... effectively does not exist. This block is the lifeblood of our Flask app.

    # App_context() essentially states: 'here are all of the individual pieces of code which my program will run.'

    with app.app_context():
        # The first thing we do inside the context is import the base parts of our app.
        # These are any Python files or logic which aren't Blueprints.

        from application import forms, models, routes
        # from .bp_folder2 import blueprint_name2
        # from .bp_folder3 import blueprint_name3

        # Next, we register Blueprints.
        # Blueprints are "registered" by calling register_blueprint() on our app object.

        # app.register_blueprint(blueprint_module_name.blueprint_name1)
        # app.register_blueprint(blueprint_module_name.blueprint_name2)
        # app.register_blueprint(blueprint_module_name.blueprint_name3)

        # If we have a database, we need to run the command .create_all() to our database schema.

        db.drop_all()
        db.create_all()

    return app

# So our function returns app, but what are we returning to, exactly? 
# That's where the mysterious wsgi.py file comes in.
