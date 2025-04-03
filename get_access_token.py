# import requests
# import base64

# from variables import client_id, client_secret, access_token

# def get_access_token():
#     # Encode the client ID and client secret
#     auth_str = f"{client_id}:{client_secret}"
#     b64_auth_str = base64.b64encode(auth_str.encode()).decode()

#     # Request headers
#     headers = {
#         'Authorization': f'Basic {b64_auth_str}',
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }

#     # Request body
#     data = {
#         'grant_type': 'client_credentials'
#     }

#     # Make the request to get the token
#     response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

#     # Check if the request was successful
#     if response.status_code == 200:
#         token_info = response.json()
#         access_token = token_info['access_token']
#         print(f"Access Token: {access_token}")
#         return access_token
#     else:
#         print(f"Failed to get token: {response.status_code}")
#         print(response.json())
#         return None


import requests
import base64
import webbrowser
from urllib.parse import urlencode, urlparse, parse_qs

# Replace these with your Spotify Client ID and Client Secret
from variables import client_id, client_secret, redirect_uri

# Step 1: Get authorization code
auth_url = 'https://accounts.spotify.com/authorize'
auth_params = {
    'client_id': client_id,
    'response_type': 'code',
    'redirect_uri': redirect_uri,
    'scope': 'user-read-playback-state user-read-currently-playing'
}
webbrowser.open(f"{auth_url}?{urlencode(auth_params)}")

# Step 2: Get the authorization code from the redirect URL
redirect_response = input("Paste the full redirect URL here: ")
parsed_url = urlparse(redirect_response)
auth_code = parse_qs(parsed_url.query)['code'][0]

# Step 3: Exchange authorization code for access token
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
access_token = token_info['access_token']

# Step 4: Use the access token to get the currently playing track
headers = {
    'Authorization': f'Bearer {access_token}'
}
response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)

if response.status_code == 200:
    track_info = response.json()
    if track_info:
        track_name = track_info['item']['name']
        artists = ', '.join([artist['name'] for artist in track_info['item']['artists']])
        print(f"Currently playing track: {track_name} by {artists}")
    else:
        print("No track is currently playing.")
else:
    print(f"Failed to get currently playing track: {response.status_code}")
    print(response.json())
