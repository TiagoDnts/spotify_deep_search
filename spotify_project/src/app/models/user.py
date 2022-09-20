import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

class User:

    def __init__(self):
        self._sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.user = self.sp.current_user()

    def followed_artists(self):
        followed_artists = self.sp.current_user_followed_artists()
        return followed_artists

    def playing_track(self):
        playing_track = self.sp.current_user_playing_track()
        return playing_track

    def playlists(self):  # ToDo: pagination limit warnings
        playlists = self.sp.current_user_playlists()
        return playlists
#
# if __name__ == '__main__':
#     u =User()
#     print(u.playlists())