import requests
import base64
import json
from urllib.parse import urlparse, parse_qs, urlencode

# Replace these with your Spotify Client ID, Client Secret, and Redirect URI
from variables import client_id, client_secret, redirect_uri

auth_url = 'https://accounts.spotify.com/authorize'
auth_params = {
    'client_id': client_id,
    'response_type': 'code',
    'redirect_uri': redirect_uri,
    'scope': 'user-read-playback-state user-read-currently-playing'
}
print(f"Open this URL in your browser and authorize the app: {auth_url}?{urlencode(auth_params)}")

# Get the authorization code from the redirect URL
redirect_response = input("Paste the full redirect URL here: ")
parsed_url = urlparse(redirect_response)
auth_code = parse_qs(parsed_url.query)['code'][0]

# Exchange authorization code for access and refresh tokens
token_url = 'https://accounts.spotify.com/api/token'
auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()
token_headers = {
    'Authorization': f'Basic {b64_auth_str}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
token_data = {
    'grant_type': 'authorization_code',
    'code': auth_code,
    'redirect_uri': redirect_uri
}
token_response = requests.post(token_url, headers=token_headers, data=token_data)
token_info = token_response.json()

# Save the tokens to a file
with open('tokens.json', 'w') as token_file:
    json.dump(token_info, token_file)

access_token = token_info['access_token']
refresh_token = token_info['refresh_token']

