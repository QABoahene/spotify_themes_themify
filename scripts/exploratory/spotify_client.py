from track import Track
from typing import List
import pandas as pd
import requests


class SpotifyClient:
    """SpotifyClient performs operations using the Spotify API."""

    def __init__(self, authorization_token: str, user_id: str) -> None:
        """
        :param authorization_token: Spotify API token
        :param user_id: Spotify user id
        """
        self._authorization_token = authorization_token
        self._user_id = user_id

    def get_last_played_tracks(self, limit: int = 10) -> List[Track]:
        """Get the last n tracks played by a user.

        :param limit: Number of tracks to get. Should be <= 50
        :return: List of last played tracks
        """
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"])
                  for track in response_json["items"]]
        return tracks

    def get_tracks_dataframe(self, limit: int = 10) -> pd.DataFrame:
        """Get the last n tracks played by a user as a DataFrame.

        :param limit: Number of tracks to get. Should be <= 50
        :return: DataFrame containing track name, track ID, and artist name
        """
        # Get the list of tracks
        tracks = self.get_last_played_tracks(limit)

        # Create a list of dictionaries containing the track data
        track_data = [{"name": track.name, "id": track.id, "artist": track.artist} for track in tracks]

        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(track_data)

        return df

    def _place_get_api_request(self, url: str) -> requests.Response:
        """Make a GET request to the specified URL with the authorization header.

        :param url: URL to make the request to
        :return: Response object
        """
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._authorization_token}"
            }
        )
        return response
