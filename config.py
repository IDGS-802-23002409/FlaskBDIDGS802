

from re import DEBUG


class Config(object):
    SECRET_KEY="Clave nueva"
    SESSION_COOKIE_SECURE=False
    
    
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:@127.0.0.1/igs802"
    SQLALCHEMY_TRACK_MODIFICATIONS=False