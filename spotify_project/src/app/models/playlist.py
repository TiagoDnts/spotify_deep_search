import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

class Playlist:

    def __init__(self):
        self._sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    def get_tracks_from_playlist(self, playlistId):
        tracks = self.sp.playlist_tracks(playlistId)

        return tracks

    def get_discography_from_all_artists(self, playlistId):
        playlist_tracks = self.get_tracks_from_playlist(playlistId=playlistId)
        tracks = [discog]
        return tracks