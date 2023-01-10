import csv
import requests

class SongScraper:
    def __init__(self, artist_name, song_name):
        self.artist_name = artist_name
        self.song_name = song_name
        self.access_token = "YOUR_ACCESS_TOKEN"
        self.base_url = "https://api.genius.com"
        self.song_id = self.get_song_id()
        
    def get_song_id(self):
        search_url = self.base_url + "/search"
        data = {'q': self.artist_name + " " + self.song_name}
        headers = {'Authorization': "Bearer " + self.access_token}
        response = requests.get(search_url, params=data, headers=headers)
        json_response = response.json()
        return json_response['response']['hits'][0]['result']['id']
    
    def get_lyrics(self):
        song_url = self.base_url + "/songs/{}".format(self.song_id)
        headers = {'Authorization': "Bearer " + self.access_token}
        response = requests.get(song_url, headers=headers)
        json_response = response.json()
        return json_response['response']['song']['lyrics']['text']
        
    def save_lyrics(self):
        song_lyrics = self.get_lyrics()
        with open('lyrics.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['artist_name', 'song_name', 'lyrics'])
            writer.writerow([self.artist_name, self.song_name, song_lyrics])
            
