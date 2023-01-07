# Exploratory Scripts

This directory holds python scripts with experimental code for data cleaning and preprocessing, and other processes. 


## The Track class
This code defines a Python class called Track which represents a piece of music. The Track class has three attributes: name, id, and artist, which represent the name of the track, the Spotify track id, and the artist who created the track, respectively.

The Track class has two methods: create_spotify_uri and ___str___. The create_spotify_uri method returns a Spotify URI (Uniform Resource Identifier) for the track, which is a string in the format spotify:track: _id_, where _id_ is the Spotify track id of the track. The ___str___ method returns a string representation of the track, which is the name of the track followed by "by" and the artist who created the track.

The ___init___ method is a special method in Python classes that is called when an instance of the class is created. It is used to initialize the attributes of the instance. The ___init___ method for the Track class takes three arguments: name, id, and artist, which are used to initialize the name, id, and artist attributes of the Track instance, respectively. The ___init___ method has a return type of None, which means it does not return anything.

