import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

class Artist:

    def __init__(self):
        self._sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    def get_album_from_artist(self, artistId):
        albums = self.sp.artist_albums(artistId)

        return albums
