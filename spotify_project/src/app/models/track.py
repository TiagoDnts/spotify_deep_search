
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

class Track:

    def __init__(self):
        self._sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    def get_trackInfo(self, trackIds):
        if isinstance(trackIds,list):  # if multiple values
            trackInfo = self.sp.tracks(trackIds)
        else:  # if single value
            trackInfo = self.sp.track(trackIds)

        return trackInfo


    def get_trackFeatures(self, trackIds):
        trackFeatures = self.sp.audio_features(trackIds)

        return trackFeatures


    def get_trackAnalysis(self, trackId):
        trackAnalysis = self.sp.audio_analysis(trackId)

        return trackAnalysis


# def get_albumInfo(album):
#     albumInfo = [album]
#     return albumInfo
#
# def get_artistInfo(artist):
#     artistInfo = [artist]
#     return artistInfo
#
# def get_playlistInfo(playlist):
#     artistInfo = [playlist]
#     return artistInfo