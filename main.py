import requests

# Replace this with your access token
from variables import access_token

# Request headers
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Make the request to get the currently playing track
response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)

# Check if the request was successful
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
