from spotify_client import SpotifyClient
import os
import sys

from spotify_client import SpotifyClient

def main():
    # Print a welcome message
    print("Welcome to the Themify testing tool!")

    # Read the authorization token from an environment variable
    authorization_token = os.getenv("SPOTIFY_AUTH_TOKEN")
    if authorization_token is None:
        print("Error: SPOTIFY_AUTH_TOKEN environment variable not set.")
        sys.exit(1)

    # Read the user ID from an environment variable
    user_id = os.getenv("SPOTIFY_USER_ID")
    if user_id is None:
        print("Error: SPOTIFY_USER_ID environment variable not set.")
        sys.exit(1)

    # Read the number of songs from the command line
    num_tracks = int(input("How many tracks would you like to show? Remember, limit is 50 "))

    # Create an instance of the SpotifyClient class
    client = SpotifyClient(authorization_token, user_id)

    # Get the last played tracks and print them
    tracks = client.get_last_played_tracks(num_tracks)
    print(f"\nHere are the last {num_tracks} tracks you listened to on Spotify:")
    for index, track in enumerate(tracks):
        print(f"{index+1}- {track}")

    # Convert the list of tracks to a DataFrame and save it to a CSV file
    df = client.get_tracks_dataframe(num_tracks)
    save_path = input("Enter the path to save the DataFrame: ")
    df.to_csv(os.path.join(save_path, "tracks.csv"), index=False)

    # Print a success message
    print("The DataFrame has been saved to the specified path.")

if __name__ == "__main__":
    main()