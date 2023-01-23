import os
import sys

from genius_api import SongLyrics

def main():
    # Introducing the user to what is going to be done
    print("You're about to download lyrics for your Spotify listening history with Genius API")

    # Read the authorization token from an environment variable
    access_token = os.getenv("GENIUS_ACCESS_TOKEN")
    if access_token is None:
        print("Error: GENIUS_ACCESS_TOKEN environment variable not set.")
        sys.exit(1)
    
    file_path = input("Enter the path of the listening history file: ")
    artist_column = "artist"
    song_column = "song_title"

    song_lyrics = SongLyrics(access_token, file_path)
    df = song_lyrics.get_lyrics(artist_column, song_column)
    song_lyrics.generate_report()
    
    save_path = input("Enter the path to save the DataFrame: ")

    df.to_csv(os.path.join(save_path, "tracks_with_lyrics.csv"), index=False)

    # Print a success message
    print("The DataFrame has been saved to the specified path.")

if __name__ == "__main__":
    main()