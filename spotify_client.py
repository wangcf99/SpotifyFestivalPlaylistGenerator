import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import List

class SpotifyClientWrapper:
    scope = "user-library-read playlist-modify-public"

    def __init__(self):
        self.spotify_client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))
        self.current_user = self.spotify_client.current_user()
    
    def get_artist_top_tracks(self, artist_name: str) -> List[str]:
        artist = self.spotify_client.search(q=f"artist:{artist_name}", type='artist', limit=1)
        artist_uri = artist['artists']['items'][0]['uri'].split(":")[-1]
        return self.spotify_client.artist_top_tracks(artist_id=artist_uri)['tracks']
    
    def create_playlist(self, playlist_name: str):
        return self.spotify_client.user_playlist_create(user=self.current_user['id'], name=playlist_name)
    
    def add_tracks_to_playlist(self, playlist_id: str, tracks: List[str]):
        page_size = 50
        num_tracks = len(tracks)
        start_index = 0

        while start_index < num_tracks:
            end_index = start_index + page_size
            if end_index > num_tracks:
                end_index = num_tracks
            
            paginated_tracks = tracks[start_index:end_index]
            self.spotify_client.playlist_add_items(playlist_id=playlist_id, items=paginated_tracks)
            start_index += page_size
    
    def update_description_to_playlist(self, playlist_id: str, description: str):
        self.spotify_client.playlist_change_details(playlist_id, description=description)