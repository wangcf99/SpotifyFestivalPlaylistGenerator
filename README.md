# SpotifyFestivalPlaylistGenerator
## WHAT
You ever plan to go to a festival and then create your schedule and then realize there are so many artists, and that making a playlist is too much work?
This script is supposed to handle that, just input a list of artists you are interested in seeing at a festival, and then it generates a playlist. This 
script works by matching the artist names, and then grabbing the top 10 most popular songs from that artist, then adding it to the playlist. 

## HOW TO USE:
1. Create a Spotify Developer Account 
2. Get your account's client ID and client secret
3. Set env variables SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, to the stuff u found in number 2
4. Set SPOTIPY_REDIRECT_URI to local host
5. Execute main.py 


## ISSUES
1. Sometimes the artist match goes wrong, i.e. when I inputted "Rezz" for some reason it matched to somebody named "The Artist Ren", so you may have to manually check to see if things are right.
