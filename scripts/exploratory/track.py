class Track:
    """
    A class representing a piece of music.
    """

    def __init__(self, name: str, id: int, artist: str) -> None:
        """
        Initialize a Track instance.

        :param name: The name of the track.
        :param id: The Spotify track id.
        :param artist: The artist who created the track.
        """
        self.name = name
        self.id = id
        self.artist = artist

    def create_spotify_uri(self) -> str:
        """
        Create and return a Spotify URI for the track.
        """
        return f"spotify:track:{self.id}"

    def __str__(self) -> str:
        """
        Return a string representation of the track.
        """
        return f"{self.name} by {self.artist}"
