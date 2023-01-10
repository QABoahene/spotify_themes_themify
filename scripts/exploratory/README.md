# Exploratory Scripts

This directory holds python scripts with experimental code for data cleaning and preprocessing, and other processes. 


## The Track class
This code defines a Python class named "Track" that represents a piece of music. The class has several attributes (name, artist, album_name, album_type, release_date) that store information about the track, such as its name, artist, album name, album type and release date respectively.

The class has an __init__ method, which is the constructor of the class and is called when a new instance of the class is created. This method accepts five parameters, namely name, artist, album_type, release_date, album_name and assigns the passed values to the corresponding attributes of the class.

The class also has a method create_spotify_uri which creates a Spotify URI for the track, but here it's missing the track id, so it will not create a URI and can raise an error.

Finally, the class has a method __str__, which is a special method that is called when the str() or print() function is called on an instance of the class. This method returns a human-readable string representation of the track, which is the track name and artist in this case.


## The SpotifyClient class
The code defines a Python class named "SpotifyClient" that performs various operations using the Spotify API. The class has an attribute _authorization_token and _user_id that store an API token and a user ID respectively, which will be used to authenticate requests to the Spotify API.

The class has a constructor __init__ method which takes in 2 parameters, authorization_token and user_id which will initialize the instance variables _authorization_token and _user_id when a new instance of the class is created.

The class has a method named get_last_played_tracks, which takes in a single parameter limit (default value is 10) and returns a list of last played tracks, by sending GET request to the Spotify API with the limit parameter, then process the response to extract the required information and creating a list of Track instances containing the extracted information.

The class also has a method named get_tracks_dataframe, which takes in a single parameter limit (default value is 10), it gets the last n tracks played by a user by calling get_last_played_tracks method and converts it into a Pandas DataFrame, containing the track name, artist name, album name, album type, and release date.

Lastly, the class has a method named _place_get_api_request which is a private method that sends a GET request to the specified URL with the authorization header and returns the response object. It also raise for error if it's not okay.


## The listeninghistory.py file
It defines a function main() that creates an instance of the SpotifyClient class from the spotify_client module, which allows the user to interact with the Spotify API.

The function starts by printing a welcome message, it then reads the Spotify API token and user ID from environment variables SPOTIFY_AUTH_TOKEN and SPOTIFY_USER_ID respectively, if either of these variables are not set, the function will print an error message and exit.

The function then asks the user to specify the number of tracks they want to retrieve using the command line, with a maximum limit of 50.

An instance of the SpotifyClient class is then created using the API token and user ID read from the environment variables, and the get_last_played_tracks method is called on this instance, passing in the number of tracks specified by the user. The function then prints the last played tracks to the command line.

Then, the function calls the get_tracks_dataframe method on the SpotifyClient instance, to convert the list of tracks into a Pandas DataFrame.
It then asks the user to specify the path where this DataFrame should be saved to, and finally saves the DataFrame to a CSV file at the specified path and prints a success message.

When the script is run, the main() function will be executed.