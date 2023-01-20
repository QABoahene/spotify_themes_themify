import pandas as pd
import lyricsgenius
from tqdm import tqdm

# Temporary global variables
access_token = "<YOUR_GENIUS_API_ACCESS_TOKEN>"
csv_file = "sample_data.csv"
artist_column = "artist"
song_column = "song_title"

class SongLyrics():
    # constructor for the class
    def __init__(self, access_token, csv_file):
        self.access_token = access_token
        self.genius = lyricsgenius.Genius(access_token)
        self.df = pd.read_csv(csv_file)
        self.not_found = []

    # method to get lyrics and add them to the csv file
    def get_lyrics(self, artist_column, song_column):
        self.df['song_lyrics'] = None
        for i, row in tqdm(self.df.iterrows(), total=len(self.df)):
            try:
                song = self.genius.search_song(row[song_column], row[artist_column])
                lyrics =song.lyrics
                self.df.at[i, 'song_lyrics'] = lyrics
            except:
                self.not_found.append(f'{row[artist_column]} - {row[song_column]}')
                self.df.at[i, 'song_lyrics'] = None
                continue
        self.df['song_lyrics'] = self.df['song_lyrics'].str.replace('\n', ' ')
        return self.df
    
    # method to generate report
    def generate_report(self):
        found = len(self.df) - len(self.not_found)
        print(f'Lyrics found for {found} songs')
        print(f'Lyrics not found for {len(self.not_found)} songs')
        if self.not_found:
            print("\nSongs for which lyrics were not found:")
            for song in self.not_found:
                print(song)


#Test code
song_lyrics = SongLyrics(access_token, csv_file)
df = song_lyrics.get_lyrics(artist_column, song_column)
song_lyrics.generate_report()

df.to_csv('output.csv', index = False)