from track import Track
from typing import List
import pandas as pd
import requests


class SpotifyClient:
    """
    SpotifyClient performs operations using the Spotify API.
    """
    def __init__(self, authorization_token: str, user_id: str) -> None:
        """
        :param authorization_token: Spotify API token
        :param user_id: Spotify user id
        """
        self._authorization_token = authorization_token
        self._user_id = user_id

    def get_last_played_tracks(self, limit: int = 10) -> List[Track]:
        """
        Get the last n tracks played by a user.

        :param limit: Number of tracks to get. Should be <= 50
        :return: List of last played tracks
        """
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self._place_get_api_request(url)
        tracks_json = response.json()["items"]
        
        tracks = []
        for track_json in tracks_json:
            track = Track(
                track_json["track"]["name"],
                track_json["track"]["artists"][0]["name"],
                track_json["track"]["album"]["album_type"],
                track_json["track"]["album"]["release_date"],
                track_json["track"]["album"]["name"])
            tracks.append(track)
        return tracks
    
    def get_tracks_dataframe(self, limit: int = 10) -> pd.DataFrame:
        """
        Get the last n tracks played by a user as a DataFrame.
        
        :param limit: Number of tracks to get. Should be <= 50
        :return: DataFrame containing track name, artist name, album name, album type and release date
        """
        # Get the list of tracks
        tracks = self.get_last_played_tracks(limit)
        # Create a list of dictionaries containing the track data
        track_data = [{
            "artist": track.artist, 
            "song_title": track.name, 
            "album_name": track.album_name,
            "album_type": track.album_type,
            "release_date": track.release_date
        } for track in tracks]
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(track_data)
        return df

    
    def _place_get_api_request(self, url: str) -> requests.Response:
        """
        Make a GET request to the specified URL with the authorization header.
        
        :param url: URL to make the request to
        :return: Response object
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._authorization_token}"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response