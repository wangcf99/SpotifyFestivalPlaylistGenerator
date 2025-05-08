from spotify_client import SpotifyClientWrapper

sp = SpotifyClientWrapper()

artist_input = input("Enter names of interested artists, separated by only a comma:")
interested_artists = artist_input.split(",")

tracks = []

for artist in interested_artists:
    tracks.extend(sp.get_artist_top_tracks(artist))

song_uris = []
for song in tracks:
    song_uris.append(song['uri'])


playlist_name = input("What do u wanna name this playlist:")

playlist = sp.create_playlist(playlist_name)
playlist_id = playlist['id']

sp.add_tracks_to_playlist(playlist_id, song_uris)
sp.update_description_to_playlist(playlist_id, description="Made by https://github.com/wangcf99/SpotifyFestivalPlaylistGenerator/tree/main")