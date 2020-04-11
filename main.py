import config
from flask import Flask,redirect,request
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!'

@app.route('/getTokens', methods=['POST'])
def success():
    authCode = request.form.get('code', '')
    payload = {
        'grant_type': 'authorization_code',
        'code': authCode,
        'redirect_uri': 'spotify-ios-quick-start://spotify-login-callback',
        'client_id': config.spotify['CLIENT_ID'],
        'client_secret': config.spotify['CLIENT_SECRET']
    }
    res = requests.post('https://accounts.spotify.com/api/token', data=payload)
    return res.json()

# @app.route('/auth')
# def auth():
#     payload = {
#         'client_id': config.spotify['CLIENT_ID'],
#         'response_type': 'code',
#         'redirect_uri': 'http://localhost:5000/success',
#         'scopes': 'user-read-private user-read-email'
#     }
#     res = requests.get('https://accounts.spotify.com/authorize', params=payload)
#     return redirect(res.url, code=302)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=5000, debug=True)
