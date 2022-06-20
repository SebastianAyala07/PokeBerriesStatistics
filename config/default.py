import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    TESTING = False
    DEBUG = False
    ERROR_404_HELP = False


class Production(Config):
    PROPAGATE_EXCEPTIONS = False

class Development(Config):
    PROPAGATE_EXCEPTIONS = True

class Testing(Config):
    TESTING = True
