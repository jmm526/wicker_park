import config
from flask import Flask,redirect,request
from flask_cors import CORS
import requests
import logging
import os

from auth.main import auth_api

logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()

def createApp():

    app = Flask(__name__)
    CORS(app)
    logger.info(f'Starting app in {config.APP_ENV} environment')

    @app.route('/')
    def hello_world():
        return 'Hello, World!!'

    app.register_blueprint(auth_api, url_prefix='/auth')

    print("suh dude")

    return app

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app = createApp()
    app.run(host='127.0.0.1', port=8080, debug=True)