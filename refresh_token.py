import requests
import base64
import json

from variables import client_id, client_secret

def save_tokens(token_info):
    with open('tokens.json', 'w') as token_file:
        json.dump(token_info, token_file)

def load_tokens():
    with open('tokens.json', 'r') as token_file:
        return json.load(token_file)


def refresh_access_token(refresh_token):
    token_url = 'https://accounts.spotify.com/api/token'
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()
    token_headers = {
        'Authorization': f'Basic {b64_auth_str}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    token_data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    token_response = requests.post(token_url, headers=token_headers, data=token_data)
    token_info = token_response.json()
    
    # Preserve the refresh token if it's not returned in the response
    if 'refresh_token' not in token_info:
        token_info['refresh_token'] = refresh_token
    
    save_tokens(token_info)
    return token_info['access_token']

