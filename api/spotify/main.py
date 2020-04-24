from flask import Blueprint,request
import config
import requests
import json

spotify_routes = Blueprint('spotify_routes', __name__)

@spotify_routes.route('/me', methods=['GET'])
def getMe():
    userId = request.args.get('id')
    if userId is not None:
        userRes = requests.get(f'{config.URL}{config.API_PREFIX}/users/getUser', params={'id': userId})
        user = userRes.json()
        access_token = user['spotify_access_token']
        refresh_token = user['spotify_refresh_token']
    else:
        access_token = request.args.get('access_token')
        refresh_token = request.args.get('refresh_token')

    headers = {'Authorization': f'Bearer {access_token}'}
    res = requests.get('https://api.spotify.com/v1/me', headers=headers)
    if res.status_code == 401:
        access_token = refreshToken(refresh_token, userId)
        params = {'access_token': access_token}
        res = requests.get('https://api.spotify.com/v1/me', params=params)
    return res.json()

# TODO: add functionality to automatically refresh if necessary (maybe put in model?)

@spotify_routes.route('/me/playback', methods=['GET'])
def getPlaybackInfo():
    userId = request.args.get('id')
    if userId is not None:
        userRes = requests.get(f'{config.URL}{config.API_PREFIX}/users/getUser', params={'id': userId})
        user = userRes.json()
        access_token = user['spotify_access_token']
        refresh_token = user['spotify_refresh_token']
    else:
        access_token = request.args.get('access_token')
        refresh_token = request.args.get('refresh_token')

    headers = {'Authorization': f'Bearer {access_token}'}
    res = requests.get('https://api.spotify.com/v1/me/player', headers=headers)
    if res.status_code == 401:
        access_token = refreshToken(refresh_token, userId)
        params = {'access_token': access_token}
        res = requests.get('https://api.spotify.com/v1/me/player', params=params)
    return res.json()

def refreshToken(refreshToken, userId = None):
    try:
        tokensRes = requests.get(f'{config.URL}/auth/refreshToken', params={'refresh_token': refreshToken})
        tokens = json.loads(tokensRes.text)
        if userId is not None:
            updateArgs = {'id': userId}
            updatePayload = { 'spotify_access_token': tokens.get('access_token') }
            requests.put(f'{config.URL}{config.API_PREFIX}/users/updateUser', params=updateArgs, data=updatePayload)
        return tokens.get('access_token')
    except Exception as e:
        return f"An Error Occured: {e}"
