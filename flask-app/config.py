class Config(object):
    # General Config

    DEBUG = False
    TESTING = False
    FLASK_APP = 'wsgi.py'
    SECRET_KEY = 'alligator 3'

    # Flask Config from Environment Variables

    # FLASK_ENV = environ.get('FLASK_ENV')
    # SECRET_KEY = environ.get('SECRET_KEY')

    # SQL-Alchemy Database Config

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:W33Y15nITj*I&k97@localhost:3306/blog_database"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Static Assets Config

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
