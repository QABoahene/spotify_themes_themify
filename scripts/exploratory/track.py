class Track:
    """
    Represents a piece of music.
    """

    def __init__(self, name: str, artist: str, album_type: str, release_date: str, album_name: str) -> None:
        """
        :param name: the track name
        :param artist: the artist who created the track
        :param album_type: album type
        :param release_date: release date of the track
        :param album_name: name of the album
        """
        self.name = name
        self.artist = artist
        self.album_name = album_name
        self.album_type = album_type
        self.release_date = release_date

    def create_spotify_uri(self) -> str:
        """ Create a Spotify URI for the track """
        return f"spotify:track:{self.id}"

    def __str__(self) -> str:
        """ Return a human-readable string representation of the track """
        return f"{self.name} by {self.artist}"