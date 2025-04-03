import json
import time

from refresh_token import refresh_access_token
from get_current_track import get_current_track

# Load tokens from file
with open('tokens.json', 'r') as token_file:
    token_info = json.load(token_file)

for i in range(10):
    access_token = token_info['access_token']
    refresh_token = token_info['refresh_token']

    track = get_current_track(access_token, refresh_token)
    print(track['progress_ms'])

    time.sleep(5)