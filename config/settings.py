from config.getSecret import getSecret

class BaseConfig():
    API_PREFIX = getSecret('API_PREFIX')
    TESTING = False
    DEBUG = False
    spotify = {
        'API_URL': getSecret('SPOTIFY_API_URL'),
        'CLIENT_ID': getSecret('SPOTIFY_CLIENT_ID'),
        'CLIENT_SECRET': getSecret('SPOTIFY_CLIENT_SECRET'),
    }
    FIRESTORE_KEY = getSecret('FIRESTORE_KEY')
    PROJECT_ID = getSecret('PROJECT_ID')


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    URL = 'http://127.0.0.1:8080'
    USERS_COLLECTION_ID = getSecret('USERS_COLLECTION_ID_DEV')


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    URL = 'https://wicker-park-dot-iconic-hue-273619.appspot.com'
    USERS_COLLECTION_ID = getSecret('USERS_COLLECTION_ID_PRODUCTION')


class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
