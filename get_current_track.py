import requests

from refresh_token import refresh_access_token

def get_current_track(access_token, refresh_token):
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
            return track_info
        else:
            print("No track is currently playing.")
    elif response.status_code == 401:  # Token expired
        print("Access token expired, refreshing...")
        access_token = refresh_access_token(refresh_token)
        get_current_track(access_token, refresh_token)
    else:
        print(f"Failed to get currently playing track: {response.status_code}")
        print(response.json())
