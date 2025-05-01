import requests
import json


# Load tokens from file
with open('tokens.json', 'r') as token_file:
    token_info = json.load(token_file)

access_token = token_info['access_token']
refresh_token = token_info['refresh_token']


def get_track_lyrics(track_id, access_token):
    base_url = 'https://spclient.wg.spotify.com/color-lyrics/v2/track/'
    headers = {
        'Accept': 'application/json',
        'App-Platform': 'WebPlayer',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(f'{base_url}{track_id}', headers=headers)
    response.raise_for_status()
    return response.json()


track_lyrics = get_track_lyrics("1rqqCSm0Qe4I9rUvWncaom", access_token)
print(track_lyrics)







# from variables import musixmatch_api_key

# url = f"https://api.musixmatch.com/ws/1.1/track.search?apikey={musixmatch_api_key}&q_track=Avalanche&q_artist=WALK THE MOON"

# response = requests.get(url)


# if response.status_code == 200:
#     data = response.json()
#     track_id = data['message']['body']['track_list'][0]['track']['track_id']
#     print(track_id)

#     url = f"https://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey={musixmatch_api_key}&track_id={track_id}"
#     response = requests.get(url)
#     data = response.json()
#     print(data)
# else:
#     print(f'Error: {response.status_code}')
