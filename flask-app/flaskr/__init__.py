# The __init__.py serves double duty. It will contain the application factory.
# It also tells Python that the 'flaskr' directory should be treated as a package.


# Imports --------------------------------------------------------------------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Globally Accessible Libraries ---------------------------------------------------------

# Setting plugins as global variables outside of create_app() makes them  accessible to other parts of our application. 
# However, we can't actually use them until after they have been initialised by our app.

db = SQLAlchemy()


# Functions -----------------------------------------------------------------------------

def create_app():  # Initialises the core application.

    # Create our Flask app object.
    app = Flask(__name__, instance_relative_config=False, template_folder='templates')

    # State that it should be configured using a class called Config, in a file named config.py.
    app.config.from_object('config.Config')

    # Initialise our Globally Accessible Libraries
    db.init_app(app)

    # Any part of our app which is not imported, initialized, or registered within the with app.app_context(): block...
    # ... effectively does not exist. This block is the lifeblood of our Flask app.

    # App_context() essentially states: 'here are all of the individual pieces of code which my program will run.'

    with app.app_context():
        # The first thing we do inside the context is import the base parts of our app.
        # These are any Python files or logic which aren't Blueprints.

        # from .bp_folder1 import blueprint_filename1
        # from .bp_folder2 import blueprint_filename2
        # from .bp_folder3 import blueprint_filename3

        from .blog import blog
        from .homepage import homepage
        from . import routes

        # Next, we register Blueprints.
        # Blueprints are "registered" by calling register_blueprint() on our app object.

        # app.register_blueprint(blueprint_module_name.blueprint_name1)
        # app.register_blueprint(blueprint_module_name.blueprint_name2)
        # app.register_blueprint(blueprint_module_name.blueprint_name3)
        app.register_blueprint(blog.blog_bp)
        app.register_blueprint(homepage.homepage_bp)

        # If we have a database, we need to run the command .create_all() to our database schema.

        db.create_all()

    return app

# So our function returns app, but what are we returning to, exactly?
# That's where the mysterious wsgi.py file comes in.
