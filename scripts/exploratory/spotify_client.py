import datetime
import pandas as pd
import requests
from typing import Optional, Tuple

class SpotifyClient:
    def __init__(self, authorization_token: str, user_id: str):
        """
        :param authorization_token: The Spotify API authorization token.
        :param user_id: The Spotify user ID.
        """
        self._authorization_token = authorization_token
        self._user_id = user_id

    def _place_get_api_request(self, url: str, params: Optional[dict] = None) -> requests.Response:
        """
        Place a GET request to the specified URL using the Spotify API.

        :param url: The URL to which to send the request.
        :param params: The query parameters for the request (optional).
        :return: The response from the server.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._authorization_token}"
        }
        return requests.get(url, params=params, headers=headers)

    def _get_time_range(self, num_days: int) -> Tuple[int, int]:
        """
        Get the start and end timestamps for the time range (i.e., the last n days).

        :param num_days: The number of days for which to retrieve the tracks.
        :return: A tuple containing the start and end timestamps.
        """
        now = datetime.datetime.now()
        start_timestamp = int((now - datetime.timedelta(days=num_days)).timestamp())
        end_timestamp = int(now.timestamp())
        return start_timestamp, end_timestamp

    def get_recently_played_tracks(self, num_days: int) -> pd.DataFrame:
        """
        Get the tracks played by the user in the last n days.

        :param num_days: The number of days for which to retrieve the tracks.
        :return: A DataFrame containing the track information.
        """
        # Get the start and end timestamps for the time range
        start_timestamp, end_timestamp = self._get_time_range(num_days)

        # Set the API endpoint URL
        endpoint_url = "https://api.spotify.com/v1/me/player/recently-played"

        # Set the query parameters for the request
        query_params = {
            "before": end_timestamp,
            "after": start_timestamp,
        }

        # Send the GET request
        response = self._place_get_api_request(endpoint_url, params=query_params)

        # Check the status code of the response
        if response.status_code == 200:
            # Parse the response JSON
            response_json = response.json()

            # Access the tracks data from the response
            tracks = response_json["items"]

            # Create a list of track dictionaries
            track_list = []
            for track in tracks:
                track_info = {
                    "track": track["track"]["name"],
                    "artist": track["track"]["artists"][0]["name"]
                }
                track_list.append(track_info)

            # Create a DataFrame from the list of tracks
            df = pd.DataFrame(track_list, columns=["track", "artist"])

            # Return the DataFrame
            return df
        else:
            # Return an empty DataFrame if the request was unsuccessful
            return pd.DataFrame()

