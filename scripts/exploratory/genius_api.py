import csv
import requests

class SongScraper:
    def __init__(self, artist_name:str, song_name:str,access_token:str):
        self.artist_name = artist_name
        self.song_name =song_name
        self.access_token = access_token
        self.base_url = "https://api.genius.com"
        self.song_id = self.get_song_id()
        
    def get_song_id(self) -> int:
        """
        Function to get the song id from the Genius API
        """
        search_url = self.base_url + "/search"
        data = {'q': self.artist_name + " " + self.song_name}
        headers = {'Authorization': f"Bearer {self.access_token}"}
        response = requests.get(search_url, params=data, headers=headers)
        json_response = response.json()
        if response.status_code !=200:
            raise ValueError(f"Failed to fetch song id: {json_response['meta']['message']}")
        return json_response['response']['hits'][0]['result']['id']
    
    def get_lyrics(self)->str:
        """
        function to get the lyrics for the song
        """
        song_url = self.base_url + f"/songs/{self.song_id}"
        headers = {'Authorization': f"Bearer {self.access_token}"}
        response = requests.get(song_url, headers=headers)
        json_response = response.json()
        if response.status_code !=200:
            raise ValueError(f"Failed to fetch lyrics for the song: {json_response['meta']['message']}")
        return json_response['response']['song']['lyrics']['text']
        
    def save_lyrics(self):
        """
        function to save the lyrics to a csv file
        """
        try:
            song_lyrics = self.get_lyrics()
            with open('lyrics.csv', mode='w', newline='') as file:
                fieldnames = ['artist_name', 'song_name', 'lyrics']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'artist_name': self.artist_name, 'song_name': self.song_name,'lyrics': song_lyrics})
            print(f"Lyrics saved to 'lyrics.csv' successfully")
        except Exception as e:
            print(f"Error Occured while saving the lyrics, {e}")

            
