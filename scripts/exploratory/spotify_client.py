import requests
from track import Track
import pandas as pd

class SpotifyClient:
    """SpotifyClient performs operations using the Spotify API."""

    def __init__(self, authorization_token, user_id):
        """
        :param authorization_token (str): Spotify API token
        :param user_id (str): Spotify user id
        """
        self._authorization_token = authorization_token
        self._user_id = user_id

    def get_last_played_tracks(self, limit=10):
        """Get the last n tracks played by a user

        :param limit (int): Number of tracks to get. Should be <= 50
        :return tracks (list of Track): List of last played tracks
        """
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for
                  track in response_json["items"]]
        return tracks

    def get_tracks_dataframe(self, limit=10):
        """Get the last n tracks played by a user as a DataFrame

        :param limit (int): Number of tracks to get. Should be <= 50
        :return df (DataFrame): DataFrame containing track name, track ID, and artist name
        """
        # Get the list of tracks
        tracks = self.get_last_played_tracks(limit)

        # Create a list of dictionaries containing the track data
        track_data = [{"name": track.name, "id": track.id, "artist": track.artist} for track in tracks]

        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(track_data)

        return df

    def _place_get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._authorization_token}"
            }
        )
        return response
