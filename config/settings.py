from config.getSecret import getSecret

# SECRET ID's

API_PREFIX = 'API_PREFIX'
SPOTIFY_API_URL = 'SPOTIFY_API_URL'
SPOTIFY_CLIENT_ID = 'SPOTIFY_CLIENT_ID'
SPOTIFY_CLIENT_SECRET = 'SPOTIFY_CLIENT_SECRET'

class BaseConfig():
   API_PREFIX = getSecret(API_PREFIX)
   TESTING = False
   DEBUG = False
   spotify = {
        'API_URL': getSecret(SPOTIFY_API_URL),
        'CLIENT_ID': getSecret(SPOTIFY_CLIENT_ID),
        'CLIENT_SECRET': getSecret(SPOTIFY_CLIENT_SECRET),
   }


class DevConfig(BaseConfig):
   FLASK_ENV = 'development'
   DEBUG = True
   URL = 'http://127.0.0.1:8080'


class ProductionConfig(BaseConfig):
   FLASK_ENV = 'production'
   URL = 'https://iconic-hue-273619.appspot.com'


class TestConfig(BaseConfig):
   FLASK_ENV = 'development'
   TESTING = True
   DEBUG = True
