# coding:utf-8

class Config(object):
    """config file"""
    DEBUG=True

    SECRET_KEY = "XHLKJI##SLDKF123"

    #database
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@192.168.1.78:3306/ihome_web01"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #redis
    REDIS_HOST = "192.168.1.78"
    REDIS_PORT = 6379

    #flask session configuration
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
    SESSION_USE_SIGNER = True #对cookie中的id进行隐藏
    PERMANENT_SESSION_LIFETIME = 86400 #SESSION数据的有效期

class DevelopmentConfig(Config):
    """开发"""
    DEBUG = True
    pass

class PrductConfig(Config):
    """生产"""
    pass

config_map = {
    "develop": DevelopmentConfig,
    "product": PrductConfig

}