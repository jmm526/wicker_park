from flask import Blueprint,request
import requests
import config

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/getTokens', methods=['GET'])
def getTokens():
    authCode = request.args.get('code', '')
    redirectUri = request.args.get('redirect_uri', '')
    payload = {
        'grant_type': 'authorization_code',
        'code': authCode,
        'redirect_uri': redirectUri or f'{config.URL}/auth/getTokens',
        'client_id': config.spotify['CLIENT_ID'],
        'client_secret': config.spotify['CLIENT_SECRET']
    }
    res = requests.post('https://accounts.spotify.com/api/token', data=payload)
    return res.json()

@auth_api.route('refreshToken', methods=['GET'])
def refreshToken():
    refreshToken = request.args.get('refresh_token')
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': refreshToken,
        'client_id': config.spotify["CLIENT_ID"],
        'client_secret': config.spotify["CLIENT_SECRET"]
    }
    res = requests.post('https://accounts.spotify.com/api/token', data=payload)
    return res.json()

