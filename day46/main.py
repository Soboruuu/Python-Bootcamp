import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL ="https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID="YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET="YOUR_SPOTIFY_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI="http://example.com"

# Get Billboard Top 100 songs from specific date #
date = input("Which year do you want to time travel to? Type the date in YYYY-MM-DD format.\n")

response = requests.get(f"{BILLBOARD_URL}{date}")
soup = BeautifulSoup(response.text,"html.parser")

songs = soup.select(selector=".o-chart-results-list__item > #title-of-a-story")

top_100_songs=[song.getText().strip("\n \t") for song in songs]
print(top_100_songs)


# Spotify authentication

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]

for song in top_100_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
