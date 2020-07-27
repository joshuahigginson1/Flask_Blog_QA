class Config(object):
    # General Config

    DEBUG = False
    TESTING = False

    # SQL-Alchemy Database Config

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:W33Y15nITj*I&k97@localhost:3306/blog_database"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
