from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Declaring needed Variables
Spotifyusername = "Suhaas"
year = input("What year would you like to travel to in YYYY-MM-DD? ")
URL = f"https://www.billboard.com/charts/hot-100/{year}"
Redirect_URL = "https://example.com"
scope = "playlist-modify-private playlist-modify-public"
CLIENT_ID="ee6a0bde8c8f4080ad031a7586dfba50"
CLIENT_SECRET="74ddd77a3fa2432cb78ca24a5c187ce7"

# SCRAPING BILLBOARD TOP 100 CHARTS WITH BEAUTIFUL SOUP
headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
response = requests.get(URL, headers=headers)
billboard_website = response.text
soup = BeautifulSoup(billboard_website, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.get_text().strip() for song in song_names_spans]
print(song_names)

# Authenticating Spotify client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=Redirect_URL,
        scope=scope,
        show_dialog=True,
        cache_path="token.txt",
        username=Spotifyusername,
    )
)

user_id = sp.current_user()["id"]

song_uris = []
for song in song_names:
    result = sp.search(q=song, type="track")
    print(result)
    if result["tracks"]["items"]:
        song_uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    else:
        print(f"{song} not found on Spotify")

#Creating and adding songs to playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
