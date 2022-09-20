import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

class Album:
    def __init__(self):
        self._sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    def get_album(self, albumIds):
        if isinstance(albumIds,list):  # multiple
            album = self.sp.album(albumIds)
        else:
            album = self.sp.albums(albumIds)

        return album

    def get_track_from_album(self, albumId):
        tracks = self.sp.album_tracks(albumId)

        return tracks
