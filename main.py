from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Declaring needed Variables
Spotifyusername = "Suhaas"
year = input("What year would you like to travel to in YY-MM-DD? ")
URL = f"https://www.billboard.com/charts/hot-100/{year}"
Redirect_URL = "https://example.com"
scope = "playlist-modify-private playlist-modify-public"
CLIENT_ID="ee6a0bde8c8f4080ad031a7586dfba50"
CLIENT_SECRET="74ddd77a3fa2432cb78ca24a5c187ce7"

# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="https://example.com",
#         client_id=CLIENT_ID,
#         client_secret=CLIENT_SECRET,
#         show_dialog=True,
#         cache_path="token.txt",
#         username="Suhaas",
#     )
# )

# SCRAPING BILLBOARD TOP 100 CHARTS WITH BEAUTIFUL SOUP
headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
response = requests.get(URL, headers=headers)
billboard_website = response.text
soup = BeautifulSoup(billboard_website, "html.parser")
top100 = soup.find_all("h3", class_="u-max-width-330")

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
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# song_uris = []
# for song in top100:
#     song_name = song.get_text().strip()
#     result = sp.search(q=song_name, type="track")
#
#     if result["tracks"]["items"]:
#         song_uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(song_uri)
#     else:
#         print(f"{song_name} not found on Spotify")
#
# # Creating a new playlist on Spotify
# playlist_name = f"Billboard Hot 100 - {year}"
# description = f"Top 100 songs on Billboard charts on {year}."
#
# playlist = sp.user_playlist_create(user=user_id,
#                                    name=playlist_name,
#                                    description=description,
#                                    public=False)
# # Adding songs to playlist
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)