# imports ------------------------------

from os import environ, path
from dotenv import load_dotenv

# .env location ------------------------

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


# declare classes ----------------------

class Config(object):
    # General Config

    DEBUG = False
    TESTING = False
    FLASK_APP = 'wsgi.py'

    # Flask Config from Environment Variables

    SECRET_KEY = os.environ.get('SECRET_KEY')
    # FLASK_ENV = os.environ.get('FLASK_ENV')

    # SQL-Alchemy Database Config

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Static Assets Config

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProductionConfig(Config):


# DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True