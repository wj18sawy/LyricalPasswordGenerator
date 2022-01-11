import spotipy.util as util
import requests
from secrets import CLIENT_ID, CLIENT_SECRET

username = input("Please input your Spotify username: ")
client_id = CLIENT_ID
client_secret = CLIENT_SECRET
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-library-read'

token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)

headers = {
    'Authorization': 'Bearer {token}'.format(token=token),
    'Content-Type': 'application/json'
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# pull all artists albums
r = requests.get(BASE_URL + 'me/tracks', headers=headers)

print(r.json())