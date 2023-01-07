import sys
from spotify_client import SpotifyClient
import os

save_path = r"/Users/qaboahene/Desktop/Personal/Themify/spotify_themes_themify/data/raw"
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

    # Read the number of days from the command line
    num_days = input("Enter the number of days: ")

    # Convert the num_days input to an integer
    try:
        num_days = int(num_days)
    except ValueError:
        print("Invalid input: num_days must be an integer.")
        sys.exit(1)

    # Create an instance of the SpotifyClient class
    client = SpotifyClient(authorization_token, user_id)

    # Get the tracks played by the user in the last n days
    df = client.get_recently_played_tracks(num_days)

    # Save the DataFrame to a specific folder on the user's laptop
    save_path = input("Enter the path to save the DataFrame: ")
    df.to_csv(os.path.join(save_path, "tracks.csv"), index=False)

    # Print a success message
    print("The DataFrame has been saved to the specified path.")

if __name__ == "__main__":
    main()

